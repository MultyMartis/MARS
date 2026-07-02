#!/usr/bin/env python3
"""FP-0002 V8 pre O-Centre content blocker resolution backup."""
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
ZIP_NAME = "FP-0002-V8-BEFORE-OCENTRE-CONTENT-BLOCKER-RESOLUTION.zip"
MANIFEST_LINE = "FP-0002 V8 O-CENTRE PRE-CONTENT-BLOCKER-RESOLUTION STATE PRESERVED"

CHARTER_PACK = [
    "audits/o-centre-page-charter/FP-0002-V8-OCENTRE-PAGE-ANATOMY-REUSE-CHARTER-v1.md",
    "audits/o-centre-page-charter/data/FP-0002-V8-OCENTRE-PAGE-ANATOMY-REUSE-CHARTER.json",
    "audits/o-centre-page-charter/FP-0002-V8-OCENTRE-PAGE-ANATOMY-v1.md",
    "audits/o-centre-page-charter/FP-0002-V8-OCENTRE-COMPOSITION-MAP-v1.md",
    "audits/o-centre-page-charter/FP-0002-V8-OCENTRE-CONTENT-INVENTORY-v1.md",
]

RESOLUTION_PACK = [
    "audits/o-centre-asset-content-resolution/FP-0002-V8-OCENTRE-GAP-REGISTER-v1.md",
    "audits/o-centre-asset-content-resolution/FP-0002-V8-OCENTRE-RESOLVED-CONTENT-PACK-v1.md",
    "audits/o-centre-asset-content-resolution/FP-0002-V8-OCENTRE-RESOLVED-COMPOSITION-v1.md",
    "audits/o-centre-asset-content-resolution/FP-0002-V8-OCENTRE-PREIMPLEMENTATION-READINESS-v1.md",
    "audits/o-centre-asset-content-resolution/data/FP-0002-V8-OCENTRE-IMPLEMENTATION-CONTENT.json",
    "audits/o-centre-asset-content-resolution/data/FP-0002-V8-OCENTRE-RESOLVED-CONTENT-PACK.json",
    "audits/o-centre-asset-content-resolution/data/FP-0002-V8-OCENTRE-FIGMA-NODE-MAP.json",
]

TARGETED_EXPORT = [
    "audits/o-centre-targeted-asset-export/FP-0002-V8-OCENTRE-INFRASTRUCTURE-ASSET-MANIFEST-v1.md",
    "audits/o-centre-targeted-asset-export/data/FP-0002-V8-OCENTRE-INFRASTRUCTURE-ASSET-MANIFEST.json",
]

INVENTORY_STATUS = [
    "foundation/FP-0002-V6-PAGE-INVENTORY.md",
    "../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-BLOCK-INVENTORY-v1.md",
    "../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PAGE-INVENTORY-v1.md",
    "foundation/FP-0002-V8-OPERATIONAL-STATUS.md",
    "../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-WORKSPACE-STATUS-v1.md",
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
    staging = OUT_DIR / "_ocentre_content_blocker_backup_staging"
    if staging.exists():
        import shutil

        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    bundle_files: list[str] = []
    checksums: dict[str, str] = {}

    all_rels = CHARTER_PACK + RESOLUTION_PACK + TARGETED_EXPORT + INVENTORY_STATUS
    for rel in all_rels:
        if rel.startswith("../"):
            src = (ROOT / rel).resolve()
            arc = rel.replace("../", "external/")
        else:
            src = ROOT / rel
            arc = rel
        if not src.is_file():
            raise SystemExit(f"FP0002_V8_OCENTRE_CONTENT_BACKUP_FAILED: missing {rel}")
        dest = staging / arc
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(src.read_bytes())
        bundle_files.append(arc)
        checksums[arc] = sha256_file(src)

    for name, content in [
        ("git-status-short.txt", git_cmd(["status", "--short"])),
        ("git-diff-stat.txt", git_cmd(["diff", "--stat"])),
        ("git-head.txt", git_cmd(["rev-parse", "HEAD"])),
        ("git-branch.txt", git_cmd(["branch", "--show-current"])),
    ]:
        (staging / name).write_text(content + "\n", encoding="utf-8")
        bundle_files.append(name)

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
            "Copy audits/ and foundation/ files back into workspaces/fp-0002-shpigovsky-v8/ preserving paths.",
            "Copy external/website-factory-operations/ files back to workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/ if needed.",
            "Do not restore src/, assets/, or Figma from this checkpoint.",
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
                zf.write(path, path.relative_to(staging).as_posix())

    import shutil

    shutil.rmtree(staging)

    result = {
        "zip": str(zip_path),
        "zip_sha256": sha256_file(zip_path),
        "manifest_line": MANIFEST_LINE,
        "valid": zip_path.exists() and zip_path.stat().st_size > 0,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
