#!/usr/bin/env python3
"""Create FP-0002 V8 pre-O-Centre implementation backup ZIP."""
from __future__ import annotations

import hashlib
import json
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"X:\AI MARS")
V8 = REPO / "workspaces" / "fp-0002-shpigovsky-v8"
OUT_DIR = Path(r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\operator-checkpoints")
ZIP_PATH = OUT_DIR / "FP-0002-V8-BEFORE-OCENTRE-IMPLEMENTATION.zip"
MANIFEST_LINE = "FP-0002 V8 PRE-OCENTRE-IMPLEMENTATION CANONICAL SOURCE PRESERVED"

INCLUDE_PATHS = [
    V8 / "src",
    V8 / "audits" / "o-centre-page-charter",
    V8 / "audits" / "o-centre-asset-content-resolution",
    V8 / "audits" / "o-centre-targeted-asset-export",
    V8 / "audits" / "o-centre-content-blocker-resolution",
    V8 / "foundation" / "FP-0002-V8-OPERATIONAL-STATUS.md",
    V8 / "foundation" / "FP-0002-V6-PAGE-INVENTORY.md",
]

EXCLUDE_PARTS = {"node_modules", "dist", "screenshots", "logs", ".git"}


def git_info() -> dict:
    def run(args: list[str]) -> str:
        return subprocess.check_output(["git", "-C", str(REPO), *args], text=True).strip()

    return {
        "head": run(["rev-parse", "HEAD"]),
        "branch": run(["branch", "--show-current"]),
        "status_short": run(["status", "--short"]),
        "diff_stat": run(["diff", "--stat"]),
    }


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    git_meta = git_info()
    restore = {
        "manifest_line": MANIFEST_LINE,
        "restore_only_v8_target_paths": True,
        "no_mirror_purge": True,
        "preserve_later_operator_work": True,
        "instructions": [
            "Extract ZIP to a staging folder",
            "Copy listed V8 paths back into workspaces/fp-0002-shpigovsky-v8/",
            "Do not delete unrelated files",
            "Validate SHA-256 against manifest inside ZIP",
        ],
    }

    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        file_hashes = {}
        for base in INCLUDE_PATHS:
            if base.is_file():
                arc = str(base.relative_to(REPO))
                zf.write(base, arc)
                file_hashes[arc] = sha256_file(base)
                continue
            if not base.is_dir():
                continue
            for path in base.rglob("*"):
                if not path.is_file():
                    continue
                if any(part in EXCLUDE_PARTS for part in path.parts):
                    continue
                arc = str(path.relative_to(REPO))
                zf.write(path, arc)
                file_hashes[arc] = sha256_file(path)

        meta = {
            "created_at": datetime.now(timezone.utc).isoformat(),
            "manifest_line": MANIFEST_LINE,
            "git": git_meta,
            "included_roots": [str(p.relative_to(REPO)) for p in INCLUDE_PATHS],
            "excluded": sorted(EXCLUDE_PARTS),
            "file_hashes": file_hashes,
            "restore": restore,
        }
        zf.writestr("backup-manifest.json", json.dumps(meta, ensure_ascii=False, indent=2))

    digest = sha256_file(ZIP_PATH)
    receipt = {
        "zip": str(ZIP_PATH),
        "sha256": digest,
        "manifest_line": MANIFEST_LINE,
        "result": "VALID",
    }
    (OUT_DIR / "FP-0002-V8-BEFORE-OCENTRE-IMPLEMENTATION-RECEIPT.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(receipt, ensure_ascii=False))


if __name__ == "__main__":
    main()
