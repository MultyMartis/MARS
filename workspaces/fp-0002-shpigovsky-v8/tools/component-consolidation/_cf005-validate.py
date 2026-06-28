#!/usr/bin/env python3
"""FP-0002 V8 CF-005 DOM + selector validation against dist output."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-005-specialists" / "data"
DIST = ROOT / "dist"

PAGES = [
    "index.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
]

OLD_PATTERNS = [
    r"home-specialists\.html",
    r"home-specialists",
    r"home-specialists__",
]

SRC_SCAN_DIRS = [
    ROOT / "src",
]


ASSET_PATH_PREFIX = "assets/img/content/home-specialists/"


def strip_asset_paths(text: str) -> str:
    return text.replace(ASSET_PATH_PREFIX, "assets/img/content/_specialists_assets/")


def scan_text(path: Path, patterns: list[str]) -> dict[str, int]:
    text = strip_asset_paths(path.read_text(encoding="utf-8"))
    return {p: len(re.findall(p, text)) for p in patterns}


def validate_dom(html: str) -> dict:
    html_scan = strip_asset_paths(html)
    neutral = len(re.findall(r'class="[^"]*\bspecialists\b', html_scan))
    old = len(re.findall(r"home-specialists", html_scan))
    sections = len(re.findall(r'<section class="specialists', html_scan))
    slides = len(re.findall(r'specialists__card swiper-slide', html_scan))
    slider = "data-specialists-slider" in html
    pagination = "data-specialists-pagination" in html
    unresolved = "@@include" in html
    return {
        "neutral_root_count": sections,
        "old_root_count": old,
        "specialists_count": sections,
        "slide_count": slides,
        "slider_hook": slider,
        "pagination_hook": pagination,
        "unresolved_include": unresolved,
        "result": "PASS"
        if sections == 1 and old == 0 and not unresolved and slides == 5 and slider and pagination
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
        "validation_id": "CF-005-DOM-VALIDATION",
        "dist_root": str(DIST),
        "pages": dom_rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in dom_rows) else "FAIL",
    }
    (AUDIT / "CF-005-DOM-VALIDATION.json").write_text(
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

    neutral_partial_count = len(list((ROOT / "src/partials/sections").glob("specialists.html")))
    neutral_include_consumers = sum(
        1
        for p in (ROOT / "src/pages").glob("*.html")
        if "specialists.html" in p.read_text(encoding="utf-8")
        and "home-specialists.html" not in p.read_text(encoding="utf-8")
    )
    scss_text = (ROOT / "src/scss/style.scss").read_text(encoding="utf-8")
    js_text = (ROOT / "src/js/main.js").read_text(encoding="utf-8")
    selector_payload = {
        "validation_id": "CF-005-SELECTOR-HOOK-VALIDATION",
        "old_partial_references": old_counts[r"home-specialists\.html"],
        "old_root_references": old_counts[r"home-specialists"],
        "old_child_class_references": old_counts[r"home-specialists__"],
        "neutral_partial_count": neutral_partial_count,
        "neutral_include_consumers": neutral_include_consumers,
        "neutral_css_family_count": len(re.findall(r"\.specialists", scss_text)),
        "slider_init_count": js_text.count("[data-specialists-slider]"),
        "page_scoped_overrides": len(re.findall(r"body\.[^\s{]+\s+\.specialists", scss_text)),
        "aliases": len(re.findall(r"home-specialists,\s*\.specialists", scss_text)),
        "old_pattern_totals": old_counts,
        "overall": "FAIL",
    }
    selector_payload["overall"] = (
        "PASS"
        if all(v == 0 for v in old_counts.values())
        and selector_payload["neutral_partial_count"] == 1
        and selector_payload["neutral_include_consumers"] == 3
        and selector_payload["neutral_css_family_count"] >= 1
        and selector_payload["slider_init_count"] >= 1
        and selector_payload["page_scoped_overrides"] == 0
        and selector_payload["aliases"] == 0
        else "FAIL"
    )

    (AUDIT / "CF-005-SELECTOR-HOOK-VALIDATION.json").write_text(
        json.dumps(selector_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(json.dumps({"dom": dom_payload["overall"], "selector": selector_payload["overall"]}, indent=2))


if __name__ == "__main__":
    main()
