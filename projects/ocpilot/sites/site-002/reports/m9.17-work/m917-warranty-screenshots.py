#!/usr/bin/env python3
"""M9.17 Warranty QA screenshots — desktop, tablet, mobile."""
import asyncio
import json
import os
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("playwright not installed")
    sys.exit(1)

BASE = "https://zpm.new-site.space/guarantee"
OUT_DIR = r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002\qa\m9.17-warranty-screenshots"

VIEWPORTS = [
    ("desktop-1440", {"width": 1440, "height": 900}),
    ("tablet-1024", {"width": 1024, "height": 768}),
    ("mobile-390", {"width": 390, "height": 844}),
]


async def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    results: dict = {"shots": [], "console_errors": [], "checks": {}, "overflow": {}}

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
            await page.wait_for_selector(".zpm-warranty-page", timeout=30000)

            full_path = os.path.join(OUT_DIR, f"m9.17-warranty-{vp_name}-full.png")
            await page.screenshot(path=full_path, full_page=True)
            results["shots"].append(full_path)

            if vp_name == "desktop-1440":
                timeline = page.locator(".zpm-warranty-process")
                if await timeline.count():
                    tl_path = os.path.join(OUT_DIR, f"m9.17-warranty-{vp_name}-timeline.png")
                    await timeline.screenshot(path=tl_path)
                    results["shots"].append(tl_path)

            overflow = await page.evaluate(
                """() => ({
                  sw: document.documentElement.scrollWidth,
                  cw: document.documentElement.clientWidth
                })"""
            )
            results["overflow"][vp_name] = overflow

        html = await page.content()
        results["checks"] = {
            "warranty_page": "zpm-warranty-page" in html,
            "timeline_steps": html.count("zpm-corp-timeline__step"),
            "faq_items": html.count('id="warranty-faq-btn-'),
            "cta_form": "zpm-warranty-form" in html,
            "equipment_model_field": 'name="equipment_model"' in html,
            "data_warranty_faq": "data-warranty-faq" in html,
        }
        results["checks"]["pass"] = (
            results["checks"]["warranty_page"]
            and results["checks"]["timeline_steps"] >= 5
            and results["checks"]["faq_items"] >= 8
            and results["checks"]["equipment_model_field"]
            and results["checks"]["data_warranty_faq"]
            and len(results["console_errors"]) == 0
            and all(v.get("sw", 0) <= v.get("cw", 9999) + 1 for v in results["overflow"].values())
        )

        await browser.close()

    out = os.path.join(OUT_DIR, "m9.17-warranty-qa-results.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
