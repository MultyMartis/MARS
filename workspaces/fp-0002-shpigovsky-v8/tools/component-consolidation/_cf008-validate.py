#!/usr/bin/env python3
"""FP-0002 V8 CF-008 DOM + selector validation against dist output."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-008-faq" / "data"
DIST = ROOT / "dist"

PAGES = [
    "index.html",
    "uslugi.html",
    "uslugi-v2.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
]

OLD_PATTERNS = [
    r"home-faq\.html",
    r"home-faq",
    r"home-faq__",
    r"initHomeFaq",
]

SRC_SCAN_DIRS = [ROOT / "src"]
EXPECTED_ITEMS = 10


def scan_text(path: Path, patterns: list[str]) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    return {p: len(re.findall(p, text)) for p in patterns}


def validate_dom(html: str) -> dict:
    sections = len(re.findall(r'<section class="faq', html))
    old = len(re.findall(r"home-faq", html))
    faq_block = re.search(r'<section class="faq[^"]*".*?</section>', html, re.DOTALL)
    faq_html = faq_block.group(0) if faq_block else ""
    faq_items = len(re.findall(r"data-accordion-item", faq_html))
    triggers = len(re.findall(r"data-accordion-button", faq_html))
    faq_ids = re.findall(r'id="([^"]+)"', faq_html)
    duplicate_ids = len(faq_ids) != len(set(faq_ids))
    unresolved = "@@include" in html
    return {
        "neutral_root_count": sections,
        "old_root_count": old,
        "faq_count": sections,
        "item_count": faq_items if faq_items else items,
        "trigger_count": triggers,
        "unresolved_include": unresolved,
        "duplicate_ids": duplicate_ids,
        "result": "PASS"
        if sections == 1 and old == 0 and not unresolved and faq_items == EXPECTED_ITEMS and not duplicate_ids
        else "FAIL",
    }


def main() -> None:
    dom_rows: list[dict] = []
    for page in PAGES:
        path = DIST / page
        html = path.read_text(encoding="utf-8")
        row = {"page": page, **validate_dom(html)}
        dom_rows.append(row)

    dom_payload = {
        "validation_id": "CF-008-DOM-ARIA-VALIDATION",
        "dist_root": str(DIST),
        "pages": dom_rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in dom_rows) else "FAIL",
    }
    (AUDIT / "CF-008-DOM-ARIA-VALIDATION.json").write_text(
        json.dumps(dom_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    old_counts: dict[str, int] = {p: 0 for p in OLD_PATTERNS}
    for base in SRC_SCAN_DIRS:
        for path in base.rglob("*"):
            if path.suffix not in {".html", ".scss", ".js"}:
                continue
            counts = scan_text(path, OLD_PATTERNS)
            for k, v in counts.items():
                old_counts[k] += v

    neutral_partial_count = len(list((ROOT / "src/partials/sections").glob("faq.html")))
    neutral_include_consumers = sum(
        1
        for p in (ROOT / "src/pages").glob("*.html")
        if "faq.html" in p.read_text(encoding="utf-8")
        and "home-faq.html" not in p.read_text(encoding="utf-8")
    )
    scss_text = (ROOT / "src/scss/style.scss").read_text(encoding="utf-8")
    js_text = (ROOT / "src/js/main.js").read_text(encoding="utf-8")
    selector_payload = {
        "validation_id": "CF-008-SELECTOR-HOOK-VALIDATION",
        "old_partial_references": old_counts[r"home-faq\.html"],
        "old_root_references": old_counts[r"home-faq"],
        "old_child_class_references": old_counts[r"home-faq__"],
        "old_init_function_references": old_counts[r"initHomeFaq"],
        "neutral_partial_count": neutral_partial_count,
        "neutral_include_consumers": neutral_include_consumers,
        "neutral_css_family_count": len(re.findall(r"\.faq", scss_text)),
        "accordion_init_count": js_text.count("[data-accordion]"),
        "page_scoped_overrides": len(re.findall(r"body\.[^\s{]+\s+\.faq", scss_text)),
        "aliases": len(re.findall(r"home-faq,\s*\.faq", scss_text)),
        "old_pattern_totals": old_counts,
        "overall": "FAIL",
    }

    selector_payload["overall"] = (
        "PASS"
        if all(v == 0 for v in old_counts.values())
        and selector_payload["neutral_partial_count"] == 1
        and selector_payload["neutral_include_consumers"] == 5
        and selector_payload["accordion_init_count"] >= 1
        and selector_payload["page_scoped_overrides"] == 0
        and selector_payload["aliases"] == 0
        else "FAIL"
    )

    (AUDIT / "CF-008-SELECTOR-HOOK-VALIDATION.json").write_text(
        json.dumps(selector_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(json.dumps({"dom": dom_payload["overall"], "selector": selector_payload["overall"]}, indent=2))


if __name__ == "__main__":
    main()
