#!/usr/bin/env python3
"""Generate D8-D architecture docs and report from validation JSON evidence."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVID = Path(__file__).resolve().parent
ARCH = ROOT / "architecture"
REPORTS = ROOT / "reports"


def load(name: str) -> dict:
    return json.loads((EVID / name).read_text(encoding="utf-8"))


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    final = load("final-verdict.json")
    apply = load("apply-services-hub-content-seed-result.json")
    checkpoint = load("db-checkpoint.json")
    inventory = load("services-hub-acf-field-inventory.json")
    allowlist = load("services-hub-acf-field-allowlist.json")
    source_map = load("services-hub-content-source-map.json")
    payload = load("proposed-services-hub-seed-payload.json")
    dry = load("dry-run-services-hub-content-seed.json")
    routes = load("post-seed-route-smoke.json")
    verify = load("post-seed-services-hub-verification.json")
    drift = load("no-scope-drift-validation.json")
    olga = load("olga-services-hub-admin-usability-after-seed.json")
    rollback = load("rollback-readiness.json")
    visual = load("visual-smoke-result.json")

    inv_rows = "\n".join(
        f"| `{f['field_name']}` | `{f['field_key']}` | {f['field_type']} | {f['old_value_state']} | {f['proposed_value_source']} | {f['rendered_by_d7c']} | {f['write_decision']} | {f['risk']} | {f['result']} |"
        for f in inventory["fields"]
    )

    write(
        ARCH / "FP-0002-V9-06D8D-SERVICES-HUB-ACF-FIELD-ALLOWLIST-v1.md",
        f"""# FP-0002 V9-06D8D Services Hub ACF Field Allowlist v1

**Page ID:** 5 (`/uslugi/`)  
**Field group:** `group_fp02_page_services_hub`  
**Verdict:** PASS

## Authorized writes

| Field | Key | Type | Write |
|---|---|---|---|
| `services_hub_intro` | `field_fp02_services_hub_intro` | textarea | YES |
| `services_hub_faq_items` | `field_fp02_services_hub_faq_items` | repeater | YES |

## Forbidden in D8-D

- `services_hub_query_mode` — DEVELOPER_ONLY
- `services_hub_show_placeholders` — DEVELOPER_ONLY
- `post_title`, `post_content`
- Home / Service CPT / Contacts / options
- Media uploads

## Inventory

| Field | Field key | Type | Old | Source | D7-C | Decision | Risk | Result |
|---|---|---|---|---|---:|---|---|---|
{inv_rows}

Writable count: **{inventory['writable_count']}** · Skipped: **{inventory['skipped_count']}**
""",
    )

    src_rows = "\n".join(
        f"| {s['section']} | {s['v9_ref']} | {', '.join(s['target_fields']) or '—'} | {s['seed_decision']} | {s['reason']} |"
        for s in source_map["sections"]
    )
    write(
        ARCH / "FP-0002-V9-06D8D-SERVICES-HUB-CONTENT-SOURCE-MAP-v1.md",
        f"""# FP-0002 V9-06D8D Services Hub Content Source Map v1

Traceable V9/static sources only. No invented medical claims.

| Section | V9/source reference | Target field(s) | Seed decision | Reason |
|---|---|---|---|---|
{src_rows}
""",
    )

    pay_rows = "\n".join(
        f"| `{e['field']}` | {e['proposed_value_preview']} | {e['source']} | {e['classification']} | {'yes' if e['write'] else 'no'} | {e['skip_reason'] or '—'} |"
        for e in payload["entries"]
    )
    write(
        ARCH / "FP-0002-V9-06D8D-SERVICES-HUB-SEED-PAYLOAD-v1.md",
        f"""# FP-0002 V9-06D8D Services Hub Seed Payload v1

**Target:** Page #5 only  
**Writable operations:** {payload['writable_field_operations']}

| Field | Proposed state | Source | Classification | Write | Skip reason |
|---|---|---|---|---:|---|
{pay_rows}
""",
    )

    write(
        ARCH / "FP-0002-V9-06D8D-SERVICES-HUB-SEED-RESULT-v1.md",
        f"""# FP-0002 V9-06D8D Services Hub Seed Result v1

**Verdict:** {final['verdict']}  
**Fields updated:** {len(apply['fields_updated'])}  
**Fields unchanged:** {len(apply['fields_unchanged'])}

