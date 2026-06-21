#!/usr/bin/env python3
"""SITE-002 M7.1 Launch Mode — FTP deploy to TEST only."""
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

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002\m7.1-launch-mode-work"
PATCH = os.path.join(BASE, "patch")
BACKUP = os.path.join(BASE, "backups")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

REMOTE_FILES = [
    "system/library/zpm/category_visibility.php",
    "catalog/controller/product/katalog.php",
    "catalog/controller/product/category.php",
    "catalog/controller/common/header.php",
    "catalog/controller/common/footer.php",
    "catalog/controller/common/home.php",
    "catalog/view/theme/default/template/common/megamenu.twig",
    "catalog/view/theme/default/template/common/footer.twig",
    "catalog/view/theme/default/template/sections/catalogsections.twig",
    "catalog/view/theme/default/template/sections/offcanvasmenu.twig",
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


def ftp_upload(remote_path, data_bytes):
    ftp = ftp_connect()
    ensure_remote_dirs(ftp, remote_path)
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
    deployed = []
    for rel in REMOTE_FILES:
        local = os.path.join(PATCH, rel.replace("/", os.sep))
        if not os.path.isfile(local):
            print("ERROR: missing", local)
            sys.exit(1)
        with open(local, "rb") as f:
            data = f.read()
        print("Uploading", rel, "...")
        ftp_upload(rel, data)
        deployed.append(
            {
                "remote": rel,
                "local": local,
                "sha256": sha256_hex(data),
                "bytes": len(data),
            }
        )

    print("Clearing Twig template cache ...")
    cleared, cache_errors = ftp_clear_template_cache()

    manifest = {
        "task": "M7.1 Launch Mode TEST deploy",
        "site": "SITE-002",
        "test_url": "https://zpm.new-site.space/",
        "deployed_at_utc": STAMP,
        "files": deployed,
        "twig_cache_cleared": len(cleared),
        "twig_cache_errors": cache_errors,
    }
    out = os.path.join(BACKUP, f"m7.1-launch-mode-deploy-{STAMP}.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Deploy manifest:", out)
    print("Files deployed:", len(deployed))
    print("Twig cache files cleared:", len(cleared))
    if cache_errors:
        print("Cache errors:", cache_errors)


if __name__ == "__main__":
    main()
