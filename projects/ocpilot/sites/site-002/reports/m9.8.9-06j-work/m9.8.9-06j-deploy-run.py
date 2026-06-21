#!/usr/bin/env python3
"""M9.8.9-06J — numeric attribute filter hotfix deploy."""
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
BACKUP_PATH = ROOT / "backups" / "product.php.pre-m9.8.9-06j-numeric-attr-filter.bak"
WORK_DIR = ROOT / "reports" / "m9.8.9-06j-work"
PATCHED_PATH = WORK_DIR / "catalog__model__catalog__product.php.patched"
CAPTURE_PATH = WORK_DIR / "live-capture" / "catalog__model__catalog__product.php"


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


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    live_raw = CAPTURE_PATH.read_bytes()
    live_sha = sha256_hex(live_raw)
    patched_raw = PATCHED_PATH.read_bytes()
    patched_sha = sha256_hex(patched_raw)

    manifest = {
        "task": "M9.8.9-06J",
        "authority": "SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01",
        "stamp": stamp,
        "remote_path": REMOTE_PATH,
        "pre_deploy": {
            "backup": str(BACKUP_PATH),
            "capture": str(CAPTURE_PATH),
            "sha256": live_sha,
            "size": len(live_raw),
        },
        "post_deploy": {
            "local_patched": str(PATCHED_PATH),
            "sha256": patched_sha,
            "size": len(patched_raw),
        },
        "rollback_sha256": live_sha,
        "rollback_file": str(BACKUP_PATH),
    }
    manifest_path = WORK_DIR / f"manifest-{stamp}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    ftp_upload(REMOTE_PATH, patched_raw)

    verify_raw = ftp_download(REMOTE_PATH)
    verify_sha = sha256_hex(verify_raw)

    result = {
        "manifest": str(manifest_path),
        "pre_sha256": live_sha,
        "patched_sha256": patched_sha,
        "post_deploy_verify_sha256": verify_sha,
        "deploy_ok": verify_sha == patched_sha,
    }
    (WORK_DIR / "deploy-result.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
