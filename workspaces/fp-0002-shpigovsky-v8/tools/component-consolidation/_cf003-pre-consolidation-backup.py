#!/usr/bin/env python3
"""FP-0002 V8 CF-003 pre-consolidation backup + SHA-256 guard (pre-change)."""
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
ZIP_NAME = "FP-0002-V8-BEFORE-CF-003-UPPER-NAV-CONSOLIDATION.zip"
MANIFEST_LINE = "FP-0002 V8 CF-003 PRE-CONSOLIDATION STATE PRESERVED"

TARGET_FILES = [
    "src/pages/uslugi-v2.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
    "src/partials/components/breadcrumbs.html",
    "src/partials/components/services-page-subnav.html",
    "src/scss/style.scss",
]

EVIDENCE_FILES = [
    "audits/component-family-audit-v8-bootstrap-01/FP-0002-V8-COMPONENT-FAMILY-REGISTRY-v1.md",
    "audits/bootstrap-reconciliation/CF-003-READINESS-RECEIPT.md",
    "audits/component-family-audit-v8-bootstrap-01/FP-0002-V8-COMPONENT-FAMILY-AUDIT-v1.md",
    "plans/component-consolidation/FP-0002-V8-CONSOLIDATION-PLAN-v1.md",
]

PROTECTED_FILES = [
    "src/pages/index.html",
    "src/partials/layout/header.html",
    "src/partials/layout/footer.html",
    "src/partials/components/modal-consultation.html",
    "src/js/main.js",
    "src/partials/sections/services-inner-hero-v2.html",
    "src/partials/components/services-program-cta-band-v2.html",
    "src/partials/sections/services-program-v2.html",
    "src/partials/sections/home-specialists.html",
    "src/partials/sections/home-reviews.html",
    "src/partials/sections/home-final-form.html",
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
    staging = OUT_DIR / "_cf003_backup_staging"
    if staging.exists():
        import shutil

        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    bundle_files: list[str] = []
    checksums: dict[str, str] = {}

    for rel in TARGET_FILES + EVIDENCE_FILES:
        src = ROOT / rel
        if not src.is_file():
            raise SystemExit(f"FP0002_V8_CF003_BACKUP_FAILED: missing {rel}")
        dest = staging / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(src.read_bytes())
        bundle_files.append(rel)
        checksums[rel] = sha256_file(src)

    # git snapshot
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
        "files": bundle_files,
        "sha256": checksums,
        "restore_instructions": [
            "Extract ZIP to a temp folder.",
            "Copy listed src/ files back into workspaces/fp-0002-shpigovsky-v8/ preserving paths.",
            "Run npm run build in the V8 workspace to verify.",
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

    pre_hashes = {
        "phase": "pre-implementation",
        "target": {rel: sha256_file(ROOT / rel) for rel in TARGET_FILES},
        "protected": {rel: sha256_file(ROOT / rel) for rel in PROTECTED_FILES if (ROOT / rel).is_file()},
    }
    audit_dir = ROOT / "audits" / "cf-003-upper-navigation" / "data"
    audit_dir.mkdir(parents=True, exist_ok=True)
    (audit_dir / "cf-003-source-hash-guard-pre.json").write_text(
        json.dumps(pre_hashes, indent=2) + "\n", encoding="utf-8"
    )

    print(json.dumps({"zip": str(zip_path), "zip_sha256": sha256_file(zip_path), "pre_hashes": pre_hashes}, indent=2))


if __name__ == "__main__":
    main()
