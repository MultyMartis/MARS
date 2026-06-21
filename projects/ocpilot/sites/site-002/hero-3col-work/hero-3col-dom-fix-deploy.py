#!/usr/bin/env python3
"""SITE-002 — deploy product hero 3-column DOM structure fix."""
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
QA_DIR = os.path.join(BASE, "qa", "hero-3col-dom-fix")
BACKUP_DIR = os.path.join(BASE, "backups")

REMOTE = {
    "producthero.twig": "catalog/view/theme/default/template/product/producthero.twig",
    "style.css": "assets/css/style.css",
}

BACKUPS = {
    "producthero.twig": os.path.join(BACKUP_DIR, "producthero.twig.pre-3col-dom-fix.bak"),
    "style.css": os.path.join(BACKUP_DIR, "style.css.pre-3col-dom-fix.bak"),
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


def dom_structure_qa(hero_html):
    grid = re.search(
        r'<div class="product-hero__grid">(.*?)</div>\s*</div>\s*</section>',
        hero_html,
        re.S,
    )
    grid_html = grid.group(1) if grid else hero_html

    direct_cols = re.findall(
        r'<div class="product-hero__col product-hero__col--(media|info|commerce)">',
        grid_html,
    )
    legacy_direct = re.findall(
        r'(?<!product-hero__col--)\bclass="product-hero__(media|identity|specs|other|commerce)"',
        grid_html,
    )

    media_in_col = "product-hero__col--media" in grid_html and "product-hero__media" in grid_html
    identity_in_info = (
        "product-hero__col--info" in grid_html
        and "product-hero__identity" in grid_html
        and grid_html.find("product-hero__col--info")
        < grid_html.find("product-hero__identity")
    )
    specs_in_info = "product-hero__specs" in grid_html and "product-hero__col--info" in grid_html
    other_in_commerce = "product-hero__other" in grid_html and "product-hero__col--commerce" in grid_html
    commerce_in_commerce = "product-hero__commerce" in grid_html

    return {
        "grid_direct_children_count": len(direct_cols),
        "grid_direct_children_classes": [f"product-hero__col--{c}" for c in direct_cols],
        "three_col_layout_ok": direct_cols == ["media", "info", "commerce"],
        "no_legacy_grid_items_as_direct": len(legacy_direct) == 0,
        "media_in_col_media": media_in_col,
        "identity_in_col_info": identity_in_info,
        "specs_in_col_info": specs_in_info,
        "other_in_col_commerce": other_in_commerce,
        "commerce_in_col_commerce": commerce_in_commerce,
    }


def qa_page(url):
    html = fetch_html(url)
    hero = re.search(r'<section class="product-hero">(.*?)</section>', html, re.S)
    hero_html = hero.group(1) if hero else ""
    dom = dom_structure_qa(hero_html)
    return {
        "url": url,
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "dom": dom,
        "has_identity": "product-hero__identity" in hero_html,
        "has_commerce": "product-hero__commerce" in hero_html,
        "has_media": "product-hero__media" in hero_html,
        "specs_blocks": len(re.findall(r"product-hero__specs", hero_html)),
        "gallery_slides": len(re.findall(r"product-gallery__fancybox", hero_html)),
        "has_thumbs": "js-product-thumbs" in hero_html,
        "cart_btn": "data-cart-add" in hero_html,
        "qty": "data-cart-qty" in hero_html,
        "wishlist": "data-fav-toggle" in hero_html,
        "compare": "data-compare-toggle" in hero_html,
        "fancybox": 'data-fancybox="product"' in hero_html,
        "request_btn": "Запросить цену" in hero_html,
        "super_atts_visible": "product-hero__props" in hero_html,
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
            await page.wait_for_selector(".product-hero", timeout=30000)
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
    twig_path = os.path.join(WORK, "producthero.twig")
    css_path = os.path.join(WORK, "style.css")

    with open(twig_path, "rb") as f:
        twig_bytes = f.read()
    with open(css_path, "rb") as f:
        css_bytes = f.read()

    assert b"product-hero__col--media" in twig_bytes
    assert b"product-hero__col--info" in twig_bytes
    assert b"product-hero__col--commerce" in twig_bytes
    assert b".product-hero__col {" in css_bytes
    assert b"align-items: stretch" in css_bytes

    ftp_upload(REMOTE["producthero.twig"], twig_bytes)
    ftp_upload(REMOTE["style.css"], css_bytes)
    cleared, cache_errors = clear_cache()

    qa = {}
    for label, url in URLS.items():
        qa[label] = qa_page(url)

    primary_url = URLS["sp_p_18_6"]
    desk = os.path.join(QA_DIR, "sp-p-18-6-hero-desktop.png")
    mob = os.path.join(QA_DIR, "sp-p-18-6-hero-mobile.png")
    overflow = asyncio.run(screenshot(primary_url, desk, mob))

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "wave": "hero-3col-dom-fix",
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
        "rollback_procedure": [
            f"Upload {BACKUPS['producthero.twig']} -> {REMOTE['producthero.twig']}",
            f"Upload {BACKUPS['style.css']} -> {REMOTE['style.css']}",
            "Clear system/storage/cache/template/",
        ],
    }
    out_path = os.path.join(WORK, "hero-3col-dom-fix-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
