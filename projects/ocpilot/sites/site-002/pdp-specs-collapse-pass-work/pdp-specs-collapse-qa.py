#!/usr/bin/env python3
"""QA — PDP V5.1 specifications collapse pass."""
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
URL_VMS = (
    BASE + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-svarnye-premium/"
    "vanna-moechnaya-vms-p-2-600-1400h700h850"
)
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\pdp-specs-collapse-pass"
RESULT_PATH = os.path.join(OUT_DIR, "pdp-specs-collapse-qa-result.json")

DESKTOP_WIDTHS = [1920, 1440, 1366, 1280]
MOBILE_WIDTHS = [768, 576, 390, 375, 360]


async def evaluate_specs(page):
    return await page.evaluate(
        """() => {
          const section = document.querySelector('.product-content__specifications');
          if (!section) return { error: 'no specs section' };
          const table = section.querySelector('.spec-table');
          const rows = table ? table.querySelectorAll('.spec-table__row') : [];
          const toggleWrap = section.querySelector('.product-content__specs-toggle-wrap');
          const toggleBtn = section.querySelector('[data-product-specs-toggle]');
          const toggleText = section.querySelector('[data-product-specs-toggle-text]');
          const styles = table ? getComputedStyle(table) : null;
          return {
            rowCount: rows.length,
            limit: window.innerWidth > 767 ? 8 : 5,
            isCollapsible: section.classList.contains('is-collapsible'),
            isCollapsed: section.classList.contains('is-collapsed'),
            isExpanded: section.classList.contains('is-expanded'),
            toggleHidden: toggleWrap ? toggleWrap.hidden : true,
            toggleText: toggleText ? toggleText.textContent.trim() : '',
            maxHeight: styles ? styles.maxHeight : '',
            overflow: styles ? styles.overflow : '',
            hasHorizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
            descriptionOk: !!document.querySelector('.product-content__description, .product-content__side'),
            documentsOk: !!document.querySelector('.product-content__documents'),
            relatedOk: !!document.querySelector('.rel-products'),
            cartOk: !!document.querySelector('[data-cart-add]'),
          };
        }"""
    )


async def shot_specs(page, url, name, viewport):
    await page.set_viewport_size(viewport)
    await page.goto(url, wait_until="networkidle", timeout=90000)
    await page.wait_for_selector(".product-content__specifications", timeout=30000)
    section = page.locator(".product-content__specifications")
    await section.scroll_into_view_if_needed()
    path = os.path.join(OUT_DIR, name)
    await section.screenshot(path=path)
    state = await evaluate_specs(page)
    return path, state


async def test_toggle(page, url, viewport, prefix):
    await page.set_viewport_size(viewport)
    await page.goto(url, wait_until="networkidle", timeout=90000)
    await page.wait_for_selector("[data-product-specs-toggle]", timeout=30000)

    before = await evaluate_specs(page)
    if before.get("toggleHidden"):
        return {"prefix": prefix, "skipped": True, "before": before}

    await page.click("[data-product-specs-toggle]")
    await page.wait_for_timeout(400)
    expanded = await evaluate_specs(page)
    path_exp = os.path.join(OUT_DIR, f"{prefix}-expanded.png")
    await page.locator(".product-content__specifications").screenshot(path=path_exp)

    await page.click("[data-product-specs-toggle]")
    await page.wait_for_timeout(400)
    collapsed = await evaluate_specs(page)
    path_col = os.path.join(OUT_DIR, f"{prefix}-collapsed-after-toggle.png")
    await page.locator(".product-content__specifications").screenshot(path=path_col)

    return {
        "prefix": prefix,
        "before": before,
        "expanded": expanded,
        "collapsed": collapsed,
        "shots": [path_exp, path_col],
    }


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    results = {"screenshots": [], "checks": [], "toggleTests": []}

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})

        for w in DESKTOP_WIDTHS:
            path, state = await shot_specs(page, URL_SPKB, f"spkb-desktop-{w}.png", {"width": w, "height": 900})
            results["screenshots"].append(path)
            results["checks"].append({"url": "SPKB", "width": w, "state": state})

        for w in MOBILE_WIDTHS:
            path, state = await shot_specs(page, URL_SPKB, f"spkb-mobile-{w}.png", {"width": w, "height": 844})
            results["screenshots"].append(path)
            results["checks"].append({"url": "SPKB", "width": w, "state": state})

        path, state = await shot_specs(page, URL_VMS, "vms-desktop-1440.png", {"width": 1440, "height": 900})
        results["screenshots"].append(path)
        results["checks"].append({"url": "VMS", "width": 1440, "state": state})

        path, state = await shot_specs(page, URL_VMS, "vms-mobile-390.png", {"width": 390, "height": 844})
        results["screenshots"].append(path)
        results["checks"].append({"url": "VMS", "width": 390, "state": state})

        results["toggleTests"].append(await test_toggle(page, URL_SPKB, {"width": 1440, "height": 900}, "spkb-1440"))
        results["toggleTests"].append(await test_toggle(page, URL_SPKB, {"width": 390, "height": 844}, "spkb-390"))

        cat = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})
        await cat.set_viewport_size({"width": 1440, "height": 900})
        await cat.goto(BASE + "/katalog/nejtralnoe-oborudovanie/stoly/", wait_until="networkidle", timeout=90000)
        cat_path = os.path.join(OUT_DIR, "category-regression-1440.png")
        await cat.locator(".page--category").screenshot(path=cat_path)
        results["screenshots"].append(cat_path)
        results["categoryRegression"] = {
            "hasViewSwitcher": await cat.locator("[data-category-view-mode]").count() > 0,
            "path": cat_path,
        }

        await browser.close()

    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("QA result:", RESULT_PATH)
    for c in results["checks"]:
        s = c["state"]
        print(
            f"  {c['url']} {c['width']}px: rows={s.get('rowCount')} limit={s.get('limit')} "
            f"collapsible={s.get('isCollapsible')} collapsed={s.get('isCollapsed')} "
            f"toggleHidden={s.get('toggleHidden')} overflow={s.get('hasHorizontalOverflow')}"
        )


if __name__ == "__main__":
    asyncio.run(main())
