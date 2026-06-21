#!/usr/bin/env python3
"""SITE-002 — deploy primary specs layout fix (positioning-only CSS)."""
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
QA_DIR = os.path.join(BASE, "qa", "primary-layout-fix")
BACKUP_DIR = os.path.join(BASE, "backups")

BACKUPS = {
    "producthero.twig": os.path.join(BACKUP_DIR, "producthero.twig.pre-primary-layout-fix.bak"),
    "style.css": os.path.join(BACKUP_DIR, "style.css.pre-primary-layout-fix.bak"),
}

REMOTE = {
    "producthero.twig": "catalog/view/theme/default/template/product/producthero.twig",
    "style.css": "assets/css/style.css",
}

FORBIDDEN_CSS = re.compile(
    r"(font-size|font-weight|line-height|color|background|border|border-radius|"
    r"letter-spacing|text-transform|word-break|overflow-wrap|"
    r"box-shadow|text-shadow|opacity)\s*:",
    re.I,
)

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


def qa_page(url, phase):
    html = fetch_html(url)
    hero_m = re.search(r'<section class="product-hero">(.*?)</section>', html, re.S)
    hero = hero_m.group(1) if hero_m else ""
    primary_m = re.search(
        r'<div class="product-hero__props product-hero__props--primary">(.*?)</div>',
        hero,
        re.S,
    )
    primary = primary_m.group(1) if primary_m else ""
    additional_m = re.search(
        r'<dl class="product-hero__props product-hero__props--additional">(.*?)</dl>',
        hero,
        re.S,
    )
    additional = additional_m.group(1) if additional_m else ""

    css_req = urllib.request.Request(
        "https://zpm.new-site.space/assets/css/style.css",
        headers={"Cookie": "beget=begetok"},
    )
    live_css = urllib.request.urlopen(css_req, timeout=60).read().decode("utf-8", "replace")
    primary_css_block = ""
    m = re.search(
        r"\.product-hero__props--primary\s*\{[^}]*\}.*?(?=\.product-hero__props--additional)",
        live_css,
        re.S,
    )
    if m:
        primary_css_block = m.group(0)

    mobile_m = re.search(
        r"@media \(max-width: 640px\)\s*\{[^}]*\.product-hero__props--primary[^}]*\}",
        live_css,
        re.S,
    )
    mobile_block = mobile_m.group(0) if mobile_m else ""

    forbidden_in_primary_css = FORBIDDEN_CSS.findall(primary_css_block + mobile_block)

    return {
        "phase": phase,
        "url": url,
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "has_prop_icons": "product-hero__prop-icon" in hero,
        "has_prop_content": "product-hero__prop-content" in hero,
        "prop_icon_count": len(re.findall(r"product-hero__prop-icon", hero)),
        "prop_count": len(re.findall(r'class="product-hero__prop"', primary)),
        "has_inline_svg": bool(re.search(r"product-hero__prop-icon[^>]*>[\s\S]*?<svg", hero)),
        "has_additional": "product-hero__props--additional" in hero,
        "additional_has_prop_icon": "product-hero__prop-icon" in additional,
        "grid_4col": "repeat(4" in primary_css_block,
        "grid_gap_12": "gap: 12px" in primary_css_block,
        "prop_gap_8": "gap: 8px" in primary_css_block,
        "prop_padding": "padding: 10px 12px" in primary_css_block,
        "icon_em_size": "1.6em" in primary_css_block,
        "mobile_2col": "repeat(2" in mobile_block,
        "grid_intact": "product-hero__grid" in hero,
        "media_intact": "product-hero__media" in hero,
        "commerce_intact": "product-hero__commerce" in hero,
        "cart_intact": "data-cart-add" in hero,
        "qty_intact": "data-cart-qty" in hero,
        "wishlist_intact": "data-fav-toggle" in hero,
        "compare_intact": "data-compare-toggle" in hero,
        "fancybox_intact": "data-fancybox" in hero,
        "gallery_intact": "js-product-gallery" in hero,
        "forbidden_css_in_primary_block": forbidden_in_primary_css,
        "primary_css_block": primary_css_block[:1500],
        "mobile_css_block": mobile_block[:500],
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


def assert_layout_css(css_bytes):
    css_text = css_bytes.decode("utf-8", "replace")
    m = re.search(
        r"\.product-hero__props--primary\s*\{[^}]*\}.*?(?=\.product-hero__props--additional)",
        css_text,
        re.S,
    )
    block = m.group(0) if m else ""
    if "gap: 12px" not in block:
        raise AssertionError("Missing gap: 12px on primary grid")
    if "padding: 10px 12px" not in block:
        raise AssertionError("Missing padding on primary prop")
    if "1.6em" not in block:
        raise AssertionError("Missing 1.6em icon sizing")
    mobile_m = re.search(
        r"@media \(max-width: 640px\)\s*\{[^}]*\.product-hero__props--primary[^}]*\}",
        css_text,
        re.S,
    )
    if not mobile_m or "repeat(2" not in mobile_m.group(0):
        raise AssertionError("Missing mobile 2-col media query")
    forbidden = FORBIDDEN_CSS.findall(block)
    if forbidden:
        raise AssertionError(f"Forbidden CSS in primary block: {forbidden}")


def main():
    os.makedirs(QA_DIR, exist_ok=True)

    twig_bytes = open(os.path.join(WORK, "producthero.twig"), "rb").read()
    css_bytes = open(os.path.join(WORK, "style.css"), "rb").read()
    assert_layout_css(css_bytes)

    ftp_upload(REMOTE["producthero.twig"], twig_bytes)
    ftp_upload(REMOTE["style.css"], css_bytes)
    cleared, cache_errors = clear_cache()

    qa_final = {k: qa_page(v, "final") for k, v in URLS.items()}

    primary_url = URLS["sp_p_18_6"]
    desk = os.path.join(QA_DIR, "sp-p-18-6-hero-desktop.png")
    mob = os.path.join(QA_DIR, "sp-p-18-6-hero-mobile.png")
    overflow = asyncio.run(screenshot(primary_url, desk, mob))

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "wave": "primary-layout-fix",
        "backups": BACKUPS,
        "deployed": REMOTE,
        "cache_cleared_count": len(cleared),
        "cache_errors": cache_errors,
        "qa": qa_final,
        "screenshots": {"desktop": desk, "mobile": mob},
        "overflow": {
            "desktop_1440": overflow.get("1440"),
            "mobile_390": overflow.get("390"),
        },
    }
    out_path = os.path.join(WORK, "primary-layout-fix-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
