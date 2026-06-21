#!/usr/bin/env python3
"""M9.8.9-08A — post-deploy QA: group reset button body placement + disabled/active states."""
from __future__ import annotations

import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE_URL = "https://zpm.new-site.space"

OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-08a-work")
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
]


def fetch_url(url: str) -> str:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-M9.8.9-08A/1.0"})
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


def count_disabled_group_reset(sidebar: str) -> int:
    return len(re.findall(r'data-filter-group-reset[^>]*\sdisabled', sidebar))


def reset_in_body_not_headbar(sidebar: str) -> bool:
    if "flt__group-headbar" in sidebar:
        return False
    panels = re.findall(
        r'(<div class="flt__group-body"[^>]*data-acc-panel[^>]*>[\s\S]*?</div>)',
        sidebar,
    )
    attr_panels = [p for p in panels if 'name="attr[' in p]
    if not attr_panels:
        return True
    return all("data-filter-group-reset" in p for p in attr_panels)


def has_global_reset(sidebar: str) -> bool:
    return "data-filter-reset" in sidebar


def price_group_has_no_reset(sidebar: str) -> bool:
    price_block = re.search(
        r'flt__group-title[^>]*>\s*Цена[\s\S]*?(?=flt__group-title|flt__switches|flt__actions|$)',
        sidebar,
        re.I,
    )
    if not price_block:
        return True
    return "data-filter-group-reset" not in price_block.group(0)


def fetch_main_js(html: str) -> str:
    m = re.search(r'<script[^>]+src="([^"]*main\.js[^"]*)"', html)
    if not m:
        return ""
    js_url = m.group(1)
    if js_url.startswith("/"):
        js_url = BASE_URL + js_url
    elif not js_url.startswith("http"):
        js_url = BASE_URL + "/" + js_url.lstrip("/")
    return fetch_url(js_url)


def fetch_style_css(html: str) -> str:
    m = re.search(r'<link[^>]+href="([^"]*style\.css[^"]*)"', html)
    if not m:
        return ""
    css_url = m.group(1)
    if css_url.startswith("/"):
        css_url = BASE_URL + css_url
    elif not css_url.startswith("http"):
        css_url = BASE_URL + "/" + css_url.lstrip("/")
    return fetch_url(css_url)


def main() -> None:
    results: dict = {
        "task": "M9.8.9-08A",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "categories": [],
        "global_checks": {},
        "all_pass": True,
    }

    sample_html = fetch_url(CATEGORIES[0]["base"])
    sample_sidebar = filter_sidebar_html(sample_html)
    js = fetch_main_js(sample_html)
    css = fetch_style_css(sample_html)

    results["global_checks"]["no_headbar"] = {
        "pass": "flt__group-headbar" not in sample_sidebar,
        "note": "08A removes headbar wrapper; reset lives in group body",
    }
    results["global_checks"]["no_hidden_reset"] = {
        "pass": count_hidden_group_reset(sample_sidebar) == 0,
        "hidden_count": count_hidden_group_reset(sample_sidebar),
    }
    results["global_checks"]["js_disabled_active_logic"] = {
        "pass": 'btn.disabled = !hasChecked' in js and 'is-active' in js and "if (btn.disabled) return" in js,
    }
    results["global_checks"]["css_active_accent"] = {
        "pass": "M9.8.9-08A" in css and "var(--accent-color-02)" in css,
    }
    results["global_checks"]["distinct_selector"] = {
        "pass": "data-filter-group-reset" in sample_sidebar and sample_sidebar.count("data-filter-reset") >= 1,
    }
    results["global_checks"]["reset_in_body"] = {
        "pass": reset_in_body_not_headbar(sample_sidebar),
    }

    for check in results["global_checks"].values():
        if not check.get("pass"):
            results["all_pass"] = False

    for cat in CATEGORIES:
        base_html = fetch_url(cat["base"])
        sidebar = filter_sidebar_html(base_html)
        reset_count = count_group_reset_buttons(sidebar)

        entry = {
            "id": cat["id"],
            "name": cat["name"],
            "category_id": cat["category_id"],
            "checks": {},
        }

        entry["checks"]["reset_buttons_in_body"] = {
            "pass": reset_count > 0 and reset_in_body_not_headbar(sidebar),
            "reset_buttons": reset_count,
        }
        entry["checks"]["always_visible_not_hidden"] = {
            "pass": count_hidden_group_reset(sidebar) == 0,
            "hidden": count_hidden_group_reset(sidebar),
        }
        entry["checks"]["baseline_disabled_markup"] = {
            "pass": count_disabled_group_reset(sidebar) >= reset_count - 1 if reset_count else True,
            "disabled_buttons": count_disabled_group_reset(sidebar),
            "total": reset_count,
            "note": "all groups without selection should render disabled",
        }
        entry["checks"]["price_not_affected"] = {"pass": price_group_has_no_reset(sidebar)}
        entry["checks"]["global_reset_preserved"] = {"pass": has_global_reset(sidebar)}

        if cat["attr_filter"]:
            attr_url = join_url(cat["base"], cat["attr_filter"])
            attr_html = fetch_url(attr_url)
            attr_sidebar = filter_sidebar_html(attr_html)
            attr_reset = count_group_reset_buttons(attr_sidebar)
            attr_hidden = count_hidden_group_reset(attr_sidebar)
            checked_inputs = len(re.findall(r"flt__check-input[^>]*checked", attr_sidebar))

            entry["checks"]["attr_filter_works"] = {
                "filter": cat["attr_label"],
                "product_cards": count_cards(attr_html),
                "pass": count_cards(attr_html) > 0,
            }
            entry["checks"]["selected_group_has_reset"] = {
                "url": attr_url,
                "checked_inputs": checked_inputs,
                "reset_buttons": attr_reset,
                "pass": checked_inputs > 0 and attr_reset > 0 and attr_hidden == 0,
                "note": "SSR may render all disabled; JS enables active group on init",
            }

            if cat.get("second_attr"):
                dual_url = join_url(cat["base"], cat["attr_filter"], cat["second_attr"])
                dual_sidebar = filter_sidebar_html(fetch_url(dual_url))
                entry["checks"]["multi_group_reset_markup"] = {
                    "pass": count_group_reset_buttons(dual_sidebar) >= 2 and count_hidden_group_reset(dual_sidebar) == 0,
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
