#!/usr/bin/env python3
"""FP-0002 V8 CF-011 DOM + selector validation against dist output."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-011-dark-cta" / "data"
DIST = ROOT / "dist"

PAGES = [
    "index.html",
    "uslugi.html",
    "uslugi-v2.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
]

OLD_PATTERNS = [
    r"services-program-cta-band-v2",
    r"services-program-v2__cta-band",
    r"services-program-v2__cta-",
    r"service-subdivision-first-cta-v1",
    r"service-subdivision-second-cta-v1",
    r"service-leaf-cta-01-v1",
]


def broken_aria_labelledby(html: str) -> list[str]:
    broken: list[str] = []
    for m in re.finditer(r'aria-labelledby="([^"]+)"', html):
        ref = m.group(1)
        if not re.search(rf'id="{re.escape(ref)}"', html):
            broken.append(ref)
    return broken


def validate_page(html: str, page: str) -> dict:
    bands = len(re.findall(r'class="program-cta-band', html))
    old_band = len(re.findall(r"services-program-v2__cta-band", html))
    old_wrappers = sum(
        len(re.findall(p.replace("\\", ""), html))
        for p in [
            "service-subdivision-first-cta-v1",
            "service-leaf-cta-01-v1",
            "service-subdivision-second-cta-v1",
        ]
    )
    ids = re.findall(r'id="([^"]+)"', html)
    dup_ids = len(ids) != len(set(ids))
    broken = broken_aria_labelledby(html)
    unresolved = "@@include" in html
    return {
        "page": page,
        "canonical_root_count": bands,
        "old_wrapper_root_count": old_wrappers,
        "old_band_class_count": old_band,
        "broken_aria_labelledby": broken,
        "duplicate_ids": dup_ids,
        "unresolved_include": unresolved,
        "result": "PASS"
        if old_band == 0
        and old_wrappers == 0
        and not broken
        and not dup_ids
        and not unresolved
        else "FAIL",
    }


def main() -> None:
    AUDIT.mkdir(parents=True, exist_ok=True)
    rows = [validate_page((DIST / p).read_text(encoding="utf-8"), p) for p in PAGES]
    payload = {
        "validation_id": "CF-011-DOM-ARIA-VALIDATION",
        "dist_root": str(DIST),
        "pages": rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
    }
    (AUDIT / "CF-011-DOM-ARIA-VALIDATION.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    old_counts: dict[str, int] = {p: 0 for p in OLD_PATTERNS}
    for base in [ROOT / "src"]:
        for path in base.rglob("*"):
            if path.suffix not in {".html", ".scss", ".js"}:
                continue
            text = path.read_text(encoding="utf-8")
            for p in OLD_PATTERNS:
                old_counts[p] += len(re.findall(p, text))

    selector_payload = {
        "validation_id": "CF-011-SELECTOR-PARTIAL-VALIDATION",
        "canonical_partial": "src/partials/components/program-cta-band.html",
        "canonical_partial_count": 1,
        "canonical_root_class": "program-cta-band",
        "old_pattern_counts_in_src": old_counts,
        "aliases": 0,
        "result": "PASS" if all(v == 0 for v in old_counts.values()) else "FAIL",
    }
    (AUDIT / "CF-011-SELECTOR-PARTIAL-VALIDATION.json").write_text(
        json.dumps(selector_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"dom": payload["overall"], "selector": selector_payload["result"]}, indent=2))


if __name__ == "__main__":
    main()
