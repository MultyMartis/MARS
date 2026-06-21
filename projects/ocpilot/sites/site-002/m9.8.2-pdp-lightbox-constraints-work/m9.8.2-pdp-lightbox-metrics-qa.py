#!/usr/bin/env python3
"""M9.8.2 lightbox metrics QA."""
import asyncio
import json
import os
from datetime import datetime

PDP_URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)
QA_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m9.8.2-pdp-lightbox-constraints"
VIEWPORTS = [
    ("desktop-1920", {"width": 1920, "height": 1080}),
    ("desktop-1440", {"width": 1440, "height": 900}),
    ("mobile-390", {"width": 390, "height": 844}),
]


async def run(label, viewport):
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport=viewport,
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        page = await context.new_page()
        await page.goto(PDP_URL, wait_until="networkidle", timeout=90000)
        await page.locator('[data-fancybox="product"]').first.click()
        await page.wait_for_selector(".fancybox__container.is-product-fancybox", timeout=20000)
        await page.wait_for_timeout(1200)

        metrics = await page.evaluate(
            """() => {
          const c = document.querySelector('.fancybox__container.is-product-fancybox');
          const img = c && c.querySelector('img.f-panzoom__content, .fancybox-image, img');
          if (!c || !img) return { ok: false };
          const ir = img.getBoundingClientRect();
          const cs = getComputedStyle(img);
          const vw = window.innerWidth;
          const vh = window.innerHeight;
          return {
            ok: true,
            hasProductClass: c.classList.contains('is-product-fancybox'),
            imgWidth: Math.round(ir.width),
            imgHeight: Math.round(ir.height),
            viewportWidth: vw,
            viewportHeight: vh,
            widthRatio: +(ir.width / vw).toFixed(3),
            heightRatio: +(ir.height / vh).toFixed(3),
            maxWidth: cs.maxWidth,
            maxHeight: cs.maxHeight,
            objectFit: cs.objectFit,
            overflow: document.documentElement.scrollWidth > vw || document.documentElement.scrollHeight > vh,
          };
        }"""
        )

        shot = os.path.join(QA_DIR, f"lightbox-{label}.png")
        await page.screenshot(path=shot, full_page=False)

        # nav
        next_btn = page.locator(
            ".fancybox__container.is-product-fancybox .f-button.is-next"
        )
        nav_metrics = None
        if await next_btn.count():
            await next_btn.first.click()
            await page.wait_for_timeout(800)
            nav_metrics = await page.evaluate(
                """() => {
              const img = document.querySelector('.fancybox__container.is-product-fancybox img.f-panzoom__content, .fancybox__container.is-product-fancybox img');
              if (!img) return { ok: false };
              const ir = img.getBoundingClientRect();
              return { ok: true, imgWidth: Math.round(ir.width), imgHeight: Math.round(ir.height) };
            }"""
            )

        await page.locator(
            ".fancybox__container.is-product-fancybox .f-button.is-close-button"
        ).first.click()
        await page.wait_for_timeout(500)
        closed = await page.locator(".fancybox__container.is-product-fancybox").count() == 0

        await context.close()
        await browser.close()

    is_mobile = viewport["width"] <= 1024
    pass_ok = bool(
        metrics.get("ok")
        and metrics.get("hasProductClass")
        and metrics.get("objectFit") == "contain"
        and (
            (not is_mobile and metrics.get("widthRatio", 1) <= 0.81 and metrics.get("heightRatio", 1) <= 0.81)
            or (is_mobile and metrics.get("widthRatio", 1) <= 0.96 and metrics.get("heightRatio", 1) <= 0.91)
        )
        and closed
    )
    return {
        "screenshot": shot,
        "open": metrics,
        "after_nav": nav_metrics,
        "close_ok": closed,
        "pass": pass_ok,
    }


async def main():
    os.makedirs(QA_DIR, exist_ok=True)
    result = {
        "task": "m9.8.2-pdp-lightbox-constraints",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "pdp_url": PDP_URL,
        "viewports": {},
    }
    for label, viewport in VIEWPORTS:
        result["viewports"][label] = await run(label, viewport)

    out = os.path.join(QA_DIR, "m9.8.2-pdp-lightbox-visual-qa.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
