# SHEETS SYNTHETIC ROWS MANIFEST v1

## Policy selected

**A — Preserve synthetic test rows as named sandbox evidence** (marker `SYNTHETIC_TEST` / `msg_synth_` / `lead_synth_`).

No broad deletion. Historical tabs untouched.

## Counts (after Phase 3B.1)

| Tab | Synthetic rows |
|-----|----------------|
| lead_raw_v2 | 2 |
| lead_clean_v2 | 3 |
| CONFIG | 0 |
| LEAD_EVENTS | 3 |
| ERRORS | 1 |
| DEDUP_INDEX | 4 |

**Total synthetic rows:** 13

## Write method

Temporary HTTP Sheets append webhook on Operational.dev (restored). Native Google Sheets append nodes were **not** used for writes because enabling them fails with stale column-cache vs v2 headers.

## PII / quality

- No real customer identifiers
- No `44` / `#ERROR!` dedupe keys written
- Workbook IDs omitted from git evidence
