#!/usr/bin/env python3
"""SITE-002 Wave 1B.1 — FTP backup/deploy producthero + producttabs + CSS."""
import ftplib
import io
import json
import os
import sys
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

REMOTE_FILES = {
    "producthero.twig": "catalog/view/theme/default/template/product/producthero.twig",
    "producttabs.twig": "catalog/view/theme/default/template/product/producttabs.twig",
    "style.css": "assets/css/style.css",
}

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
BACKUP_DIR = os.path.join(BASE, "backups")
WORK_DIR = os.path.join(BASE, "w1b1-work")
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
    os.makedirs(WORK_DIR, exist_ok=True)

    rollback_aliases = {
        "producthero.twig": "producthero.twig.pre-w1b1.bak",
        "producttabs.twig": "producttabs.twig.pre-w1b1.bak",
        "style.css": "style.css.pre-w1b1.bak",
    }

    backup_paths = {}
    live_data = {}

    print("Downloading live files for backup...")
    for local_name, remote_path in REMOTE_FILES.items():
        data = ftp_download(remote_path)
        live_data[local_name] = data

        ts_path = os.path.join(BACKUP_DIR, f"{local_name}.{STAMP}.bak")
        rb_path = os.path.join(BACKUP_DIR, rollback_aliases[local_name])
        work_path = os.path.join(WORK_DIR, local_name)

        for path in (ts_path, rb_path):
            with open(path, "wb") as f:
                f.write(data)
            print("  saved", path, len(data), "bytes")

        if mode == "backup-only":
            work_path = os.path.join(WORK_DIR, local_name)
            with open(work_path, "wb") as f:
                f.write(data)
            print("  saved", work_path, len(data), "bytes")

        backup_paths[local_name] = {
            "timestamped": ts_path,
            "rollback": rb_path,
            "remote": remote_path,
        }

    manifest = {
        "stamp": STAMP,
        "wave": "1B.1",
        "remote_files": REMOTE_FILES,
        "backup_paths": backup_paths,
        "rollback_procedure": [
            f"Upload {backup_paths['producthero.twig']['rollback']} -> {REMOTE_FILES['producthero.twig']}",
            f"Upload {backup_paths['producttabs.twig']['rollback']} -> {REMOTE_FILES['producttabs.twig']}",
            f"Upload {backup_paths['style.css']['rollback']} -> {REMOTE_FILES['style.css']}",
            "Clear system/storage/cache/template/",
        ],
    }

    if mode == "backup-only":
        manifest_path = os.path.join(BACKUP_DIR, f"w1b1-backup-manifest-{STAMP}.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
        print("BACKUP ONLY — manifest:", manifest_path)
        return

    for local_name, remote_path in REMOTE_FILES.items():
        local_path = os.path.join(WORK_DIR, local_name)
        if not os.path.isfile(local_path):
            print("ERROR: missing", local_path)
            sys.exit(1)
        with open(local_path, "rb") as f:
            data = f.read()
        print(f"Uploading {local_name}...")
        ftp_upload(remote_path, data)

    cleared, errors = ftp_clear_template_cache()
    manifest["deployed"] = True
    manifest["cache_cleared"] = len(cleared)
    manifest["cache_errors"] = errors

    manifest_path = os.path.join(BACKUP_DIR, f"w1b1-deploy-manifest-{STAMP}.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Deploy complete. Manifest:", manifest_path)
    print("Cache files cleared:", len(cleared))
    if errors:
        print("Cache errors:", errors)


if __name__ == "__main__":
    main()
