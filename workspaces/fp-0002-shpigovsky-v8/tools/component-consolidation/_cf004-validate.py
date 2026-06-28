#!/usr/bin/env python3
"""FP-0002 V8 CF-004 DOM + selector validation against dist output."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-004-founder-quote" / "data"
DIST = ROOT / "dist"

PAGES = [
    "index.html",
    "uslugi-v2.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
    "uslugi.html",
]

OLD_PATTERNS = [
    r"home-founder-quote\.html",
    r"home-founder-quote",
    r"home-founder-quote__",
    r"home-founder-quote-label",
]

SRC_SCAN_DIRS = [
    ROOT / "src",
]


def scan_text(path: Path, patterns: list[str]) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    return {p: len(re.findall(p, text)) for p in patterns}


def validate_dom(html: str) -> dict:
    neutral = len(re.findall(r'class="[^"]*\bfounder-quote\b', html))
    old = len(re.findall(r"home-founder-quote", html))
    quote_sections = len(re.findall(r'<section class="founder-quote', html))
    label_ids = re.findall(r'id="founder-quote-label"', html)
    aria = 'aria-labelledby="founder-quote-label"' in html
    cta = "founder-quote__cta" in html and "data-modal-open" in html
    unresolved = "@@include" in html
    return {
        "neutral_root_count": quote_sections,
        "old_root_count": old,
        "quote_count": quote_sections,
        "duplicate_label_ids": len(label_ids) != 1,
        "label_id_count": len(label_ids),
        "aria_valid": aria and len(label_ids) == 1,
        "cta_preserved": cta,
        "unresolved_include": unresolved,
        "result": "PASS"
        if quote_sections == 1 and old == 0 and not unresolved and len(label_ids) == 1 and aria and cta
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
        "validation_id": "CF-004-DOM-VALIDATION",
        "dist_root": str(DIST),
        "pages": dom_rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in dom_rows) else "FAIL",
    }
    (AUDIT / "CF-004-DOM-VALIDATION.json").write_text(
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

    neutral_partial_count = len(list((ROOT / "src/partials/sections").glob("founder-quote.html")))
    neutral_include_consumers = sum(
        1
        for p in (ROOT / "src/pages").glob("*.html")
        if "founder-quote.html" in p.read_text(encoding="utf-8")
    )
    scss_text = (ROOT / "src/scss/style.scss").read_text(encoding="utf-8")
    selector_payload = {
        "validation_id": "CF-004-SELECTOR-VALIDATION",
        "old_partial_references": old_counts[r"home-founder-quote\.html"],
        "old_root_references": old_counts[r"home-founder-quote"],
        "old_child_class_references": old_counts[r"home-founder-quote__"],
        "old_label_references": old_counts[r"home-founder-quote-label"],
        "neutral_partial_count": neutral_partial_count,
        "neutral_include_consumers": neutral_include_consumers,
        "neutral_css_family_count": len(re.findall(r"\.founder-quote", scss_text)),
        "page_scoped_overrides": len(re.findall(r"body\.[^\s{]+\s+\.founder-quote", scss_text)),
        "aliases": len(re.findall(r"home-founder-quote,\s*\.founder-quote", scss_text)),
        "old_pattern_totals": old_counts,
        "overall": "FAIL",
    }
    selector_payload["overall"] = (
        "PASS"
        if all(v == 0 for v in old_counts.values())
        and selector_payload["neutral_partial_count"] == 1
        and selector_payload["neutral_include_consumers"] == 5
        and selector_payload["neutral_css_family_count"] >= 1
        and selector_payload["page_scoped_overrides"] == 0
        and selector_payload["aliases"] == 0
        else "FAIL"
    )

    (AUDIT / "CF-004-SELECTOR-VALIDATION.json").write_text(
        json.dumps(selector_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(json.dumps({"dom": dom_payload["overall"], "selector": selector_payload["overall"]}, indent=2))


if __name__ == "__main__":
    main()
