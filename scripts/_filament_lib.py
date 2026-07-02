"""
Shared helpers for scripts/find_missing_filaments.py and
scripts/convert_old_repo_to_printer.py.

Central piece: a machine-compatibility tier system so the converter never
fabricates a filament/printer pairing it has no evidence for. See
CLAUDE.md "Machine compatibility gating" for the policy this encodes.
"""
import json
import re
import time
import zipfile
import zlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OLD_REPO_DIR = REPO_ROOT / "reference-old-repo"

# Every printer folder in this repo, its exact compatible_printers string,
# and the @BBL machine code(s) old-repo deltas use to tag that same
# physical printer (see reference-old-repo/*.json "inherits" fields).
# A1 (full-size) and P1P/P1S/X1C/X1E system profiles exist in the old repo
# but have no folder in this repo, so they're not registered as targets --
# only used as fallback source data for base-tier materials.
PRINTERS = {
    "A1mini": {"dir": "A1mini", "compatible": "Bambu Lab A1 mini 0.4 nozzle", "bbl_codes": {"a1m"}},
    "A2L": {"dir": "A2L", "compatible": "Bambu Lab A2L 0.4 nozzle", "bbl_codes": set()},
    "H2C": {"dir": "H2C", "compatible": "Bambu Lab H2C 0.4 nozzle", "bbl_codes": {"h2c"}},
    "H2D": {"dir": "H2D", "compatible": "Bambu Lab H2D 0.4 nozzle", "bbl_codes": {"h2d"}},
    "H2S": {"dir": "H2S", "compatible": "Bambu Lab H2S 0.4 nozzle", "bbl_codes": {"h2s"}},
    "P2S": {"dir": "P2S", "compatible": "Bambu Lab P2S 0.4 nozzle", "bbl_codes": {"p2s"}},
    "X2D": {"dir": "X2D/0.4mm", "compatible": "Bambu Lab X2D 0.4 nozzle", "bbl_codes": {"x2d"}},
}

# Materials that print fine on any Bambu machine regardless of enclosure --
# includes fiber-reinforced PETG/PLA/PET variants, which Bambu Studio itself
# ships "Generic ...-CF" system profiles for on open-frame printers (A1).
TIER_BASE = {"PLA", "PETG", "TPU", "PLA-CF", "PETG-CF", "PET-CF"}

# Warp-prone / fume-relevant materials that Bambu recommends an enclosure
# for. Only generated for a printer if (a) the old repo has a machine-coded
# ("@BBL <code>") delta for THAT printer, or (b) the printer already ships
# an engineering-tier bundle in this repo, proving real hardware capability.
TIER_ENGINEERING_MED = {"ABS", "ASA", "ASA-CF", "PC"}

# High-temperature engineering materials (nylon-based) that need a hardened,
# high-limit hotend and usually a heated chamber. Only generated for a
# printer with DIRECT machine-coded old-repo evidence -- tier-proof via
# other engineering materials is not considered sufficient.
TIER_ENGINEERING_HIGH = {"PA", "PA-CF", "PAHT-CF"}


def tier_of(filament_type: str) -> str:
    if filament_type in TIER_ENGINEERING_HIGH:
        return "engineering_high"
    if filament_type in TIER_ENGINEERING_MED:
        return "engineering_med"
    return "base"


# Polymer families for TEMPLATE SELECTION only (separate from the coarser
# compatibility tiers above). Tier answers "does this printer support the
# heat/enclosure this needs"; family answers "whose temperature/retraction
# profile is close enough to borrow machine defaults from" -- e.g. within
# TIER_BASE, PLA/PETG/TPU are not interchangeable templates even though
# they're all fine on an open-frame printer.
POLYMER_FAMILY = {
    "PLA": "PLA", "PLA-CF": "PLA",
    "PETG": "PETG", "PETG-CF": "PETG", "PET-CF": "PETG",
    "TPU": "TPU",
    "ABS": "ABS-ASA-PC", "ASA": "ABS-ASA-PC", "ASA-CF": "ABS-ASA-PC", "PC": "ABS-ASA-PC",
    "PA": "PA", "PA-CF": "PA", "PAHT-CF": "PA",
}


