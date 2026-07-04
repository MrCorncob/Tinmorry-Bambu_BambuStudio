# Diff Report: TINMORRY PETG Matte (X2D)

**Comparing:**
- **Source:** `reference-bambuprinters/PETG_Matte_Filament(X2D-TinmorryBinhDuong).json` (TinmorryBinhDuong's BambuPrinters export)
- **Generated bundle:** `X2D/0.4mm/TINMORRY PETG Matte.bbsflmt` (produced by `scripts/convert_old_repo_to_printer.py`)

**Date generated:** 2026-07-04

---

## Summary

| Metric | Count |
|---|---|
| Total keys (both files) | 147 |
| Keys only in source | 0 |
| Keys only in generated bundle | 0 |
| Identical keys | 140 |
| Differing keys | 7 |

The key sets match exactly, and **140 of 147 keys are byte-identical** — all real material tuning (nozzle/plate temps, fan speeds, flow ratio, max volumetric speed, retraction, cooling curve, pressure advance, etc.) passed through from the source unchanged.

---

## The 7 differing keys

| Key | Source (BambuPrinters) | Generated bundle | Reason |
|---|---|---|---|
| `name` | `PETG Matte(X2D-TinmorryBinhDuong)` | `TINMORRY PETG Matte @Bambu Lab X2D 0.4 nozzle` | Renamed to this repo's naming convention (`build_bundle`) |
| `filament_settings_id` | `['PETG Matte(X2D-TinmorryBinhDuong)']` | `['TINMORRY PETG Matte']` | Same — repo's display-name convention |
| `filament_id` | `P0806e7b` | `Pf913838` | Regenerated via `make_filament_id` (hashes printer dir + name so it can't collide across printer folders) |
| `filament_vendor` | `['Tinmorry']` | `['TINMORRY']` | Casing normalized, set explicitly in `build_bundle` |
| `version` | `2.7.0.8` | `2.6.0.2` | Comes from the **template** bundle (X2D PETG CF), not the delta — `version` is in `SKIP_KEYS`, deliberately not copied from source |
| `filament_dev_ams_drying_temperature` | `['65', '65', '55', '55']` | `['65', '65', '65', '65']` | ⚠️ See fidelity note below |
| `retraction_distances_when_ec` | `['3', '3', '4', '4']` | `['3', '3', '3', '3']` | ⚠️ See fidelity note below |

The first five are expected, intentional identity/bookkeeping normalization — not a data-fidelity concern.

---

## ⚠️ Fidelity note: per-variant mirroring collapses distinct Bowden values

Both `filament_dev_ams_drying_temperature` and `retraction_distances_when_ec` are per-extruder-variant arrays over:

```
[Direct Drive Standard, Direct Drive High Flow, Bowden Standard, Bowden High Flow]
```

The **source** specifies genuinely different values for the Bowden slots than for Direct Drive:

| Variant | Drying temp (source) | Retraction distance (source) |
|---|---|---|
| Direct Drive Standard | 65°C | 3mm |
| Direct Drive High Flow | 65°C | 3mm |
| Bowden Standard | **55°C** | **4mm** |
| Bowden High Flow | **55°C** | **4mm** |

`_filament_lib.merge_profile`'s per-variant merge convention — documented in this repo's CLAUDE.md as "consistently mirror the Direct Drive High Flow value into both Bowden slots" — overwrote the source's distinct Bowden-specific values with the Direct Drive High Flow value for both fields. This is consistent with how every other bundle in this repo is built (a deliberate, repo-wide convention, not a one-off bug), but it means this specific generated bundle is measurably less accurate for **Bowden-extruder X2D setups** than the original BambuPrinters export:

- AMS drying temperature overstated by **10°C** (65°C vs. the source's real 55°C for Bowden)
- Retraction distance understated by **1mm** (3mm vs. the source's real 4mm for Bowden)

**Recommendation:** if this matters for real prints on a Bowden-extruder X2D, this is exactly the kind of correction the repo's new custom-override mechanism (`scripts/custom_overrides/X2D/0.4mm/TINMORRY PETG Matte.json`) was built for — it can force the correct per-slot values without changing the generic merge convention used by every other bundle.

---

## Everything else (140 identical keys)

Includes, non-exhaustively: `filament_type`, `compatible_printers`, `nozzle_temperature`, `nozzle_temperature_initial_layer`, `hot_plate_temp`, `cool_plate_temp`, `eng_plate_temp`, `fan_min_speed`, `fan_max_speed`, `filament_flow_ratio`, `filament_max_volumetric_speed`, `filament_density`, `filament_diameter`, `filament_cost`, `pressure_advance`, `chamber_temperatures`, `filament_scarf_*`, `filament_z_hop*`, `filament_start_gcode`, `filament_end_gcode`, and all other cooling/overhang/tower-related settings — an exact pass-through of the BambuPrinters source.
