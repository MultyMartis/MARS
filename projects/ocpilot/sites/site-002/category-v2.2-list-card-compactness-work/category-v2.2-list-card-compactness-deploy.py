#!/usr/bin/env python3
"""SITE-002 CATEGORY V2.2 list card compactness pass — FTP deploy (CSS only)."""
import ftplib
import hashlib
import io
import json
import os
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
WORK_DIR = os.path.join(BASE, "category-v2.1-list-card-commerce-work")
BACKUP_DIR = os.path.join(BASE, "backups")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

REMOTE = {
    "style.css": "assets/css/style.css",
}

ROLLBACK = {
    "style.css": os.path.join(
        BACKUP_DIR, "style.css.pre-list-card-compactness-pass.bak"
    ),
}


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_upload(remote_path, data_bytes):
    ftp = ftp_connect()
    bio = io.BytesIO(data_bytes)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def main():
    deployed = {}
    for local_name, remote_path in REMOTE.items():
        local_path = os.path.join(WORK_DIR, local_name)
        with open(local_path, "rb") as f:
            data = f.read()
        print(f"Uploading {local_name} -> {remote_path} ({len(data)} bytes)")
        ftp_upload(remote_path, data)
        deployed[local_name] = {
            "remote_path": remote_path,
            "local_path": local_path,
            "size": len(data),
            "sha256": sha256_hex(data),
        }

    manifest = {
        "pass": "CATEGORY-V2.2-LIST-CARD-COMPACTNESS-PASS",
        "site_id": "SITE-002",
        "deployed_at": datetime.now(timezone.utc).isoformat(),
        "files": deployed,
        "rollback_files": ROLLBACK,
        "php_touched": False,
        "twig_touched": False,
    }
    manifest_path = os.path.join(
        BACKUP_DIR, f"category-v2.2-list-card-compactness-deploy-manifest-{STAMP}.json"
    )
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("Manifest:", manifest_path)


if __name__ == "__main__":
    main()
