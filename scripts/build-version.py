#!/usr/bin/env python3
"""Regenerate version.json from the files this repo syncs.

Synced paths are INSTALL.md, README.md, LICENSE, and everything under
bot/, data/, kb/, skills/, and tests/. version.json does not hash itself.
scripts/ and .github/ are tooling, not knowledge, so they are omitted.

The script writes version.json only when the file map changes. A change
bumps the patch version (1.0.0 -> 1.0.1) and sets "updated" to today's UTC
date. An unchanged tree leaves the manifest untouched, so a second run
does not create a new commit.

Usage:
  python3 scripts/build-version.py
  python3 scripts/build-version.py --check
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "version.json"
SYNC_PATHS = (
    "INSTALL.md",
    "LICENSE",
    "README.md",
    "bot",
    "data",
    "kb",
    "skills",
    "tests",
)


def synced_files() -> list[Path]:
    found: list[Path] = []
    for rel in SYNC_PATHS:
        path = ROOT / rel
        if path.is_file():
            found.append(path)
        elif path.is_dir():
            found.extend(p for p in path.rglob("*") if p.is_file())
        else:
            print(f"missing synced path: {rel}", file=sys.stderr)
            sys.exit(2)
    return sorted(found, key=lambda p: p.relative_to(ROOT).as_posix())


def file_map(paths: list[Path]) -> dict[str, str]:
    mapped: dict[str, str] = {}
    for path in paths:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        mapped[path.relative_to(ROOT).as_posix()] = digest
    return mapped


def bump_patch(version: str) -> str:
    parts = version.split(".")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        return "1.0.0"
    major, minor, patch = (int(part) for part in parts)
    return f"{major}.{minor}.{patch + 1}"


def load_manifest() -> dict | None:
    if not MANIFEST.exists():
        return None
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def build(check: bool) -> int:
    current = file_map(synced_files())
    previous = load_manifest()
    if previous is not None and previous.get("files") == current:
        print(f"version.json is current ({previous.get('version')}, {len(current)} files)")
        return 0
    if check:
        print("version.json is stale", file=sys.stderr)
        return 1

    if previous is None:
        version = "1.0.0"
    else:
        version = bump_patch(str(previous.get("version", "1.0.0")))
    updated = datetime.now(timezone.utc).date().isoformat()
    document = {
        "version": version,
        "updated": updated,
        "files": current,
    }
    MANIFEST.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
    print(f"wrote version.json {version} ({updated}, {len(current)} files)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 when version.json does not match the synced files",
    )
    args = parser.parse_args()
    return build(check=args.check)


if __name__ == "__main__":
    sys.exit(main())
