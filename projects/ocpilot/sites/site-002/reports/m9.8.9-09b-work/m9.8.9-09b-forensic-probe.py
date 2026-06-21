#!/usr/bin/env python3
"""M9.8.9-09B forensic — live HTML href extraction for filter→limit scenario."""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
OUT = Path(__file__).resolve().parent


def fetch(url: str) -> tuple[str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "M989-09B-FORENSIC"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return resp.read().decode("utf-8", "replace"), resp.geturl()


def limit_hrefs(html: str) -> list[str]:
    hrefs: list[str] = []
    for m in re.finditer(r'href="([^"]*limit=(?:15|25|30|50|100)[^"]*)"', html):
        hrefs.append(m.group(1).replace("&amp;", "&"))
    seen: set[str] = set()
    out: list[str] = []
    for h in hrefs:
        if h not in seen:
            seen.add(h)
            out.append(h)
    return out


def category_limit_block(html: str) -> str | None:
    m = re.search(r'(<div class="category__limit"[\s\S]{0,2500})', html)
    if m:
        return m.group(1)
    m = re.search(r'(Показывать[\s\S]{0,1500})', html)
    return m.group(1) if m else None


def sort_controls(html: str) -> list[dict]:
    out: list[dict] = []
    for m in re.finditer(
        r'<button[^>]*data-sort="([^"]+)"[^>]*data-order="([^"]+)"[^>]*>',
        html,
    ):
        out.append({"type": "button", "data-sort": m.group(1), "data-order": m.group(2)})
    for m in re.finditer(r'href="([^"]*sort=[^"]*)"', html):
        out.append({"type": "href", "href": m.group(1).replace("&amp;", "&")})
    return out[:25]


def pagination_hrefs(html: str) -> list[str]:
    out: list[str] = []
    for m in re.finditer(r'href="([^"]*page=[^"]*)"', html):
        out.append(m.group(1).replace("&amp;", "&"))
    seen: set[str] = set()
    ded: list[str] = []
    for h in out:
        if h not in seen:
            seen.add(h)
            ded.append(h)
    return ded[:20]


def has_checked_only_with_price(html: str) -> bool:
    return bool(
        re.search(
            r'name="only_with_price"[^>]*checked|checked[^>]*name="only_with_price"',
            html,
        )
    )


def main() -> None:
    urls = {
        "plain": BASE,
        "filtered": BASE + "?filters=" + urllib.parse.quote("only_with_price=1", safe="=;"),
        "filtered_limit50": BASE
        + "?filters="
        + urllib.parse.quote("only_with_price=1", safe="=;")
        + "&limit=50",
    }

    results: dict = {}
    for key, url in urls.items():
        html, final = fetch(url)
        (OUT / f"{key}.html").write_text(html, encoding="utf-8")
        results[key] = {
            "requested_url": url,
            "final_url": final,
            "only_with_price_checked": has_checked_only_with_price(html),
            "limit_hrefs": limit_hrefs(html),
            "limit_block": category_limit_block(html),
            "sort_controls": sort_controls(html),
            "pagination_hrefs": pagination_hrefs(html),
        }

    # Simulate AJAX filter request (updateProducts path)
    ajax_url = (
        BASE
        + "?filters="
        + urllib.parse.quote("only_with_price=1", safe="=;")
        + "&ajax=1"
    )
    try:
        ajax_html, ajax_final = fetch(ajax_url)
        (OUT / "ajax-filtered.html").write_text(ajax_html, encoding="utf-8")
        results["ajax_filtered"] = {
            "requested_url": ajax_url,
            "final_url": ajax_final,
            "is_json": ajax_html.strip().startswith("{"),
            "snippet_start": ajax_html[:500],
            "limit_hrefs_in_response": limit_hrefs(ajax_html),
        }
    except Exception as exc:
        results["ajax_filtered"] = {"error": str(exc)}

    # Fetch live main.js hash snippet for updateBrowserUrl / updateProducts
    js_url = "https://zpm.new-site.space/assets/js/main.js"
    js_html, _ = fetch(js_url)
    (OUT / "main-live.js").write_text(js_html, encoding="utf-8")

    def extract_fn(name: str) -> str | None:
        m = re.search(rf"function {name}\([^)]*\)\s*\{{[\s\S]{{0,1200}}", js_html)
        return m.group(0) if m else None

    results["live_js"] = {
        "url": js_url,
        "bytes": len(js_html),
        "updateBrowserUrl": extract_fn("updateBrowserUrl"),
        "updateProducts": extract_fn("updateProducts"),
        "buildFilterUrl": extract_fn("buildFilterUrl") if "buildFilterUrl" in js_html else None,
    }

    # grep alternate URL builders
    for pat in [
        r"fullPath \+ \"\?filters=\"",
        r"pathname \+ \"\?filters=\"",
        r"category__limit",
        r"data-limit",
    ]:
        results.setdefault("live_js_patterns", {})[pat] = len(re.findall(pat, js_html))

    summary_path = OUT / "forensic-results.json"
    summary_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
