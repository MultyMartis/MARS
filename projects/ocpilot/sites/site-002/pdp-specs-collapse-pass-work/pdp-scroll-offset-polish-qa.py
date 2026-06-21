#!/usr/bin/env python3
"""QA — PDP V5.1 scroll offset polish (live getBoundingClientRect)."""
import asyncio
import json
import os
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("playwright not installed")
    sys.exit(1)

BASE = "https://zpm.new-site.space"
URL_SPKB = (
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
    "stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
)
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\pdp-v5.1-scroll-offset-polish"
RESULT_PATH = os.path.join(OUT_DIR, "pdp-v5.1-scroll-offset-polish-qa-result.json")

DESKTOP_EXPECT = 140
MOBILE_EXPECT = 100
TOLERANCE = 15


async def wait_for_scroll_end(page, timeout_ms=5000):
    """Wait until scroll position stabilizes after smooth scroll."""
    await page.wait_for_timeout(300)
    prev = -1
    stable = 0
    elapsed = 0
    step = 100
    while elapsed < timeout_ms:
        y = await page.evaluate("window.pageYOffset")
        if y == prev:
            stable += 1
            if stable >= 3:
                return y
        else:
            stable = 0
            prev = y
        await page.wait_for_timeout(step)
        elapsed += step
    return prev


async def measure_main_top(page):
    return await page.evaluate(
        """() => {
          const el = document.querySelector('.product-content__main');
          if (!el) return null;
          return Math.round(el.getBoundingClientRect().top * 10) / 10;
        }"""
    )


async def run_viewport_test(page, viewport, expected, label):
    await page.set_viewport_size(viewport)
    await page.goto(URL_SPKB, wait_until="networkidle", timeout=90000)
    await page.wait_for_selector("[data-product-specs-toggle]", timeout=30000)

    toggle = page.locator("[data-product-specs-toggle]")
    toggle_text = await page.locator("[data-product-specs-toggle-text]").inner_text()

    await toggle.scroll_into_view_if_needed()
    await page.wait_for_timeout(200)

    await toggle.click()
    await wait_for_scroll_end(page)
    expand_top = await measure_main_top(page)
    expanded_text = await page.locator("[data-product-specs-toggle-text]").inner_text()

    await toggle.click()
    await wait_for_scroll_end(page)
    collapse_top = await measure_main_top(page)
    collapsed_text = await page.locator("[data-product-specs-toggle-text]").inner_text()

    expand_ok = expand_top is not None and abs(expand_top - expected) <= TOLERANCE
    collapse_ok = collapse_top is not None and abs(collapse_top - expected) <= TOLERANCE

    return {
        "label": label,
        "viewport": viewport,
        "expected_top": expected,
        "tolerance": TOLERANCE,
        "expand_top": expand_top,
        "collapse_top": collapse_top,
        "expand_ok": expand_ok,
        "collapse_ok": collapse_ok,
        "toggle_before": toggle_text.strip(),
        "toggle_after_expand": expanded_text.strip(),
        "toggle_after_collapse": collapsed_text.strip(),
        "pass": expand_ok and collapse_ok,
    }


async def verify_live_js(page):
    stamp = __import__("datetime").datetime.now().strftime("%Y%m%d%H%M%S")
    url = f"{BASE}/assets/js/main.js?v=qa-{stamp}"
    resp = await page.request.get(url, headers={"Cookie": "beget=begetok"})
    body = await resp.text()
    return {
        "url": url,
        "size": len(body),
        "has_window_scrollTo_offset": "offset = isMobile ? 100 : 140" in body,
        "has_scrollIntoView_in_fn": "target.scrollIntoView" in body,
        "has_scrollToProductContentMain": "scrollToProductContentMain" in body,
    }


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    results = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})

        results["liveMainJs"] = await verify_live_js(page)
        results["desktop"] = await run_viewport_test(
            page, {"width": 1440, "height": 900}, DESKTOP_EXPECT, "desktop-1440"
        )
        results["mobile"] = await run_viewport_test(
            page, {"width": 390, "height": 844}, MOBILE_EXPECT, "mobile-390"
        )

        await browser.close()

    results["qa_pass"] = (
        results["liveMainJs"].get("has_window_scrollTo_offset")
        and not results["liveMainJs"].get("has_scrollIntoView_in_fn")
        and results["desktop"]["pass"]
        and results["mobile"]["pass"]
    )

    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(json.dumps(results, ensure_ascii=False, indent=2))
    print("QA result:", RESULT_PATH)
    print("QA_PASS:", results["qa_pass"])
    sys.exit(0 if results["qa_pass"] else 1)


if __name__ == "__main__":
    asyncio.run(main())
