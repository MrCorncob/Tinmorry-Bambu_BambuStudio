#!/usr/bin/env python3
"""
Find plain .zip files that wrap a .bbsflmt bundle (rather than being a
bundle themselves -- see README.md "Known quirks") and extract the inner
.bbsflmt file(s) directly into the same printer folder, flattening away
the wrapper's own subfolder.

Usage:
    python3 scripts/unzip_wrapper_zips.py             # extract, keep the .zip
    python3 scripts/unzip_wrapper_zips.py --delete-zip # extract, then remove the .zip
    python3 scripts/unzip_wrapper_zips.py --dry-run    # preview only
"""
import argparse
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PRINTER_DIRS = ["A1mini", "A2L", "H2C", "H2D", "H2S", "P2S", "X2D"]


def find_wrapper_zips():
    for d in PRINTER_DIRS:
        for path in sorted((REPO_ROOT / d).rglob("*.zip")):
            yield path


def extract(zip_path: Path, dry_run: bool, delete_zip: bool):
    with zipfile.ZipFile(zip_path) as z:
        bbsflmt_members = [n for n in z.namelist() if n.endswith(".bbsflmt")]
        if not bbsflmt_members:
            print(f"  skip {zip_path.relative_to(REPO_ROOT)}: no .bbsflmt inside")
            return
        for member in bbsflmt_members:
            out_name = Path(member).name  # drop the wrapper's subfolder
            out_path = zip_path.parent / out_name
            action = "overwrite" if out_path.exists() else "extract"
            print(f"  {'[dry-run] ' if dry_run else ''}{action}: {zip_path.relative_to(REPO_ROOT)} "
                  f"-> {out_path.relative_to(REPO_ROOT)}")
            if dry_run:
                continue
            out_path.write_bytes(z.read(member))
    if delete_zip and not dry_run:
        print(f"  delete: {zip_path.relative_to(REPO_ROOT)}")
        zip_path.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="preview without writing files")
    parser.add_argument("--delete-zip", action="store_true", help="remove the wrapper .zip after extracting")
    args = parser.parse_args()

    zips = list(find_wrapper_zips())
    if not zips:
        print("No wrapper .zip files found.")
        return
    for zip_path in zips:
        extract(zip_path, args.dry_run, args.delete_zip)


if __name__ == "__main__":
    main()
