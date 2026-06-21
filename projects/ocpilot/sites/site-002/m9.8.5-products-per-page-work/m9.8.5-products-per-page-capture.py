#!/usr/bin/env python3
"""SITE-002 M9.8.5 products per page — live FTP capture (read-only)."""
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
BACKUP_DIR = os.path.join(BASE, "backups")
WORK_DIR = os.path.join(BASE, "m9.8.5-products-per-page-work")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

REMOTE = {
    "category.php": "catalog/controller/product/category.php",
    "category.twig": "catalog/view/theme/default/template/product/category.twig",
    "style.css": "assets/css/style.css",
    "main.js": "assets/js/main.js",
}


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path):
    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs(WORK_DIR, exist_ok=True)
    captured_at = datetime.now(timezone.utc).isoformat()
    entries = {}

    print("Downloading live files (read-only)...")
    for local_name, remote_path in REMOTE.items():
        data = ftp_download(remote_path)
        backup_path = os.path.join(
            BACKUP_DIR, f"{local_name}.pre-m9.8.5-products-per-page-{STAMP}.bak"
        )
        work_path = os.path.join(WORK_DIR, local_name)
        with open(backup_path, "wb") as f:
            f.write(data)
        with open(work_path, "wb") as f:
            f.write(data)
        digest = sha256_hex(data)
        entries[local_name] = {
            "remote": remote_path,
            "backup": backup_path,
            "work": work_path,
            "size": len(data),
            "sha256": digest,
        }
        print(f"  OK {remote_path} ({len(data)} bytes)")
        print(f"     backup: {backup_path}")
        print(f"     sha256: {digest}")

    manifest = {
        "task": "m9.8.5-products-per-page",
        "captured_at": captured_at,
        "stamp": STAMP,
        "entries": entries,
    }
    manifest_path = os.path.join(
        BACKUP_DIR, f"m9.8.5-products-per-page-capture-{STAMP}.json"
    )
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("Manifest:", manifest_path)
    print("STAMP:", STAMP)
    print("Live capture complete.")


if __name__ == "__main__":
    main()
