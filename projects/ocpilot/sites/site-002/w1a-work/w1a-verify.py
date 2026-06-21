#!/usr/bin/env python3
"""Verify W1A deploy on live PDP."""
import re
import urllib.request

URLS = [
    (
        "stol-sp-p-18-6",
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
        "stoly-serii-premium/stoly-premium-600/"
        "stol-proizvodstvennyy-sp-p-18-6-1800h600h850",
    ),
    (
        "vmtc-p3-2-500",
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"
        "vanny-serii-premium-3/vanna-moechnaya-vmtc-p3-2-500",
    ),
]

checks = {
    "layout": "product-hero__layout",
    "buybox": "product-hero__buybox",
    "fit_grid": "product-hero__fit-grid",
    "context": "product-hero__context",
    "actions_row": "product-hero__actions-row",
    "no_brand": "product-hero__brand",
    "no_subtitle": "product-hero__subtitle",
    "data_copy": 'data-copy="',
    "cart_pdp": "data-cart-pdp",
    "fav_toggle": "data-fav-toggle",
    "compare_toggle": "data-compare-toggle",
}


def fetch(url):
    req = urllib.request.Request(
        url, headers={"User-Agent": "MARS-W1A-Verify/1.0", "Cookie": "beget=begetok"}
    )
    return urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")


for label, url in URLS:
    print("\n===", label, "===")
    try:
        html = fetch(url)
    except Exception as e:
        print("FETCH ERROR:", e)
        continue

    m = re.search(r'<section class="product-hero">.*?</section>', html, re.S)
    hero = m.group(0) if m else ""
    print("hero_len", len(hero))
    for name, token in checks.items():
        present = token in hero if name not in ("no_brand", "no_subtitle") else token not in hero
        print(f"  {name}: {'OK' if present else 'FAIL'}")

    props = re.findall(
        r'class="product-hero__fit-cell".*?<dt>([^<]+)</dt>\s*<dd>([^<]+)</dd>', hero, re.S
    )
    print("  fit_cells:", len(props))
    ctx = re.search(r'class="product-hero__context-link"[^>]*>([^<]+)', hero)
    print("  context:", ctx.group(1).strip() if ctx else "(hidden)")
