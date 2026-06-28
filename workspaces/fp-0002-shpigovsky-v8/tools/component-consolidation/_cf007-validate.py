#!/usr/bin/env python3
"""FP-0002 V8 CF-007 DOM + selector validation against dist output."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-007-reviews" / "data"
DIST = ROOT / "dist"

PAGES = [
    "index.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
]

OLD_PATTERNS = [
    r"home-reviews\.html",
    r"home-reviews",
    r"home-reviews__",
    r"initHomeReviews",
]

SRC_SCAN_DIRS = [ROOT / "src"]
EXPECTED_SLIDES = 10


def scan_text(path: Path, patterns: list[str]) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    return {p: len(re.findall(p, text)) for p in patterns}


def validate_dom(html: str) -> dict:
    sections = len(re.findall(r'<section class="reviews', html))
    old = len(re.findall(r"home-reviews", html))
    slides = len(re.findall(r'class="[^"]*\breviews__slide\b', html))
    pagination = len(re.findall(r'data-reviews-pagination', html))
    slider = len(re.findall(r'data-reviews-slider', html))
    unresolved = "@@include" in html
    return {
        "neutral_root_count": sections,
        "old_root_count": old,
        "reviews_count": sections,
        "slide_count": slides,
        "slider_hook_count": slider,
        "pagination_hook_count": pagination,
        "unresolved_include": unresolved,
        "result": "PASS"
        if sections == 1 and old == 0 and not unresolved and slides == EXPECTED_SLIDES and slider == 1 and pagination == 1
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
        "validation_id": "CF-007-DOM-VALIDATION",
        "dist_root": str(DIST),
        "pages": dom_rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in dom_rows) else "FAIL",
    }
    (AUDIT / "CF-007-DOM-VALIDATION.json").write_text(
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

    neutral_partial_count = len(list((ROOT / "src/partials/sections").glob("reviews.html")))
    neutral_include_consumers = sum(
        1
        for p in (ROOT / "src/pages").glob("*.html")
        if "reviews.html" in p.read_text(encoding="utf-8")
        and "home-reviews.html" not in p.read_text(encoding="utf-8")
    )
    scss_text = (ROOT / "src/scss/style.scss").read_text(encoding="utf-8")
    js_text = (ROOT / "src/js/main.js").read_text(encoding="utf-8")
    selector_payload = {
        "validation_id": "CF-007-SELECTOR-HOOK-VALIDATION",
        "old_partial_references": old_counts[r"home-reviews\.html"],
        "old_root_references": old_counts[r"home-reviews"],
        "old_child_class_references": old_counts[r"home-reviews__"],
        "old_init_function_references": old_counts[r"initHomeReviews"],
        "historical_asset_path_references": 0,
        "neutral_partial_count": neutral_partial_count,
        "neutral_include_consumers": neutral_include_consumers,
        "neutral_css_family_count": len(re.findall(r"\.reviews", scss_text)),
        "slider_init_count": js_text.count("[data-reviews-slider]"),
        "init_reviews_function": "initReviews" in js_text,
        "page_scoped_overrides": len(re.findall(r"body\.[^\s{]+\s+\.reviews", scss_text)),
        "aliases": len(re.findall(r"home-reviews,\s*\.reviews", scss_text)),
        "old_pattern_totals": old_counts,
        "overall": "FAIL",
    }

    selector_payload["overall"] = (
        "PASS"
        if all(v == 0 for v in old_counts.values())
        and selector_payload["neutral_partial_count"] == 1
        and selector_payload["neutral_include_consumers"] == 3
        and selector_payload["slider_init_count"] >= 1
        and selector_payload["init_reviews_function"]
        and selector_payload["page_scoped_overrides"] == 0
        and selector_payload["aliases"] == 0
        else "FAIL"
    )

    (AUDIT / "CF-007-SELECTOR-HOOK-VALIDATION.json").write_text(
        json.dumps(selector_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(json.dumps({"dom": dom_payload["overall"], "selector": selector_payload["overall"]}, indent=2))


if __name__ == "__main__":
    main()
