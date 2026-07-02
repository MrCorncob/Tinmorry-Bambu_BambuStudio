#!/usr/bin/env python3
"""
Regenerate the "Available profiles" section in every README.*.md: one
collapsible, per-printer table with a direct raw-download link and an
Original/Derived tag for every .bbsflmt bundle, aimed at non-technical
users who just want to click a link rather than clone the repo.

Usage:
    python3 scripts/gen_readme_tables.py               # print all language blocks
    python3 scripts/gen_readme_tables.py --write        # splice into every README
    python3 scripts/gen_readme_tables.py --check         # exit 1 if any is stale

Splicing looks for the markers below (already present in every README) and
replaces everything between them -- keep the markers intact when hand-editing
anything else in the "Available profiles" section.

Adding a language: add a row to LANGS with the README filename, column
headers, and the (Original, Derived, link-text) labels.
"""
import argparse
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _filament_lib import INVENTORY_FOLDERS, REPO_ROOT, inventory_rows  # noqa: E402

GITHUB_OWNER = "MrCorncob"
GITHUB_REPO = "Tinmorry-Bambu_BambuStudio"
GITHUB_BRANCH = "refactor/X2D"

BEGIN = "<!-- BEGIN GENERATED PROFILE TABLES -->"
END = "<!-- END GENERATED PROFILE TABLES -->"

# One entry per language: README filename, (Filament, Source, Download)
# column headers, and (Original, Derived, link-text) labels.
LANGS = {
    "en": {
        "file": "README.md",
        "headers": ("Filament", "Source", "Download"),
        "labels": ("Original", "Derived", "download"),
    },
    "vi": {
        "file": "README.vi.md",
        "headers": ("Sợi in", "Nguồn gốc", "Tải xuống"),
        "labels": ("Nguyên bản", "Được tạo", "tải về"),
    },
    "zh": {
        "file": "README.zh.md",
        "headers": ("耗材", "来源", "下载"),
        "labels": ("原版", "衍生", "下载"),
    },
}

# Display name shown as each collapsible section's heading.
PRINTER_LABELS = {
    "A1": "Bambu Lab A1",
    "A1mini": "Bambu Lab A1 mini",
    "A2L": "Bambu Lab A2L",
    "H2C": "Bambu Lab H2C",
    "H2D": "Bambu Lab H2D",
    "H2S": "Bambu Lab H2S",
    "P1S": "Bambu Lab P1S",
    "P2S": "Bambu Lab P2S",
    "X2D/0.4mm": "Bambu Lab X2D",
}


def raw_url(folder: str, filename: str) -> str:
    path = f"{folder}/{filename}"
    encoded = urllib.parse.quote(path)
    return f"https://raw.githubusercontent.com/{GITHUB_OWNER}/{GITHUB_REPO}/{urllib.parse.quote(GITHUB_BRANCH, safe='')}/{encoded}"


def grouped_rows():
    rows = sorted(inventory_rows(), key=lambda r: (r["folder"], r["filament_name"]))
    by_folder = {folder: [] for folder in INVENTORY_FOLDERS}
    for r in rows:
        by_folder[r["folder"]].append(r)
    return by_folder


def render(lang: str) -> str:
    by_folder = grouped_rows()
    headers = LANGS[lang]["headers"]
    original_label, derived_label, link_label = LANGS[lang]["labels"]

    blocks = []
    for folder in INVENTORY_FOLDERS:
        rows = by_folder[folder]
        if not rows:
            continue
        summary = f"{PRINTER_LABELS[folder]} ({len(rows)})"
        lines = [
            "<details>",
            f"<summary><strong>{summary}</strong></summary>",
            "",
            f"| {headers[0]} | {headers[1]} | {headers[2]} |",
            "|---|---|---|",
        ]
        for r in rows:
            source = original_label if r["original"] else derived_label
            url = raw_url(folder, r["filename"])
            lines.append(f"| {r['filament_name']} | {source} | [{link_label}]({url}) |")
        lines.append("")
        lines.append("</details>")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def splice(path: Path, body: str) -> str:
    content = path.read_text()
    start = content.index(BEGIN)
    end = content.index(END) + len(END)
    return content[:start] + BEGIN + "\n\n" + body + "\n\n" + END + content[end:]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="splice the generated tables into every README")
    parser.add_argument("--check", action="store_true", help="exit 1 if any README's tables are stale")
    args = parser.parse_args()

    tables = {lang: render(lang) for lang in LANGS}

    if args.check:
        stale = []
        for lang, cfg in LANGS.items():
            path = REPO_ROOT / cfg["file"]
            if tables[lang] not in path.read_text():
                stale.append(cfg["file"])
        if stale:
            print(f"Stale profile tables in: {', '.join(stale)} -- run --write to regenerate.", file=sys.stderr)
            sys.exit(1)
        print(f"{', '.join(cfg['file'] for cfg in LANGS.values())} profile tables are up to date.")
        return

    if args.write:
        for lang, cfg in LANGS.items():
            path = REPO_ROOT / cfg["file"]
            path.write_text(splice(path, tables[lang]))
        print(f"Wrote {', '.join(cfg['file'] for cfg in LANGS.values())}.")
        return

    for lang, cfg in LANGS.items():
        print(f"=== {cfg['file']} ===")
        print(tables[lang])
        print()


if __name__ == "__main__":
    main()
