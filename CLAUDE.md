# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Not a software project — a collection of Bambu Studio filament preset bundles (`.bbsflmt` files) for TINMORRY filaments, organized by printer model, plus a small Python toolchain that derives new bundles for printers/materials this repo is missing from an older, unbundled TINMORRY profile source. There is no build, lint, or test suite.

## Commands

```bash
# Report gaps: filament types in reference-old-repo/ and reference-bambuprinters/ with no
# bundle yet for a given printer, each labeled ALLOW or SKIP per the compatibility policy below
python3 scripts/find_missing_filaments.py                 # all printers
python3 scripts/find_missing_filaments.py --printer H2D   # one printer

# Generate new .bbsflmt bundles for the ALLOW-labeled gaps (never overwrites an existing bundle)
python3 scripts/convert_old_repo_to_printer.py --dry-run  # preview
python3 scripts/convert_old_repo_to_printer.py             # write
python3 scripts/convert_old_repo_to_printer.py --printer P2S

# Regenerate REFERENCES.md's inventory table from the bundles actually on disk
python3 scripts/gen_inventory_table.py               # print the table
python3 scripts/gen_inventory_table.py --check       # exit 1 if REFERENCES.md is stale

# Regenerate the collapsible per-printer download tables in every README.*.md
python3 scripts/gen_readme_tables.py                 # print every language's block
python3 scripts/gen_readme_tables.py --write          # splice into every README
python3 scripts/gen_readme_tables.py --check          # exit 1 if any is stale

# Extract any plain .zip wrapping a .bbsflmt (rather than being a bundle itself) into its printer folder
python3 scripts/unzip_wrapper_zips.py --dry-run
python3 scripts/unzip_wrapper_zips.py --delete-zip
```

Run `gen_inventory_table.py` and `gen_readme_tables.py --write` together any time a bundle is added, removed, or renamed — both derive from `_filament_lib.inventory_rows()`, so they can't drift from each other, but neither is regenerated automatically. `gen_readme_tables.py`'s raw-download links are hardcoded to `GITHUB_OWNER`/`GITHUB_REPO`/`GITHUB_BRANCH` at the top of that file — update those constants (and rerun with `--write`) if the repo moves or this work lands on a different branch.

`find_missing_filaments.py` and `convert_old_repo_to_printer.py` read from two gitignored local delta sources, neither tracked in this repo — reclone both before running either script:
- `reference-old-repo/`: TINMORRY's older per-printer profile repo (https://github.com/TINMORRY/TINMORRY-filament-profile-for-Bambu-printers.git). Small `"inherits"`-based deltas, tagged by printer via an `"@BBL <code>"` string inside `inherits`.
- `reference-bambuprinters/`: TINMORRY (Binh Duong)'s repo (https://github.com/tinmorrybinhduong/BambuPrinters) — see REFERENCES.md's External references. Many of its `*_Filament(*).json` files are complete per-printer exports with a blank `inherits`, tagged by printer via the filename instead (`*_Process(*).json` files are print/process settings and are ignored — out of scope, this repo only bundles filament presets).

Both sources are merged into one set of gaps by `_filament_lib.delta_entries()`, so `find_gaps()` picks whichever source has evidence for a given printer (preferring a direct match over an arbitrary same-material entry from another printer — see `find_gaps` in `_filament_lib.py`). Shared logic (printer registry, gating policy, delta-source parsing, template selection, bundle merging) lives in `scripts/_filament_lib.py`.

**Custom overrides**: to hand-force specific fields on a generated bundle (e.g. a real spec-sheet temperature that no delta source has), add `scripts/custom_overrides/<printer_dir>/<output_name>.json` — a flat `{key: value}` dict, committed (not gitignored). `convert_old_repo_to_printer.py` applies it as the last step after the template/delta merge, so it always wins; values must already be in the profile's final shape (e.g. a list with one entry per `filament_extruder_variant` for per-variant fields). See `_filament_lib.load_custom_override`'s docstring.

## Architecture

