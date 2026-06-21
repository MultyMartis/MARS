#!/usr/bin/env python3
"""SITE-002 CATEGORY V2.1 list card layout fix — FTP deploy (twig + css only)."""
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
    "productcard.twig": "catalog/view/theme/default/template/product/productcard.twig",
    "style.css": "assets/css/style.css",
}

ROLLBACK = {
    "productcard.twig": os.path.join(
        BACKUP_DIR, "productcard.twig.pre-list-card-layout-fix.bak"
    ),
    "style.css": os.path.join(BACKUP_DIR, "style.css.pre-list-card-layout-fix.bak"),
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


def ftp_clear_template_cache():
    cache_dir = "system/storage/cache/template"
    cleared = []
    errors = []
    try:
        ftp = ftp_connect()
        ftp.cwd(cache_dir)
        entries = []
        ftp.retrlines("LIST", entries.append)
        for line in entries:
            parts = line.split(None, 8)
            if len(parts) < 9:
                continue
            name = parts[8]
            if name in (".", ".."):
                continue
            if not line.startswith("d"):
                try:
                    ftp.delete(name)
                    cleared.append(name)
                except ftplib.error_perm as e:
                    errors.append(f"{name}: {e}")
        ftp.quit()
    except Exception as e:
        errors.append(str(e))
    return cleared, errors


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

    cleared, cache_errors = ftp_clear_template_cache()
    manifest = {
        "pass": "CATEGORY-V2.1-LIST-CARD-LAYOUT-FIX",
        "site_id": "SITE-002",
        "deployed_at": datetime.now(timezone.utc).isoformat(),
        "files": deployed,
        "rollback_files": ROLLBACK,
        "php_touched": False,
        "template_cache_cleared": len(cleared),
        "template_cache_errors": cache_errors,
    }
    manifest_path = os.path.join(
        BACKUP_DIR, f"category-v2.1-list-card-layout-fix-deploy-manifest-{STAMP}.json"
    )
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("Manifest:", manifest_path)
    print("Template cache cleared:", len(cleared))
    if cache_errors:
        print("Cache errors:", cache_errors)


if __name__ == "__main__":
    main()
