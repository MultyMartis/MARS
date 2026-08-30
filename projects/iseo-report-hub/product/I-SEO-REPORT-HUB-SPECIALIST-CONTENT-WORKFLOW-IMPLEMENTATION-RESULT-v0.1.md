# I-SEO Report Hub — Specialist Content Workflow Implementation Result v0.1

**Status:** IMPLEMENTED (local MVP)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-26  
**Wave:** Specialist Report Content Workflow Implementation 01  
**Parent charter:** [I-SEO-REPORT-HUB-SPECIALIST-REPORT-CONTENT-WORKFLOW-CHARTER-v0.1.md](I-SEO-REPORT-HUB-SPECIALIST-REPORT-CONTENT-WORKFLOW-CHARTER-v0.1.md)  
**Parent plan:** [I-SEO-REPORT-HUB-SPECIALIST-CONTENT-WORKFLOW-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-SPECIALIST-CONTENT-WORKFLOW-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Implemented routes

| Method | Path | Behavior |
|--------|------|----------|
| GET | `/monthly-reports/{id}/content-workflow` | Friendly section cards; login required; roles `seo_specialist`, `seo_lead_reviewer`, `admin_owner` |
| POST | `/monthly-reports/{id}/content-workflow/sections/{sectionKey}` | Save one allowed section; CSRF; specialist only when parent not finalized |
| existing | `/monthly-reports/{id}` | CTA **Тексты отчета** when editable context |
| existing | `/monthly-reports/{id}/preview` | Reflects saved block body |
| existing | `/report-blocks/{id}/edit` | Remains denied for `seo_specialist` (403) |

---

## 2. Role behavior

| Role / state | GET workflow | POST save | Raw block edit |
|--------------|--------------|-----------|----------------|
| `seo_specialist` + `in_progress` / `draft` / `ready_for_review` | Editable cards | Allowed for allowlisted keys | Denied |
| `seo_specialist` + `finalized` | Read-only notice | Denied | Denied |
| `seo_lead_reviewer` / `admin_owner` | Allowed (compatibility) | Allowed when not finalized | Unchanged (existing raw editor) |

Finalized message: **Отчет финализирован. Тексты доступны только для просмотра.**

---

## 3. Data / write model actually used

- **No migration.** No new tables.
- Primary write: `report_blocks.body` for stable `block_key`.
- Mirror: allowlisted flat columns on `monthly_report_contents` (`executive_summary`, `work_completed`, `results_summary`, `key_findings`, `risks_and_blockers`, `next_month_plan`).
- Missing block: page shows warning **Раздел пока не найден в структуре отчета.** — **no auto-create** in this wave.
- Audit events: `report_block.specialist_content_saved`, `monthly_report_content.specialist_section_mirrored`.
- Does **not** create PDF / export / share / snapshot.

---

## 4. Section policy implemented

| Key | Label |
|-----|-------|
| `executive_summary` | Краткое резюме |
| `work_completed` | Что сделали |
| `results_summary` | Результаты |
| `key_findings` | Ключевые выводы |
| `risks_and_blockers` | Риски и блокеры |
| `next_month_plan` | План на следующий месяц |

Deferred: `client_notes`, `internal_notes`.

---

## 5. Assembly hints

- Loaded via existing `MonthlyReportSummaryAssemblyService` (preview/format path) — **read-only hints**.
- UI panel **Черновик из работ за месяц**; optional client-side **Подставить в поле** (no auto DB write).
- User must click **Сохранить раздел** to persist.

---

## 6. Validation write result

- Section: `key_findings` on monthly content id **8**.
- Block id **25**; body length 205 → 257.
- Flat mirror `key_findings` length 257; text matches block body.
- Marker: `Проверено через локальный редактор текстов отчета.`
- Preview reflects marker.
- July id **7** unchanged; work entries 23 unchanged; snapshots/exports/shares **0**.

---

## 7. Remaining backlog

- Specialist Content Workflow Review Pass 01 (visual / copy polish).
- Admin/lead visual review of the same page.
- Richer assembly hints if needed.
- PDF / export / share remain parked.
- Production / host config remains paused.

---

## 8. What was not touched

- Host / production
- DB schema
- PDF / export / share / snapshot pipelines
- Work-entry form UX polish 02
- `.env.local` / credentials
- Foreign WIP outside i-SEO Report Hub
