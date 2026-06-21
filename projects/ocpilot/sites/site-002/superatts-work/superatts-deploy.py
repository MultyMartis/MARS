#!/usr/bin/env python3
"""Deploy SUPER_ATTS controller fix + clear OC cache on SITE-002 TEST."""
import ftplib
import io
import json
import os
import urllib.request
from datetime import datetime, timezone
from html import unescape
import re

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
WORK = os.path.join(BASE, "superatts-work")
LOCAL_PHP = os.path.join(WORK, "product.php")
REMOTE_PHP = "catalog/controller/product/product.php"
CACHE_DIR = "system/storage/cache"

BATH = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850"
TABLE = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850"


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def clear_cache():
    cleared = []
    errors = []
    ftp = ftp_connect()
    try:
        ftp.cwd(CACHE_DIR)
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
            try:
                ftp.delete(name)
                cleared.append(name)
            except ftplib.error_perm as e:
                errors.append(f"{name}: {e}")
    except Exception as e:
        errors.append(str(e))
    finally:
        ftp.quit()
    return cleared, errors


def upload_product_php():
    with open(LOCAL_PHP, "rb") as f:
        data = f.read()
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + REMOTE_PHP, bio)
    ftp.quit()
    return len(data)


def hero_names(url):
    html = urllib.request.urlopen(url, timeout=60).read().decode("utf-8")
    b = re.search(r"product-hero__props\">(.*?)</dl>", html, re.S)
    if not b:
        return [], "Fatal error" in html
    names = []
    for m in re.finditer(r"<dt>(.*?)</dt>", b.group(1), re.S):
        names.append(unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1)).strip())))
    return names, "Fatal error" in html or "Parse error" in html


def main():
    size = upload_product_php()
    cleared, errors = clear_cache()
    qa = {}
    for label, url in [("bath", BATH), ("table", TABLE)]:
        names, err = hero_names(url)
        qa[label] = {"url": url, "hero_names": names, "hero_count": len(names), "php_error": err}
    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "deployed": REMOTE_PHP,
        "bytes": size,
        "cache_cleared": cleared,
        "cache_errors": errors,
        "qa": qa,
    }
    out_path = os.path.join(WORK, "superatts-deploy-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
