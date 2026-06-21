#!/usr/bin/env python3
"""Read-only probe — SITE-002 category audit V1."""
import json
import os
import re
import ssl
import urllib.request

BASE = "https://zpm.new-site.space"
URL = BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/"
OUT_DIR = r"C:\AI MARS\projects\ocpilot\sites\site-002\category-audit-v1-work"
OUT_HTML = os.path.join(OUT_DIR, "category-live.html")
OUT_JSON = os.path.join(OUT_DIR, "category-probe-result.json")


def fetch(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url,
        headers={"Cookie": "beget=begetok", "User-Agent": "MARS-Category-Audit-V1"},
    )
    return urllib.request.urlopen(req, context=ctx, timeout=90).read().decode(
        "utf-8", "replace"
    )


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    html = fetch(URL)
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    title = re.search(r"<title>([^<]+)", html)
    cards = re.findall(r'class="([^"]*product-card[^"]*)"', html)
    breadcrumbs = re.findall(r'class="([^"]*breadcrumb[^"]*)"', html, re.I)
    seo = re.search(r'category__seo|seo-text|category-description|zpm-seo', html, re.I)
    pagination = re.findall(r'class="([^"]*pagination[^"]*)"', html, re.I)
    filter_sidebar = "data-filter-sidebar" in html
    sort_btn = "category__sort" in html
    view_switch = re.findall(r'category__view|view-switch|grid-view|list-view', html, re.I)
    subcats = re.findall(r"zpm-sub-cat", html)
    grid = "category__grid" in html

    # extract first product card block
    card_match = re.search(
        r'(<(?:article|div)[^>]*class="[^"]*product-card[^"]*"[^>]*>.*?</(?:article|div)>)',
        html,
        re.S,
    )
    card_sample = card_match.group(1)[:2500] if card_match else None

    # DOM skeleton: major blocks in order
    blocks = []
    for pat, name in [
        (r'<nav[^>]*class="[^"]*breadcrumb', "breadcrumbs"),
        (r"<h1", "h1"),
        (r"zpm-sub-cat-chips|zpm-sub-cat-sections", "subcategories"),
        (r"category__layout", "category__layout"),
        (r"category__sidebar|filters__", "filter_sidebar"),
        (r"category__topbar", "topbar_sort"),
        (r"category__grid", "product_grid"),
        (r"pagination", "pagination"),
        (r"category__seo|seo-text|category-description", "seo_block"),
        (r"<footer", "footer"),
    ]:
        if re.search(pat, html, re.I):
            blocks.append(name)

    result = {
        "url": URL,
        "html_len": len(html),
        "title": title.group(1).strip() if title else None,
        "h1": strip_tags(h1.group(1)) if h1 else None,
        "product_card_count": len(cards),
        "product_card_classes_sample": cards[:3],
        "has_filter_sidebar_attr": filter_sidebar,
        "has_sort": sort_btn,
        "view_switch_markers": view_switch,
        "subcat_markers": len(subcats),
        "has_grid": grid,
        "pagination_classes": pagination[:3],
        "seo_marker": bool(seo),
        "breadcrumb_markers": len(breadcrumbs),
        "dom_blocks_found": blocks,
        "card_html_sample_len": len(card_sample) if card_sample else 0,
    }
    if card_sample:
        with open(os.path.join(OUT_DIR, "product-card-sample.html"), "w", encoding="utf-8") as f:
            f.write(card_sample)

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
