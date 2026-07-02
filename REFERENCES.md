# References

## `.bbsflmt` bundle format

A `.bbsflmt` file is a standard zip archive produced by Bambu Studio's filament config export. Structure observed across every bundle in this repo:

```
<bundle>.bbsflmt
├── bundle_structure.json
└── TINMORRY/
    └── <filament name> @<printer model> 0.4 nozzle.json   (one per compatible printer)
```

`bundle_structure.json` fields:

| Field | Description |
|---|---|
| `bundle_id` | Internal id, format `<numeric-id>_<filament name>_<unix timestamp>` |
| `bundle_type` | Always `"filament config bundle"` in this repo |
| `filament_name` | Display name of the filament |
| `filament_vendor` | Array mapping vendor name (`TINMORRY`) to the relative path(s) of the profile JSON(s) inside the archive |
| `version` | Bambu Studio version the bundle was exported from |

Each per-printer profile JSON follows Bambu Studio's standard filament settings schema (the same keys used in Bambu Studio's built-in system filament profiles), including `filament_type`, `compatible_printers`, temperature/cooling/flow/retraction parameters, etc.

## Full profile inventory

| Folder | File | Filament | Type | Compatible printer | Studio version | Bundle id |
|---|---|---|---|---|---|---|
| A1mini | TINMORRY PETG Matte.bbsflmt | TINMORRY PETG Matte | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PETG Matte_1780301588 |
| A1mini | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY TPU 95A_1782271111 |
| A2L | TINMORRY PETG ECO.bbsflmt | TINMORRY PETG ECO | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG ECO_1780887719 |
| A2L | TINMORRY PETG Metallic.bbsflmt | TINMORRY PETG Metallic | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Metallic_1780919570 |
| A2L | TINMORRY PLA Rapid.bbsflmt | TINMORRY PLA Rapid | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Rapid_1780888326 |
| A2L | TINMORRY PLA Silk.bbsflmt | TINMORRY PLA Silk | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Silk_1781160724 |
| A2L | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY TPU 95A_1780887573 |
| H2C | TINMORRY PLA CF.bbsflmt | TINMORRY PLA CF | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA CF_1781245287 |
| H2C | TINMORRY PLA Rapid.bbsflmt | TINMORRY PLA Rapid | PLA | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PLA Rapid_1780309015 |
| H2D | TINMORRY ABS pro.bbsflmt | TINMORRY ABS pro | ABS | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ABS pro_1780299462 |
| H2D | TINMORRY ASA CF.bbsflmt | TINMORRY ASA CF | ASA | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ASA CF_1780303223 |
| H2D | TINMORRY PLA Matte，.bbsflmt | TINMORRY PLA Matte， | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Matte，_1779697060 |
| H2S | TINMORRY ASA CF.bbsflmt | TINMORRY ASA CF | ASA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ASA CF_1780304244 |
| H2S | TINMORRY PETG CF.bbsflmt | TINMORRY PETG CF | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG CF_1782456820 |
| H2S | TINMORRY PLA Rapid.bbsflmt | TINMORRY PLA Rapid | PLA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PLA Rapid_1780308480 |
| H2S | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY TPU 95A_1780369052 |
| P2S | TINMORRY ABS Pro.bbsflmt | TINMORRY ABS Pro | ABS | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ABS Pro_1780300252 |
| P2S | TINMORRY PP-CF `.bbsflmt | TINMORRY PP-CF ` | PP-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PP-CF `_1780312363 |
| P2S | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY TPU 95A_1780368775 |
| P2S | P2S-PETG-Matte.zip | TINMORRY PETG Matte | PETG | (nested `.bbsflmt`, not a bundle itself) | — | — |
| X2D/0.4mm | TINMORRY ABS Pro.bbsflmt | TINMORRY ABS Pro | ABS | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS Pro_1777370656 |
| X2D/0.4mm | TINMORRY ASA basic.bbsflmt | TINMORRY ASA basic | ASA | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA basic_1777370656 |
| X2D/0.4mm | TINMORRY PETG CF.bbsflmt | TINMORRY PETG CF | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_1777370656 |
| X2D/0.4mm | TINMORRY PETG ECO.bbsflmt | TINMORRY PETG ECO | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_1777370656 |
| X2D/0.4mm | TINMORRY PETG GF.bbsflmt | TINMORRY PETG GF | PETG | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY PETG GF_1778039341 |
| X2D/0.4mm | TINMORRY PETG Galaxy.bbsflmt | TINMORRY PETG Galaxy | PETG | Bambu Lab X2D 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Galaxy_1781058844 |
| X2D/0.4mm | TINMORRY PETG Marble.bbsflmt | TINMORRY PETG Marble | PETG | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY PETG Marble_1778039341 |
| X2D/0.4mm | TINMORRY PETG Metallic.bbsflmt | TINMORRY PETG Metallic | PETG | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY PETG Metallic_1778039341 |
| X2D/0.4mm | TINMORRY PETG Sparkly.bbsflmt | TINMORRY PETG Sparkly | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_1777370656 |
| X2D/0.4mm | TINMORRY PLA matte.bbsflmt | TINMORRY PLA matte | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA matte_1779247765 |
| X2D/0.4mm | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU 95A_1778039341 |

Generated by extracting and inspecting each `.bbsflmt` archive's `bundle_structure.json` and per-printer profile JSON in this repository (2026-07-02).

## External references

- [Bambu Studio (GitHub)](https://github.com/bambulab/BambuStudio) — the slicer these profiles are built for; its `resources/profiles` directory documents the same filament-setting schema used inside each bundle here.
