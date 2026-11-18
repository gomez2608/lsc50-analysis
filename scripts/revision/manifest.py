"""Manifest of data and result files (path, size, MD5, modification time).

Walks one or more directories and prints a Markdown table, so the register
records exactly which inputs and outputs exist where. Directories that hold
model weights, checkpoints or Arrow shards are summarized (file count and total
size) instead of listed file by file.

Usage:
    python scripts/revision/manifest.py --root WORK --label "Mac WORK" > manifest_mac.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
from pathlib import Path

BULK_DIR_MARKERS = ("checkpoint-", "clips_all")
BULK_SUFFIXES = (".arrow", ".safetensors", ".bin", ".pt", ".pth")
SKIP = {"__pycache__", ".ipynb_checkpoints"}


def md5(path: Path, chunk: int = 1 << 22) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def human(n: float) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", required=True)
    parser.add_argument("--label", required=True)
    parser.add_argument("--exclude", nargs="*", default=[], help="Top-level entries to skip.")
    args = parser.parse_args()
    root = Path(args.root)

    files, bulk = [], {}
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = Path(dirpath).relative_to(root)
        if rel_dir.parts and rel_dir.parts[0] in args.exclude:
            dirnames[:] = []
            continue
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP)
        for name in sorted(filenames):
            p = Path(dirpath) / name
            rel = p.relative_to(root)
            parts = rel.parts
            bulk_key = next((str(Path(*parts[: i + 1])) for i, part in enumerate(parts[:-1])
                             if part.startswith(BULK_DIR_MARKERS)), None)
            if bulk_key is None and name.endswith(BULK_SUFFIXES):
                bulk_key = str(rel.parent / f"*{p.suffix}")
            if bulk_key is not None:
                n, size = bulk.get(bulk_key, (0, 0))
                bulk[bulk_key] = (n + 1, size + p.stat().st_size)
                continue
            st = p.stat()
            files.append((str(rel), st.st_size, md5(p), dt.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M")))

    print(f"### {args.label}: `{root}`\n")
    print(f"Generated {dt.datetime.now():%Y-%m-%d %H:%M}. {len(files)} files listed; {len(bulk)} bulk groups summarized.\n")
    print("| File | Size | MD5 | Modified |")
    print("|------|------|-----|----------|")
    for rel, size, digest, mtime in files:
        print(f"| `{rel}` | {human(size)} | `{digest}` | {mtime} |")
    if bulk:
        print("\n| Bulk group (weights, checkpoints, Arrow shards) | Files | Total size |")
        print("|-----------------------------------------------|-------|------------|")
        for key, (n, size) in sorted(bulk.items()):
            print(f"| `{key}` | {n} | {human(size)} |")
    print()


if __name__ == "__main__":
    main()
