#!/usr/bin/env python3
import json
import re
import urllib.request
from collections import Counter

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def classify(html):
    if "product-hero" not in html:
        return "not_pdp"
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
    return "unknown"


def main():
    xml = fetch(BASE + "/sitemap.xml")
    urls = [u.split("?")[0].rstrip("/") for u in re.findall(r"<loc>([^<]+)</loc>", xml)]
    product_urls = [u for u in urls if "/katalog/" in u and u.count("/") >= 6]

    counts = Counter()
    examples = {}
    rows = []

    for url in product_urls:
        try:
            html = fetch(url)
        except Exception as e:
            counts["fetch_error"] += 1
            continue
        case = classify(html)
        counts[case] += 1
        if case not in examples:
            examples[case] = url
        rows.append({"url": url, "case": case})

    out = {
        "total": len(product_urls),
        "counts": dict(counts),
        "examples": examples,
    }
    path = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-rebuild-work\scan-all-states-result.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
