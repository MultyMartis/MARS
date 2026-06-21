#!/usr/bin/env python3
import re
import urllib.request

req = urllib.request.Request
html_cache = {}

SAMPLE = [
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850",
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850",
]


def probe(url):
    html = urllib.request.urlopen(
        req(url, headers={"Cookie": "beget=begetok"}),
        timeout=60,
    ).read().decode("utf-8", "replace")
    hero = re.search(r'<section class="product-hero">(.*?)</section>', html, re.S)
    h = hero.group(1) if hero else ""
    return {
        "slides": len(re.findall(r'data-fancybox="product"', h)),
        "thumbs": "js-product-thumbs" in h,
        "request": "Запросить цену" in h,
        "cart": "data-cart-add" in h,
    }


for url in SAMPLE:
    print(url.split("/")[-1], probe(url))
