#!/usr/bin/env python3
import urllib.request, re

URLS = [
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850",
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850",
]

for url in URLS:
    html = urllib.request.urlopen(url, timeout=60).read().decode("utf-8")
    checks = {
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "cart_btn": "data-cart-add" in html,
        "wishlist": bool(re.search(r"wishlist|data-wishlist|zpm_ico__heart", html, re.I)),
        "compare": bool(re.search(r"compare|data-compare|zpm_ico__compare", html, re.I)),
        "hero_props": "product-hero__props" in html,
        "spec_tab": 'id="tab-spec"' in html,
    }
    print(url.split("/")[-1], checks)
