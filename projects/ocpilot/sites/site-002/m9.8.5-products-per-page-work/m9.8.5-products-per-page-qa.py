#!/usr/bin/env python3
"""M9.8.5 products per page selector — live QA checks."""
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime

BASE = "https://zpm.new-site.space"
CATEGORY_URL = BASE + "/index.php?route=product/category&path=301"
OUT = r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m9.8.5-products-per-page"
LIMITS = [15, 25, 50, 100]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-QA-M985"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", "replace"), resp.geturl()


def count_product_cards(html):
    articles = len(re.findall(r'<article\s+class="p-card"', html))
    if articles:
        return articles
    return len(re.findall(r'<article[^>]*class="[^"]*\bp-card\b', html))


def main():
    result = {
        "task": "m9.8.5-products-per-page",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "base": BASE,
        "category_url": CATEGORY_URL,
        "audit": {},
        "asset_checks": {},
        "limit_checks": {},
        "qa": {},
    }

    main_js = fetch(BASE + "/assets/js/main.js")[0]
    style_css = fetch(BASE + "/assets/css/style.css")[0]
    cat_html, cat_final_url = fetch(CATEGORY_URL)

    result["asset_checks"] = {
        "main_js_has_limit_block": "category__limit" in main_js
        and "data-limit-open" in main_js,
        "css_has_limit_grouped_with_sort": ".category__limit" in style_css,
        "category_page_has_limit_ui": "category__limit" in cat_html
        and "data-limit-open" in cat_html
        and "Показывать:" in cat_html,
        "category_page_has_sort_ui": "category__sort" in cat_html,
        "category_page_has_view_switcher": "data-category-view" in cat_html,
    }

    default_cards = count_product_cards(cat_html)
    result["limit_checks"]["default"] = {
        "url": cat_final_url,
        "product_card_count": default_cards,
        "limit_in_url": "limit=" in cat_final_url,
    }

    for limit in LIMITS:
        url = CATEGORY_URL + "&limit=" + str(limit)
        html, final_url = fetch(url)
        cards = count_product_cards(html)
        limit_links = len(re.findall(rf'href="[^"]*limit={limit}[^"]*"', html))
        pagination_pages = re.findall(r'class="[^"]*pagination[^"]*"', html, re.I)
        has_active = (
            f'is-active">{limit}</a>' in html
            or f'is-active">{limit}<' in html
            or f">{limit}</span>" in html
        )
        result["limit_checks"][str(limit)] = {
            "url": final_url,
            "limit_param_present": f"limit={limit}" in final_url,
            "product_card_count": cards,
            "cards_match_limit": cards == limit or (cards < limit and cards > 0),
            "limit_option_links": limit_links,
            "pagination_present": bool(pagination_pages),
            "active_marker_in_html": has_active,
        }

    sort_url = CATEGORY_URL + "&limit=25&sort=p.price&order=ASC"
    sort_html, sort_final = fetch(sort_url)
    result["limit_checks"]["sort_preserved"] = {
        "url": sort_final,
        "has_sort": "sort=p.price" in sort_final,
        "has_order": "order=ASC" in sort_final,
        "has_limit": "limit=25" in sort_final,
        "has_limit_ui": "category__limit" in sort_html,
    }

    ac = result["asset_checks"]
    lc = result["limit_checks"]
    all_limits_ok = all(
        lc[str(n)].get("limit_param_present")
        and lc[str(n)].get("cards_match_limit")
        and lc[str(n)].get("limit_option_links", 0) >= 1
        for n in LIMITS
    )

    result["qa"] = {
        "limit_ui_deployed": ac["category_page_has_limit_ui"],
        "js_limit_toggle": ac["main_js_has_limit_block"],
        "css_limit_styles": ac["css_has_limit_grouped_with_sort"],
        "limits_15_25_50_100": all_limits_ok,
        "sort_still_present": ac["category_page_has_sort_ui"],
        "view_switcher_still_present": ac["category_page_has_view_switcher"],
        "sort_with_limit": result["limit_checks"]["sort_preserved"]["has_sort"]
        and result["limit_checks"]["sort_preserved"]["has_limit"],
        "grid_list_mobile": "MANUAL — verify grid/list toggle and mobile topbar on TEST",
    }

    import os

    os.makedirs(OUT, exist_ok=True)
    out_path = os.path.join(OUT, "m9.8.5-products-per-page-qa-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result["qa"], ensure_ascii=False, indent=2))
    print("Written:", out_path)


if __name__ == "__main__":
    main()
