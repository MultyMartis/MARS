# I-SEO Report Hub — Specialist Content Workflow Implementation Plan v0.1

**Status:** IMPLEMENTATION PLAN — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-26  
**Parent charter:** [I-SEO-REPORT-HUB-SPECIALIST-REPORT-CONTENT-WORKFLOW-CHARTER-v0.1.md](I-SEO-REPORT-HUB-SPECIALIST-REPORT-CONTENT-WORKFLOW-CHARTER-v0.1.md)  
**Target wave name:** `I-SEO Report Hub — Specialist Report Content Workflow Implementation 01`

---

## 1. Scope (in)

- New specialist-friendly content workflow for monthly report **August id 8** (primary target).  
- Route/page/UI + service write path for allowed section texts.  
- CTA on monthly show for specialist flow.  
- Local validation + screenshots.  
- Keep raw block editor denied for `seo_specialist`.

## 2. Scope (out)

- Host / production deploy  
- DB schema migration (none expected)  
- PDF / export / share / snapshot generation  
- AI summary generation  
- Work Entry Form UX Polish 02  
- Broad reviewer finalization redesign  
- Exposing `assembly-preview` as primary specialist UI (hints may be embedded; full apply UI stays lead-oriented unless explicitly narrowed)

---

## 3. Exact routes / pages

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/monthly-reports/{id}/content-workflow` | Friendly section cards |
| POST | `/monthly-reports/{id}/content-workflow` | Per-section save (or save-all if forced; prefer per-section) |
| existing | `/monthly-reports/{id}` | Add CTA **Тексты отчета** |
| existing | `/monthly-reports/{id}/preview` | Verify text after save |
| existing | `/report-blocks/{id}/edit` | Must remain 403 for specialist |

Suggested controller: extend `MonthlyReportContentController` **or** new `MonthlyReportContentWorkflowController` (prefer dedicated controller to avoid bloating show/edit).

Suggested view: `Views/pages/monthly-reports/content-workflow.php`.

Suggested service method(s):

- load section DTOs from blocks (+ flat fallback)  
- `saveSection(user, monthlyId, blockKey, body)` with role + status guards + flat mirror  

Reuse (read-only): `MonthlyReportSummaryAssemblyService::preview` / `formatBlockBody` for auto-section hints.

---

## 4. Data backup requirements

Before first write:

1. Confirm volume `AI WS` and local DB `iseo_report_hub_dev`.  
2. Dump at least:

```text
monthly_report_contents
report_blocks
monthly_report_work_entries
```

3. Store dump under Storage incoming (not git), e.g.:

`X:\AI MARS STORAGE\incoming\iseo-report-hub\specialist-report-content-workflow-implementation-01\<timestamp>\db-backup.sql`

4. Record row counts for monthly 7/8 before/after.

Rollback: restore dump if specialist write corrupts demo texts.

---

## 5. Auth / write rules (implement exactly)

| Actor | Parent not finalized | Parent finalized |
|-------|----------------------|------------------|
| `seo_specialist` | save allowed section bodies | deny mutation |
| `admin_owner` / `seo_lead_reviewer` | save + raw editor | follow existing reopen/admin locks |
| others | read if list-allowed; no specialist workflow mutate | — |

Writable keys MVP:  
`executive_summary`, `results_summary`, `work_completed`, `key_findings`, `risks_and_blockers`, `next_month_plan`.

Do **not** accept POST fields: `block_key`, `data_json`, `source_metric_refs`, `block_type`, `sort_order`.

---

## 6. Validation routes (local)

Login as demo specialist `test@mail.ru` (password not recorded in commits).

| Check | Expected |
|-------|----------|
| GET `/monthly-reports/8` | 200; CTA **Тексты отчета** visible |
| GET `/monthly-reports/8/content-workflow` | 200; section cards; no JSON fields |
| POST save one section on 8 | 302/200 success; body persisted on block + flat |
| GET `/monthly-reports/8/preview` | updated text visible |
| GET `/monthly-reports/7/content-workflow` | read-only or mutation denied |
| POST mutate on 7 as specialist | denied |
| GET `/report-blocks/22/edit` (or August block id) as specialist | branded 403 |
| snapshots/exports/shares counts | remain 0 |

---

## 7. Screenshots to capture

Under Storage evidence (not git):

1. August detail with **Тексты отчета**  
2. Content workflow page (full)  
3. One section in edit state  
4. After-save confirmation / reloaded card  
5. Client preview reflecting change  
6. July finalized lock / read-only  
7. Access denied raw block edit  

---

## 8. What not to touch

- Host `reports.i-seo.su`  
- `.env.local` secrets  
- PDF/export/share controllers beyond leaving parked  
- Foreign WIP outside `projects/iseo-report-hub/`  
- Broad git add  
- Demo user password changes  
- Invented production metrics claims  

---

## 9. Suggested file touch list (Implementation 01)

Exact list may vary; expected:

- `app-source/app/routes.php`  
- new or extended controller under `app-source/app/Controllers/`  
- service method(s) under `app-source/app/Services/`  
- `app-source/app/Views/pages/monthly-reports/content-workflow.php`  
- `app-source/app/Views/pages/monthly-reports/show.php` (CTA only)  
- optional small CSS if required for cards  
- product result + REPORT docs  

Runtime sync: Model A source → runtime only as chartered in implementation wave.

---

## 10. Done definition

Implementation 01 is done when:

1. Charter acceptance criteria pass locally.  
2. Docs/report committed (exact paths).  
3. No host; no PDF/export/share rows created.  
4. Tip HEAD recorded; push none unless separately authorized.