def family_of(filament_type: str) -> str:
    return POLYMER_FAMILY.get(filament_type, filament_type)


PRINTER_TOKENS = {
    "a1", "a1m", "a1mini", "a2l", "p1p", "p1s", "p2s", "x1", "x1c", "x1e",
    "h2c", "h2d", "h2s", "x2d", "bbl", "bambu", "tinmorry", "nozzle", "0.4",
}
NOISE_WORDS = {"generic", "bambu"}


# A handful of old-repo filenames glue the material and grade together with
# no separator (e.g. "TPU95A"), which would otherwise tokenize as one blob
# that never matches the "TPU" + "95A" tokens used everywhere else.
GLUED_TOKEN_FIXES = {"tpu95a": "tpu 95a"}


def normalize(text: str, drop_noise: bool = True) -> set:
    text = text.lower()
    for glued, fixed in GLUED_TOKEN_FIXES.items():
        text = text.replace(glued, fixed)
    tokens = re.findall(r"[a-z0-9]+", text)
    stop = PRINTER_TOKENS | (NOISE_WORDS if drop_noise else set())
    return {t for t in tokens if t not in stop}


# Substrings checked against the lowercased "inherits" string (the part
# before "@"), most specific first, to assign a canonical filament_type.
INHERITS_BASE_MATERIAL = [
    ("asa-cf", "ASA-CF"),
    ("petg-cf", "PETG-CF"),
    ("pla-cf", "PLA-CF"),
    ("pa-cf", "PA-CF"),
    ("pet-cf", "PET-CF"),
    ("abs", "ABS"),
    ("asa", "ASA"),
    ("petg", "PETG"),
    ("pla", "PLA"),
    ("pc", "PC"),
    ("tpu", "TPU"),
]

# reference-old-repo/PET-CF (X1 X1C P1S P1P).json has a typo'd
# "inherits": "Generic ABS" (its filename and content are unambiguously
# PET-CF) -- override rather than let the bad source label fabricate a
# bogus "ABS"-tier product out of what is actually a base-tier material.
FILE_BASE_MATERIAL_OVERRIDE = {
    "PET-CF (X1 X1C P1S P1P).json": "PET-CF",
}


def old_repo_entries():
    """Yield dicts describing every reference-old-repo/*.json delta."""
    for path in sorted(OLD_REPO_DIR.glob("*.json")):
        data = json.loads(path.read_text())
        inherits = data.get("inherits", "") or ""
        m = re.search(r"@BBL\s+([A-Za-z0-9]+)", inherits)
        bbl_code = m.group(1).lower() if m else None

        if path.name in FILE_BASE_MATERIAL_OVERRIDE:
            base_material = FILE_BASE_MATERIAL_OVERRIDE[path.name]
        else:
            lineage = inherits.split("@")[0].lower()
            base_material = next((mat for sub, mat in INHERITS_BASE_MATERIAL if sub in lineage), None)

        descriptor_part = re.sub(r"\(.*", "", path.stem)
        descriptor = normalize(descriptor_part) - normalize(base_material or "")
        yield {
            "file": path.name,
            "inherits": inherits,
            "bbl_code": bbl_code,
            "base_material": base_material,
            "descriptor": descriptor,
        }


def bundle_labels(printer_dir: str):
    """List (path, filament_name, token set) for a printer's existing bundles."""
    d = REPO_ROOT / printer_dir
    labels = []
    if not d.exists():
        return labels
    for path in sorted(d.glob("*.bbsflmt")):
        with zipfile.ZipFile(path) as z:
            bundle = json.loads(z.read("bundle_structure.json"))
        labels.append((path, bundle["filament_name"], normalize(bundle["filament_name"])))
    return labels


