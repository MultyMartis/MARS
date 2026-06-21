#!/usr/bin/env python3
"""QA for PDP content structure rebuild — four render states."""
import json
import re
import sys
import urllib.error
import urllib.request
from html import unescape

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"

# Known + discovered PDP URLs (filled by probe if needed)
CANDIDATES = []


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def classify_pdp(html):
    if "product-hero" not in html or 'class="product-content"' not in html:
        return None
    has_desc = "product-content__description" in html
    has_docs = (
        "product-content__documents" in html and "docs-list__item" in html
    )
    if has_desc and has_docs:
        return "case_a_desc_docs"
    if has_desc and not has_docs:
        return "case_b_desc_no_docs"
    if not has_desc and has_docs:
        return "case_c_no_desc_docs"
    if not has_desc and not has_docs:
        return "case_d_no_desc_no_docs"
    return None


def probe_catalog():
    """Find one URL per render state from catalog listings."""
    found = {}
    seeds = [
        BASE + "/katalog/",
        BASE + "/katalog/nejtralnoe-oborudovanie/",
        BASE + "/katalog/nejtralnoe-oborudovanie/stoly/",
        BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/",
        BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/",
    ]
    product_links = []
    for cat_url in seeds:
        try:
            html = fetch(cat_url)
        except urllib.error.HTTPError:
            continue
        for link in re.findall(r'href="(/katalog/[^"]+)"', html):
            if link.count("/") >= 6 and link not in product_links:
                product_links.append(link)

    for link in product_links:
        url = BASE + link
        try:
            html = fetch(url)
        except Exception:
            continue
        case = classify_pdp(html)
        if case and case not in found:
            found[case] = url
        if len(found) == 4:
            break

    return found


EXPECTED = {
    "case_a_desc_docs": {
        "has_description": True,
        "has_documents": True,
        "has_specs_docs_wrapper": True,
        "standalone_specs": False,
    },
    "case_b_desc_no_docs": {
        "has_description": True,
        "has_documents": False,
        "has_specs_docs_wrapper": False,
        "standalone_specs": True,
    },
    "case_c_no_desc_docs": {
        "has_description": False,
        "has_documents": True,
        "has_specs_docs_wrapper": True,
        "standalone_specs": False,
    },
    "case_d_no_desc_no_docs": {
        "has_description": False,
        "has_documents": False,
        "has_specs_docs_wrapper": False,
        "standalone_specs": True,
    },
}


def analyze(url, label):
    html = fetch(url)
    has_description = "product-content__description" in html
    has_documents = (
        "product-content__documents" in html and "docs-list__item" in html
    )
    has_specs_docs_wrapper = "product-content__specs-docs" in html
    standalone_specs = (
        "product-content__specifications" in html
        and not has_specs_docs_wrapper
    )

    checks = {
        "url": url,
        "label": label,
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "twig_ok": "Twig_Error" not in html,
        "product_content": 'class="product-content"' in html,
        "no_tabs": 'class="tabs js-tabs"' not in html,
        "specs_visible": "product-content__specifications" in html,
        "help_visible": "product-help" in html,
        "related_visible": "rel-products" in html,
        "has_description": has_description,
        "has_documents": has_documents,
        "has_specs_docs_wrapper": has_specs_docs_wrapper,
        "standalone_specs": standalone_specs,
    }

    if has_documents:
        checks["docs_not_empty"] = "docs-list__item" in html
    else:
        checks["no_empty_docs_block"] = "product-content__documents" not in html

    if not has_description:
        checks["no_empty_desc_block"] = "product-content__description" not in html

    exp = EXPECTED.get(label, {})
    for key, want in exp.items():
        checks[f"expect_{key}"] = checks.get(key) == want

    fails = []
    for key, val in checks.items():
        if key in ("url", "label") or key.startswith("expect_"):
            continue
        if isinstance(val, bool) and not val:
            fails.append(key)
    for key, val in checks.items():
        if key.startswith("expect_") and not val:
            fails.append(key)

    checks["pass"] = len(fails) == 0
    checks["fails"] = fails
    return checks


def main():
    discovered = probe_catalog()
    order = [
        "case_a_desc_docs",
        "case_b_desc_no_docs",
        "case_c_no_desc_docs",
        "case_d_no_desc_no_docs",
    ]
    urls = [(label, discovered[label]) for label in order if label in discovered]

    results = {"cases": [], "discovered": discovered}
    all_pass = True
    for label, url in urls:
        try:
            case = analyze(url, label)
        except Exception as e:
            case = {"label": label, "url": url, "pass": False, "error": str(e)}
            all_pass = False
        else:
            all_pass = all_pass and case.get("pass", False)
        results["cases"].append(case)

    out = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-rebuild-work\content-rebuild-qa-result.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(json.dumps(results, ensure_ascii=False, indent=2))
    print("OVERALL:", "PASS" if all_pass else "FAIL")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