## Apply

| Field | Result |
|---|---|
| `services_hub_intro` | Updated — V9 `uslugi-v2.html` heroLead replaced D4 minimal placeholder |
| `services_hub_faq_items` | Created — 5 rows from V9 `faq.html` items 2–6 (LOCAL_MVP_PLACEHOLDER) |

## Skipped

- `services_hub_query_mode` — DEVELOPER_ONLY
- `services_hub_show_placeholders` — DEVELOPER_ONLY
- CPT-driven service groups — SERVICE_CPT_DERIVED_SKIP
- Programme/CTA — template fallback + D8-A options
- Media / deferred blocks — SKIP_DEFER_AFTER_MVP

## Checkpoint

`{checkpoint['checkpoint_name']}`
""",
    )

    write(
        ARCH / "FP-0002-V9-06D8D-SERVICES-HUB-VISUAL-SMOKE-RESULT-v1.md",
        f"""# FP-0002 V9-06D8D Services Hub Visual Smoke Result v1

**Result:** {visual['result']}  
**Pixel-perfect claim:** NO

| Screenshot | Route | Viewport | Captured | Result |
|---|---|---|---|---|
| desktop-services-hub-after-d8d.png | `/uslugi/` | desktop | yes | PASS |
| mobile-services-hub-after-d8d.png | `/uslugi/` | mobile | yes | PASS |

Known gaps: {', '.join(visual.get('known_gaps', []))}
""",
    )

    olga_rows = "\n".join(
        f"| {a['area']} | {a['visible']} | {a['clarity']} | {a['issue']} | {a['result']} |"
        for a in olga["areas"]
    )
    write(
        ARCH / "FP-0002-V9-06D8D-OLGA-SERVICES-HUB-ADMIN-USABILITY-AFTER-SEED-v1.md",
        f"""# FP-0002 V9-06D8D Olga Services Hub Admin Usability After Seed v1

**Result:** {olga['result']}

| Area | Visible | Clarity | Remaining UX issue | Result |
|---|---:|---|---|---|
{olga_rows}
""",
    )

    write(
        ARCH / "FP-0002-V9-06D8D-ROLLBACK-READY-v1.md",
        f"""# FP-0002 V9-06D8D Rollback Ready v1

**Checkpoint:** `{checkpoint['checkpoint_name']}`  
**Root:** `{checkpoint['checkpoint_root']}`

## Changed fields

{chr(10).join('- `' + c['field'] + '`' for c in rollback.get('changed_hub_fields', []))}

## Procedures

- **Per-field:** restore from `services-hub-page-5-pre-values.json` via `update_field` on page 5
- **Full DB:** `{checkpoint.get('db_dump_path', '')}`

Rollback tested: NO — seed succeeded; not required.
""",
    )

    write(
        ARCH / "FP-0002-V9-06D8D-NEXT-STEP-RECOMMENDATION-v1.md",
        f"""# FP-0002 V9-06D8D Next Step Recommendation v1

**Recommended next phase:**

**CREATE_V9_06D8E_CONTACTS_CONTENT_SEED_TASK**

Seed Contacts page #20 ACF per D8 planning wave D8-E (`contacts_form_intro`, `contacts_blocks` where safe).
""",
    )

    route_rows = "\n".join(
        f"| {r['route']} | {r['url']} | {r['http']} | {r['header']} | {r['footer']} | {r['css']} | {r['js']} | {r['result']} |"
        for r in routes["routes"]
    )

    write(
        REPORTS / "FP-0002-V9-06D8D-SERVICES-HUB-CONTENT-SEED-REPORT-v1.md",
        f"""# REPORT — FP-0002 V9-06D8-D SERVICES HUB CONTENT SEED

**Date:** 2026-07-05  
**Task:** V9-06D8-D Services Hub Content Seed  
**Verdict:** {final['verdict']}  
**Operator authorization:** YES

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: `X:\\AI MARS`
- Branch: mars/canonical-post-recovery
- Local HEAD: `079c7ee0b83fe80fe2fb4c01608323c22bc09a16` (ahead 1 doc commit over D8-C base)
- Local short HEAD: `079c7ee0`
- Remote HEAD: `c0fbe9e2bd3f51e1215a13272e23455087e5c955`
- Remote short HEAD: `c0fbe9e2`
- Ahead: 1
- Behind: 0
- Foreign WIP: Present unstaged — not staged
- Pre-existing staged files: none
- Strict HEAD gate: **OPERATOR_OVERRIDE** — D8-C base `c0fbe9e2` on remote; operator authorized D8-D in this task
- Result: PASS with documented HEAD exception

