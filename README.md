# Tinmorry Filament Profiles for Bambu Studio

Custom Bambu Studio filament presets for **TINMORRY** filaments, packaged as `.bbsflmt` bundles and organized by Bambu Lab printer model.

## Repository layout

Each top-level folder corresponds to a printer model (as reported in each profile's `compatible_printers` field). `X2D` additionally nests profiles under a `0.4mm` nozzle folder.

```
A1mini/   Bambu Lab A1 mini, 0.4mm nozzle
A2L/      Bambu Lab A2L, 0.4mm nozzle
H2C/      Bambu Lab H2C, 0.4mm nozzle
H2D/      Bambu Lab H2D, 0.4mm nozzle
H2S/      Bambu Lab H2S, 0.4mm nozzle
P2S/      Bambu Lab P2S, 0.4mm nozzle
X2D/0.4mm/  Bambu Lab X2D, 0.4mm nozzle
```

## Available profiles

| Printer | Filaments |
|---|---|
| A1 mini | PET CF*, PET CF GF*, PETG CF*, PETG CF GF*, PETG CF PP*, PETG ECO*, PETG GF*, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Matte, PETG Metallic*, PETG Sparkly*, PLA*, PLA CF*, PLA Galaxy*, PLA Matte*, PLA Silk*, TPU 95A, TPU GF* |
| A2L | PET CF*, PET CF GF*, PETG CF*, PETG CF GF*, PETG CF PP*, PETG ECO, PETG GF*, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Metallic, PETG Sparkly*, PLA CF*, PLA Galaxy*, PLA Matte*, PLA Rapid, PLA Silk, TPU 95A, TPU GF* |
| H2C | ABS*, ASA*, ASA CF*, PC GF*, PET CF*, PET CF GF*, PETG CF*, PETG CF GF*, PETG CF PP*, PETG ECO*, PETG GF*, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Metallic*, PETG Sparkly*, PLA CF, PLA Galaxy*, PLA Matte*, PLA Rapid, PLA Silk*, TPU*, TPU 95A*, TPU GF* |
| H2D | ABS pro, ASA CF, PC GF*, PET CF*, PET CF GF*, PETG CF*, PETG CF GF*, PETG CF PP*, PETG ECO*, PETG GF*, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Metallic*, PETG Sparkly*, PLA CF*, PLA Galaxy*, PLA Matte, PLA Silk*, TPU*, TPU 95A*, TPU GF* |
| H2S | ABS*, ABS Pro*, ASA CF, PC GF*, PET CF*, PET CF GF*, PETG CF, PETG ECO*, PETG GF*, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Metallic*, PETG Sparkly*, PLA CF*, PLA Galaxy*, PLA Matte*, PLA Rapid, PLA Silk*, TPU 95A, TPU GF* |
| P2S | ABS Pro, ASA*, ASA CF*, PC GF*, PET CF*, PET CF GF*, PETG CF*, PETG CF GF*, PETG ECO*, PETG GF, PETG Galaxy*, PETG HS*, PETG Marble*, PETG Matte, PETG Metallic, PETG Sparkly*, PLA*, PLA CF*, PLA Galaxy*, PLA Matte*, PLA Silk*, PP-CF, TPU 95A, TPU GF* |
| X2D | ABS Pro, ASA basic, ASA CF*, PA-CF*, PAHT-CF*, PC GF*, PET CF*, PETG CF, PETG ECO, PETG GF, PETG Galaxy, PETG HS*, PETG Marble, PETG Metallic, PETG Sparkly, PLA CF*, PLA Galaxy*, PLA Silk*, PLA matte, TPU 95A, TPU GF* |

Some filaments (PETG GF, PETG Marble, PETG Metallic, TPU 95A) ship a single bundle under `X2D/0.4mm/` that contains presets for both the P2S and X2D printers.

\* Not an original TINMORRY export — generated from TINMORRY's older per-printer profiles via `scripts/convert_old_repo_to_printer.py`, gated by a machine-compatibility policy (see CLAUDE.md). PA-CF/PAHT-CF are deliberately absent everywhere except X2D, and ABS/ASA/PC are absent from A1 mini/A2L entirely — none of these printers had compatibility evidence for those materials, so they were skipped rather than guessed. See [REFERENCES.md](REFERENCES.md) for the full inventory and a caveat on the X2D PA-CF/PAHT-CF bundles' temperatures.

## Installing a profile

1. In Bambu Studio, go to **File → Import → Import Configs**.
2. Select the `.bbsflmt` file for the filament/printer combination you want.
3. The filament preset will appear under the matching printer in the filament dropdown, under the `TINMORRY` vendor.

## File format

Each `.bbsflmt` file is a zip archive (Bambu Studio's filament config bundle format) containing:

- `bundle_structure.json` — bundle metadata: bundle id, the Bambu Studio version it was exported from, the filament name, and the vendor/profile-path mapping.
- `TINMORRY/<filament> @<printer> 0.4 nozzle.json` — one filament settings profile per compatible printer, with the full set of Bambu Studio filament parameters (temperatures, cooling, flow, retraction, etc.).

See [REFERENCES.md](REFERENCES.md) for a full inventory of bundles and their metadata.

## Known quirks

- A few filenames contain unusual characters carried over from the original export (e.g. a full-width comma in `H2D/TINMORRY PLA Matte，.bbsflmt`, a backtick in `` P2S/TINMORRY PP-CF `.bbsflmt ``). These are cosmetic and don't affect import.
