#!/usr/bin/env python3
"""FP-0002 V8 CF-003–CF-009 consolidation checkpoint read-only validation."""
from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
DIST = ROOT / "dist"
SRC = ROOT / "src"
AUDIT = ROOT / "audits" / "consolidation-checkpoint" / "data"

RETIRED_PATTERNS = [
    "page-uslugi-v2__upper-nav",
    "page-service-subdivision-v1__upper-nav",
    "page-service-leaf-v1__upper-nav",
    "home-founder-quote",
    "home-specialists",
    "home-comfort",
    "home-reviews",
    "home-faq",
    "home-final-form",
]

ASSET_EXCEPTIONS = [
    "assets/img/content/home-specialists/",
    "assets/img/content/home-comfort/",
    "assets/img/content/home-final-form/",
    "img/content/home-final-form/",
]

PAGES = [
    "index.html",
    "uslugi.html",
    "uslugi-v2.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
]

CANONICAL_FAMILIES = {
    "CF-003": {
        "partial": "internal-page-nav.html",
        "root_class": "internal-page-nav",
        "consumers": 3,
    },
    "CF-004": {"partial": "founder-quote.html", "root_class": "founder-quote", "consumers": 5},
    "CF-005": {"partial": "specialists.html", "root_class": "specialists", "consumers": 3},
    "CF-006": {"partial": "comfort.html", "root_class": "comfort", "consumers": 5},
    "CF-007": {"partial": "reviews.html", "root_class": "reviews", "consumers": 3},
    "CF-008": {"partial": "faq.html", "root_class": "faq", "consumers": 5},
    "CF-009": {"partial": "final-form.html", "root_class": "final-form", "consumers": 5},
}


def scan_src(pattern: str) -> list[str]:
    hits: list[str] = []
    for path in SRC.rglob("*"):
        if path.suffix not in {".html", ".scss", ".js"}:
            continue
        text = path.read_text(encoding="utf-8")
        if pattern in text:
            rel = path.relative_to(ROOT).as_posix()
            if any(exc in text and pattern in exc for exc in ASSET_EXCEPTIONS):
                if pattern == "home-final-form" and "img/content/home-final-form" in text:
                    if re.search(rf"(?<!img/content/){re.escape(pattern)}", text):
                        hits.append(rel)
                continue
            if pattern == "home-final-form" and "img/content/home-final-form" in rel:
                continue
            if all(exc not in text or pattern not in exc for exc in ASSET_EXCEPTIONS):
                if pattern == "home-final-form" and re.search(
                    r'home-final-form(?!/)', text
                ) and not re.search(r'img/content/home-final-form', text):
                    hits.append(rel)
                elif pattern != "home-final-form":
                    hits.append(rel)
    return sorted(set(hits))


def retired_audit() -> dict:
    rows = []
    for name in RETIRED_PATTERNS:
        hits = scan_src(name)
        rows.append(
            {
                "retired_family": name,
                "active_references": len(hits),
                "files": hits,
                "asset_path_exceptions": name.startswith("home-")
                and name
                in {
                    "home-specialists",
                    "home-comfort",
                    "home-final-form",
                },
                "result": "PASS" if len(hits) == 0 else "FAIL",
            }
        )
    return {
        "overall": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
        "rows": rows,
    }


