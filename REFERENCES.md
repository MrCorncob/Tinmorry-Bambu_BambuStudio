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
| A1mini | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| A1mini | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| A1mini | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| A1mini | TINMORRY PETG CF PP.bbsflmt* | TINMORRY PETG CF PP | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF PP_&lt;generated&gt; |
| A1mini | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| A1mini | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| A1mini | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| A1mini | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| A1mini | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| A1mini | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| A1mini | TINMORRY PETG Matte.bbsflmt | TINMORRY PETG Matte | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PETG Matte_1780301588 |
| A1mini | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| A1mini | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab A1 mini 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| A1mini | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| A1mini | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| A1mini | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| A1mini | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| A1mini | TINMORRY PLA.bbsflmt* | TINMORRY PLA | PLA | Bambu Lab A1 mini 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA_&lt;generated&gt; |
| A1mini | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY TPU 95A_1782271111 |
| A1mini | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab A1 mini 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| A2L | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| A2L | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| A2L | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| A2L | TINMORRY PETG CF PP.bbsflmt* | TINMORRY PETG CF PP | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG CF PP_&lt;generated&gt; |
| A2L | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| A2L | TINMORRY PETG ECO.bbsflmt | TINMORRY PETG ECO | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG ECO_1780887719 |
| A2L | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| A2L | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| A2L | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| A2L | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| A2L | TINMORRY PETG Metallic.bbsflmt | TINMORRY PETG Metallic | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Metallic_1780919570 |
| A2L | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| A2L | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| A2L | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| A2L | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| A2L | TINMORRY PLA Rapid.bbsflmt | TINMORRY PLA Rapid | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Rapid_1780888326 |
| A2L | TINMORRY PLA Silk.bbsflmt | TINMORRY PLA Silk | PLA | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Silk_1781160724 |
| A2L | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY TPU 95A_1780887573 |
| A2L | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab A2L 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| H2C | TINMORRY ABS.bbsflmt* | TINMORRY ABS | ABS | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS_&lt;generated&gt; |
| H2C | TINMORRY ASA CF.bbsflmt* | TINMORRY ASA CF | ASA-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA CF_&lt;generated&gt; |
| H2C | TINMORRY ASA.bbsflmt* | TINMORRY ASA | ASA | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA_&lt;generated&gt; |
| H2C | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| H2C | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| H2C | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| H2C | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| H2C | TINMORRY PETG CF PP.bbsflmt* | TINMORRY PETG CF PP | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF PP_&lt;generated&gt; |
| H2C | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| H2C | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| H2C | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| H2C | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| H2C | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| H2C | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| H2C | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| H2C | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| H2C | TINMORRY PLA CF.bbsflmt | TINMORRY PLA CF | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA CF_1781245287 |
| H2C | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| H2C | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| H2C | TINMORRY PLA Rapid.bbsflmt | TINMORRY PLA Rapid | PLA | Bambu Lab H2C 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PLA Rapid_1780309015 |
| H2C | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab H2C 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| H2C | TINMORRY TPU 95a.bbsflmt* | TINMORRY TPU 95a | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU 95a_&lt;generated&gt; |
| H2C | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| H2C | TINMORRY TPU.bbsflmt* | TINMORRY TPU | TPU | Bambu Lab H2C 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU_&lt;generated&gt; |
| H2D | TINMORRY ABS pro.bbsflmt | TINMORRY ABS pro | ABS | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ABS pro_1780299462 |
| H2D | TINMORRY ASA CF.bbsflmt | TINMORRY ASA CF | ASA | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ASA CF_1780303223 |
| H2D | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| H2D | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| H2D | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| H2D | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| H2D | TINMORRY PETG CF PP.bbsflmt* | TINMORRY PETG CF PP | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF PP_&lt;generated&gt; |
| H2D | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| H2D | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| H2D | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| H2D | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| H2D | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| H2D | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| H2D | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| H2D | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab H2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| H2D | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| H2D | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| H2D | TINMORRY PLA Matte，.bbsflmt | TINMORRY PLA Matte， | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Matte，_1779697060 |
| H2D | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab H2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| H2D | TINMORRY TPU 95a.bbsflmt* | TINMORRY TPU 95a | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU 95a_&lt;generated&gt; |
| H2D | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| H2D | TINMORRY TPU.bbsflmt* | TINMORRY TPU | TPU | Bambu Lab H2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU_&lt;generated&gt; |
| H2S | TINMORRY ABS Pro.bbsflmt* | TINMORRY ABS Pro | ABS | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS Pro_&lt;generated&gt; |
| H2S | TINMORRY ABS.bbsflmt* | TINMORRY ABS | ABS | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS_&lt;generated&gt; |
| H2S | TINMORRY ASA CF.bbsflmt | TINMORRY ASA CF | ASA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ASA CF_1780304244 |
| H2S | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| H2S | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| H2S | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| H2S | TINMORRY PETG CF.bbsflmt | TINMORRY PETG CF | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG CF_1782456820 |
| H2S | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| H2S | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| H2S | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| H2S | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| H2S | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| H2S | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| H2S | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab H2S 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| H2S | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| H2S | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| H2S | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| H2S | TINMORRY PLA Rapid.bbsflmt | TINMORRY PLA Rapid | PLA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PLA Rapid_1780308480 |
| H2S | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| H2S | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY TPU 95A_1780369052 |
| H2S | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab H2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| P2S | TINMORRY ABS Pro.bbsflmt | TINMORRY ABS Pro | ABS | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY ABS Pro_1780300252 |
| P2S | TINMORRY ASA CF.bbsflmt* | TINMORRY ASA CF | ASA-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA CF_&lt;generated&gt; |
| P2S | TINMORRY ASA.bbsflmt* | TINMORRY ASA | ASA | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA_&lt;generated&gt; |
| P2S | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| P2S | TINMORRY PET CF GF.bbsflmt* | TINMORRY PET CF GF | PET-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF GF_&lt;generated&gt; |
| P2S | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| P2S | TINMORRY PETG CF GF.bbsflmt* | TINMORRY PETG CF GF | PETG-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF GF_&lt;generated&gt; |
| P2S | TINMORRY PETG CF.bbsflmt* | TINMORRY PETG CF | PETG-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_&lt;generated&gt; |
| P2S | TINMORRY PETG ECO.bbsflmt* | TINMORRY PETG ECO | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_&lt;generated&gt; |
| P2S | TINMORRY PETG GF.bbsflmt* | TINMORRY PETG GF | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG GF_&lt;generated&gt; |
| P2S | TINMORRY PETG Galaxy.bbsflmt* | TINMORRY PETG Galaxy | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Galaxy_&lt;generated&gt; |
| P2S | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| P2S | TINMORRY PETG Marble.bbsflmt* | TINMORRY PETG Marble | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Marble_&lt;generated&gt; |
| P2S | TINMORRY PETG Matte.bbsflmt | TINMORRY PETG Matte | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Matte_1780387842 |
| P2S | TINMORRY PETG Metallic.bbsflmt* | TINMORRY PETG Metallic | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Metallic_&lt;generated&gt; |
| P2S | TINMORRY PETG Sparkly.bbsflmt* | TINMORRY PETG Sparkly | PETG | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_&lt;generated&gt; |
| P2S | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| P2S | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| P2S | TINMORRY PLA Matte.bbsflmt* | TINMORRY PLA Matte | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Matte_&lt;generated&gt; |
| P2S | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| P2S | TINMORRY PLA.bbsflmt* | TINMORRY PLA | PLA | Bambu Lab P2S 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA_&lt;generated&gt; |
| P2S | TINMORRY PP-CF `.bbsflmt | TINMORRY PP-CF ` | PP-CF | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 80099216_TINMORRY PP-CF `_1780312363 |
| P2S | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY TPU 95A_1780368775 |
| P2S | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab P2S 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |
| X2D/0.4mm | TINMORRY ABS Pro.bbsflmt | TINMORRY ABS Pro | ABS | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ABS Pro_1777370656 |
| X2D/0.4mm | TINMORRY ASA CF.bbsflmt* | TINMORRY ASA CF | ASA-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA CF_&lt;generated&gt; |
| X2D/0.4mm | TINMORRY ASA basic.bbsflmt | TINMORRY ASA basic | ASA | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY ASA basic_1777370656 |
| X2D/0.4mm | TINMORRY PA-CF.bbsflmt* | TINMORRY PA-CF | PA-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PA-CF_&lt;generated&gt; |
| X2D/0.4mm | TINMORRY PAHT-CF.bbsflmt* | TINMORRY PAHT-CF | PAHT-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PAHT-CF_&lt;generated&gt; |
| X2D/0.4mm | TINMORRY PC GF.bbsflmt* | TINMORRY PC GF | PC | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PC GF_&lt;generated&gt; |
| X2D/0.4mm | TINMORRY PET CF.bbsflmt* | TINMORRY PET CF | PET-CF | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PET CF_&lt;generated&gt; |
| X2D/0.4mm | TINMORRY PETG CF.bbsflmt | TINMORRY PETG CF | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG CF_1777370656 |
| X2D/0.4mm | TINMORRY PETG ECO.bbsflmt | TINMORRY PETG ECO | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG ECO_1777370656 |
| X2D/0.4mm | TINMORRY PETG GF.bbsflmt | TINMORRY PETG GF | PETG | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY PETG GF_1778039341 |
| X2D/0.4mm | TINMORRY PETG Galaxy.bbsflmt | TINMORRY PETG Galaxy | PETG | Bambu Lab X2D 0.4 nozzle | 02.07.01.51 | 3412907432_TINMORRY PETG Galaxy_1781058844 |
| X2D/0.4mm | TINMORRY PETG HS.bbsflmt* | TINMORRY PETG HS | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG HS_&lt;generated&gt; |
| X2D/0.4mm | TINMORRY PETG Marble.bbsflmt | TINMORRY PETG Marble | PETG | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY PETG Marble_1778039341 |
| X2D/0.4mm | TINMORRY PETG Metallic.bbsflmt | TINMORRY PETG Metallic | PETG | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY PETG Metallic_1778039341 |
| X2D/0.4mm | TINMORRY PETG Sparkly.bbsflmt | TINMORRY PETG Sparkly | PETG | Bambu Lab X2D 0.4 nozzle | 02.06.00.50 | 3412907432_TINMORRY PETG Sparkly_1777370656 |
| X2D/0.4mm | TINMORRY PLA CF.bbsflmt* | TINMORRY PLA CF | PLA-CF | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA CF_&lt;generated&gt; |
| X2D/0.4mm | TINMORRY PLA Galaxy.bbsflmt* | TINMORRY PLA Galaxy | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Galaxy_&lt;generated&gt; |
| X2D/0.4mm | TINMORRY PLA Silk.bbsflmt* | TINMORRY PLA Silk | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA Silk_&lt;generated&gt; |
| X2D/0.4mm | TINMORRY PLA matte.bbsflmt | TINMORRY PLA matte | PLA | Bambu Lab X2D 0.4 nozzle | 02.07.00.50 | 3412907432_TINMORRY PLA matte_1779247765 |
| X2D/0.4mm | TINMORRY TPU 95A.bbsflmt | TINMORRY TPU 95A | TPU | Bambu Lab P2S 0.4 nozzle + Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU 95A_1778039341 |
| X2D/0.4mm | TINMORRY TPU GF.bbsflmt* | TINMORRY TPU GF | TPU | Bambu Lab X2D 0.4 nozzle | 02.06.01.50 | 3412907432_TINMORRY TPU GF_&lt;generated&gt; |

\* Not an original TINMORRY export. Generated by `scripts/convert_old_repo_to_printer.py` from a filament type present in `reference-old-repo/` (a local, gitignored clone of TINMORRY's older per-printer profile repo -- see External references) that had no bundle for that printer yet. Machine-level parameters (temps, per-extruder-variant behavior) come from the closest existing bundle for that same printer (or, failing that, a repo-wide canonical template); material-specific tuning (flow ratio, plate temp, fan speed, max volumetric speed) comes from the old-repo profile. Generation is gated by a machine-compatibility policy -- see "Machine compatibility gating" in CLAUDE.md -- so materials without real evidence of working on a given printer (e.g. PA-CF/PAHT-CF almost everywhere, or any ABS/ASA/PC on the open-frame A1 mini/A2L) are deliberately skipped rather than guessed. **PA-CF and PAHT-CF's X2D bundles in particular did not have nozzle/bed temperature overrides in their source profile**, so they inherited PETG CF's temperature range (245-260 C) rather than PA-CF/PAHT-CF's typically higher real-world requirement (~270-300 C) -- verify against TINMORRY's spec sheet before printing with these two.

Generated by extracting and inspecting each `.bbsflmt` archive's `bundle_structure.json` and per-printer profile JSON in this repository (2026-07-02), updated after generalizing the conversion tooling to all printers (2026-07-02).

## Scripts

- `scripts/_filament_lib.py` — shared library: the printer registry, machine-compatibility tiers/gating policy, old-repo parsing, template selection, and bundle-merging logic used by both scripts below.
- `scripts/find_missing_filaments.py [--printer NAME]` — compares filament types in `reference-old-repo/` against what's already bundled for each printer folder and reports gaps, labeled ALLOW or SKIP per the compatibility policy.
- `scripts/convert_old_repo_to_printer.py [--printer NAME] [--dry-run]` — generates new `.bbsflmt` bundles for the ALLOW-labeled gaps. Never modifies an existing bundle, and every generated bundle's machine template traces back to a real, originally-existing bundle (never to another bundle generated earlier in the same run). Requires `reference-old-repo/` to be present locally (see External references to reclone it).
- `scripts/gen_inventory_table.py [--check]` — regenerates the "Full profile inventory" table above from the bundles actually on disk. Run after adding/removing any bundle.
- `scripts/unzip_wrapper_zips.py [--dry-run] [--delete-zip]` — finds plain `.zip` files that wrap a `.bbsflmt` bundle inside a subfolder (rather than being a bundle themselves) and extracts the inner `.bbsflmt` directly into the printer folder.

## External references

- [Bambu Studio (GitHub)](https://github.com/bambulab/BambuStudio) — the slicer these profiles are built for; its `resources/profiles` directory documents the same filament-setting schema used inside each bundle here.
- [TINMORRY-filament-profile-for-Bambu-printers (GitHub)](https://github.com/TINMORRY/TINMORRY-filament-profile-for-Bambu-printers.git) — TINMORRY's own upstream profile repo; useful for recovering profiles that are missing or older than what's tracked here. Clone it to `reference-old-repo/` (gitignored) to run the scripts above.
