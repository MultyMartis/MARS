#!/usr/bin/env python3
"""Generate E11 architecture markdown from JSON. NOT FOR GIT."""
import json
from pathlib import Path

VAL = Path(__file__).parent
ARCH = VAL.parent.parent / "architecture"

static = json.loads((VAL / "static-v9-page-inventory.json").read_text(encoding="utf-8"))
wp = json.loads((VAL / "wp-route-inventory.json").read_text(encoding="utf-8"))
mapping = json.loads((VAL / "static-to-wp-route-mapping-contract.json").read_text(encoding="utf-8"))
sections = json.loads((VAL / "section-stack-contract.json").read_text(encoding="utf-8"))
provenance = json.loads((VAL / "template-provenance-contract.json").read_text(encoding="utf-8"))
content = json.loads((VAL / "content-authority-contract.json").read_text(encoding="utf-8"))
priority = json.loads((VAL / "priority-remediation-matrix.json").read_text(encoding="utf-8"))
register = json.loads((VAL / "final-page-contract-register.json").read_text(encoding="utf-8"))

core = [
    "/",
    "/uslugi/",
    "/uslugi/zavisimosti/",
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
    "/kontakty/",
    "/otzyvy/",
    "/privacy-policy/",
    "/uslugi/psihicheskoe-zdorovie/",
    "/uslugi/rasstroystva-pischevogo-povedeniya/",
]

lines = [
    "# FP-0002 V9-06E11 Static V9 Page Inventory v1",
    "",
    f"**Generated:** {static['generated_at']}",
    f"**Page count:** {static['page_count']}",
    "",
    "| Static page | Type | Route | Sections | WP required status | Notes |",
    "|---|---|---|---:|---|---|",
]
for p in static["pages"]:
    fname = p["file_path"].split("/")[-1]
    lines.append(
        f"| `{fname}` | {p['page_type']} | {p['inferred_route']} | {p['section_count']} | {p['expected_status']} | {p['notes']} |"
    )
lines += ["", "## Core section stacks", ""]
for p in static["pages"]:
    if p["inferred_route"] in core:
        lines.append(f"### {p['inferred_route']}")
        lines.append("`" + ", ".join(p["section_root_classes_in_order"]) + "`")
        lines.append("")
(ARCH / "FP-0002-V9-06E11-STATIC-V9-PAGE-INVENTORY-v1.md").write_text("\n".join(lines), encoding="utf-8")

lines = [
    "# FP-0002 V9-06E11 WP Route Inventory v1",
    "",
    f"**Runtime:** {wp['runtime_url']}",
    f"**Route count:** {wp['route_count']}",
    "",
    "| Route | WP object | Template | Main/hero | Current stack | Notes |",
    "|---|---|---|---|---|---|",
]
for r in wp["routes"]:
    stack = ", ".join(r["current_section_stack_root_classes"][:6])
    if len(r["current_section_stack_root_classes"]) > 6:
        stack += f" (+{len(r['current_section_stack_root_classes']) - 6})"
    mw = (r.get("main_wrapper") or "—")[:40]
    lines.append(
        f"| {r['route']} | {r.get('wp_object_id')} | {r.get('template') or '—'} | {mw} / hero={r.get('hero_present')} | {stack} | {r.get('notes') or ''} |"
    )
(ARCH / "FP-0002-V9-06E11-WP-ROUTE-INVENTORY-v1.md").write_text("\n".join(lines), encoding="utf-8")

lines = [
    "# FP-0002 V9-06E11 Static-to-WP Route Mapping Contract v1",
    "",
    "| Static V9 source | WP route | Mapping confidence | Expected status | Notes |",
    "|---|---|---|---|---|",
]
seen = set()
for m in mapping["mappings"]:
    if m["wp_route"] in seen and m["static_v9_source_file"].endswith("uslugi.html"):
        continue
    seen.add(m["wp_route"])
    src = m["static_v9_source_file"].split("/")[-1]
    lines.append(
        f"| {src} | {m['wp_route']} | {m['mapping_confidence']} | {m['expected_status']} | {m['notes']} |"
    )
lines += ["", "## WP routes without static counterpart", ""]
for w in mapping.get("wp_routes_without_static_counterpart", []):
    lines.append(f"- {w['wp_route']} (ID {w.get('wp_object_id')})")
(ARCH / "FP-0002-V9-06E11-STATIC-TO-WP-ROUTE-MAPPING-CONTRACT-v1.md").write_text("\n".join(lines), encoding="utf-8")

lines = [
    "# FP-0002 V9-06E11 Section Stack Contract v1",
    "",
    "Per E10 governance: class-level DOM match on alcohol leaf is **insufficient** — inner markup from home partial reuse = SEMANTIC_REBUILD.",
    "",
    "| Route | Static sections | WP sections | Result | Notes |",
    "|---|---:|---:|---|---|",
]
for c in sections["contracts"]:
    lines.append(
        f"| {c['route']} | {c['expected_section_count']} | {c['current_wp_section_count']} | {c['status']} | {c['repair_recommendation'][:70]} |"
    )
