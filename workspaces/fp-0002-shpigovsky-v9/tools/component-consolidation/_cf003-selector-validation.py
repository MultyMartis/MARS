#!/usr/bin/env python3
"""FP-0002 V8 CF-003 final selector validation."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-003-upper-navigation" / "data"
SCSS = ROOT / "src" / "scss" / "style.scss"
SRC = ROOT / "src"

OLD_CLASSES = [
    "page-uslugi-v2__upper-nav",
    "page-service-subdivision-v1__upper-nav",
    "page-service-leaf-v1__upper-nav",
]

TARGET_PAGES = [
    "src/pages/uslugi-v2.html",
    "src/pages/usluga-podrazdel-v1.html",
    "src/pages/usluga-konechnaya-v1.html",
]

PAGE_SCOPED_BC = re.compile(
    r"\.page-(?:uslugi-v2|service-subdivision-v1|service-leaf-v1)\s+\.breadcrumbs"
)
PAGE_SCOPED_SN = re.compile(
    r"\.page-(?:uslugi-v2|service-subdivision-v1|service-leaf-v1)\s+\.services-page-subnav"
)


def count_in_tree(pattern: str, root: Path) -> dict[str, int]:
    rx = re.compile(pattern)
    counts: dict[str, int] = {}
    for path in root.rglob("*"):
        if path.suffix not in {".html", ".scss", ".js", ".md", ".json"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        n = len(rx.findall(text))
        if n:
            counts[rel] = n
    return counts


def main() -> None:
    scss = SCSS.read_text(encoding="utf-8")
    old_counts = {cls: count_in_tree(re.escape(cls), SRC) for cls in OLD_CLASSES}

    internal_include_pages = []
    for rel in TARGET_PAGES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        internal_include_pages.append(
            {
                "file": rel,
                "uses_internal_page_nav": "partials/components/internal-page-nav.html" in text,
            }
        )

    canonical_css_blocks = len(re.findall(r"\.internal-page-nav\b", scss))
    page_scoped_bc = PAGE_SCOPED_BC.findall(scss)
    page_scoped_sn = PAGE_SCOPED_SN.findall(scss)
    dual_activation = len(
        re.findall(
            r"body\.page-(?:uslugi-v2|service-subdivision-v1|service-leaf-v1)[^{]*\.internal-page-nav",
            scss,
        )
    )

    issues = []
    for cls, hits in old_counts.items():
        if hits:
            issues.append(f"{cls} still present: {hits}")
    if not all(p["uses_internal_page_nav"] for p in internal_include_pages):
        issues.append("not all target pages include internal-page-nav partial")
    if page_scoped_bc:
        issues.append(f"page-scoped breadcrumbs overrides: {page_scoped_bc}")
    if page_scoped_sn:
        issues.append(f"page-scoped subnav overrides: {page_scoped_sn}")
    if dual_activation:
        issues.append("dual body/page activation for internal-page-nav")

    report = {
        "overall": "PASS" if not issues else "FAIL",
        "old_wrapper_counts": old_counts,
        "old_wrapper_total": sum(sum(v.values()) for v in old_counts.values()),
        "canonical_partial": "src/partials/components/internal-page-nav.html",
        "canonical_class": "internal-page-nav",
        "target_pages": internal_include_pages,
        "canonical_css_selector_occurrences": canonical_css_blocks,
        "page_scoped_breadcrumbs_overrides": page_scoped_bc,
        "page_scoped_subnav_overrides": page_scoped_sn,
        "dual_body_page_activation": dual_activation,
        "compatibility_aliases": count_in_tree(r"upper-nav", SRC),
        "issues": issues,
    }
    (AUDIT / "CF-003-FINAL-SELECTOR-VALIDATION.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
