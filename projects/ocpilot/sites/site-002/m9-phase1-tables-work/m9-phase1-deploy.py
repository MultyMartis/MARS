#!/usr/bin/env python3
"""BZPM M9 Phase 1 — FTP deploy to TEST only (Tables filter profile 301)."""
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

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002\m9-phase1-tables-work"
PATCH = os.path.join(BASE, "patch")
BACKUP_DIR = os.path.join(BASE, "backups")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

REMOTE_FILES = [
    "system/library/zpm/filter_profile_resolver.php",
    "system/library/zpm/filter_profiles/global_hidden.php",
    "system/library/zpm/filter_profiles/301_stoly.php",
    "catalog/model/catalog/product.php",
    "catalog/controller/product/category.php",
    "catalog/view/theme/default/template/sections/filterssidebar.twig",
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


def ftp_clear_caches():
    cleared_attrs = []
    cleared_twig = []
    errors = []
    try:
        ftp = ftp_connect()
        for cache_dir, prefix, bucket in (
            ("system/storage/cache", "cache.category.attributes.", cleared_attrs),
            ("system/storage/cache/template", None, cleared_twig),
        ):
            ftp.cwd("/")
            ftp.cwd(cache_dir)
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
                if prefix is None or name.startswith(prefix):
                    try:
                        ftp.delete(name)
                        bucket.append(name)
                    except ftplib.error_perm as e:
                        errors.append(f"{cache_dir}/{name}: {e}")
        ftp.quit()
    except Exception as e:
        errors.append(str(e))
    return cleared_attrs, cleared_twig, errors


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
            pre_path = os.path.join(BACKUP_DIR, f"pre-m9-phase1-{rel.replace('/', '__')}")
            os.makedirs(os.path.dirname(pre_path), exist_ok=True)
            with open(pre_path, "wb") as f:
                f.write(live)
            pre_backup.append(
                {"remote": rel, "local_backup": pre_path, "sha256": sha256_hex(live), "bytes": len(live)}
            )
        except ftplib.error_perm as e:
            pre_backup.append({"remote": rel, "local_backup": None, "note": f"new file: {e}"})

        with open(local, "rb") as f:
            data = f.read()
        print("Uploading", rel, "...")
        ftp_upload(rel, data)
        deployed.append(
            {"remote": rel, "local": local, "sha256": sha256_hex(data), "bytes": len(data)}
        )

    print("Clearing attribute + twig cache ...")
    cleared_attrs, cleared_twig, cache_errors = ftp_clear_caches()

    manifest = {
        "task": "M9 Phase 1 Tables filter profile (301)",
        "site": "SITE-002",
        "test_url": "https://zpm.new-site.space/",
        "rollback_source": "SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159",
        "deployed_at_utc": STAMP,
        "pre_backup": pre_backup,
        "files": deployed,
        "attribute_cache_cleared": len(cleared_attrs),
        "twig_cache_cleared": len(cleared_twig),
        "cache_errors": cache_errors,
    }
    out = os.path.join(BACKUP_DIR, f"m9-phase1-deploy-{STAMP}.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Deploy manifest:", out)
    print("Files deployed:", len(deployed))
    print("Attribute cache files cleared:", len(cleared_attrs))
    print("Twig cache files cleared:", len(cleared_twig))
    if cache_errors:
        print("Cache errors:", cache_errors)


if __name__ == "__main__":
    main()
