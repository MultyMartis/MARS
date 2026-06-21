#!/usr/bin/env python3
"""Screenshots — SITE-002 PDP mobile pass V1."""
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
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\mobile-pass-v1"

VIEWPORTS = [
    (768, 900),
    (576, 900),
    (390, 844),
    (375, 812),
    (360, 800),
]


async def shot_full(page, width, height):
    await page.set_viewport_size({"width": width, "height": height})
    await page.goto(URL_SPKB, wait_until="networkidle", timeout=90000)
    await page.wait_for_selector(".product-hero", timeout=30000)
    path = os.path.join(OUT_DIR, f"spkb-pdp-{width}.png")
    await page.screenshot(path=path, full_page=True)
    print("saved", path)


async def shot_hero(page, width, height):
    await page.set_viewport_size({"width": width, "height": height})
    await page.goto(URL_SPKB, wait_until="networkidle", timeout=90000)
    await page.wait_for_selector(".product-hero", timeout=30000)
    el = page.locator(".product-hero")
    path = os.path.join(OUT_DIR, f"spkb-hero-{width}.png")
    await el.screenshot(path=path)
    print("saved", path)


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})
        for width, height in VIEWPORTS:
            await shot_full(page, width, height)
            await shot_hero(page, width, height)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