def printer_filament_types(printer_dir: str) -> set:
    """filament_type values already shipped for a printer (for the
    engineering-tier hardware-capability proof).

    Walks the zip's actual namelist rather than bundle_structure.json's
    declared filament_path -- a couple of bundles in this repo have
    non-ASCII characters (e.g. a full-width comma) that round-trip
    correctly as JSON text but don't byte-match the zip's stored (cp437)
    entry name, so looking them up by the declared path raises KeyError.
    """
    printer_code = printer_dir.split("/")[0]  # e.g. "H2D", "X2D"
    d = REPO_ROOT / printer_dir
    types = set()
    if not d.exists():
        return types
    for path in sorted(d.glob("*.bbsflmt")):
        with zipfile.ZipFile(path) as z:
            for name in z.namelist():
                if not name.endswith(".json") or name == "bundle_structure.json":
                    continue
                if printer_code not in name:
                    continue
                profile = json.loads(z.read(name))
                types.update(profile.get("filament_type", []))
    return types


def is_engineering_capable(printer_dir: str) -> bool:
    types = printer_filament_types(printer_dir)
    return bool(types & (TIER_ENGINEERING_MED | TIER_ENGINEERING_HIGH))


def classify_gap(base_material: str, bbl_code: str, printer_codes: set, engineering_capable: bool) -> str:
    """The compatibility-gating policy. See module docstring / CLAUDE.md."""
    tier = tier_of(base_material)
    direct = bool(bbl_code and bbl_code in printer_codes)
    if tier == "base":
        return "ALLOW (direct evidence)" if direct else "ALLOW (family evidence)"
    if tier == "engineering_med":
        if direct:
            return "ALLOW (direct evidence)"
        if engineering_capable:
            return "ALLOW (tier-proof)"
        return "SKIP (needs review: no enclosure evidence)"
    if tier == "engineering_high":
        if direct:
            return "ALLOW (direct evidence)"
        return "SKIP (needs review: high-temp material, no machine-specific evidence)"
    return "SKIP (unknown material)"


def find_gaps(printer_name: str):
    """Yield one dict per old-repo filament family missing from a printer.

    Each dict has: base_material, descriptor (token set), label, verdict
    (see classify_gap), and source (the chosen old-repo entry dict, biased
    towards a machine-coded delta for this printer when one exists).
    """
    info = PRINTERS[printer_name]
    existing_tokens = [tokens for _, _, tokens in bundle_labels(info["dir"])]
    engineering_capable = is_engineering_capable(info["dir"])

    groups = {}
    for entry in old_repo_entries():
        if entry["base_material"] is None:
            continue
        key = (entry["base_material"], frozenset(entry["descriptor"]))
        groups.setdefault(key, []).append(entry)

    for (base_material, descriptor), entries in sorted(groups.items(), key=lambda kv: (kv[0][0], sorted(kv[0][1]))):
        combined = normalize(base_material) | descriptor
        if any(combined <= tokens or tokens <= combined for tokens in existing_tokens):
            continue
        direct_sources = [e for e in entries if e["bbl_code"] in info["bbl_codes"]]
        source = direct_sources[0] if direct_sources else entries[0]
        verdict = classify_gap(base_material, source["bbl_code"], info["bbl_codes"], engineering_capable)
        yield {
            "base_material": base_material,
            "descriptor": descriptor,
            "label": f"{base_material} {' '.join(sorted(descriptor))}".strip(),
            "verdict": verdict,
            "source": source,
        }


# ---------------------------------------------------------------------------
# Bundle construction (used by convert_old_repo_to_printer.py)
# ---------------------------------------------------------------------------

# Materials whose hyphen is part of the actual product name, not a
# base-polymer + reinforcement suffix -- keep the hyphen in display names.
HYPHENATED_MATERIALS = {"PA-CF", "PAHT-CF", "PP-CF"}


def display_material(base_material: str) -> str:
    if base_material in HYPHENATED_MATERIALS:
        return base_material
    return base_material.replace("-", " ")


