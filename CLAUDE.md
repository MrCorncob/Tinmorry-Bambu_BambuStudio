# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Not a software project — a collection of Bambu Studio filament preset bundles (`.bbsflmt` files) for TINMORRY filaments, organized by printer model, plus two Python scripts used to derive new bundles for the newest printer (X2D) from an older, unbundled profile source. There is no build, lint, or test suite.

## Commands

```bash
# Report which filament types exist in reference-old-repo/ but have no X2D/0.4mm bundle yet
python3 scripts/find_missing_x2d_filaments.py

# Generate new X2D/0.4mm/*.bbsflmt bundles for those gaps (never overwrites an existing bundle it reads as a template)
python3 scripts/convert_old_repo_to_x2d.py --dry-run   # preview
python3 scripts/convert_old_repo_to_x2d.py              # write
```

Both scripts read from `reference-old-repo/` — a gitignored local clone of TINMORRY's older per-printer profile repo (https://github.com/TINMORRY/TINMORRY-filament-profile-for-Bambu-printers.git). Reclone it there before running either script; it isn't tracked in this repo.

## Architecture

**Repo layout**: one top-level folder per printer model (`A1mini/`, `A2L/`, `H2C/`, `H2D/`, `H2S/`, `P2S/`, `X2D/0.4mm/`), each holding `.bbsflmt` files for that printer's compatible filaments.

**`.bbsflmt` format**: a zip archive containing `bundle_structure.json` (bundle id, filament name, Studio version, and a `filament_vendor[].filament_path[]` list mapping to the profile JSON(s) inside) plus one fully-flattened filament settings JSON per compatible printer under `TINMORRY/`. "Fully flattened" means every parameter (temps, cooling, flow, retraction, etc.) is a literal value — no `inherits` chain to resolve. Some bundles (e.g. TPU 95A, PETG GF/Marble/Metallic on X2D) are dual-printer: `filament_path` has one entry for P2S and one for X2D — when reading these programmatically, select by filename substring, don't assume index 0.

**Per-extruder-variant fields**: parameters that vary by extruder (e.g. `filament_flow_ratio`, `nozzle_temperature`, `filament_max_volumetric_speed`) are arrays parallel to `filament_extruder_variant`. X2D bundles use 4 variants: `[Direct Drive Standard, Direct Drive High Flow, Bowden Standard, Bowden High Flow]`. Every existing X2D bundle mirrors the "Direct Drive High Flow" value into both Bowden slots — `scripts/convert_old_repo_to_x2d.py` relies on and preserves this convention.

**`reference-old-repo/` vs this repo's format**: the old repo's profiles are small deltas (`"inherits": "Generic PC @BBL P1S"` + a handful of overridden keys) against Bambu Studio's own built-in system profiles for *other* printers — they are not self-contained and can't be flattened for X2D without X2D's own system profile data (which isn't available locally). `convert_old_repo_to_x2d.py` works around this by taking an existing X2D bundle of the closest material family as a machine-parameter template and layering the old-repo delta's material-specific tuning on top, leaving `"nil"`/unspecified fields at the template's already-validated value. The material→template mapping is the `CONVERSIONS` list at the top of that script — extend it by hand as new gaps are found via `find_missing_x2d_filaments.py`.

**Generated vs original bundles**: X2D bundles produced by the conversion script are marked with a trailing `*` in `README.md`'s and `REFERENCES.md`'s inventory tables, since they aren't real TINMORRY-tested exports. PA-CF and PAHT-CF in particular inherited PETG CF's nozzle/bed temperatures (no override existed in their source delta) rather than their real higher-temperature requirements — flag this if touching those two bundles.

See `README.md` for the full profile inventory table and installation steps, and `REFERENCES.md` for the complete per-bundle metadata inventory and external references.
