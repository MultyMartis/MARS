#!/usr/bin/env python3
"""BZPM M9.7C — deploy category images + megamenu empty-category fix (TEST only)."""
import ftplib
import hashlib
import io
import json
import os
import re
import ssl
import sys
import urllib.parse
import urllib.request
import http.cookiejar
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"

BASE = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\m9.7c-image-megamenu-work")
PATCH = BASE / "patch"
BACKUP_DIR = BASE / "backups"
IMAGE_SRC = Path(r"C:\AI MARS\image\catalog\Category-image")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

REMOTE_FILES = [
    "system/library/zpm/category_visibility.php",
    "catalog/controller/common/header.php",
    "catalog/controller/product/katalog.php",
]

IMAGE_DEPLOY = [
    ("stoly.webp", 301, "catalog/Category-image/stoly.webp"),
    ("moechnye-vanny.webp", 80, "catalog/Category-image/moechnye-vanny.webp"),
    ("podtovarniki-i-podstavki.webp", 322, "catalog/Category-image/podtovarniki-i-podstavki.webp"),
    ("zonty-vytyazhnye.webp", 207, "catalog/Category-image/zonty-vytyazhnye.webp"),
    ("telezhki-servirovochnye.webp", 326, "catalog/Category-image/telezhki-servirovochnye.webp"),
]


def sha256_hex(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ensure_remote_dirs(ftp, remote_path: str):
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


def ftp_download(remote_path: str) -> bytes:
    ftp = ftp_connect()
    buf = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, buf.write)
    ftp.quit()
    return buf.getvalue()


def ftp_upload(remote_path: str, data_bytes: bytes):
    ftp = ftp_connect()
    ensure_remote_dirs(ftp, remote_path)
    bio = io.BytesIO(data_bytes)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def ftp_clear_caches():
    cleared = {"attrs": [], "twig": [], "catlist": [], "image_cache": [], "errors": []}
    try:
        ftp = ftp_connect()
        for cache_dir, prefix, bucket in (
            ("system/storage/cache", "cache.category.attributes.", cleared["attrs"]),
            ("system/storage/cache/template", None, cleared["twig"]),
            ("system/storage/cache", "cache.cat-list-header", cleared["catlist"]),
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
                        cleared["errors"].append(f"{cache_dir}/{name}: {e}")

        # Clear resized thumbs for branch category images (safe prefix match only)
        prefixes = (
            "catalog/Category-image/stoly",
            "catalog/Category-image/moechnye-vanny",
            "catalog/Category-image/podtovarniki-i-podstavki",
            "catalog/Category-image/zonty-vytyazhnye",
            "catalog/Category-image/telezhki-servirovochnye",
        )
        ftp.cwd("/")
        ftp.cwd("image/cache")
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
            if any(name.startswith(p.replace("/", "-")) for p in prefixes):
                try:
                    ftp.delete(name)
                    cleared["image_cache"].append(name)
                except ftplib.error_perm as e:
                    cleared["errors"].append(f"image/cache/{name}: {e}")
        ftp.quit()
    except Exception as e:
        cleared["errors"].append(str(e))
    return cleared


def pma_session():
    ctx = ssl.create_default_context()
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj),
        urllib.request.HTTPSHandler(context=ctx),
    )
    lp = op.open(PMA + "/", timeout=60).read().decode("utf-8", "replace")
    token = re.search(r'name="token"\s+value="([^"]+)"', lp).group(1)
    op.open(
        urllib.request.Request(
            PMA + "/index.php",
            data=urllib.parse.urlencode(
                {
                    "pma_username": DB_USER,
                    "pma_password": DB_PASS,
                    "server": "1",
                    "target": "index.php",
                    "token": token,
                }
            ).encode(),
            method="POST",
        ),
        timeout=60,
    )
    return op


