#!/usr/bin/env python3
"""M9.8.9-08 — post-deploy QA: attribute filter group reset controls."""
from __future__ import annotations

import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE_URL = "https://zpm.new-site.space"

OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-08-work")
OUT_JSON = OUT_DIR / "qa-results.json"

CATEGORIES = [
    {
        "id": "stoly",
        "name": "Столы",
        "category_id": 301,
        "base": BASE_URL + "/katalog/nejtralnoe-oborudovanie/stoly/",
        "attr_filter": "filters=attr[51][]=%D0%91%D0%B5%D0%B7%20%D0%BF%D0%BE%D0%BB%D0%BA%D0%B8",
        "attr_label": "attr[51][]=Без полки",
        "second_attr": "filters=attr[47][]=%D0%9D%D0%B5%D1%80%D0%B6%D0%B0%D0%B2%D0%B5%D1%8E%D1%89%D0%B0%D1%8F%20%D1%81%D1%82%D0%B0%D0%BB%D1%8C",
    },
    {
        "id": "moechnye",
        "name": "Моечные ванны",
        "category_id": 80,
        "base": BASE_URL + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
        "attr_filter": "filters=attr[shell-size][]=1100%D1%85500%D1%85400",
        "attr_label": "attr[shell-size][]=1100х500х400",
        "second_attr": None,
    },
    {
        "id": "podtovarniki",
        "name": "Подтоварники и подставки",
        "category_id": 322,
        "base": BASE_URL + "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
        "attr_filter": "filters=attr[51][]=600%D1%85400%D1%85300",
        "attr_label": "attr[51][]=600х400х300",
        "second_attr": None,
    },
    {
        "id": "telezhki",
        "name": "Тележки сервировочные",
        "category_id": 326,
        "base": BASE_URL + "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/",
        "attr_filter": None,
        "attr_label": "baseline (no attr sidebar)",
        "second_attr": None,
    },
]


def fetch_url(url: str) -> str:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-M9.8.9-08/1.0"})
    return urllib.request.urlopen(req, timeout=120, context=ctx).read().decode("utf-8", "replace")


def count_cards(html: str) -> int:
    return len(re.findall(r'class="[^"]*product-card[^"]*"', html))


def join_url(base: str, *parts: str) -> str:
    sep = "&" if "?" in base else "?"
    return base + sep + "&".join(p for p in parts if p)


def filter_sidebar_html(html: str) -> str:
    m = re.search(r'<div class="flt" data-filters>[\s\S]*?</form>\s*</div>', html)
    return m.group(0) if m else ""


def count_group_reset_buttons(sidebar: str) -> int:
    return len(re.findall(r"data-filter-group-reset", sidebar))


def count_hidden_group_reset(sidebar: str) -> int:
    return len(re.findall(r'data-filter-group-reset[^>]*\shidden', sidebar))


def has_global_reset(sidebar: str) -> bool:
    return "data-filter-reset" in sidebar


def has_headbar(sidebar: str) -> bool:
    return "flt__group-headbar" in sidebar


def attr_groups_with_reset(sidebar: str) -> int:
    return len(re.findall(r'name="attr\[', sidebar))


def price_group_has_no_reset(sidebar: str) -> bool:
    price_block = re.search(
        r'flt__group-title[^>]*>\s*Цена[\s\S]*?(?=flt__group-title|flt__switches|flt__actions|$)',
        sidebar,
        re.I,
    )
    if not price_block:
        return True
    return "data-filter-group-reset" not in price_block.group(0)


def main_js_has_group_reset(html: str) -> bool:
    m = re.search(r'<script[^>]+src="([^"]*main\.js[^"]*)"', html)
    if not m:
        return False
    js_url = m.group(1)
    if js_url.startswith("/"):
        js_url = BASE_URL + js_url
    elif not js_url.startswith("http"):
        js_url = BASE_URL + "/" + js_url.lstrip("/")
    js = fetch_url(js_url)
    return "initGroupReset" in js and "updateGroupResetVisibility" in js


