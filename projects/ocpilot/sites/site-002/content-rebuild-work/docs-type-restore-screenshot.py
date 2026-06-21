#!/usr/bin/env python3
"""Screenshot SPKB documents block after docs-type restore."""
import asyncio
import os
import sys

SPKB_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)
QA_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\docs-type-restore"


async def main():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        from playwright.async_api import async_playwright

    os.makedirs(QA_DIR, exist_ok=True)
    out = os.path.join(QA_DIR, "spkb-18-7-vl5-documents-1440.png")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        page = await context.new_page()
        await page.goto(SPKB_URL, wait_until="networkidle", timeout=90000)
        await page.wait_for_selector(".product-content__documents .docs-list__link", timeout=30000)
        await page.locator(".product-content__documents").scroll_into_view_if_needed()
        await page.locator(".product-content__documents").screenshot(path=out)
        await context.close()
        await browser.close()
    print("OK", out)


if __name__ == "__main__":
    asyncio.run(main())