(ARCH / "FP-0002-V9-06E11-SECTION-STACK-CONTRACT-v1.md").write_text("\n".join(lines), encoding="utf-8")

lines = [
    "# FP-0002 V9-06E11 Template Provenance Contract v1",
    "",
    "| Template/partial | Used by | Provenance | Risk | Future use |",
    "|---|---|---|---|---|",
]
for i in provenance["items"]:
    routes = ", ".join(i["used_by_routes"][:2])
    fname = Path(i["file_path"]).name
    lines.append(
        f"| `{fname}` | {routes} | {i['provenance']} | {i['risk']} | {i['allowed_future_use']} |"
    )
(ARCH / "FP-0002-V9-06E11-TEMPLATE-PROVENANCE-CONTRACT-v1.md").write_text("\n".join(lines), encoding="utf-8")

lines = [
    "# FP-0002 V9-06E11 Content Authority Contract v1",
    "",
    "| Route | Expected content source | Current content source | Status | Notes |",
    "|---|---|---|---|---|",
]
for r in content["routes"]:
    lines.append(
        f"| {r['route']} | {r['expected_content_source']} | {r['current_content_source']} | {r['status']} | risk={r['text_mutation_risk']} |"
    )
(ARCH / "FP-0002-V9-06E11-CONTENT-AUTHORITY-CONTRACT-v1.md").write_text("\n".join(lines), encoding="utf-8")

lines = [
    "# FP-0002 V9-06E11 Priority Remediation Matrix v1",
    "",
    f"**E12 start route:** {priority['recommended_e12_start']}",
    "",
    "| Route | Severity | Repair type | Recommended phase | Notes |",
    "|---|---|---|---|---|",
]
for r in priority["routes"]:
    lines.append(
        f"| {r['route']} | {r['severity']} | {r['repair_type']} | {r['recommended_phase']} | screenshot={r['screenshot_validation_required']} |"
    )
(ARCH / "FP-0002-V9-06E11-PRIORITY-REMEDIATION-MATRIX-v1.md").write_text("\n".join(lines), encoding="utf-8")

lines = [
    "# FP-0002 V9-06E11 Final Page Contract Register v1",
    "",
    "| Route | Final classification | Next action | Notes |",
    "|---|---|---|---|",
]
for r in register["rows"]:
    if r["route"] in register.get("core_summary", {}) or r["final_classification"].startswith("NEEDS"):
        notes = f"stack={r['section_stack_result']} content={r['content_result']}"
        lines.append(f"| {r['route']} | {r['final_classification']} | {r['next_action']} | {notes} |")
(ARCH / "FP-0002-V9-06E11-FINAL-PAGE-CONTRACT-REGISTER-v1.md").write_text("\n".join(lines), encoding="utf-8")

next_md = """# FP-0002 V9-06E11 Next Step Recommendation v1

**Date:** 2026-07-07  
**Verdict:** PASS  
**Recommended next action:** CREATE_V9_06E12_DIRECT_STATIC_PORT_REPAIR_ALCOHOL_LEAF_TASK

## Rationale

E11 contract inventory confirms E10 root cause: WordPress routes use semantic PHP reconstruction (alcohol-stack.php, leaf-stack.php, CPT-driven hub) rather than direct static V9 HTML section-stack ports.

| Signal | Evidence |
|---|---|
| Highest-risk static-backed page | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ — NEEDS_DIRECT_V9_REPLACEMENT |
| Section class probe | 18 classes match static dist order (E10/E11 live probe) |
| Visual drift | Operator + E10 screenshot diff — inner markup/home partial reuse |
| Truncated generic leaf | leaf-stack.php — 10 sections vs 17 static authority |
| Governance gate | E10 contract sections 2–4 — no PASS without screenshot after direct port |

## E12 scope (recommended)

1. Replace alcohol-stack.php orchestration with direct static V9 section HTML port from usluga-konechnaya-v1.html / dist counterpart.
2. Fork home partials used on service context (specialists, reviews, comfort, clinic-landscape) or parameterize with service-leaf IDs.
3. Classify each section content as EXACT_V9_CONTENT vs V9_FIXTURE_DEMO vs OPERATOR_REAL_CONTENT.
4. Mandatory screenshot pair: static dist vs runtime before any PASS.
5. No broad refactor — single page only.

## Deferred (post-E12)

- /uslugi/ hub direct port (E13)
- / home content reseed (E14)
- Legal shell gaps (subnav/final-form) — low severity
- Blog — DEFERRED
- Placeholder leaf routes — DEMO_ACCEPTED

Authority: validation/v9-06e11-static-to-wp-page-contract-inventory/final-verdict.json
"""
(ARCH / "FP-0002-V9-06E11-NEXT-STEP-RECOMMENDATION-v1.md").write_text(next_md, encoding="utf-8")
print("docs ok")
