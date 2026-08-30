# I-SEO Report Hub — Report Blocks CRUD Implementation Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Blocks CRUD Implementation 01  
**Related:** [REPORT-BLOCKS-CRUD-CHARTER-v0.1](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md), [IMPLEMENTATION-PLAN-v0.1](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md), [REPORT](../reports/REPORT-iseo-report-hub-report-blocks-crud-implementation-01.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Status | **complete** |
| CRUD implemented | **yes** |
| Report blocks section on monthly report detail | **yes** |
| Fixture block edited | **yes** — `executive_summary` id **1** `draft` → `in_progress` (sort_order → **15**) |
| Additional block created | **yes** — `risks_and_blockers` id **9**, draft, sort_order **35** |
| Real client data | **no** — `LOCAL_FIXTURE_ONLY` only |

---

## 2. Source Changes

Created:

- `app-source/app/Controllers/ReportBlockController.php`
- `app-source/app/Services/ReportBlockService.php`
- `app-source/app/Repositories/ReportBlockRepository.php`
- `app-source/app/Views/pages/report-blocks/index.php`
- `app-source/app/Views/pages/report-blocks/show.php`
- `app-source/app/Views/pages/report-blocks/form.php`
- `app-source/app/Views/pages/report-blocks/create.php`
- `app-source/app/Views/pages/report-blocks/edit.php`

Modified:

- `app-source/app/routes.php`
- `app-source/app/bootstrap.php`
- `app-source/app/Controllers/MonthlyReportContentController.php`
- `app-source/app/Controllers/DashboardController.php`
- `app-source/app/Views/pages/monthly-reports/show.php`
- `app-source/app/Views/pages/dashboard.php`
- `app-source/public/assets/css/app.css`
- `app-source/README.md`

Not created (optional, not needed):

- top-level `/report-blocks` index
- `app.js` changes (no JS required; no drag/drop)
- header top-level block nav (monthly-scoped entry documented)

Not modified (as required):

- AuthService / DatabaseService / CsrfService / AuthController / HealthController
- migrations / tools
- MonthlyReportContentService / MonthlyReportContentRepository (read-only parent context via ReportBlockRepository)

---

## 3. Runtime Changes

Allowlist sync source → runtime (exact mirrors only):

- Same relative paths under `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- `.env.local` **untouched**
- No broad sync
- No migrations/tools sync

---

## 4. Routes

| Method | Path | Action |
|--------|------|--------|
| GET | `/monthly-reports/{monthly_report_id}/blocks` | Nested block list |
| GET | `/monthly-reports/{monthly_report_id}/blocks/create` | Create form |
| POST | `/monthly-reports/{monthly_report_id}/blocks` | Store (CSRF; unique parent+key) |
| GET | `/report-blocks/{id}` | Flat detail |
| GET | `/report-blocks/{id}/edit` | Edit form |
| POST | `/report-blocks/{id}` | Update (CSRF) |

No DELETE route. No drag/drop route. No top-level `/report-blocks` index.

---

## 5. Parent Integration

Monthly report detail `/monthly-reports/{id}` shows a **Report blocks** section ordered by `sort_order`, with block_key / type / status / title, View/Edit links, Create block link, and Open block list link. Existing monthly content/details remain intact.

---

## 6. Data Model Use

- Existing `report_blocks` table (DB-06) — **no schema changes**
- Parent FK: `monthly_report_content_id` → `monthly_report_contents`
- Source weekly IDs: JSON array validated against same reporting period
- `source_metric_refs` / `data_json`: JSON object/array only (no FK)
- Unique `(monthly_report_content_id, block_key)`

---

## 7. Access / Auth

- Auth required on all block routes; unauth → `/login`
- Roles: admin_owner / seo_lead_reviewer full; seo_specialist draft→ready_for_review; account_client_manager / internal_viewer read-only; client_viewer denied via internal-role gate
- Current smoke: **admin_owner only** (session injection; password-form login deferred)

---

## 8. Validation

- Parent monthly archived blocks create/edit; finalized locks non-admin
- block_key required, ≤64, `[a-z0-9_\-]+`, unique per parent
- block_type in DB-06 set
- status transitions + role gates
- source weekly IDs same-period
- JSON object/array for data_json / source_metric_refs
- sort_order integer ≥0
- owner/reviewer internal users
- CSRF on POST

---

## 9. DB Actions

| Metric | Before | After |
|--------|--------|-------|
| report_blocks | 5 | 6 |
| monthly_report_contents | 1 | 1 |
| reporting_periods | 2 | 2 |
| weekly_checkpoints | 4 | 4 |

- Updated `executive_summary` id **1** → status `in_progress`, sort_order **15**, `LOCAL_FIXTURE_ONLY` retained
- Created `risks_and_blockers` id **9** — draft, sort_order **35**, sources `[1,2,3,7]`
- Duplicate / invalid JSON / invalid source IDs refused; rows not corrupted
- Audit: `report_block.created`, `report_block.updated`, `report_block.status_changed`, `report_block.reordered`

---

## 10. Smoke Tests

| Gate | Result |
|------|--------|
| PHP lint | PASS |
| Unauth blocks list | PASS 302 → `/login` |
| Auth list 5 fixtures | PASS |
| Detail / edit CSRF | PASS |
| Update → in_progress | PASS |
| Create risks_and_blockers | PASS |
| Duplicate guard | PASS |
| Invalid JSON / source IDs | PASS |
| Manual sort_order | PASS |
| Monthly show blocks section | PASS |
| No DELETE | PASS |
| Regression (health/login/404/periods/weekly/monthly/dashboard) | PASS |
| Auth mode | session injection |

---

## 11. Restrictions

- No production / remote DB; no real client data; no secrets in Git/report
- No schema edits; no DELETE; no drag/drop; no PDF/export/client portal
- No monthly/weekly/period row mutations

---

## 12. What Still Does Not Exist

- Drag/drop reorder
- Rich text / Markdown editor
- PDF / export
- Topvisor imports / metric tables
- Client portal / public share
- Evidence / uploads
- Multi-role fixture users / password-form login re-smoke this session

---

## 13. Next Phase

**Recommended:** `Report Preview / Render Charter 01`

---

## 14. SAFE UNKNOWN

- Password-form login path not re-smoked this session (`ISEO_ADMIN_PASSWORD` unset).
- Multi-role HTTP smoke not executed (only admin_owner fixture user present).
