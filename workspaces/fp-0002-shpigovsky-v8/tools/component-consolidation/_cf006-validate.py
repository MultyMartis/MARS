#!/usr/bin/env python3
"""FP-0002 V8 CF-006 DOM + selector validation against dist output."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-006-comfort" / "data"
DIST = ROOT / "dist"

PAGES = [
    "index.html",
    "uslugi.html",
    "uslugi-v2.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
]

OLD_PATTERNS = [
    r"home-comfort\.html",
    r"home-comfort",
    r"home-comfort__",
]

SRC_SCAN_DIRS = [ROOT / "src"]

ASSET_PATH_PREFIX = "assets/img/content/home-comfort/"


def strip_asset_paths(text: str) -> str:
    return text.replace(ASSET_PATH_PREFIX, "assets/img/content/_comfort_assets/")


def scan_text(path: Path, patterns: list[str]) -> dict[str, int]:
    text = strip_asset_paths(path.read_text(encoding="utf-8"))
    return {p: len(re.findall(p, text)) for p in patterns}


def validate_dom(html: str) -> dict:
    html_scan = strip_asset_paths(html)
    sections = len(re.findall(r'<section class="comfort', html_scan))
    old = len(re.findall(r"home-comfort", html_scan))
    items = len(re.findall(r'class="[^"]*\bcomfort__gallery-item\b', html_scan))
    links = len(re.findall(r'data-fancybox="comfort"', html_scan))
    unresolved = "@@include" in html
    return {
        "neutral_root_count": sections,
        "old_root_count": old,
        "comfort_count": sections,
        "item_count": items,
        "gallery_link_count": links,
        "gallery_group": "comfort" if 'data-fancybox="comfort"' in html_scan else None,
        "unresolved_include": unresolved,
        "result": "PASS"
        if sections == 1 and old == 0 and not unresolved and items == 7 and links == 6
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
        "validation_id": "CF-006-DOM-VALIDATION",
        "dist_root": str(DIST),
        "pages": dom_rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in dom_rows) else "FAIL",
    }
    (AUDIT / "CF-006-DOM-VALIDATION.json").write_text(
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

    neutral_partial_count = len(list((ROOT / "src/partials/sections").glob("comfort.html")))
    neutral_include_consumers = sum(
        1
        for p in (ROOT / "src/pages").glob("*.html")
        if "comfort.html" in p.read_text(encoding="utf-8")
        and "home-comfort.html" not in p.read_text(encoding="utf-8")
    )
    scss_text = strip_asset_paths((ROOT / "src/scss/style.scss").read_text(encoding="utf-8"))
    js_text = (ROOT / "src/js/main.js").read_text(encoding="utf-8")
    selector_payload = {
        "validation_id": "CF-006-SELECTOR-HOOK-VALIDATION",
        "old_partial_references": old_counts[r"home-comfort\.html"],
        "old_root_references": old_counts[r"home-comfort"],
        "old_child_class_references": old_counts[r"home-comfort__"],
        "historical_asset_path_references": len(
            re.findall(r"assets/img/content/home-comfort/", (ROOT / "src").read_text() if False else "")
        ),
        "neutral_partial_count": neutral_partial_count,
        "neutral_include_consumers": neutral_include_consumers,
        "neutral_css_family_count": len(re.findall(r"\.comfort", scss_text)),
        "fancybox_init_count": js_text.count('[data-fancybox="comfort"]'),
        "page_scoped_overrides": len(re.findall(r"body\.[^\s{]+\s+\.comfort", scss_text)),
        "aliases": len(re.findall(r"home-comfort,\s*\.comfort", scss_text)),
        "old_pattern_totals": old_counts,
        "overall": "FAIL",
    }
    asset_refs = 0
    for path in (ROOT / "src").rglob("*"):
        if path.suffix in {".html", ".scss", ".js"}:
            asset_refs += path.read_text(encoding="utf-8").count("assets/img/content/home-comfort/")
    selector_payload["historical_asset_path_references"] = asset_refs

    selector_payload["overall"] = (
        "PASS"
        if all(v == 0 for v in old_counts.values())
        and selector_payload["neutral_partial_count"] == 1
        and selector_payload["neutral_include_consumers"] == 5
        and selector_payload["neutral_css_family_count"] >= 1
        and selector_payload["fancybox_init_count"] >= 1
        and selector_payload["page_scoped_overrides"] == 0
        and selector_payload["aliases"] == 0
        else "FAIL"
    )

    (AUDIT / "CF-006-SELECTOR-HOOK-VALIDATION.json").write_text(
        json.dumps(selector_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(json.dumps({"dom": dom_payload["overall"], "selector": selector_payload["overall"]}, indent=2))


if __name__ == "__main__":
    main()
