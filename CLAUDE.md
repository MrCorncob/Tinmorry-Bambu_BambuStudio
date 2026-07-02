# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Not a software project — a collection of Bambu Studio filament preset bundles (`.bbsflmt` files) for TINMORRY filaments, organized by printer model, plus a small Python toolchain that derives new bundles for printers/materials this repo is missing from an older, unbundled TINMORRY profile source. There is no build, lint, or test suite.

## Commands

```bash
# Report gaps: filament types in reference-old-repo/ with no bundle yet for a given printer,
# each labeled ALLOW or SKIP per the compatibility policy below
python3 scripts/find_missing_filaments.py                 # all printers
python3 scripts/find_missing_filaments.py --printer H2D   # one printer

# Generate new .bbsflmt bundles for the ALLOW-labeled gaps (never overwrites an existing bundle)
python3 scripts/convert_old_repo_to_printer.py --dry-run  # preview
python3 scripts/convert_old_repo_to_printer.py             # write
python3 scripts/convert_old_repo_to_printer.py --printer P2S

# Regenerate REFERENCES.md's inventory table from the bundles actually on disk
python3 scripts/gen_inventory_table.py               # print the table
python3 scripts/gen_inventory_table.py --check       # exit 1 if REFERENCES.md is stale
```

All three read from `reference-old-repo/` — a gitignored local clone of TINMORRY's older per-printer profile repo (https://github.com/TINMORRY/TINMORRY-filament-profile-for-Bambu-printers.git). Reclone it there before running any of them; it isn't tracked in this repo. Shared logic (printer registry, gating policy, old-repo parsing, template selection, bundle merging) lives in `scripts/_filament_lib.py`.

## Architecture

**Repo layout**: one top-level folder per printer model (`A1mini/`, `A2L/`, `H2C/`, `H2D/`, `H2S/`, `P2S/`, `X2D/0.4mm/`), each holding `.bbsflmt` files for that printer's compatible filaments.

**`.bbsflmt` format**: a zip archive containing `bundle_structure.json` (bundle id, filament name, Studio version, and a `filament_vendor[].filament_path[]` list mapping to the profile JSON(s) inside) plus one fully-flattened filament settings JSON per compatible printer under `TINMORRY/`. "Fully flattened" means every parameter (temps, cooling, flow, retraction, etc.) is a literal value — no `inherits` chain to resolve. Some bundles (e.g. TPU 95A, PETG GF/Marble/Metallic under `X2D/0.4mm/`) are dual-printer: `filament_path` has one entry for P2S and one for X2D — when reading these programmatically, select by filename substring (or printer code), don't assume index 0. A couple of bundles have non-ASCII filenames (a full-width comma, a backtick) that round-trip correctly as JSON text but don't byte-match the zip's cp437-stored entry name — walk `zipfile.namelist()` rather than looking up `bundle_structure.json`'s declared path directly.

**Per-extruder-variant fields**: parameters that vary by extruder (e.g. `filament_flow_ratio`, `nozzle_temperature`, `filament_max_volumetric_speed`) are arrays parallel to `filament_extruder_variant`. Bundles with 4 variants (`[Direct Drive Standard, Direct Drive High Flow, Bowden Standard, Bowden High Flow]`) consistently mirror the "Direct Drive High Flow" value into both Bowden slots — the merge logic in `_filament_lib.merge_profile` relies on and preserves this convention.

**`reference-old-repo/` vs this repo's format**: the old repo's profiles are small deltas (`"inherits": "Generic PC @BBL P1S"` + a handful of overridden keys) against Bambu Studio's own built-in system profiles for *other* printers — not self-contained, and can't be flattened for a printer without that printer's own system profile data (not available locally). The converter works around this by taking an existing bundle (ideally for the *same* printer, same material) as a machine-parameter template and layering the old-repo delta's material-specific tuning (flow ratio, plate temp, fan speed, max volumetric speed, retraction) on top, leaving `"nil"`/unspecified fields at the template's already-validated value.

**Template selection** (`_filament_lib.choose_template`): (1) an existing bundle for the *same printer* with the same `filament_type` — best; (2) an existing bundle for the same printer in the same **polymer family** (`_filament_lib.POLYMER_FAMILY` — PLA-ish, PETG-ish, TPU, ABS/ASA/PC, or PA-ish; deliberately finer than the compatibility tiers below, since e.g. a PLA-CF bundle is a bad temperature template for a PETG Galaxy gap even though both are "base tier"); (3) `_filament_lib.FALLBACK_TEMPLATE`, a repo-wide canonical set (mostly pointing at `X2D/0.4mm/`, which has the broadest coverage). Template lookups always use a bundle-list **snapshot taken before a conversion run starts writing** — never a live re-scan — so bundle N+1 in a batch can't template off bundle N that the same run just generated; everything traces back to a real, originally-existing bundle.

**Machine compatibility gating** (`_filament_lib.classify_gap`, `TIER_BASE`/`TIER_ENGINEERING_MED`/`TIER_ENGINEERING_HIGH`): the converter never invents a filament/printer pairing without evidence.
- Base materials (PLA, PETG, TPU, and CF-reinforced PLA/PETG/PET) are generated freely — safe on any Bambu machine.
- "Engineering" materials (ABS, ASA, ASA-CF, PC) require either a machine-coded old-repo delta (`"inherits": "... @BBL H2D"`) for that *exact* printer, or that the printer already ships another engineering-tier bundle in this repo (proving real enclosure/hardware capability).
- High-temperature nylon materials (PA, PA-CF, PAHT-CF) require a machine-coded delta for that exact printer — never inferred from another material's tier-proof, since a working ABS profile doesn't prove a hotend can hit 300°C.
- Gaps that don't clear their bar are left as `SKIP (needs review)` and reported by `find_missing_filaments.py`, not silently generated. Consequently PA-CF/PAHT-CF exist only on X2D (the one printer with historical evidence for them), and no ABS/ASA/PC exists on the open-frame A1 mini/A2L.

One known data quirk baked into `_filament_lib.py`: `reference-old-repo/PET-CF (X1 X1C P1S P1P).json` has a typo'd `"inherits": "Generic ABS"` even though its filename/content are unambiguously PET-CF — `FILE_BASE_MATERIAL_OVERRIDE` corrects this rather than trusting the source label.

**Generated vs original bundles**: bundles produced by the converter are marked with a trailing `*` in `README.md`'s and `REFERENCES.md`'s inventory tables (`gen_inventory_table.py` derives this from `KNOWN_ORIGINAL_BUNDLES`, an explicit allowlist that must be extended when a genuinely new original TINMORRY export is added). They aren't real TINMORRY-tested exports. The X2D PA-CF/PAHT-CF bundles in particular inherited PETG CF's nozzle/bed temperatures (no override existed in their source delta) rather than their real higher-temperature requirements — flag this if touching those two bundles.

See `README.md` for the full profile inventory table and installation steps, and `REFERENCES.md` for the complete per-bundle metadata inventory and external references.
