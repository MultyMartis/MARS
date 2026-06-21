#!/usr/bin/env python3
"""BZPM M8.3 Wave 2 — FTP deploy to TEST only (filter visibility STORE_ONLY)."""
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

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002\m8.3-wave2-cleanup-work"
PATCH = os.path.join(BASE, "patch")
BACKUP_DIR = os.path.join(BASE, "backups")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

REMOTE_FILES = [
    "system/library/zpm/attribute_filter_visibility.php",
    "catalog/model/catalog/product.php",
]


def sha256_hex(data):
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ensure_remote_dirs(ftp, remote_path):
    parts = remote_path.split("/")[:-1]
    if not parts:
        return
    ftp.cwd("/")
    for part in parts:
        try:
            ftp.cwd(part)
        except ftplib.error_perm:
            ftp.mkd(part)
            ftp.cwd(part)
    ftp.cwd("/")


def ftp_download(remote_path):
    ftp = ftp_connect()
    buf = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, buf.write)
    ftp.quit()
    return buf.getvalue()


def ftp_upload(remote_path, data_bytes):
    ftp = ftp_connect()
    ensure_remote_dirs(ftp, remote_path)
    bio = io.BytesIO(data_bytes)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def ftp_clear_attribute_cache():
    cleared = []
    errors = []
    try:
        ftp = ftp_connect()
        ftp.cwd("system/storage/cache")
        entries = []
        ftp.retrlines("LIST", entries.append)
        for line in entries:
            parts = line.split(None, 8)
            if len(parts) < 9:
                continue
            name = parts[8]
            if name in (".", "..", "index.html"):
                continue
            if line.startswith("d"):
                continue
            if name.startswith("cache.category.attributes."):
                try:
                    ftp.delete(name)
                    cleared.append(name)
                except ftplib.error_perm as e:
                    errors.append(f"{name}: {e}")
        ftp.quit()
    except Exception as e:
        errors.append(str(e))
    return cleared, errors


def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    pre_backup = []
    deployed = []

    for rel in REMOTE_FILES:
        local = os.path.join(PATCH, rel.replace("/", os.sep))
        if not os.path.isfile(local):
            print("ERROR: missing", local)
            sys.exit(1)

        try:
            live = ftp_download(rel)
            pre_path = os.path.join(BACKUP_DIR, f"pre-m8.3-wave2-{rel.replace('/', '__')}")
            os.makedirs(os.path.dirname(pre_path), exist_ok=True)
            with open(pre_path, "wb") as f:
                f.write(live)
            pre_backup.append(
                {"remote": rel, "local_backup": pre_path, "sha256": sha256_hex(live), "bytes": len(live)}
            )
        except ftplib.error_perm as e:
            if rel.endswith("attribute_filter_visibility.php"):
                pre_backup.append({"remote": rel, "local_backup": None, "note": f"new file: {e}"})
            else:
                raise

        with open(local, "rb") as f:
            data = f.read()
        print("Uploading", rel, "...")
        ftp_upload(rel, data)
        deployed.append(
            {"remote": rel, "local": local, "sha256": sha256_hex(data), "bytes": len(data)}
        )

    print("Clearing category.attributes cache ...")
    cleared, cache_errors = ftp_clear_attribute_cache()

    manifest = {
        "task": "M8.3 Wave 2 Packaging & Service filter visibility",
        "site": "SITE-002",
        "test_url": "https://zpm.new-site.space/",
        "deployed_at_utc": STAMP,
        "pre_backup": pre_backup,
        "files": deployed,
        "attribute_cache_cleared": len(cleared),
        "attribute_cache_errors": cache_errors,
    }
    out = os.path.join(BACKUP_DIR, f"m8.3-wave2-deploy-{STAMP}.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Deploy manifest:", out)
    print("Files deployed:", len(deployed))
    print("Attribute cache files cleared:", len(cleared))
    if cache_errors:
        print("Cache errors:", cache_errors)


if __name__ == "__main__":
    main()