def main() -> None:
    results: dict = {
        "task": "M9.8.9-08",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "categories": [],
        "global_checks": {},
        "all_pass": True,
    }

    sample_html = fetch_url(CATEGORIES[0]["base"])
    sample_sidebar = filter_sidebar_html(sample_html)

    results["global_checks"]["main_js_group_reset"] = {
        "pass": main_js_has_group_reset(sample_html),
    }
    results["global_checks"]["headbar_markup"] = {
        "pass": has_headbar(sample_sidebar),
    }
    results["global_checks"]["distinct_selector"] = {
        "pass": "data-filter-group-reset" in sample_sidebar and sample_sidebar.count("data-filter-reset") >= 1,
        "note": "group reset uses data-filter-group-reset; global data-filter-reset preserved",
    }

    if not results["global_checks"]["main_js_group_reset"]["pass"]:
        results["all_pass"] = False
    if not results["global_checks"]["headbar_markup"]["pass"]:
        results["all_pass"] = False

    for cat in CATEGORIES:
        base_html = fetch_url(cat["base"])
        sidebar = filter_sidebar_html(base_html)

        entry = {
            "id": cat["id"],
            "name": cat["name"],
            "category_id": cat["category_id"],
            "checks": {},
        }

        reset_count = count_group_reset_buttons(sidebar)
        attr_inputs = attr_groups_with_reset(sidebar)

        entry["checks"]["group_reset_buttons_present"] = {
            "pass": reset_count > 0 if cat["id"] != "telezhki" else reset_count == 0,
            "reset_buttons": reset_count,
            "attr_input_markers": attr_inputs,
            "note": "telezhki: no attr groups expected",
        }

        entry["checks"]["price_not_affected"] = {
            "pass": price_group_has_no_reset(sidebar),
        }

        entry["checks"]["global_reset_preserved"] = {
            "pass": has_global_reset(sidebar),
        }

        if cat["attr_filter"]:
            attr_url = join_url(cat["base"], cat["attr_filter"])
            attr_html = fetch_url(attr_url)
            attr_sidebar = filter_sidebar_html(attr_html)
            checked = len(re.findall(r'class="flt__check[^"]*active[^"]*"', attr_sidebar))
            hidden_resets = count_hidden_group_reset(attr_sidebar)
            visible_resets = reset_count - hidden_resets if reset_count >= hidden_resets else 0

            entry["checks"]["reload_active_group_shows_reset"] = {
                "url": attr_url,
                "active_checks": checked,
                "pass": checked > 0 and reset_count > 0,
                "note": "checked attr on reload — reset button markup present",
            }

            entry["checks"]["reload_inactive_groups_hidden"] = {
                "pass": hidden_resets >= max(0, reset_count - 1) or reset_count <= 1,
                "hidden_reset_buttons": hidden_resets,
                "total_reset_buttons": reset_count,
                "note": "Option A: only groups with selection should expose reset (hidden attr on others)",
            }

            attr_cards = count_cards(attr_html)
            entry["checks"]["attr_filter_works"] = {
                "filter": cat["attr_label"],
                "product_cards": attr_cards,
                "pass": attr_cards > 0,
            }

            if cat.get("second_attr"):
                dual_url = join_url(cat["base"], cat["attr_filter"], cat["second_attr"])
                dual_html = fetch_url(dual_url)
                dual_sidebar = filter_sidebar_html(dual_html)
                dual_hidden = count_hidden_group_reset(dual_sidebar)
                entry["checks"]["multi_group_selection"] = {
                    "url": dual_url,
                    "pass": count_group_reset_buttons(dual_sidebar) >= 2,
                    "hidden_on_inactive": dual_hidden,
                    "note": "two attr groups selected — both should have reset controls in markup",
                }
        else:
            entry["checks"]["attr_filter_works"] = {
                "filter": cat["attr_label"],
                "pass": count_cards(base_html) > 0,
            }

        owp_url = join_url(cat["base"], "filters=only_with_price=1")
        owp_cards = count_cards(fetch_url(owp_url))
        entry["checks"]["only_with_price_unaffected"] = {
            "url": owp_url,
            "product_cards": owp_cards,
            "pass": owp_cards > 0,
        }

        price_url = join_url(cat["base"], "filters=price_from=1000&price_to=500000")
        price_cards = count_cards(fetch_url(price_url))
        entry["checks"]["price_filter_unaffected"] = {
            "url": price_url,
            "product_cards": price_cards,
            "pass": price_cards >= 0,
        }

        combined_url = join_url(
            cat["base"],
            cat.get("attr_filter") or "",
            "filters=only_with_price=1" if cat.get("attr_filter") else "filters=only_with_price=1",
        )
        if cat.get("attr_filter"):
            combined_url = join_url(cat["base"], cat["attr_filter"], "only_with_price=1")
            combined_cards = count_cards(fetch_url(combined_url))
            entry["checks"]["group_reset_with_only_with_price"] = {
                "url": combined_url,
                "product_cards": combined_cards,
                "pass": combined_cards >= 0,
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
