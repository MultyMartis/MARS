#!/usr/bin/env python3
"""M9.8.9-09A QA — HTTP probes for filter/limit/sort/pagination persistence on Столы PLP."""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
FILTERS_ONLY_PRICE = "only_with_price=1"
OUT = Path(__file__).resolve().parent / "qa-results.json"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "M989-09A-QA"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return resp.read().decode("utf-8", "replace")


def cards(html: str) -> int:
    return len(re.findall(r'<article class="p-card', html))


def has_checked_only_with_price(html: str) -> bool:
    return bool(
        re.search(
            r'name="only_with_price"[^>]*checked|checked[^>]*name="only_with_price"',
            html,
        )
    )


def limit_href_has_filters(html: str) -> bool:
    for m in re.finditer(r'href="([^"]*limit=50[^"]*)"', html):
        href = m.group(1)
        if "filters=" in href and "only_with_price" in href:
            return True
    return False


def pagination_page2_has_filters(html: str) -> bool:
    for m in re.finditer(r'href="([^"]*page=2[^"]*)"', html):
        href = m.group(1)
        if "filters=" in href and "only_with_price" in href:
            return True
    return False


def parse_query(url: str) -> dict[str, str]:
    q = urllib.parse.urlparse(url).query
    return {k: v[0] for k, v in urllib.parse.parse_qs(q, keep_blank_values=True).items()}


def main() -> None:
    results: list[dict] = []

    # Scenario baseline counts
    plain = fetch(BASE)
    plain_cards = cards(plain)
    filtered_url = BASE + "?filters=" + urllib.parse.quote(FILTERS_ONLY_PRICE, safe="=;")
    filtered = fetch(filtered_url)
    filtered_cards = cards(filtered)

    # S1 proxy: limit=50 page includes filter state in limit links when filters active
    limit50_filtered_url = filtered_url + "&limit=50"
    limit50_filtered = fetch(limit50_filtered_url)
    s1 = {
        "scenario": "S1 limit=50 + only_with_price page load",
        "url": limit50_filtered_url,
        "limit_in_url": "limit=50" in limit50_filtered_url,
        "only_with_price_checked": has_checked_only_with_price(limit50_filtered),
        "cards": cards(limit50_filtered),
        "filtered_cards_baseline": filtered_cards,
        "pass": has_checked_only_with_price(limit50_filtered)
        and "limit=50" in limit50_filtered_url,
    }
    results.append(s1)

    # S2: only_with_price page — limit=50 href must carry filters
    s2 = {
        "scenario": "S2 only_with_price -> limit=50 href",
        "url": filtered_url,
        "limit50_href_has_filters": limit_href_has_filters(filtered),
        "pass": limit_href_has_filters(filtered),
    }
    results.append(s2)

    # S3: only_with_price + sort price asc via URL (JS sort preserves params when filters in URL)
    sort_url = filtered_url + "&sort=p.price&order=ASC"
    sort_html = fetch(sort_url)
    s3 = {
        "scenario": "S3 only_with_price + sort price ASC",
        "url": sort_url,
        "only_with_price_checked": has_checked_only_with_price(sort_html),
        "query_has_sort": "sort=p.price" in sort_url and "order=ASC" in sort_url,
        "pass": has_checked_only_with_price(sort_html),
    }
    results.append(s3)

    # S4: only_with_price + page 2
    page2_url = filtered_url + "&page=2"
    page2_html = fetch(page2_url)
    s4 = {
        "scenario": "S4 only_with_price + page 2",
        "url": page2_url,
        "only_with_price_checked": has_checked_only_with_price(page2_html),
        "pagination_link_page2_has_filters": pagination_page2_has_filters(filtered),
        "pass": has_checked_only_with_price(page2_html)
        and pagination_page2_has_filters(filtered),
    }
    results.append(s4)

    # S5: full combo URL params coexist
    combo_url = filtered_url + "&limit=50&sort=p.price&order=ASC&page=2"
    combo_q = parse_query(combo_url)
    combo_html = fetch(combo_url)
    s5 = {
        "scenario": "S5 filters+limit+sort+order+page together",
        "url": combo_url,
        "params_present": {
            "filters": "only_with_price" in combo_q.get("filters", ""),
            "limit": combo_q.get("limit") == "50",
            "sort": combo_q.get("sort") == "p.price",
            "order": combo_q.get("order") == "ASC",
            "page": combo_q.get("page") == "2",
        },
        "only_with_price_checked": has_checked_only_with_price(combo_html),
        "pass": all(
            [
                "only_with_price" in combo_q.get("filters", ""),
                combo_q.get("limit") == "50",
                combo_q.get("sort") == "p.price",
                combo_q.get("order") == "ASC",
                combo_q.get("page") == "2",
                has_checked_only_with_price(combo_html),
            ]
        ),
    }
    results.append(s5)

    # S2 follow-through: fetch limit=50 link from filtered page
    m = re.search(r'href="([^"]*\?[^"]*limit=50[^"]*filters=[^"]*only_with_price[^"]*)"', filtered)
    if not m:
        m = re.search(r'href="([^"]*filters=[^"]*only_with_price[^"]*limit=50[^"]*)"', filtered)
    s2_fetch = {"scenario": "S2 follow-through limit=50 href fetch", "found_href": bool(m)}
    if m:
        href = m.group(1).replace("&amp;", "&")
        if href.startswith("/"):
            href = "https://zpm.new-site.space" + href
        html2 = fetch(href)
        s2_fetch.update(
            {
                "href": href,
                "only_with_price_checked": has_checked_only_with_price(html2),
                "limit50_active": 'limit=50' in href or 'is-active' in html2,
                "pass": has_checked_only_with_price(html2),
            }
        )
    else:
        s2_fetch["pass"] = False
    results.append(s2_fetch)

    summary = {
        "base": BASE,
        "plain_cards": plain_cards,
        "filtered_cards": filtered_cards,
        "all_pass": all(r.get("pass") for r in results),
        "results": results,
    }
    OUT.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
