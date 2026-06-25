#!/usr/bin/env python3
"""Post-restore QA screenshots — M9.13 About restore to pre-redesign."""
import asyncio
import json
import os
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("playwright not installed")
    sys.exit(1)

BASE = "https://zpm.new-site.space/about"
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m9.13-about-restore-screenshots"

VIEWPORTS = [
    ("desktop-1440", {"width": 1440, "height": 900}),
    ("mobile-390", {"width": 390, "height": 844}),
]


async def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    results: dict = {"shots": [], "console_errors": [], "checks": {}}

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})

        def on_console(msg):
            if msg.type == "error":
                results["console_errors"].append(msg.text)

        page.on("console", on_console)

        for vp_name, viewport in VIEWPORTS:
            await page.set_viewport_size(viewport)
            resp = await page.goto(BASE, wait_until="networkidle", timeout=90000)
            results.setdefault("http", {})[vp_name] = resp.status if resp else None
            await page.wait_for_selector(".about-page--main-wrap", timeout=30000)

            full_path = os.path.join(OUT_DIR, f"{vp_name}-full.png")
            await page.screenshot(path=full_path, full_page=True)
            results["shots"].append(full_path)

            overflow = await page.evaluate(
                """() => ({
                  sw: document.documentElement.scrollWidth,
                  cw: document.documentElement.clientWidth
                })"""
            )
            results.setdefault("overflow", {})[vp_name] = overflow

        html = await page.content()
        results["checks"] = {
            "header_present": "site-header" in html or "header" in html[:5000],
            "footer_present": "site-footer" in html or "footer" in html[-8000:],
            "breadcrumb_present": "breadcrumb" in html.lower(),
            "no_m913_hero": "zpm-about-hero" not in html,
            "old_video": "about-page-video" in html,
        }

        await browser.close()

    out = os.path.join(OUT_DIR, "restore-qa-results.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