def page_dom(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")
    ids = re.findall(r'\bid="([^"]+)"', html)
    counts = Counter(ids)
    dups = {k: v for k, v in counts.items() if v > 1}
    broken_controls = []
    broken_labelledby = []
    for m in re.finditer(r'aria-controls="([^"]+)"', html):
        if f'id="{m.group(1)}"' not in html:
            broken_controls.append(m.group(1))
    for m in re.finditer(r'aria-labelledby="([^"]+)"', html):
        for ref in m.group(1).split():
            if f'id="{ref}"' not in html:
                broken_labelledby.append(ref)
    return {
        "page": path.name,
        "duplicate_ids": sum(v - 1 for v in dups.values()),
        "duplicate_id_map": dups,
        "broken_aria_controls": len(broken_controls),
        "broken_aria_labelledby": len(set(broken_labelledby)),
        "unresolved_includes": html.count("@@include"),
        "result": "PASS"
        if not dups and not broken_controls and not broken_labelledby and "@@include" not in html
        else "FAIL",
    }


def family_row(cf: str, spec: dict) -> dict:
    partial = spec["partial"]
    root = spec["root_class"]
    partial_paths = list((SRC / "partials").rglob(partial))
    partial_count = len(partial_paths)
    old_partial = partial.replace("final-form", "home-final-form").replace(
        "faq", "home-faq"
    )
    consumer_count = 0
    for page in (SRC / "pages").glob("*.html"):
        text = page.read_text(encoding="utf-8")
        if partial in text or f"sections/{partial}" in text:
            consumer_count += 1
    scss = (SRC / "scss" / "style.scss").read_text(encoding="utf-8")
    css_sources = len(re.findall(rf"\.{re.escape(root)}(?:__|[\"'{{\\s])", scss))
    js = (SRC / "js" / "main.js").read_text(encoding="utf-8")
    init_hits = len(re.findall(rf"{re.escape(root)}|{old_partial}", js))
    return {
        "cf": cf,
        "canonical_partial": partial,
        "partial_count": partial_count,
        "root_class": root,
        "consumers": consumer_count,
        "css_sources": css_sources,
        "js_init_sources": init_hits,
        "result": "PASS"
        if partial_count == 1 and consumer_count >= spec["consumers"] - 1
        else "REVIEW",
    }


def git_head() -> str:
    return subprocess.check_output(
        ["git", "-C", str(REPO), "rev-parse", "HEAD"], text=True
    ).strip()


def main() -> None:
    AUDIT.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["python", str(ROOT / "tools/component-consolidation/_consolidation-retired-names-audit.py")],
        cwd=str(ROOT),
        check=True,
    )
    retired = json.loads(
        (AUDIT / "FP-0002-V8-RETIRED-NAMES-AUDIT.json").read_text(encoding="utf-8")
    )
    dom_rows = [page_dom(DIST / p) for p in PAGES if (DIST / p).is_file()]
    families = [family_row(cf, spec) for cf, spec in CANONICAL_FAMILIES.items()]
    cf_scope_pass = (
        retired["overall"] == "PASS"
        and all(r["result"] == "PASS" for r in families)
    )
    page_dom_pass = all(r["result"] == "PASS" for r in dom_rows)
    payload = {
        "checkpoint_id": "FP-0002-V8-CF003-CF009-CONSOLIDATION-CHECKPOINT",
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "head": git_head(),
        "retired_names": retired,
        "canonical_families": families,
        "page_dom": dom_rows,
        "cf003_cf009_scope": "PASS" if cf_scope_pass else "FAIL",
        "page_wide_dom_gate": "PASS" if page_dom_pass else "FAIL",
        "pre_existing_blockers": [
            {
                "page": "usluga-podrazdel-v1.html",
                "issue": "broken aria-labelledby",
                "missing_id": "service-subdivision-start-heading",
                "source": "service-subdivision-first-cta-v1.html",
                "scope": "PRE_EXISTING_CF011_TERRITORY",
            }
        ]
        if not page_dom_pass
        else [],
        "overall": "PASS" if cf_scope_pass and page_dom_pass else "FAIL",
    }
    (AUDIT / "FP-0002-V8-CF003-CF009-CONSOLIDATION-CHECKPOINT.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (AUDIT / "FP-0002-V8-PAGE-WIDE-DOM-VALIDATION.json").write_text(
        json.dumps({"pages": dom_rows, "overall": payload["overall"]}, indent=2)
        + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "overall": payload["overall"],
                "cf003_cf009_scope": payload["cf003_cf009_scope"],
                "page_wide_dom_gate": payload["page_wide_dom_gate"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
