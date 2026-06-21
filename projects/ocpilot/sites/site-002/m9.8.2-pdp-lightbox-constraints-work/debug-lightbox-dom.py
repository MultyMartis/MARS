#!/usr/bin/env python3
import asyncio
import json
import sys

PDP_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)


async def main():
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={"width": 1440, "height": 900},
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        page = await context.new_page()
        await page.goto(PDP_URL, wait_until="networkidle", timeout=90000)
        await page.wait_for_selector('[data-fancybox="product"]', timeout=30000)
        await page.locator('[data-fancybox="product"]').first.click()
        await page.wait_for_timeout(2000)
        info = await page.evaluate(
            """() => {
          const c = document.querySelector('.fancybox__container');
          const imgs = c ? Array.from(c.querySelectorAll('img, .fancybox-image, .f-panzoom__content')) : [];
          return {
            hasContainer: !!c,
            containerClass: c ? c.className : null,
            htmlSnippet: c ? c.innerHTML.slice(0, 1200) : null,
            imgCount: imgs.length,
          };
        }"""
        )
        print(json.dumps(info, ensure_ascii=False, indent=2))
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
