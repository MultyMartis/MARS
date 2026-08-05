# REPORTING SYNC v1 — Phase 3F.2

## Intent

Describe how a reporting workbook (see [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md)) would stay current against CLEAN without re-reading the full sheet on every intake event — reusing the same lesson already applied to `DEDUP_INDEX` (avoid uncontrolled full-sheet reads, per [architecture/LEAD-DATA-MODEL-v1.md](../../architecture/LEAD-DATA-MODEL-v1.md) §5.6, the "MetaBOT Sheets quota lesson").

## Proposed sync shape (design-level, not yet implemented)

| Aspect | Approach |
|---|---|
| Trigger | Scheduled/batched (e.g. the existing internal Schedule Trigger pattern already used for the pending-reminder gate in Admin.dev), **not** a per-lead synchronous write |
| Source read | Aggregate only — counts/rollups computed from CLEAN, never a row-by-row identifiable copy |
| Direction | One-way, CLEAN → reporting workbook. Reporting is a **read replica of aggregates**, never a place operators edit lead state back into CLEAN |
| Scope filter | Same `real-only-v1` / `archive_excluded` / epoch filter as [PRODUCTION-STATS-EPOCH-v1.md](PRODUCTION-STATS-EPOCH-v1.md) applied consistently at sync time, not left to the reporting side to re-derive inconsistently |
| Idempotency | Sync writes should be safe to re-run for the same period (recompute-and-overwrite an aggregate row, not append-and-accumulate duplicates) |

## Status

| Item | Status |
|---|---|
| Sync design (this document) | **IMPLEMENTED** (design-level) |
| Sync workflow/schedule actually built and running | **PENDING OPERATOR** — no new n8n workflow has been created for this; `workflows created=0` for Phase 3F.2 overall, see [FINAL-WORKFLOW-STATE-v1.md](FINAL-WORKFLOW-STATE-v1.md) |
| Call-budget analysis for the sync | See [REPORTING-CALL-BUDGET-v1.md](REPORTING-CALL-BUDGET-v1.md) |

*Related: [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md), [REPORTING-CALL-BUDGET-v1.md](REPORTING-CALL-BUDGET-v1.md).*
