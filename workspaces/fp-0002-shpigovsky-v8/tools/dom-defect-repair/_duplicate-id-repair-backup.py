#!/usr/bin/env python3
"""FP-0002 V8 treatment-prevention duplicate ID pre-repair backup."""
from __future__ import annotations

import hashlib
import json
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
STORAGE = Path(r"C:\MARS Phenix\AI MARS STORAGE")
OUT_DIR = STORAGE / "website-factory" / "fp-0002-shpigovsky-v8" / "operator-checkpoints"
ZIP_NAME = "FP-0002-V8-BEFORE-TREATMENT-PREVENTION-DUPLICATE-ID-REPAIR.zip"
MANIFEST_LINE = "FP-0002 V8 TREATMENT PREVENTION DUPLICATE ID PRE-REPAIR STATE PRESERVED"

TARGET_FILES = [
    "src/partials/sections/home-why-us.html",
    "src/partials/sections/home-treatment-prevention.html",
    "src/pages/index.html",
    "src/scss/style.scss",
    "src/js/main.js",
    "audits/dom-defect-repair/FP-0002-V8-DUPLICATE-ID-ROOT-CAUSE-v1.md",
    "foundation/FP-0002-V8-OPERATIONAL-STATUS.md",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git_cmd(args: list[str]) -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), *args], text=True, stderr=subprocess.STDOUT
    ).strip()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = OUT_DIR / ZIP_NAME
    staging = OUT_DIR / "_duplicate_id_repair_staging"
    if staging.exists():
        import shutil

        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    checksums: dict[str, str] = {}
    bundle_files: list[str] = []
    for rel in TARGET_FILES:
        src = ROOT / rel
        if not src.is_file():
            raise SystemExit(f"FP0002_V8_DUPLICATE_ID_REPAIR_BACKUP_FAILED: missing {rel}")
        dest = staging / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(src.read_bytes())
        bundle_files.append(rel)
        checksums[rel] = sha256_file(src)

    git_status = git_cmd(["status", "--short"])
    git_diff = git_cmd(["diff", "--stat"])
    (staging / "git-status-short.txt").write_text(git_status + "\n", encoding="utf-8")
    (staging / "git-diff-stat.txt").write_text(git_diff + "\n", encoding="utf-8")
    bundle_files.extend(["git-status-short.txt", "git-diff-stat.txt"])

    manifest = {
        "manifest_line": MANIFEST_LINE,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "repository": str(REPO),
        "branch": git_cmd(["branch", "--show-current"]),
        "head": git_cmd(["rev-parse", "HEAD"]),
        "v8_workspace": str(ROOT),
        "restore_instructions": [
            "Extract ZIP preserving paths relative to workspaces/fp-0002-shpigovsky-v8/",
            "Verify each file SHA-256 against manifest.sha256 before overwrite",
            "Run npm run build from v8 workspace and re-check dist/index.html duplicate IDs",
        ],
        "files": bundle_files,
        "sha256": checksums,
    }
    (staging / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(staging.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(staging).as_posix())

    import shutil

    shutil.rmtree(staging)
    print(json.dumps({"zip": str(zip_path), "zip_sha256": sha256_file(zip_path)}, indent=2))


if __name__ == "__main__":
    main()
