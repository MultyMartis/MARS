#!/usr/bin/env python3
import asyncio


async def main():
    from playwright.async_api import async_playwright

    url = (
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
        "stoly-serii-premium/stoly-premium-600/"
        "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
    )
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 390, "height": 844},
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        await page.goto(url, wait_until="networkidle", timeout=90000)
        result = await page.evaluate(
            """() => {
          const vw = document.documentElement.clientWidth;
          const nodes = ['.product-hero', '.product-hero .container', '.product-hero__grid',
            '.product-hero__commerce', '.product-hero__actions', '.product-hero__title'];
          const widths = {};
          nodes.forEach(sel => {
            const el = document.querySelector(sel);
            if (!el) return;
            const r = el.getBoundingClientRect();
            widths[sel] = {left: r.left, right: r.right, width: r.width, scrollWidth: el.scrollWidth};
          });
          return {vw, widths};
        }"""
        )
        print(result)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
