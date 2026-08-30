# i-SEO Report Hub — Report 5 Current State Audit v0.1

**Wave:** Report 5 Draft Path Cleanup Charter 01  
**Date:** 2026-08-21  
**Scope:** read-only audit (docs / screenshots / source / optional DB GET)  
**Not:** implementation, DB mutation, seed, delete, export/PDF/share

---

## Object

| Field | Value |
|-------|-------|
| **Monthly report id** | `5` |
| **Routes** | `GET /monthly-reports/5`, `GET /monthly-reports/5/preview` |
| **Related period** | `reporting_period_id` **3** · `period_key` **2026-08** · status **archived** |
| **Report status** | **draft** (`finalized_at` NULL) |
| **Title (DB)** | contains fixture marker suffix (`LOCAL_FIXTURE_ONLY`) — render-layer sanitizer should strip for normal UI |

---

## Counts (local DB read-only probe, 2026-08-21)

| Metric | Report 5 | Report 1 (contrast) |
|--------|----------|---------------------|
| Status | `draft` | `finalized` |
| Report blocks | **0** | **6** |
| Work entries | **0** | **7** |
| Snapshots | **0** | **1** |
| Exports | **0** | **4** (all local exports) |
| Shares | **none on report 5** | shares attach via report 1 exports (totals: 7 shares / 1 active / 6 revoked) |

**Content columns on report 5 row:** short non-empty lengths remain on several text fields (`executive_summary` / `work_completed` / `results_summary` / `key_findings` lengths 5/4/6/3; risks/plan empty). These are the historical numeric/test fragments. **P0 render sanitizer** treats them as demo junk and replaces with calm section fallbacks on client preview — **without** clearing DB.

**Export 4** belongs to report 1 path; size/checksum context unchanged (`117055` / prefix `a8c4d61c6216`). **Do not** touch.

---

## Evidence

### Before P0 (broken / junk-looking)

| File | Route | What operator saw |
|------|-------|-------------------|
| `X:\AI MARS STORAGE\incoming\iseo-report-hub\automated-screenshot-capture-01\20260821-010501\14_monthly_report_5_empty.png` | `/monthly-reports/5` | Draft + archived period; readiness checklist with multiple red fails (no active blocks / missing mandatory blocks); work counters 0; content list showed numeric/test fragments; blocks empty |
| `...\20260821-010501\15_monthly_report_5_preview.png` | `/monthly-reports/5/preview` | Client document layout with numeric junk in first sections (`78678`, `786786`, `6786`, `786`); calm fallbacks only on some empty sections |

### After P0 (preview calmed; deeper draft UX still weak)

| File | Route | What operator saw |
|------|-------|-------------------|
| `X:\AI MARS STORAGE\incoming\iseo-report-hub\screenshot-qa-p0-fix-implementation-01\20260821-023143\15_monthly_report_5_preview_after.png` | `/monthly-reports/5/preview` | Calm RU empty states for all six sections; status **Черновик**; draft disclaimer present; **no** numeric junk in normal visible preview |
| P0 index / assertions | same folder | Preview listed as calm empty; forbidden P0 strings absent on assert pages |

### After P1 (report 1 focus; report 5 detail not re-shot)

P1 monthly detail UX collapse improved manager IA on `/monthly-reports/{id}` (validated primarily on report **1**). Report **5** inherits the same layout, but **no dedicated empty-draft framing** was added. Fresh authenticated screenshot of `/monthly-reports/5` after P1 was **not** captured in this charter — treat post-P1 detail presentation for id 5 as **inferred from source + prior evidence**.

---

## What the operator sees today (synthesis)

### `/monthly-reports/5`

- Valid draft row for archived smoke period `2026-08`.
- **0** blocks / **0** work entries → empty operational object.
- Manager summary/workflow from P1 applies (status draft, PDF/link not ready, work-entries empty, diagnostics collapsed).
- Finalization readiness still **fails** for missing blocks — correct technically, but without an explicit “empty draft” story it can still feel like a broken checklist object rather than an intentional empty workspace.
- Title/period labels may still carry fixture history in DB; normal UI should use `UiTextSanitizer` / `ui_display_label`.

### `/monthly-reports/5/preview`

- After P0: **acceptable calm empty client document** (six section fallbacks + draft note).
- Remaining gap vs target charter UX: stronger empty-draft framing on manager side and list/period demotion — not reintroducing junk.

### Period / list surfaces

- `/reporting-periods` lists **periods**, not monthly report ids. Period **3** (`2026-08`) is **archived** and owns report 5.
- `/reporting-periods/3` shows monthly report card with sanitized title + status badge only — **no** “пустой черновик / без работ” demotion label yet.

---

## Why it looks confusing

1. **Dual demo objects:** report **1** (finalized, rich) vs report **5** (empty draft on archived period) without a clear product role label.
2. **Historical junk** still lives in DB content fields even though preview sanitizes them.
3. **Readiness fails** are expected for empty drafts but read as “broken report” if shown as the primary story.
4. **Archived period + draft report** pairing is easy to misread as abandoned smoke debris.

---

## What must not be done (this charter and next impl wave)

- **No** delete of report 5  
- **No** SQL cleanup / hide-by-query  
- **No** fake seed of blocks/work entries in this UX wave  
- **No** mutation of report 1  
- **No** snapshot/export/share/PDF mutation; **no** export 4 change  
- **No** auto-create blocks or work entries on open  

---

## Source anchors (read-only)

- `app/Views/pages/monthly-reports/show.php` — P1 manager IA; no empty-draft special case  
- `app/Views/pages/reporting-periods/index.php` — period list badges only  
- `app/Views/pages/reporting-periods/show.php` — monthly card without emptiness demotion  
- `app/Support/ClientReportDocument.php` + `UiTextSanitizer.php` — calm empty section fallbacks (P0)  
- Controller note: monthly detail is served by `MonthlyReportContentController` (not a separate `MonthlyReportController.php`)

---

## Audit verdict

Report 5 is a **valid local draft** with **0/0** operational payload, **no** delivery artifacts, and **preview largely fixed by P0**. Remaining problem is **product/UX framing** of the empty draft path (manager detail + period card demotion), not deletion or DB reseeding.
