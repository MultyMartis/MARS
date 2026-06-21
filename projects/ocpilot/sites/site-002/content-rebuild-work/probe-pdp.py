#!/usr/bin/env python3
import json
import re
import urllib.request

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def inspect_pdp(url):
    html = fetch(url)
    m = re.search(r'<section class="product-content">(.*?)</section>', html, re.S)
    content = m.group(1) if m else ""
    rel_snippets = sorted(set(re.findall(r'class="([^"]*rel[^"]*)"', html, re.I)))
    return {
        "url": url,
        "has_desc": "product-content__description" in content,
        "has_docs": "product-content__documents" in content,
        "docs_items": content.count("docs-list__item"),
        "has_specs": "product-content__specifications" in content,
        "has_help": "product-help" in content,
        "rel_classes": rel_snippets[:15],
        "related_text_hits": [t for t in ["С этим товаром", "Похожие", "related", "relproducts"] if t.lower() in html.lower()],
    }


def scan_catalog(limit=80):
    html = fetch(BASE + "/katalog/")
    links = []
    for link in re.findall(r'href="(/katalog/[^"]+)"', html):
        if link.count("/") >= 6 and link not in links:
            links.append(link)
    results = []
    for link in links[:limit]:
        url = BASE + link
        try:
            html = fetch(url)
        except Exception:
            continue
        if "product-hero" not in html:
            continue
        m = re.search(r'<section class="product-content">(.*?)</section>', html, re.S)
        if not m:
            continue
        content = m.group(1)
        has_desc = "product-content__description" in content
        has_docs = "product-content__documents" in content and "docs-list__item" in content
        results.append({"url": url, "has_desc": has_desc, "has_docs": has_docs})
    return results


if __name__ == "__main__":
    spkb = (
        BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
        "stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
    )
    spp = (
        BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/"
        "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
    )
    out = {
        "spkb": inspect_pdp(spkb),
        "spp": inspect_pdp(spp),
        "catalog_scan": scan_catalog(100),
    }
    cases = {"a": None, "b": None, "c": None, "d": None}
    for row in out["catalog_scan"]:
        key = (
            ("a" if row["has_desc"] and row["has_docs"] else None)
            or ("b" if row["has_desc"] and not row["has_docs"] else None)
            or ("c" if not row["has_desc"] and row["has_docs"] else None)
            or ("d" if not row["has_desc"] and not row["has_docs"] else None)
        )
        if key and cases[key] is None:
            cases[key] = row["url"]
    out["case_urls"] = cases
    path = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-rebuild-work\probe-pdp-result.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))