**Repo layout**: one top-level folder per printer model (`A1/`, `A1mini/`, `A2L/`, `H2C/`, `H2D/`, `H2S/`, `P1S/`, `P2S/`, `X2D/0.4mm/`), each holding `.bbsflmt` files for that printer's compatible filaments.

**`.bbsflmt` format**: a zip archive containing `bundle_structure.json` (bundle id, filament name, Studio version, and a `filament_vendor[].filament_path[]` list mapping to the profile JSON(s) inside) plus one fully-flattened filament settings JSON per compatible printer under `TINMORRY/`. "Fully flattened" means every parameter (temps, cooling, flow, retraction, etc.) is a literal value — no `inherits` chain to resolve. Some bundles (e.g. TPU 95A, PETG GF/Marble/Metallic under `X2D/0.4mm/`) are dual-printer: `filament_path` has one entry for P2S and one for X2D — when reading these programmatically, select by filename substring (or printer code), don't assume index 0. A couple of bundles have non-ASCII filenames (a full-width comma, a backtick) that round-trip correctly as JSON text but don't byte-match the zip's cp437-stored entry name — walk `zipfile.namelist()` rather than looking up `bundle_structure.json`'s declared path directly.

**Per-extruder-variant fields**: parameters that vary by extruder (e.g. `filament_flow_ratio`, `nozzle_temperature`, `filament_max_volumetric_speed`) are arrays parallel to `filament_extruder_variant`. Bundles with 4 variants (`[Direct Drive Standard, Direct Drive High Flow, Bowden Standard, Bowden High Flow]`) consistently mirror the "Direct Drive High Flow" value into both Bowden slots — the merge logic in `_filament_lib.merge_profile` relies on and preserves this convention.

**Delta sources vs this repo's format**: `reference-old-repo/`'s profiles are small deltas (`"inherits": "Generic PC @BBL P1S"` + a handful of overridden keys) against Bambu Studio's own built-in system profiles for *other* printers — not self-contained, and can't be flattened for a printer without that printer's own system profile data (not available locally). `reference-bambuprinters/`'s `*_Filament(*).json` files are a mix of the same small-delta shape and complete per-printer exports (blank `inherits`, ~150 keys) — `_filament_lib.merge_profile` treats both shapes identically, since a delta with (nearly) every key just overwrites (nearly) everything the template would have supplied. Either way, the converter works around the non-self-contained cases by taking an existing bundle (ideally for the *same* printer, same material) as a machine-parameter template and layering the delta's material-specific tuning (flow ratio, plate temp, fan speed, max volumetric speed, retraction) on top, leaving `"nil"`/unspecified fields at the template's already-validated value.

**Template selection** (`_filament_lib.choose_template`): (1) an existing bundle for the *same printer* with the same `filament_type` — best; (2) an existing bundle for the same printer in the same **polymer family** (`_filament_lib.POLYMER_FAMILY` — PLA-ish, PETG-ish, TPU, ABS/ASA/PC, or PA-ish; deliberately finer than the compatibility tiers below, since e.g. a PLA-CF bundle is a bad temperature template for a PETG Galaxy gap even though both are "base tier"); (3) `_filament_lib.FALLBACK_TEMPLATE`, a repo-wide canonical set (mostly pointing at `X2D/0.4mm/`, which has the broadest coverage). Template lookups always use a bundle-list **snapshot taken before a conversion run starts writing** — never a live re-scan — so bundle N+1 in a batch can't template off bundle N that the same run just generated; everything traces back to a real, originally-existing bundle.

