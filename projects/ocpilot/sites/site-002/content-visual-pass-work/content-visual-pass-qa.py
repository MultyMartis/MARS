#!/usr/bin/env python3
"""QA — PDP content visual structure pass."""
import json
import re
import sys
import urllib.request

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"

URLS = {
    "case_a_desc_docs": (
        BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
        "stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
    ),
    "case_c_no_desc_docs": (
        BASE + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-svarnye-premium/"
        "vanna-moechnaya-vms-p-2-600-1400h700h850"
    ),
}

EXPECTED = {
    "case_a_desc_docs": {
        "has_description": True,
        "has_documents": True,
        "has_top": True,
        "has_standalone_specs": True,
        "has_desc_heading": True,
        "has_specs_heading": True,
        "has_docs_heading": True,
    },
    "case_c_no_desc_docs": {
        "has_description": False,
        "has_documents": True,
        "has_top": True,
        "has_standalone_specs": False,
        "has_desc_heading": False,
        "has_specs_heading": True,
        "has_docs_heading": True,
    },
}


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def extract_product_content(html):
    start = html.find('<section class="product-content">')
    if start < 0:
        return ""
    marker = '<section class="rel-products"'
    end = html.find(marker, start)
    if end < 0:
        end = html.find("</main>", start)
    if end < 0:
        end = len(html)
    return html[start:end]


def count_specs_sections(content):
    return len(re.findall(r'class="product-content__specifications', content))


def analyze(label, url):
    html = fetch(url)
    content = extract_product_content(html)

    doc_block = ""
    m = re.search(
        r'<section class="product-content__documents[^"]*".*?</section>',
        content,
        re.S,
    )
    if m:
        doc_block = m.group(0)

    links = re.findall(
        r'<a class="docs-list__link ([^"]+)" href="([^"]+)"([^>]*)><span>([^<]*)</span></a>',
        doc_block,
    )
    first = links[0] if links else None

    specs_count = count_specs_sections(content)
    has_top = "product-content__top" in content
    after_top = ""
    m_top = re.search(r"product-content__top\">(.*?)</div>", content, re.S)
    if m_top:
        after_top = content[m_top.end() :]
    has_standalone_specs = "product-content__specifications" in after_top

    checks = {
        "url": url,
        "label": label,
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "twig_ok": "Twig_Error" not in html,
        "product_content": 'class="product-content"' in html,
        "product_content_grid": "product-content__grid" in content,
        "product_content_card": "product-content__card" in content,
        "no_tabs": 'class="tabs js-tabs"' not in html,
        "no_js_tabs": "js-tabs" not in html,
        "specs_visible": "product-content__specifications" in content,
        "specs_count": specs_count,
        "help_visible": "product-help" in html,
        "related_visible": "rel-products" in html,
        "has_description": "product-content__description" in content,
        "has_documents": "product-content__documents" in content and "docs-list__item" in content,
        "has_top": has_top,
        "has_standalone_specs": has_standalone_specs,
        "has_desc_heading": "product-content__description" in content and ">Описание</h3>" in content,
        "has_specs_heading": "product-content__specifications" in content
        and "section-title__like-h3" in content,
        "has_docs_heading": ">Документы</h3>" in content if "product-content__documents" in content else True,
        "docs_list_preserved": "docs-list" in doc_block and "docs-list__item" in doc_block,
        "docs_link_class": "docs-list__link" in doc_block,
        "pdf_class": bool(first and first[0] == "pdf") if doc_block else True,
        "download_attr": bool(first and "download" in first[2]) if first else True,
        "href_ok": bool(first and first[1].startswith("http")) if first else True,
        "tabs_panel_hook": "tabs__panel is-active" in doc_block if doc_block else True,
        "no_specs_docs_wrapper": "product-content__specs-docs" not in content,
        "sample_link": (
            f'<a class="docs-list__link {first[0]}" href="{first[1]}" download>'
            f"<span>{first[3]}</span></a>"
            if first
            else None
        ),
    }

    if not checks["has_description"]:
        checks["no_empty_desc_block"] = "product-content__description" not in content
    if not checks["has_documents"]:
        checks["no_empty_docs_block"] = "product-content__documents" not in content

    exp = EXPECTED[label]
    for key, want in exp.items():
        checks[f"expect_{key}"] = checks.get(key) == want

    always = [
        "php_ok", "twig_ok", "product_content", "no_tabs", "no_js_tabs",
        "specs_visible", "help_visible", "related_visible",
        "docs_list_preserved", "docs_link_class", "no_specs_docs_wrapper",
        "product_content_grid", "product_content_card",
    ]
    fails = [k for k in always if isinstance(checks.get(k), bool) and not checks[k]]
    fails += [k for k, v in checks.items() if k.startswith("expect_") and not v]

    checks["pass"] = len(fails) == 0
    checks["fails"] = fails
    return checks


def main():
    results = {
        "cases_tested_live": [],
        "cases_not_in_catalog": {
            "case_b_desc_no_docs": "557+ PDP URLs scanned previously; no live SKU without documents — SAFE UNKNOWN",
            "case_d_no_desc_no_docs": "557+ PDP URLs scanned previously; no SKU without description and documents — SAFE UNKNOWN",
        },
        "twig_branches_verified_static": {
            "case_b": "has_desc and not has_docs: description full width + specifications",
            "case_d": "not has_desc and not has_docs: specifications only",
        },
    }
    ok = True
    for label, url in URLS.items():
        case = analyze(label, url)
        ok = ok and case["pass"]
        results["cases_tested_live"].append(case)

    out = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-visual-pass-work\content-visual-pass-qa-result.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(json.dumps(results, ensure_ascii=False, indent=2))
    print("OVERALL:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
