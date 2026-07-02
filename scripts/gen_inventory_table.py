#!/usr/bin/env python3
"""
Regenerate the "Full profile inventory" markdown table in REFERENCES.md
from the actual .bbsflmt bundles on disk. Run this after adding/removing
any bundle so the table doesn't drift from reality.

Usage:
    python3 scripts/gen_inventory_table.py            # print the table
    python3 scripts/gen_inventory_table.py --check    # exit 1 if REFERENCES.md is stale
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _filament_lib import REPO_ROOT, inventory_rows  # noqa: E402

REFERENCES_MD = REPO_ROOT / "REFERENCES.md"


def build_table():
    rows = sorted(inventory_rows(), key=lambda r: (r["folder"], r["filename"]))

    lines = ["| Folder | File | Filament | Type | Compatible printer | Studio version | Bundle id |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        mark = "" if r["original"] else "*"
        bundle_id = r["bundle_id"] if r["original"] else re.sub(r"_\d+$", "_&lt;generated&gt;", r["bundle_id"])
        lines.append(f"| {r['folder']} | {r['filename']}{mark} | {r['filament_name']} | {r['type']} | "
                      f"{' + '.join(r['printers'])} | {r['version']} | {bundle_id} |")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit 1 if REFERENCES.md's table is stale")
    args = parser.parse_args()

    table = build_table()
    if args.check:
        content = REFERENCES_MD.read_text()
        if table not in content:
            print("REFERENCES.md inventory table is stale -- run without --check and paste it in.", file=sys.stderr)
            sys.exit(1)
        print("REFERENCES.md inventory table is up to date.")
    else:
        print(table)


if __name__ == "__main__":
    main()
