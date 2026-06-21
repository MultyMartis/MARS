#!/usr/bin/env python3
"""Read-only screenshots — SITE-002 category audit V1."""
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
URL = BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/"
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\category-audit-v1"
QA_JSON = os.path.join(OUT_DIR, "category-audit-qa-result.json")

DESKTOP = [(1920, 1080), (1440, 900), (1366, 768), (1280, 800), (1024, 768)]
MOBILE = [(768, 1024), (576, 900), (390, 844), (375, 812), (360, 800)]


async def measure_grid(page):
    return await page.evaluate(
        """() => {
        const grid = document.querySelector('.category__grid');
        if (!grid) return null;
        const cards = grid.querySelectorAll('.product-card, .p-card, [class*="product-card"]');
        const style = getComputedStyle(grid);
        const cols = style.gridTemplateColumns.split(' ').filter(Boolean).length;
        const rect = grid.getBoundingClientRect();
        const cardRects = [...cards].slice(0, 6).map(c => {
            const r = c.getBoundingClientRect();
            return { w: Math.round(r.width), h: Math.round(r.height) };
        });
        const docW = document.documentElement.scrollWidth;
        const viewW = window.innerWidth;
        return {
            card_count: cards.length,
            grid_cols_computed: cols,
            grid_width: Math.round(rect.width),
            card_sizes: cardRects,
            horizontal_overflow: docW > viewW + 2,
            scroll_width: docW,
            viewport_width: viewW,
        };
    }"""
    )


async def measure_card(page):
    return await page.evaluate(
        """() => {
        const card = document.querySelector('.product-card, .p-card');
        if (!card) return null;
        const q = (sel) => {
            const el = card.querySelector(sel);
            if (!el) return false;
            const r = el.getBoundingClientRect();
            return { present: true, text: (el.innerText || '').trim().slice(0, 80), h: Math.round(r.height), w: Math.round(r.width) };
        };
        return {
            classes: card.className,
            height: Math.round(card.getBoundingClientRect().height),
            width: Math.round(card.getBoundingClientRect().width),
            img: !!card.querySelector('img'),
            title: q('.p-card__title, .product-card__title, a[href*="katalog"]'),
            sku: q('.p-card__sku, .product-card__sku, [class*="sku"]'),
            status: q('.p-card__status, .product-card__status, [class*="status"]'),
            price: q('.p-card__price, .product-card__price, [class*="price"]'),
            old_price: q('.p-card__priceold, .priceold, [class*="priceold"]'),
            cart: q('[data-cart-add], .p-card__buy'),
            wishlist: q('[data-wishlist], .wishlist, [class*="wishlist"]'),
            compare: q('[data-compare], .compare, [class*="compare"]'),
        };
    }"""
    )


async def shot(page, width, height, label):
    await page.set_viewport_size({"width": width, "height": height})
    await page.goto(URL, wait_until="networkidle", timeout=120000)
    await page.wait_for_selector(".category__grid, .category__layout", timeout=45000)
    path = os.path.join(OUT_DIR, f"category-{label}-{width}.png")
    await page.screenshot(path=path, full_page=True)
    grid = await measure_grid(page)
    card = await measure_card(page)
    overflow = await page.evaluate(
        "() => document.documentElement.scrollWidth > window.innerWidth + 2"
    )
    filter_btn = await page.locator(".category__filters-btn").count()
    sidebar_visible = await page.evaluate(
        """() => {
        const sb = document.querySelector('.category__sidebar');
        if (!sb) return null;
        const s = getComputedStyle(sb);
        return s.display !== 'none' && sb.getBoundingClientRect().width > 20;
    }"""
    )
    print("saved", path)
    return {
        "viewport": f"{width}x{height}",
        "label": label,
        "screenshot": path,
        "grid": grid,
        "card": card,
        "horizontal_overflow": overflow,
        "filter_btn_visible": filter_btn > 0,
        "sidebar_visible": sidebar_visible,
    }


async def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    results = {"url": URL, "desktop": [], "mobile": []}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(extra_http_headers={"Cookie": "beget=begetok"})
        for w, h in DESKTOP:
            results["desktop"].append(await shot(page, w, h, "desktop"))
        for w, h in MOBILE:
            results["mobile"].append(await shot(page, w, h, "mobile"))
        await browser.close()
    with open(QA_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("QA JSON", QA_JSON)


if __name__ == "__main__":
    asyncio.run(main())
