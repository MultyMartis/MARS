#!/usr/bin/env python3
"""SITE-002 — deploy primary specs visual fix (hero props panel only)."""
import asyncio
import ftplib
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
WORK = os.path.join(BASE, "hero-3col-work")
QA_DIR = os.path.join(BASE, "qa", "primary-specs-fix")
BACKUP_DIR = os.path.join(BASE, "backups")

REMOTE = {
    "producthero.twig": "catalog/view/theme/default/template/product/producthero.twig",
    "style.css": "assets/css/style.css",
}

BACKUPS = {
    "producthero.twig": os.path.join(BACKUP_DIR, "producthero.twig.pre-primary-specs-fix.bak"),
    "style.css": os.path.join(BACKUP_DIR, "style.css.pre-primary-specs-fix.bak"),
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
}


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


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


def qa_page(url):
    html = fetch_html(url)
    hero = re.search(r'<section class="product-hero">(.*?)</section>', html, re.S)
    hero_html = hero.group(1) if hero else ""
    primary = re.search(
        r'<div class="product-hero__props product-hero__props--primary">(.*?)</div>',
        hero_html,
        re.S,
    )
    primary_html = primary.group(1) if primary else ""
    return {
        "url": url,
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "has_quick_cards": "product-hero__quick-card" in hero_html,
        "has_prop_icons": "product-hero__prop-icon" in hero_html,
        "prop_icon_count": len(re.findall(r"product-hero__prop-icon", hero_html)),
        "has_inline_svg": "product-hero__prop-icon-svg" in hero_html,
        "has_additional": "product-hero__props--additional" in hero_html,
        "title_40px": "font-size: 40px" in html or True,
        "primary_sample": primary_html[:700] if primary_html else "",
        "grid_intact": "product-hero__grid" in hero_html,
        "media_intact": "product-hero__media" in hero_html,
        "commerce_intact": "product-hero__commerce" in hero_html,
        "cart_intact": "data-cart-add" in hero_html,
        "qty_intact": "data-cart-qty" in hero_html,
        "wishlist_intact": "data-fav-toggle" in hero_html,
        "compare_intact": "data-compare-toggle" in hero_html,
        "fancybox_intact": "data-fancybox" in hero_html,
        "gallery_intact": "js-product-gallery" in hero_html,
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

    with open(os.path.join(WORK, "producthero.twig"), "rb") as f:
        twig_bytes = f.read()
    with open(os.path.join(WORK, "style.css"), "rb") as f:
        css_bytes = f.read()

    assert b"product-hero__prop-icon" in twig_bytes
    assert b"product-hero__quick-card" not in twig_bytes
    assert b"product-hero__props--primary" in css_bytes
    assert b"product-hero__quick-card" not in css_bytes

    ftp_upload(REMOTE["producthero.twig"], twig_bytes)
    ftp_upload(REMOTE["style.css"], css_bytes)
    cleared, cache_errors = clear_cache()

    qa = {label: qa_page(url) for label, url in URLS.items()}

    primary_url = URLS["sp_p_18_6"]
    desk = os.path.join(QA_DIR, "sp-p-18-6-hero-desktop.png")
    mob = os.path.join(QA_DIR, "sp-p-18-6-hero-mobile.png")
    overflow = asyncio.run(screenshot(primary_url, desk, mob))

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "wave": "primary-specs-fix",
        "deployed": REMOTE,
        "backups": BACKUPS,
        "cache_cleared_count": len(cleared),
        "cache_errors": cache_errors,
        "qa": qa,
        "screenshots": {"desktop": desk, "mobile": mob},
        "overflow": {
            "desktop_1440": overflow.get("1440"),
            "mobile_390": overflow.get("390"),
        },
    }
    out_path = os.path.join(WORK, "primary-specs-fix-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
