#!/usr/bin/env python3
"""SITE-002 — full PDP rollback to pre-W1A baseline on TEST."""
import ftplib
import io
import json
import os
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

REMOTE = {
    "producthero": "catalog/view/theme/default/template/product/producthero.twig",
    "producttabs": "catalog/view/theme/default/template/product/producttabs.twig",
    "style": "assets/css/style.css",
}

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
BACKUP_DIR = os.path.join(BASE, "backups")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

ROLLBACK = {
    "producthero": os.path.join(BACKUP_DIR, "producthero.twig.pre-w1a.bak"),
    "producttabs": os.path.join(BACKUP_DIR, "producttabs.twig.pre-w1b.bak"),
    "style": os.path.join(BACKUP_DIR, "style.css.pre-w1a.bak"),
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
    for key, path in ROLLBACK.items():
        if not os.path.isfile(path):
            raise SystemExit(f"Missing rollback file: {path}")

    pre_rollback = {}
    print("Saving current live files before rollback...")
    for key, remote in REMOTE.items():
        live = ftp_download(remote)
        out = os.path.join(BACKUP_DIR, f"{key}.{STAMP}.pre-rollback.bak")
        with open(out, "wb") as f:
            f.write(live)
        pre_rollback[key] = out
        print(f"  saved {out} ({len(live)} bytes)")

    print("Uploading pre-W1A baseline files...")
    for key, remote in REMOTE.items():
        with open(ROLLBACK[key], "rb") as f:
            data = f.read()
        ftp_upload(remote, data)
        print(f"  {key}: {ROLLBACK[key]} -> {remote} ({len(data)} bytes)")

    cleared, errors = ftp_clear_template_cache()
    manifest = {
        "stamp": STAMP,
        "action": "full-rollback-pre-w1a",
        "restored_from": ROLLBACK,
        "remote_paths": REMOTE,
        "pre_rollback_backup": pre_rollback,
        "cache_cleared": len(cleared),
        "cache_errors": errors,
    }
    manifest_path = os.path.join(BACKUP_DIR, f"rollback-pre-w1a-manifest-{STAMP}.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Rollback complete. Manifest:", manifest_path)
    print("Cache files cleared:", len(cleared))
    if errors:
        print("Cache errors:", errors)


if __name__ == "__main__":
    main()
