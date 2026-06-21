#!/usr/bin/env python3
"""Measure PDP heights before/after W1B.2 compactness pass."""
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


async def measure_page(page):
    return await page.evaluate(
        """() => {
          const hero = document.querySelector('.product-hero');
          const docs = document.querySelector('.product-pdp-section--docs');
          const docsLink = document.querySelector('.product-pdp-section--docs .docs-list__item > a');
          const buybox = document.querySelector('.product-hero__buybox-inner');
          const sections = document.querySelector('.product-pdp-sections');
          const media = document.querySelector('.product-hero__media');
          const rect = el => el ? Math.round(el.getBoundingClientRect().height) : null;
          return {
            pageHeight: Math.round(document.documentElement.scrollHeight),
            heroHeight: rect(hero),
            buyboxHeight: rect(buybox),
            mediaWidthPct: media && hero
              ? Math.round((media.getBoundingClientRect().width / hero.getBoundingClientRect().width) * 100)
              : null,
            sectionsHeight: rect(sections),
            docsSectionHeight: rect(docs),
            docsCardHeight: rect(docsLink),
            scrollWidth: document.documentElement.scrollWidth,
            clientWidth: document.documentElement.clientWidth,
          };
        }"""
    )


async def main():
    label = sys.argv[1] if len(sys.argv) > 1 else "post-w1b2"
    results = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for vp_label, w, h, mobile in [
            ("desktop", 1440, 900, False),
            ("mobile", 390, 844, True),
        ]:
            page = await browser.new_page(
                viewport={"width": w, "height": h},
                is_mobile=mobile,
                extra_http_headers={"Cookie": "beget=begetok"},
            )
            await page.goto(URL, wait_until="networkidle", timeout=90000)
            await page.wait_for_selector(".product-hero", timeout=30000)
            results[vp_label] = await measure_page(page)
            await page.close()
        await browser.close()

    out = {"label": label, "measurements": results}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
