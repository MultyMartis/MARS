#!/usr/bin/env python3
"""QA — SITE-002 PDP mobile pass V1."""
import asyncio
import json
import os
import re
import sys
import urllib.request

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"

URL_SPKB = (
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
    "stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
)

WORK_CSS = r"C:\AI MARS\projects\ocpilot\sites\site-002\mobile-pass-v1-work\style.css"
OUT_JSON = r"C:\AI MARS\projects\ocpilot\sites\site-002\mobile-pass-v1-work\mobile-pass-v1-qa-result.json"

VIEWPORTS = [768, 576, 390, 375, 360]


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def fetch_css():
    req = urllib.request.Request(
        BASE + "/assets/css/style.css",
        headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def static_checks(html, css_live, css_work):
    hero = ""
    start = html.find('<section class="product-hero">')
    if start >= 0:
        end = html.find('<section class="product-content">', start)
        if end < 0:
            end = html.find("</section>", start) + 10
        hero = html[start:end]

    content = ""
    cstart = html.find('<section class="product-content">')
    if cstart >= 0:
        cend = html.find('<section class="rel-products"', cstart)
        if cend < 0:
            cend = len(html)
        content = html[cstart:cend]

    return {
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "twig_ok": "Twig_Error" not in html,
        "hero_dom": "product-hero__col--commerce" in hero,
        "super_atts": "product-hero__props--primary" in hero,
        "commerce_card": "product-hero__commerce-card" in hero,
        "service_card": "product-hero__service-card" in hero and "Нужна помощь?" in hero,
        "cart_hooks": "data-cart-pdp" in hero and "data-cart-add" in hero,
        "wishlist_compare": "data-fav-toggle" in hero and "data-compare-toggle" in hero,
        "gallery_fancybox": "product-gallery__fancybox" in hero and 'data-fancybox="product"' in hero,
        "content_grid": "product-content__grid--with-side" in content,
        "docs_list": "docs-list" in content,
        "docs_download": "docs-list__download" in content and "fa-download" in content,
        "docs_note": "product-content__docs-note" in content,
        "product_help": "product-help" in content,
        "related": "rel-products" in html,
        "live_css_has_mobile_pass": "PDP MOBILE PASS V1" in css_live,
        "work_css_has_mobile_pass": "PDP MOBILE PASS V1" in css_work,
        "mobile_primary_grid": "grid-template-columns: repeat(2, minmax(0, 1fr))" in css_live,
        "mobile_help_stack": "product-help__left" in css_live and "order: 1" in css_live,
        "mobile_content_order": "product-content__side" in css_live and "order: 2" in css_live,
    }


async def viewport_checks(page):
    results = {}
    for w in VIEWPORTS:
        await page.set_viewport_size({"width": w, "height": 900})
        await page.goto(URL_SPKB, wait_until="networkidle", timeout=90000)
        await page.wait_for_selector(".product-hero", timeout=30000)

        metrics = await page.evaluate(
            """() => {
              const vw = document.documentElement.clientWidth;
              const sw = document.body.scrollWidth;
              const hero = document.querySelector('.product-hero');
              const commerce = document.querySelector('.product-hero__commerce-card');
              const service = document.querySelector('.product-hero__service-card');
              const specs = document.querySelector('.product-hero__specs');
              const primary = document.querySelector('.product-hero__props--primary');
              const help = document.querySelector('.product-help__content');
              const docs = document.querySelector('.product-content__documents');
              const rel = document.querySelector('.rel-products');
              const footer = document.querySelector('.zpm-footer');

              function rectTop(el) {
                return el ? el.getBoundingClientRect().top + window.scrollY : null;
              }

              const order = {
                commerce: rectTop(commerce),
                service: rectTop(service),
                specs: rectTop(specs),
                docs: rectTop(docs),
                help: rectTop(help),
              };

              let primaryCols = null;
              if (primary) {
                const cs = getComputedStyle(primary);
                primaryCols = cs.gridTemplateColumns || cs.flexDirection;
              }

              let helpCols = null;
              if (help) {
                helpCols = getComputedStyle(help).gridTemplateColumns;
              }

              return {
                viewport: vw,
                scrollWidth: sw,
                noHorizontalOverflow: sw <= vw + 1,
                heroOrderOk: order.commerce !== null && order.service !== null && order.specs !== null
                  && order.commerce < order.specs && order.service < order.specs,
                contentOrderOk: order.specs !== null && order.docs !== null && order.help !== null
                  && order.specs < order.docs && order.docs < order.help,
                primaryLayout: primaryCols,
                helpLayout: helpCols,
                galleryImgHeight: document.querySelector('.product-gallery__img')
                  ? document.querySelector('.product-gallery__img').getBoundingClientRect().height
                  : null,
                relVisible: !!rel,
                footerVisible: !!footer,
              };
            }"""
        )
        results[str(w)] = metrics
    return results


async def run_playwright():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        return {"error": "playwright not installed", "viewport_checks": {}}

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": COOKIE})
        viewport = await viewport_checks(page)
        await browser.close()
        return {"viewport_checks": viewport}


def main():
    html = fetch(URL_SPKB)
    css_live = fetch_css()
    with open(WORK_CSS, encoding="utf-8") as f:
        css_work = f.read()

    static = static_checks(html, css_live, css_work)
    viewport = asyncio.run(run_playwright())

    all_viewport_pass = True
    for w, data in viewport.get("viewport_checks", {}).items():
        if isinstance(data, dict):
            if not data.get("noHorizontalOverflow", False):
                all_viewport_pass = False
            if not data.get("heroOrderOk", False):
                all_viewport_pass = False
            if not data.get("contentOrderOk", False):
                all_viewport_pass = False

    result = {
        "url": URL_SPKB,
        "static": static,
        **viewport,
        "summary": {
            "static_pass": all(static.values()),
            "viewport_pass": all_viewport_pass,
            "overall": all(static.values()) and all_viewport_pass,
        },
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
    print("Saved", OUT_JSON)
    return 0 if result["summary"]["overall"] else 1


if __name__ == "__main__":
    sys.exit(main())
