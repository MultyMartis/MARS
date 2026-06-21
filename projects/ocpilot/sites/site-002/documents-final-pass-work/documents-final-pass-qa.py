#!/usr/bin/env python3
"""QA — PDP documents block final pass."""
import json
import re
import sys
import urllib.request

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"

URL_SPKB = (
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
    "stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
)


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


def analyze_spkb():
    html = fetch(URL_SPKB)
    content = extract_product_content(html)

    doc_block = ""
    m = re.search(
        r'<section class="product-content__documents[^"]*".*?</section>',
        content,
        re.S,
    )
    if m:
        doc_block = m.group(0)

    link_match = re.search(
        r'<a class="docs-list__link ([^"]+)" href="([^"]+)"([^>]*)>',
        doc_block,
    )

    checks = {
        "url": URL_SPKB,
        "sku": "SPKB-18/7-ВЛ5",
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "twig_ok": "Twig_Error" not in html,
        "product_content_grid_with_side": "product-content__grid--with-side" in content,
        "has_side": "product-content__side" in content,
        "has_documents_section": "product-content__documents" in content,
        "docs_heading_h2": ">Документы</h2>" in doc_block,
        "docs_list_preserved": "docs-list" in doc_block,
        "docs_list_item": "docs-list__item" in doc_block,
        "docs_link_class": "docs-list__link" in doc_block,
        "file_main_structure": "docs-list__file-main" in doc_block,
        "file_title_structure": "docs-list__file-title" in doc_block,
        "file_type_structure": "docs-list__file-type" in doc_block,
        "download_icon": "docs-list__download" in doc_block and "fa-download" in doc_block,
        "docs_note": "product-content__docs-note" in doc_block,
        "contact_link_hook": 'data-src="#zpmFbQuestion"' in doc_block and "свяжитесь с нами" in doc_block,
        "no_tabs_panel": "tabs__panel" not in doc_block,
        "help_visible": "product-help" in html,
        "related_visible": "rel-products" in html,
        "mobile_stack_css": "product-content__side" in open(
            r"C:\AI MARS\projects\ocpilot\sites\site-002\documents-final-pass-work\style.css",
            encoding="utf-8",
        ).read(),
    }

    if link_match:
        checks["pdf_class"] = link_match.group(1) == "pdf"
        checks["href_ok"] = link_match.group(2).startswith("http")
        checks["download_attr"] = "download" in link_match.group(3)
        checks["sample_href"] = link_match.group(2)
    else:
        checks["pdf_class"] = False
        checks["href_ok"] = False
        checks["download_attr"] = False
        checks["sample_href"] = None

    fails = [k for k, v in checks.items() if isinstance(v, bool) and not v]
    checks["pass"] = len(fails) == 0
    checks["fails"] = fails
    return checks


def verify_empty_branch_static():
    twig_path = r"C:\AI MARS\projects\ocpilot\sites\site-002\documents-final-pass-work\producttabs.twig"
    with open(twig_path, encoding="utf-8") as f:
        twig = f.read()
    return {
        "else_branch_present": "{% else %}" in twig and "product-content__docs-empty" in twig,
        "empty_cta_hook": 'data-src="#zpmFbQuestion"' in twig and "Запросить документы" in twig,
        "sidebar_always": "product-content__grid--with-side" in twig and "{% if documents %}" in twig,
        "aside_always": twig.count("product-content__side") == 1,
    }


def main():
    spkb = analyze_spkb()
    empty_static = verify_empty_branch_static()

    results = {
        "case_a_with_documents_live": spkb,
        "case_b_no_documents_live": {
            "status": "SAFE UNKNOWN",
            "note": "557+ PDP URLs scanned previously; no live SKU without documents found in catalog",
        },
        "case_b_empty_branch_static": empty_static,
        "twig_empty_checks_pass": all(empty_static.values()),
    }

    ok = spkb["pass"] and results["twig_empty_checks_pass"]
    out = r"C:\AI MARS\projects\ocpilot\sites\site-002\documents-final-pass-work\documents-final-pass-qa-result.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(json.dumps(results, ensure_ascii=False, indent=2))
    print("OVERALL:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
