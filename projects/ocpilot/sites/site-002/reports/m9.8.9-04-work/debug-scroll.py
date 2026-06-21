#!/usr/bin/env python3
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})
        await page.set_viewport_size({"width": 1440, "height": 900})
        await page.goto(
            "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/",
            wait_until="networkidle",
            timeout=90000,
        )
        await page.evaluate("window.scrollTo(0, 1200)")
        await page.wait_for_timeout(500)
        await page.locator('input[name="price_from"]').fill("1000")
        await page.locator('input[name="price_to"]').fill("500000")
        await page.locator('input[name="price_to"]').dispatch_event("change")
        await page.wait_for_timeout(2500)
        data = await page.evaluate(
            """() => {
          const section = document.querySelector('section.category');
          const stickyD = document.querySelector('[data-header-sticky]');
          return {
            scrollY: window.pageYOffset,
            sectionTop: section ? section.getBoundingClientRect().top : null,
            stickyH: stickyD ? stickyD.getBoundingClientRect().height : null,
            stickySticky: stickyD ? stickyD.classList.contains('sticky') : null,
            headerH: document.querySelector('[data-header]')?.getBoundingClientRect().height,
            url: location.href,
            cards: document.querySelectorAll('.p-card').length,
          };
        }"""
        )
        print(data)
        await browser.close()

asyncio.run(main())
