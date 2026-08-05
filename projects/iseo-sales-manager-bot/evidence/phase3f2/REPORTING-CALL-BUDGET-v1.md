# REPORTING CALL BUDGET v1 — Phase 3F.2

## Why this matters

The project already carries a documented Sheets-quota lesson (`DEDUP_INDEX` exists specifically to "avoid full CLEAN sheet reads on every lead" — [architecture/LEAD-DATA-MODEL-v1.md](../../architecture/LEAD-DATA-MODEL-v1.md) §5.6). A reporting sync (see [REPORTING-SYNC-v1.md](REPORTING-SYNC-v1.md)) that re-reads all of CLEAN on a tight schedule would reintroduce the same class of problem at a different layer.

## Budget principles (design-level)

| Principle | Detail |
|---|---|
| Batch, don't poll per-lead | Reporting aggregation runs on its own schedule (e.g. hourly/daily), decoupled from the per-lead intake cadence — it must never run once per incoming lead |
| Read once per cycle | One full (or incrementally-bounded) CLEAN read per sync cycle, not one read per statistic computed |
| Reuse existing quota headroom awareness | Follow the same fail-closed posture already adopted for the reminder engine (`Ledger read error sends zero`, `Claim failure sends zero` — [../phase3f1/HARNESS-RESULTS-v1.md](../phase3f1/HARNESS-RESULTS-v1.md) checks #33–34): if a reporting read fails or quota is exhausted, skip that cycle rather than retry aggressively |
| No duplicate readers | If a reporting sync and the pending-reminder gate both need CLEAN data in the same window, they should not each independently re-read the full sheet — share a read where practical |

## Status

| Item | Status |
|---|---|
| Call-budget principles (this document) | **IMPLEMENTED** (design-level, consistent with existing project precedent) |
| Actual measured call volume for a live reporting sync | **PENDING OPERATOR** — no live reporting sync exists yet to measure (see [REPORTING-SYNC-v1.md](REPORTING-SYNC-v1.md)) |

*Related: [REPORTING-SYNC-v1.md](REPORTING-SYNC-v1.md), [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md).*
