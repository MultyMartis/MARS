#!/usr/bin/env python3
"""Verify W1A.2 deploy on live PDP."""
import re
import urllib.request

URLS = [
    (
        "stol-sp-p-18-6",
        "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
        "stoly-serii-premium/stoly-premium-600/"
        "stol-proizvodstvennyy-sp-p-18-6-1800h600h850",
    ),
]

checks_present = {
    "layout": "product-hero__layout",
    "buybox": "product-hero__buybox",
    "fit_grid": "product-hero__fit-grid",
    "context": "product-hero__context",
    "brand": "product-hero__brand",
    "data_copy_model": 'data-copy="',
    "cart_pdp": "data-cart-pdp",
    "fav_toggle": "data-fav-toggle",
    "compare_toggle": "data-compare-toggle",
    "btn_no_text_fav": 'class="btn-no-text zpm-tip',
    "fancybox": 'data-fancybox="product"',
}

checks_absent = {
    "no_dealer": "Купить как дилер",
    "no_action_btn": "product-hero__action-btn",
    "no_b2b_preview": "product-hero__b2b-preview",
    "no_old_grid": "product-hero__grid",
    "placeholder_subtitle": "это надо сделать дополнительным мини-описанием товара",
}


def fetch(url):
    req = urllib.request.Request(
        url, headers={"User-Agent": "MARS-W1A2-Verify/1.0", "Cookie": "beget=begetok"}
    )
    return urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")


results = {}

for label, url in URLS:
    print("\n===", label, "===")
    row = {}
    try:
        html = fetch(url)
    except Exception as e:
        print("FETCH ERROR:", e)
        results[label] = {"error": str(e)}
        continue

    m = re.search(r'<section class="product-hero">.*?</section>', html, re.S)
    hero = m.group(0) if m else ""
    print("hero_len", len(hero))

    for name, token in checks_present.items():
        ok = token in hero
        row[name] = ok
        print(f"  {name}: {'OK' if ok else 'FAIL'}")

    for name, token in checks_absent.items():
        ok = token not in hero
        row[name] = ok
        print(f"  {name}: {'OK' if ok else 'FAIL'}")

    props = re.findall(
        r'class="product-hero__fit-cell".*?<dt>([^<]+)</dt>\s*<dd>([^<]+)</dd>', hero, re.S
    )
    row["fit_cells"] = len(props)
    print("  fit_cells:", len(props))

    ctx = re.search(r'class="product-hero__context-link"[^>]*>([^<]+)', hero)
    ctx_text = ctx.group(1).strip() if ctx else "(hidden)"
    row["context_text"] = ctx_text
    print("  context:", ctx_text)

    buy_idx = hero.find("product-hero__buybox")
    media_idx = hero.find("product-hero__media")
    row["buybox_after_media"] = buy_idx > media_idx
    print("  buybox_after_media:", row["buybox_after_media"])

    results[label] = row

print("\n=== SUMMARY ===")
for label, row in results.items():
    if "error" in row:
        print(label, "ERROR", row["error"])
        continue
    fails = [k for k, v in row.items() if isinstance(v, bool) and not v]
    print(label, "FAILS:", fails or "none")
