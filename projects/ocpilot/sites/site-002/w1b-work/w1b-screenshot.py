#!/usr/bin/env python3
"""Capture PDP scroll-section screenshots for Wave 1B QA."""
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

OUT = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\w1b-screenshots"
URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-serii-premium/stoly-premium-600/"
    "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
)

LABEL = sys.argv[1] if len(sys.argv) > 1 else "w1b"

SHOTS = [
    ("desktop-sections-full", 1440, 900, False, True),
    ("desktop-sections-fold", 1366, 768, False, False),
    ("mobile-sections-full", 390, 844, True, True),
    ("mobile-sections-fold", 375, 667, True, False),
]


async def main():
    os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name, w, h, mobile, full_page in SHOTS:
            context = await browser.new_context(
                viewport={"width": w, "height": h},
                is_mobile=mobile,
                user_agent="MARS-W1B-Screenshot/1.0",
                extra_http_headers={"Cookie": "beget=begetok"},
            )
            page = await context.new_page()
            await page.goto(URL, wait_until="networkidle", timeout=90000)
            await page.wait_for_selector(".product-pdp-sections", timeout=30000)
            filename = f"{LABEL}-{name}.png"
            path = os.path.join(OUT, filename)
            if full_page:
                sections = page.locator(".product-tabs")
                await sections.screenshot(path=path)
            else:
                await page.screenshot(path=path, full_page=False)
            print("saved", path)
            await context.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
