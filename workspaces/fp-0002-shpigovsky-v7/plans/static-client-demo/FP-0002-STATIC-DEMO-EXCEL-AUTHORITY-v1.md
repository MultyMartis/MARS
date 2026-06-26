# FP-0002 Static Demo — Excel Authority v1

**Date:** 2026-06-26

## Candidate table

| Candidate | Path | Size | Modified | Sheets | Likely role | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| Предварит структура и спрос.xlsx | workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/02_CONTENT/Предварит структура и спрос.xlsx | 14102 | 2026-06-13 | Структура; Спрос набросок | Site IA + URL tree + demand | CANONICAL_STRUCTURE_SOURCE |
| Предварит структура и спрос.xlsx (snapshot) | AI MARS STORAGE/website-factory/snapshots/FP-0002-PRE-M2-OPS-2026-06-13-v1/... | 14102 (expected) | 2026-06-13 | same | Ops snapshot copy | SUPPORTING_SOURCE |

## Canonical Excel

**File:** `Предварит структура и спрос.xlsx`  
**Path:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/02_CONTENT/Предварит структура и спрос.xlsx`  
**Size:** 14102 bytes  
**Modified:** 2026-06-13 03:34:52

## Selection evidence

1. Referenced as SOURCE-025 in `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` §10–11 (intake approved PD-08).
2. Sheet `Структура` contains full URL tree with hierarchy levels 1–4.
3. Sheet `Спрос набросок` contains Moscow search demand (supporting, not page registry).
4. No competing structure workbook in priority search paths.
5. STORAGE snapshot copy matches size/date (supporting backup only).

## Supporting files

- `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` §10–11 (prior human intake)
- STORAGE snapshot `FP-0002-PRE-M2-OPS-2026-06-13-v1`

## Rejected candidates

All other `.xlsx`/`.csv` under `AI MARS` / `AI MARS STORAGE` — unrelated projects (ORCA, BZPM, Makita, Corvonero, Atlas, etc.).

## Result

**CONFIRMED** — `fp0002_static_demo_excel_authority: CONFIRMED`