DESCRIPTOR_CASE_OVERRIDES = {
    "cf": "CF", "gf": "GF", "hs": "HS", "eco": "ECO", "pp": "PP", "pc": "PC",
}


def display_descriptor(descriptor: set) -> str:
    words = [DESCRIPTOR_CASE_OVERRIDES.get(w, w.capitalize()) for w in sorted(descriptor)]
    return " ".join(words)


def output_bundle_name(base_material: str, descriptor: set) -> str:
    parts = ["TINMORRY", display_material(base_material)]
    desc = display_descriptor(descriptor)
    if desc:
        parts.append(desc)
    return " ".join(parts)


# Repo-wide structural templates for materials with no in-printer or
# same-tier analog to copy machine parameters from. All point at this
# repo's X2D bundles since X2D has (as of this writing) the broadest
# material coverage and each of these was itself either an original
# TINMORRY export or already vetted when generated.
FALLBACK_TEMPLATE = {
    "ABS": ("X2D/0.4mm", "TINMORRY ABS Pro"),
    "ASA": ("X2D/0.4mm", "TINMORRY ASA basic"),
    "ASA-CF": ("X2D/0.4mm", "TINMORRY ASA CF"),
    "PC": ("X2D/0.4mm", "TINMORRY ABS Pro"),
    "PA-CF": ("X2D/0.4mm", "TINMORRY PA-CF"),
    "PAHT-CF": ("X2D/0.4mm", "TINMORRY PAHT-CF"),
    "PET-CF": ("X2D/0.4mm", "TINMORRY PET CF"),
    "PETG-CF": ("X2D/0.4mm", "TINMORRY PETG CF"),
    "PLA-CF": ("X2D/0.4mm", "TINMORRY PLA CF"),
    "PLA": ("X2D/0.4mm", "TINMORRY PLA matte"),
    "PETG": ("X2D/0.4mm", "TINMORRY PETG ECO"),
    "TPU": ("X2D/0.4mm", "TINMORRY TPU 95A"),
}


def choose_template(printer_dir: str, base_material: str, existing_labels=None):
    """Pick (template_printer_dir, template_bundle_name) for a gap.

    Priority: (1) an existing bundle in the SAME printer folder with the
    same filament_type -- best, real machine calibration for this exact
    printer; (2) an existing bundle in the same folder with the same
    POLYMER FAMILY (e.g. any PLA-ish bundle for a PLA-ish gap -- not just
    "some other base-tier material", which would wrongly offer up a TPU or
    PETG bundle's temperature profile as a PLA template); (3) the
    repo-wide fallback.

    IMPORTANT: pass `existing_labels` as a snapshot taken with
    bundle_labels() BEFORE a conversion run starts writing new bundles into
    this same folder. Without it this re-globs the directory live, which
    lets bundle N+1 in a batch template off bundle N that this same run
    just generated -- compounding approximation on approximation instead of
    everything tracing back to a real, originally-existing bundle.
    """
    family = family_of(base_material)
    labels = bundle_labels(printer_dir) if existing_labels is None else existing_labels
    for path, name, _ in labels:
        with zipfile.ZipFile(path) as z:
            for zname in z.namelist():
                if not zname.endswith(".json") or zname == "bundle_structure.json":
                    continue
                if printer_dir.split("/")[0] not in zname:
                    continue
                profile = json.loads(z.read(zname))
                if base_material in profile.get("filament_type", []):
                    return printer_dir, name
    for path, name, _ in labels:
        with zipfile.ZipFile(path) as z:
            for zname in z.namelist():
                if not zname.endswith(".json") or zname == "bundle_structure.json":
                    continue
                if printer_dir.split("/")[0] not in zname:
                    continue
                profile = json.loads(z.read(zname))
                if any(family_of(t) == family for t in profile.get("filament_type", [])):
                    return printer_dir, name
    return FALLBACK_TEMPLATE.get(base_material)


