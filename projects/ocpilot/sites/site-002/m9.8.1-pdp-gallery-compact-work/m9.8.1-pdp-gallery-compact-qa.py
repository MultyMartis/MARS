#!/usr/bin/env python3
"""M9.8.1 PDP gallery compact thumbs side rail — live QA."""
import asyncio
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime

BASE = "https://zpm.new-site.space"
SKU_MULTI = "СПКБ-18/7-ВЛ5"
PDP_MULTI_URL = (
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
    "stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
)
PDP_SINGLE_URL = (
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-standart/"
    "stoly-standart-700-s-polkoy-reshetkoy/stol-proizvodstvennyy-spb-s-6-7-600h700h850"
)
OUT = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m9.8.1-pdp-gallery-compact"
SHOT_DIR = os.path.join(OUT, "screenshots")

VIEWPORTS = {
    "desktop_1920": {"width": 1920, "height": 1080},
    "desktop_1440": {"width": 1440, "height": 900},
    "desktop_1366": {"width": 1366, "height": 768},
    "desktop_1280": {"width": 1280, "height": 800},
    "mobile_768": {"width": 768, "height": 1024},
    "mobile_390": {"width": 390, "height": 844},
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-QA-M981"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", "replace")


def find_product_url(sku):
    search_url = BASE + "/index.php?route=product/search&search=" + urllib.parse.quote(sku)
    search_html = fetch(search_url)
    for href in re.findall(r'href="([^"]+)"', search_html):
        if "route=product/product" in href or "product_id=" in href:
            if href.startswith("/"):
                return BASE + href
            if not href.startswith("http"):
                return BASE + "/" + href.lstrip("/")
            return href
    return None


def find_single_image_product_url():
    cat_url = BASE + "/index.php?route=product/category&path=301"
    html = fetch(cat_url)
    links = []
    for href in re.findall(r'href="([^"]+)"', html):
        if "route=product/product" in href or "product_id=" in href:
            if href.startswith("/"):
                href = BASE + href
            elif not href.startswith("http"):
                href = BASE + "/" + href.lstrip("/")
            if href not in links:
                links.append(href)
        if len(links) >= 12:
            break
    for url in links:
        pdp = fetch(url)
        thumbs = len(re.findall(r'product-gallery__thumb', pdp))
        if thumbs == 0 and "product-gallery" in pdp:
            return url
    return links[0] if links else None


async def ensure_playwright():
    try:
        from playwright.async_api import async_playwright

        return async_playwright
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        from playwright.async_api import async_playwright

        return async_playwright


async def qa_viewport(async_playwright, label, viewport, pdp_url):
    shots = {}
    metrics = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport=viewport)
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))

        await page.goto(pdp_url, wait_until="networkidle", timeout=60000)
        await page.wait_for_selector(".product-gallery", timeout=20000)

        metrics = await page.evaluate(
            """() => {
              const g = document.querySelector('.product-gallery');
              const thumbs = document.querySelector('.product-gallery__thumbs');
              const main = document.querySelector('.product-gallery__main');
              if (!g) return { error: 'no gallery' };
              const cs = getComputedStyle(g);
              const ts = thumbs ? getComputedStyle(thumbs) : null;
              const thumbSwiper = thumbs && thumbs.swiper ? thumbs.swiper : null;
              return {
                flexDirection: cs.flexDirection,
                flexFlow: cs.flexFlow,
                hasThumbs: !!thumbs,
                thumbsWidth: ts ? ts.width : null,
                thumbsDirection: thumbSwiper ? thumbSwiper.params.direction : null,
                mainWidth: main ? getComputedStyle(main).width : null,
                overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth,
                thumbCount: document.querySelectorAll('.product-gallery__thumb').length,
                activeThumb: !!document.querySelector('.swiper-slide-thumb-active'),
                fancyboxLinks: document.querySelectorAll('[data-fancybox="product"]').length
              };
            }"""
        )

        metrics["jsErrors"] = errors

        shot_path = os.path.join(SHOT_DIR, f"{label}.png")
        await page.screenshot(path=shot_path, full_page=False)
        shots["gallery"] = shot_path

        next_btn = page.locator(".product-gallery__btn--next")
        if await next_btn.count() and await next_btn.is_enabled():
            await next_btn.click()
            await page.wait_for_timeout(400)
            nav_path = os.path.join(SHOT_DIR, f"{label}_after_next.png")
            await page.screenshot(path=nav_path, full_page=False)
            shots["after_next"] = nav_path
            metrics["activeThumbAfterNext"] = await page.evaluate(
                "() => !!document.querySelector('.swiper-slide-thumb-active')"
            )

        await browser.close()

    metrics["jsErrors"] = errors
    return shots, metrics


