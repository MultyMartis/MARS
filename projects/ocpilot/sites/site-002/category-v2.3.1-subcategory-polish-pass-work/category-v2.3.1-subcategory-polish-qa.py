#!/usr/bin/env python3
"""QA + screenshots — SITE-002 CATEGORY V2.3.1 subcategory polish pass."""
import asyncio
import json
import os
import re
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
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\category-v2.3.1-subcategory-polish"
QA_JSON = os.path.join(OUT_DIR, "category-v2.3.1-subcategory-polish-qa-result.json")

DESKTOP = [(1920, 1080), (1440, 900), (1366, 768), (1280, 800)]
MOBILE = [(768, 1024), (576, 800), (390, 844), (375, 812), (360, 800)]


async def measure_subcats(page):
    return await page.evaluate(
        """() => {
        const block = document.querySelector('.page--category [data-subcat-chips]');
        const list = block ? block.querySelector('[data-subcat-chips-list]') : null;
        const toggle = block ? block.querySelector('[data-subcat-chips-toggle]') : null;
        const label = block ? block.querySelector('[data-subcat-chips-toggle-label]') : null;
        const chevron = block ? block.querySelector('[data-subcat-chips-toggle-chevron]') : null;
        const title = block ? block.querySelector('.zpm-sub-cat-chip--title') : null;
        const titleIcon = title ? title.querySelector('.fa-sitemap, .fa-layer-group') : null;
        const chips = list ? list.querySelectorAll('.zpm-sub-cat-chip') : [];
        const blockRect = block ? block.getBoundingClientRect() : null;
        const listRect = list ? list.getBoundingClientRect() : null;
        const docEl = document.documentElement;
        const body = document.body;
        const overflowX = Math.max(
            docEl.scrollWidth,
            body ? body.scrollWidth : 0
        ) > window.innerWidth + 1;

        let hiddenCount = null;
        if (list && chips.length) {
            const listRectInner = list.getBoundingClientRect();
            const rows = [];
            chips.forEach((chip) => {
                const top = Math.round(chip.getBoundingClientRect().top - listRectInner.top);
                let rowIndex = rows.findIndex((r) => Math.abs(r.top - top) <= 2);
                if (rowIndex === -1) rows.push({ top, count: 1 });
                else rows[rowIndex].count += 1;
            });
            rows.sort((a, b) => a.top - b.top);
            if (rows.length > 2) {
                const visible = rows.slice(0, 2).reduce((s, r) => s + r.count, 0);
                hiddenCount = chips.length - visible;
            } else {
                hiddenCount = 0;
            }
        }

        return {
            has_block: !!block,
            chip_count: chips.length,
            is_collapsible: block ? block.classList.contains('is-collapsible') : false,
            is_collapsed: block ? block.classList.contains('is-collapsed') : false,
            is_expanded: block ? block.classList.contains('is-expanded') : false,
            toggle_hidden: toggle ? toggle.hidden : true,
            toggle_label: label ? (label.textContent || '').trim() : '',
            toggle_aria: toggle ? toggle.getAttribute('aria-expanded') : null,
            chevron_class: chevron ? chevron.className : '',
            title_has_icon: !!titleIcon,
            title_icon_class: titleIcon ? titleIcon.className : '',
            hidden_count_expected: hiddenCount,
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


def label_has_hidden_count(label, hidden):
    if hidden is None or hidden <= 0:
        return True
    return str(hidden) in label and "подкатег" in label.lower()


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

    many_1920 = next(
        c for c in results["cases"] if c["label"] == "moechnye-vanny" and c["viewport"][0] == 1920
    )
    few_1920 = next(
        c
        for c in results["cases"]
        if c["label"] == "stoly-tumby-premium" and c["viewport"][0] == 1920
    )

    checks = [
        {
            "name": "title_icon_visible",
            "pass": many_1920["collapsed"]["title_has_icon"],
        },
        {
            "name": "many_subcats_collapsible",
            "pass": many_1920["collapsed"]["is_collapsible"]
            and not many_1920["collapsed"]["toggle_hidden"],
        },
        {
            "name": "many_subcats_collapsed_default",
            "pass": many_1920["collapsed"]["is_collapsed"]
            and many_1920["collapsed"]["toggle_aria"] == "false",
        },
        {
            "name": "collapsed_chevron_down",
            "pass": "fa-chevron-down" in many_1920["collapsed"]["chevron_class"],
        },
        {
            "name": "collapsed_label_has_count",
            "pass": label_has_hidden_count(
                many_1920["collapsed"]["toggle_label"],
                many_1920["collapsed"]["hidden_count_expected"],
            ),
        },
        {
            "name": "many_subcats_expanded_works",
            "pass": bool(
                many_1920["expanded"]
                and many_1920["expanded"]["is_expanded"]
                and many_1920["expanded"]["toggle_aria"] == "true"
            ),
        },
        {
            "name": "expanded_chevron_up",
            "pass": bool(
                many_1920["expanded"]
                and "fa-chevron-up" in many_1920["expanded"]["chevron_class"]
            ),
        },
        {
            "name": "expanded_label_collapse",
            "pass": bool(
                many_1920["expanded"]
                and many_1920["expanded"]["toggle_label"] == "Свернуть"
            ),
        },
        {
            "name": "few_subcats_no_toggle",
            "pass": few_1920["collapsed"]["toggle_hidden"]
            or not few_1920["collapsed"]["is_collapsible"],
        },
    ]

    desktop_cases = [c for c in results["cases"] if c["viewport"][0] >= 1280]
    mobile_cases = [c for c in results["cases"] if c["viewport"][0] <= 768]

    checks.append(
        {
            "name": "desktop_title_icon_all",
            "pass": all(
                (not c["collapsed"]["has_block"]) or c["collapsed"]["title_has_icon"]
                for c in desktop_cases
                if c["label"] == "moechnye-vanny"
            ),
        }
    )
    checks.append(
        {
            "name": "mobile_no_horizontal_overflow",
            "pass": all(
                not c["collapsed"]["horizontal_overflow"]
                for c in mobile_cases
                if c["label"] == "moechnye-vanny"
            ),
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
    checks.append(
        {
            "name": "filter_regression",
            "pass": results["leaf"]["regression"]["filter_btn"],
        }
    )
    checks.append(
        {
            "name": "view_switcher_regression",
            "pass": results["leaf"]["regression"]["view_display"] not in (None, "none"),
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
