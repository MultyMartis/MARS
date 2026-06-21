#!/usr/bin/env python3
"""Capture rollback verification screenshots for SITE-002 PDP."""
import asyncio
import os
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    import subprocess

    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.async_api import async_playwright

OUT = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\rollback-pre-w1a"
URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-serii-premium/stoly-premium-600/"
    "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
)

SHOTS = [
    ("desktop-full-page", 1440, 900, False, "full"),
    ("desktop-hero", 1440, 900, False, "hero"),
    ("mobile-full-page", 390, 844, True, "full"),
    ("mobile-hero", 390, 844, True, "hero"),
]


async def main():
    os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name, w, h, mobile, mode in SHOTS:
            context = await browser.new_context(
                viewport={"width": w, "height": h},
                is_mobile=mobile,
                user_agent="MARS-Rollback-Screenshot/1.0",
                extra_http_headers={"Cookie": "beget=begetok"},
            )
            page = await context.new_page()
            await page.goto(URL, wait_until="networkidle", timeout=90000)
            await page.wait_for_selector(".product-hero", timeout=30000)
            path = os.path.join(OUT, f"{name}.png")
            if mode == "hero":
                await page.locator(".product-hero").screenshot(path=path)
            else:
                await page.screenshot(path=path, full_page=True)
            print("saved", path)
            await context.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