def pma_run(op, sql: str, expect_rows=True):
    db_html = op.open(PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60).read().decode(
        "utf-8", "replace"
    )
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)
    html = op.open(
        urllib.request.Request(
            PMA + "/sql.php",
            data=urllib.parse.urlencode(
                {"db": DB, "sql_query": sql, "token": csrf, "sql_delimiter": ";"}
            ).encode(),
            method="POST",
        ),
        timeout=240,
    ).read().decode("utf-8", "replace")
    if "MySQL said:" in html or "#1064" in html:
        err = re.search(r"MySQL said:\s*<[^>]+>([^<]+)", html)
        raise RuntimeError(err.group(1).strip() if err else "mysql error")
    if not expect_rows:
        affected = re.search(r"(\d+)\s+rows?\s+affected", html, re.I)
        return {"affected": affected.group(1) if affected else "unknown"}
    rows = []
    for tbl in re.findall(r'<table[^>]*class="[^"]*table[^"]*"[^>]*>(.*?)</table>', html, re.S):
        if "Browse" in tbl and "Drop" in tbl:
            continue
        parsed = []
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S):
            cells = [
                unescape(re.sub(r"<[^>]+>", " ", c).strip())
                for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)
            ]
            cells = [re.sub(r"\s+", " ", c) for c in cells if c.strip()]
            if cells:
                parsed.append(cells)
        if len(parsed) >= 2 and not parsed[0][0].startswith("Table navigation"):
            rows = parsed
            break
    if len(rows) < 2:
        if "MySQL returned an empty result set" in html:
            return []
        m = re.search(r"(\d+)\s+rows?\s+affected", html, re.I)
        if m:
            return [{"affected": m.group(1)}]
        return []
    header = [x.lower() for x in rows[0]]
    return [dict(zip(header, r)) for r in rows[1:] if len(r) == len(header)]


def deploy_images():
    uploaded = []
    for filename, _cat_id, remote_rel in IMAGE_DEPLOY:
        local = IMAGE_SRC / filename
        if not local.is_file():
            raise FileNotFoundError(local)
        data = local.read_bytes()
        remote = "image/" + remote_rel
        print("Upload image", remote, "...")
        ftp_upload(remote, data)
        uploaded.append(
            {
                "local": str(local),
                "remote": remote,
                "bytes": len(data),
                "sha256": sha256_hex(data),
            }
        )
    return uploaded


def update_category_images(op):
    before = pma_run(
        op,
        "SELECT category_id, image FROM oc_category WHERE category_id IN (301,80,322,207,326) ORDER BY category_id",
    )
    updates = []
    for _filename, cat_id, db_path in IMAGE_DEPLOY:
        sql = (
            f"UPDATE oc_category SET image = '{db_path}' "
            f"WHERE category_id = {cat_id}"
        )
        result = pma_run(op, sql, expect_rows=False)
        updates.append({"category_id": cat_id, "image": db_path, "result": result})
    after = pma_run(
        op,
        "SELECT category_id, image FROM oc_category WHERE category_id IN (301,80,322,207,326) ORDER BY category_id",
    )
    return before, updates, after


def deploy_php():
    pre_backup = []
    deployed = []
    for rel in REMOTE_FILES:
        local = PATCH / rel.replace("/", os.sep)
        if not local.is_file():
            print("ERROR missing patch", local)
            sys.exit(1)
        try:
            live = ftp_download(rel)
            pre_path = BACKUP_DIR / f"pre-m9.7c-{rel.replace('/', '__')}"
            pre_path.parent.mkdir(parents=True, exist_ok=True)
            pre_path.write_bytes(live)
            pre_backup.append(
                {"remote": rel, "local_backup": str(pre_path), "sha256": sha256_hex(live), "bytes": len(live)}
            )
        except ftplib.error_perm as e:
            pre_backup.append({"remote": rel, "local_backup": None, "note": str(e)})
        data = local.read_bytes()
        print("Upload PHP", rel, "...")
        ftp_upload(rel, data)
        deployed.append({"remote": rel, "local": str(local), "sha256": sha256_hex(data), "bytes": len(data)})
    return pre_backup, deployed


def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)

    print("=== PHASE 1: Image deploy ===")
    images = deploy_images()

    print("=== PHASE 2: DB image wiring ===")
    op = pma_session()
    before_db, db_updates, after_db = update_category_images(op)

    print("=== PHASE 5: PHP deploy (megamenu fix) ===")
    pre_backup, deployed = deploy_php()

    print("=== Cache flush ===")
    cache_result = ftp_clear_caches()

    manifest = {
        "task": "M9.7C category image deploy + megamenu cleanup",
        "site": "SITE-002",
        "test_url": "https://zpm.new-site.space/",
        "rollback_source": "SITE-002-STABLE-M9-COMPLETE-20260615",
        "deployed_at_utc": STAMP,
        "images": images,
        "db_before": before_db,
        "db_updates": db_updates,
        "db_after": after_db,
        "pre_backup": pre_backup,
        "files": deployed,
        "cache": cache_result,
    }
    out = BACKUP_DIR / f"m9.7c-deploy-{STAMP}.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("Manifest:", out)
    print("Images uploaded:", len(images))
    print("PHP files deployed:", len(deployed))
    print("DB after:", after_db)


if __name__ == "__main__":
    main()
