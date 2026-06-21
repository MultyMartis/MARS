#!/usr/bin/env python3
"""Final QA — PDP content structure rebuild (known live cases)."""
import json
import sys

import re
import urllib.request

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"

TEST_URLS = [
    (
        "case_a_desc_docs",
        BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
        "stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
    ),
    (
        "case_c_no_desc_docs",
        BASE + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-svarnye-premium/"
        "vanna-moechnaya-vms-p-2-600-1400h700h850",
    ),
]

EXPECTED = {
    "case_a_desc_docs": {
        "has_description": True,
        "has_documents": True,
        "has_specs_docs_wrapper": True,
        "standalone_specs": False,
    },
    "case_c_no_desc_docs": {
        "has_description": False,
        "has_documents": True,
        "has_specs_docs_wrapper": True,
        "standalone_specs": False,
    },
}


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def analyze_case(url, label):
    html = fetch(url)
    has_description = "product-content__description" in html
    has_documents = (
        "product-content__documents" in html and "docs-list__item" in html
    )
    has_specs_docs_wrapper = "product-content__specs-docs" in html
    standalone_specs = (
        "product-content__specifications" in html and not has_specs_docs_wrapper
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

    exp = EXPECTED[label]
    for key, want in exp.items():
        checks[f"expect_{key}"] = checks.get(key) == want

    always_true = {
        "php_ok",
        "twig_ok",
        "product_content",
        "no_tabs",
        "specs_visible",
        "help_visible",
        "related_visible",
        "docs_not_empty",
        "no_empty_docs_block",
        "no_empty_desc_block",
    }

    fails = []
    for key, val in checks.items():
        if key in ("url", "label") or key.startswith("expect_"):
            continue
        if key in always_true and isinstance(val, bool) and not val:
            fails.append(key)
    for key, val in checks.items():
        if key.startswith("expect_") and not val:
            fails.append(key)

    checks["pass"] = len(fails) == 0
    checks["fails"] = fails
    return checks


def main():
    results = {
        "cases_tested_live": [],
        "cases_not_in_catalog": {
            "case_b_desc_no_docs": "557+ PDP URLs scanned; all had category documents — no live SKU found",
            "case_d_no_desc_no_docs": "557+ PDP URLs scanned; no SKU without description and without documents",
        },
        "template_logic_unverified_live": ["case_b_desc_no_docs", "case_d_no_desc_no_docs"],
    }
    all_pass = True
    for label, url in TEST_URLS:
        case = analyze_case(url, label)
        all_pass = all_pass and case["pass"]
        results["cases_tested_live"].append(case)

    out = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-rebuild-work\content-rebuild-qa-result.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(json.dumps(results, ensure_ascii=False, indent=2))
    print("OVERALL:", "PASS" if all_pass else "FAIL")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