SKIP_KEYS = {
    "name", "filament_settings_id", "from", "inherits", "version",
    "filament_extruder_variant", "compatible_printers",
    "compatible_printers_condition", "compatible_prints",
    "compatible_prints_condition", "filament_id", "filament_vendor",
    "setting_id", "instantiation",
}

BUNDLE_ID_PREFIX = "3412907432"  # matches the account/store id used across this repo's other bundles


def load_bundle_profile(printer_dir: str, bundle_name: str):
    """Load one bundle's profile JSON for its own printer.

    Some bundles (e.g. TPU 95A) cover more than one printer with one
    filament_path per compatible printer -- select by filename rather than
    trusting index 0. Walks the zip's actual namelist rather than
    bundle_structure.json's declared path, since a couple of bundles have
    non-ASCII filenames that don't byte-match their cp437-stored zip entry.
    """
    printer_code = printer_dir.split("/")[0]
    path = REPO_ROOT / printer_dir / f"{bundle_name}.bbsflmt"
    with zipfile.ZipFile(path) as z:
        bundle_structure = json.loads(z.read("bundle_structure.json"))
        name = next(n for n in z.namelist() if n.endswith(".json") and n != "bundle_structure.json" and printer_code in n)
        profile = json.loads(z.read(name))
    return bundle_structure, profile


def merge_profile(template: dict, delta: dict) -> dict:
    """Layer an old-repo delta's material tuning onto a template profile.

    Per-extruder-variant fields (flow ratio, temps, etc.) apply the delta's
    [Direct Drive Standard, Direct Drive High Flow] pair onto the
    template's first two variant slots, leaving "nil"/missing values at the
    template's own validated default, then mirror the High Flow value into
    any further variants (Bowden Standard/High Flow) -- the convention
    every bundle in this repo already follows.
    """
    result = dict(template)
    for key, delta_val in delta.items():
        if key in SKIP_KEYS:
            continue
        template_val = template.get(key)
        if not isinstance(delta_val, list):
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
                new_val = [delta_val[0]] * variant_count
            for i in range(2, variant_count):
                new_val[i] = new_val[1]
            result[key] = new_val
        else:
            result[key] = delta_val
    return result


def make_filament_id(output_name: str, printer_dir: str) -> str:
    # Same product name (e.g. "TINMORRY PETG ECO") recurs across printer
    # folders as distinct bundles -- hash printer_dir in too, or they'd all
    # collide on the same filament_id and Studio could conflate them.
    return f"Pf{zlib.crc32(f'{printer_dir}:{output_name}'.encode()) % 900000 + 100000}"


def build_bundle(printer_dir: str, output_name: str, filament_type: str,
                  template_printer_dir: str, template_bundle: str, source_file: str):
    """Merge a template + old-repo delta into a new bundle dict pair, ready to write."""
    bundle_structure, template_profile = load_bundle_profile(template_printer_dir, template_bundle)
    delta = json.loads((OLD_REPO_DIR / source_file).read_text())

    compatible = next(p for p in PRINTERS.values() if p["dir"] == printer_dir)["compatible"]

    profile = merge_profile(template_profile, delta)
    profile_name = f"{output_name} @{compatible}"
    profile["name"] = profile_name
    profile["filament_settings_id"] = [output_name]
    profile["filament_id"] = make_filament_id(output_name, printer_dir)
    profile["filament_type"] = [filament_type]
    profile["filament_vendor"] = ["TINMORRY"]
    profile["compatible_printers"] = [compatible]

    profile_path = f"TINMORRY/{profile_name}.json"
    new_bundle_structure = {
        "bundle_id": f"{BUNDLE_ID_PREFIX}_{output_name}_{int(time.time())}",
        "bundle_type": "filament config bundle",
        "filament_name": output_name,
        "filament_vendor": [{"filament_path": [profile_path], "vendor": "TINMORRY"}],
        "version": bundle_structure["version"],
    }
    return new_bundle_structure, profile_path, profile
