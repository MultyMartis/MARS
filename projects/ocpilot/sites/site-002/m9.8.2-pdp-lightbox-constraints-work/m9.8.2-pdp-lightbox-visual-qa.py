#!/usr/bin/env python3
"""M9.8.2 — PDP lightbox visual QA (SPKB-18/7-ВЛ5)."""
import asyncio
import json
import os
import sys
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


async def ensure_playwright():
    try:
        from playwright.async_api import async_playwright

        return async_playwright
    except ImportError:
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        from playwright.async_api import async_playwright

        return async_playwright


async def measure_lightbox(page):
    return await page.evaluate(
        """() => {
      const c = document.querySelector('.fancybox__container.is-product-fancybox');
      const img = document.querySelector('.fancybox__container.is-product-fancybox img.f-panzoom__content, .fancybox__container.is-product-fancybox .fancybox-image, .fancybox__container.is-product-fancybox img');
      if (!c || !img) return { ok: false, reason: 'missing container or image' };
      const ir = img.getBoundingClientRect();
      const vw = window.innerWidth;
      const vh = window.innerHeight;
      const cs = getComputedStyle(img);
      return {
        ok: true,
        hasProductClass: c.classList.contains('is-product-fancybox'),
        imgWidth: Math.round(ir.width),
        imgHeight: Math.round(ir.height),
        viewportWidth: vw,
        viewportHeight: vh,
        widthRatio: +(ir.width / vw).toFixed(3),
        heightRatio: +(ir.height / vh).toFixed(3),
        objectFit: cs.objectFit,
        overflowX: document.documentElement.scrollWidth > vw,
        overflowY: document.documentElement.scrollHeight > vh,
      };
    }"""
    )


async def run_viewport(async_playwright, label, viewport):
    shots = {}
    metrics = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport=viewport,
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        page = await context.new_page()
        await page.goto(PDP_URL, wait_until="networkidle", timeout=90000)
        await page.wait_for_selector('[data-fancybox="product"]', timeout=30000)
        await page.locator('[data-fancybox="product"]').first.click()
        await page.wait_for_selector(
            ".fancybox__container.is-product-fancybox img.f-panzoom__content, .fancybox__container.is-product-fancybox .fancybox-image",
            timeout=20000,
        )
        await page.wait_for_timeout(500)

        open_path = os.path.join(QA_DIR, f"lightbox-open-{label}.png")
        await page.screenshot(path=open_path, full_page=False)
        shots["open_first"] = open_path
        metrics["open_first"] = await measure_lightbox(page)

        next_btn = page.locator(
            ".fancybox__container.is-product-fancybox .f-button.is-next, .fancybox__container.is-product-fancybox [data-carousel-next]"
        )
        if await next_btn.count() > 0:
            await next_btn.first.click()
            await page.wait_for_timeout(500)
            nav_path = os.path.join(QA_DIR, f"lightbox-nav-{label}.png")
            await page.screenshot(path=nav_path, full_page=False)
            shots["after_nav"] = nav_path
            metrics["after_nav"] = await measure_lightbox(page)

        await page.locator(
            ".fancybox__container.is-product-fancybox .f-button.is-close-button"
        ).first.click()
        await page.wait_for_timeout(400)
        closed = not await page.locator(".fancybox__container.is-product-fancybox").count()
        metrics["close_ok"] = closed

        await context.close()
        await browser.close()

    return shots, metrics


async def main():
    os.makedirs(QA_DIR, exist_ok=True)
    async_playwright = await ensure_playwright()

    result = {
        "task": "m9.8.2-pdp-lightbox-constraints",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "pdp_url": PDP_URL,
        "viewports": {},
    }

    for label, viewport in VIEWPORTS:
        shots, metrics = await run_viewport(async_playwright, label, viewport)
        is_mobile = viewport["width"] <= 1024
        open_m = metrics.get("open_first", {})
        result["viewports"][label] = {
            "screenshots": shots,
            "metrics": metrics,
            "pass": bool(
                open_m.get("ok")
                and open_m.get("hasProductClass")
                and open_m.get("objectFit") == "contain"
                and (
                    (not is_mobile and open_m.get("widthRatio", 1) <= 0.81 and open_m.get("heightRatio", 1) <= 0.81)
                    or (
                        is_mobile
                        and open_m.get("widthRatio", 1) <= 0.96
                        and open_m.get("heightRatio", 1) <= 0.91
                    )
                )
                and metrics.get("close_ok")
            ),
        }

    out_path = os.path.join(QA_DIR, "m9.8.2-pdp-lightbox-visual-qa.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("Saved:", out_path)


if __name__ == "__main__":
    asyncio.run(main())
