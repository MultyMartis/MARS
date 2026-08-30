# I-SEO Report Hub — Report Preview / Render Implementation Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Preview / Render Implementation 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md), [REPORT-iseo-report-hub-report-preview-render-implementation-01.md](../reports/REPORT-iseo-report-hub-report-preview-render-implementation-01.md)

---

## 1. Status

| Item | Value |
|------|-------|
| Wave | **complete** |
| Preview implemented | **yes** |
| Print route implemented | **yes** (`/monthly-reports/{id}/preview/print`) |
| DB unchanged | **yes** |
| No public / export / PDF | **yes** |

---

## 2. Source Changes

Created:

- `app-source/app/Controllers/ReportPreviewController.php`
- `app-source/app/Services/ReportPreviewService.php`
- `app-source/app/Repositories/ReportPreviewRepository.php`
- `app-source/app/Views/pages/report-preview/show.php`
- `app-source/app/Views/pages/report-preview/print.php`

Modified:

- `app-source/app/routes.php`
- `app-source/app/bootstrap.php`
- `app-source/app/Views/pages/monthly-reports/show.php` — Preview link
- `app-source/app/Views/pages/reporting-periods/show.php` — Preview link when monthly exists
- `app-source/public/assets/css/app.css` — preview / print / internal-only styles
- `app-source/README.md` — preview routes + no public/PDF note

Not modified: auth/csrf/db services, health, migrations, tools, fixture tools.

---

## 3. Runtime Changes

Allowlist sync source → runtime (exact mirrors only):

- `app/routes.php`
- `app/bootstrap.php`
- `app/Controllers/ReportPreviewController.php`
- `app/Services/ReportPreviewService.php`
- `app/Repositories/ReportPreviewRepository.php`
- `app/Views/pages/report-preview/show.php`
- `app/Views/pages/report-preview/print.php`
- `app/Views/pages/monthly-reports/show.php`
- `app/Views/pages/reporting-periods/show.php`
- `public/assets/css/app.css`
- `README.md`

`.env.local` **untouched**. No broad sync.

---

## 4. Routes

| Method | Path | Auth | Notes |
|--------|------|------|-------|
| GET | `/monthly-reports/{id}/preview` | Required (internal read roles) | Assembled preview |
| GET | `/monthly-reports/{id}/preview/print` | Required | Print-friendly twin; browser print only |

No `/pdf`, `/share`, `/export`, no public token routes.

---

## 5. Render Data Sources

- Reporting period + client / project / primary site context (JOIN)
- `monthly_report_contents` row
- Non-archived `report_blocks` for the monthly id
- Source weekly checkpoints from monthly `source_weekly_checkpoint_ids` (+ per-block source chips)
- DB-05 flat fields for fallback / legacy diagnostics

---

## 6. Render Rules

| Rule | Implementation |
|------|----------------|
| Order | `sort_order ASC`, then `id ASC` |
| Include | draft / in_progress / ready_for_review / reviewed / approved (and any non-archived) |
| Exclude | `archived` |
| Primary mode | `blocks_primary` when ≥1 non-archived block |
| Fallback | `flat_fallback` when 0 blocks and flat fields non-empty |
| Empty | `empty` when neither |
| Text | HTML escape + `nl2br`; no raw HTML; no Markdown |
| Diagnostics | render mode, block count, archived excluded, flat availability/active, source/missing weekly ids, metric refs placeholder, generated-at |

---

## 7. Access / Auth

- Auth required; `requireInternalUser` gate
- Read roles: `admin_owner`, `seo_lead_reviewer`, `seo_specialist`, `account_client_manager`, `internal_viewer`
- `client_viewer` denied in MVP (no internal role)
- Smoke: **admin_owner** via session injection only (`ISEO_ADMIN_PASSWORD` unset)

---

## 8. DB Actions

- **Read-only** (SELECT composition + verification)
- Before/after: reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **6**
- Fingerprint of business rows unchanged
- No schema / migrate / mutation

---

## 9. Smoke Tests

| Area | Result |
|------|--------|
| PHP lint (changed files) | PASS (0 syntax errors) |
| Unauth GET `/monthly-reports/1/preview` | PASS → 302 `/login` |
| Auth preview 200 + content | PASS |
| Block order / count 6 | PASS |
| Print route 200 | PASS |
| Monthly detail Preview link | PASS |
| No pdf/share/export | PASS (404) |
| Regression (health/login/404/periods/weekly/monthly/blocks) | PASS |
| DB unchanged | PASS |

Overall: **22/22 PASS** (HTTP/order/count matrix this wave).

---

## 10. Restrictions

Confirmed: no production/remote DB; no real client data; no credentials/password/hash/session in reports; no `.env` commit; no source `.env.local`; no schema edits; no db-migrate; no auth/health edits; no fixture tool changes; no business-row mutations; no DROP/TRUNCATE/DELETE; no PDF/export/public share; no push.

---

## 11. What Still Does Not Exist

- PDF / export
- Public share / token URL
- Client portal
- Charts / Topvisor metrics rendering
- Rich text / Markdown
- Immutable snapshots
- Finalization / approval preview lock

---

## 12. Next Phase

**Report Finalization Charter 01**

---

## 13. SAFE UNKNOWN

- Multi-role HTTP preview paths beyond `admin_owner` session injection — deferred
- Live archived-block exclusion smoke (no archive mutation this wave; fixture has zero archived blocks)
- Password-form login re-smoke (`ISEO_ADMIN_PASSWORD` unset)
