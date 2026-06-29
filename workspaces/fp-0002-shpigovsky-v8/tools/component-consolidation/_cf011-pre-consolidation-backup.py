#!/usr/bin/env python3
"""FP-0002 V8 CF-011 pre-consolidation backup from git HEAD + SHA-256 guard."""
from __future__ import annotations

import hashlib
import json
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
STORAGE = Path(r"X:\AI MARS STORAGE")
OUT_DIR = STORAGE / "website-factory" / "fp-0002-shpigovsky-v8" / "operator-checkpoints"
ZIP_NAME = "FP-0002-V8-BEFORE-CF-011-DARK-CTA-CONSOLIDATION.zip"
MANIFEST_LINE = "FP-0002 V8 CF-011 DARK CTA PRE-CONSOLIDATION STATE PRESERVED"

TARGET_FILES = [
    "src/partials/components/services-program-cta-band-v2.html",
    "src/partials/sections/service-subdivision-first-cta-v1.html",
    "src/partials/sections/service-subdivision-second-cta-v1.html",
    "src/partials/sections/service-leaf-cta-01-v1.html",
    "src/pages/uslugi-v2.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
    "src/partials/sections/services-program-v2.html",
    "src/partials/sections/service-subdivision-stages-v1.html",
    "src/partials/sections/service-leaf-stages-v1.html",
    "src/scss/style.scss",
    "src/js/main.js",
]

REGISTRY_FILES = [
    "audits/shared-component-universalization/FP-0002-V8-SHARED-INCLUDE-REGISTRY-v1.md",
    "audits/shared-component-universalization/data/shared-include-registry-v1.json",
    "audits/shared-component-universalization/FP-0002-V8-UNIVERSALIZATION-ROADMAP-v1.md",
    "audits/consolidation-checkpoint/data/FP-0002-V8-PAGE-WIDE-DOM-VALIDATION.json",
    "foundation/FP-0002-V8-OPERATIONAL-STATUS.md",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_cmd(args: list[str]) -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), *args], text=True, stderr=subprocess.STDOUT
    ).strip()


def git_file_at_head(rel: str) -> bytes:
    path = f"workspaces/fp-0002-shpigovsky-v8/{rel}"
    return subprocess.check_output(["git", "-C", str(REPO), "show", f"HEAD:{path}"])


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = OUT_DIR / ZIP_NAME
    staging = OUT_DIR / "_cf011_backup_staging"
    if staging.exists():
        import shutil

        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    bundle_files: list[str] = []
    checksums: dict[str, str] = {}

    for rel in TARGET_FILES + REGISTRY_FILES:
        try:
            data = git_file_at_head(rel)
        except subprocess.CalledProcessError as exc:
            raise SystemExit(f"FP0002_V8_CF011_BACKUP_FAILED: missing {rel}: {exc}") from exc
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
        "v8_workspace": str(ROOT),
        "source": "git HEAD snapshot (pre-CF-011 implementation)",
        "files": bundle_files,
        "sha256": checksums,
        "restore_instructions": [
            "Extract ZIP to a temp folder.",
            "Copy listed src/ and audit files back into workspaces/fp-0002-shpigovsky-v8/ preserving paths.",
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
    (OUT_DIR / "FP-0002-V8-BEFORE-CF-011-DARK-CTA-CONSOLIDATION.sha256").write_text(
        f"{zip_sha}  {ZIP_NAME}\n", encoding="utf-8"
    )
    print(json.dumps({"zip": str(zip_path), "sha256": zip_sha, "files": len(bundle_files)}, indent=2))


if __name__ == "__main__":
    main()
