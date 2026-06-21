#!/usr/bin/env python3
import asyncio
import json

PDP_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)


async def main():
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(extra_http_headers={"Cookie": "beget=begetok"})
        page = await context.new_page()
        main_src = None

        def on_response(resp):
            nonlocal main_src
            if "main.js" in resp.url:
                main_src = resp.url

        page.on("response", on_response)
        await page.goto(PDP_URL, wait_until="networkidle", timeout=90000)
        has_call = await page.evaluate(
            """() => {
          const scripts = Array.from(document.scripts).map(s => s.src).filter(Boolean);
          return scripts.filter(s => s.includes('main.js'));
        }"""
        )
        print("script tags:", json.dumps(has_call, ensure_ascii=False))
        print("loaded response:", main_src)
        if main_src:
            import urllib.request

            body = urllib.request.urlopen(main_src).read().decode("utf-8", "replace")
            print("applyProductFancyboxClasses(fb) in loaded:", "applyProductFancyboxClasses(fb)" in body)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
