#!/usr/bin/env python3
"""SITE-002 — deploy primary specs FA icon switch (producthero.twig only)."""
import asyncio
import ftplib
import hashlib
import io
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
WORK = os.path.join(BASE, "fa-icon-work")
QA_DIR = os.path.join(BASE, "qa", "primary-fa-icon-switch")
BACKUP_DIR = os.path.join(BASE, "backups")
BASELINE_CSS_SHA = "0a6e8d4e2035ba12a2095966213a6d5669260203a806efd62ab00c876c405ef6"

REMOTE_TWIG = "catalog/view/theme/default/template/product/producthero.twig"
REMOTE_CSS = "assets/css/style.css"
BACKUP_TWIG = os.path.join(BACKUP_DIR, "producthero.twig.pre-primary-fa-icon-switch.bak")
LOCAL_TWIG = os.path.join(WORK, "producthero.twig")

SPKB_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)

EXPECTED_ICONS = {
    "Длина": "fal fa-ruler-horizontal",
    "Ширина": "fal fa-arrows-alt-h",
    "Высота": "fal fa-arrows-alt-v",
    "Масса": "fas fa-weight-hanging",
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
    ftp.cwd("/")
    parts = os.path.dirname(remote_path).replace("\\", "/").split("/")
    for part in parts:
        if not part:
            continue
        try:
            ftp.cwd(part)
        except ftplib.error_perm:
            ftp.mkd(part)
            ftp.cwd(part)
    bio = io.BytesIO(data_bytes)
    ftp.storbinary("STOR " + os.path.basename(remote_path), bio)
    ftp.quit()


def clear_cache():
    cleared = []
    errors = []
    for cache_dir in ("system/storage/cache", "system/storage/cache/template"):
        ftp = ftp_connect()
        try:
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
                try:
                    ftp.delete(name)
                    cleared.append(f"{cache_dir}/{name}")
                except ftplib.error_perm as e:
                    errors.append(f"{name}: {e}")
        except Exception as e:
            errors.append(f"{cache_dir}: {e}")
        finally:
            ftp.quit()
    return cleared, errors


def fetch_html(url):
    req = urllib.request.Request(url, headers={"Cookie": "beget=begetok"})
    return urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def qa_spkb(url):
    html = fetch_html(url)
    hero = re.search(r'<section class="product-hero">(.*?)</section>', html, re.S)
    hero_html = hero.group(1) if hero else ""
    primary = re.search(
        r'<dl class="product-hero__props product-hero__props--primary">(.*?)</dl>',
        hero_html,
        re.S,
    )
    primary_html = primary.group(1) if primary else ""

    icon_checks = {}
    for label, icon_class in EXPECTED_ICONS.items():
        block = re.search(
            rf'product-hero__prop--primary.*?<i class="([^"]+)".*?<dt>[^<]*{re.escape(label)}',
            primary_html,
            re.S | re.I,
        )
        if block:
            icon_checks[label] = {
                "expected": icon_class,
                "actual": block.group(1),
                "ok": icon_class in block.group(1),
            }
        else:
            icon_checks[label] = {"expected": icon_class, "actual": None, "ok": False}

    return {
        "url": url,
        "php_ok": "Fatal error" not in html and "Parse error" not in html and "Twig_Error" not in html,
        "has_primary": "product-hero__props--primary" in hero_html,
        "icon_checks": icon_checks,
        "all_icons_ok": all(v["ok"] for v in icon_checks.values()),
        "fad_removed_from_primary": "fad fa-weight-hanging" not in primary_html,
        "cart_intact": "data-cart-add" in hero_html,
        "qty_intact": "data-cart-qty" in hero_html,
        "wishlist_intact": "data-fav-toggle" in hero_html,
        "compare_intact": "data-compare-toggle" in hero_html,
        "fancybox_intact": "data-fancybox" in hero_html,
        "gallery_intact": "js-product-gallery" in hero_html,
        "primary_sample": primary_html[:900] if primary_html else "",
    }


async def screenshot(url, out_desktop, out_mobile):
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        from playwright.async_api import async_playwright

    os.makedirs(os.path.dirname(out_desktop), exist_ok=True)
    overflow = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for viewport, path in [
            ({"width": 1440, "height": 900}, out_desktop),
            ({"width": 390, "height": 844}, out_mobile),
        ]:
            context = await browser.new_context(
                viewport=viewport,
                extra_http_headers={"Cookie": "beget=begetok"},
            )
            page = await context.new_page()
            await page.goto(url, wait_until="networkidle", timeout=90000)
            await page.wait_for_selector(".product-hero__props--primary", timeout=30000)
            hero = page.locator(".product-hero")
            await hero.screenshot(path=path)
            sw = await page.evaluate(
                "() => Math.max(document.documentElement.scrollWidth, document.body.scrollWidth) > window.innerWidth + 1"
            )
            overflow[str(viewport["width"])] = sw
            await context.close()
        await browser.close()
    return overflow


def main():
    os.makedirs(QA_DIR, exist_ok=True)

    with open(LOCAL_TWIG, "rb") as f:
        twig_bytes = f.read()

    assert b"prop_name = a.name|lower" in twig_bytes
    assert b"fal fa-ruler-horizontal" in twig_bytes
    assert b"fas fa-weight-hanging" in twig_bytes
    assert b"fad fa-weight-hanging" not in twig_bytes

    with open(BACKUP_TWIG, "rb") as f:
        backup_bytes = f.read()
    assert sha256_hex(backup_bytes) == "92e74fd92329bd5451b6985820d5e60bce4b2233f9f3d549bb1f4edf9de840e9"

    css_before = ftp_download(REMOTE_CSS)
    css_sha_before = sha256_hex(css_before)

    ftp_upload(REMOTE_TWIG, twig_bytes)
    cleared, cache_errors = clear_cache()

    css_after = ftp_download(REMOTE_CSS)
    css_sha_after = sha256_hex(css_after)
    remote_twig_after = ftp_download(REMOTE_TWIG)

    qa = qa_spkb(SPKB_URL)

    desk = os.path.join(QA_DIR, "spkb-18-7-vl5-hero-desktop.png")
    mob = os.path.join(QA_DIR, "spkb-18-7-vl5-hero-mobile.png")
    overflow = asyncio.run(screenshot(SPKB_URL, desk, mob))

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "wave": "primary-fa-icon-switch",
        "backup_path": BACKUP_TWIG,
        "changed_file": REMOTE_TWIG,
        "local_changed_file": LOCAL_TWIG,
        "style_css_unchanged": css_sha_before == css_sha_after == BASELINE_CSS_SHA,
        "style_css_sha256": css_sha_after,
        "twig_sha256_deployed": sha256_hex(remote_twig_after),
        "twig_sha256_local": sha256_hex(twig_bytes),
        "cache_cleared_count": len(cleared),
        "cache_errors": cache_errors,
        "qa": qa,
        "screenshots": {"desktop": desk, "mobile": mob},
        "overflow": {
            "desktop_1440": overflow.get("1440"),
            "mobile_390": overflow.get("390"),
        },
        "rollback": {
            "restore_from": BACKUP_TWIG,
            "remote_path": REMOTE_TWIG,
            "note": "FTP upload backup twig, then clear OC template cache",
        },
    }
    out_path = os.path.join(WORK, "primary-fa-icon-switch-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