async def run_all():
    os.makedirs(SHOT_DIR, exist_ok=True)
    result = {
        "task": "m9.8.1-pdp-gallery-compact",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "base": BASE,
        "asset_checks": {},
        "multi_image": {},
        "single_image": {},
        "viewports": {},
        "category_regression": {},
    }

    main_js = fetch(BASE + "/assets/js/main.js")
    style_css = fetch(BASE + "/assets/css/style.css")

    result["asset_checks"] = {
        "css_row_at_1025": bool(
            re.search(
                r"@media \(min-width: 1025px\)\s*\{[\s\S]{0,500}\.product-gallery\s*\{[\s\S]{0,120}flex-flow:\s*row",
                style_css,
            )
        ),
        "js_vertical_direction": "direction: 'vertical'" in main_js,
        "js_horizontal_direction": "direction: 'horizontal'" in main_js,
        "js_mq_reinit": "GALLERY_DESKTOP_MQ" in main_js and "scheduleGalleryRebuild" in main_js,
        "js_thumbs_link_preserved": "thumbs: { swiper: thumbs }" in main_js,
    }

    multi_url = PDP_MULTI_URL
    single_url = PDP_SINGLE_URL

    result["multi_image"]["url"] = multi_url
    result["single_image"]["url"] = single_url

    async_playwright = await ensure_playwright()

    if multi_url:
        for label, viewport in VIEWPORTS.items():
            shots, metrics = await qa_viewport(async_playwright, f"multi_{label}", viewport, multi_url)
            is_desktop = viewport["width"] >= 1025
            flex_flow = metrics.get("flexFlow", "")
            flex_dir = metrics.get("flexDirection", "")
            is_row = flex_flow.startswith("row") or flex_dir == "row"
            is_col = flex_flow.startswith("column") or flex_dir == "column"
            result["viewports"][f"multi_{label}"] = {
                "screenshots": shots,
                "metrics": metrics,
                "checks": {
                    "row_layout": is_row if is_desktop else is_col,
                    "thumbs_vertical": (metrics.get("thumbsDirection") == "vertical") if is_desktop else (metrics.get("thumbsDirection") == "horizontal"),
                    "no_overflow": not metrics.get("overflowX", True),
                    "has_thumbs": metrics.get("hasThumbs", False),
                    "fancybox_hooks": metrics.get("fancyboxLinks", 0) > 0,
                },
            }

    if single_url:
        shots, metrics = await qa_viewport(async_playwright, "single_desktop_1440", {"width": 1440, "height": 900}, single_url)
        result["single_image"]["screenshots"] = shots
        result["single_image"]["metrics"] = metrics
        result["single_image"]["checks"] = {
            "no_thumbs_rail": metrics.get("thumbCount", 0) == 0 or not metrics.get("hasThumbs"),
            "gallery_present": "error" not in metrics,
            "fancybox_hooks": metrics.get("fancyboxLinks", 0) > 0,
            "no_overflow": not metrics.get("overflowX", True),
        }

    cat_html = fetch(BASE + "/index.php?route=product/category&path=301")
    result["category_regression"] = {
        "has_view_switcher": "category--view" in cat_html or "data-category-view" in cat_html,
        "page_loads": "page--category" in cat_html or "category" in cat_html.lower(),
    }

    ac = result["asset_checks"]
    vp = result["viewports"]
    desktop_rows = [v["checks"]["row_layout"] for k, v in vp.items() if "desktop" in k]
    mobile_cols = [v["checks"]["row_layout"] for k, v in vp.items() if "mobile" in k]

    result["qa_summary"] = {
        "assets_ok": all(ac.values()),
        "desktop_row_layout": all(desktop_rows) if desktop_rows else False,
        "mobile_column_layout": all(mobile_cols) if mobile_cols else False,
        "desktop_thumbs_vertical": all(
            v["checks"]["thumbs_vertical"] for k, v in vp.items() if "desktop" in k
        ),
        "mobile_thumbs_horizontal": all(
            v["checks"]["thumbs_vertical"] for k, v in vp.items() if "mobile" in k
        ),
        "no_horizontal_overflow": all(v["checks"]["no_overflow"] for v in vp.values()),
        "single_image_ok": result.get("single_image", {}).get("checks", {}).get("gallery_present", False),
        "category_ok": result["category_regression"]["page_loads"],
    }

    out_path = os.path.join(OUT, "m9.8.1-pdp-gallery-compact-qa-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result["qa_summary"], ensure_ascii=False, indent=2))
    print("Saved:", out_path)


if __name__ == "__main__":
    asyncio.run(run_all())
