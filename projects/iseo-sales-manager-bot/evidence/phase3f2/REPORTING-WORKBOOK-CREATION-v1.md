# REPORTING WORKBOOK CREATION v1 — Phase 3F.2

## Intent

A separate Google Spreadsheet file (not a tab inside the technical backend workbook) for human viewing and reporting: **«i-SEO — Учёт лидов и статистика»**.

## Live outcome (Phase 3F.2)

| Item | Status |
|---|---|
| Separate Spreadsheet file created | **PASS** (via authorized Google credential; temporary Admin in-place runner, then restored) |
| Tabs `Лиды`, `История изменений`, `Статистика`, `Справка` | **PASS** (created + seeded) |
| Клиент A baseline row once | **PASS** |
| File ID / URL in Git | **FORBIDDEN** — stored only in private CONFIG `reporting_workbook_ref` and Storage private contour |
| Public / anyone-with-link access | **Not set** — private by default |
| Automatic employee/client share | **Not performed** — requires separate operator instruction |

## Notes

- Backend workbook remains source of truth.
- Continuous Operational/Admin sync beyond the baseline seed is documented separately — see [REPORTING-SYNC-v1.md](REPORTING-SYNC-v1.md).

*Related: [REPORTING-WORKBOOK-PRIVACY-v1.md](REPORTING-WORKBOOK-PRIVACY-v1.md), [REPORTING-SYNC-v1.md](REPORTING-SYNC-v1.md), [PHASE3F2-ACCEPTANCE-RECEIPT-v1.md](PHASE3F2-ACCEPTANCE-RECEIPT-v1.md).*
