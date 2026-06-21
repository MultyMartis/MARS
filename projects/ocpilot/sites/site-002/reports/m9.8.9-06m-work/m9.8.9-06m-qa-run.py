#!/usr/bin/env python3
"""M9.8.9-06M — post-deploy QA: attr filter, only_with_price, price sort."""
from __future__ import annotations

import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE_URL = "https://zpm.new-site.space"

OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06m-work")
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
        "attr_label": "N/A (no attr sidebar — baseline only)",
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
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-M9.8.9-06M/1.0"})
    return urllib.request.urlopen(req, timeout=120, context=ctx).read().decode("utf-8", "replace")


def count_cards(html: str) -> int:
    return len(re.findall(r'class="[^"]*product-card[^"]*"', html))


def extract_prices(html: str) -> list[float]:
    """Parse visible price values from product cards (best-effort)."""
    prices: list[float] = []
    for m in re.finditer(
        r'class="[^"]*product-card[^"]*"[\s\S]*?(?=(class="[^"]*product-card|$))',
        html,
    ):
        block = m.group(0)
        for pm in re.finditer(r'[\d\s]+(?:[.,]\d+)?\s*(?:₽|руб)', block, re.I):
            raw = re.sub(r"[^\d.,]", "", pm.group(0).replace(",", "."))
            if raw:
                try:
                    prices.append(float(raw))
                except ValueError:
                    pass
        if not prices:
            for pm in re.finditer(r'data-price="([\d.]+)"', block):
                prices.append(float(pm.group(1)))
    return prices[:20]


def join_url(base: str, *parts: str) -> str:
    sep = "&" if "?" in base else "?"
    return base + sep + "&".join(p for p in parts if p)


def sort_monotonic(prices: list[float], order: str) -> bool | None:
    if len(prices) < 2:
        return None
    pairs = list(zip(prices, prices[1:]))
    if order == "ASC":
        return all(a <= b for a, b in pairs)
    return all(a >= b for a, b in pairs)


def main() -> None:
    results: dict = {
        "task": "M9.8.9-06M",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "categories": [],
        "all_pass": True,
    }

    for cat in CATEGORIES:
        entry = {
            "id": cat["id"],
            "name": cat["name"],
            "category_id": cat["category_id"],
            "checks": {},
        }

        # 1. Attribute filter (or baseline for telezhki)
        if cat["attr_filter"]:
            attr_url = join_url(cat["base"], cat["attr_filter"])
            attr_cards = count_cards(fetch_url(attr_url))
            entry["checks"]["attr_filter"] = {
                "filter": cat["attr_label"],
                "url": attr_url,
                "product_cards": attr_cards,
                "pass": attr_cards > 0,
            }
        else:
            base_cards = count_cards(fetch_url(cat["base"]))
            entry["checks"]["attr_filter"] = {
                "filter": cat["attr_label"],
                "url": cat["base"],
                "product_cards": base_cards,
                "pass": base_cards > 0,
                "note": "baseline — no attribute sidebar on category",
            }

        # 2. only_with_price
        owp_url = join_url(cat["base"], "filters=only_with_price=1")
        owp_cards = count_cards(fetch_url(owp_url))
        entry["checks"]["only_with_price"] = {
            "url": owp_url,
            "product_cards": owp_cards,
            "pass": owp_cards > 0,
        }

        # 3. Sort ASC
        asc_url = join_url(cat["base"], "sort=p.price&order=ASC")
        asc_html = fetch_url(asc_url)
        asc_cards = count_cards(asc_html)
        asc_prices = extract_prices(asc_html)
        asc_mono = sort_monotonic(asc_prices, "ASC")
        entry["checks"]["sort_price_asc"] = {
            "url": asc_url,
            "product_cards": asc_cards,
            "prices_sample": asc_prices[:8],
            "monotonic": asc_mono,
            "pass": asc_cards > 0 and (asc_mono is not False),
        }

        # 4. Sort DESC
        desc_url = join_url(cat["base"], "sort=p.price&order=DESC")
        desc_html = fetch_url(desc_url)
        desc_cards = count_cards(desc_html)
        desc_prices = extract_prices(desc_html)
        desc_mono = sort_monotonic(desc_prices, "DESC")
        entry["checks"]["sort_price_desc"] = {
            "url": desc_url,
            "product_cards": desc_cards,
            "prices_sample": desc_prices[:8],
            "monotonic": desc_mono,
            "pass": desc_cards > 0 and (desc_mono is not False),
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
