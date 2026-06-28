#!/usr/bin/env python3
"""FP-0002 V8 CF-003 DOM validation against built dist HTML."""
from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
AUDIT = ROOT / "audits" / "cf-003-upper-navigation" / "data"

PAGES = [
    ("services-hub", "uslugi-v2.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
]

OLD_WRAPPERS = [
    "page-uslugi-v2__upper-nav",
    "page-service-subdivision-v1__upper-nav",
    "page-service-leaf-v1__upper-nav",
]


class NavCounter(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.internal_page_nav = 0
        self.breadcrumbs = 0
        self.services_subnav = 0
        self.nav_total = 0
        self.ul_depth = 0
        self.nested_ul_in_ul = False
        self.empty_nav = False
        self.in_nav = False
        self.nav_has_content = False
        self.aria_current = False
        self.breadcrumbs_aria: str | None = None
        self.subnav_aria: str | None = None
        self.issues: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        cls = attr.get("class", "") or ""
        if tag == "div" and "internal-page-nav" in cls.split():
            self.internal_page_nav += 1
        if tag == "nav":
            self.nav_total += 1
            self.in_nav = True
            self.nav_has_content = False
            if "breadcrumbs" in cls.split():
                self.breadcrumbs += 1
                self.breadcrumbs_aria = attr.get("aria-label")
            if "services-page-subnav" in cls.split():
                self.services_subnav += 1
                self.subnav_aria = attr.get("aria-label")
        if tag == "ul":
            if self.ul_depth > 0:
                self.nested_ul_in_ul = True
            self.ul_depth += 1
        if attr.get("aria-current") == "page":
            self.aria_current = True
        if tag in {"a", "span", "li"}:
            self.nav_has_content = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "ul" and self.ul_depth:
            self.ul_depth -= 1
        if tag == "nav":
            if self.in_nav and not self.nav_has_content:
                self.empty_nav = True
            self.in_nav = False


def validate_page(page_id: str, rel: str) -> dict:
    path = DIST / rel
    html = path.read_text(encoding="utf-8")
    issues: list[str] = []

    if "@@" in html:
        issues.append("unexpanded @@ token")
    if re.search(r"&lt;(li|a|nav|ul)", html):
        issues.append("escaped HTML in output")
    for old in OLD_WRAPPERS:
        if old in html:
            issues.append(f"legacy wrapper present: {old}")

    parser = NavCounter()
    parser.feed(html)

    if parser.internal_page_nav != 1:
        issues.append(f"internal-page-nav count={parser.internal_page_nav}")
    if parser.breadcrumbs != 1:
        issues.append(f"breadcrumbs count={parser.breadcrumbs}")
    if parser.services_subnav != 1:
        issues.append(f"services-page-subnav count={parser.services_subnav}")
    if not parser.aria_current:
        issues.append("missing aria-current on breadcrumb")
    if parser.breadcrumbs_aria != "Хлебные крошки":
        issues.append(f"breadcrumbs aria-label={parser.breadcrumbs_aria!r}")
    if parser.subnav_aria != "Разделы страницы услуг":
        issues.append(f"subnav aria-label={parser.subnav_aria!r}")
    if parser.nested_ul_in_ul:
        issues.append("nested ul inside ul")
    if parser.empty_nav:
        issues.append("empty nav element")

    subnav_links = len(re.findall(r'class="services-page-subnav__link"', html))
    if subnav_links < 1:
        issues.append("no subnav links")

    return {
        "page_id": page_id,
        "file": rel,
        "internal_page_nav_count": parser.internal_page_nav,
        "breadcrumbs_count": parser.breadcrumbs,
        "subnav_count": parser.services_subnav,
        "aria_current": parser.aria_current,
        "breadcrumbs_aria": parser.breadcrumbs_aria,
        "subnav_aria": parser.subnav_aria,
        "subnav_link_count": subnav_links,
        "nested_ul_in_ul": parser.nested_ul_in_ul,
        "escaped_html": bool(re.search(r"&lt;(li|a|nav|ul)", html)),
        "unexpanded_tokens": "@@" in html,
        "issues": issues,
        "result": "PASS" if not issues else "FAIL",
    }


def main() -> None:
    results = [validate_page(pid, rel) for pid, rel in PAGES]
    overall = "PASS" if all(r["result"] == "PASS" for r in results) else "FAIL"
    report = {"overall": overall, "pages": results}
    (AUDIT / "CF-003-DOM-VALIDATION.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    if overall != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
