#!/usr/bin/env python3
"""SITE-002 CATEGORY V2.3.1 subcategory polish pass — FTP deploy."""
import ftplib
import hashlib
import io
import json
import os
import sys
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
WORK_DIR = os.path.join(BASE, "category-v2.3.1-subcategory-polish-pass-work")
BACKUP_DIR = os.path.join(BASE, "backups")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

REMOTE = {
    "category.twig": "catalog/view/theme/default/template/product/category.twig",
    "style.css": "assets/css/style.css",
    "main.js": "assets/js/main.js",
}

ROLLBACK = {
    "category.twig": os.path.join(BACKUP_DIR, "category.twig.pre-subcategory-polish-pass.bak"),
    "style.css": os.path.join(BACKUP_DIR, "style.css.pre-subcategory-polish-pass.bak"),
    "main.js": os.path.join(BACKUP_DIR, "main.js.pre-subcategory-polish-pass.bak"),
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
        if not os.path.isfile(local_path):
            print("ERROR: missing", local_path)
            sys.exit(1)
        with open(local_path, "rb") as f:
            data = f.read()
        print("Uploading", remote_path, "...")
        ftp_upload(remote_path, data)
        rollback_path = ROLLBACK[local_name]
        deployed[local_name] = {
            "remote": remote_path,
            "local": local_path,
            "sha256": sha256_hex(data),
            "rollback": rollback_path,
            "rollback_sha256": sha256_hex(open(rollback_path, "rb").read()),
        }

    cleared, errors = ftp_clear_template_cache()
    manifest = {
        "stamp": STAMP,
        "task": "category-v2.3.1-subcategory-polish-pass",
        "deployed_at": datetime.now(timezone.utc).isoformat(),
        "deployed": deployed,
        "cache_cleared": len(cleared),
        "cache_errors": errors,
        "rollback_procedure": [
            f"Upload {ROLLBACK['category.twig']} -> {REMOTE['category.twig']}",
            f"Upload {ROLLBACK['style.css']} -> {REMOTE['style.css']}",
            f"Upload {ROLLBACK['main.js']} -> {REMOTE['main.js']}",
            "Clear system/storage/cache/template/",
        ],
    }
    manifest_path = os.path.join(
        BACKUP_DIR, f"category-v2.3.1-subcategory-polish-deploy-manifest-{STAMP}.json"
    )
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Deploy complete. Manifest:", manifest_path)
    print("Cache files cleared:", len(cleared))
    if errors:
        print("Cache errors:", errors)


if __name__ == "__main__":
    main()
