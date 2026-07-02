#!/usr/bin/env python3
"""
Generate new X2D/0.4mm/*.bbsflmt bundles for filament types that TINMORRY's
old per-printer profile repo (reference-old-repo/) has but this repo's X2D
folder doesn't yet -- without touching any existing .bbsflmt file.

Why this approach (and not a from-scratch flatten):
Old-repo profiles are tiny deltas ("inherits": "Generic PC @BBL P1S", plus a
handful of overridden keys) against Bambu Studio's built-in system profiles
for OTHER printers. We don't have X2D's own system filament profiles here,
so we can't correctly re-derive X2D-specific machine defaults (nozzle temp
ceiling, chamber behavior, per-extruder-variant defaults, etc.) from first
principles.

Instead, each new bundle is built by taking an existing X2D bundle that's
already been validated for this machine (closest material match) as the
structural/machine-parameter template, and layering the old-repo profile's
material-specific tuning (flow ratio, print/plate temps, fan speeds, max
volumetric speed, retraction) on top of it. Where the old-repo delta says
"nil" (no override) or doesn't mention a field, the template's own
X2D-validated value is kept rather than guessed.

Run:
    python3 scripts/convert_old_repo_to_x2d.py            # write new bundles
    python3 scripts/convert_old_repo_to_x2d.py --dry-run   # preview only

Re-running is safe for iterating on the mapping table below, but it WILL
overwrite bundles this script previously generated (identified by being in
CONVERSIONS). It never touches a .bbsflmt that isn't listed as an "output".
"""
import argparse
import json
import time
import zipfile
import zlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OLD_REPO_DIR = REPO_ROOT / "reference-old-repo"
X2D_DIR = REPO_ROOT / "X2D" / "0.4mm"

# Keys that describe lineage/identity rather than material behavior -- never
# copied from the old-repo delta onto the new bundle.
SKIP_KEYS = {
    "name", "filament_settings_id", "from", "inherits", "version",
    "filament_extruder_variant", "compatible_printers",
    "compatible_printers_condition", "compatible_prints",
    "compatible_prints_condition", "filament_id", "filament_vendor",
    "setting_id", "instantiation",
}

BUNDLE_ID_PREFIX = "3412907432"  # matches the account/store id used across this repo's other bundles

# output_name          filament_type   template bundle (X2D)      source old-repo delta file
CONVERSIONS = [
    ("TINMORRY ASA CF", "ASA-CF", "TINMORRY ASA basic",
     "ASA-CF(H2S-Bambu-TINMORRY).json"),
    ("TINMORRY PET CF", "PET-CF", "TINMORRY PETG CF",
     "PET CF   GF(H2S-Bambu-TINMORRY).json"),
    ("TINMORRY PA-CF", "PA-CF", "TINMORRY PETG CF",
     "PA-CF(P1S.X1C-Bambu-TINMORRY).json"),
    ("TINMORRY PAHT-CF", "PAHT-CF", "TINMORRY PETG CF",
     "PAHT-CF(P1S.X1C-Bambu-TINMORRY).json"),
    ("TINMORRY PLA CF", "PLA-CF", "TINMORRY PLA matte",
     "PLA-CF(H2D-Bambu-TINMORRY).json"),
    ("TINMORRY PLA Galaxy", "PLA", "TINMORRY PLA matte",
     "Galaxy PLA(P2S-Bambu-TINMORRY).json"),
    ("TINMORRY PC GF", "PC", "TINMORRY ABS Pro",
     "PC-GF(X1C-Bambu-TINMORRY).json"),
    ("TINMORRY TPU GF", "TPU", "TINMORRY TPU 95A",
     "TPU-GF(P1S,X1C-Bambu-TINMORRY).json"),
    ("TINMORRY PETG HS", "PETG", "TINMORRY PETG ECO",
     "PETG-HS(X1C-Bambu-TINMORRY).json"),
    ("TINMORRY PLA Silk", "PLA", "TINMORRY PLA matte",
     "Silk PLA(H2S-Bambu-TINMORRY).json"),
]

