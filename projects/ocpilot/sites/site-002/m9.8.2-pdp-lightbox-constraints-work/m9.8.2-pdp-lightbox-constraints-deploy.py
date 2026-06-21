#!/usr/bin/env python3
"""SITE-002 M9.8.2 PDP lightbox constraints — FTP deploy."""
import ftplib
import hashlib
import io
import json
import os
import sys
from datetime import datetime

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
WORK_DIR = os.path.join(BASE, "m9.8.2-pdp-lightbox-constraints-work")
BACKUP_DIR = os.path.join(BASE, "backups")
STAMP = "20260617-210353"

REMOTE = {
    "style.css": "assets/css/style.css",
    "main.js": "assets/js/main.js",
}

ROLLBACK = {
    "style.css": os.path.join(
        BACKUP_DIR, f"style.css.pre-m9.8.2-pdp-lightbox-constraints-{STAMP}.bak"
    ),
    "main.js": os.path.join(
        BACKUP_DIR, f"main.js.pre-m9.8.2-pdp-lightbox-constraints-{STAMP}.bak"
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
        if not os.path.isfile(local_path):
            print("ERROR: missing", local_path)
            sys.exit(1)
        with open(local_path, "rb") as f:
            data = f.read()
        print("Uploading", remote_path, "...")
        ftp_upload(remote_path, data)
        deployed[local_name] = {
            "remote": remote_path,
            "sha256": sha256_hex(data),
            "rollback": ROLLBACK[local_name],
            "rollback_sha256": sha256_hex(open(ROLLBACK[local_name], "rb").read()),
        }

    manifest_path = os.path.join(
        BACKUP_DIR,
        f"m9.8.2-pdp-lightbox-constraints-deploy-manifest-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json",
    )
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(
            {"task": "m9.8.2-pdp-lightbox-constraints", "deployed": deployed},
            f,
            ensure_ascii=False,
            indent=2,
        )

    print("Deploy complete. Manifest:", manifest_path)


if __name__ == "__main__":
    main()
