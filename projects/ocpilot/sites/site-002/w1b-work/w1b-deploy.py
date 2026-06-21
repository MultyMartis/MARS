#!/usr/bin/env python3
"""SITE-002 Wave 1B — FTP backup, deploy producttabs + CSS, cache clear."""
import ftplib
import io
import json
import os
import sys
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

TWIG_REMOTE = "catalog/view/theme/default/template/product/producttabs.twig"
CSS_REMOTE = "assets/css/style.css"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
BACKUP_DIR = os.path.join(BASE, "backups")
WORK_DIR = os.path.join(BASE, "w1b-work")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


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


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "deploy"
    os.makedirs(BACKUP_DIR, exist_ok=True)

    twig_backup = os.path.join(BACKUP_DIR, f"producttabs.twig.{STAMP}.bak")
    css_backup = os.path.join(BACKUP_DIR, f"style.css.{STAMP}.bak")
    twig_latest = os.path.join(BACKUP_DIR, "producttabs.twig.pre-w1b.bak")
    css_latest = os.path.join(BACKUP_DIR, "style.css.pre-w1b.bak")

    print("Downloading live files for backup...")
    twig_live = ftp_download(TWIG_REMOTE)
    css_live = ftp_download(CSS_REMOTE)

    for path, data in [
        (twig_backup, twig_live),
        (css_backup, css_live),
        (twig_latest, twig_live),
        (css_latest, css_live),
    ]:
        with open(path, "wb") as f:
            f.write(data)
        print("  saved", path, len(data), "bytes")

    manifest = {
        "stamp": STAMP,
        "wave": "1B",
        "remote_twig": TWIG_REMOTE,
        "remote_css": CSS_REMOTE,
        "backup_paths": {
            "twig_timestamped": twig_backup,
            "css_timestamped": css_backup,
            "twig_rollback": twig_latest,
            "css_rollback": css_latest,
        },
        "rollback_procedure": [
            f"Upload {twig_latest} -> {TWIG_REMOTE}",
            f"Upload {css_latest} -> {CSS_REMOTE}",
            "Clear system/storage/cache/template/",
        ],
    }

    if mode == "backup-only":
        manifest_path = os.path.join(BACKUP_DIR, f"w1b-backup-manifest-{STAMP}.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
        print("BACKUP ONLY — manifest:", manifest_path)
        return

    twig_local = os.path.join(WORK_DIR, "producttabs.twig")
    css_local = os.path.join(WORK_DIR, "style.css")
    if not os.path.isfile(twig_local):
        print("ERROR: missing", twig_local)
        sys.exit(1)
    if not os.path.isfile(css_local):
        print("ERROR: missing", css_local)
        sys.exit(1)

    with open(twig_local, "rb") as f:
        twig_new = f.read()
    with open(css_local, "rb") as f:
        css_new = f.read()

    print("Uploading producttabs.twig...")
    ftp_upload(TWIG_REMOTE, twig_new)
    print("Uploading style.css...")
    ftp_upload(CSS_REMOTE, css_new)

    cleared, errors = ftp_clear_template_cache()
    manifest["deployed"] = True
    manifest["cache_cleared"] = len(cleared)
    manifest["cache_errors"] = errors

    manifest_path = os.path.join(BACKUP_DIR, f"w1b-deploy-manifest-{STAMP}.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Deploy complete. Manifest:", manifest_path)
    print("Cache files cleared:", len(cleared))
    if errors:
        print("Cache errors:", errors)


if __name__ == "__main__":
    main()
