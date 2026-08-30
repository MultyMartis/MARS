# I-SEO Report Hub — Browser Demo UX Fix Review Pass v0.1

**Date:** 2026-08-24  
**Wave:** Browser Demo UX Fix Review Pass 01  
**Status:** BROWSER DEMO UX FIX REVIEW PASS_WITH_RESIDUALS  
**Scope:** local browser QA + screenshots only (no app-source, no runtime edit, no host, no PDF/export/share)

## Screenshot folder

`X:\AI MARS STORAGE\incoming\iseo-report-hub\browser-demo-ux-fix-review-pass-01\20260824-161254\`

Browser mode: Edge Chromium fallback (Firefox Developer persistent profile launch timed out; screenshots still valid at 1920 full-page).

## Route list

| Route | Expected | HTTP | Screenshot |
|-------|----------|------|------------|
| `/login` | login form | 200 | `01_login.png` |
| `/` | specialist dashboard | 200 | `02_dashboard.png` |
| `/reporting-periods` | periods list | 200 | `03_reporting_periods.png` |
| `/monthly-reports/7` | July finalized detail | 200 | `04_july_detail.png` |
| `/monthly-reports/7/preview` | July preview | 200 | `05_july_preview.png` |
| `/monthly-reports/8` | August in-progress detail | 200 | `06_august_detail.png` |
| `/monthly-reports/8/preview` | August preview | 200 | `07_august_preview.png` |
| `/monthly-reports/8/work-entries/create` | create work | 200 | `08_august_work_entry_create.png` |
| `/monthly-report-work-entries/28/edit` | edit August work | 200 | `09_august_work_entry_edit.png` |
| `/reporting-periods/create` | denied | 403 | `10_period_create_denied.png` |
| `/monthly-reports/8/edit` | denied | 403 | `11_monthly_report_edit_denied.png` |
| `/report-blocks/22/edit` | denied | 403 | `12_block_edit_denied.png` |

## Assertions summary

- Global / dashboard / periods / July / August / work forms / restricted routes: **PASS** after visual confirmation.
- One automated keyword miss on July read-only notice (`july:readonly_notice`) — **visual PASS** (badge «Только для чтения — заблокировано» + banner «Заблокировано. Отчет финализирован… только для просмотра»).
- Login flash: **`Вход выполнен.`** (no English «Signed in successfully.»).
- Stale export/share paths absent; parked PDF/share copy present.
- Work entry id **28** and block id **22** confirmed present.

Evidence files: `UX-FIX-REVIEW-ASSERTIONS.md`, `route-status-review.json`, `db-counts-before.json`, `db-counts-after.json`, `REVIEW-FINDINGS.md`.

## Visual review summary

1. Specialist dashboard is focused on `ПРОВЕРКА.рф`; system status collapsed; not a primary CTA.
2. Periods page has no «Создать период»; helper does not promise live files/PDF/share.
3. July is clearly finalized/read-only for `seo_specialist`; no add/edit work; preview available.
4. August is clearly editable via work entries; primary actions add work + client draft preview.
5. Previews are credible and free of admin/raw marker clutter.
6. Restricted routes return clean Russian 403 pages without stacks.
7. Screenshots are ready for Web-GPT / operator visual review.

## Residual issues

| Priority | Item |
|----------|------|
| P1 | none |
| P2 | Work-entry form still dense (many fields + help icons); catalogue-first polish deferred |
| P2 | 403 pages are safe but minimal/unbranded |
| P3 | Firefox profile automation flaky; Edge fallback used for this pack |

## Recommended next action

**Web-GPT Visual Review of UX Fix Screenshots**

Optional follow-up after visual accept: `I-SEO Report Hub — Work Entry Form UX Polish 01`.
