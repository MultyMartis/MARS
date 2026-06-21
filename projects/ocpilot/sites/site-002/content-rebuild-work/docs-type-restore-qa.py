#!/usr/bin/env python3
"""QA — PDP document type logic restore (SPKB-18/7-ВЛ5)."""
import json
import re
import urllib.request

BASE = "https://zpm.new-site.space"
COOKIE = "beget=begetok"
SPKB_URL = (
    BASE + "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/"
    "stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850"
)
OUT = r"C:\AI MARS\projects\ocpilot\sites\site-002\content-rebuild-work\docs-type-restore-qa-result.json"


def fetch(url):
    req = urllib.request.Request(url, headers={"Cookie": COOKIE, "User-Agent": "MARS-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", "replace")


def main():
    html = fetch(SPKB_URL)
    doc_block = ""
    m = re.search(
        r'<section class="product-content__documents">.*?</section>',
        html,
        re.S,
    )
    if m:
        doc_block = m.group(0)

    links = re.findall(
        r'<a class="docs-list__link ([^"]+)" href="([^"]+)"([^>]*)><span>([^<]*)</span></a>',
        doc_block,
    )
    first = links[0] if links else None

    checks = {
        "url": SPKB_URL,
        "php_ok": "Fatal error" not in html and "Parse error" not in html,
        "twig_ok": "Twig_Error" not in html,
        "1_docs_list": "docs-list" in doc_block,
        "2_link_class": "docs-list__link" in doc_block,
        "3_pdf_class": bool(first and first[0] == "pdf"),
        "4_href_ok": bool(first and first[1].startswith("http") and "Product_DOCs" in first[1]),
        "5_download_attr": bool(first and "download" in first[2]),
        "6_clickable_link": bool(first and first[1]),
        "7_css_hook": "tabs__panel is-active" in doc_block,
        "8_product_content": 'class="product-content"' in html,
        "9_no_tabs_ui": 'class="tabs js-tabs"' not in html,
        "10_no_php_twig_errors": "Fatal error" not in html and "Twig_Error" not in html,
    }
    checks["pass"] = all(
        checks[k]
        for k in checks
        if k not in ("url", "pass") and isinstance(checks[k], bool)
    )
    checks["sample_link_html"] = (
        f'<a class="docs-list__link {first[0]}" href="{first[1]}" download>'
        f"<span>{first[3]}</span></a>"
        if first
        else None
    )
    checks["doc_block_snippet"] = doc_block[:800] if doc_block else None

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(checks, f, ensure_ascii=False, indent=2)
    print(json.dumps(checks, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
