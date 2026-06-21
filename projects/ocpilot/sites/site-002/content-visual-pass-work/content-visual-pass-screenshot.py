#!/usr/bin/env python3
"""Screenshots — PDP content visual structure pass."""
import asyncio
import os
import sys

URLS = {
    "spkb-1440": (
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
        "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
        "stol-tumba-spkb-18-7-vl5-1800h700h850",
        {"width": 1440, "height": 900},
        ".product-content",
    ),
    "spkb-390": (
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
        "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
        "stol-tumba-spkb-18-7-vl5-1800h700h850",
        {"width": 390, "height": 844},
        ".product-content",
    ),
    "vms-1440": (
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"
        "vanny-svarnye-premium/vanna-moechnaya-vms-p-2-600-1400h700h850",
        {"width": 1440, "height": 900},
        ".product-content",
    ),
}

QA_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\content-visual-pass"


async def main():
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        from playwright.async_api import async_playwright

    os.makedirs(QA_DIR, exist_ok=True)
    paths = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for name, (url, viewport, selector) in URLS.items():
            context = await browser.new_context(
                viewport=viewport,
                extra_http_headers={"Cookie": "beget=begetok"},
            )
            page = await context.new_page()
            await page.goto(url, wait_until="networkidle", timeout=90000)
            await page.wait_for_selector(selector, timeout=30000)
            await page.locator(selector).scroll_into_view_if_needed()
            out = os.path.join(QA_DIR, f"{name}.png")
            await page.locator(selector).screenshot(path=out)
            paths.append(out)

            if "390" in name:
                overflow = await page.evaluate(
                    """() => {
                      const el = document.documentElement;
                      return {
                        scrollWidth: el.scrollWidth,
                        clientWidth: el.clientWidth,
                        overflow: el.scrollWidth > el.clientWidth
                      };
                    }"""
                )
                print(name, "overflow", overflow)

            await context.close()
        await browser.close()

    for pth in paths:
        print("OK", pth)


if __name__ == "__main__":
    asyncio.run(main())
