# REPORT — I-SEO REPORT HUB REPORT PREVIEW / RENDER CHARTER 01

**Status:** COMPLETE (docs/policy only)  
**project_id:** `iseo-report-hub`  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Preview / Render Charter 01  
**Primary commit:** `f9604d4b103ed984aaa83382ee87ee60c865e28c`  
**Hash-record commit:** `PENDING_AFTER_HASH_RECORD`

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `5c65ac8817e94ad146c7aee80d876b2290e65ef5` |
| Staged/index before | **empty** |
| i-SEO WIP before | **clean** (`projects/iseo-report-hub/` no modified/untracked) |
| Foreign WIP | **preserved** (untouched) |
| Write scope | Active Brain docs only under allowlisted `product/` + `reports/` + `OPERATIONAL-INDEX.md` |

HEAD matched Report Blocks CRUD hash-record `5c65ac88`. No STOP.

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| Report Blocks CRUD primary | `135da2137cef401e16225b8f1e653dfbe3e18699` — `feat(iseo-report-hub): add report blocks crud` |
| Report Blocks CRUD hash-record | `5c65ac8817e94ad146c7aee80d876b2290e65ef5` |
| Push (blocks CRUD) | **no** |
| Smoke (blocks CRUD) | **42/42 PASS** (per prior closeout) |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Counts (read-only this wave) | migrations **5**; tables **13**; users **1**; roles **6**; clients/projects/sites **1/1/1**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **6** |
| Parent monthly | id **1**; period `2026-07`; status `in_progress`; title/markers `LOCAL_FIXTURE_ONLY`; sources `[1,2,3,7]` |
| Blocks | `executive_summary` id **1** `in_progress` sort **15**; + `work_completed`/`results_summary`/`key_findings`/`next_month_plan`; + `risks_and_blockers` id **9** draft sort **35** |
| Current limitation | **No** rendered monthly report preview; **no** preview route/service/view; **no** print/PDF/public share |

This charter wave did not mutate DB.

---

## 3. Charter Output

Created/updated:

- `product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-report-preview-render-charter-01.md` (this file)
- `OPERATIONAL-INDEX.md` — Report Preview / Render Charter status; baseline on Report Blocks CRUD; next = Implementation 01; no code/runtime/DB in charter

---

## 4. Render Design Summary

| Area | Design |
|------|--------|
| Routes | `GET /monthly-reports/{id}/preview` (required); optional `GET …/preview/print` |
| Data sources | Period (+ client/project/site) + monthly row (DB-05) + non-archived blocks (DB-06) + weekly sources |
| Block order | `sort_order ASC`, then `id ASC` |
| Inclusion | draft/in_progress/reviewed/approved (non-archived) with status labels |
| Exclusion | archived excluded by default |
| Fallback | Blocks primary when any non-archived blocks exist; DB-05 flat fields diagnostics/legacy only; flat fallback if zero blocks |
| Source weekly | Resolve monthly source ids; link W1–W4; warn on missing |
| Diagnostics | Block count, render mode, flat presence, metric refs collapsed, generated-at, Internal only |
| Print | Same data; print CSS; browser print only; no PDF |
| Access | Auth + internal read roles; `client_viewer` denied MVP |
| Safe rendering | Escape HTML; newlines preserved; no Markdown/raw HTML/CDN |
| Policy | No public token; no PDF; no client portal; no export package |

Controller/service: `ReportPreviewController` / `ReportPreviewService` (+ optional `ReportPreviewRepository`). Views: `pages/report-preview/show.php` (+ optional `print.php`). Monthly show gets Preview link.

---

## 5. Validation Plan

Documented for next implementation wave:

- Route smoke (preview 200; optional print; no PDF/share);
- Auth smoke (unauth → login);
- Preview content (title, `2026-07`, `in_progress`, 6 blocks, keys, Internal only);
- Render order validation;
- Fallback rules (documented; no forced archive mutation);
- Source weekly links W1–W4;
- Internal diagnostics;
- DB unchanged before/after;
- Regression (monthly/blocks/weekly/periods/health/login/404);
- No-public / no-export checks.

---

## 6. Restrictions Confirmed

| Restriction | Confirmed |
|-------------|-----------|
| No app-source edits | **yes** |
| No runtime edits | **yes** |
| No DB mutation | **yes** (read-only check only) |
| No SQL/migration create/edit | **yes** |
| No report_blocks row changes | **yes** |
| No monthly_report_contents row changes | **yes** |
| No weekly_checkpoint row changes | **yes** |
| No reporting_period row changes | **yes** |
| No admin/password/hash changes | **yes** |
| No `.env` / `.env.local` changes | **yes** |
| No source→runtime sync | **yes** |
| No service restart | **yes** |
| No push / fetch / pull / reset / clean / stash | **yes** (push no; others not run) |

---

## 7. Commit

| Item | Value |
|------|-------|
| Exact-path git add | allowlisted docs only |
| Primary commit message | `docs(iseo-report-hub): add report preview render charter` |
| Primary commit hash | `f9604d4b103ed984aaa83382ee87ee60c865e28c` |
| Hash-record message | `docs(iseo-report-hub): record report preview render charter commit hash` |
| Hash-record commit hash | `PENDING_AFTER_HASH_RECORD` |
| Push | **no** |

---

## 8. SAFE UNKNOWN

- Whether optional `/preview/print` will be included in Implementation 01 vs deferred — operator may choose at implementation start; design allows either.
- Exact multi-role HTTP smoke for preview beyond admin_owner — not required for MVP smoke; multi-role remains optional hardening.
- Whether a dedicated `ReportPreviewRepository` is needed vs reuse of existing repos — deferred to implementation judgment.
- Live archived-block exclusion smoke without temporary mutation — not exercised in this docs wave (fixture has zero archived blocks).

---

## 9. Recommended Next Action

**I-SEO Report Hub — Report Preview / Render Implementation 01**

---

## 10. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-preview-render-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 11. Git Actions

| Action | Done? |
|--------|-------|
| Exact-path git add | **yes** (allowlisted docs) |
| Commit | **yes** (primary + hash-record) |
| Push | **no** |
| Fetch | **no** |
| Pull | **no** |
| Checkout | **no** |
| Reset | **no** |
| Restore | **no** |
| Clean | **no** |
| Stash | **no** |
| Broad git add (`.` / `-A` / `commit -a`) | **no** |
