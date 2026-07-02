#!/usr/bin/env python3
"""
Compare filament types present in reference-old-repo/ (TINMORRY's older,
per-printer-delta filament profiles) against what's already bundled for
X2D/0.4mm/ in this repo, and report old-repo filament types that have no
X2D equivalent yet.

Usage:
    python3 scripts/find_missing_x2d_filaments.py

Matching is a best-effort "bag of words" comparison (order- and
punctuation-insensitive) between:
  - the base material extracted from each old-repo profile's "inherits"
    field (e.g. "Generic PETG-CF @BBL H2C 0.4 nozzle" -> "petg cf")
  - descriptive words pulled from the old-repo filename (e.g. "Marble",
    "Galaxy", "Sparkly", "Matte", "Metallic", "Silk", "95A", "HS", "pro")
against the existing X2D bundle filament_name strings (e.g.
"TINMORRY PETG Marble" -> "petg marble").

This is a fuzzy classification aid, not a guarantee -- always eyeball the
"UNMATCHED" section before treating it as the authoritative gap list.
"""
import json
import re
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OLD_REPO_DIR = REPO_ROOT / "reference-old-repo"
X2D_DIR = REPO_ROOT / "X2D" / "0.4mm"

# Printer model tokens that show up in old-repo filenames/inherits and
# should be dropped when deriving a filament's descriptive name.
PRINTER_TOKENS = {
    "a1", "a1m", "a1mini", "p1p", "p1s", "p2s", "x1", "x1c", "x1e",
    "h2c", "h2d", "h2s", "bbl", "bambu", "tinmorry", "nozzle", "0.4",
}

# Words that describe *lineage* rather than the product itself. Kept out of
# the token set used for matching (so "Generic ASA" still matches "ASA
# basic"), but the raw inherits string is still printed for context.
NOISE_WORDS = {"generic", "bambu"}


def normalize(text: str, drop_noise: bool = True) -> set:
    """Lowercase, strip punctuation, drop printer/vendor noise tokens."""
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    stop = PRINTER_TOKENS | (NOISE_WORDS if drop_noise else set())
    return {t for t in tokens if t not in stop}


def old_repo_entries():
    """Yield (filename, inherits, descriptor_tokens, base_material_tokens)."""
    for path in sorted(OLD_REPO_DIR.glob("*.json")):
        data = json.loads(path.read_text())
        inherits = data.get("inherits", "") or ""
        base_material = normalize(inherits.split("@")[0])
        # Strip the parenthesized printer suffix, e.g. "PC-GF(X1C-...)" -> "PC-GF"
        descriptor_part = re.sub(r"\(.*", "", path.stem)
        descriptor = normalize(descriptor_part) - base_material
        yield path.name, inherits, descriptor, base_material


def x2d_bundle_labels():
    labels = []
    for path in sorted(X2D_DIR.glob("*.bbsflmt")):
        with zipfile.ZipFile(path) as z:
            bundle = json.loads(z.read("bundle_structure.json"))
        name = bundle["filament_name"]
        labels.append((path.name, name, normalize(name)))
    return labels


def main():
    x2d_labels = x2d_bundle_labels()

    print("=== Existing X2D/0.4mm bundles ===")
    for fname, name, tokens in x2d_labels:
        print(f"  {name:28s} {sorted(tokens)}")

    print("\n=== Old-repo filament profiles grouped by (base material, descriptor) ===")
    groups = {}
    for fname, inherits, descriptor, base_material in old_repo_entries():
        key = (frozenset(base_material), frozenset(descriptor))
        groups.setdefault(key, []).append(fname)

    unmatched = []
    for (base_material, descriptor), files in sorted(groups.items(), key=lambda kv: sorted(kv[0][0] | kv[0][1])):
        combined = set(base_material) | set(descriptor)
        match = None
        for fname, name, tokens in x2d_labels:
            # Consider it matched if the material+descriptor tokens are a
            # subset of the bundle's tokens, or vice versa, with at least
            # one non-generic descriptor word in common when present.
            if combined and (combined <= tokens or tokens <= combined):
                match = name
                break
        status = f"MATCHES: {match}" if match else "UNMATCHED (no X2D bundle yet)"
        label = " ".join(sorted(descriptor)) or " ".join(sorted(base_material))
        print(f"  [{' '.join(sorted(base_material)):15s}] {label:20s} -> {status}")
        print(f"      source files: {', '.join(files)}")
        if not match:
            unmatched.append((base_material, descriptor, files))

    print("\n=== SUMMARY: old-repo filament types with no X2D bundle yet ===")
    for base_material, descriptor, files in unmatched:
        label = " ".join(sorted(set(base_material) | set(descriptor)))
        print(f"  - {label}  (from: {', '.join(files)})")


if __name__ == "__main__":
    main()
