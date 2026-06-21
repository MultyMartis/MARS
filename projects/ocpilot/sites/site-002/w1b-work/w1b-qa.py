#!/usr/bin/env python3
"""Functional QA for Wave 1B PDP scroll sections."""
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
    errors = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        for label, w, h, mobile in [
            ("desktop", 1440, 900, False),
            ("mobile", 390, 844, True),
        ]:
            page = await browser.new_page(
                viewport={"width": w, "height": h},
                is_mobile=mobile,
                extra_http_headers={"Cookie": "beget=begetok"},
            )
            js_errors = []
            page.on("pageerror", lambda exc: js_errors.append(str(exc)))

            await page.goto(URL, wait_until="networkidle", timeout=90000)
            await page.wait_for_selector(".product-pdp-sections", timeout=30000)

            prefix = f"{label}_"
            results[prefix + "no_tabs"] = await page.locator(".js-tabs").count() == 0
            results[prefix + "desc_visible"] = await page.locator(
                ".product-pdp-section--desc"
            ).is_visible()
            results[prefix + "key_specs_visible"] = await page.locator(
                ".product-pdp-section--key-specs"
            ).is_visible()
            results[prefix + "full_specs_visible"] = await page.locator(
                ".product-pdp-section--full-specs"
            ).is_visible()

            doc_count = await page.locator(".product-pdp-section--docs").count()
            results[prefix + "docs_section_ok"] = doc_count == 0 or await page.locator(
                ".product-pdp-section--docs"
            ).is_visible()

            overflow = await page.evaluate(
                """() => ({
                  sw: document.documentElement.scrollWidth,
                  cw: document.documentElement.clientWidth
                })"""
            )
            results[prefix + "no_horizontal_scroll"] = overflow["sw"] <= overflow["cw"] + 2

            hero_tabs = await page.locator(".product-hero .tabs__head").count()
            results[prefix + "hero_untouched"] = hero_tabs == 0

            results[prefix + "no_js_errors"] = len(js_errors) == 0
            if js_errors:
                errors.extend([f"{label}: {e}" for e in js_errors])

            await page.close()

        page = await browser.new_page(
            viewport={"width": 1440, "height": 900},
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        await page.goto(URL, wait_until="networkidle", timeout=90000)
        await page.wait_for_selector(".product-pdp-sections", timeout=30000)

        doc_links = page.locator(".product-pdp-section--docs .docs-list__link")
        doc_n = await doc_links.count()
        results["documents_present"] = doc_n > 0
        if doc_n > 0:
            href = await doc_links.first.get_attribute("href")
            results["document_link_has_href"] = bool(href and href != "#")
        else:
            results["document_link_has_href"] = True

        titles = await page.locator(".product-pdp-section__title").all_inner_texts()
        results["section_order"] = titles

        await browser.close()

    print(json.dumps(results, ensure_ascii=False, indent=2))
    fails = [k for k, v in results.items() if k != "section_order" and not v]
    print("FAILS:", fails or "none")
    if errors:
        print("JS ERRORS:", errors)
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
