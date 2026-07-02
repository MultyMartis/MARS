#!/usr/bin/env python3
"""Controlled local WPilot replacement from verified RC5 package."""
from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"X:\AI MARS")
LOCALHOST = Path(r"X:\MARS-Localhost")
STORAGE = Path(r"X:\AI MARS STORAGE")

PLUGIN_TARGET = (
    LOCALHOST
    / "sites"
    / "wordpress"
    / "projects"
    / "shpigovsky"
    / "wp-content"
    / "plugins"
    / "metacode-wpilot"
)
RC5_ZIP = STORAGE / "wpilot" / "deploy-packages" / "metacode-wpilot-v0.3.0-rc5.zip"
LOCAL_PKG_DIR = LOCALHOST / "storage" / "packages" / "wpilot"
LOCAL_PKG = LOCAL_PKG_DIR / "metacode-wpilot-v0.3.0-rc5.zip"
TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
CHECKPOINT_ROOT = (
    LOCALHOST
    / "backups"
    / "wordpress"
    / "projects"
    / "shpigovsky"
    / f"wpilot-pre-dev-runtime-reconciliation-{TS}"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dir_manifest(root: Path) -> dict:
    files = {}
    for path in sorted(root.rglob("*")):
        if path.is_file():
            rel = path.relative_to(root).as_posix()
            files[rel] = {
                "size": path.stat().st_size,
                "sha256": sha256_bytes(path.read_bytes()),
            }
    return files


def main() -> int:
    CHECKPOINT_ROOT.mkdir(parents=True, exist_ok=True)
    LOCAL_PKG_DIR.mkdir(parents=True, exist_ok=True)

    snapshot_dir = CHECKPOINT_ROOT / "plugin-snapshot"
    shutil.copytree(PLUGIN_TARGET, snapshot_dir)

    pre_manifest = {
        "checkpoint_root": str(CHECKPOINT_ROOT),
        "created_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "plugin_target": str(PLUGIN_TARGET),
        "pre_replace_file_count": len(dir_manifest(PLUGIN_TARGET)),
        "pre_replace_aggregate": sha256_bytes(
            "\n".join(
                f"{k}|{v['sha256']}"
                for k, v in sorted(dir_manifest(PLUGIN_TARGET).items())
            ).encode()
        ),
        "package_source": str(RC5_ZIP),
        "package_sha256": sha256_bytes(RC5_ZIP.read_bytes()),
        "build_id": "v0.3.0-rc5",
        "token_file_reference": str(REPO / "local" / "tokens" / "wpilot-local-shpigovsky.token"),
        "rollback": f"Stop WP if needed; delete {PLUGIN_TARGET}; copy {snapshot_dir} to {PLUGIN_TARGET}; reactivate plugin in wp-admin if required.",
        "files": dir_manifest(PLUGIN_TARGET),
    }
    (CHECKPOINT_ROOT / "pre-replace-manifest.json").write_text(
        json.dumps(pre_manifest, indent=2), encoding="utf-8"
    )

    if not LOCAL_PKG.exists():
        shutil.copy2(RC5_ZIP, LOCAL_PKG)

    # Classify unknown files before replacement
    with zipfile.ZipFile(RC5_ZIP) as zf:
        zip_rels = {
            n.split("/", 1)[1]
            for n in zf.namelist()
            if "/" in n and not n.endswith("/")
        }
    local_rels = set(dir_manifest(PLUGIN_TARGET))
    unknown_local_only = sorted(local_rels - zip_rels)
    missing_in_local = sorted(zip_rels - local_rels)

    # Bounded replacement: remove only files present in target, then extract zip
    for path in sorted(PLUGIN_TARGET.rglob("*"), reverse=True):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass

    with zipfile.ZipFile(RC5_ZIP) as zf:
        zf.extractall(PLUGIN_TARGET.parent)

    post_files = dir_manifest(PLUGIN_TARGET)
    post_agg = sha256_bytes(
        "\n".join(f"{k}|{v['sha256']}" for k, v in sorted(post_files.items())).encode()
    )

    with zipfile.ZipFile(RC5_ZIP) as zf:
        zip_manifest = {}
        for name in zf.namelist():
            if name.endswith("/"):
                continue
            rel = name.split("/", 1)[1]
            zip_manifest[rel] = sha256_bytes(zf.read(name))

    mismatches = [
        rel
        for rel, digest in zip_manifest.items()
        if post_files.get(rel, {}).get("sha256") != digest
    ]

    result = {
        "replaced_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "old_build": "v0.3.0-pre-ux01",
        "new_build": "v0.3.0-rc5",
        "files_replaced": len(post_files),
        "unknown_local_only_removed": unknown_local_only,
        "missing_before_replace": missing_in_local,
        "post_replace_aggregate": post_agg,
        "package_sha256": sha256_bytes(RC5_ZIP.read_bytes()),
        "hash_mismatches_after_copy": mismatches,
        "success": not mismatches and len(post_files) == len(zip_manifest),
    }
    (CHECKPOINT_ROOT / "replacement-result.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )
    print(json.dumps(result, indent=2))
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
