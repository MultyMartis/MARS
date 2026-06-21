#!/usr/bin/env python3
"""Screenshots — PDP documents block final pass."""
import asyncio
import os
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("playwright not installed")
    sys.exit(1)

BASE = "https://zpm.new-site.space"
URL_SPKB = (
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
    "stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
)
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\documents-final-pass"


async def shot_documents(page, url, name, viewport):
    await page.set_viewport_size(viewport)
    await page.goto(url, wait_until="networkidle", timeout=90000)
    await page.wait_for_selector(".product-content__documents", timeout=30000)
    el = page.locator(".product-content__documents")
    await el.scroll_into_view_if_needed()
    path = os.path.join(OUT_DIR, name)
    await el.screenshot(path=path)
    print("saved", path)


async def shot_content(page, url, name, viewport):
    await page.set_viewport_size(viewport)
    await page.goto(url, wait_until="networkidle", timeout=90000)
    await page.wait_for_selector(".product-content", timeout=30000)
    el = page.locator(".product-content")
    await el.scroll_into_view_if_needed()
    path = os.path.join(OUT_DIR, name)
    await el.screenshot(path=path)
    print("saved", path)


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})
        await shot_documents(page, URL_SPKB, "spkb-documents-1440.png", {"width": 1440, "height": 900})
        await shot_documents(page, URL_SPKB, "spkb-documents-390.png", {"width": 390, "height": 844})
        await shot_content(page, URL_SPKB, "spkb-content-1440.png", {"width": 1440, "height": 900})
        await shot_content(page, URL_SPKB, "spkb-content-390.png", {"width": 390, "height": 844})
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
