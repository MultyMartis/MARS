#!/usr/bin/env python3
import json
import re
import urllib.request
from urllib.parse import urljoin

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"
TARGETS = ["case_b_desc_no_docs", "case_d_no_desc_no_docs"]


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def classify(html):
    if "product-hero" not in html:
        return None
    has_desc = "product-content__description" in html
    has_docs = "product-content__documents" in html and "docs-list__item" in html
    if has_desc and has_docs:
        return "case_a_desc_docs"
    if has_desc and not has_docs:
        return "case_b_desc_no_docs"
    if not has_desc and has_docs:
        return "case_c_no_desc_docs"
    if not has_desc and not has_docs:
        return "case_d_no_desc_no_docs"
    return None


def extract_links(html, base_url):
    links = set()
    for href in re.findall(r'href="([^"]+)"', html):
        if "katalog" not in href:
            continue
        if href.startswith("/"):
            href = BASE + href
        elif not href.startswith("http"):
            href = urljoin(base_url, href)
        if "zpm.new-site.space" not in href:
            continue
        links.add(href.split("?")[0].rstrip("/"))
    return links


def main():
    # resume from broader catalog branches
    seeds = [
        BASE + "/katalog/kholodilnoe-oborudovanie/",
        BASE + "/katalog/teplovoe-oborudovanie/",
        BASE + "/katalog/hlebopekarnoe-oborudovanie/",
        BASE + "/katalog/posuda-i-inventar/",
        BASE + "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/",
        BASE + "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/",
    ]
    queue = list(seeds)
    seen = set()
    cases = {}
    scanned = 0
    max_scan = 500

    while queue and scanned < max_scan:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        try:
            html = fetch(url)
        except Exception:
            continue
        scanned += 1

        case = classify(html)
        if case in TARGETS and case not in cases:
            cases[case] = url

        for link in extract_links(html, url):
            if link not in seen and link.startswith(BASE + "/katalog"):
                queue.append(link)

        if len(cases) == len(TARGETS):
            break

    out = {"scanned": scanned, "cases": cases}
    path = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-rebuild-work\scan-bfs2-result.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
