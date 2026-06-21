#!/usr/bin/env python3
"""QA + screenshots — SITE-002 CATEGORY V2.3 subcategory chips pass."""
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
URL_MANY = BASE + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"
URL_FEW = BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
URL_LEAF = BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/"
PDP_URL = (
    BASE
    + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
    + "stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
)
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\category-v2.3-subcategory-chips"
QA_JSON = os.path.join(OUT_DIR, "category-v2.3-subcategory-chips-qa-result.json")

DESKTOP = [(1920, 1080), (1440, 900)]
MOBILE = [(768, 1024), (576, 800), (390, 844), (375, 812), (360, 800)]


async def measure_subcats(page):
    return await page.evaluate(
        """() => {
        const block = document.querySelector('.page--category [data-subcat-chips]');
        const list = block ? block.querySelector('[data-subcat-chips-list]') : null;
        const toggle = block ? block.querySelector('[data-subcat-chips-toggle]') : null;
        const chips = list ? list.querySelectorAll('.zpm-sub-cat-chip') : [];
        const blockRect = block ? block.getBoundingClientRect() : null;
        const listRect = list ? list.getBoundingClientRect() : null;
        const docEl = document.documentElement;
        const body = document.body;
        const overflowX = Math.max(
            docEl.scrollWidth,
            body ? body.scrollWidth : 0
        ) > window.innerWidth + 1;
        return {
            has_block: !!block,
            chip_count: chips.length,
            is_collapsible: block ? block.classList.contains('is-collapsible') : false,
            is_collapsed: block ? block.classList.contains('is-collapsed') : false,
            is_expanded: block ? block.classList.contains('is-expanded') : false,
            toggle_hidden: toggle ? toggle.hidden : true,
            toggle_label: toggle ? (toggle.textContent || '').trim() : '',
            toggle_aria: toggle ? toggle.getAttribute('aria-expanded') : null,
            block_height: blockRect ? Math.round(blockRect.height) : null,
            list_height: listRect ? Math.round(listRect.height) : null,
            list_scroll_height: list ? list.scrollHeight : null,
            horizontal_overflow: overflowX,
        };
    }"""
    )


async def measure_regression(page):
    return await page.evaluate(
        """() => {
        const section = document.querySelector('.page--category section.category');
        const grid = document.querySelector('.category__grid');
        const view = document.querySelector('.category__view');
        const filterBtn = document.querySelector('.category__filters-btn');
        const card = document.querySelector('.p-card');
        const gridStyle = grid ? getComputedStyle(grid) : null;
        const cols = gridStyle
            ? gridStyle.gridTemplateColumns.split(' ').filter(Boolean).length
            : 0;
        return {
            has_category: !!section,
            grid_cols: cols,
            card_count: grid ? grid.querySelectorAll('.p-card').length : 0,
            view_display: view ? getComputedStyle(view).display : null,
            filter_btn: !!filterBtn,
            has_card: !!card,
        };
    }"""
    )


async def measure_pdp(page):
    return await page.evaluate(
        """() => {
        const hero = document.querySelector('.pdp-hero, .product-hero, [class*="pdp"]');
        const commerce = document.querySelector('.product-card__actions, .pdp-commerce');
        return {
            is_pdp: document.body.classList.contains('page--product'),
            has_hero: !!document.querySelector('.pdp-v4, .product-page'),
            has_commerce: !!commerce,
            subcat_block_on_pdp: !!document.querySelector('[data-subcat-chips]'),
        };
    }"""
    )


async def screenshot(page, name):
    path = os.path.join(OUT_DIR, name)
    await page.screenshot(path=path, full_page=False)
    return path


