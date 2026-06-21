#!/usr/bin/env python3
"""QA — M9.8.9-01 wishlist/compare smart titles + tip dedup."""
import asyncio
import json
import sys
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("playwright not installed")
    sys.exit(1)

BASE = "https://zpm.new-site.space"
PLP_STOLY = BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/"
PLP_VANNY = BASE + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"
PDP_URL = BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m9.8.9-01-wishlist-compare-tooltips")
OUT_JSON = OUT_DIR / "m9.8.9-01-qa-result.json"

TITLE_FAV_ADD = "Добавить в избранное"
TITLE_FAV_REMOVE = "Удалить из избранного"
TITLE_COMPARE_ADD = "Добавить к сравнению"
TITLE_COMPARE_REMOVE = "Удалить из сравнения"


async def probe_actions(page):
    return await page.evaluate(
        """() => {
        const fav = document.querySelector('[data-fav-toggle]');
        const compare = document.querySelector('[data-compare-toggle]');
        const copy = document.querySelector('[data-copy]');
        return {
            fav_title: fav ? fav.getAttribute('title') : null,
            fav_active: fav ? fav.classList.contains('active') : null,
            compare_title: compare ? compare.getAttribute('title') : null,
            compare_active: compare ? compare.classList.contains('active') : null,
            copy_present: !!copy,
            main_js_has_titles: typeof window.__m98901 !== 'undefined'
        };
    }"""
    )


async def click_and_check(page, selector, expect_title_after, expect_active_after):
    btn = page.locator(selector).first
    await btn.click()
    await page.wait_for_timeout(400)
    state = await page.evaluate(
        """(sel) => {
        const el = document.querySelector(sel);
        if (!el) return null;
        const others = Array.from(document.querySelectorAll('[data-fav-toggle], [data-compare-toggle]'))
          .filter(n => n !== el)
          .map(n => ({ is_tip: n.classList.contains('is-tip'), is_remove: n.classList.contains('is-remove') }));
        return {
            title: el.getAttribute('title'),
            active: el.classList.contains('active'),
            is_tip: el.classList.contains('is-tip'),
            is_remove: el.classList.contains('is-remove'),
            others_with_tip: others.filter(o => o.is_tip).length
        };
    }""",
        selector,
    )
    ok_title = state and state["title"] == expect_title_after
    ok_active = state and state["active"] == expect_active_after
    return {
        "selector": selector,
        "state": state,
        "title_ok": ok_title,
        "active_ok": ok_active,
        "pass": bool(ok_title and ok_active),
    }


async def test_copy(page):
    result = await page.evaluate(
        """async () => {
        const copy = document.querySelector('[data-copy]');
        if (!copy) return { pass: false, reason: 'no copy button' };
        copy.click();
        await new Promise(r => setTimeout(r, 200));
        const body = copy.querySelector('.zpm-tip__body');
        return {
            pass: copy.classList.contains('is-tip') && body && body.textContent.includes('Артикул скопирован'),
            body_text: body ? body.textContent : null,
            is_tip: copy.classList.contains('is-tip')
        };
    }"""
    )
    return result


async def test_tip_dedup(page):
    return await page.evaluate(
        """async () => {
        const fav = document.querySelector('[data-fav-toggle]');
        const compare = document.querySelector('[data-compare-toggle]');
        if (!fav || !compare) return { pass: false, reason: 'buttons missing' };

        fav.click();
        await new Promise(r => setTimeout(r, 50));
        const favTip = fav.classList.contains('is-tip');
        const compareTipBefore = compare.classList.contains('is-tip');

        compare.click();
        await new Promise(r => setTimeout(r, 50));
        const favTipAfterCompare = fav.classList.contains('is-tip');
        const compareTipAfter = compare.classList.contains('is-tip');

        return {
            pass: favTip && compareTipAfter && !favTipAfterCompare,
            fav_tip_initial: favTip,
            compare_tip_before: compareTipBefore,
            fav_tip_after_compare_click: favTipAfterCompare,
            compare_tip_after: compareTipAfter
        };
    }"""
    )


async def run_page_suite(page, label, url):
    await page.goto(url, wait_until="domcontentloaded", timeout=120000)
    await page.wait_for_timeout(1500)

    initial = await probe_actions(page)

    fav_add = await click_and_check(
        page, "[data-fav-toggle]", TITLE_FAV_REMOVE, True
    )
    fav_remove = await click_and_check(
        page, "[data-fav-toggle]", TITLE_FAV_ADD, False
    )
    compare_add = await click_and_check(
        page, "[data-compare-toggle]", TITLE_COMPARE_REMOVE, True
    )
    compare_remove = await click_and_check(
        page, "[data-compare-toggle]", TITLE_COMPARE_ADD, False
    )

    dedup = await test_tip_dedup(page)
    copy = await test_copy(page)

    return {
        "label": label,
        "url": url,
        "initial": initial,
        "fav_add": fav_add,
        "fav_remove": fav_remove,
        "compare_add": compare_add,
        "compare_remove": compare_remove,
        "tip_dedup": dedup,
        "copy_article": copy,
        "pass": all(
            [
                initial.get("fav_title") in (TITLE_FAV_ADD, TITLE_FAV_REMOVE),
                initial.get("compare_title") in (TITLE_COMPARE_ADD, TITLE_COMPARE_REMOVE),
                fav_add["pass"],
                fav_remove["pass"],
                compare_add["pass"],
                compare_remove["pass"],
                dedup.get("pass"),
                copy.get("pass"),
            ]
        ),
    }


async def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = {"task": "M9.8.9-01", "pages": []}

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        for label, url in [
            ("PLP Столы", PLP_STOLY),
            ("PLP Моечные ванны", PLP_VANNY),
            ("PDP", PDP_URL),
        ]:
            try:
                suite = await run_page_suite(page, label, url)
            except Exception as exc:
                suite = {"label": label, "url": url, "pass": False, "error": str(exc)}
            results["pages"].append(suite)
            print(label, "PASS" if suite.get("pass") else "FAIL")

        await browser.close()

    results["pass"] = all(p.get("pass") for p in results["pages"])
    OUT_JSON.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"pass": results["pass"], "out": str(OUT_JSON)}, ensure_ascii=False))
    return 0 if results["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
