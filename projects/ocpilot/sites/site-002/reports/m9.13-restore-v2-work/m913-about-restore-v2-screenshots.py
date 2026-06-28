#!/usr/bin/env python3
"""Screenshots + console probe — M9.13 About redesign restore v2."""
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
OUT_ROOT = r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002\qa\m9.13-about-redesign-v2-screenshots"

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


async def capture() -> dict:
    os.makedirs(OUT_ROOT, exist_ok=True)
    results: dict = {"shots": [], "console_errors": []}

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

            full_path = os.path.join(OUT_ROOT, f"{vp_name}-full.png")
            await page.screenshot(path=full_path, full_page=True)
            results["shots"].append(full_path)

            for sec_name, selector in SECTIONS:
                el = page.locator(selector).first
                if await el.count():
                    sec_path = os.path.join(OUT_ROOT, f"{vp_name}-{sec_name}.png")
                    await el.screenshot(path=sec_path)
                    results["shots"].append(sec_path)

            overflow = await page.evaluate(
                "({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth })"
            )
            results.setdefault("overflow", {})[vp_name] = overflow["sw"] <= overflow["cw"]

        await browser.close()

    results["all_pass"] = (
        len(results["console_errors"]) == 0
        and all(results.get("overflow", {}).values())
    )
    out = os.path.join(OUT_ROOT, "screenshot-manifest.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(json.dumps(results, indent=2, ensure_ascii=False))
    return results


if __name__ == "__main__":
    asyncio.run(capture())
