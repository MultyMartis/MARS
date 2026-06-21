#!/usr/bin/env python3
"""QA + screenshots — SITE-002 CATEGORY V2.2 list card compactness pass."""
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
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\category-v2.2-list-card-compactness"
QA_JSON = os.path.join(OUT_DIR, "category-v2.2-list-card-compactness-qa-result.json")

DESKTOP = [(1920, 1080), (1440, 900), (1366, 768), (1280, 800), (1025, 768)]
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
    await page.wait_for_timeout(400)


async def measure_list_card(page):
    return await page.evaluate(
        """() => {
        const card = document.querySelector('.p-card');
        if (!card) return { error: 'no card' };
        const r = (el) => {
            if (!el) return null;
            const b = el.getBoundingClientRect();
            return { top: b.top, left: b.left, right: b.right, bottom: b.bottom, width: b.width, height: b.height };
        };
        const prices = card.querySelector('.p-card__prices');
        const wishlist = card.querySelector('[data-fav-toggle]');
        const compare = card.querySelector('[data-compare-toggle]');
        const cart = card.querySelector('[data-cart-add]');
        const qty = card.querySelector('[data-cart-qty]:not([aria-hidden="true"])');
        const details = card.querySelector('.p-card__footer .btn-no-text');
        const specs = card.querySelector('.p-card__primary-specs');
        const specItems = specs ? specs.querySelectorAll('.p-card__primary-spec') : [];
        const specIcons = specs ? specs.querySelectorAll('.p-card__primary-spec-icon i') : [];
        const iconClasses = Array.from(specIcons).map(i => i.className);
        const cs = specs ? getComputedStyle(specs) : null;
        const media = card.querySelector('.p-card__media-wrap');
        const img = card.querySelector('.p-card__img');
        const overlap = (a, b) => {
            if (!a || !b) return false;
            const m = 2;
            return !(a.right + m <= b.left || b.right + m <= a.left || a.bottom + m <= b.top || b.bottom + m <= a.top);
        };
        const pr = r(prices);
        const wr = r(wishlist);
        const cr = r(compare);
        const car = r(cart);
        const qr = r(qty);
        const dr = r(details);
        const cardRect = card.getBoundingClientRect();
        const specTops = Array.from(specItems).map(el => Math.round(el.getBoundingClientRect().top));
        const specRows = new Set(specTops).size;
        const imgCs = img ? getComputedStyle(img) : null;
        return {
            card_height: Math.round(cardRect.height),
            media_width: media ? Math.round(media.getBoundingClientRect().width) : null,
            img_width: img ? Math.round(img.getBoundingClientRect().width) : null,
            img_height: img ? Math.round(img.getBoundingClientRect().height) : null,
            img_object_fit: imgCs ? imgCs.objectFit : null,
            specs_visible: cs && cs.display !== 'none',
            specs_bg: cs ? cs.backgroundColor : null,
            specs_border_width: cs ? cs.borderWidth : null,
            spec_icon_count: specIcons.length,
            spec_row_count: specRows,
            icon_classes: iconClasses,
            price_visible: prices ? getComputedStyle(prices).display !== 'none' && pr && pr.height > 0 : false,
            price_over_wishlist: overlap(pr, wr),
            price_over_compare: overlap(pr, cr),
            qty_over_cart: overlap(qr, car),
            cart_over_details: overlap(car, dr),
            wishlist_visible: !!wishlist && wr && wr.height > 0,
            compare_visible: !!compare && cr && cr.height > 0,
            cart_visible: !!cart && car && car.height > 0,
            qty_visible: !!qty && qr && qr.height > 0,
            details_visible: !!details && dr && dr.height > 0,
            horizontal_overflow: document.documentElement.scrollWidth > window.innerWidth + 2,
        };
    }"""
    )


async def measure_category(page, mode):
    base = await page.evaluate(
        """(mode) => {
        const section = document.querySelector('.page--category section.category');
        const grid = document.querySelector('.category__grid');
        const card = document.querySelector('.p-card');
        const specs = card ? card.querySelector('.p-card__primary-specs') : null;
        const specsDisplay = specs ? getComputedStyle(specs).display : null;
        const media = card ? card.querySelector('.p-card__media-wrap') : null;
        return {
            mode,
            list_class: section ? section.classList.contains('category--view-list') : false,
            card_count: grid ? grid.querySelectorAll('.p-card').length : 0,
            media_width: media ? Math.round(media.getBoundingClientRect().width) : null,
            specs_visible: specsDisplay !== 'none',
            spec_count: specs ? specs.querySelectorAll('.p-card__primary-spec').length : 0,
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
    if mode == "list":
        detail = await measure_list_card(page)
        base.update(detail)
        width = int(base.get("viewport", "1920x1080").split("x")[0]) if "viewport" in base else 1920
        specs_single_row = base.get("spec_row_count", 99) == 1
        base["pass"] = (
            base.get("specs_visible")
            and base.get("spec_icon_count", 0) >= 4
            and specs_single_row
            and not base.get("price_over_wishlist")
            and not base.get("price_over_compare")
            and not base.get("qty_over_cart")
            and not base.get("cart_over_details")
            and (base.get("media_width") or 0) >= 150
            and (base.get("media_width") or 0) <= 165
            and base.get("price_visible")
            and base.get("cart_visible")
            and base.get("has_qty")
            and base.get("details_visible")
            and base.get("wishlist_visible")
            and base.get("compare_visible")
            and base.get("img_object_fit") == "contain"
            and not base.get("horizontal_overflow")
        )
    else:
        base["pass"] = not base["specs_visible"] and not base.get("horizontal_overflow")
    return base


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
    print("saved", path, "pass=", metrics.get("pass"), "card_h=", metrics.get("card_height"))
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
        return { context: label, card_count: cards.length, visible_specs_blocks: visibleSpecs, pass: visibleSpecs === 0 };
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
        m["pass"] = m["view_hidden"] and not m["specs_visible"]
        results.append(m)
    return results


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    results = {
        "pass": "CATEGORY-V2.2-LIST-CARD-COMPACTNESS",
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

    results["summary"] = {
        "grid_pass": all(m.get("pass") for m in results["desktop_grid"]),
        "list_pass": all(m.get("pass") for m in results["desktop_list"]),
        "mobile_pass": all(m.get("pass") for m in results["mobile_grid"]),
        "shared_pass": all(v.get("pass") for v in results["shared_contexts"].values()),
        "pdp_pass": results["pdp"]["pass"] if results["pdp"] else False,
    }

    with open(QA_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("QA JSON", QA_JSON)
    print("Summary", results["summary"])


if __name__ == "__main__":
    asyncio.run(main())
