#!/usr/bin/env python3
import asyncio
import json

PDP_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)


async def one(w, h, label):
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": w, "height": h},
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        await page.goto(PDP_URL, wait_until="networkidle", timeout=90000)
        await page.locator('[data-fancybox="product"]').first.click()
        await page.wait_for_selector(".fancybox__container.is-product-fancybox")
        await page.wait_for_timeout(1500)
        m = await page.evaluate(
            """() => {
          const c = document.querySelector('.fancybox__container.is-product-fancybox');
          const img = c && c.querySelector('img.f-panzoom__content, img');
          const ir = img.getBoundingClientRect();
          const cs = getComputedStyle(img);
          return {
            className: c.className,
            imgW: Math.round(ir.width), imgH: Math.round(ir.height),
            vw: innerWidth, vh: innerHeight,
            wRatio: +(ir.width/innerWidth).toFixed(3),
            hRatio: +(ir.height/innerHeight).toFixed(3),
            maxWidth: cs.maxWidth, maxHeight: cs.maxHeight, objectFit: cs.objectFit
          };
        }"""
        )
        await browser.close()
        return label, m


async def main():
    out = {}
    for label, w, h in [("1920", 1920, 1080), ("1440", 1440, 900), ("390", 390, 844)]:
        label, m = await one(w, h, label)
        out[label] = m
    print(json.dumps(out, ensure_ascii=False, indent=2))


asyncio.run(main())
