# REPORTING CALL BUDGET v1 — Phase 3F.2

## Rules

- No reporting reads/writes on empty Operational polls.
- No full-workbook read per lead.
- One lead upsert + one history append per real event where practical.
- Statistics refresh only after meaningful changes (or bounded schedule later).
- Test fixtures → zero reporting writes.

## Measured / observed in 3F.2

| Scenario | Observation |
|---|---|
| Empty Ops poll | Unchanged discipline expected; no reporting nodes added to empty-poll path |
| Baseline reporting create + seed | Finite one-shot Sheets/Drive calls during migration window (workflows temporarily swapped, then restored) |
| Follow-up archive copy | Hit Google Sheets quota (`too many requests`) — stopped; no destructive retry storm |
| Continuous sync call volume | **SAFE UNKNOWN / not measured** — continuous path still PARTIAL |

*Related: [REPORTING-SYNC-v1.md](REPORTING-SYNC-v1.md).*
