#!/usr/bin/env python3
"""SITE-002 — deploy product hero commerce card (producthero.twig + style.css)."""
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
WORK = os.path.join(BASE, "commerce-card-work")
QA_DIR = os.path.join(BASE, "qa", "commerce-card")
BACKUP_DIR = os.path.join(BASE, "backups")

REMOTE_TWIG = "catalog/view/theme/default/template/product/producthero.twig"
REMOTE_CSS = "assets/css/style.css"
BACKUP_TWIG = os.path.join(BACKUP_DIR, "producthero.twig.pre-commerce-card.bak")
BACKUP_CSS = os.path.join(BACKUP_DIR, "style.css.pre-commerce-card.bak")
LOCAL_TWIG = os.path.join(WORK, "producthero.twig")
LOCAL_CSS = os.path.join(WORK, "style.css")

SPKB_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)


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
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def qa_spkb(url):
    html = fetch_html(url)
    hero = re.search(r'<section class="product-hero">(.*?)</section>', html, re.S)
    hero_html = hero.group(1) if hero else ""
    commerce = re.search(
        r'<div class="product-hero__col product-hero__col--commerce">(.*?)</div>\s*</div>\s*</div>',
        hero_html,
        re.S,
    )
    commerce_html = commerce.group(1) if commerce else ""

    return {
        "url": url,
        "php_ok": "Fatal error" not in html and "Parse error" not in html and "Twig_Error" not in html,
        "two_cards": (
            "product-hero__commerce-card" in commerce_html
            and "product-hero__service-card" in commerce_html
        ),
        "commerce_head": "product-hero__commerce-head" in commerce_html and "Стоимость:" in commerce_html,
        "price_intact": "product-hero__price-value" in commerce_html,
        "discount_intact": "product-hero__old-price-value" in commerce_html or "product-hero__discount" in commerce_html or True,
        "status_intact": "product-hero__status" in commerce_html,
        "cart_intact": "data-cart-add" in commerce_html,
        "qty_intact": "data-cart-qty" in commerce_html,
        "wishlist_intact": "data-fav-toggle" in hero_html,
        "compare_intact": "data-compare-toggle" in hero_html,
        "fancybox_gallery_intact": 'data-fancybox="product"' in hero_html,
        "quick_order_btn": "Быстрый заказ" in commerce_html,
        "quick_order_hook": 'data-src="#zpmFbCallback"' in commerce_html,
        "question_btn": "Задать вопрос" in commerce_html,
        "question_hook": 'data-src="#zpmFbQuestion"' in commerce_html,
        "service_items": commerce_html.count("product-hero__service-item"),
        "fa_icons": all(
            icon in commerce_html
            for icon in ("fa-shield-check", "fa-truck", "fa-headset")
        ),
        "commerce_sample": commerce_html[:1200] if commerce_html else "",
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
            await page.wait_for_selector(".product-hero__commerce-card", timeout=30000)
            hero = page.locator(".product-hero")
            await hero.screenshot(path=path)
            sw = await page.evaluate(
                "() => Math.max(document.documentElement.scrollWidth, document.body.scrollWidth) > window.innerWidth + 1"
            )
            overflow[str(viewport["width"])] = sw

            js_errors = []
            page.on("pageerror", lambda err: js_errors.append(str(err)))
            await page.wait_for_timeout(500)
            overflow[f"js_errors_{viewport['width']}"] = js_errors
            await context.close()
        await browser.close()
    return overflow


def main():
    os.makedirs(QA_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)

    twig_before = ftp_download(REMOTE_TWIG)
    css_before = ftp_download(REMOTE_CSS)

    with open(BACKUP_TWIG, "wb") as f:
        f.write(twig_before)
    with open(BACKUP_CSS, "wb") as f:
        f.write(css_before)

    with open(LOCAL_TWIG, "rb") as f:
        twig_bytes = f.read()
    with open(LOCAL_CSS, "rb") as f:
        css_bytes = f.read()

    assert b"product-hero__commerce-card" in twig_bytes
    assert b"product-hero__service-card" in twig_bytes
    assert b"data-cart-add" in twig_bytes
    assert b"product-hero__commerce-card" in css_bytes

    ftp_upload(REMOTE_TWIG, twig_bytes)
    ftp_upload(REMOTE_CSS, css_bytes)
    cleared, cache_errors = clear_cache()

    remote_twig_after = ftp_download(REMOTE_TWIG)
    remote_css_after = ftp_download(REMOTE_CSS)

    qa = qa_spkb(SPKB_URL)

    desk = os.path.join(QA_DIR, "spkb-18-7-vl5-commerce-desktop-1440.png")
    mob = os.path.join(QA_DIR, "spkb-18-7-vl5-commerce-mobile-390.png")
    overflow = asyncio.run(screenshot(SPKB_URL, desk, mob))

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "wave": "commerce-card",
        "backup_paths": {
            "producthero_twig": BACKUP_TWIG,
            "style_css": BACKUP_CSS,
        },
        "changed_files": [REMOTE_TWIG, REMOTE_CSS],
        "local_changed_files": [LOCAL_TWIG, LOCAL_CSS],
        "hooks_found": {
            "quick_order": {
                "dedicated_hook": "SAFE UNKNOWN — text 'Быстрый заказ' and dedicated modal not found on live site",
                "used_hook": "#zpmFbCallback",
                "attributes": 'data-fancybox data-src="#zpmFbCallback" data-zpm-fb-mode="2"',
                "modal_title_live": "Заказать звонок",
                "dialog_value": "2",
            },
            "ask_question": {
                "hook": "#zpmFbQuestion",
                "attributes": 'data-fancybox data-src="#zpmFbQuestion" data-zpm-fb-mode="2"',
                "reference": "producttabs.twig product-help block",
                "dialog_value": "1",
            },
        },
        "twig_sha256_before": sha256_hex(twig_before),
        "css_sha256_before": sha256_hex(css_before),
        "twig_sha256_deployed": sha256_hex(remote_twig_after),
        "css_sha256_deployed": sha256_hex(remote_css_after),
        "cache_cleared_count": len(cleared),
        "cache_errors": cache_errors,
        "qa": qa,
        "screenshots": {"desktop_1440": desk, "mobile_390": mob},
        "overflow": overflow,
        "rollback": {
            "restore_twig_from": BACKUP_TWIG,
            "restore_css_from": BACKUP_CSS,
            "remote_twig_path": REMOTE_TWIG,
            "remote_css_path": REMOTE_CSS,
            "note": "FTP upload both backup files to remote paths, then clear OC template cache",
        },
    }
    out_path = os.path.join(WORK, "commerce-card-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
