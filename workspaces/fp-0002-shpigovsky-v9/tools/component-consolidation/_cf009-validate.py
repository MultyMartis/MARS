#!/usr/bin/env python3
"""FP-0002 V8 CF-009 DOM + selector validation against dist output."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-009-final-form" / "data"
DIST = ROOT / "dist"

PAGES = [
    "index.html",
    "uslugi.html",
    "uslugi-v2.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
]

OLD_PATTERNS = [
    r"home-final-form\.html",
    r"home-final-form",
    r"home-final-form__",
]

SRC_SCAN_DIRS = [ROOT / "src"]


def scan_text(path: Path, patterns: list[str]) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    return {p: len(re.findall(p, text)) for p in patterns}


def validate_dom(html: str) -> dict:
    sections = len(re.findall(r'<section class="final-form', html))
    old = len(re.findall(r"home-final-form", html))
    block = re.search(r'<section class="final-form[^"]*".*?</section>', html, re.DOTALL)
    form_html = block.group(0) if block else ""
    forms = len(re.findall(r'data-lead-form', form_html))
    phone_inputs = len(re.findall(r'data-phone-input', form_html))
    ids = re.findall(r'id="([^"]+)"', form_html)
    duplicate_ids = len(ids) != len(set(ids))
    unresolved = "@@include" in html
    return {
        "neutral_root_count": sections,
        "old_root_count": old,
        "form_count": forms,
        "phone_input_count": phone_inputs,
        "unresolved_include": unresolved,
        "duplicate_ids": duplicate_ids,
        "result": "PASS"
        if sections == 1 and old == 0 and not unresolved and forms >= 1 and not duplicate_ids
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
        "validation_id": "CF-009-DOM-ARIA-VALIDATION",
        "dist_root": str(DIST),
        "pages": dom_rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in dom_rows) else "FAIL",
    }
    (AUDIT / "CF-009-DOM-ARIA-VALIDATION.json").write_text(
        json.dumps(dom_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    old_counts: dict[str, int] = {p: 0 for p in OLD_PATTERNS}
    for base in SRC_SCAN_DIRS:
        for path in base.rglob("*"):
            if path.suffix not in {".html", ".scss", ".js"}:
                continue
            text = path.read_text(encoding="utf-8")
            for p in OLD_PATTERNS:
                if p == r"home-final-form":
                    old_counts[p] += len(
                        re.findall(
                            r"home-final-form(?!-background\.webp)(?!/)",
                            text,
                        )
                    )
                else:
                    old_counts[p] += len(re.findall(p, text))

    neutral_partial_count = len(list((ROOT / "src/partials/sections").glob("final-form.html")))
    neutral_include_consumers = sum(
        1
        for p in (ROOT / "src/pages").glob("*.html")
        if "final-form.html" in p.read_text(encoding="utf-8")
        and "home-final-form.html" not in p.read_text(encoding="utf-8")
    )
    scss_text = (ROOT / "src/scss/style.scss").read_text(encoding="utf-8")
    js_text = (ROOT / "src/js/main.js").read_text(encoding="utf-8")
    selector_payload = {
        "validation_id": "CF-009-SELECTOR-HOOK-VALIDATION",
        "old_partial_references": old_counts[r"home-final-form\.html"],
        "old_root_references": old_counts[r"home-final-form"],
        "old_child_class_references": old_counts[r"home-final-form__"],
        "neutral_partial_count": neutral_partial_count,
        "neutral_include_consumers": neutral_include_consumers,
        "neutral_css_family_count": len(re.findall(r"\.final-form", scss_text)),
        "lead_form_init_count": js_text.count("[data-lead-form]"),
        "page_scoped_overrides": len(re.findall(r"body\.[^\s{]+\s+\.final-form", scss_text)),
        "aliases": len(re.findall(r"home-final-form,\s*\.final-form", scss_text)),
        "old_pattern_totals": old_counts,
        "overall": "FAIL",
    }

    selector_payload["overall"] = (
        "PASS"
        if all(v == 0 for v in old_counts.values())
        and selector_payload["neutral_partial_count"] == 1
        and selector_payload["neutral_include_consumers"] == 5
        and selector_payload["lead_form_init_count"] >= 1
        and selector_payload["page_scoped_overrides"] == 0
        and selector_payload["aliases"] == 0
        else "FAIL"
    )

    (AUDIT / "CF-009-SELECTOR-HOOK-VALIDATION.json").write_text(
        json.dumps(selector_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(json.dumps({"dom": dom_payload["overall"], "selector": selector_payload["overall"]}, indent=2))


if __name__ == "__main__":
    main()