async def run_case(page, url, label, viewport, suffix):
    await page.set_viewport_size({"width": viewport[0], "height": viewport[1]})
    await page.goto(url, wait_until="networkidle", timeout=90000)
    await page.wait_for_timeout(800)

    collapsed = await measure_subcats(page)
    shot_collapsed = await screenshot(
        page, f"{label}-{viewport[0]}x{viewport[1]}-{suffix}-collapsed.png"
    )

    expanded = None
    shot_expanded = None
    if collapsed["has_block"] and not collapsed["toggle_hidden"]:
        await page.click("[data-subcat-chips-toggle]")
        await page.wait_for_timeout(400)
        expanded = await measure_subcats(page)
        shot_expanded = await screenshot(
            page, f"{label}-{viewport[0]}x{viewport[1]}-{suffix}-expanded.png"
        )

    regression = await measure_regression(page) if "category" in url else None
    return {
        "url": url,
        "label": label,
        "viewport": viewport,
        "collapsed": collapsed,
        "expanded": expanded,
        "regression": regression,
        "screenshots": {
            "collapsed": shot_collapsed,
            "expanded": shot_expanded,
        },
    }


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    results = {"cases": [], "pdp": None, "leaf": None}

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for vp in DESKTOP:
            results["cases"].append(
                await run_case(page, URL_MANY, "moechnye-vanny", vp, "desktop")
            )
            results["cases"].append(
                await run_case(page, URL_FEW, "stoly-tumby-premium", vp, "desktop")
            )

        for vp in MOBILE:
            results["cases"].append(
                await run_case(page, URL_MANY, "moechnye-vanny", vp, "mobile")
            )
            results["cases"].append(
                await run_case(page, URL_FEW, "stoly-tumby-premium", vp, "mobile")
            )

        await page.set_viewport_size({"width": 1440, "height": 900})
        await page.goto(URL_LEAF, wait_until="networkidle", timeout=90000)
        await page.wait_for_timeout(500)
        results["leaf"] = {
            "url": URL_LEAF,
            "subcats": await measure_subcats(page),
            "regression": await measure_regression(page),
        }

        await page.goto(PDP_URL, wait_until="networkidle", timeout=90000)
        await page.wait_for_timeout(500)
        results["pdp"] = {
            "url": PDP_URL,
            "metrics": await measure_pdp(page),
            "screenshot": await screenshot(page, "pdp-v4-regression-1440x900.png"),
        }

        await browser.close()

    checks = []
    many_desktop = next(c for c in results["cases"] if c["label"] == "moechnye-vanny" and c["viewport"][0] == 1920)
    few_desktop = next(c for c in results["cases"] if c["label"] == "stoly-tumby-premium" and c["viewport"][0] == 1920)

    checks.append(
        {
            "name": "many_subcats_collapsible",
            "pass": many_desktop["collapsed"]["is_collapsible"]
            and not many_desktop["collapsed"]["toggle_hidden"],
        }
    )
    checks.append(
        {
            "name": "many_subcats_collapsed_default",
            "pass": many_desktop["collapsed"]["is_collapsed"]
            and many_desktop["collapsed"]["toggle_aria"] == "false",
        }
    )
    checks.append(
        {
            "name": "many_subcats_expanded_works",
            "pass": bool(
                many_desktop["expanded"]
                and many_desktop["expanded"]["is_expanded"]
                and many_desktop["expanded"]["toggle_aria"] == "true"
            ),
        }
    )
    checks.append(
        {
            "name": "few_subcats_no_toggle",
            "pass": few_desktop["collapsed"]["toggle_hidden"]
            or not few_desktop["collapsed"]["is_collapsible"],
        }
    )

    mobile_overflow = [
        c
        for c in results["cases"]
        if c["viewport"][0] <= 768 and c["label"] == "moechnye-vanny"
    ]
    checks.append(
        {
            "name": "mobile_no_horizontal_overflow",
            "pass": all(not c["collapsed"]["horizontal_overflow"] for c in mobile_overflow),
        }
    )
    checks.append(
        {
            "name": "leaf_no_subcat_block_or_ok",
            "pass": not results["leaf"]["subcats"]["has_block"]
            or results["leaf"]["subcats"]["chip_count"] == 0,
        }
    )
    checks.append(
        {
            "name": "pdp_no_subcat_block",
            "pass": not results["pdp"]["metrics"]["subcat_block_on_pdp"],
        }
    )
    checks.append(
        {
            "name": "grid_regression",
            "pass": results["leaf"]["regression"]["card_count"] > 0
            and results["leaf"]["regression"]["grid_cols"] >= 2,
        }
    )

    results["checks"] = checks
    results["all_pass"] = all(c["pass"] for c in checks)

    with open(QA_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("QA JSON:", QA_JSON)
    print("All pass:", results["all_pass"])
    for c in checks:
        print(f"  {'PASS' if c['pass'] else 'FAIL'} — {c['name']}")


if __name__ == "__main__":
    asyncio.run(main())
