# I-SEO Report Hub — Report Delivery Public Share Implementation Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-28  
**Authority:** Operator I-SEO Report Hub Report Delivery Public Share Implementation 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DB10-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DB10-MIGRATION-APPLY-RESULT-v0.1.md)
- [REPORT-iseo-report-hub-report-delivery-public-share-implementation-01.md](../reports/REPORT-iseo-report-hub-report-delivery-public-share-implementation-01.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Status | **complete** |
| Share service | **yes** |
| Public token route | **yes** — `GET /share/report/{token}` |
| Internal create/revoke UI | **yes** |
| DB final | migrations **9**; tables **16**; `report_exports` **4**; `report_export_shares` **2** revoked (smoke create×2 + revoke×2; no active) |
| Artifact checksums unchanged | **yes** |
| Smoke | **46/46 PASS** |

---

## 2. Source Changes

Created:

- `app-source/app/Support/SafeToken.php`
- `app-source/app/Repositories/ReportExportShareRepository.php`
- `app-source/app/Services/ReportExportShareService.php`
- `app-source/app/Controllers/ReportExportShareController.php`
- `app-source/app/Controllers/PublicReportShareController.php`
- `app-source/app/Views/pages/report-export-shares/index.php`

Modified:

- `app-source/app/bootstrap.php`
- `app-source/app/routes.php`
- `app-source/app/Controllers/ReportExportController.php`
- `app-source/app/Views/pages/report-exports/index.php`
- `app-source/app/Views/pages/report-exports/show.php`
- `app-source/app/Views/pages/report-snapshots/show.php`
- `app-source/app/Views/pages/monthly-reports/show.php`
- `app-source/public/assets/css/app.css`
- `app-source/public/assets/js/app.js`
- `app-source/README.md`

---

## 3. Runtime Sync

Exact allowlist copy to `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` for all changed app-source paths above.

`.env.local` untouched. No broad sync. No artifact sync.

---

## 4. Token Model

| Item | Behavior |
|------|----------|
| Generation | `bin2hex(random_bytes(32))` (64 hex chars) |
| Storage | SHA-256 hash only in `token_hash` |
| Plaintext | shown once after create (session flash + copy UI) |
| DB plaintext | never stored |
| Reports | token redacted (`[REDACTED]`) |

---

## 5. Eligibility Policy

| Export id | Eligible | Reason |
|-----------|----------|--------|
| 1 | no | HTML + legacy metadata |
| 2 | no | PDF but legacy metadata NULL |
| 3 | no | HTML (styled) |
| 4 | **yes** | ready PDF + `iseo_default_v1` + `render_target=pdf_export` + artifact/checksum OK |

---

## 6. Public Route

- Route: `GET /share/report/{token}` (no auth)
- Validation: hash lookup → active → not expired → eligibility → artifact checksum/PDF magic
- Success headers: `Content-Type: application/pdf`; `Content-Disposition: attachment`; `X-Content-Type-Options: nosniff`; `Cache-Control: private, no-store`; `X-Robots-Tag: noindex, nofollow`
- Denial: **404** invalid/missing; **410** revoked/expired
- `/share` listing: remains 404; no `/r/{token}`

---

## 7. Internal UI

- Export detail share card + eligibility badge
- Shares page: create form, one-time URL copy, revoke, status table
- Export list share column / badge
- Snapshot/monthly notes for shareable PDF candidate
- No token hash / raw storage path in public responses

---

## 8. DB / Artifact Validation

| Metric | Before | After smoke |
|--------|--------|-------------|
| schema_migrations | 9 | 9 |
| tables | 16 | 16 |
| report_exports | 4 | 4 |
| report_export_shares | 0 | **2** revoked (export id 4 only) |
| business tables | unchanged | unchanged |

Artifacts: v1/v2 HTML/PDF checksums unchanged; PDFs `%PDF`; no public webroot artifacts.

---

## 9. HTTP Smoke

Server: PHP built-in `127.0.0.1:8092` + session injection (password not printed).

Assertions covered: health/login/404; export details 1–4 eligibility; create share id 4; public PDF headers/body; access_count++; revoke → 410; deny create ids 2/3; `/share` + `/r/test` 404; auth downloads 1–4.

Token redacted in all outputs.

---

## 10. Restrictions

Confirmed: no production/remote DB; no real data beyond fixture; no raw token in DB/report; no raw path in public response; no public files; no export row mutation; no artifact changes; no package install; no secrets in Git.

---

## 11. What Still Does Not Exist

- client portal
- email delivery
- short `/r/{token}` route
- one-time token UX / max_access enforcement UI
- detailed denied-access audit table
- rate limiter
- production deployment

---

## 12. Next Phase

**Report Delivery Public Share Hardening 01**

---

## 13. SAFE UNKNOWN

- Exact Laragon Apache listen state during PHP `-S` smoke not re-audited beyond prior waves.
- Whether operator wants the two revoked smoke rows pruned later (requires separate destructive/DB charter; not done here).
