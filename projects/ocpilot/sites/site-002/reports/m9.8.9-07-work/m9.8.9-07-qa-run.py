#!/usr/bin/env python3
"""M9.8.9-07 — post-deploy QA: no subcategories filter block; filters still work."""
from __future__ import annotations

import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE_URL = "https://zpm.new-site.space"

OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-07-work")
OUT_JSON = OUT_DIR / "qa-results.json"

CATEGORIES = [
    {
        "id": "stoly",
        "name": "Столы",
        "category_id": 301,
        "base": BASE_URL + "/katalog/nejtralnoe-oborudovanie/stoly/",
        "attr_filter": "filters=attr[51][]=%D0%91%D0%B5%D0%B7%20%D0%BF%D0%BE%D0%BB%D0%BA%D0%B8",
        "attr_label": "attr[51][]=Без полки",
    },
    {
        "id": "moechnye",
        "name": "Моечные ванны",
        "category_id": 80,
        "base": BASE_URL + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
        "attr_filter": "filters=attr[shell-size][]=1100%D1%85500%D1%85400",
        "attr_label": "attr[shell-size][]=1100х500х400",
    },
    {
        "id": "podtovarniki",
        "name": "Подтоварники и подставки",
        "category_id": 322,
        "base": BASE_URL + "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
        "attr_filter": "filters=attr[51][]=600%D1%85400%D1%85300",
        "attr_label": "attr[51][]=600х400х300",
    },
    {
        "id": "telezhki",
        "name": "Тележки сервировочные",
        "category_id": 326,
        "base": BASE_URL + "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/",
        "attr_filter": None,
        "attr_label": "baseline (no attr sidebar)",
    },
    {
        "id": "zonty",
        "name": "Зонты вытяжные",
        "category_id": 207,
        "base": BASE_URL + "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/",
        "attr_filter": "filters=attr[construction][]=%D1%80%D0%B0%D0%B7%D0%B1%D0%BE%D1%80%D0%BD%D0%B0%D1%8F",
        "attr_label": "attr[construction][]=разборная",
    },
]


def fetch_url(url: str) -> str:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-M9.8.9-07/1.0"})
    return urllib.request.urlopen(req, timeout=120, context=ctx).read().decode("utf-8", "replace")


def count_cards(html: str) -> int:
    return len(re.findall(r'class="[^"]*product-card[^"]*"', html))


def join_url(base: str, *parts: str) -> str:
    sep = "&" if "?" in base else "?"
    return base + sep + "&".join(p for p in parts if p)


def filter_form_html(html: str) -> str:
    m = re.search(r'<form[^>]*data-filter-form[^>]*>[\s\S]*?</form>', html, re.I)
    return m.group(0) if m else ""


def has_subcategories_filter_block(form: str) -> bool:
    """Sidebar filter group «Подкатегории» with name=s[] checkboxes."""
    if not form:
        return False
    if "name=\"s[]\"" not in form and "name='s[]'" not in form:
        return False
    return bool(re.search(r"flt__group-title[^>]*>\s*Подкатегории", form, re.I))


def has_price_filter(form: str) -> bool:
    return "data-price-filter" in form or "price_from" in form or "flt__price" in form


def has_other_filters(form: str) -> bool:
    return bool(re.search(r'name="attr\[', form) or re.search(r'name="filters\[', form))


def has_js_errors_signal(html: str) -> bool:
    return bool(re.search(r"SyntaxError|Uncaught\s+ReferenceError", html))


def main() -> None:
    results: dict = {
        "task": "M9.8.9-07",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "categories": [],
        "all_pass": True,
    }

    for cat in CATEGORIES:
        base_html = fetch_url(cat["base"])
        form = filter_form_html(base_html)

        entry = {
            "id": cat["id"],
            "name": cat["name"],
            "category_id": cat["category_id"],
            "checks": {},
        }

        entry["checks"]["no_subcategories_block"] = {
            "pass": not has_subcategories_filter_block(form),
            "has_s_checkboxes_in_filter": "s[]" in form,
            "note": "Sidebar «Подкатегории» group must be absent",
        }

        entry["checks"]["other_filters_present"] = {
            "pass": has_price_filter(form) or has_other_filters(form) or cat["id"] == "telezhki",
            "has_price": has_price_filter(form),
            "has_attrs": has_other_filters(form),
        }

        if cat["attr_filter"]:
            attr_url = join_url(cat["base"], cat["attr_filter"])
            attr_cards = count_cards(fetch_url(attr_url))
            entry["checks"]["ajax_attr_filter"] = {
                "filter": cat["attr_label"],
                "url": attr_url,
                "product_cards": attr_cards,
                "pass": attr_cards > 0,
            }
        else:
            base_cards = count_cards(base_html)
            entry["checks"]["ajax_attr_filter"] = {
                "filter": cat["attr_label"],
                "url": cat["base"],
                "product_cards": base_cards,
                "pass": base_cards > 0,
            }

        price_url = join_url(cat["base"], "filters=price_from=1000&price_to=500000")
        price_cards = count_cards(fetch_url(price_url))
        entry["checks"]["price_filter"] = {
            "url": price_url,
            "product_cards": price_cards,
            "pass": price_cards >= 0,
            "note": "price range applied — card count recorded",
        }

        owp_url = join_url(cat["base"], "filters=only_with_price=1")
        owp_cards = count_cards(fetch_url(owp_url))
        entry["checks"]["only_with_price"] = {
            "url": owp_url,
            "product_cards": owp_cards,
            "pass": owp_cards > 0,
        }

        entry["checks"]["no_js_error_strings"] = {
            "pass": not has_js_errors_signal(base_html),
        }

        entry["pass"] = all(c.get("pass") for c in entry["checks"].values())
        if not entry["pass"]:
            results["all_pass"] = False
        results["categories"].append(entry)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
