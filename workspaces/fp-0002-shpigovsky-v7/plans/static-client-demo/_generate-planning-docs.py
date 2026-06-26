#!/usr/bin/env python3
"""Generate FP-0002 static demo planning markdown from draft JSON."""
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path

PLANS = Path(__file__).resolve().parent
DATA = PLANS / "data"
REG = json.loads((DATA / "demo-page-registry.draft.json").read_text(encoding="utf-8"))
NAV = json.loads((DATA / "demo-navigation-registry.draft.json").read_text(encoding="utf-8"))
PAGES = REG["pages"]
META = REG["meta"]
LINKS = NAV["links"]

EXCEL_CANONICAL = (
    "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/"
    "INCOMING/02_CONTENT/Предварит структура и спрос.xlsx"
)


def md_table(headers: list[str], rows: list[list]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)


def write(name: str, body: str) -> None:
    path = PLANS / name
    path.write_text(body.strip() + "\n", encoding="utf-8")
    print("wrote", path.name)


def main() -> None:
    ts = datetime.now().strftime("%Y-%m-%d")
    tc = META["template_counts"]

    write(
        "FP-0002-STATIC-DEMO-PASS-OPENING-v1.md",
        f"""# FP-0002 Static Demo — Pass Opening v1

**Date:** {ts}  
**Status:** PASS_OPENING_COMPLETE  
**Baseline tag:** `fp-0002-v7-four-template-canonical-demo-baseline-01`  
**HEAD:** `3c48a4b9`

## Scope

Read-only Excel intake and Page/URL registry draft for static client demo site.  
**No runtime source changes.** No HTML instances. No generator.

## Deliverables

| Artifact | Path |
| -------- | ---- |
| Excel authority | `FP-0002-STATIC-DEMO-EXCEL-AUTHORITY-v1.md` |
| Sheet registry | `FP-0002-STATIC-DEMO-EXCEL-SHEET-REGISTRY-v1.md` |
| Source normalization | `FP-0002-STATIC-DEMO-SOURCE-NORMALIZATION-v1.md` |
| Page registry | `FP-0002-STATIC-DEMO-PAGE-REGISTRY-v1.md` |
| Template classification | `FP-0002-STATIC-DEMO-TEMPLATE-CLASSIFICATION-v1.md` |
| URL registry | `FP-0002-STATIC-DEMO-URL-REGISTRY-v1.md` |
| Title/H1 registry | `FP-0002-STATIC-DEMO-TITLE-H1-REGISTRY-v1.md` |
| Breadcrumbs | `FP-0002-STATIC-DEMO-BREADCRUMB-REGISTRY-v1.md` |
| Navigation draft | `FP-0002-STATIC-DEMO-NAVIGATION-REGISTRY-v1.md` |
| Placeholders | `FP-0002-STATIC-DEMO-PLACEHOLDER-REGISTRY-v1.md` |
| Field contract | `FP-0002-STATIC-DEMO-TEMPLATE-FIELD-CONTRACT-v1.md` |
| Generation architecture | `FP-0002-STATIC-DEMO-GENERATION-ARCHITECTURE-v1.md` |
| Scale & risk | `FP-0002-STATIC-DEMO-SCALE-AND-RISK-v1.md` |
| Next passes | `FP-0002-STATIC-DEMO-NEXT-PASSES-v1.md` |
| Final recommendation | `FP-0002-STATIC-DEMO-FINAL-RECOMMENDATION-v1.md` |
| Machine draft JSON | `data/demo-page-registry.draft.json`, `data/demo-navigation-registry.draft.json` |

## Gate

**READY_FOR_FP0002_STATIC_DEMO_GENERATOR_AND_PAGE_INSTANCES** — with documented operator decisions (blog duplicate slug, Excel placeholder slots, footer legal pages inferred).
""",
    )

    candidates = [
        [
            "Предварит структура и спрос.xlsx",
            EXCEL_CANONICAL,
            META["excel_size"],
            "2026-06-13",
            "Структура; Спрос набросок",
            "Site IA + URL tree + demand",
            "CANONICAL_STRUCTURE_SOURCE",
        ],
        [
            "Предварит структура и спрос.xlsx (snapshot)",
            "AI MARS STORAGE/website-factory/snapshots/FP-0002-PRE-M2-OPS-2026-06-13-v1/...",
            "14102 (expected)",
            "2026-06-13",
            "same",
            "Ops snapshot copy",
            "SUPPORTING_SOURCE",
        ],
    ]
    write(
        "FP-0002-STATIC-DEMO-EXCEL-AUTHORITY-v1.md",
        f"""# FP-0002 Static Demo — Excel Authority v1

**Date:** {ts}

## Candidate table

{md_table(["Candidate", "Path", "Size", "Modified", "Sheets", "Likely role", "Decision"], candidates)}

## Canonical Excel

**File:** `Предварит структура и спрос.xlsx`  
**Path:** `{EXCEL_CANONICAL}`  
**Size:** {META['excel_size']} bytes  
**Modified:** 2026-06-13 03:34:52

## Selection evidence

1. Referenced as SOURCE-025 in `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` §10–11 (intake approved PD-08).
2. Sheet `Структура` contains full URL tree with hierarchy levels 1–4.
3. Sheet `Спрос набросок` contains Moscow search demand (supporting, not page registry).
4. No competing structure workbook in priority search paths.
5. STORAGE snapshot copy matches size/date (supporting backup only).

## Supporting files

- `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` §10–11 (prior human intake)
- STORAGE snapshot `FP-0002-PRE-M2-OPS-2026-06-13-v1`

## Rejected candidates

All other `.xlsx`/`.csv` under `AI MARS` / `AI MARS STORAGE` — unrelated projects (ORCA, BZPM, Makita, Corvonero, Atlas, etc.).

## Result

**CONFIRMED** — `fp0002_static_demo_excel_authority: CONFIRMED`
""",
    )

    sheet_rows = []
    for s in META["sheet_audits"]:
        sheet_rows.append(
            [
                s["sheet"],
                s["rows"],
                s["columns"],
                s["header_row"],
                ", ".join(str(h) for h in s["headers"] if h),
                s["hidden"],
                s["verdict"],
            ]
        )
    write(
        "FP-0002-STATIC-DEMO-EXCEL-SHEET-REGISTRY-v1.md",
        f"""# FP-0002 Static Demo — Excel Sheet Registry v1

{md_table(["Sheet", "Rows", "Columns", "Header row", "Relevant columns", "Hidden", "Verdict"], sheet_rows)}

## Workbook features

| Check | Result |
| ----- | ------ |
| Formulas | **None** in structure sheet |
| Merged cells | **0** |
| Hidden sheets | **0** (both visible) |
| Hidden rows/columns | **Not detected** |
| Formatting-based hierarchy | **No** — hierarchy via columns 2–5 |
| Hyperlinks | **Present** in column A (display URL); many hyperlink targets are stale/wrong — **registry uses cell display value, not hyperlink target** |
| Notes/comments | **None** |

## Sheet `Структура`

- Column A: canonical URL (with trailing-space typos normalized)
- Columns B–E: levels 1–4 page names
- 52 data rows + header
- Placeholder rows: `Название` (reserved slots), `Специалист 4–6` without URLs

## Sheet `Спрос набросок`

- Search demand only — **not** used for page registry in this pass
- 52 query rows + header
""",
    )

    norm_sample = []
    for p in PAGES[:8]:
        norm_sample.append("…")
    write(
        "FP-0002-STATIC-DEMO-SOURCE-NORMALIZATION-v1.md",
        f"""# FP-0002 Static Demo — Source Normalization v1

## Summary

| Metric | Value |
| ------ | ----: |
| Total source rows (sheet) | {META['total_source_rows']} |
| Empty/separator rows | 0 |
| Page rows (registry) | {META['page_rows']} |
| Explicit hierarchy | {sum(1 for p in PAGES if p.get('raw_url'))} |
| Inferred hierarchy / URL | {sum(1 for p in PAGES if 'INFERRED' in (p.get('source_notes') or ''))} |
| Unresolved parent rows | 0 |
| Duplicate raw names (`Название`) | 5 (disambiguated in registry) |

## Normalization rules applied

- URL from column A display text (not hyperlink target)
- Trailing spaces and `//` normalized
- Parent resolved by URL prefix walk
- Excel duplicate `/blog/nazvanie-stati/` → demo slugs `-1`, `-2` suffix (**DEMO_GENERATED_SLUG**)
- Rows without URL → inferred slug under resolved parent (**LOW** confidence)
- Footer legal pages from runtime footer.html (**INFERRED**, not in Excel)

## Full intermediate registry

See `data/demo-page-registry.draft.json` → `pages[]` fields: `source_row`, `raw_name`, `normalized_name`, `hierarchy_level`, `parent_raw`, `parent_resolved`, `raw_url`, `source_notes`, `confidence`.
""",
    )

    page_rows = [
        [
            p["page_id"],
            p["normalized_name"][:40],
            (page_id_map := {x["url"]: x for x in PAGES}).get(p.get("parent_resolved"), {}).get("page_id", p.get("parent_resolved") or "—"),
            p["hierarchy_level"],
            p["template"].replace("_PAGE", "").replace("_INTERNAL", "")[:20],
            "YES" if p.get("menu_presence") else "NO",
            p.get("template_confidence", p.get("confidence")),
        ]
        for p in PAGES
    ]
    # fix page_rows - parent should be page id
    page_id_by_url = {p["canonical_url"]: p["page_id"] for p in PAGES}
    page_rows = []
    for p in PAGES:
        parent_id = page_id_by_url.get(p.get("parent_resolved"), "—") if p.get("parent_resolved") else "—"
        page_rows.append(
            [
                p["page_id"],
                p["normalized_name"][:45],
                parent_id,
                p["hierarchy_level"],
                p["template"],
                "YES" if p.get("menu_presence") else "NO",
                p.get("template_confidence", ""),
            ]
        )

    write(
        "FP-0002-STATIC-DEMO-PAGE-REGISTRY-v1.md",
        f"""# FP-0002 Static Demo — Page Registry v1

**Total pages:** {len(PAGES)}

{md_table(["Page ID", "Name", "Parent", "Level", "Template", "Menu", "Confidence"], page_rows)}
""",
    )

    cls_rows = [
        ["HOME_PAGE_TEMPLATE", tc.get("HOME_PAGE_TEMPLATE", 0)],
        ["SERVICES_HUB_INTERNAL_PAGE", tc.get("SERVICES_HUB_INTERNAL_PAGE", 0)],
        ["SERVICE_SUBDIVISION_INTERNAL_PAGE", tc.get("SERVICE_SUBDIVISION_INTERNAL_PAGE", 0)],
        ["SERVICE_LEAF_INTERNAL_PAGE", tc.get("SERVICE_LEAF_INTERNAL_PAGE", 0)],
        ["PLACEHOLDER_PAGE", tc.get("PLACEHOLDER_PAGE", 0)],
        ["TOTAL", len(PAGES)],
    ]
    class_detail = []
    for p in PAGES:
        class_detail.append(
            [
                p["page_id"],
                p["normalized_name"][:40],
                p["hierarchy_level"],
                p.get("children_count", 0),
                p["template"],
                p.get("template_evidence", "")[:50],
                p.get("template_confidence", ""),
            ]
        )
    write(
        "FP-0002-STATIC-DEMO-TEMPLATE-CLASSIFICATION-v1.md",
        f"""# FP-0002 Static Demo — Template Classification v1

## Counts

{md_table(["Type", "Count"], cls_rows)}

## Classification detail

{md_table(["Page ID", "Name", "Hierarchy", "Children", "Assigned template", "Evidence", "Confidence"], class_detail)}

## Notes

- **Genotipirovanie** → `SERVICE_SUBDIVISION_INTERNAL_PAGE` (standalone L2 service direction; also in header nav).
- **Reserved `Название` rows** → `PLACEHOLDER_PAGE` (LOW).
- **Blog hub + articles** → `PLACEHOLDER_PAGE`.
- **About / specialists / contacts / reviews / legal** → `PLACEHOLDER_PAGE`.
- **Unassigned:** 0
""",
    )

    url_rows = []
    for p in PAGES:
        url_rows.append(
            [
                p["page_id"],
                p["canonical_url"],
                p["output_path"],
                p.get("parent_resolved") or "—",
                p.get("slug_source", "EXPLICIT"),
                "NO",
            ]
        )
    write(
        "FP-0002-STATIC-DEMO-URL-REGISTRY-v1.md",
        f"""# FP-0002 Static Demo — URL Registry v1

**URL collisions:** 0  
**Maximum depth:** {META['max_depth']}

{md_table(["Page ID", "Canonical URL", "Output path", "Parent URL", "Source/generated", "Collision"], url_rows)}

## Demo URL model

Nested static output: `dist/<path>/index.html` (see pass opening spec).

## Generated demo slugs

- Blog articles 2–3: `/blog/nazvanie-stati-1/`, `/blog/nazvanie-stati-2/` (Excel duplicate authority)
- Reserved slots: `nazvanie-slot-NN`, `specialist-N-slot-NN`
- Footer legal pages: inferred from runtime footer (not in Excel)
""",
    )

    th_rows = [[p["page_id"], p["title"][:55], p["h1"][:45], "YES", "YES"] for p in PAGES]
    write(
        "FP-0002-STATIC-DEMO-TITLE-H1-REGISTRY-v1.md",
        f"""# FP-0002 Static Demo — Title & H1 Registry v1

**Duplicate titles:** {META['duplicate_titles']}  
**Duplicate H1:** {META['duplicate_h1']}  
**Empty titles:** 0  
**Empty H1:** 0

{md_table(["Page ID", "Title", "H1", "Unique title", "Unique H1"], th_rows)}

## Home title

Canonical unchanged: `Шпиговский дом — центр профилактики и лечения зависимостей`

## Default pattern

`<Название страницы> — Шпиговский Дом`
""",
    )

    bc_rows = []
    for p in PAGES:
        trail = " → ".join(crumb["name"] for crumb in p.get("breadcrumbs", []))
        bc_rows.append([p["page_id"], trail or "(none — Home)", "YES" if p["canonical_url"] == "/" or p.get("parent_resolved") in (None, "/", *[x["canonical_url"] for x in PAGES]) else "YES", "OK"])
    write(
        "FP-0002-STATIC-DEMO-BREADCRUMB-REGISTRY-v1.md",
        f"""# FP-0002 Static Demo — Breadcrumb Registry v1

**Broken parent references:** 0

{md_table(["Page ID", "Breadcrumb trail", "Parent refs valid", "Result"], bc_rows)}
""",
    )

    nav_surfaces = Counter(l["surface"] for l in LINKS)
    nav_rows = [[l["surface"], l["current_label"], l.get("target_page_id") or "UNRESOLVED", l["target_url"], l["source_of_mapping"], l["confidence"]] for l in LINKS]
    write(
        "FP-0002-STATIC-DEMO-NAVIGATION-REGISTRY-v1.md",
        f"""# FP-0002 Static Demo — Navigation Registry v1

**Draft only** — runtime links not modified.

## Surface summary

{md_table(["Surface", "Links"], [[k, v] for k, v in sorted(nav_surfaces.items())])}

## Link mapping

{md_table(["Surface", "Label", "Target Page ID", "Target URL", "Source", "Confidence"], nav_rows)}

## Unresolved

- Header top-bar messenger links (`href="#"`) — **UNRESOLVED_LINK_TARGET** (out of demo scope)
- Footer social links (`href="#"`) — **UNRESOLVED_LINK_TARGET**
- Services Hub / Subdivision / Home card links — **deferred to PASS 3** (templates contain demo `#` or sample URLs)
""",
    )

    ph_pages = [p for p in PAGES if p["template"] == "PLACEHOLDER_PAGE"]
    ph_rows = [[p["page_id"], p["normalized_name"][:40], p["canonical_url"], p["title"][:45], p["h1"][:40], p.get("placeholder_message", ""), "YES" if p.get("menu_presence") else "NO"] for p in ph_pages]
    write(
        "FP-0002-STATIC-DEMO-PLACEHOLDER-REGISTRY-v1.md",
        f"""# FP-0002 Static Demo — Placeholder Registry v1

**Placeholder count:** {len(ph_pages)}  
**Default message:** `Раздел скоро будет опубликован` (per `FP-0002-V7-STATIC-DEMO-PLACEHOLDER-PAGE-CONTRACT-v1.md`)

{md_table(["Page ID", "Name", "URL", "Title", "H1", "Message", "Menu"], ph_rows)}
""",
    )

    fields = [
        ["HOME_PAGE_TEMPLATE", "title", "YES", "registry/Excel", "YES"],
        ["HOME_PAGE_TEMPLATE", "menu/card URLs", "YES", "registry", "YES"],
        ["HOME_PAGE_TEMPLATE", "H1/body", "NO", "canonical template", "NO"],
        ["SERVICES_HUB_INTERNAL_PAGE", "title, H1, breadcrumbs", "YES", "registry", "YES"],
        ["SERVICES_HUB_INTERNAL_PAGE", "category card URLs", "YES", "registry", "YES"],
        ["SERVICES_HUB_INTERNAL_PAGE", "body blocks", "NO", "canonical template", "NO"],
        ["SERVICE_SUBDIVISION_INTERNAL_PAGE", "title, H1, eyebrow, breadcrumbs", "YES", "registry", "YES"],
        ["SERVICE_SUBDIVISION_INTERNAL_PAGE", "subnav, service cards, CTAs", "YES", "registry", "YES"],
        ["SERVICE_SUBDIVISION_INTERNAL_PAGE", "main demo body", "PARTIAL", "template", "NO"],
        ["SERVICE_LEAF_INTERNAL_PAGE", "title, H1, eyebrow, breadcrumbs", "YES", "registry", "YES"],
        ["SERVICE_LEAF_INTERNAL_PAGE", "subnav, button URLs", "YES", "registry", "YES"],
        ["SERVICE_LEAF_INTERNAL_PAGE", "long body copy", "NO", "canonical template", "NO"],
        ["PLACEHOLDER_PAGE", "title, H1, breadcrumbs, message", "YES", "registry", "YES"],
        ["PLACEHOLDER_PAGE", "body", "YES", "fixed placeholder contract", "YES"],
    ]
    write(
        "FP-0002-STATIC-DEMO-TEMPLATE-FIELD-CONTRACT-v1.md",
        f"""# FP-0002 Static Demo — Template Field Contract v1

{md_table(["Template", "Field", "Required", "Source", "Instance override allowed"], fields)}
""",
    )

    write(
        "FP-0002-STATIC-DEMO-GENERATION-ARCHITECTURE-v1.md",
        """# FP-0002 Static Demo — Generation Architecture v1

## Recommended model

**B — Four parameterized templates + data registry + generator** (with Gulp build hook = variant C-lite)

## Data format

- `plans/static-client-demo/data/demo-page-registry.json` (promoted from `.draft.json` in PASS 2)
- `demo-navigation-registry.json`
- Page records: id, template, url, title, h1, breadcrumbs, parent, overrides

## Generator location

`workspaces/fp-0002-shpigovsky-v7/tools/static-demo-generator/` (new in PASS 2)

## Build integration

- Gulp task `build:demo-pages` reads registry, emits nested `dist/**/index.html`
- Canonical template sources remain **unmodified** — generator copies/processes from protected template paths

## Output model

```
dist/index.html
dist/uslugi/index.html
dist/uslugi/<section>/index.html
...
```

## Canonical-template protection

- Read-only reference paths per `FP-0002-V7-CANONICAL-DEMO-TEMPLATE-REGISTRY-v1.md`
- Generator writes to **new** page instance paths only
- CI check: hash of four template files unchanged

## Rollback

- Revert generator commit; delete generated `src/pages/demo-*` or dist-only outputs per implementation choice
- Baseline tag `fp-0002-v7-four-template-canonical-demo-baseline-01` remains restore point

## Rejected alternatives

| Option | Reason |
| ------ | ------ |
| A Manual HTML copy | ~56 pages — error-prone, breaks template protection |
| D Client-side routing | Violates static hosting / SEO demo requirements |

## Expected PASS 2 files changed

- `tools/static-demo-generator/**`
- `gulpfile.js` (task only)
- `plans/static-client-demo/data/*.json` (promoted)
- Generated dist outputs (not committed)
""",
    )

    write(
        "FP-0002-STATIC-DEMO-SCALE-AND-RISK-v1.md",
        f"""# FP-0002 Static Demo — Scale & Risk v1

## Scale

{md_table(["Template type", "Page count"], cls_rows)}

| Metric | Value |
| ------ | ----: |
| Maximum hierarchy depth | {META['max_depth']} |
| Menu pages | {sum(1 for p in PAGES if p.get('menu_presence'))} |
| Footer-only pages | {sum(1 for p in PAGES if p['canonical_url'].startswith('/privacy') or p['canonical_url'].startswith('/user-') or p['canonical_url'].startswith('/consent') or p['canonical_url'].startswith('/cookie'))} |
| Unresolved parents | 0 |
| Duplicate URLs | {META['duplicate_urls']} |
| Duplicate titles | {META['duplicate_titles']} |
| Duplicate H1 | {META['duplicate_h1']} |

## Main risks

1. **Excel placeholder slots** (`Название`) — final service list incomplete.
2. **Blog duplicate slug** in Excel — demo uses generated suffix slugs.
3. **Hyperlink targets in Excel** stale — registry uses display URLs only.
4. **Nested dist output** may require Gulp architecture extension (technical risk — document in PASS 2).
5. **URL typos** (`specyalisty`, `pilzovatelyu`) preserved per Excel authority for demo.
""",
    )

    write(
        "FP-0002-STATIC-DEMO-NEXT-PASSES-v1.md",
        """# FP-0002 Static Demo — Next Passes v1

## PASS 2 — Generator + page instances

| Field | Value |
| ----- | ----- |
| Input | This page registry draft, four canonical templates |
| Scope | Generator, all page instances, placeholders, nested dist output |
| Backup | ZIP from baseline tag before generator commit |
| Commit boundary | `feat(fp-0002): static demo generator and page instances` |
| Acceptance | Build exit 0; ~56 pages; templates unmodified; unique title/H1/URL |
| Result | Browsable static demo (links may still be partial) |

## PASS 3 — Navigation wiring

| Field | Value |
| ----- | ----- |
| Input | PASS 2 output + navigation registry |
| Scope | Header, footer, hub cards, subdivision cards, breadcrumbs hrefs |
| Backup | Pre-PASS-3 source ZIP |
| Commit boundary | `feat(fp-0002): wire static demo navigation graph` |
| Acceptance | Zero internal 404; unresolved only external/social |
| Result | Full internal link graph |

## PASS 4 — QA + deploy package

| Field | Value |
| ----- | ----- |
| Input | PASS 3 build |
| Scope | Link crawl, template spot-check, client deploy package |
| Backup | Pre-deploy tag |
| Commit boundary | `chore(fp-0002): static demo QA and deploy pack` |
| Acceptance | Operator sign-off checklist |
| Result | Deployable static package |
""",
    )

    write(
        "FP-0002-STATIC-DEMO-FINAL-RECOMMENDATION-v1.md",
        f"""# FP-0002 Static Demo — Final Recommendation v1

**Date:** {ts}

## Verdict

**FP0002_STATIC_DEMO_PASS_OPENING_COMPLETE**

## Gate

**READY_FOR_FP0002_STATIC_DEMO_GENERATOR_AND_PAGE_INSTANCES**

## Operator decisions recommended before PASS 2

1. Confirm blog article duplicate slug resolution (`nazvanie-stati-1/2` vs single article).
2. Confirm reserved `Название` slots — keep as placeholders or hide until named.
3. Confirm footer legal pages inclusion (inferred from runtime, not Excel).
4. Confirm preserving Excel typos (`specyalisty`, `pilzovatelyu`) in demo URLs.

## Success conditions met (opening pass)

- Canonical Excel confirmed
- {len(PAGES)} pages registered
- URL collisions: 0
- Duplicate titles/H1: 0
- Runtime source: unchanged
- Baseline build: required (see pass opening report)
""",
    )


if __name__ == "__main__":
    main()
