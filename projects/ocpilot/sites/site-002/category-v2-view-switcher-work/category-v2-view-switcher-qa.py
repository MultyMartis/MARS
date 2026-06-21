#!/usr/bin/env python3
"""QA + screenshots — SITE-002 CATEGORY V2 view switcher pass."""
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
CATEGORY_URL = BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/"
PDP_URL = BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
SEARCH_URL = BASE + "/index.php?route=product/search&search=стол"
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\category-v2-view-switcher"
QA_JSON = os.path.join(OUT_DIR, "category-v2-view-switcher-qa-result.json")

DESKTOP = [(1920, 1080), (1440, 900), (1366, 768), (1280, 800), (1024, 768)]


async def set_view(page, mode):
    if mode == "list":
        await page.evaluate(
            """() => {
            localStorage.setItem('zpm_category_view', 'list');
            const s = document.querySelector('.page--category section.category');
            if (s) s.classList.add('category--view-list');
            document.querySelectorAll('[data-category-view-mode]').forEach(btn => {
                const active = btn.getAttribute('data-category-view-mode') === 'list';
                btn.classList.toggle('is-active', active);
                btn.setAttribute('aria-pressed', active ? 'true' : 'false');
            });
        }"""
        )
    else:
        await page.evaluate(
            """() => {
            localStorage.setItem('zpm_category_view', 'grid');
            const s = document.querySelector('.page--category section.category');
            if (s) s.classList.remove('category--view-list');
            document.querySelectorAll('[data-category-view-mode]').forEach(btn => {
                const active = btn.getAttribute('data-category-view-mode') === 'grid';
                btn.classList.toggle('is-active', active);
                btn.setAttribute('aria-pressed', active ? 'true' : 'false');
            });
        }"""
        )
    await page.wait_for_timeout(300)


async def measure_category(page, mode):
    return await page.evaluate(
        """(mode) => {
        const section = document.querySelector('.page--category section.category');
        const grid = document.querySelector('.category__grid');
        const view = document.querySelector('.category__view');
        const card = document.querySelector('.p-card');
        const media = card ? card.querySelector('.p-card__media-wrap') : null;
        const bodyStatus = card ? card.querySelector('.p-card__body .p-card__status') : null;
        const topStatus = card ? card.querySelector('.p-card__top .p-card__status') : null;
        const gridStyle = grid ? getComputedStyle(grid) : null;
        const cols = gridStyle ? gridStyle.gridTemplateColumns.split(' ').filter(Boolean).length : 0;
        const mediaW = media ? Math.round(media.getBoundingClientRect().width) : null;
        const viewDisplay = view ? getComputedStyle(view).display : null;
        const listClass = section ? section.classList.contains('category--view-list') : false;
        const bodyStatusDisplay = bodyStatus ? getComputedStyle(bodyStatus).display : null;
        const topStatusDisplay = topStatus ? getComputedStyle(topStatus).display : null;
        return {
            mode,
            list_class: listClass,
            grid_cols: cols,
            card_count: grid ? grid.querySelectorAll('.p-card').length : 0,
            view_visible: viewDisplay !== 'none',
            view_display: viewDisplay,
            media_width: mediaW,
            body_status_display: bodyStatusDisplay,
            top_status_display: topStatusDisplay,
            has_sort: !!document.querySelector('.category__sort'),
            has_filter_btn: !!document.querySelector('.category__filters-btn'),
            has_pagination: !!document.querySelector('.pagination'),
            has_cart: !!document.querySelector('[data-cart-add]'),
            has_wishlist: !!document.querySelector('[data-fav-toggle]'),
            has_compare: !!document.querySelector('[data-compare-toggle]'),
            horizontal_overflow: document.documentElement.scrollWidth > window.innerWidth + 2,
        };
    }""",
        mode,
    )


async def shot_category(page, width, height, mode):
    await page.set_viewport_size({"width": width, "height": height})
    await page.goto(CATEGORY_URL, wait_until="networkidle", timeout=120000)
    await page.wait_for_selector(".category__grid .p-card", timeout=45000)
    await set_view(page, mode)
    path = os.path.join(OUT_DIR, f"category-{mode}-{width}.png")
    await page.screenshot(path=path, full_page=False)
    metrics = await measure_category(page, mode)
    metrics["viewport"] = f"{width}x{height}"
    metrics["screenshot"] = path
    print("saved", path)
    return metrics


