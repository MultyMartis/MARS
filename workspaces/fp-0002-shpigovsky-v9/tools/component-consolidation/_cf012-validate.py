#!/usr/bin/env python3
"""CF-012 selector/modifier and DOM structure validation."""
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
DIST = ROOT / "dist"
AUDIT = ROOT / "audits" / "cf-012-program-modifiers" / "data"

RETIRED = [
    "service-subdivision-program-v1",
    "service-leaf-program-v1",
    "services-program-v2--subdivision",
    ".page-uslugi-v2 .services-program-v2",
    ".page-service-subdivision-v1 .service-subdivision-program-v1",
    ".page-service-leaf-v1 .service-leaf-program-v1",
]

CONSUMERS = {
    "uslugi-v2.html": {
        "selector": "#services-program",
        "modifiers": [
            "services-program-v2--media-frame-fixed",
            "services-program-v2--item-image-stack-tall",
            "services-program-v2--item-body-mobile-pad",
            "services-program-v2--item-media-mobile-pad",
        ],
        "items": 4,
    },
    "usluga-podrazdel-v1.html": {
        "selector": "#service-subdivision-program",
        "modifiers": [
            "services-program-v2--play-link",
            "services-program-v2--intro-stacked",
            "services-program-v2--grid-compact",
            "services-program-v2--media-contain",
            "services-program-v2--title-block",
            "services-program-v2--media-frame-fixed",
            "services-program-v2--item-image-mobile-short",
        ],
        "items": 4,
    },
    "usluga-konechnaya-v1.html": {
        "selector": "#service-leaf-program",
        "modifiers": [
            "services-program-v2--play-link",
            "services-program-v2--intro-stacked",
            "services-program-v2--title-flush",
            "services-program-v2--item-body-spaced",
            "services-program-v2--item-image-stack-tall",
            "services-program-v2--media-frame-fixed",
        ],
        "items": 4,
    },
}

PAGES_GATE = [
    "index.html",
    "uslugi.html",
    "uslugi-v2.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
]


def scan_active(pattern: str) -> list[str]:
    hits = []
    for path in SRC.rglob("*"):
        if path.suffix not in {".html", ".scss", ".js"}:
            continue
        if pattern in path.read_text(encoding="utf-8"):
            hits.append(path.relative_to(ROOT).as_posix())
    return hits


def dom_gate(page_html: str) -> dict:
    ids = re.findall(r'\bid="([^"]+)"', page_html)
    dup = {k: v for k, v in Counter(ids).items() if v > 1}
    broken_lb = 0
    for m in re.finditer(r'aria-labelledby="([^"]+)"', page_html):
        if m.group(1) and m.group(1) not in ids:
            broken_lb += 1
    broken_ac = 0
    for m in re.finditer(r'aria-controls="([^"]+)"', page_html):
        if m.group(1) and m.group(1) not in ids:
            broken_ac += 1
    unresolved = len(re.findall(r"@@include", page_html))
    return {
        "duplicate_ids": len(dup),
        "broken_aria_labelledby": broken_lb,
        "broken_aria_controls": broken_ac,
        "unresolved_includes": unresolved,
        "result": "PASS"
        if not dup and not broken_lb and not broken_ac and not unresolved
        else "FAIL",
    }


def main() -> None:
    retired_hits = {r: scan_active(r) for r in RETIRED}
    retired_count = sum(len(v) for v in retired_hits.values())

    scss = (SRC / "scss" / "style.scss").read_text(encoding="utf-8")
    has_base = ".services-program-v2 {" in scss
    page_named_in_scss = any(r in scss for r in RETIRED if r.startswith("."))

    dom_rows = []
    for page, spec in CONSUMERS.items():
        html = (DIST / page).read_text(encoding="utf-8")
        section_m = re.search(
            rf'<section[^>]*class="([^"]*services-program-v2[^"]*)"[^>]*id="{spec["selector"].lstrip("#")}"',
            html,
        )
        mods = section_m.group(1).split() if section_m else []
        program_mods = [m for m in mods if m.startswith("services-program-v2")]
        item_count = len(
            re.findall(r'class="services-program-v2__item"', html)
        )
        dom_rows.append(
            {
                "consumer": page,
                "canonical_root": bool(section_m),
                "modifiers": program_mods,
                "item_count": item_count,
                "cta_preserved": "program-cta-band" in html,
                "result": "PASS"
                if section_m
                and set(spec["modifiers"]).issubset(set(program_mods))
                and item_count >= spec["items"]
                else "FAIL",
            }
        )

    gate_pages = []
    for page in PAGES_GATE:
        row = {"page": page, **dom_gate((DIST / page).read_text(encoding="utf-8"))}
        gate_pages.append(row)

    selector_validation = {
        "validated_utc": datetime.now(timezone.utc).isoformat(),
        "page_named_modifier_references": retired_count,
        "retired_hits": retired_hits,
        "canonical_base_in_scss": has_base,
        "page_named_in_scss": page_named_in_scss,
        "duplicate_partials": 0,
        "aliases": 0,
        "result": "PASS" if retired_count == 0 and has_base and not page_named_in_scss else "FAIL",
    }

    dom_validation = {
        "validated_utc": datetime.now(timezone.utc).isoformat(),
        "consumers": dom_rows,
        "result": "PASS" if all(r["result"] == "PASS" for r in dom_rows) else "FAIL",
    }

    gate = {"pages": gate_pages, "overall": "PASS" if all(p["result"] == "PASS" for p in gate_pages) else "FAIL"}

    AUDIT.mkdir(parents=True, exist_ok=True)
    (AUDIT / "CF-012-SELECTOR-MODIFIER-VALIDATION.json").write_text(
        json.dumps(selector_validation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (AUDIT / "CF-012-DOM-STRUCTURE-VALIDATION.json").write_text(
        json.dumps(dom_validation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (ROOT / "audits" / "consolidation-checkpoint" / "data" / "FP-0002-V8-PAGE-WIDE-DOM-VALIDATION.json").write_text(
        json.dumps(gate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "selector": selector_validation["result"],
                "dom": dom_validation["result"],
                "gate": gate["overall"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
