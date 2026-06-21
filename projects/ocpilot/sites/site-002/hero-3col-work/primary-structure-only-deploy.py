#!/usr/bin/env python3
"""SITE-002 — rollback pre-primary-specs-fix, then deploy structure-only primary specs."""
import asyncio
import ftplib
import io
import json
import os
import re
import shutil
import sys
import urllib.request
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
WORK = os.path.join(BASE, "hero-3col-work")
QA_DIR = os.path.join(BASE, "qa", "primary-structure-only")
BACKUP_DIR = os.path.join(BASE, "backups")

ROLLBACK_BACKUPS = {
    "producthero.twig": os.path.join(BACKUP_DIR, "producthero.twig.pre-primary-specs-fix.bak"),
    "style.css": os.path.join(BACKUP_DIR, "style.css.pre-primary-specs-fix.bak"),
}

NEW_BACKUPS = {
    "producthero.twig": os.path.join(BACKUP_DIR, "producthero.twig.pre-primary-structure-only.bak"),
    "style.css": os.path.join(BACKUP_DIR, "style.css.pre-primary-structure-only.bak"),
}

REMOTE = {
    "producthero.twig": "catalog/view/theme/default/template/product/producthero.twig",
    "style.css": "assets/css/style.css",
}

FORBIDDEN_CSS = re.compile(
    r"(font-size|font-weight|line-height|color|background|border|border-radius|"
    r"padding|margin|letter-spacing|text-transform|word-break|overflow-wrap|"
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

    forbidden_in_primary_css = FORBIDDEN_CSS.findall(primary_css_block)

    return {
        "phase": phase,
        "url": url,
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "has_quick_cards": "product-hero__quick-card" in hero,
        "has_prop_icons": "product-hero__prop-icon" in hero,
        "has_prop_content": "product-hero__prop-content" in hero,
        "prop_icon_count": len(re.findall(r"product-hero__prop-icon", hero)),
        "has_inline_svg": bool(re.search(r"product-hero__prop-icon[^>]*>[\s\S]*?<svg", hero)),
        "has_fa_primary": "fas fa-" in primary,
        "has_additional": "product-hero__props--additional" in hero,
        "additional_unchanged_sample": additional[:400] if additional else "",
        "primary_sample": primary[:800] if primary else "",
        "grid_intact": "product-hero__grid" in hero,
        "media_intact": "product-hero__media" in hero,
        "commerce_intact": "product-hero__commerce" in hero,
        "cart_intact": "data-cart-add" in hero,
        "qty_intact": "data-cart-qty" in hero,
        "wishlist_intact": "data-fav-toggle" in hero,
        "compare_intact": "data-compare-toggle" in hero,
        "fancybox_intact": "data-fancybox" in hero,
        "gallery_intact": "js-product-gallery" in hero,
        "super_atts_present": "product-hero__specs" in hero,
        "forbidden_css_in_primary_block": forbidden_in_primary_css,
        "primary_css_block": primary_css_block[:1200],
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


def assert_structure_files(twig_bytes, css_bytes):
    assert b"product-hero__prop-content" in twig_bytes
    assert b"product-hero__prop-icon" in twig_bytes
    assert b"<svg" in twig_bytes
    assert b"product-hero__quick-card" not in twig_bytes
    assert b"fas fa-" not in twig_bytes
    assert b"product-hero__props--primary" in css_bytes
    assert b"product-hero__quick-card" not in css_bytes
    assert b"Font Awesome" not in css_bytes

    css_text = css_bytes.decode("utf-8", "replace")
    m = re.search(
        r"\.product-hero__props--primary\s*\{[^}]*\}.*?(?=\.product-hero__props--additional)",
        css_text,
        re.S,
    )
    block = m.group(0) if m else ""
    forbidden = FORBIDDEN_CSS.findall(block)
    if forbidden:
        raise AssertionError(f"Forbidden CSS in primary block: {forbidden}")


def main():
    os.makedirs(QA_DIR, exist_ok=True)

    # STEP 1 — rollback
    rollback_twig = open(ROLLBACK_BACKUPS["producthero.twig"], "rb").read()
    rollback_css = open(ROLLBACK_BACKUPS["style.css"], "rb").read()
    ftp_upload(REMOTE["producthero.twig"], rollback_twig)
    ftp_upload(REMOTE["style.css"], rollback_css)
    cleared1, cache_errors1 = clear_cache()

    qa_rollback = {k: qa_page(v, "rollback") for k, v in URLS.items()}
    rollback_ok = (
        qa_rollback["sp_p_18_6"]["has_quick_cards"]
        and qa_rollback["sp_p_18_6"]["php_ok"]
        and not qa_rollback["sp_p_18_6"]["has_prop_icons"]
    )

    # STEP 2 — backup clean rollback state
    for key, src in ROLLBACK_BACKUPS.items():
        shutil.copy2(src, NEW_BACKUPS[key])

    # STEP 3 — deploy structure-only
    twig_bytes = open(os.path.join(WORK, "producthero.twig"), "rb").read()
    css_bytes = open(os.path.join(WORK, "style.css"), "rb").read()
    assert_structure_files(twig_bytes, css_bytes)

    ftp_upload(REMOTE["producthero.twig"], twig_bytes)
    ftp_upload(REMOTE["style.css"], css_bytes)
    cleared2, cache_errors2 = clear_cache()

    qa_final = {k: qa_page(v, "final") for k, v in URLS.items()}

    primary_url = URLS["sp_p_18_6"]
    desk = os.path.join(QA_DIR, "sp-p-18-6-hero-desktop.png")
    mob = os.path.join(QA_DIR, "sp-p-18-6-hero-mobile.png")
    overflow = asyncio.run(screenshot(primary_url, desk, mob))

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "wave": "primary-structure-only",
        "rollback": {
            "sources": ROLLBACK_BACKUPS,
            "remote": REMOTE,
            "cache_cleared_count": len(cleared1),
            "cache_errors": cache_errors1,
            "verified": rollback_ok,
            "qa": qa_rollback,
        },
        "new_backups": NEW_BACKUPS,
        "deployed": REMOTE,
        "cache_cleared_count": len(cleared2),
        "cache_errors": cache_errors2,
        "qa": qa_final,
        "screenshots": {"desktop": desk, "mobile": mob},
        "overflow": {
            "desktop_1440": overflow.get("1440"),
            "mobile_390": overflow.get("390"),
        },
    }
    out_path = os.path.join(WORK, "primary-structure-only-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