**Machine compatibility gating** (`_filament_lib.classify_gap`, `TIER_BASE`/`TIER_ENGINEERING_MED`/`TIER_ENGINEERING_HIGH`): the converter never invents a filament/printer pairing without evidence.
- Base materials (PLA, PETG, TPU, and CF-reinforced PLA/PETG/PET) are generated freely — safe on any Bambu machine.
- "Engineering" materials (ABS, ASA, ASA-CF, PC) require either a machine-coded old-repo delta (`"inherits": "... @BBL H2D"`) for that *exact* printer, OR that the printer already ships another engineering-tier bundle in this repo AND has `PRINTERS[...]["enclosed"] == True`. The `enclosed` flag (physical side panels/lid, not necessarily an actively heated chamber) exists because "tier-proof" alone is too coarse: the old repo has a direct, real `"Generic PC @BBL A1"` system-profile delta even though A1 is Bambu's open-frame budget printer, and that single fact doesn't imply ABS/ASA (whose fumes/warping specifically call for an enclosure) are also fine there. Direct evidence is trusted regardless of `enclosed`, since it's a real vendor-declared fact rather than our own inference — this is why A1 has a generated PC GF bundle but no ABS/ASA.
- High-temperature nylon materials (PA, PA-CF, PAHT-CF) require a machine-coded delta for that exact printer — never inferred from another material's tier-proof, since a working ABS profile doesn't prove a hotend can hit 300°C.
- Gaps that don't clear their bar are left as `SKIP (needs review)` and reported by `find_missing_filaments.py`, not silently generated. Consequently PA-CF/PAHT-CF exist only on X2D (the one printer with historical evidence for them), and no ABS/ASA exists on the open-frame A1/A1 mini/A2L (`enclosed: False` in `PRINTERS`).
- Because tier-proof depends on what's already on disk, generating bundles for a brand-new printer can unlock further gaps on a second pass (e.g. generating A1's direct-evidence PC GF, then rerunning, doesn't unlock anything further there since A1 isn't enclosed — but the same pattern on an enclosed printer like P1S generates PC GF first, then a rerun sees `engineering_capable and enclosed` and unlocks ABS/ASA/ASA-CF via tier-proof). Always rerun `find_missing_filaments.py` after a conversion pass to check for newly-unlocked gaps.

One known data quirk baked into `_filament_lib.py`: `reference-old-repo/PET-CF (X1 X1C P1S P1P).json` has a typo'd `"inherits": "Generic ABS"` even though its filename/content are unambiguously PET-CF — `FILE_BASE_MATERIAL_OVERRIDE` corrects this rather than trusting the source label.

**Generated vs original bundles**: `_filament_lib.is_original_bundle(folder, filament_name)` checks an explicit allowlist, `KNOWN_ORIGINAL_BUNDLES` — there's no reliable in-band signal on disk (a generated `bundle_id` looks like any other), so this list is maintained by hand and must be extended whenever a genuinely new original TINMORRY export is added. `gen_inventory_table.py` (REFERENCES.md, trailing `*` on the filename) and `gen_readme_tables.py` (every `README.*.md`, an "Original"/"Derived"-equivalent column per language) both derive from the same `_filament_lib.inventory_rows()`, so they can't disagree with each other — but forgetting to extend `KNOWN_ORIGINAL_BUNDLES` would make a real export show up mislabeled as "Derived" everywhere at once. The X2D PA-CF/PAHT-CF bundles in particular inherited PETG CF's nozzle/bed temperatures (no override existed in their source delta) rather than their real higher-temperature requirements — flag this if touching those two bundles.

**README.md / README.vi.md / README.zh.md structure**: three parallel translations (English, Vietnamese, Chinese), each linking to the other two at the top. All three start with a fork-provenance line, then a **⚠️ Caution** section (non-technical warning about Derived profiles, not to be confused with the machine-compatibility gating policy above — the caution is aimed at end users, the gating policy at this tooling), then the "Available profiles" section, which is entirely generated content between `<!-- BEGIN/END GENERATED PROFILE TABLES -->` markers — don't hand-edit inside those markers, they're overwritten by `gen_readme_tables.py --write`. Adding a fourth language: add a file + headers + labels entry to `LANGS` in `gen_readme_tables.py`, create the new `README.<lang>.md` with the same prose sections translated (and the markers in place), and add its link to the language switcher at the top of the other README files.

See `README.md` for the full profile inventory table and installation steps, and `REFERENCES.md` for the complete per-bundle metadata inventory and external references.
