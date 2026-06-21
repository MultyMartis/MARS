#!/usr/bin/env python3
"""M9.8.9-06J — post-deploy QA for numeric attribute filter hotfix."""
from __future__ import annotations

import json
import re
import ssl
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE_URL = "https://zpm.new-site.space"

OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06j-work")
OUT_JSON = OUT_DIR / "qa-results.json"

PROBES = [
    {
        "id": "stoly_baseline",
        "category": "Столы",
        "category_id": 301,
        "kind": "primary",
        "pass_min_cards": 1,
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/stoly/",
    },
    {
        "id": "stoly_attr51",
        "category": "Столы",
        "category_id": 301,
        "kind": "primary",
        "pass_min_cards": 1,
        "filter": "attr[51][]=Без полки",
        "url": BASE_URL
        + "/katalog/nejtralnoe-oborudovanie/stoly/?filters=attr[51][]=%D0%91%D0%B5%D0%B7%20%D0%BF%D0%BE%D0%BB%D0%BA%D0%B8",
    },
    {
        "id": "stoly_construction_slug",
        "category": "Столы",
        "category_id": 301,
        "kind": "regression",
        "pass_min_cards": 1,
        "filter": "attr[construction][]=сварная (неразборная)",
        "url": BASE_URL
        + "/katalog/nejtralnoe-oborudovanie/stoly/?filters=attr[construction][]=%D1%81%D0%B2%D0%B0%D1%80%D0%BD%D0%B0%D1%8F%20%28%D0%BD%D0%B5%D1%80%D0%B0%D0%B7%D0%B1%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%29",
    },
    {
        "id": "podtovarniki_baseline",
        "category": "Подтоварники",
        "category_id": 322,
        "kind": "primary",
        "pass_min_cards": 1,
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
    },
    {
        "id": "podtovarniki_attr51",
        "category": "Подтоварники",
        "category_id": 322,
        "kind": "primary",
        "pass_min_cards": 1,
        "filter": "attr[51][]",
        "url": BASE_URL
        + "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/?filters=attr[51][]=600%D1%85400%D1%85300",
    },
    {
        "id": "sinks_shell_size",
        "category": "Моечные ванны",
        "category_id": 80,
        "kind": "regression",
        "pass_min_cards": 1,
        "filter": "attr[shell-size][]=1100х500х400",
        "url": BASE_URL
        + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/?filters=attr[shell-size][]=1100%D1%85500%D1%85400",
    },
    {
        "id": "zonty_construction",
        "category": "Зонты вытяжные",
        "category_id": 207,
        "kind": "regression",
        "pass_min_cards": 1,
        "filter": "attr[construction][]=угловая, купольная",
        "url": BASE_URL
        + "/zonty-vytyazhnye/?filters=attr[construction][]=%D1%83%D0%B3%D0%BB%D0%BE%D0%B2%D0%B0%D1%8F%2C%20%D0%BA%D1%83%D0%BF%D0%BE%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F",
    },
]


def fetch_url(url: str) -> str:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-M9.8.9-06J/1.0"})
    return urllib.request.urlopen(req, timeout=120, context=ctx).read().decode("utf-8", "replace")


def count_cards(html: str) -> int:
    return len(re.findall(r'class="[^"]*product-card[^"]*"', html))


def main() -> None:
    results: dict = {
        "task": "M9.8.9-06J",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "probes": [],
        "checks": {},
    }

    for probe in PROBES:
        html = fetch_url(probe["url"])
        cards = count_cards(html)
        entry = {
            "id": probe["id"],
            "category": probe["category"],
            "category_id": probe["category_id"],
            "kind": probe["kind"],
            "filter": probe.get("filter"),
            "url": probe["url"],
            "product_cards": cards,
            "pass": cards >= probe["pass_min_cards"],
        }
        results["probes"].append(entry)
        results["checks"][probe["id"]] = {
            "product_cards": cards,
            "pass_min_cards": probe["pass_min_cards"],
            "pass": entry["pass"],
        }

    results["checks"]["primary_attr51_fixed"] = {
        "pass": all(
            results["checks"][k]["pass"]
            for k in ("stoly_attr51", "podtovarniki_attr51")
        ),
        "stoly_attr51_cards": results["checks"]["stoly_attr51"]["product_cards"],
        "podtovarniki_attr51_cards": results["checks"]["podtovarniki_attr51"]["product_cards"],
    }
    results["checks"]["regression_slug_filters"] = {
        "pass": all(
            results["checks"][k]["pass"]
            for k in ("stoly_construction_slug", "sinks_shell_size", "zonty_construction")
        ),
    }
    results["all_pass"] = all(
        v.get("pass") is True
        for k, v in results["checks"].items()
        if isinstance(v, dict) and "pass" in v
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
