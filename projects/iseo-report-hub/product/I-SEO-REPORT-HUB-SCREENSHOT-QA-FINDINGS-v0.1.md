# i-SEO Report Hub — Screenshot QA Findings v0.1

**Wave:** Screenshot QA Fix Charter 01  
**Evidence run:** Automated Screenshot Capture 01  
**Date:** 2026-08-21  
**Scope:** triage / findings only — **no** app-source / runtime / DB mutation in this wave

---

## Evidence

| Field | Value |
|-------|-------|
| **Screenshot folder** | `X:\AI MARS STORAGE\incoming\iseo-report-hub\automated-screenshot-capture-01\20260821-010501` |
| **Index** | `SCREENSHOT-INDEX.md`, `SCREENSHOT-INDEX.json` |
| **URL map** | `URL-MAP-FOR-OPERATOR.md` |
| **Captured count** | **16** full-page PNG @1920 |
| **Prior QA prep** | App Pages Visual QA Preparation 01 (`09921d94` / tip `1deadfeb`) |
| **Operator decision** | PDF / export regeneration **deferred**; export 4 frozen; no share mutation |

Screenshots reviewed (all 16):

`01_login.png` … `16_404.png` (see index).

---

## Direction OK (not in P0 queue)

- Login — visually acceptable.
- Dashboard — generally acceptable.
- Work entry create/edit — readable fields.
- Summary Assembly Preview — usable vs earlier state.
- Client preview / print — document direction correct; content quality separate.
- Exports / shares — acceptable as internal pages for now.

---

## P0 findings

### P0-1 — Fixture markers visible in normal UI

| Field | Value |
|-------|-------|
| **Screenshots** | `03_reporting_periods.png`, `04_monthly_report_1_detail.png`, `05_monthly_report_1_work_entries.png`, `06_work_entry_create.png`, `07_work_entry_edit.png`, (also titles/notes on related monthly surfaces) |
| **Visible symptom** | Strings like `LOCAL_FIXTURE_ONLY` appear in period titles, monthly report titles/details, work-entry parent banners, content lists, notes, block labels. Example: `Demo August 2026 LOCAL_FIXTURE_ONLY edited`. |
| **Expected** | Technical fixture markers **not** visible in normal manager/client UI. DB may keep markers; render layer must hide/sanitize. Markers may remain only inside collapsed technical/debug details if useful. |
| **Likely area** | Extend / centralize sanitizer beyond `ClientReportDocument::stripFixtureMarkers()`; apply in reporting-periods list, monthly report show, work-entry form header, assembly preview labels, client document titles/bodies. |
| **Safety** | **Render-only** in P0. No DB UPDATE of titles/blocks. |

### P0-2 — Bad demo / test garbage content

| Field | Value |
|-------|-------|
| **Screenshots** | `09_client_preview.png`, `10_client_preview_print.png`, `15_monthly_report_5_preview.png` (also mirrored in monthly detail content areas) |
| **Visible symptom** | Client-facing sections show test junk: `Updated body`, `Risks body`; report 5 preview shows numeric junk (`78678`, `786786`, `6786`, `786`). |
| **Expected** | Client preview and demo report show calm empty states or normal SEO-demo copy — not obvious test garbage. |
| **Likely area** | `ClientReportDocument` body formatting + empty-state fallbacks; optional shared “junk body” detector for display. |
| **Safety** | Prefer **render-layer** empty/demo fallbacks in P0. True DB content replacement → separate local-only cleanup wave with backup (not this charter’s implementation). |

### P0-3 — Empty yellow action buttons on reporting periods

| Field | Value |
|-------|-------|
| **Screenshots** | `03_reporting_periods.png` (also similar yellow pills may appear in other data tables) |
| **Visible symptom** | Actions column shows solid yellow pills with **no readable label**; secondary «Изменить» is visible. |
| **Expected** | Labels like `Открыть` / `Изменить` clearly readable; or remove redundant CTA. No empty pills. |
| **Likely area** | View already contains text `Открыть` in `reporting-periods/index.php`; CSS override `.data-table .actions a { color: var(--color-accent); }` paints yellow text on yellow `.btn-primary` background → appears empty. Fix specificity / button text color; confirm GET links only. |
| **Safety** | CSS/view only. No POST. |

### P0-4 — Technical / English 404

| Field | Value |
|-------|-------|
| **Screenshots** | `16_404.png` |
| **Visible symptom** | Card shows `404 — Not Found`, `No route matches …`, `Phase 1A exact-path router only…`, button `Dashboard`. Shell title already Russian. |
| **Expected** | Friendly Russian: heading `Страница не найдена`; body `Такой страницы нет или ссылка устарела.`; button `На главную`. Hide router internals from normal view (optional collapsed tech details). |
| **Likely area** | `app/Views/pages/not-found.php` (+ CSS if needed). Do **not** rewrite router matching logic. |
| **Safety** | View-only. Keep HTTP 404. |

---

## P1 findings

### P1-1 — Monthly report detail too technical by default

| Field | Value |
|-------|-------|
| **Screenshots** | `04_monthly_report_1_detail.png`, `05_monthly_report_1_work_entries.png`, `14_monthly_report_5_empty.png` |
| **Symptom** | Long operational page: diagnostics, readiness checks, raw content lists, fixture text in open UI. |
| **Expected** | Manager-friendly default; technical blocks collapsed; dangerous actions clear; no fixture/test garbage in primary view. |
| **Queue** | After P0 sanitizer + content fallbacks; may be separate UX collapse wave. |

### P1-2 — Report 5 empty/draft looks broken

| Field | Value |
|-------|-------|
| **Screenshots** | `14_monthly_report_5_empty.png`, `15_monthly_report_5_preview.png` |
| **Symptom** | Numeric junk in preview; empty/draft still feels half-broken. |
| **Expected** | Clean empty draft, exclude from primary demo path, or normal demo empty states. |
| **Queue** | P0 render fallbacks cover client-visible junk; deeper fixture/demo path decision may stay parked. |

### P1-3 — Client preview layout OK, content not show-ready

| Field | Value |
|-------|-------|
| **Screenshots** | `09_client_preview.png`, `10_client_preview_print.png` |
| **Symptom** | Document layout good; section bodies include test strings. |
| **Expected** | After content cleanup (render and/or later DB), usable as local demo. |
| **Queue** | P0 addresses visible junk; polish / demo narrative can follow. |

---

## P2 findings

| ID | Topic | Notes |
|----|-------|-------|
| P2-1 | Exports / shares polish | Internal pages acceptable; later UI polish. |
| P2-2 | PDF / export pipeline | **Deferred** by operator — no regen, no export 4 change. |
| P2-3 | Mobile / responsive QA | Deferred. |

---

## Out of scope for this findings doc

- Implementation.
- DB mutation.
- Export / share / PDF mutation.
- Public share token routes.
