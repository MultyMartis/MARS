#!/usr/bin/env python3
"""FP-0002 V8 CF-003 completion backup before browser QA and commit."""
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
ZIP_NAME = "FP-0002-V8-BEFORE-CF-003-COMPLETION.zip"
MANIFEST_LINE = "FP-0002 V8 CF-003 IMPLEMENTATION PRESERVED BEFORE BROWSER QA AND COMMIT"

TARGET_FILES = [
    "src/pages/uslugi-v2.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
    "src/partials/components/internal-page-nav.html",
    "src/partials/components/breadcrumbs.html",
    "src/partials/components/services-page-subnav.html",
    "src/scss/style.scss",
]

AUDIT_FILES = [
    "audits/cf-003-upper-navigation/CF-003-IMPLEMENTATION-RECEIPT.md",
    "audits/cf-003-upper-navigation/CF-003-PRE-IMPLEMENTATION-INVENTORY.md",
    "audits/cf-003-upper-navigation/data/cf-003-pre-implementation-inventory.json",
    "audits/cf-003-upper-navigation/data/cf-003-source-hash-guard-pre.json",
    "audits/cf-003-upper-navigation/data/cf-003-source-hash-guard-post.json",
    "audits/bootstrap-reconciliation/CF-003-READINESS-RECEIPT.md",
    "audits/component-family-audit-v8-bootstrap-01/FP-0002-V8-COMPONENT-FAMILY-REGISTRY-v1.md",
    "plans/component-consolidation/FP-0002-V8-CONSOLIDATION-PLAN-v1.md",
]

TOOL_FILES = [
    "tools/component-consolidation/_cf003-pre-consolidation-backup.py",
    "tools/component-consolidation/_cf003-post-hash-guard.py",
    "tools/component-consolidation/_cf003-completion-backup.py",
    "tools/bootstrap-reconciliation/_browser-parity-capture.py",
    "tools/component-audit/_run-v8-component-family-audit.py",
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
    staging = OUT_DIR / "_cf003_completion_backup_staging"
    if staging.exists():
        import shutil

        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    bundle_files: list[str] = []
    checksums: dict[str, str] = {}

    for rel in TARGET_FILES + AUDIT_FILES + TOOL_FILES:
        src = ROOT / rel
        if not src.is_file():
            raise SystemExit(f"FP0002_V8_CF003_BACKUP_FAILED: missing {rel}")
        dest = staging / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(src.read_bytes())
        bundle_files.append(rel)
        checksums[rel] = sha256_file(src)

    git_status = git_cmd(["status", "--short"])
    git_diff_stat = git_cmd(["diff", "--stat"])
    git_diff_name = git_cmd(["diff", "--name-status"])
    (staging / "git-status-short.txt").write_text(git_status + "\n", encoding="utf-8")
    (staging / "git-diff-stat.txt").write_text(git_diff_stat + "\n", encoding="utf-8")
    (staging / "git-diff-name-status.txt").write_text(git_diff_name + "\n", encoding="utf-8")
    bundle_files.extend(
        ["git-status-short.txt", "git-diff-stat.txt", "git-diff-name-status.txt"]
    )

    manifest = {
        "manifest_line": MANIFEST_LINE,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "repository": str(REPO),
        "branch": git_cmd(["branch", "--show-current"]),
        "head": git_cmd(["rev-parse", "HEAD"]),
        "v8_workspace": str(ROOT),
        "v8_protected_baseline": "82af1b02daaeb6aa0bd0257270b94620f6dc6662",
        "files": bundle_files,
        "sha256": checksums,
        "restore_instructions": [
            "Extract ZIP to a temp folder.",
            "Copy listed src/ and audits/ files back into workspaces/fp-0002-shpigovsky-v8/ preserving paths.",
            "Run npm run build in the V8 workspace to verify.",
            "Re-run CF-003 browser QA if visual sign-off is required.",
        ],
    }
    (staging / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (staging / "RESTORE.md").write_text(
        "\n".join(
            [
                f"# {MANIFEST_LINE}",
                "",
                f"Created: {manifest['created_utc']}",
                f"HEAD: {manifest['head']}",
                f"Branch: {manifest['branch']}",
                "",
                "## Restore",
                "",
                *manifest["restore_instructions"],
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(staging.rglob("*")):
            if path.is_file():
                arc = path.relative_to(staging).as_posix()
                zf.write(path, arc)

    import shutil

    shutil.rmtree(staging)

    zip_sha = sha256_file(zip_path)
    result = {
        "zip": str(zip_path),
        "zip_sha256": zip_sha,
        "file_count": len(bundle_files),
        "manifest_line": MANIFEST_LINE,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