async def check_regression(page):
    results = {}
    await page.set_viewport_size({"width": 1920, "height": 1080})

    await page.goto(PDP_URL, wait_until="networkidle", timeout=120000)
    await page.wait_for_selector(".product-hero__grid", timeout=45000)
    pdp = await page.evaluate(
        """() => ({
            hero_cols: document.querySelectorAll('.product-hero__col').length,
            commerce: !!document.querySelector('.product-hero__commerce-card'),
            content: !!document.querySelector('.product-content'),
            docs: !!document.querySelector('.product-content__documents'),
            related: !!document.querySelector('.rel-products'),
        })"""
    )
    results["pdp"] = {"url": PDP_URL, "checks": pdp, "pass": pdp["hero_cols"] >= 3 and pdp["commerce"] and pdp["content"]}

    await page.goto(SEARCH_URL, wait_until="networkidle", timeout=120000)
    search = await page.evaluate(
        """() => ({
            has_grid: !!document.querySelector('.category__grid'),
            list_class_on_search: !!document.querySelector('section.category.category--view-list'),
            card_count: document.querySelectorAll('.p-card').length,
        })"""
    )
    results["search"] = {"url": SEARCH_URL, "checks": search, "pass": search["has_grid"] and not search["list_class_on_search"]}

    await page.goto(CATEGORY_URL, wait_until="networkidle", timeout=120000)
    await page.wait_for_selector(".p-card [data-fav-toggle]", timeout=45000)
    related_check = await page.evaluate(
        """() => {
        const card = document.querySelector('.p-card');
        return {
            wishlist: !!document.querySelector('[data-fav-toggle]'),
            compare: !!document.querySelector('[data-compare-toggle]'),
            cart: !!document.querySelector('[data-cart-add]'),
            qty: !!document.querySelector('[data-cart-qty]'),
        };
    }"""
    )
    results["category_interactions"] = related_check

    return results


async def test_localstorage(page):
    await page.set_viewport_size({"width": 1920, "height": 1080})
    await page.goto(CATEGORY_URL, wait_until="networkidle", timeout=120000)
    await page.wait_for_selector("[data-category-view-mode='list']", timeout=45000)
    await page.click("[data-category-view-mode='list']")
    await page.wait_for_timeout(200)
    await page.reload(wait_until="networkidle")
    await page.wait_for_selector(".category__grid .p-card", timeout=45000)
    persisted = await page.evaluate(
        """() => ({
            ls: localStorage.getItem('zpm_category_view'),
            list_class: document.querySelector('section.category')?.classList.contains('category--view-list'),
        })"""
    )
    return persisted


async def test_mobile_forces_grid(page):
    await page.set_viewport_size({"width": 768, "height": 1024})
    await page.goto(CATEGORY_URL, wait_until="networkidle", timeout=120000)
    await page.evaluate("localStorage.setItem('zpm_category_view', 'list')")
    await page.reload(wait_until="networkidle")
    await page.wait_for_selector(".category__grid", timeout=45000)
    return await page.evaluate(
        """() => ({
            view_hidden: getComputedStyle(document.querySelector('.category__view')).display === 'none',
            list_class: document.querySelector('section.category')?.classList.contains('category--view-list'),
            grid_cols: getComputedStyle(document.querySelector('.category__grid')).gridTemplateColumns,
        })"""
    )


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    results = {
        "category_url": CATEGORY_URL,
        "desktop_grid": [],
        "desktop_list": [],
        "localstorage": None,
        "mobile_grid_guard": None,
        "regression": None,
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})

        for w, h in DESKTOP:
            results["desktop_grid"].append(await shot_category(page, w, h, "grid"))
        for w, h in DESKTOP:
            results["desktop_list"].append(await shot_category(page, w, h, "list"))

        results["localstorage"] = await test_localstorage(page)
        results["mobile_grid_guard"] = await test_mobile_forces_grid(page)
        results["regression"] = await check_regression(page)

        await browser.close()

    with open(QA_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("QA JSON", QA_JSON)


if __name__ == "__main__":
    asyncio.run(main())
