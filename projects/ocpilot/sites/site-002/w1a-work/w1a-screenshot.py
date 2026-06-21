#!/usr/bin/env python3
"""Capture PDP hero screenshots via Playwright."""
import asyncio
import os
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Installing playwright...")
    import subprocess

    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.async_api import async_playwright

OUT = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\w1a-screenshots"
URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-serii-premium/stoly-premium-600/"
    "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
)

LABEL = sys.argv[1] if len(sys.argv) > 1 else "w1a2"
HERO_SELECTOR = ".product-hero__layout, .product-hero__grid"

SHOTS = [
    ("desktop-hero-full", 1440, 900, False),
    ("desktop-hero-fold", 1366, 768, False),
    ("mobile-hero-full", 390, 844, True),
    ("mobile-hero-fold", 375, 667, True),
]


async def main():
    os.makedirs(OUT, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name, w, h, mobile in SHOTS:
            context = await browser.new_context(
                viewport={"width": w, "height": h},
                is_mobile=mobile,
                user_agent="MARS-W1A-Screenshot/1.0",
                extra_http_headers={"Cookie": "beget=begetok"},
            )
            page = await context.new_page()
            await page.goto(URL, wait_until="networkidle", timeout=90000)
            await page.wait_for_selector(HERO_SELECTOR, timeout=30000)
            filename = f"{LABEL}-{name}.png" if LABEL else f"{name}.png"
            path = os.path.join(OUT, filename)
            if "fold" in name:
                await page.screenshot(path=path, full_page=False)
            else:
                hero = page.locator(".product-hero")
                await hero.screenshot(path=path)
            print("saved", path)
            await context.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
