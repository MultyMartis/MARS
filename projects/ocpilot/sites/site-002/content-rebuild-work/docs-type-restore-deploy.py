#!/usr/bin/env python3
"""SITE-002 PDP document type logic restore — FTP deploy producttabs.twig only."""
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

TWIG_REMOTE = "catalog/view/theme/default/template/product/producttabs.twig"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
BACKUP_DIR = os.path.join(BASE, "backups")
WORK_DIR = os.path.join(BASE, "content-rebuild-work")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
ROLLBACK_BAK = os.path.join(BACKUP_DIR, "producttabs.twig.pre-docs-type-restore.bak")


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
    twig_local = os.path.join(WORK_DIR, "producttabs.twig")
    if not os.path.isfile(twig_local):
        print("ERROR: missing", twig_local)
        sys.exit(1)
    if not os.path.isfile(ROLLBACK_BAK):
        print("ERROR: missing rollback backup", ROLLBACK_BAK)
        sys.exit(1)

    with open(twig_local, "rb") as f:
        twig_new = f.read()

    print("Uploading producttabs.twig...")
    ftp_upload(TWIG_REMOTE, twig_new)

    cleared, errors = ftp_clear_template_cache()
    manifest = {
        "stamp": STAMP,
        "task": "pdp-document-type-logic-restore",
        "remote_twig": TWIG_REMOTE,
        "local_twig": twig_local,
        "rollback_path": ROLLBACK_BAK,
        "deployed_sha256": sha256_hex(twig_new),
        "rollback_sha256": sha256_hex(open(ROLLBACK_BAK, "rb").read()),
        "cache_cleared": len(cleared),
        "cache_errors": errors,
        "rollback_procedure": [
            f"Upload {ROLLBACK_BAK} -> {TWIG_REMOTE}",
            "Clear system/storage/cache/template/",
        ],
    }
    manifest_path = os.path.join(BACKUP_DIR, f"docs-type-restore-deploy-manifest-{STAMP}.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Deploy complete. Manifest:", manifest_path)
    print("Cache files cleared:", len(cleared))
    if errors:
        print("Cache errors:", errors)


if __name__ == "__main__":
    main()
