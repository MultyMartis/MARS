#!/usr/bin/env python3
"""Interactive QA smoke for W1A.2 hero controls."""
import asyncio
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    import subprocess

    subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    from playwright.async_api import async_playwright

URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-serii-premium/stoly-premium-600/"
    "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
)


async def main():
    results = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1440, "height": 900},
            extra_http_headers={"Cookie": "beget=begetok"},
        )
        await page.goto(URL, wait_until="networkidle", timeout=90000)
        await page.wait_for_selector(".product-hero__layout", timeout=30000)

        brand = await page.locator(".product-hero__brand img").is_visible()
        results["assum_brand_visible"] = brand

        subtitle_count = await page.locator(".product-hero__subtitle").count()
        results["placeholder_subtitle_hidden"] = subtitle_count == 0

        buybox = page.locator(".product-hero__buybox")
        title = page.locator(".product-hero__title")
        buy_y = (await buybox.bounding_box())["y"]
        title_y = (await title.bounding_box())["y"]
        results["buybox_near_title"] = abs(buy_y - title_y) < 320

        media = page.locator(".product-hero__media")
        buy_x = (await buybox.bounding_box())["x"]
        media_x = (await media.bounding_box())["x"]
        media_w = (await media.bounding_box())["width"]
        results["buybox_not_under_image"] = buy_x >= media_x + media_w - 40

        gallery_main = await page.locator(".js-product-gallery .swiper-slide").count()
        results["gallery_slides"] = gallery_main > 0

        thumbs = await page.locator(".js-product-thumbs .swiper-slide").count()
        results["gallery_thumbs"] = thumbs > 0

        fav = page.locator("[data-fav-toggle]").first
        fav_class = await fav.get_attribute("class") or ""
        results["fav_round_btn"] = "btn-no-text" in fav_class
        await fav.click()
        await page.wait_for_timeout(800)
        fav_after = await fav.get_attribute("class") or ""
        results["fav_toggle_feedback"] = "active" in fav_after or await fav.locator(".zpm-tip__popup").is_visible()

        cmp_btn = page.locator("[data-compare-toggle]").first
        cmp_class = await cmp_btn.get_attribute("class") or ""
        results["compare_round_btn"] = "btn-no-text" in cmp_class
        await cmp_btn.click()
        await page.wait_for_timeout(800)
        cmp_after = await cmp_btn.get_attribute("class") or ""
        results["compare_toggle_feedback"] = "active" in cmp_after or await cmp_btn.locator(".zpm-tip__popup").is_visible()

        add_btn = page.locator("[data-cart-add]").first
        qty_val = page.locator("[data-qty-value]").first
        before = await qty_val.inner_text()
        await add_btn.click()
        await page.wait_for_timeout(1500)
        after = await qty_val.inner_text()
        results["add_to_cart_works"] = after != before or int(after or "0") >= 1

        plus = page.locator("[data-qty-plus]").first
        await plus.click()
        await page.wait_for_timeout(800)
        after_plus = await qty_val.inner_text()
        results["qty_stepper_works"] = int(after_plus or "0") > int(after or "0")

        fancybox_link = page.locator('[data-fancybox="product"]').first
        await fancybox_link.click()
        await page.wait_for_timeout(1200)
        fancy_visible = await page.locator(".fancybox__container, .fancybox-container").count()
        results["fancybox_opens"] = fancy_visible > 0

        await browser.close()

    print("QA RESULTS")
    for key, val in results.items():
        print(f"  {key}: {'OK' if val else 'FAIL'}")

    fails = [k for k, v in results.items() if not v]
    print("FAILS:", fails or "none")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