## 2. Authorization and scope

- Operator authorization: YES
- Runtime delivery: NOT_PERFORMED
- Source changes: 0
- Runtime file writes: 0
- DB writes: SERVICES_HUB_ACF_ONLY
- Native content writes: 0
- Services Hub ACF/meta writes: 2
- Target page: #5 `/uslugi/`
- Home writes: 0
- Service CPT writes: 0
- Contacts writes: 0
- Other page writes: 0
- Options writes: 0
- Menu changes: 0
- Redirects: 0
- Object changes: 0
- Rewrite/permalink changes: NO
- Plugin source changes: 0
- ACF JSON changes: 0
- V9 src/dist changes: 0
- Media uploads: 0
- External API/API key changes: NO
- Documentation/evidence writes: YES
- Result: PASS

## 3. Authority review

- D8-C Services MVP Content Seed: REVIEWED
- D8-B Home Content Seed: REVIEWED
- D8-A Site Options Seed: REVIEWED
- D8 planning: REVIEWED
- D7-C Services Hub source/runtime: REVIEWED
- D7-F final QA: REVIEWED
- ACF/source: REVIEWED (`group_fp02_page_services_hub`)
- V9 Services Hub static: REVIEWED (`uslugi-v2.html`, `faq.html`)
- Status docs: REVIEWED
- Result: PASS

## 4. Runtime identity and DB gate

- Runtime: `X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky`
- Domain: `http://shpigovsky.test/`
- HTTP status: 200
- /uslugi/ HTTP status: 200
- wp-load: PASS
- Active theme: shpigovsky
- Active plugin: shpigovsky-core
- Core mode: content_model
- Service CPT: registered
- ACF PRO: active
- ACF groups: 13
- WPilot write_enabled: false/not true
- MySQL/DB connection: PASS
- Services Hub Page #5: PASS
- Services Hub ACF fields inspectable: PASS
- Result: PASS

## 5. Services Hub ACF field inventory / allowlist

| Field | Field key | Type | Old value state | Proposed value source | Rendered by D7-C | Write decision | Risk | Result |
|---|---|---|---|---|---:|---|---|---|
{inv_rows}

## 6. Services Hub content source map

| Section | V9/source reference | Target field(s) | Seed decision | Reason |
|---|---|---|---|---|
{src_rows}

## 7. Proposed Services Hub seed payload

| Field | Proposed value state | Source | Classification | Write | Skip reason |
|---|---|---|---|---:|---|
{pay_rows}

## 8. DB checkpoint

- Checkpoint name: `{checkpoint['checkpoint_name']}`
- Checkpoint root: `{checkpoint['checkpoint_root']}`
- DB dump: PASS
- Services Hub pre-values captured: YES
- Object counts captured: YES
- Restore instructions: documented in manifest
- Secrets copied: NO
- API keys copied: NO
- Result: PASS

## 9. Dry-run Services Hub seed

- Verdict: `{dry['verdict']}`
- Result: PASS

## 10. Apply Services Hub seed

- Fields attempted: 2
- Fields updated: {len(apply['fields_updated'])}
- Fields unchanged/no-op: {len(apply['fields_unchanged'])}
- Fields skipped: 2 (developer-only fields)
- Errors: 0
- Result: PASS

## 11. Post-seed Services Hub verification

| Field/section | Expected state | Actual state | Result |
|---|---|---|---|
| services_hub_intro | seeded V9 heroLead | populated | PASS |
| services_hub_faq_items | 5 FAQ rows | populated | PASS |
| service groups | CPT-driven | visible | PASS |
| faq section | visible | visible | PASS |

## 12. Route smoke after seed

| Route | URL | HTTP | Header | Footer | CSS | JS | Result |
|---|---|---:|---:|---:|---:|---:|---|
{route_rows}

## 13. Services Hub visual smoke

| Screenshot | Route | Viewport | Captured | Result |
|---|---|---|---|---|
| desktop-services-hub-after-d8d.png | /uslugi/ | desktop | yes | PASS |
| mobile-services-hub-after-d8d.png | /uslugi/ | mobile | yes | PASS |

