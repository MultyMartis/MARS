# I-SEO Report Hub — Client Preview Show-ready Content Implementation Scope v0.1

**Status:** implementation charter for next wave (docs only now)  
**Date:** 2026-08-21  
**Wave name:** `I-SEO Report Hub — Client Preview Show-ready Content Implementation 01`  
**Strategy:** Option A — render-layer show-ready local demo fallback

---

## 1. Objective

Make `/monthly-reports/1/preview` and `/monthly-reports/1/preview/print` show-ready for local demo without mutating DB, report blocks, PDF, export, or shares.

---

## 2. Allowed work

| Allowed | Notes |
|---------|--------|
| Render-layer only | Preview/print client document path |
| `ClientReportDocument` / mapper changes | Inject demo fallback when empty + local/demo gate |
| Optional read-only assembly reuse | Build auto-section text from work entries in memory |
| Partial display adjustments | `document.php` only if needed for empty vs body switching |
| Optional CSS minor polish | `client-report.css` only if readability requires |
| Controller display flag | `ReportPreviewController.php` only if gate/flag needed |
| Screenshot recapture | Storage incoming evidence folder |
| GET validation | Preview/print/report 5/health |

---

## 3. Forbidden work

- DB mutation of any kind
- `report_blocks` / `monthly_report_contents` UPDATE
- Reopen / finalize / snapshot create
- PDF regeneration / new export row / export artifact edit
- Export **4** file or checksum change
- Share create/revoke/change; public share route mutation
- Report 5 content seeding
- Runtime sync beyond exact allowlisted source files (if any code ships)
- Production / WordPress / i-seo.su / WPilot
- Package install

---

## 4. Likely files (app-source)

Primary:

- `projects/iseo-report-hub/app-source/app/Support/ClientReportDocument.php`
- `projects/iseo-report-hub/app-source/app/Views/partials/client-report/document.php`

Possible:

- `projects/iseo-report-hub/app-source/public/assets/css/client-report.css`
- `projects/iseo-report-hub/app-source/app/Controllers/ReportPreviewController.php`
- small helper under `app/Support/` for demo copy constants (optional)

Reuse, do not rewrite broadly:

- `UiTextSanitizer.php` (keep junk stripping; do not weaken)
- `MonthlyReportSummaryAssemblyService.php` (read-only reuse OK; no apply/write)

Copy source of truth for strings:

- `product/I-SEO-REPORT-HUB-CLIENT-PREVIEW-REPORT-1-DEMO-COPY-v0.1.md`

---

## 5. Behavioral requirements

1. **Gate:** demo fallback only when `app.env` is local (or equivalent existing local demo signal) **and** section would otherwise be empty after sanitize.
2. **Report 1:** all six sections show useful client-safe text after fallback.
3. **Prefer work entries** for auto sections when assembly can produce non-empty text without DB write.
4. **Report 5:** remains calm empty draft — no demo pack.
5. **No fake KPI** numbers.
6. **Export/PDF/share** code paths must not consume the demo overlay (preview-only).

---

## 6. Validation checklist (Implementation 01)

| Check | Expected |
|-------|----------|
| `GET /monthly-reports/1/preview` | 200; six filled sections; no placeholder “ручной редакции” on filled demo |
| `GET /monthly-reports/1/preview/print` | 200; same content intent |
| `GET /monthly-reports/5/preview` | 200; calm empties; no demo pack |
| `GET /health` | 200; still OK |
| DB | unchanged |
| Export 4 size/checksum context | unchanged (`117055` / `a8c4d61c6216` prefix context) |
| Shares | unchanged |
| P1 manager detail report 1 | no regression |
| P0 sanitizer | still strips junk on non-demo paths |

Screenshots (suggested names):

- `09_client_preview_show_ready_after.png`
- `10_client_preview_print_show_ready_after.png`
- `15_monthly_report_5_preview_regression.png`

Evidence root (create in impl wave): under  
`X:\AI MARS STORAGE\incoming\iseo-report-hub\client-preview-show-ready-content-implementation-01\`

---

## 7. Exit criteria for Implementation 01

- Show-ready demo visible on report 1 preview/print.
- Safety freezes hold.
- Docs result + closeout report + OPERATIONAL-INDEX update.
- Exact-path commit only; no push unless separately authorized.
