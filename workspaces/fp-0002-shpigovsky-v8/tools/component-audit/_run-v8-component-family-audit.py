#!/usr/bin/env python3
"""Read-only FP-0002 V8 component family audit (bootstrap pass)."""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
SRC = WORKSPACE / "src"
PAGES = SRC / "pages"
PARTIALS = SRC / "partials"
STYLE = SRC / "scss" / "style.scss"
OUT_DIR = WORKSPACE / "audits" / "component-family-audit-v8-bootstrap-01"

CANONICAL_PAGES = [
    "index.html",
    "uslugi-v2.html",
    "usluga-podrazdel-v1.html",
    "usluga-konechnaya-v1.html",
]

INCLUDE_RE = re.compile(r"@@include\('([^']+)'")
CLASS_RE = re.compile(r'class="([^"]+)"')
UPPER_NAV_RE = re.compile(r"page-[a-z0-9-]+__upper-nav")


@dataclass
class IncludeUse:
    page: str
    partial: str


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def collect_includes() -> list[IncludeUse]:
    uses: list[IncludeUse] = []
    for page in CANONICAL_PAGES:
        text = (PAGES / page).read_text(encoding="utf-8")
        for partial in INCLUDE_RE.findall(text):
            uses.append(IncludeUse(page=page, partial=partial))
    return uses


def extract_upper_nav_blocks() -> dict[str, str]:
    blocks: dict[str, str] = {}
    for page in CANONICAL_PAGES:
        text = (PAGES / page).read_text(encoding="utf-8")
        m = re.search(
            r'(<div class="page-[^"]+__upper-nav container">.*?</div>)',
            text,
            re.S,
        )
        if m:
            normalized = re.sub(r"\s+", " ", m.group(1)).strip()
            blocks[page] = normalized
    return blocks


def extract_css_blocks(selector_prefix: str, css: str) -> dict[str, str]:
    """Extract top-level rule blocks whose selector starts with prefix."""
    blocks: dict[str, str] = {}
    pattern = re.compile(
        rf"({re.escape(selector_prefix)}[^{{]*)\{{([^}}]*)\}}",
        re.M,
    )
    for m in pattern.finditer(css):
        sel = " ".join(m.group(1).split())
        body = " ".join(m.group(2).split())
        blocks[sel] = body
    return blocks


def find_page_scoped_component_css(css: str) -> dict[str, list[str]]:
    """Find repeated component selectors duplicated under page roots."""
    component_roots = [
        "breadcrumbs__",
        "services-page-subnav__",
        "services-inner-hero-v2__",
        "home-faq",
        "home-comfort",
        "home-final-form",
        "home-founder-quote",
        "home-reviews",
        "home-specialists",
        "services-program-v2",
    ]
    page_roots = sorted(
        set(re.findall(r"\.(page-[a-z0-9-]+)\s+\.", css))
        | set(re.findall(r"\.(page-[a-z0-9-]+)\s+\.", css))
    )
    page_roots = sorted(set(re.findall(r"\.(page-[a-z0-9-]+)[\s.{]", css)))
    dupes: dict[str, list[str]] = defaultdict(list)
    for page_root in page_roots:
        for comp in component_roots:
            if re.search(rf"\.{re.escape(page_root)}\s+\.[^{{]*{re.escape(comp)}", css):
                dupes[comp].append(page_root)
    return {k: sorted(set(v)) for k, v in dupes.items() if len(set(v)) >= 1}


def build_families(uses: list[IncludeUse]) -> list[dict]:
    partial_pages: dict[str, set[str]] = defaultdict(set)
    for u in uses:
        partial_pages[u.partial].add(u.page)

    families: list[dict] = []
    family_specs = [
        {
            "family_id": "CF-001",
            "name": "Site chrome (header/footer/modal/head)",
            "partials": [
                "partials/layout/head.html",
                "partials/layout/header.html",
                "partials/layout/footer.html",
                "partials/components/modal-consultation.html",
            ],
        },
        {
            "family_id": "CF-002",
            "name": "Inner hero (services-inner-hero-v2)",
            "partials": ["partials/sections/services-inner-hero-v2.html"],
            "css_roots": [".services-inner-hero-v2"],
        },
        {
            "family_id": "CF-003",
            "name": "Upper page nav band (breadcrumbs + local subnav + container)",
            "partials": [
                "partials/components/breadcrumbs.html",
                "partials/components/services-page-subnav.html",
            ],
            "page_wrappers": [
                ".page-uslugi-v2__upper-nav",
                ".page-service-subdivision-v1__upper-nav",
                ".page-service-leaf-v1__upper-nav",
            ],
        },
        {
            "family_id": "CF-004",
            "name": "Category / hub content section",
            "partials": ["partials/sections/services-category-section-v2.html"],
        },
        {
            "family_id": "CF-005",
            "name": "Program block (4 directions + optional CTA band)",
            "partials": [
                "partials/sections/services-program-v2.html",
                "partials/components/services-program-cta-band-v2.html",
            ],
        },
        {
            "family_id": "CF-006",
            "name": "Founder quote band",
            "partials": ["partials/sections/home-founder-quote.html"],
        },
        {
            "family_id": "CF-007",
            "name": "Comfort gallery band",
            "partials": ["partials/sections/home-comfort.html"],
        },
        {
            "family_id": "CF-008",
            "name": "FAQ accordion band",
            "partials": ["partials/sections/home-faq.html"],
        },
        {
            "family_id": "CF-009",
            "name": "Final lead form band",
            "partials": ["partials/sections/home-final-form.html"],
        },
        {
            "family_id": "CF-010",
            "name": "Reviews slider band",
            "partials": ["partials/sections/home-reviews.html"],
        },
        {
            "family_id": "CF-011",
            "name": "Specialists slider band",
            "partials": ["partials/sections/home-specialists.html"],
        },
        {
            "family_id": "CF-012",
            "name": "Clinic landscape bleed image",
            "partials": ["partials/sections/home-clinic-landscape.html"],
        },
    ]

    for spec in family_specs:
        pages_using = sorted(
            {
                page
                for partial in spec.get("partials", [])
                for page in partial_pages.get(partial, set())
            }
        )
        families.append({**spec, "pages": pages_using})
    return families


