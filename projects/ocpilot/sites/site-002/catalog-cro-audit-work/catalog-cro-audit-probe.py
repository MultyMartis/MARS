#!/usr/bin/env python3
"""BZPM catalog CRO/UX/SEO audit probe — read-only live fetch."""
import json
import re
import ssl
import urllib.request
from pathlib import Path

BASE = "https://zpm.new-site.space"
OUT = Path(__file__).resolve().parent / "audit-probe-result.json"

URLS = {
    "home": "/",
    "katalog": "/katalog",
    "neutral_hub": "/katalog/nejtralnoe-oborudovanie",
    "stoly": "/katalog/nejtralnoe-oborudovanie/stoly/",
    "vanny": "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
    "podtovarniki": "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
    "zonty": "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/",
    "telezhki": "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/",
    "table_pdp": "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
    "sink_pdp": "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850",
}


def fetch(path: str) -> str:
    req = urllib.request.Request(path, headers={"User-Agent": "BZPM-CRO-Audit/1.0"})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
        return resp.read().decode("utf-8", "replace")


def meta(html: str, name: str) -> str | None:
    m = re.search(rf'<meta[^>]+name="{re.escape(name)}"[^>]+content="([^"]*)"', html, re.I)
    if not m:
        m = re.search(rf'<meta[^>]+content="([^"]*)"[^>]+name="{re.escape(name)}"', html, re.I)
    return m.group(1) if m else None


def og(html: str, prop: str) -> str | None:
    m = re.search(rf'<meta[^>]+property="{re.escape(prop)}"[^>]+content="([^"]*)"', html, re.I)
    return m.group(1) if m else None


def title(html: str) -> str | None:
    m = re.search(r"<title>([^<]+)</title>", html, re.I)
    return m.group(1).strip() if m else None


def h1(html: str) -> str | None:
    m = re.search(r"<h1[^>]*>([^<]+)</h1>", html, re.I)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else None


def breadcrumbs(html: str) -> list:
    items = re.findall(r'class="[^"]*breadcrumb[^"]*"[^>]*>.*?<a[^>]+>([^<]+)</a>', html, re.S | re.I)
    if not items:
        items = re.findall(r'class="breadcrumb[^"]*"[^>]*>(.*?)</', html, re.S | re.I)
    return [re.sub(r"\s+", " ", x).strip() for x in items if x.strip()][:10]


def count_products(html: str) -> int | None:
    m = re.search(r"(\d+)\s*(?:товар|sku|позиц)", html, re.I)
    if m:
        return int(m.group(1))
    cards = len(re.findall(r'class="p-card"', html))
    return cards if cards else None


def has_cta(html: str, markers: list) -> dict:
    return {m: m.lower() in html.lower() for m in markers}


def pdp_signals(html: str) -> dict:
    return {
        "has_price": bool(re.search(r'class="[^"]*price[^"]*"', html, re.I)),
        "has_cart": "data-cart-add" in html,
        "has_fav": "data-fav-toggle" in html,
        "has_compare": "data-compare-toggle" in html,
        "has_docs": "docs-list" in html or "документ" in html.lower(),
        "has_specs": "product-specs" in html or "характеристик" in html.lower(),
        "has_gallery": "data-fancybox" in html or "product-gallery" in html,
        "has_phone": bool(re.search(r"tel:|\+7|8\s*\(\d{3}\)", html)),
        "has_whatsapp": "whatsapp" in html.lower() or "wa.me" in html.lower(),
        "has_callback": "обратн" in html.lower() or "заявк" in html.lower(),
        "has_delivery": "доставк" in html.lower(),
        "has_warranty": "гарант" in html.lower(),
        "has_brand": "assum" in html.lower() or "бренд" in html.lower(),
        "related_count": len(re.findall(r'relproducts|related|похож', html, re.I)),
    }


def plp_signals(html: str) -> dict:
    return {
        "has_filter": "data-filter-sidebar" in html,
        "has_sort": "sort" in html.lower() or "сортир" in html.lower(),
        "has_view_switch": "category--view" in html or "view-switch" in html,
        "has_pagination": "pagination" in html.lower() or "page-link" in html,
        "has_empty_state": "нет товар" in html.lower() or "ничего не найден" in html.lower(),
        "product_cards": len(re.findall(r'class="p-card"', html)),
        "has_category_desc": bool(re.search(r'category-desc|category__intro|category-description', html, re.I)),
        "has_hub_cards": "zpm-cat-card" in html,
        "has_breadcrumb": "breadcrumb" in html.lower(),
    }


def home_signals(html: str) -> dict:
    cards = len(re.findall(r'zpm-cat-sections.*?zpm-cat-card', html, re.S))
    return {
        "category_cards": cards,
        "has_hero": bool(re.search(r"hero|zpm-hero|main-banner", html, re.I)),
        "has_about": "о компани" in html.lower() or "о нас" in html.lower(),
        "has_contacts_block": "контакт" in html.lower(),
        "has_reviews": "отзыв" in html.lower(),
        "has_certificates": "сертификат" in html.lower(),
        "has_lead_form": "<form" in html and ("email" in html.lower() or "телефон" in html.lower()),
    }


def analyze(name: str, html: str) -> dict:
    base = {
        "title": title(html),
        "h1": h1(html),
        "meta_description": meta(html, "description"),
        "meta_robots": meta(html, "robots"),
        "og_title": og(html, "og:title"),
        "og_description": og(html, "og:description"),
        "canonical": None,
    }
    can = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', html, re.I)
    if can:
        base["canonical"] = can.group(1)
    if name == "home":
        base["signals"] = home_signals(html)
    elif "pdp" in name:
        base["signals"] = pdp_signals(html)
    else:
        base["signals"] = plp_signals(html)
        base["product_count_hint"] = count_products(html)
    base["cta"] = has_cta(
        html,
        [
            "Заказать звонок",
            "Получить КП",
            "Запросить цену",
            "Купить",
            "В корзину",
            "Связаться",
            "WhatsApp",
        ],
    )
    return base


def main():
    result = {"base_url": BASE, "pages": {}}
    for name, path in URLS.items():
        url = BASE + path
        print("fetch", url)
        html = fetch(url)
        result["pages"][name] = {"url": url, "analysis": analyze(name, html), "html_length": len(html)}
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print("saved", OUT)


if __name__ == "__main__":
    main()
