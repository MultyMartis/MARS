#!/usr/bin/env python3
"""SITE-002 — deploy super_atts hero presentation (debug removal + compact layout)."""
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
WORK = os.path.join(BASE, "superatts-work")
QA_DIR = os.path.join(BASE, "qa", "superatts-presentation")

REMOTE = {
    "producthero.twig": "catalog/view/theme/default/template/product/producthero.twig",
    "style.css": "assets/css/style.css",
}

URLS = {
    "spkb": (
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
        "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
        "stol-tumba-spkb-18-7-vl5-1800h700h850"
    ),
    "vmc": (
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


def parse_hero_specs(html):
    m = re.search(
        r'<div class="product-hero__specs[^"]*">(.*?)</div>\s*<div class="product-hero__actions-wrap">',
        html,
        re.S,
    )
    if not m:
        return {"found": False, "primary": 0, "additional": 0, "names": []}
    block = m.group(1)
    primary = len(re.findall(r'product-hero__props--primary', block))
    additional = len(re.findall(r'product-hero__props--additional', block))
    names = []
    for dt in re.finditer(r"<dt>(.*?)</dt>", block, re.S):
        names.append(unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", dt.group(1)).strip())))
    return {
        "found": True,
        "primary_blocks": primary,
        "additional_blocks": additional,
        "count": len(names),
        "names": names,
        "split": "product-hero__specs--split" in m.group(0),
    }


def qa_page(url):
    html = fetch_html(url)
    hero_box = re.search(r"\.product-hero\s*\{[^}]*\}", html)
    specs = parse_hero_specs(html)
    return {
        "url": url,
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "debug_removed": "MARS-SUPER-ATTS-DEBUG" not in html
        and 'data-debug="super-atts"' not in html,
        "cart_btn": "data-cart-add" in html,
        "qty": "data-cart-qty" in html,
        "wishlist": "data-fav-toggle" in html,
        "compare": "data-compare-toggle" in html,
        "fancybox": 'data-fancybox="product"' in html,
        "specs": specs,
        "hero_height_px": None,
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
            box = await hero.bounding_box()
            await hero.screenshot(path=path)
            if viewport["width"] == 1440 and box:
                globals()["_hero_h"] = box["height"]
            await context.close()
        await browser.close()


def main():
    os.makedirs(QA_DIR, exist_ok=True)
    twig_path = os.path.join(WORK, "producthero.live.twig")
    css_path = os.path.join(WORK, "style.live.css")

    with open(twig_path, "rb") as f:
        twig_bytes = f.read()
    with open(css_path, "rb") as f:
        css_bytes = f.read()

    assert b"MARS-SUPER-ATTS-DEBUG" not in twig_bytes
    assert b'data-debug="super-atts"' not in twig_bytes

    ftp_upload(REMOTE["producthero.twig"], twig_bytes)
    ftp_upload(REMOTE["style.css"], css_bytes)
    cleared, cache_errors = clear_cache()

    qa = {}
    for label, url in URLS.items():
        qa[label] = qa_page(url)

    spkb_url = URLS["spkb"]
    desk = os.path.join(QA_DIR, "spkb-18-7-vl5-hero-desktop.png")
    mob = os.path.join(QA_DIR, "spkb-18-7-vl5-hero-mobile.png")
    asyncio.run(screenshot(spkb_url, desk, mob))

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "deployed": REMOTE,
        "backups": {
            "producthero": os.path.join(BASE, "backups", "producthero.twig.debug-before-cleanup.bak"),
            "style": os.path.join(BASE, "backups", "style.css.pre-superatts-presentation.bak"),
        },
        "cache_cleared_count": len(cleared),
        "cache_errors": cache_errors,
        "qa": qa,
        "screenshots": {"desktop": desk, "mobile": mob},
    }
    out_path = os.path.join(WORK, "superatts-presentation-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
