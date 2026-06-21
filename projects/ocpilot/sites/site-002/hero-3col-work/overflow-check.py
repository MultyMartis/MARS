#!/usr/bin/env python3
import asyncio
import re
import urllib.request


async def hero_overflow(url, width):
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": width, "height": 844},
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        await page.goto(url, wait_until="networkidle", timeout=90000)
        result = await page.evaluate(
            """() => {
          const vw = document.documentElement.clientWidth;
          const out = [];
          document.querySelectorAll('.product-hero *').forEach(el => {
            const r = el.getBoundingClientRect();
            if (r.right > vw + 1) {
              out.push({
                tag: el.tagName,
                cls: String(el.className).slice(0, 80),
                right: Math.round(r.right),
                vw,
              });
            }
          });
          return {
            pageScrollWidth: document.documentElement.scrollWidth,
            heroScrollWidth: document.querySelector('.product-hero').scrollWidth,
            offenders: out.slice(0, 20),
          };
        }"""
        )
        await browser.close()
        return result


def html_probe(url):
    html = urllib.request.urlopen(
        urllib.request.Request(url, headers={"Cookie": "beget=begetok"}),
        timeout=60,
    ).read().decode("utf-8", "replace")
    hero = re.search(r'<section class="product-hero">(.*?)</section>', html, re.S)
    h = hero.group(1) if hero else ""
    return {
        "slides": len(re.findall(r"product-gallery__fancybox", h)),
        "thumbs": "js-product-thumbs" in h,
        "request": "Запросить цену" in h,
        "cart": "data-cart-add" in h,
        "get_price": "product-hero__get-price" in h,
    }


async def main():
    urls = {
        "sp_p": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850",
        "vmc": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850",
    }
    for label, url in urls.items():
        print("HTML", label, html_probe(url))
    for width in (390, 1440):
        r = await hero_overflow(urls["sp_p"], width)
        print(f"overflow {width}", r)


if __name__ == "__main__":
    asyncio.run(main())
