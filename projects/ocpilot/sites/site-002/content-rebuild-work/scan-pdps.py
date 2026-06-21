#!/usr/bin/env python3
import json
import re
import urllib.request
from urllib.parse import urljoin

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"
SEEDS = [
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/",
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/",
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/",
    BASE + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-premium-600/",
]


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def classify(html):
    if "product-hero" not in html:
        return None, {}
    has_desc = "product-content__description" in html
    has_docs = "product-content__documents" in html and "docs-list__item" in html
    meta = {
        "has_desc": has_desc,
        "has_docs": has_docs,
        "specs": "product-content__specifications" in html,
        "help": "product-help" in html,
        "related": "rel-products" in html,
    }
    if has_desc and has_docs:
        return "case_a_desc_docs", meta
    if has_desc and not has_docs:
        return "case_b_desc_no_docs", meta
    if not has_desc and has_docs:
        return "case_c_no_desc_docs", meta
    if not has_desc and not has_docs:
        return "case_d_no_desc_no_docs", meta
    return None, meta


def extract_links(html, base_url):
    links = set()
    for href in re.findall(r'href="([^"]+)"', html):
        if "katalog" not in href:
            continue
        if href.startswith("/"):
            href = BASE + href
        elif href.startswith("http"):
            pass
        else:
            href = urljoin(base_url, href)
        if "zpm.new-site.space" not in href:
            continue
        if "?" in href:
            href = href.split("?")[0]
        links.add(href.rstrip("/"))
    return links


def main():
    queue = list(SEEDS)
    seen = set()
    cases = {}
    scanned = 0

    while queue and scanned < 120:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        try:
            html = fetch(url)
        except Exception:
            continue
        scanned += 1

        case, meta = classify(html)
        if case and case not in cases:
            cases[case] = {"url": url, **meta}

        if case is None:
            for link in extract_links(html, url):
                if link not in seen and link.startswith(BASE + "/katalog/"):
                    queue.append(link)

        if len(cases) == 4:
            break

    out = {"scanned": scanned, "cases": cases}
    path = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-rebuild-work\scan-pdps-result.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
