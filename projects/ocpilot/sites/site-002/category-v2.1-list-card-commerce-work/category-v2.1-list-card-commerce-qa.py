#!/usr/bin/env python3
"""QA + screenshots — SITE-002 CATEGORY V2.1 list card commerce pass."""
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
WISHLIST_URL = BASE + "/index.php?route=account/wishlist"
COMPARE_URL = BASE + "/index.php?route=product/compare"
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\category-v2.1-list-card-commerce"
QA_JSON = os.path.join(OUT_DIR, "category-v2.1-list-card-commerce-qa-result.json")

DESKTOP = [(1920, 1080), (1440, 900), (1366, 768), (1280, 800), (1024, 768)]
MOBILE = [(768, 1024), (576, 800), (390, 844), (375, 812), (360, 800)]


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
        const card = document.querySelector('.p-card');
        const media = card ? card.querySelector('.p-card__media-wrap') : null;
        const specs = card ? card.querySelector('.p-card__primary-specs') : null;
        const specItems = specs ? specs.querySelectorAll('.p-card__primary-spec') : [];
        const specsDisplay = specs ? getComputedStyle(specs).display : null;
        const mediaW = media ? Math.round(media.getBoundingClientRect().width) : null;
        const listClass = section ? section.classList.contains('category--view-list') : false;
        const specLabels = specs ? Array.from(specs.querySelectorAll('dt')).map(el => el.textContent.trim()) : [];
        const specValues = specs ? Array.from(specs.querySelectorAll('dd')).map(el => el.textContent.trim()) : [];
        return {
            mode,
            list_class: listClass,
            card_count: grid ? grid.querySelectorAll('.p-card').length : 0,
            media_width: mediaW,
            specs_visible: specsDisplay !== 'none',
            specs_display: specsDisplay,
            spec_count: specItems.length,
            spec_labels: specLabels,
            spec_values: specValues,
            has_cart: !!document.querySelector('[data-cart-add]'),
            has_qty: !!document.querySelector('[data-cart-qty]'),
            has_wishlist: !!document.querySelector('[data-fav-toggle]'),
            has_compare: !!document.querySelector('[data-compare-toggle]'),
            has_details: !!document.querySelector('.p-card__footer .btn-no-text, .p-card__footer .btn_dark'),
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


async def check_shared_specs_hidden(page, url, label):
    await page.set_viewport_size({"width": 1920, "height": 1080})
    await page.goto(url, wait_until="networkidle", timeout=120000)
    await page.wait_for_timeout(1000)
    return await page.evaluate(
        """(label) => {
        const cards = document.querySelectorAll('.p-card');
        let visibleSpecs = 0;
        cards.forEach(card => {
            const specs = card.querySelector('.p-card__primary-specs');
            if (specs && getComputedStyle(specs).display !== 'none') visibleSpecs++;
        });
        return {
            context: label,
            card_count: cards.length,
            visible_specs_blocks: visibleSpecs,
            pass: visibleSpecs === 0,
        };
    }""",
        label,
    )


async def check_pdp(page):
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
            card_specs_in_related: Array.from(document.querySelectorAll('.rel-products .p-card__primary-specs')).filter(el => getComputedStyle(el).display !== 'none').length,
        })"""
    )
    path = os.path.join(OUT_DIR, "pdp-v4-regression-1920.png")
    await page.screenshot(path=path, full_page=False)
    pdp["screenshot"] = path
    pdp["pass"] = pdp["hero_cols"] >= 3 and pdp["commerce"] and pdp["content"] and pdp["card_specs_in_related"] == 0
    return pdp


async def test_mobile_grid(page):
    results = []
    for w, h in MOBILE:
        await page.set_viewport_size({"width": w, "height": h})
        await page.goto(CATEGORY_URL, wait_until="networkidle", timeout=120000)
        await page.wait_for_selector(".category__grid", timeout=45000)
        m = await page.evaluate(
            """(vp) => {
            const specs = document.querySelector('.p-card__primary-specs');
            return {
                viewport: vp,
                view_hidden: getComputedStyle(document.querySelector('.category__view')).display === 'none',
                list_class: document.querySelector('section.category')?.classList.contains('category--view-list'),
                specs_visible: specs ? getComputedStyle(specs).display !== 'none' : false,
            };
        }""",
            f"{w}x{h}",
        )
        path = os.path.join(OUT_DIR, f"category-mobile-grid-{w}.png")
        await page.screenshot(path=path, full_page=False)
        m["screenshot"] = path
        m["pass"] = not m["specs_visible"]
        results.append(m)
        print("mobile", w, m)
    return results


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    results = {
        "category_url": CATEGORY_URL,
        "desktop_grid": [],
        "desktop_list": [],
        "mobile_grid": [],
        "shared_contexts": {},
        "pdp": None,
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})

        for w, h in DESKTOP:
            results["desktop_grid"].append(await shot_category(page, w, h, "grid"))
        for w, h in DESKTOP:
            results["desktop_list"].append(await shot_category(page, w, h, "list"))

        results["mobile_grid"] = await test_mobile_grid(page)
        results["shared_contexts"]["search"] = await check_shared_specs_hidden(page, SEARCH_URL, "search")
        results["shared_contexts"]["wishlist"] = await check_shared_specs_hidden(page, WISHLIST_URL, "wishlist")
        results["shared_contexts"]["compare"] = await check_shared_specs_hidden(page, COMPARE_URL, "compare")
        results["pdp"] = await check_pdp(page)

        await browser.close()

    grid_ok = all(not m["specs_visible"] for m in results["desktop_grid"])
    list_ok = all(
        m["specs_visible"] and m["spec_count"] >= 1 and m["media_width"] == 200
        for m in results["desktop_list"]
    )
    results["summary"] = {
        "grid_specs_hidden": grid_ok,
        "list_specs_visible": list_ok,
        "mobile_specs_hidden": all(m["pass"] for m in results["mobile_grid"]),
        "shared_pass": all(v.get("pass") for v in results["shared_contexts"].values()),
        "pdp_pass": results["pdp"]["pass"] if results["pdp"] else False,
    }

    with open(QA_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("QA JSON", QA_JSON)
    print("Summary", results["summary"])


if __name__ == "__main__":
    asyncio.run(main())
