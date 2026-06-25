#!/usr/bin/env python3
"""Screenshots + console probe — M9.13 About polish pass."""
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
OUT_ROOT = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m9.13-about-polish-screenshots"

VIEWPORTS = [
    ("desktop-1440", {"width": 1440, "height": 900}),
    ("tablet-1024", {"width": 1024, "height": 900}),
    ("mobile-390", {"width": 390, "height": 844}),
]

SECTIONS = [
    ("hero", ".zpm-about-hero"),
    ("company", ".zpm-about-company"),
    ("certs", ".zpm-about-certs"),
    ("geo", ".zpm-about-geo"),
    ("cta", ".zpm-about-cta"),
]


async def capture(prefix: str) -> dict:
    os.makedirs(OUT_ROOT, exist_ok=True)
    subdir = os.path.join(OUT_ROOT, prefix)
    os.makedirs(subdir, exist_ok=True)
    results: dict = {"prefix": prefix, "shots": [], "console_errors": []}

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})

        def on_console(msg):
            if msg.type == "error":
                results["console_errors"].append(msg.text)

        page.on("console", on_console)

        for vp_name, viewport in VIEWPORTS:
            await page.set_viewport_size(viewport)
            await page.goto(BASE, wait_until="networkidle", timeout=90000)
            await page.wait_for_selector(".zpm-about-page", timeout=30000)

            full_path = os.path.join(subdir, f"{vp_name}-full.png")
            await page.screenshot(path=full_path, full_page=True)
            results["shots"].append(full_path)

            for sec_name, selector in SECTIONS:
                el = page.locator(selector).first
                if await el.count():
                    sec_path = os.path.join(subdir, f"{vp_name}-{sec_name}.png")
                    await el.scroll_into_view_if_needed()
                    await el.screenshot(path=sec_path)
                    results["shots"].append(sec_path)

            overflow = await page.evaluate(
                """() => ({
                  sw: document.documentElement.scrollWidth,
                  cw: document.documentElement.clientWidth
                })"""
            )
            results.setdefault("overflow", {})[vp_name] = overflow

        # Fancybox smoke on desktop
        await page.set_viewport_size({"width": 1440, "height": 900})
        await page.goto(BASE, wait_until="networkidle", timeout=90000)
        cert = page.locator('.zpm-about-certs a[data-fancybox="certificates-about"]').first
        if await cert.count():
            await cert.click()
            await page.wait_for_timeout(800)
            fb_path = os.path.join(subdir, "fancybox-cert-1440.png")
            await page.screenshot(path=fb_path)
            results["shots"].append(fb_path)
            results["fancybox_opened"] = True
            close = page.locator("[data-fancybox-close]").first
            if await close.count():
                try:
                    await close.click(timeout=3000)
                except Exception:
                    await page.keyboard.press("Escape")
        else:
            results["fancybox_opened"] = False

        await browser.close()

    out_json = os.path.join(OUT_ROOT, f"{prefix}-results.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(json.dumps(results, indent=2, ensure_ascii=False))
    return results


async def main():
    prefix = sys.argv[1] if len(sys.argv) > 1 else "after"
    await capture(prefix)


if __name__ == "__main__":
    asyncio.run(main())
