#!/usr/bin/env python3
"""SITE-002 — rollback SUPER_ATTS presentation only (twig + css), keep controller fix."""
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
from html import unescape

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
BACKUPS = os.path.join(BASE, "backups")
QA_DIR = os.path.join(BASE, "qa", "superatts-presentation-rollback")
WORK = os.path.join(BASE, "superatts-work")

BACKUP_TWIG = os.path.join(BACKUPS, "producthero.twig.pre-superatts-fix.bak")
BACKUP_CSS = os.path.join(BACKUPS, "style.css.pre-superatts-presentation.bak")

REMOTE = {
    "producthero.twig": "catalog/view/theme/default/template/product/producthero.twig",
    "style.css": "assets/css/style.css",
    "product.php": "catalog/controller/product/product.php",
}

SPKB_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)

CONTROLLER_MARKERS = [
    "defined('SUPER_ATTS')",
    "foreach (SUPER_ATTS as $super_attr_id)",
    "$data['super_atts']",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_upload(remote_path, data_bytes):
    ftp = ftp_connect()
    bio = io.BytesIO(data_bytes)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def ftp_download(remote_path):
    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


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


def parse_hero(html):
    m = re.search(r'<section class="product-hero">.*?</section>', html, re.S)
    hero = m.group(0) if m else ""
    props_m = re.search(r'<dl class="product-hero__props">(.*?)</dl>', hero, re.S)
    names = []
    if props_m:
        for dt in re.finditer(r"<dt>(.*?)</dt>", props_m.group(1), re.S):
            names.append(unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", dt.group(1)).strip())))
    return {
        "hero_found": bool(hero),
        "has_specs": "product-hero__specs" in hero,
        "has_primary": "product-hero__props--primary" in hero,
        "has_additional": "product-hero__props--additional" in hero,
        "has_debug": "MARS-SUPER-ATTS-DEBUG" in hero or 'data-debug="super-atts"' in hero,
        "has_original_props": 'class="product-hero__props"' in hero,
        "super_atts_count": len(names),
        "super_atts_names": names,
        "cart_btn": "data-cart-add" in hero,
        "qty": "data-cart-qty" in hero,
        "wishlist": "data-fav-toggle" in hero,
        "compare": "data-compare-toggle" in hero,
        "fancybox": 'data-fancybox="product"' in hero,
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
    }


def verify_controller(remote_php_bytes):
    text = remote_php_bytes.decode("utf-8", "replace")
    return {
        "markers_present": {m: m in text for m in CONTROLLER_MARKERS},
        "all_markers_ok": all(m in text for m in CONTROLLER_MARKERS),
        "sha256": sha256_bytes(remote_php_bytes),
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
            await context.close()
        await browser.close()


def main():
    os.makedirs(QA_DIR, exist_ok=True)

    for label, path in [("twig", BACKUP_TWIG), ("css", BACKUP_CSS)]:
        if not os.path.isfile(path):
            raise SystemExit(f"Missing backup: {path}")

    with open(BACKUP_TWIG, "rb") as f:
        twig_bytes = f.read()
    with open(BACKUP_CSS, "rb") as f:
        css_bytes = f.read()

    pre_php = ftp_download(REMOTE["product.php"])
    pre_controller = verify_controller(pre_php)

    ftp_upload(REMOTE["producthero.twig"], twig_bytes)
    ftp_upload(REMOTE["style.css"], css_bytes)
    cleared, cache_errors = clear_cache()

    post_php = ftp_download(REMOTE["product.php"])
    post_controller = verify_controller(post_php)
    remote_twig = ftp_download(REMOTE["producthero.twig"])
    remote_css = ftp_download(REMOTE["style.css"])

    html = fetch_html(SPKB_URL)
    hero_qa = parse_hero(html)

    desk = os.path.join(QA_DIR, "spkb-18-7-vl5-hero-desktop.png")
    mob = os.path.join(QA_DIR, "spkb-18-7-vl5-hero-mobile.png")
    asyncio.run(screenshot(SPKB_URL, desk, mob))

    checklist = {
        "1_hero_baseline_restored": hero_qa["hero_found"] and hero_qa["has_original_props"],
        "2_no_specs_class": not hero_qa["has_specs"],
        "3_no_primary_class": not hero_qa["has_primary"],
        "4_no_additional_class": not hero_qa["has_additional"],
        "5_no_debug_marker": not hero_qa["has_debug"],
        "6_twig_matches_backup": sha256_bytes(remote_twig) == sha256_bytes(twig_bytes),
        "7_css_matches_backup": sha256_bytes(remote_css) == sha256_bytes(css_bytes),
        "8_controller_super_atts_intact": post_controller["all_markers_ok"]
        and pre_controller["sha256"] == post_controller["sha256"],
        "9_php_ok": hero_qa["php_ok"],
        "10_cart_qty_wishlist_compare": all(
            hero_qa[k] for k in ("cart_btn", "qty", "wishlist", "compare", "fancybox")
        ),
        "11_super_atts_rendered": hero_qa["super_atts_count"] > 0,
    }

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "task": "SUPER_ATTS presentation rollback (twig + css only)",
        "restored_files": REMOTE,
        "backups_used": {
            "producthero.twig": BACKUP_TWIG,
            "style.css": BACKUP_CSS,
        },
        "backup_hashes": {
            "producthero.twig": sha256_bytes(twig_bytes),
            "style.css": sha256_bytes(css_bytes),
        },
        "controller_not_rolled_back": {
            "pre_deploy_sha256": pre_controller["sha256"],
            "post_deploy_sha256": post_controller["sha256"],
            "unchanged": pre_controller["sha256"] == post_controller["sha256"],
            "markers": post_controller["markers_present"],
        },
        "cache_cleared_count": len(cleared),
        "cache_errors": cache_errors,
        "qa_url": SPKB_URL,
        "hero_qa": hero_qa,
        "checklist": checklist,
        "checklist_pass": all(checklist.values()),
        "screenshots": {"desktop": desk, "mobile": mob},
        "rollback_confidence": "HIGH"
        if all(checklist.values())
        else "LOW — see failed checklist items",
    }

    out_path = os.path.join(WORK, "superatts-presentation-rollback-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out["checklist_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
