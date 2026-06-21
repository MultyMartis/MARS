#!/usr/bin/env python3
"""SITE-002 — rollback to hero 3-column DOM fix baseline (twig + css only)."""
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
QA_DIR = os.path.join(BASE, "qa", "hero-3col-baseline-rollback")
WORK = os.path.join(BASE, "hero-3col-work")

RESTORE_TWIG = os.path.join(BACKUPS, "producthero.twig.pre-quick-props.bak")
RESTORE_CSS = os.path.join(BACKUPS, "style.css.pre-quick-props.bak")

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

POST_CHANGE_MARKERS = [
    "quick-card",
    "product-hero__prop-icon",
    "prop-icon",
    "fa-solid",
    "fontawesome",
    "primary-layout-fix",
    "primary-structure-only",
    "primary-specs-fix",
]

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
    return {
        "grid_direct_children_count": len(direct_cols),
        "grid_direct_children_classes": [f"product-hero__col--{c}" for c in direct_cols],
        "three_col_layout_ok": direct_cols == ["media", "info", "commerce"],
        "media_in_col_media": "product-hero__col--media" in grid_html and "product-hero__media" in grid_html,
        "identity_in_col_info": "product-hero__identity" in grid_html and "product-hero__col--info" in grid_html,
        "specs_in_col_info": "product-hero__specs" in grid_html,
        "other_in_col_commerce": "product-hero__other" in grid_html and "product-hero__col--commerce" in grid_html,
        "commerce_in_col_commerce": "product-hero__commerce" in grid_html,
    }


def parse_hero(html):
    m = re.search(r'<section class="product-hero">(.*?)</section>', html, re.S)
    hero = m.group(0) if m else ""
    hero_inner = m.group(1) if m else ""
    dom = dom_structure_qa(hero)
    names = []
    for dt in re.finditer(r"<dt>(.*?)</dt>", hero, re.S):
        names.append(unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", dt.group(1)).strip())))
    return {
        "hero_found": bool(hero),
        "dom": dom,
        "post_change_markers": {k: k in hero for k in POST_CHANGE_MARKERS},
        "any_post_change_marker": any(k in hero for k in POST_CHANGE_MARKERS),
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
    os.makedirs(BACKUPS, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")

    for label, path in [("twig", RESTORE_TWIG), ("css", RESTORE_CSS)]:
        if not os.path.isfile(path):
            raise SystemExit(f"Missing restore backup: {path}")

    new_backups = {}
    pre_live = {}
    for key in ("producthero.twig", "style.css"):
        data = ftp_download(REMOTE[key])
        pre_live[key] = {"bytes": len(data), "sha256": sha256_bytes(data)}
        backup_name = f"{key}.{ts}.pre-hero-3col-baseline-rollback.bak"
        backup_path = os.path.join(BACKUPS, backup_name)
        with open(backup_path, "wb") as f:
            f.write(data)
        new_backups[key] = backup_path

    pre_php = ftp_download(REMOTE["product.php"])
    pre_controller = verify_controller(pre_php)

    with open(RESTORE_TWIG, "rb") as f:
        twig_bytes = f.read()
    with open(RESTORE_CSS, "rb") as f:
        css_bytes = f.read()

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
        "1_grid_three_direct_children": hero_qa["dom"]["grid_direct_children_count"] == 3,
        "2_three_col_classes_ok": hero_qa["dom"]["three_col_layout_ok"],
        "3_super_atts_rendered": hero_qa["super_atts_count"] > 0,
        "4_no_quick_cards": "quick-card" not in html,
        "5_no_prop_icons": "product-hero__prop-icon" not in html,
        "6_no_post_change_markers": not hero_qa["any_post_change_marker"],
        "7_twig_matches_backup": sha256_bytes(remote_twig) == sha256_bytes(twig_bytes),
        "8_css_matches_backup": sha256_bytes(remote_css) == sha256_bytes(css_bytes),
        "9_controller_unchanged": pre_controller["sha256"] == post_controller["sha256"],
        "10_controller_super_atts_ok": post_controller["all_markers_ok"],
        "11_php_ok": hero_qa["php_ok"],
        "12_cart_wishlist_compare": all(
            hero_qa[k] for k in ("cart_btn", "qty", "wishlist", "compare", "fancybox")
        ),
    }

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "task": "ROLLBACK TO HERO 3-COLUMN DOM STRUCTURE FIX BASELINE",
        "restore_backups_used": {
            "producthero.twig": RESTORE_TWIG,
            "style.css": RESTORE_CSS,
            "note": "pre-quick-props = state immediately after hero-3col-dom-fix deploy",
        },
        "restore_backup_hashes": {
            "producthero.twig": sha256_bytes(twig_bytes),
            "style.css": sha256_bytes(css_bytes),
        },
        "new_pre_rollback_backups": new_backups,
        "pre_live_hashes": pre_live,
        "files_restored": {
            "producthero.twig": REMOTE["producthero.twig"],
            "style.css": REMOTE["style.css"],
        },
        "files_not_touched": {
            "product.php": REMOTE["product.php"],
            "config.php": "not accessed",
            "js": "not accessed",
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
        "status": "3-column baseline restored" if all(checklist.values()) else "ROLLBACK INCOMPLETE",
    }

    out_path = os.path.join(WORK, "hero-3col-baseline-rollback-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out["checklist_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
