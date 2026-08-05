# REPORTING SYNC v1 — Phase 3F.2

## Intent

Backend remains source of truth. Reporting workbook is a secondary, idempotent mirror.

## Live baseline sync

| Step | Status |
|---|---|
| Create private reporting Spreadsheet | **PASS** |
| Seed `Лиды` / `История` / `Статистика` / `Справка` for Клиент A | **PASS** |
| Store `reporting_workbook_ref` in CONFIG (private) | **PASS** |
| New n8n workflow created | **0** (in-place temporary runners only) |

## Ongoing sync

| Aspect | Status |
|---|---|
| Design (upsert by public lead ID; event append; fail-open for backend) | **IMPLEMENTED** |
| Continuous per-lead sync wired inside Operational/Admin beyond baseline | **PARTIAL** — baseline seed done; full continuous path remains follow-up |
| Empty-poll reporting writes | **Must remain 0** |

*Related: [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md), [REPORTING-CALL-BUDGET-v1.md](REPORTING-CALL-BUDGET-v1.md), [REPORTING-SYNC-IDEMPOTENCY-v1.md](../../architecture/REPORTING-SYNC-IDEMPOTENCY-v1.md).*
