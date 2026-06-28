#!/usr/bin/env python3
"""M9.18 Custom Manufacturing QA screenshots — desktop, tablet, mobile."""
import asyncio
import json
import os
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("playwright not installed")
    sys.exit(1)

BASE = "https://zpm.new-site.space/custom-equipment"
OUT_DIR = r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002\qa\m9.18-custom-screenshots"

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
            await page.wait_for_selector(".zpm-custom-page", timeout=30000)

            full_path = os.path.join(OUT_DIR, f"m9.18-custom-{vp_name}-full.png")
            await page.screenshot(path=full_path, full_page=True)
            results["shots"].append(full_path)

            if vp_name == "desktop-1440":
                timeline = page.locator(".zpm-custom-process")
                if await timeline.count():
                    tl_path = os.path.join(OUT_DIR, f"m9.18-custom-{vp_name}-timeline.png")
                    await timeline.screenshot(path=tl_path)
                    results["shots"].append(tl_path)

                outcomes = page.locator(".zpm-custom-outcomes")
                if await outcomes.count():
                    oc_path = os.path.join(OUT_DIR, f"m9.18-custom-{vp_name}-outcomes.png")
                    await outcomes.screenshot(path=oc_path)
                    results["shots"].append(oc_path)

                form = page.locator("#zpm-custom-form")
                if await form.count():
                    fm_path = os.path.join(OUT_DIR, f"m9.18-custom-{vp_name}-form.png")
                    await form.screenshot(path=fm_path)
                    results["shots"].append(fm_path)

            overflow = await page.evaluate(
                """() => ({
                  sw: document.documentElement.scrollWidth,
                  cw: document.documentElement.clientWidth
                })"""
            )
            results["overflow"][vp_name] = overflow

        html = await page.content()
        results["checks"] = {
            "custom_page": "zpm-custom-page" in html,
            "timeline_steps": html.count("zpm-corp-timeline__step"),
            "faq_items": html.count('id="custom-faq-btn-'),
            "cta_form": "zpm-custom-form" in html,
            "company_field": 'name="company"' in html,
            "project_description_field": 'name="project_description"' in html,
            "data_custom_faq": "data-custom-faq" in html,
            "approval_badge": "Согласование до производства" in html,
            "no_file_input": 'type="file"' not in html,
        }
        results["checks"]["pass"] = (
            results["checks"]["custom_page"]
            and results["checks"]["timeline_steps"] >= 8
            and results["checks"]["faq_items"] >= 8
            and results["checks"]["company_field"]
            and results["checks"]["project_description_field"]
            and results["checks"]["data_custom_faq"]
            and results["checks"]["no_file_input"]
            and len(results["console_errors"]) == 0
            and all(v.get("sw", 0) <= v.get("cw", 9999) + 1 for v in results["overflow"].values())
        )

        await browser.close()

    out = os.path.join(OUT_DIR, "m9.18-custom-qa-results.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
