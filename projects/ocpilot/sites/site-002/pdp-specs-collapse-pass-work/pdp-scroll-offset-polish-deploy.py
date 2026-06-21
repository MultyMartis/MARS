#!/usr/bin/env python3
"""SITE-002 PDP V5.1 scroll offset polish — FTP deploy main.js only."""
import ftplib
import hashlib
import io
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"
BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
BACKUP_DIR = os.path.join(BASE, "backups")
WORK_MAIN = os.path.join(BASE, "pdp-specs-collapse-pass-work", "main.js")
REMOTE = "assets/js/main.js"
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def main():
    with open(WORK_MAIN, "rb") as f:
        local_data = f.read()
    local_sha = sha256_hex(local_data)
    print("LOCAL_SHA256:", local_sha)

    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + REMOTE, bio.write)
    live_before = bio.getvalue()
    live_before_sha = sha256_hex(live_before)
    print("LIVE_SHA256_BEFORE:", live_before_sha)

    backup_path = os.path.join(
        BACKUP_DIR, f"main.js.pre-pdp-v5.1-scroll-offset-polish-{STAMP}.bak"
    )
    with open(backup_path, "wb") as f:
        f.write(live_before)
    print("BACKUP_PATH:", backup_path)

    bio_up = io.BytesIO(local_data)
    ftp.storbinary("STOR " + REMOTE, bio_up)

    cleared = []
    errors = []
    try:
        ftp.cwd("system/storage/cache/template")
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
    except Exception as e:
        errors.append(str(e))
    ftp.quit()
    print("CACHE_CLEARED:", len(cleared))

    time.sleep(2)
    url = f"https://zpm.new-site.space/assets/js/main.js?v={STAMP}"
    req = urllib.request.Request(url, headers={"Cookie": "beget=begetok"})
    with urllib.request.urlopen(req, timeout=60) as r:
        live_after = r.read()
    live_after_sha = sha256_hex(live_after)
    print("LIVE_SHA256_AFTER:", live_after_sha)
    print("DEPLOY_MATCH_LOCAL:", live_after == local_data)

    manifest = {
        "stamp": STAMP,
        "task": "pdp-v5.1-scroll-offset-polish",
        "backup_path": backup_path,
        "backup_sha256": live_before_sha,
        "uploaded_local": WORK_MAIN,
        "uploaded_remote": REMOTE,
        "local_sha256": local_sha,
        "live_sha256_before": live_before_sha,
        "live_sha256_after": live_after_sha,
        "cache_cleared": len(cleared),
        "cache_errors": errors,
    }
    manifest_path = os.path.join(
        BACKUP_DIR, f"pdp-v5.1-scroll-offset-polish-deploy-manifest-{STAMP}.json"
    )
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("MANIFEST:", manifest_path)

    if live_after != local_data:
        print("ERROR: live after deploy does not match local")
        sys.exit(1)


if __name__ == "__main__":
    main()
