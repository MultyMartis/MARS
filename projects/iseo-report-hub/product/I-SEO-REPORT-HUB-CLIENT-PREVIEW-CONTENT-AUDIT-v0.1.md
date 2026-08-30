# I-SEO Report Hub — Client Preview Content Audit v0.1

**Status:** charter audit (docs only)  
**Date:** 2026-08-21  
**Scope:** client-facing preview content readiness for local demo show  
**Not in scope:** implementation, DB mutation, PDF/export/share

---

## 1. Routes under review

| Route | Role |
|-------|------|
| `/monthly-reports/1/preview` | Internal client preview (report 1, finalized demo) |
| `/monthly-reports/1/preview/print` | Print layout of the same document |

Related (regression / contrast only):

| Route | Role |
|-------|------|
| `/monthly-reports/5/preview` | Empty draft preview — must stay calm empty |
| `/monthly-reports/1` | Manager detail — accepted after P1 collapse |
| `/health` | Local MVP health — accepted after refresh |

---

## 2. Current visual state

### Accepted (layout / chrome)

- Paper-like client document layout is acceptable.
- No admin chrome in the document body.
- Six-section order is correct (`executive_summary` → `results_summary` → `work_completed` → `key_findings` → `risks_and_blockers` → `next_month_plan`).
- Cover meta (client, project, site, period, status, date) is readable.
- Local demo label and draft disclaimer patterns exist where appropriate.
- Report 5 empty-draft preview is intentionally clean after Report 5 Draft Path Cleanup + Health Refresh Implementation 01.

### Not show-ready (content)

- Report 1 client preview is **too dry** for Nikita / manager / internal demo.
- Most body sections render **calm empty / fallback** messages after P0 sanitizer strips fixture junk.
- Document looks finished as a shell, but **not** as a finished SEO report.
- No fake KPI numbers are shown today (good) — but there is also almost no substantive narrative.

### Evidence (screenshots)

- Report 1 client preview (P0 after):  
  `X:\AI MARS STORAGE\incoming\iseo-report-hub\screenshot-qa-p0-fix-implementation-01\20260821-023143\09_client_preview_after.png`
- Report 1 print (P0 after):  
  `X:\AI MARS STORAGE\incoming\iseo-report-hub\screenshot-qa-p0-fix-implementation-01\20260821-023143\10_client_preview_print_after.png`
- Report 5 preview (cleanup after):  
  `X:\AI MARS STORAGE\incoming\iseo-report-hub\report-5-draft-path-cleanup-health-refresh-implementation-01\20260821-041956\15_monthly_report_5_preview_after_cleanup.png`

Observed empty/fallback pattern on report 1 preview (typical):

| Section | Typical visible copy today |
|---------|----------------------------|
| Краткое резюме | «Раздел будет заполнен после ручной редакции.» |
| Результаты | «Метрики и результаты не заполнены…» |
| Что сделали | empty / manual-edit fallback |
| Ключевые выводы | empty / manual-edit fallback |
| Риски и блокеры | calm “no significant risks” fallback |
| План на следующий месяц | empty / manual-edit fallback |

---

## 3. Source data available (local context)

From accepted programme state / prior waves (not re-mutated in this charter):

| Fact | Value |
|------|--------|
| Report id 1 status | **finalized** / issued context |
| Report id 1 blocks | **6** section shells |
| Report id 1 work entries | **7** fixture-shaped entries |
| Report id 5 | **draft / empty** (0 blocks / 0 work entries intended) |
| Exports total | **4** (export **4** frozen) |
| Shares | frozen for this track (no create/revoke) |
| PDF / export regeneration | **deferred** by operator |

Assembly capability (already implemented):

- `MonthlyReportSummaryAssemblyService` can draft **three auto sections** from work entries:
  - `work_completed`
  - `next_month_plan`
  - `risks_and_blockers`
- Manual-only shells remain:
  - `executive_summary`
  - `results_summary`
  - `key_findings`
- Apply to finalized report 1 is **blocked** (correct safety).
- Client preview mapper (`ClientReportDocument`) reads assemble payload only; does **not** write DB; does **not** feed export/PDF today.

Work-entry themes available for honest demo narrative (fixture sample titles):

- technical monitoring;
- indexation check;
- semantic update;
- commercial factor recommendations;
- planned meta-tag refinement;
- planned new texts;
- risk: priority pages need agreement.

---

## 4. Why this matters

- Manager detail UX is already demoable; client preview is the **client-facing proof**.
- Empty fallbacks communicate “system works but report is blank,” not “this is what a monthly SEO report looks like.”
- For Nikita / шеф / internal team, the page must demonstrate **value of the finished client document**, without inventing traffic/position/lead KPIs and without touching frozen export 4 / shares.

---

## 5. Root cause (product, not layout)

| Layer | State |
|-------|--------|
| Visual template | Acceptable |
| Sanitizer / junk removal | Working (P0) — strips unsafe fixture text |
| Manual block bodies on report 1 | Sparse / sanitized empty after cleanup |
| Auto sections in DB | Not necessarily filled with client-ready text for preview (apply blocked on finalized) |
| Metrics model | Deferred — cannot honestly fill “Результаты” with numbers |

Therefore: **show-ready content is a render/demo policy problem for Implementation 01**, not a PDF problem and not a layout problem.

---

## 6. Constraints that shape the fix

- Do not mutate report 1 blocks / reopen / re-finalize.
- Do not regenerate PDF / create export / change export 4.
- Do not mutate shares or print share tokens.
- Do not regress report 5 empty-draft calm states.
- Prefer reversible local/demo render fallback over DB writes.

---

## 7. Audit verdict

**Layout:** accepted.  
**Content for demo show:** not ready.  
**Safe next step:** Option A — render-layer show-ready local demo fallback (see strategy doc).
