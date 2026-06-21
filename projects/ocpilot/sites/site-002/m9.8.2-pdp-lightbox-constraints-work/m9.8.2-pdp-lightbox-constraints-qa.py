#!/usr/bin/env python3
"""M9.8.2 PDP lightbox constraints — live QA checks."""
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime

BASE = "https://zpm.new-site.space"
SKU = "СПКБ-18/7-ВЛ5"
OUT = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m9.8.2-pdp-lightbox-constraints"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-QA-M982"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", "replace")


def main():
    result = {
        "task": "m9.8.2-pdp-lightbox-constraints",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "base": BASE,
        "sku": SKU,
        "asset_checks": {},
        "pdp": {},
        "qa": {},
    }

    main_js = fetch(BASE + "/assets/js/main.js")
    style_css = fetch(BASE + "/assets/css/style.css")

    result["asset_checks"] = {
        "main_js_has_applyProductFancyboxClasses_fn": "function applyProductFancyboxClasses"
        in main_js,
        "main_js_calls_apply_in_init": "applyProductFancyboxClasses(fb)" in main_js,
        "css_desktop_80vw_80vh": bool(
            re.search(
                r"\.fancybox__container\.is-product-fancybox[\s\S]{0,800}max-width:\s*80vw[\s\S]{0,120}max-height:\s*80vh",
                style_css,
            )
        ),
        "css_mobile_95vw_90vh": bool(
            re.search(
                r"@media \(max-width: 1024px\)[\s\S]{0,1200}max-width:\s*95vw[\s\S]{0,120}max-height:\s*90vh",
                style_css,
            )
        ),
        "css_object_fit_contain": "object-fit: contain" in style_css,
    }

    search_url = (
        BASE
        + "/index.php?route=product/search&search="
        + urllib.parse.quote(SKU)
    )
    search_html = fetch(search_url)
    product_links = []
    for href in re.findall(r'href="([^"]+)"', search_html):
        if "route=product/product" in href or "product_id=" in href:
            if href.startswith("/"):
                href = BASE + href
            elif not href.startswith("http"):
                href = BASE + "/" + href.lstrip("/")
            if href not in product_links:
                product_links.append(href)

    result["pdp"]["search_url"] = search_url
    result["pdp"]["product_links_found"] = len(product_links)
    result["pdp"]["product_links_sample"] = product_links[:5]

    if product_links:
        pdp_html = fetch(product_links[0])
        result["pdp"]["url"] = product_links[0]
        result["pdp"]["has_product_gallery"] = "product-gallery" in pdp_html
        result["pdp"]["has_data_fancybox_product"] = 'data-fancybox="product"' in pdp_html
        result["pdp"]["sku_in_page"] = SKU in pdp_html or "СПКБ" in pdp_html
    else:
        result["pdp"]["error"] = "No product link from search"

    ac = result["asset_checks"]
    result["qa"] = {
        "applyProductFancyboxClasses_connected": ac["main_js_calls_apply_in_init"],
        "desktop_constraints_in_css": ac["css_desktop_80vw_80vh"],
        "mobile_constraints_in_css": ac["css_mobile_95vw_90vh"],
        "contain_scaling": ac["css_object_fit_contain"],
        "pdp_gallery_present": result["pdp"].get("has_product_gallery", False),
        "fancybox_hooks_present": result["pdp"].get("has_data_fancybox_product", False),
        "visual_resize_verified": "MANUAL — open lightbox on TEST; automated visual not run",
        "overflow_verified": "MANUAL — open lightbox on TEST",
        "navigation_close_verified": "MANUAL — open lightbox on TEST",
    }

    import os

    os.makedirs(OUT, exist_ok=True)
    out_path = os.path.join(OUT, "m9.8.2-pdp-lightbox-constraints-qa-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("Saved:", out_path)


if __name__ == "__main__":
    main()
