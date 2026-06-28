#!/usr/bin/env python3
"""FP-0002 V8 CF-010 pre-neutralization backup from working tree + SHA-256 guard."""
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
ZIP_NAME = "FP-0002-V8-BEFORE-CF-010-CLINIC-LANDSCAPE-NEUTRALIZATION.zip"
MANIFEST_LINE = "FP-0002 V8 CF-010 CLINIC LANDSCAPE PRE-NEUTRALIZATION CANONICAL STATE PRESERVED"

TARGET_FILES = [
    "src/partials/sections/home-clinic-landscape.html",
    "src/pages/index.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
    "src/scss/style.scss",
    "src/js/main.js",
    "src/img/content/pre-reviews/shpigovsky-clinic-landscape.webp",
]

REGISTRY_FILES = [
    "audits/shared-component-universalization/FP-0002-V8-SHARED-INCLUDE-REGISTRY-v1.md",
    "audits/shared-component-universalization/data/shared-include-registry-v1.json",
    "audits/shared-component-universalization/FP-0002-V8-UNIVERSALIZATION-ROADMAP-v1.md",
    "audits/component-family-audit-v8-bootstrap-01/FP-0002-V8-COMPONENT-FAMILY-REGISTRY-v1.md",
    "audits/consolidation-checkpoint/data/FP-0002-V8-PAGE-WIDE-DOM-VALIDATION.json",
    "foundation/FP-0002-V8-OPERATIONAL-STATUS.md",
    "audits/cf-010-clinic-landscape/CF-010-PRE-IMPLEMENTATION-INVENTORY.md",
    "audits/cf-010-clinic-landscape/data/CF-010-PRE-IMPLEMENTATION-INVENTORY.json",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_cmd(args: list[str]) -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), *args], text=True, stderr=subprocess.STDOUT
    ).strip()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = OUT_DIR / ZIP_NAME
    staging = OUT_DIR / "_cf010_backup_staging"
    if staging.exists():
        import shutil

        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    bundle_files: list[str] = []
    checksums: dict[str, str] = {}

    for rel in TARGET_FILES + REGISTRY_FILES:
        src = ROOT / rel
        if not src.exists():
            raise SystemExit(f"FP0002_V8_CF010_BACKUP_FAILED: missing {rel}")
        data = src.read_bytes()
        dest = staging / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        bundle_files.append(rel)
        checksums[rel] = sha256_bytes(data)

    git_status = git_cmd(["status", "--short"])
    git_diff_stat = git_cmd(["diff", "--stat"])
    (staging / "git-status-short.txt").write_text(git_status + "\n", encoding="utf-8")
    (staging / "git-diff-stat.txt").write_text(git_diff_stat + "\n", encoding="utf-8")
    bundle_files.extend(["git-status-short.txt", "git-diff-stat.txt"])

    manifest = {
        "manifest_line": MANIFEST_LINE,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "repository": str(REPO),
        "branch": git_cmd(["branch", "--show-current"]),
        "head": git_cmd(["rev-parse", "HEAD"]),
        "manual_polish_authority": "472be1abffb666a836eb83d5644e1fd3a233cc2d",
        "v8_workspace": str(ROOT),
        "source": "working tree snapshot (pre-CF-010 neutralization)",
        "files": bundle_files,
        "sha256": checksums,
        "restore_instructions": [
            "Extract ZIP to a temp folder.",
            "Copy listed src/ and audit files back into workspaces/fp-0002-shpigovsky-v8/ preserving paths only.",
            "Do NOT delete unrelated files; do NOT use mirror/purge/robocopy /MIR.",
            "Verify SHA-256 hashes against MANIFEST.json before restore.",
            "Source authority before CF-010: commit 472be1ab — do not roll back operator manual polish outside CF-010 selectors.",
            "Run npm run build in the V8 workspace to verify.",
        ],
    }
    (staging / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (staging / "RESTORE.md").write_text(
        "\n".join(
            [
                MANIFEST_LINE,
                "",
                f"Created: {manifest['created_utc']}",
                f"HEAD: {manifest['head']}",
                f"Manual polish authority: {manifest['manual_polish_authority']}",
                "",
                "## Restore",
                *manifest["restore_instructions"],
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    bundle_files.extend(["MANIFEST.json", "RESTORE.md"])

    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name in bundle_files:
            zf.write(staging / name, arcname=name)

    zip_sha = sha256_bytes(zip_path.read_bytes())
    (OUT_DIR / "FP-0002-V8-BEFORE-CF-010-CLINIC-LANDSCAPE-NEUTRALIZATION.sha256").write_text(
        f"{zip_sha}  {ZIP_NAME}\n", encoding="utf-8"
    )
    print(json.dumps({"zip": str(zip_path), "sha256": zip_sha, "files": len(bundle_files)}, indent=2))


if __name__ == "__main__":
    main()