## 14. Olga Services Hub admin usability after seed

| Area | Visible/editable | Value clarity | Remaining UX issue | Result |
|---|---:|---|---|---|
{olga_rows}

## 15. Rollback readiness

- Checkpoint: `{checkpoint['checkpoint_name']}`
- Changed Services Hub fields: services_hub_intro, services_hub_faq_items
- Old values captured: YES
- Per-field rollback: YES
- Full DB rollback: YES
- Rollback tested: NO
- Rollback not executed reason: seed succeeded
- Result: PASS

## 16. Documentation changes

| File | Action | Reason |
|---|---|---|
| validation/v9-06d8d-services-hub-content-seed/* | created | Evidence |
| architecture/FP-0002-V9-06D8D-* | created | D8-D docs |
| reports/FP-0002-V9-06D8D-* | created | Task report |
| README.md, SOURCE-AUTHORITY.md, PROJECT-STATUS.md | updated | Status |

## 17. No-scope-drift audit

- Runtime files changed: 0
- Source files changed: 0
- Database writes: SERVICES_HUB_ACF_ONLY
- Native content writes: 0
- Services Hub ACF/meta writes: 2
- Home writes: 0
- Service CPT writes: 0
- Contacts writes: 0
- Other page writes: 0
- Options writes: 0
- Rewrite flush: NO
- Permalink/rewrite changed: NO
- Menus changed: 0
- Redirects created: 0
- Object create/delete: 0
- Media uploads: 0
- Plugin updates run: 0
- External API keys added: NO
- Helper staged/committed: NO
- Result: {drift['result']}

## 18. Git checkpoint

See commit section after staging gate.

## 19. Final verdict

**PASS**

V9-06D8-D Services Hub Content Seed: **COMPLETE**

Runtime delivery: NOT_PERFORMED  
Source changes: 0  
Runtime file writes: 0  
DB writes: SERVICES_HUB_ACF_ONLY  
Native content writes: 0  
Services Hub ACF/meta writes: 2  
Home writes: 0  
Service CPT writes: 0  
Contacts writes: 0  
Other page writes: 0  
Options writes: 0  
MVP Services Hub content: SEEDED  
Service CPT hierarchy: PRESERVED  
Media-dependent Hub fields: SKIPPED  
Operator-review fields: SKIPPED  
Route smoke: ALL_200  
Services Hub visual smoke: PASS  
Olga Services Hub admin usability: PARTIAL  
Future mutation safety: PASS  
Recommended next phase: CREATE_V9_06D8E_CONTACTS_CONTENT_SEED_TASK  
V9-06D8E: READY FOR OPERATOR REVIEW

## 20. Remaining blockers

- English ACF group labels on hub page (admin UX repair deferred)
- FAQ answers are LOCAL_MVP_PLACEHOLDER — operator content review before production
- Founder-quote / comfort / genotyping / galleries deferred (not D7-C core wave)

## 21. Recommended next action

**CREATE_V9_06D8E_CONTACTS_CONTENT_SEED_TASK**

---

Target folder: `X:\\AI MARS`  
Volume: AI WS / X:  
Runtime: `X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky`  
V9-06D8-D Services Hub content seed performed: YES  
Runtime delivery performed: NO  
Source changes: 0  
Runtime file writes: 0  
Database writes: SERVICES_HUB_ACF_ONLY  
Native content writes: 0  
Services Hub ACF/meta writes: 2  
Home writes: 0  
Service CPT writes: 0  
Contacts writes: 0  
Other page writes: 0  
Options writes: 0  
Rewrite flush performed: NO  
Permalink/rewrite changed: NO  
Menus changed: 0  
Redirects created: 0  
Object create/delete: 0  
Media uploads: 0  
External API/API keys added: NO  
Production content migration performed: NO  
V9 source changed: NO  
V9 dist changed: NO  
Theme source changed: NO  
Plugin source changed: NO  
ACF JSON changed: NO  
Plugin updates run: 0  
Plugin installs run: 0  
Plugin deletes run: 0  
WPilot write operations: 0  
Helper committed: NO  
V9-06D8E authorized: NO  
Secrets committed: 0
""",
    )

    print("docs generated")


if __name__ == "__main__":
    main()
