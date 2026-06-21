#!/usr/bin/env python3
"""SITE-002 — deploy product hero 3-column layout (layout-only)."""
import asyncio
import ftplib
import io
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from html import unescape

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
WORK = os.path.join(BASE, "hero-3col-work")
QA_DIR = os.path.join(BASE, "qa", "hero-3col")
BACKUP_DIR = os.path.join(BASE, "backups")

REMOTE = {
    "producthero.twig": "catalog/view/theme/default/template/product/producthero.twig",
    "style.css": "assets/css/style.css",
}

URLS = {
    "sp_p_18_6": (
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
        "stoly-serii-premium/stoly-premium-600/"
        "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
    ),
    "spkb_multi": (
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
        "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
        "stol-tumba-spkb-18-7-vl5-1800h700h850"
    ),
    "vmc_request": (
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"
        "vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850"
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


def qa_page(url):
    html = fetch_html(url)
    hero = re.search(r'<section class="product-hero">(.*?)</section>', html, re.S)
    hero_html = hero.group(1) if hero else ""
    specs = len(re.findall(r"product-hero__specs", hero_html))
    thumbs = len(re.findall(r"js-product-thumbs", hero_html))
    slides = len(re.findall(r"product-gallery__fancybox", hero_html))
    overflow = False
    return {
        "url": url,
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "has_identity": "product-hero__identity" in hero_html,
        "has_commerce": "product-hero__commerce" in hero_html,
        "has_media": "product-hero__media" in hero_html,
        "specs_blocks": specs,
        "gallery_slides": slides,
        "has_thumbs": thumbs > 0,
        "cart_btn": "data-cart-add" in hero_html,
        "qty": "data-cart-qty" in hero_html,
        "wishlist": "data-fav-toggle" in hero_html,
        "compare": "data-compare-toggle" in hero_html,
        "fancybox": 'data-fancybox="product"' in hero_html,
        "request_btn": "Запросить цену" in hero_html,
        "super_atts_visible": "product-hero__props" in hero_html,
        "overflow_hint": overflow,
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
            await page.wait_for_selector(".product-hero", timeout=30000)
            hero = page.locator(".product-hero")
            await hero.screenshot(path=path)
            sw = await page.evaluate(
                "() => Math.max(document.documentElement.scrollWidth, document.body.scrollWidth) > window.innerWidth + 1"
            )
            globals()["_overflow_" + str(viewport["width"])] = sw
            await context.close()
        await browser.close()


def main():
    os.makedirs(QA_DIR, exist_ok=True)
    twig_path = os.path.join(WORK, "producthero.twig")
    css_path = os.path.join(WORK, "style.css")

    with open(twig_path, "rb") as f:
        twig_bytes = f.read()
    with open(css_path, "rb") as f:
        css_bytes = f.read()

    assert b"product-hero__identity" in twig_bytes
    assert b"product-hero__commerce" in twig_bytes
    assert b"minmax(0, 2fr)" in css_bytes

    ftp_upload(REMOTE["producthero.twig"], twig_bytes)
    ftp_upload(REMOTE["style.css"], css_bytes)
    cleared, cache_errors = clear_cache()

    qa = {}
    for label, url in URLS.items():
        qa[label] = qa_page(url)

    primary_url = URLS["sp_p_18_6"]
    desk = os.path.join(QA_DIR, "sp-p-18-6-hero-desktop.png")
    mob = os.path.join(QA_DIR, "sp-p-18-6-hero-mobile.png")
    asyncio.run(screenshot(primary_url, desk, mob))

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "wave": "hero-3col",
        "deployed": REMOTE,
        "backups": {
            "producthero.twig": os.path.join(BACKUP_DIR, "producthero.twig.pre-hero-3col.bak"),
            "style.css": os.path.join(BACKUP_DIR, "style.css.pre-hero-3col.bak"),
        },
        "cache_cleared_count": len(cleared),
        "cache_errors": cache_errors,
        "qa": qa,
        "screenshots": {"desktop": desk, "mobile": mob},
        "overflow": {
            "desktop_1440": globals().get("_overflow_1440"),
            "mobile_390": globals().get("_overflow_390"),
        },
        "rollback_procedure": [
            f"Upload {os.path.join(BACKUP_DIR, 'producthero.twig.pre-hero-3col.bak')} -> {REMOTE['producthero.twig']}",
            f"Upload {os.path.join(BACKUP_DIR, 'style.css.pre-hero-3col.bak')} -> {REMOTE['style.css']}",
            "Clear system/storage/cache/template/",
        ],
    }
    out_path = os.path.join(WORK, "hero-3col-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
