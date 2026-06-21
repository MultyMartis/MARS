#!/usr/bin/env python3
"""Interactive functional QA for W1B.2 — cart, qty, fav, compare, gallery, docs."""
import asyncio
import json
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    import subprocess

    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.async_api import async_playwright

URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-serii-premium/stoly-premium-600/"
    "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
)


async def main():
    results = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1440, "height": 900},
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        await page.goto(URL, wait_until="networkidle", timeout=90000)
        await page.wait_for_selector(".product-hero", timeout=30000)

        add_btn = page.locator(".product-hero [data-cart-add]")
        qty_val = page.locator(".product-hero [data-qty-value]")
        qty_plus = page.locator(".product-hero [data-qty-plus]")
        fav = page.locator(".product-hero [data-fav-toggle]")
        compare = page.locator(".product-hero [data-compare-toggle]")
        gallery_link = page.locator(".product-gallery__fancybox").first
        doc_link = page.locator(".product-pdp-section--docs .docs-list__link").first

        await add_btn.click()
        await page.wait_for_timeout(800)
        qty_text = (await qty_val.inner_text()).strip()
        results["cart_add_shows_qty"] = qty_text not in ("", "0")

        await qty_plus.click()
        await page.wait_for_timeout(500)
        qty_after = int((await qty_val.inner_text()).strip())
        results["qty_plus_works"] = qty_after >= 2

        await fav.click()
        await page.wait_for_timeout(400)
        results["wishlist_toggle_class"] = "active" in (await fav.get_attribute("class") or "")

        await compare.click()
        await page.wait_for_timeout(400)
        results["compare_toggle_class"] = "active" in (await compare.get_attribute("class") or "")

        href = await gallery_link.get_attribute("href")
        results["gallery_fancybox_href"] = bool(href)
        results["gallery_fancybox_data_attr"] = await gallery_link.get_attribute("data-fancybox") == "product"

        doc_href = await doc_link.get_attribute("href")
        results["document_href_valid"] = bool(doc_href and doc_href.endswith(".pdf"))

        await browser.close()

    print(json.dumps(results, ensure_ascii=False, indent=2))
    fails = [k for k, v in results.items() if not v]
    print("FAILS:", fails or "none")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
