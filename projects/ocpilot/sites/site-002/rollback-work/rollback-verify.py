#!/usr/bin/env python3
"""Verify SITE-002 PDP full rollback to pre-W1A baseline."""
import asyncio
import json
import re
import urllib.request

URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-serii-premium/stoly-premium-600/"
    "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
)


def fetch_html(url):
    req = urllib.request.Request(
        url, headers={"User-Agent": "MARS-Rollback-Verify/1.0", "Cookie": "beget=begetok"}
    )
    return urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")


def static_checks(html):
    hero_m = re.search(r'<section class="product-hero">.*?</section>', html, re.S)
    hero = hero_m.group(0) if hero_m else ""
    tabs_m = re.search(r'<div class="tabs js-tabs">.*?</div>\s*</div>', html, re.S)
    tabs = tabs_m.group(0) if tabs_m else ""

    return {
        "hero_original_grid": "product-hero__grid" in hero,
        "no_w1a_layout": "product-hero__layout" not in hero,
        "no_w1a_context": "product-hero__context" not in hero,
        "no_w1a_fit_grid": "product-hero__fit-grid" not in hero,
        "assum_brand_present": "product-hero__brand" in hero and "assum_logo" in hero.lower(),
        "subtitle_present": "product-hero__subtitle" in hero,
        "tabs_present": "tabs js-tabs" in html,
        "tab_opisanie": "Описание" in tabs,
        "tab_harakteristiki": "Характеристики" in tabs,
        "tab_dokumenty": "Документы" in tabs,
        "no_scroll_sections": "product-pdp-sections" not in html,
        "related_products_present": "relproducts" in html or "product-related" in html,
        "gallery_fancybox": "data-fancybox=\"product\"" in hero,
        "cart_controls": "data-cart-add" in hero and "data-cart-pdp" in hero,
        "qty_controls": "data-qty-plus" in hero and "data-qty-minus" in hero,
        "wishlist_toggle": "data-fav-toggle" in hero,
        "compare_toggle": "data-compare-toggle" in hero,
    }


async def interactive_checks():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        import subprocess
        import sys

        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        from playwright.async_api import async_playwright

    results = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1440, "height": 900},
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        await page.goto(URL, wait_until="networkidle", timeout=90000)
        await page.wait_for_selector(".product-hero", timeout=30000)
        await page.wait_for_selector(".tabs.js-tabs", timeout=30000)

        tab_spec = page.locator('.tabs__tab[data-tab="spec"]')
        await tab_spec.click()
        await page.wait_for_timeout(400)
        spec_panel = page.locator("#tab-spec")
        results["tab_switch_spec"] = await spec_panel.is_visible()

        tab_docs = page.locator('.tabs__tab[data-tab="docs"]')
        await tab_docs.click()
        await page.wait_for_timeout(400)
        docs_panel = page.locator("#tab-docs")
        results["tab_switch_docs"] = await docs_panel.is_visible()

        add_btn = page.locator(".product-hero [data-cart-add]")
        qty_val = page.locator(".product-hero [data-qty-value]")
        qty_plus = page.locator(".product-hero [data-qty-plus]")
        fav = page.locator(".product-hero [data-fav-toggle]")
        compare = page.locator(".product-hero [data-compare-toggle]")
        gallery_link = page.locator(".product-gallery__fancybox").first

        await add_btn.click()
        await page.wait_for_timeout(800)
        qty_text = (await qty_val.inner_text()).strip()
        results["cart_add_works"] = qty_text not in ("", "0")

        await qty_plus.click()
        await page.wait_for_timeout(500)
        qty_after = int((await qty_val.inner_text()).strip())
        results["qty_plus_works"] = qty_after >= 2

        await fav.click()
        await page.wait_for_timeout(400)
        results["wishlist_works"] = "active" in (await fav.get_attribute("class") or "")

        await compare.click()
        await page.wait_for_timeout(400)
        results["compare_works"] = "active" in (await compare.get_attribute("class") or "")

        href = await gallery_link.get_attribute("href")
        results["gallery_fancybox_works"] = bool(href) and await gallery_link.get_attribute("data-fancybox") == "product"

        await browser.close()
    return results


async def main():
    html = fetch_html(URL)
    results = static_checks(html)
    results.update(await interactive_checks())
    print(json.dumps(results, ensure_ascii=False, indent=2))
    fails = [k for k, v in results.items() if not v]
    print("FAILS:", fails or "none")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
