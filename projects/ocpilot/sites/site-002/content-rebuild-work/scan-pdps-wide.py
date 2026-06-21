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


def main():
    sitemap_urls = []
    for sm in [BASE + "/sitemap.xml", BASE + "/index.php?route=extension/feed/google_sitemap"]:
        try:
            xml = fetch(sm)
        except Exception:
            continue
        sitemap_urls.extend(re.findall(r"<loc>([^<]+)</loc>", xml))

    product_urls = [u for u in sitemap_urls if "/katalog/" in u and u.count("/") >= 6]
    if not product_urls:
        # fallback: product links from home/search
        home = fetch(BASE + "/")
        product_urls = re.findall(
            r"https://zpm\.new-site\.space/katalog/[^\"'\s<>]+", home
        )

    cases = {}
    checked = 0
    for url in product_urls:
        if checked >= 200:
            break
        url = url.split("?")[0].rstrip("/")
        try:
            html = fetch(url)
        except Exception:
            continue
        checked += 1
        if "product-hero" not in html:
            continue
        case = classify(html)
        if case and case not in cases:
            cases[case] = url
        if len(cases) == 4:
            break

    out = {"checked": checked, "sitemap_total": len(product_urls), "cases": cases}
    path = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-rebuild-work\scan-pdps-wide-result.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
