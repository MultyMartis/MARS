#!/usr/bin/env python3
"""SITE-002 — rollback hero to pre-W1A backups on TEST."""
import ftplib
import io
import json
import os
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

TWIG_REMOTE = "catalog/view/theme/default/template/product/producthero.twig"
CSS_REMOTE = "assets/css/style.css"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
BACKUP_DIR = os.path.join(BASE, "backups")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

TWIG_ROLLBACK = os.path.join(BACKUP_DIR, "producthero.twig.pre-w1a.bak")
CSS_ROLLBACK = os.path.join(BACKUP_DIR, "style.css.pre-w1a.bak")


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
    os.makedirs(BACKUP_DIR, exist_ok=True)
    for path in (TWIG_ROLLBACK, CSS_ROLLBACK):
        if not os.path.isfile(path):
            raise SystemExit(f"Missing rollback file: {path}")

    print("Saving current live (failed W1A) before rollback...")
    twig_live = ftp_download(TWIG_REMOTE)
    css_live = ftp_download(CSS_REMOTE)
    failed_twig = os.path.join(BACKUP_DIR, f"producthero.twig.failed-w1a.{STAMP}.bak")
    failed_css = os.path.join(BACKUP_DIR, f"style.css.failed-w1a.{STAMP}.bak")
    for path, data in ((failed_twig, twig_live), (failed_css, css_live)):
        with open(path, "wb") as f:
            f.write(data)
        print("  saved", path, len(data), "bytes")

    with open(TWIG_ROLLBACK, "rb") as f:
        twig_restore = f.read()
    with open(CSS_ROLLBACK, "rb") as f:
        css_restore = f.read()

    print("Uploading pre-W1A producthero.twig...")
    ftp_upload(TWIG_REMOTE, twig_restore)
    print("Uploading pre-W1A style.css...")
    ftp_upload(CSS_REMOTE, css_restore)

    cleared, errors = ftp_clear_template_cache()
    manifest = {
        "stamp": STAMP,
        "action": "rollback-pre-w1a",
        "restored_from": {
            "twig": TWIG_ROLLBACK,
            "css": CSS_ROLLBACK,
        },
        "failed_w1a_backup": {
            "twig": failed_twig,
            "css": failed_css,
        },
        "cache_cleared": len(cleared),
        "cache_errors": errors,
    }
    manifest_path = os.path.join(BACKUP_DIR, f"w1a-rollback-manifest-{STAMP}.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Rollback complete. Manifest:", manifest_path)
    print("Cache files cleared:", len(cleared))
    if errors:
        print("Cache errors:", errors)


if __name__ == "__main__":
    main()
