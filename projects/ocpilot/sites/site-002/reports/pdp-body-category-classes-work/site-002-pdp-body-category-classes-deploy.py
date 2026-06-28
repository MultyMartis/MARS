#!/usr/bin/env python3
"""SITE-002 — PDP body category classes: backup, deploy, QA."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
WORK = ROOT / "reports" / "pdp-body-category-classes-work"
BACKUP = ROOT / "backups"
BACKUP_SUFFIX = "pre-pdp-body-category-classes.bak"
REMOTE = "catalog/controller/product/product.php"
LOCAL_PATCHED = WORK / "catalog__controller__product__product.php.patched"
BASE = "https://zpm.new-site.space"

QA_URLS = {
    "podtovarniki": f"{BASE}/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki",
    "stoly": f"{BASE}/katalog/nejtralnoe-oborudovanie/stoly",
    "teplovoe": f"{BASE}/katalog/teplovoe-oborudovanie",
}


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path: str) -> bytes | None:
    ftp = ftp_connect()
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + remote_path, bio.write)
        ftp.quit()
        return bio.getvalue()
    except ftplib.error_perm:
        ftp.quit()
        return None


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def clear_twig_cache() -> list[str]:
    cleared: list[str] = []
    ftp = ftp_connect()
    try:
        ftp.cwd("system/storage/cache")
        entries: list[str] = []
        ftp.retrlines("LIST", entries.append)
        for line in entries:
            parts = line.split(None, 8)
            if len(parts) < 9:
                continue
            name = parts[8]
            if name in (".", "..", "index.html") or line.startswith("d"):
                continue
            try:
                ftp.delete(name)
                cleared.append(name)
            except ftplib.error_perm:
                pass
    finally:
        ftp.quit()
    return cleared


def http_get(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "SITE-002-pdp-body-category-classes/1.0"})
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return e.code, body


def extract_body_class(html: str) -> str | None:
    m = re.search(r'<body[^>]*class="([^"]*)"', html, re.I)
    return m.group(1) if m else None


def find_product_url(plp_html: str) -> str | None:
    m = re.search(r'href="(https://zpm\.new-site\.space/katalog/[^"]+/[^"]+)"', plp_html)
    if m:
        return m.group(1)
    m = re.search(r'href="(/katalog/[^"]+/[^"]+/[^"]+)"', plp_html)
    if m:
        return BASE + m.group(1)
    return None


def qa_scan(html: str) -> dict:
    body = extract_body_class(html) or ""
    return {
        "body_class": body,
        "has_page_product": "page--product" in body,
        "has_category_root": bool(re.search(r"\bcategory-root-\d+\b", body)),
        "has_category_parent": bool(re.search(r"\bcategory-parent-\d+\b", body)),
        "category_root": re.search(r"\bcategory-root-(\d+)\b", body).group(1) if re.search(r"\bcategory-root-(\d+)\b", body) else None,
        "category_parent": re.search(r"\bcategory-parent-(\d+)\b", body).group(1) if re.search(r"\bcategory-parent-(\d+)\b", body) else None,
        "php_warning": bool(re.search(r"(?i)(PHP Warning|PHP Notice|Fatal error|Parse error)", html)),
    }


def main() -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest: dict = {
        "timestamp": ts,
        "checkpoint": "SITE-002-STABLE-LIVE-PDP-BODY-CATEGORY-CLASSES-01",
        "remote": REMOTE,
        "backups": [],
        "deploy": {},
        "qa": [],
        "product_samples": [],
    }

    live = ftp_download(REMOTE)
    if live is not None:
        backup_path = BACKUP / f"catalog__controller__product__product.php.{BACKUP_SUFFIX}"
        backup_path.write_bytes(live)
        manifest["backups"].append({"remote": REMOTE, "backup": str(backup_path), "sha256": sha256_hex(live)})

    patched = LOCAL_PATCHED.read_bytes()
    ftp_upload(REMOTE, patched)
    manifest["deploy"] = {"remote": REMOTE, "sha256": sha256_hex(patched), "bytes": len(patched)}
    manifest["twig_cache_cleared"] = clear_twig_cache()

    for label, plp_url in QA_URLS.items():
        status, plp_html = http_get(plp_url)
        product_url = find_product_url(plp_html)
        entry = {"label": label, "plp_url": plp_url, "plp_status": status}
        if product_url:
            p_status, p_html = http_get(product_url)
            scan = qa_scan(p_html)
            entry.update({"product_url": product_url, "product_status": p_status, **scan})
            manifest["product_samples"].append(entry)
        else:
            entry["error"] = "no product link found on PLP"
            manifest["product_samples"].append(entry)

    out = WORK / "deploy-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
