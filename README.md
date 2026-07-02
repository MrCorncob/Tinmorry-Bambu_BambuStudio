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
| A1 mini | PETG Matte, TPU 95A |
| A2L | PETG ECO, PETG Metallic, PLA Rapid, PLA Silk, TPU 95A |
| H2C | PLA CF, PLA Rapid |
| H2D | ABS pro, ASA CF, PLA Matte |
| H2S | ASA CF, PETG CF, PLA Rapid, TPU 95A |
| P2S | ABS Pro, PETG GF, PETG Marble, PETG Metallic, PP-CF, TPU 95A |
| X2D | ABS Pro, ASA basic, PETG CF, PETG ECO, PETG GF, PETG Galaxy, PETG Marble, PETG Metallic, PETG Sparkly, PLA matte, TPU 95A |

Some filaments (PETG GF, PETG Marble, PETG Metallic, TPU 95A) ship a single bundle under `X2D/0.4mm/` that contains presets for both the P2S and X2D printers.

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
- `P2S/P2S-PETG-Matte.zip` is a plain zip wrapper around a `.bbsflmt` bundle rather than a bundle itself; unzip it first if Bambu Studio doesn't accept it directly.