PRINTER_SUFFIX = "@Bambu Lab X2D 0.4 nozzle"


def load_template(bundle_name: str):
    """Load a template bundle's X2D profile.

    Some templates (e.g. TPU 95A) are dual-printer bundles that also cover
    P2S, with one filament_path per compatible printer -- pick the one
    whose filename mentions X2D rather than assuming index 0.
    """
    path = X2D_DIR / f"{bundle_name}.bbsflmt"
    with zipfile.ZipFile(path) as z:
        bundle_structure = json.loads(z.read("bundle_structure.json"))
        candidates = bundle_structure["filament_vendor"][0]["filament_path"]
        profile_path = next(p for p in candidates if "X2D" in p)
        profile = json.loads(z.read(profile_path))
    return bundle_structure, profile


def merge_profile(template: dict, delta: dict) -> dict:
    result = dict(template)
    for key, delta_val in delta.items():
        if key in SKIP_KEYS:
            continue
        template_val = template.get(key)
        if not isinstance(delta_val, list):
            # Non-list override (rare) -- take it verbatim.
            result[key] = delta_val
            continue
        if isinstance(template_val, list) and len(template_val) > 1:
            variant_count = len(template_val)
            new_val = list(template_val)
            if len(delta_val) >= 1 and delta_val[0] not in (None, "nil"):
                new_val[0] = delta_val[0]
            if len(delta_val) >= 2:
                if delta_val[1] not in (None, "nil"):
                    new_val[1] = delta_val[1]
            elif delta_val and delta_val[0] not in (None, "nil"):
                # Old-repo gave a single uniform value -- apply to all variants.
                new_val = [delta_val[0]] * variant_count
            # Bundles in this repo consistently mirror "Direct Drive High
            # Flow" (index 1) into any Bowden variants (index >= 2).
            for i in range(2, variant_count):
                new_val[i] = new_val[1]
            result[key] = new_val
        else:
            result[key] = delta_val
    return result


def make_filament_id(output_name: str) -> str:
    return f"Pf{zlib.crc32(output_name.encode()) % 900000 + 100000}"


def build_bundle(output_name: str, filament_type: str, template_bundle: str,
                  source_file: str, dry_run: bool):
    bundle_structure, template_profile = load_template(template_bundle)
    delta = json.loads((OLD_REPO_DIR / source_file).read_text())

    profile = merge_profile(template_profile, delta)
    profile_name = f"{output_name} {PRINTER_SUFFIX}"
    profile["name"] = profile_name
    profile["filament_settings_id"] = [output_name]
    profile["filament_id"] = make_filament_id(output_name)
    profile["filament_type"] = [filament_type]
    profile["filament_vendor"] = ["TINMORRY"]
    # compatible_printers / compatible_printers_condition / inherits / from
    # are intentionally left as copied from the template (X2D-specific,
    # already correct).

    profile_path = f"TINMORRY/{profile_name}.json"
    new_bundle_structure = {
        "bundle_id": f"{BUNDLE_ID_PREFIX}_{output_name}_{int(time.time())}",
        "bundle_type": "filament config bundle",
        "filament_name": output_name,
        "filament_vendor": [
            {"filament_path": [profile_path], "vendor": "TINMORRY"}
        ],
        "version": bundle_structure["version"],
    }

    out_path = X2D_DIR / f"{output_name}.bbsflmt"
    print(f"{'[dry-run] ' if dry_run else ''}{out_path.relative_to(REPO_ROOT)}"
          f"  (template={template_bundle!r}, source={source_file!r}, type={filament_type})")
    if dry_run:
        return

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("bundle_structure.json", json.dumps(new_bundle_structure, indent=4))
        z.writestr(profile_path, json.dumps(profile, indent=4))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="preview without writing files")
    args = parser.parse_args()

    for output_name, filament_type, template_bundle, source_file in CONVERSIONS:
        build_bundle(output_name, filament_type, template_bundle, source_file, args.dry_run)


if __name__ == "__main__":
    main()
