#!/usr/bin/env python3
"""Screenshots — PDP content layout fix."""
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
URL_VMS = (
    BASE + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-svarnye-premium/"
    "vanna-moechnaya-vms-p-2-600-1400h700h850"
)
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\content-layout-fix"


async def shot(page, url, name, viewport, selector=".product-content"):
    await page.set_viewport_size(viewport)
    await page.goto(url, wait_until="networkidle", timeout=90000)
    await page.wait_for_selector(selector, timeout=30000)
    el = page.locator(selector)
    await el.scroll_into_view_if_needed()
    path = os.path.join(OUT_DIR, name)
    await el.screenshot(path=path)
    print("saved", path)


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})
        await shot(page, URL_SPKB, "spkb-1440.png", {"width": 1440, "height": 900})
        await shot(page, URL_SPKB, "spkb-390.png", {"width": 390, "height": 844})
        await shot(page, URL_VMS, "vms-1440.png", {"width": 1440, "height": 900})
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
