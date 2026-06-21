#!/usr/bin/env python3
"""M9.8.9-04 — QA: filter apply scroll to section.category with header offset."""
from __future__ import annotations

import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("playwright not installed")
    sys.exit(1)

BASE = "https://zpm.new-site.space"
OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-04-work")
OUT_JSON = OUT_DIR / "qa-results.json"

TOLERANCE = 20

CATEGORIES = [
    {
        "id": "stoly",
        "name": "Столы",
        "url": BASE + "/katalog/nejtralnoe-oborudovanie/stoly/",
    },
    {
        "id": "moechnye",
        "name": "Моечные ванны",
        "url": BASE + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
    },
    {
        "id": "podtovarniki",
        "name": "Подтоварники",
        "url": BASE + "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
    },
    {
        "id": "telezhki",
        "name": "Тележки",
        "url": BASE + "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/",
    },
]


async def wait_for_scroll_end(page, timeout_ms=6000):
    await page.wait_for_timeout(300)
    prev = -1
    stable = 0
    elapsed = 0
    while elapsed < timeout_ms:
        y = await page.evaluate("window.pageYOffset")
        if y == prev:
            stable += 1
            if stable >= 3:
                return y
        else:
            stable = 0
            prev = y
        await page.wait_for_timeout(100)
        elapsed += 100
    return prev


async def measure_section_top(page):
    return await page.evaluate(
        """() => {
          const el = document.querySelector('.page--category section.category') ||
            document.querySelector('section.category');
          if (!el) return { top: null, found: false };
          return {
            found: true,
            top: Math.round(el.getBoundingClientRect().top * 10) / 10,
            tag: el.tagName,
            className: el.className
          };
        }"""
    )


async def get_expected_offset(page):
    return await page.evaluate(
        """() => {
          const isMobile = window.innerWidth <= 1024;
          const stickyEl = isMobile
            ? document.querySelector('[data-header-mobilebar]')
            : document.querySelector('[data-header-sticky]');
          let measured = 0;
          if (stickyEl) measured = Math.ceil(stickyEl.getBoundingClientRect().height);
          const cssVal = getComputedStyle(document.documentElement)
            .getPropertyValue('--header-posotopn-and-size').trim();
          const parsed = parseInt(cssVal, 10);
          const fallback = isMobile ? 100 : 140;
          return {
            isMobile,
            measured,
            cssVar: parsed || null,
            expected: measured > 0 ? measured : (parsed > 0 ? parsed : fallback)
          };
        }"""
    )


async def verify_live_js(page):
    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    url = f"{BASE}/assets/js/main.js?v=qa-{stamp}"
    resp = await page.request.get(url, headers={"Cookie": "beget=begetok"})
    body = await resp.text()
    return {
        "url": url,
        "size": len(body),
        "has_scrollToCategorySection": "function scrollToCategorySection()" in body,
        "has_getPageScrollOffset": "function getPageScrollOffset()" in body,
        "no_grid_scrollIntoView_in_updateProducts": "grid.scrollIntoView" not in body,
    }


async def run_category_test(page, cat, viewport):
    await page.set_viewport_size(viewport)
    await page.goto(cat["url"], wait_until="networkidle", timeout=90000)
    await page.wait_for_selector("section.category", timeout=30000)

    is_mobile = viewport["width"] <= 1024
    if is_mobile:
        open_btn = page.locator("[data-filter-open]")
        if await open_btn.count() > 0:
            await open_btn.first.click()
            await page.wait_for_timeout(400)

    await page.wait_for_selector("[data-filters-form]", timeout=30000, state="visible")

    errors: list[str] = []
    page.on("pageerror", lambda err: errors.append(str(err)))

    offset_info = await get_expected_offset(page)
    expected = offset_info["expected"]

    await page.evaluate("window.scrollTo(0, 1200)")
    await page.wait_for_timeout(400)

    before = await measure_section_top(page)
    initial_cards = await page.locator(".p-card").count()

    await page.locator('input[name="price_from"]').scroll_into_view_if_needed()
    await page.locator('input[name="price_from"]').fill("1000")
    await page.locator('input[name="price_to"]').fill("500000")
    await page.locator('input[name="price_to"]').dispatch_event("change")
    await page.wait_for_timeout(900)

    try:
        await page.wait_for_function(
            "() => document.querySelector('.category__grid')?.style.opacity === '0.5'",
            timeout=5000,
        )
    except Exception:
        pass

    await page.wait_for_function(
        """() => {
          const g = document.querySelector('.category__grid');
          return g && g.style.opacity === '1' && g.style.pointerEvents === 'all';
        }""",
        timeout=20000,
    )
    await wait_for_scroll_end(page)

    after = await measure_section_top(page)
    scroll_y = await page.evaluate("window.pageYOffset")
    final_cards = await page.locator(".p-card").count()
    ajax_ok = final_cards > 0

    top = after.get("top")
    offset_ok = top is not None and abs(top - expected) <= TOLERANCE

    return {
        "viewport": viewport,
        "offset_info": offset_info,
        "expected_top": expected,
        "tolerance": TOLERANCE,
        "section_found": after.get("found"),
        "section_top_after": top,
        "scroll_y_after": scroll_y,
        "offset_ok": offset_ok,
        "ajax_cards_before": initial_cards,
        "ajax_cards_after": final_cards,
        "ajax_ok": ajax_ok,
        "js_errors": errors,
        "pass": offset_ok and ajax_ok and after.get("found") and not errors,
    }


async def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results: dict = {
        "task": "M9.8.9-04",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "categories": [],
        "all_pass": True,
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})

        results["liveMainJs"] = await verify_live_js(page)
        js_ok = (
            results["liveMainJs"]["has_scrollToCategorySection"]
            and results["liveMainJs"]["has_getPageScrollOffset"]
            and results["liveMainJs"]["no_grid_scrollIntoView_in_updateProducts"]
        )
        if not js_ok:
            results["all_pass"] = False

        for cat in CATEGORIES:
            entry = {
                "id": cat["id"],
                "name": cat["name"],
                "url": cat["url"],
                "desktop": await run_category_test(
                    page, cat, {"width": 1440, "height": 900}
                ),
                "mobile": await run_category_test(
                    page, cat, {"width": 390, "height": 844}
                ),
            }
            entry["pass"] = entry["desktop"]["pass"] and entry["mobile"]["pass"]
            if not entry["pass"]:
                results["all_pass"] = False
            results["categories"].append(entry)

        await browser.close()

    results["qa_pass"] = results["all_pass"] and js_ok
    OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))
    print("QA result:", OUT_JSON)
    print("QA_PASS:", results["qa_pass"])
    sys.exit(0 if results["qa_pass"] else 1)


if __name__ == "__main__":
    asyncio.run(main())