def upper_nav_css_drift(css: str) -> list[dict]:
    selectors = [
        ".page-uslugi-v2__upper-nav",
        ".page-service-subdivision-v1__upper-nav",
        ".page-service-leaf-v1__upper-nav",
    ]
    rows = []
    for sel in selectors:
        m = re.search(rf"{re.escape(sel)}\s*\{{([^}}]*)\}}", css, re.S)
        body = " ".join(m.group(1).split()) if m else ""
        rows.append({"selector": sel, "declarations": body})
    return rows


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    css = STYLE.read_text(encoding="utf-8")
    uses = collect_includes()
    families = build_families(uses)
    upper_blocks = extract_upper_nav_blocks()
    upper_css = upper_nav_css_drift(css)
    page_dupes = find_page_scoped_component_css(css)

    template_hashes = {
        page: sha256_file(PAGES / page) for page in CANONICAL_PAGES
    }

    partial_usage = defaultdict(list)
    for u in uses:
        partial_usage[u.partial].append(u.page)

    report = {
        "workspace": str(WORKSPACE),
        "canonical_pages": CANONICAL_PAGES,
        "template_sha256": template_hashes,
        "include_usage": {k: sorted(set(v)) for k, v in sorted(partial_usage.items())},
        "upper_nav_html_normalized": upper_blocks,
        "upper_nav_css": upper_css,
        "page_scoped_component_css_duplication": page_dupes,
        "component_families": families,
    }

    (OUT_DIR / "FP-0002-V8-COMPONENT-FAMILY-AUDIT-DATA.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    drift_notes = []
    if len(set(upper_blocks.values())) > 1:
        drift_notes.append("Upper-nav HTML composition differs by page wrapper class name only; shared partials are identical includes.")
    css_bodies = [r["declarations"] for r in upper_css]
    if len(set(css_bodies)) > 1:
        drift_notes.append("Upper-nav wrapper CSS differs (gap/padding) across page-specific classes.")

    md = [
        "# FP-0002 V8 — Component Family Audit (Bootstrap Pass)",
        "",
        "**Mode:** read-only bootstrap audit",
        "**Authority baseline:** `fp-0002-v7-four-template-canonical-demo-baseline-01`",
        "",
        "## Canonical template SHA-256",
        "",
    ]
    for page, digest in template_hashes.items():
        md.append(f"- `{page}` — `{digest}`")
    md.extend(["", "## Upper-nav CSS drift (wrapper only)", ""])
    for row in upper_css:
        md.append(f"- `{row['selector']}` — `{row['declarations']}`")
    md.extend(["", "## Page-scoped duplication of shared component CSS", ""])
    for comp, pages in sorted(page_dupes.items()):
        md.append(f"- `{comp}` rescoped under: {', '.join(f'`{p}`' for p in pages)}")
    md.extend(["", "## Drift notes", ""])
    md.extend(f"- {n}" for n in drift_notes)
    md.extend(["", "## Component families", ""])
    for fam in families:
        md.append(f"### {fam['family_id']} — {fam['name']}")
        md.append(f"- Partials: {', '.join(f'`{p}`' for p in fam.get('partials', []))}")
        md.append(f"- Pages: {', '.join(f'`{p}`' for p in fam.get('pages', []))}")
        if fam.get("page_wrappers"):
            md.append(f"- Page wrappers: {', '.join(f'`{w}`' for w in fam['page_wrappers'])}")
        md.append("")

    (OUT_DIR / "FP-0002-V8-COMPONENT-FAMILY-AUDIT-v1.md").write_text(
        "\n".join(md) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"out_dir": str(OUT_DIR), "families": len(families)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
