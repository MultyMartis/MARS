#!/usr/bin/env python3
import asyncio
import os
import sys

SPKB_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)
QA_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\primary-fa-icon-switch"


async def main():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        from playwright.async_api import async_playwright

    os.makedirs(QA_DIR, exist_ok=True)
    desk = os.path.join(QA_DIR, "spkb-18-7-vl5-hero-desktop.png")
    mob = os.path.join(QA_DIR, "spkb-18-7-vl5-hero-mobile.png")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for viewport, path in [
            ({"width": 1440, "height": 900}, desk),
            ({"width": 390, "height": 844}, mob),
        ]:
            context = await browser.new_context(
                viewport=viewport,
                extra_http_headers={"Cookie": "beget=begetok"},
            )
            page = await context.new_page()
            await page.goto(SPKB_URL, wait_until="networkidle", timeout=90000)
            await page.wait_for_selector(".product-hero__props--primary", timeout=30000)
            await page.locator(".product-hero").screenshot(path=path)
            await context.close()
        await browser.close()
    print(desk)
    print(mob)


if __name__ == "__main__":
    asyncio.run(main())
