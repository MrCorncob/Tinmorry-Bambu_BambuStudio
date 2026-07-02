#!/usr/bin/env python3
"""
Generate new *.bbsflmt bundles for filament types that TINMORRY's old
per-printer profile repo (reference-old-repo/) has but a given printer
folder in this repo doesn't yet -- without touching any existing .bbsflmt
file, and without ever inventing a filament/printer pairing we have no
compatibility evidence for.

Compatibility gating (see scripts/_filament_lib.py and CLAUDE.md):
  - Base materials (PLA, PETG, TPU, and CF-reinforced PLA/PETG/PET) are
    generated freely -- they print fine on any Bambu machine.
  - "Engineering" materials (ABS, ASA, ASA-CF, PC) are only generated for a
    printer if the old repo has a machine-specific delta for that exact
    printer, or the printer already ships another engineering-tier bundle
    in this repo (proving it has an enclosure/hardware for it).
  - High-temperature nylon materials (PA, PA-CF, PAHT-CF) are only
    generated with a machine-specific old-repo delta for that exact
    printer -- never inferred from another material's tier-proof.
  - Anything that doesn't clear its bar is skipped and left for manual
    review; run find_missing_filaments.py to see the full gap list
    including skips and why.

Each generated bundle takes its machine parameters (temps, per-extruder-
variant behavior) from the closest existing bundle for that SAME printer,
falling back to a same-tier bundle on that printer, then to a repo-wide
canonical template (see _filament_lib.FALLBACK_TEMPLATE) -- and layers the
old-repo delta's own material tuning (flow ratio, fan speed, plate temp,
max volumetric speed) on top.

Usage:
    python3 scripts/convert_old_repo_to_printer.py                   # all printers
    python3 scripts/convert_old_repo_to_printer.py --printer H2D     # one printer
    python3 scripts/convert_old_repo_to_printer.py --dry-run         # preview only
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _filament_lib import (  # noqa: E402
    PRINTERS, REPO_ROOT, bundle_labels, build_bundle, choose_template, find_gaps, output_bundle_name,
)


def convert_printer(printer_name: str, dry_run: bool):
    info = PRINTERS[printer_name]
    printer_dir = info["dir"]
    out_dir = REPO_ROOT / printer_dir
    skipped = []

    # Snapshot the ORIGINAL bundles before writing anything, so every gap
    # in this run templates off real, pre-existing bundles -- never off a
    # bundle this same run just generated a moment earlier (see
    # choose_template's docstring).
    existing_labels = bundle_labels(printer_dir)

    for gap in find_gaps(printer_name):
        if not gap["verdict"].startswith("ALLOW"):
            skipped.append(gap)
            continue

        template = choose_template(printer_dir, gap["base_material"], existing_labels)
        if template is None:
            print(f"  [no template available, skipping] {gap['label']}")
            continue
        template_printer_dir, template_bundle = template

        output_name = output_bundle_name(gap["base_material"], gap["descriptor"])
        out_path = out_dir / f"{output_name}.bbsflmt"

        print(f"{'[dry-run] ' if dry_run else ''}{out_path.relative_to(REPO_ROOT)}"
              f"  (verdict={gap['verdict']}, template={template_printer_dir}/{template_bundle!r},"
              f" source={gap['source']['file']!r})")
        if dry_run:
            continue

        bundle_structure, profile_path, profile = build_bundle(
            printer_dir, output_name, gap["base_material"],
            template_printer_dir, template_bundle, gap["source"]["file"],
        )
        with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("bundle_structure.json", json.dumps(bundle_structure, indent=4))
            z.writestr(profile_path, json.dumps(profile, indent=4))

    if skipped:
        print(f"  -- {len(skipped)} gap(s) skipped for {printer_name}, needs manual review:")
        for gap in skipped:
            print(f"       {gap['label']:24s} [{gap['verdict']}] <- {gap['source']['file']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--printer", choices=sorted(PRINTERS), help="limit to one printer")
    parser.add_argument("--dry-run", action="store_true", help="preview without writing files")
    args = parser.parse_args()

    for name in ([args.printer] if args.printer else sorted(PRINTERS)):
        print(f"\n=== {name} ===")
        convert_printer(name, args.dry_run)


if __name__ == "__main__":
    main()
