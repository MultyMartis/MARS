#!/usr/bin/env python3
"""FP-0002 V8 CF-010 DOM structure + selector validation."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-010-clinic-landscape" / "data"
DIST = ROOT / "dist"
SRC = ROOT / "src"

CONSUMERS = [
    ("index.html", 1),
    ("usluga-podrazdel-v1.html", 1),
    ("usluga-konechnaya-v1.html", 1),
]

ALL_PAGES = [
    "index.html",
    "uslugi.html",
    "uslugi-v2.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
]

OLD_PATTERNS = [
    "home-clinic-landscape",
    "partials/sections/home-clinic-landscape.html",
]


def broken_aria(html: str) -> dict:
    broken_labelledby = []
    broken_controls = []
    for m in re.finditer(r'aria-labelledby="([^"]+)"', html):
        for ref in m.group(1).split():
            if f'id="{ref}"' not in html:
                broken_labelledby.append(ref)
    for m in re.finditer(r'aria-controls="([^"]+)"', html):
        if f'id="{m.group(1)}"' not in html:
            broken_controls.append(m.group(1))
    return {
        "broken_aria_labelledby": len(set(broken_labelledby)),
        "broken_aria_controls": len(set(broken_controls)),
    }


def validate_consumer(page: str, expected: int) -> dict:
    html = (DIST / page).read_text(encoding="utf-8")
    old_root = len(re.findall(r'class="[^"]*\bhome-clinic-landscape\b', html))
    neutral_root = len(re.findall(r'class="[^"]*\bclinic-landscape\b', html))
    img_match = re.search(
        r'class="clinic-landscape__image"[^>]*src="([^"]+)"[^>]*alt="([^"]*)"',
        html,
    )
    ids = re.findall(r'id="([^"]+)"', html)
    aria = broken_aria(html)
    return {
        "page": page,
        "expected_component_count": expected,
        "neutral_root_count": neutral_root,
        "old_root_count": old_root,
        "structure_valid": neutral_root == expected and old_root == 0,
        "image_source": img_match.group(1) if img_match else None,
        "alt": img_match.group(2) if img_match else None,
        "ids_unique": len(ids) == len(set(ids)),
        **aria,
        "unresolved_includes": html.count("@@include"),
        "result": "PASS"
        if neutral_root == expected
        and old_root == 0
        and img_match
        and len(ids) == len(set(ids))
        and not aria["broken_aria_labelledby"]
        and not aria["broken_aria_controls"]
        and "@@include" not in html
        else "FAIL",
    }


def scan_old_refs() -> dict:
    hits: list[str] = []
    for path in SRC.rglob("*"):
        if path.suffix not in {".html", ".scss", ".js"}:
            continue
        text = path.read_text(encoding="utf-8")
        for pat in OLD_PATTERNS:
            if pat in text:
                # asset filename exception
                if pat == "home-clinic-landscape" and "shpigovsky-clinic-landscape.webp" in text:
                    if re.search(r"home-clinic-landscape", text.replace("shpigovsky-clinic-landscape.webp", "")):
                        hits.append(f"{path.relative_to(ROOT)}:{pat}")
                elif pat in text:
                    hits.append(f"{path.relative_to(ROOT)}:{pat}")
    partial_count = len(list((SRC / "partials" / "sections").glob("clinic-landscape.html")))
    return {
        "old_active_references": hits,
        "old_active_count": len(hits),
        "neutral_partial_count": partial_count,
        "aliases": 0,
        "asset_path_exceptions": ["assets/img/content/pre-reviews/shpigovsky-clinic-landscape.webp"],
        "result": "PASS" if len(hits) == 0 and partial_count == 1 else "FAIL",
    }


def main() -> None:
    AUDIT.mkdir(parents=True, exist_ok=True)
    dom_rows = [validate_consumer(p, n) for p, n in CONSUMERS]
    dom_payload = {
        "validation_id": "CF-010-DOM-STRUCTURE-VALIDATION",
        "consumers": dom_rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in dom_rows) else "FAIL",
    }
    (AUDIT / "CF-010-DOM-STRUCTURE-VALIDATION.json").write_text(
        json.dumps(dom_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    selector = scan_old_refs()
    scss = (SRC / "scss" / "style.scss").read_text(encoding="utf-8")
    selector["neutral_css_family_count"] = len(re.findall(r"\.clinic-landscape(?:__|\.|\s|\{)", scss))
    (AUDIT / "CF-010-SELECTOR-REFERENCE-VALIDATION.json").write_text(
        json.dumps(selector, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    page_rows = []
    for p in ALL_PAGES:
        html = (DIST / p).read_text(encoding="utf-8")
        ids = re.findall(r'id="([^"]+)"', html)
        from collections import Counter

        dups = {k: v for k, v in Counter(ids).items() if v > 1}
        aria = broken_aria(html)
        page_rows.append(
            {
                "page": p,
                "duplicate_ids": sum(v - 1 for v in dups.values()),
                **aria,
                "unresolved_includes": html.count("@@include"),
                "result": "PASS"
                if not dups and not aria["broken_aria_labelledby"] and "@@include" not in html
                else "FAIL",
            }
        )
    print(
        json.dumps(
            {
                "dom": dom_payload["overall"],
                "selector": selector["result"],
                "page_wide": "PASS" if all(r["result"] == "PASS" for r in page_rows) else "FAIL",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
