#!/usr/bin/env python3
"""M9.8.9-06M — effective price hotfix: capture, backup, patch, deploy."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"
REMOTE_PATH = "catalog/model/catalog/product.php"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002")
WORK_DIR = ROOT / "reports" / "m9.8.9-06m-work"
CAPTURE_DIR = WORK_DIR / "live-capture"
CAPTURE_PATH = CAPTURE_DIR / "catalog__model__catalog__product.php"
BACKUP_PATH = ROOT / "backups" / "product.php.pre-m9.8.9-06m-effective-price.bak"
PATCHED_PATH = WORK_DIR / "catalog__model__catalog__product.php.patched"

OLD_EXPR = "IFNULL(ppi.special, ppi.price)"
NEW_EXPR = "IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path: str) -> bytes:
    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def apply_patch(content: str) -> tuple[str, int]:
    count = content.count(OLD_EXPR)
    if count != 3:
        raise RuntimeError(f"Expected 3 occurrences of {OLD_EXPR!r}, found {count}")
    return content.replace(OLD_EXPR, NEW_EXPR), count


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    CAPTURE_DIR.mkdir(parents=True, exist_ok=True)
    ROOT.joinpath("backups").mkdir(parents=True, exist_ok=True)

    # 1. FTP capture
    live_raw = ftp_download(REMOTE_PATH)
    live_sha = sha256_hex(live_raw)
    CAPTURE_PATH.write_bytes(live_raw)

    # 2. Backup
    BACKUP_PATH.write_bytes(live_raw)

    # 3. Patch
    live_text = live_raw.decode("utf-8")
    patched_text, replacements = apply_patch(live_text)
    patched_raw = patched_text.encode("utf-8")
    patched_sha = sha256_hex(patched_raw)
    PATCHED_PATH.write_bytes(patched_raw)

    # 4. Manifest (pre-deploy)
    manifest_pre = {
        "task": "M9.8.9-06M",
        "authority": "SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01",
        "basis": ["M9.8.9-06K", "M9.8.9-06L"],
        "stamp": stamp,
        "remote_path": REMOTE_PATH,
        "phase": "pre-deploy",
        "capture": str(CAPTURE_PATH),
        "backup": str(BACKUP_PATH),
        "sha256": live_sha,
        "size": len(live_raw),
        "patch": {
            "old": OLD_EXPR,
            "new": NEW_EXPR,
            "replacements": replacements,
            "locations": [
                "getProducts() $effective_price",
                "getProducts() ORDER BY p.price",
                "getTotalProducts() $effective_price",
            ],
        },
    }
    manifest_pre_path = WORK_DIR / f"manifest-pre-{stamp}.json"
    manifest_pre_path.write_text(
        json.dumps(manifest_pre, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # 5. Deploy
    ftp_upload(REMOTE_PATH, patched_raw)

    # 6. Verify SHA256 on live
    verify_raw = ftp_download(REMOTE_PATH)
    verify_sha = sha256_hex(verify_raw)

    manifest_post = {
        **manifest_pre,
        "phase": "post-deploy",
        "patched_local": str(PATCHED_PATH),
        "patched_sha256": patched_sha,
        "post_deploy_verify_sha256": verify_sha,
        "deploy_ok": verify_sha == patched_sha,
        "rollback_sha256": live_sha,
        "rollback_file": str(BACKUP_PATH),
    }
    manifest_post_path = WORK_DIR / f"manifest-{stamp}.json"
    manifest_post_path.write_text(
        json.dumps(manifest_post, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    result = {
        "manifest_pre": str(manifest_pre_path),
        "manifest_post": str(manifest_post_path),
        "pre_sha256": live_sha,
        "patched_sha256": patched_sha,
        "post_deploy_verify_sha256": verify_sha,
        "replacements": replacements,
        "deploy_ok": verify_sha == patched_sha,
    }
    (WORK_DIR / "deploy-result.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
