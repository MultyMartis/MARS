#!/usr/bin/env python3
"""FP-0002 V8 CF-009 pre-universalization backup + SHA-256 guard (pre-change)."""
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
ZIP_NAME = "FP-0002-V8-BEFORE-CF-009-FINAL-FORM-UNIVERSALIZATION.zip"
MANIFEST_LINE = "FP-0002 V8 CF-009 FINAL FORM PRE-UNIVERSALIZATION STATE PRESERVED"

TARGET_FILES = [
    "src/partials/sections/home-final-form.html",
    "src/pages/index.html",
    "src/pages/uslugi.html",
    "src/pages/uslugi-v2.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
    "src/scss/style.scss",
    "src/js/main.js",
]

REGISTRY_FILES = [
    "audits/component-family-audit-v8-bootstrap-01/FP-0002-V8-COMPONENT-FAMILY-REGISTRY-v1.md",
    "audits/shared-component-universalization/FP-0002-V8-UNIVERSALIZATION-ROADMAP-v1.md",
    "foundation/FP-0002-V8-OPERATIONAL-STATUS.md",
]

PROTECTED_FILES = [
    "src/partials/components/internal-page-nav.html",
    "src/partials/sections/founder-quote.html",
    "src/partials/sections/specialists.html",
    "src/partials/sections/comfort.html",
    "src/partials/sections/reviews.html",
    "src/partials/sections/faq.html",
    "src/partials/layout/header.html",
    "src/partials/layout/footer.html",
    "src/partials/components/modal-consultation.html",
    "src/partials/sections/hero.html",
    "src/partials/sections/home-clinic-landscape.html",
    "src/partials/sections/home-gallery.html",
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
    staging = OUT_DIR / "_cf009_backup_staging"
    if staging.exists():
        import shutil

        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    bundle_files: list[str] = []
    checksums: dict[str, str] = {}

    for rel in TARGET_FILES + REGISTRY_FILES:
        src = ROOT / rel
        if not src.is_file():
            raise SystemExit(f"FP0002_V8_CF009_BACKUP_FAILED: missing {rel}")
        dest = staging / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(src.read_bytes())
        bundle_files.append(rel)
        checksums[rel] = sha256_file(src)

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
    }
    (staging / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
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
        "protected": {
            rel: sha256_file(ROOT / rel) for rel in PROTECTED_FILES if (ROOT / rel).is_file()
        },
    }
    audit_dir = ROOT / "audits" / "cf-009-final-form" / "data"
    audit_dir.mkdir(parents=True, exist_ok=True)
    (audit_dir / "cf-009-source-hash-guard-pre.json").write_text(
        json.dumps(pre_hashes, indent=2) + "\n", encoding="utf-8"
    )

    print(json.dumps({"zip": str(zip_path), "zip_sha256": sha256_file(zip_path)}, indent=2))


if __name__ == "__main__":
    main()
