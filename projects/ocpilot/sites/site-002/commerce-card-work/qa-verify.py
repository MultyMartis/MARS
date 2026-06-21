#!/usr/bin/env python3
import json
import re
import urllib.request

URL = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/"
    "stol-tumba-spkb-18-7-vl5-1800h700h850"
)
req = urllib.request.Request(URL, headers={"Cookie": "beget=begetok"})
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
hero = re.search(r'<section class="product-hero">(.*?)</section>', html, re.S)
hero_html = hero.group(1) if hero else ""
checks = {
    "php_ok": "Fatal error" not in html,
    "commerce_card": "product-hero__commerce-card" in hero_html,
    "service_card": "product-hero__service-card" in hero_html,
    "commerce_head": "Стоимость:" in hero_html,
    "price": "product-hero__price-value" in hero_html,
    "old_price": "product-hero__old-price-value" in hero_html,
    "discount": "product-hero__discount" in hero_html,
    "status": "product-hero__status" in hero_html,
    "cart": "data-cart-add" in hero_html,
    "qty": "data-cart-qty" in hero_html,
    "wishlist": "data-fav-toggle" in hero_html,
    "compare": "data-compare-toggle" in hero_html,
    "gallery": 'data-fancybox="product"' in hero_html,
    "quick_order": "Быстрый заказ" in hero_html,
    "callback_hook": '#zpmFbCallback' in hero_html,
    "question": "Задать вопрос" in hero_html,
    "question_hook": '#zpmFbQuestion' in hero_html,
    "service_items": hero_html.count("product-hero__service-item"),
    "fa_shield": "fa-shield-check" in hero_html,
    "fa_truck": "fa-truck" in hero_html,
    "fa_headset": "fa-headset" in hero_html,
}
out = r"C:\AI MARS\projects\ocpilot\sites\site-002\commerce-card-work\qa-verify.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(checks, f, ensure_ascii=False, indent=2)
