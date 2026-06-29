#!/usr/bin/env python3
"""FP-0002 V8 O-Centre implementation QA runner."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
AUDIT_DATA = ROOT / "audits" / "o-centre-implementation" / "data"
PAGES = [
    "index.html",
    "uslugi.html",
    "uslugi-v2.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
    "o-centre.html",
]
ANCHORS = [
    "who-we-are",
    "who-we-treat",
    "our-approach",
    "our-program",
    "our-home",
    "specialists",
    "reviews",
]
LOREM = re.compile(r"lorem ipsum", re.I)
INFRA_RE = re.compile(r"o-centre-infrastructure-(\d+)\.webp")


class DomParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids: list[str] = []
        self.h_tags: list[tuple[str, str]] = []
        self.aria_labelledby: list[str] = []
        self.aria_controls: list[str] = []
        self.stack: list[str] = []
        self.invalid_nesting = 0

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        if tag in {"html", "head", "body", "main", "section", "article", "div", "p", "ul", "li", "h1", "h2", "h3", "button", "form", "figure", "img", "a"}:
            self.stack.append(tag)
        if "id" in attrs_d:
            self.ids.append(attrs_d["id"])
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.h_tags.append((tag, attrs_d.get("id", "")))
        if "aria-labelledby" in attrs_d:
            self.aria_labelledby.append(attrs_d["aria-labelledby"])
        if "aria-controls" in attrs_d:
            self.aria_controls.append(attrs_d["aria-controls"])

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()


def analyze_page(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")
    parser = DomParser()
    parser.feed(html)
    id_set = set(parser.ids)
    dup_ids = len(parser.ids) - len(id_set)
    h1_count = sum(1 for t, _ in parser.h_tags if t == "h1")
    broken_labelledby = [x for x in parser.aria_labelledby if x not in id_set]
    broken_controls = [x for x in parser.aria_controls if x not in id_set]
    missing_targets = []
    if path.name == "o-centre.html":
        for a in ANCHORS:
            if a not in id_set:
                missing_targets.append(a)
    is_ocentre = path.name == "o-centre.html"
    lorem_count = len(LOREM.findall(html))
    return {
        "file": path.name,
        "h1": h1_count,
        "duplicate_ids": dup_ids,
        "broken_aria_labelledby": len(broken_labelledby),
        "broken_aria_controls": len(broken_controls),
        "missing_anchor_targets": missing_targets,
        "lorem_count": lorem_count,
        "unresolved_includes": html.count("@@include"),
        "result": "PASS"
        if h1_count == 1
        and dup_ids == 0
        and not broken_labelledby
        and not broken_controls
        and not missing_targets
        and (not is_ocentre or not LOREM.search(html))
        and "@@include" not in html
        else "FAIL",
    }


def content_qa(html: str) -> dict:
    checks = {
        "invented_lorem": bool(LOREM.search(html)),
        "phantom_steps": "service-leaf-stages" in html or "BLK-018" in html,
        "faq_accordion": 'data-accordion' in html or 'class="faq' in html,
        "home_gallery": "home-gallery" in html,
        "home_staff_photo": "home-staff-photo" in html,
        "founder_quote_present": "founder-quote" in html,
        "final_form_present": "final-form" in html,
        "subnav_labels": all(
            label in html
            for label in [
                "Кто мы",
                "Кого мы лечим",
                "Наш подход к лечению",
                "Наша программа лечения",
                "Наш Дом",
                "Специалисты",
                "Отзывы",
            ]
        ),
    }
    checks["result"] = "PASS" if not any(
        [checks["invented_lorem"], checks["phantom_steps"], checks["faq_accordion"], checks["home_gallery"], checks["home_staff_photo"]]
    ) and checks["founder_quote_present"] and checks["final_form_present"] and checks["subnav_labels"] else "FAIL"
    return checks


def infrastructure_qa(html: str, base_url: str | None) -> dict:
    found = sorted({int(m.group(1)) for m in INFRA_RE.finditer(html)})
    missing = [i for i in range(1, 21) if i not in found]
    http = {}
    if base_url:
        for i in found:
            url = f"{base_url}/assets/img/content/o-centre/o-centre-infrastructure-{i:02d}.webp"
            try:
                with urlopen(url, timeout=5) as resp:
                    http[str(i)] = resp.status
            except Exception as exc:
                http[str(i)] = str(exc)
    hero_ok = None
    if base_url:
        try:
            with urlopen(f"{base_url}/assets/img/content/o-centre/o-centre-hero.webp", timeout=5) as resp:
                hero_ok = resp.status
        except Exception as exc:
            hero_ok = str(exc)
    return {
        "asset_count_rendered": len(found),
        "asset_ids_rendered": found,
        "missing_from_dom": missing,
        "hero_http": hero_ok,
        "asset_http": http,
        "result": "PASS" if len(found) == 20 and not missing and (not base_url or all(v == 200 for v in http.values())) else "FAIL",
    }


def main() -> int:
    AUDIT_DATA.mkdir(parents=True, exist_ok=True)
    dom_rows = [analyze_page(DIST / p) for p in PAGES if (DIST / p).exists()]
    dom_out = {"pages": dom_rows, "result": "PASS" if all(r["result"] == "PASS" for r in dom_rows) else "FAIL"}
    (AUDIT_DATA / "FP-0002-V8-OCENTRE-DOM-VALIDATION.json").write_text(json.dumps(dom_out, ensure_ascii=False, indent=2), encoding="utf-8")

    oc_html = (DIST / "o-centre.html").read_text(encoding="utf-8")
    content_out = content_qa(oc_html)
    (AUDIT_DATA / "FP-0002-V8-OCENTRE-CONTENT-QA.json").write_text(json.dumps(content_out, ensure_ascii=False, indent=2), encoding="utf-8")

    base = sys.argv[1] if len(sys.argv) > 1 else None
    infra_out = infrastructure_qa(oc_html, base)
    (AUDIT_DATA / "FP-0002-V8-OCENTRE-INFRASTRUCTURE-RUNTIME-QA.json").write_text(json.dumps(infra_out, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({"dom": dom_out["result"], "content": content_out["result"], "infra": infra_out["result"]}, ensure_ascii=False))
    return 0 if dom_out["result"] == content_out["result"] == infra_out["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
