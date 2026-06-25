# REPORT — КОРВО НЕРО — COMMANDER V6 PRODUCTION

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` |
| HEAD | `bf313e4` |
| V5 QA Repair Gate v2 | **PASS — V6 PRODUCTION AUTHORIZED** |
| V6 authorization | `production/approvals/v6-production-authorization.md` present |
| Repair package | `production/repair/v6-production-input-package.json` readable |
| Unrelated WIP | Not modified (ocpilot/BZPM copy outside corvonero scope) |
| Split / import / launch / commit / push | **NOT AUTHORIZED** |

## 2. QA Repair Authorization

- Gate: `production/validation/v5-qa-repair-gate-v2.json` — **PASS**
- 12/12 checks passed; 0 blockers
- Career/education corrections: 4 (leakage to future production = 0)
- Controlled tests reviewed: 234; justified controlled: 27
- Unique negatives: UNRESOLVED=0, BLOCKING=0
- Exact collision actions: 20/20

## 3. Repair Package Applied

- Source: `production/repair/v6-production-input-package.json`
- Applied to: `production/direct-commander-production-dataset-v5.json`
- Semantic exclusions: 4 education phrases
- Status changes: 234 entries (74 EXCLUDE, remainder ACTIVE / CONTROLLED TEST — JUSTIFIED)
- Negative removals: 30
- Exact collision actions: 20
- Group reassignments: 0 (empty in package)
- Group status changes: 0 (empty in package)

## 4. Semantic Corrections

- Active keywords v5 → v6: **348 → 274** (−74 exclusions)
- Education/career phrases excluded and verified absent from export:
  - `1с программист без образования`
  - `образование программист 1с`
  - `программист 1с без высшего образования`
  - `программист 1с высшее образование`
- Registry: `production/final-keyword-registry-v6.json` / `.md`
- Diff: `production/keyword-v5-to-v6-diff.md`

## 5. Controlled Tests

- Retained justified controlled tests: **27**
- Each has: commercial hypothesis, noise risk, bid tier, post-launch evaluation rule
- Registry embedded in dataset `controlled_tests` and review sheet **Controlled tests**
- Unapproved controlled tests in export: **0**

## 6. Group Changes

- Active exported groups: **40** (was 48 in v5)
- Held groups (documented, not exported): **8**
- No merges; viability recalculated after keyword exclusions
- Registry: `production/final-group-registry-v6.json` / `.md`
- Diff: `production/group-v5-to-v6-diff.md`

## 7. Negative Resolution

- Applied: `production/repair/v5-negative-resolution-final.json`
- Collision actions: `production/repair/v5-collision-actions-final.json`
- Global negatives: 52
- Unresolved unique negatives: **0**
- Registry: `production/final-negative-registry-v6.json`
- Matrix: `production/final-conflict-negative-matrix-v6.md`
- Diff: `production/negative-v5-to-v6-diff.md`

## 8. Collision QA

- Validation: `production/validation/negative-collision-validation-v6.json` / `.md`
- Literal collisions before: 20 → after: **0**
- Blocking collisions: **0**
- Unresolved unique negative risks: **0**
- Pair-layer semantic warnings: 1445 (reconciled per repair package — not unresolved findings)
- Final status: **PASS**

## 9. Ads

- Ads exported: **45** (one+ per active group)
- Changes from v5 text: **0** (mappings unchanged)
- Evidence audit: **PASSED**
- Registry: `production/final-ad-registry-v6.json` / `.md`

## 10. Bids

| Tier | Count |
|------|------:|
| T1 | 170 |
| T2 | 73 |
| T3 | 31 |
| Minimum | 250 ₽ |
| Maximum | 550 ₽ |
| Median | 450 ₽ |
| Controlled-test bids | 27 |
| Groups low-tier only | CORV-G03-06, CORV-G02-05 |

## 11. URLs and UTM

- Base domain: `https://lk.corvonero.ru/`
- UTM campaign: `corvonero_1c_search_nsk`
- UTM content: stable group ID
- UTM term: `{keyword}`
- All URLs marked **PLANNED** internally; no Triumph data

## 12. Dataset V6

- Canonical: `production/direct-commander-production-dataset-v6.json`
- Single unified campaign; 8 logical directions; full negatives/ads/bids/UTM metadata
- v5 supersession noted in `audit_input`

## 13. Commander XLSX V6

- Output: `exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v6.xlsx`
- Fill rows: 319 (45 ads + 274 keywords)
- Export validation: **STRUCTURALLY_VALIDATED**
- v5 file preserved unchanged

## 14. Review Workbook V6

- Output: `exports/CORVONERO-CAMPAIGN-REVIEW-v6.xlsx`
- Sheets: **28** (all required sheets present)
- Integrity: **PASSED**
- CSV mirror: `exports/review-v6-csv/`

## 15. Independent Validation

| Gate | File | Status |
|------|------|--------|
| Semantic | `semantic-validation-v6.json` | PASS |
| Group | `group-validation-v6.json` | PASS |
| Negative | `negative-validation-v6.json` | PASS |
| Collision | `negative-collision-validation-v6.json` | PASS |
| Ads | `ad-validation-v6.json` | PASS |
| Review workbook | `review-workbook-validation-v6.json` | PASS |
| Commander XLSX | `direct-commander-validation-v6.json` | PASS |
| Export consistency | `report-export-consistency-v6.json` | PASS |

## 16. Import Instructions

- `exports/CORVONERO-COMMANDER-IMPORT-INSTRUCTIONS-v6.md`

## 17. Dry-Run Template

- `exports/CORVONERO-COMMANDER-DRY-RUN-RESULT-TEMPLATE-v6.md`

## 18. Landing Copy Handoff

- `production/landing-copy-handoff-v6.json`
- Status: **NOT STARTED**

## 19. Production Counts

| Entity | v5 | v6 |
|--------|---:|---:|
| Active keywords | 348 | 274 |
| Active groups | 48 | 40 |
| Held groups | 0 | 8 |
| Ads | 45 | 45 |
| Controlled tests | — | 27 |
| Exclusions applied | — | 74 |

## 20. Files Created or Changed

**Tools (new):**

- `tools/lib/v6-repair-apply.mjs`
- `tools/lib/workbook-integrity-v6.cjs`
- `tools/run-full-production-v6.mjs`
- `tools/export-commander-xlsx-v6.cjs`
- `tools/generate-review-workbook-v6.cjs`
- `tools/validate-commander-xlsx-v6.cjs`

**Production v6 registries and dataset** — under `production/` (keyword, group, negative, ad, semantic, dataset, diffs, landing handoff)

**Validation v6** — under `production/validation/`

**Exports** — Commander v6 XLSX, Review v6 XLSX, import instructions, dry-run template

**Audit** — `production/audit/version-lifecycle-status.json`

## 21. Git Status

- Entire `projects/orca/projects/corvonero-yandex-direct/` tree: **untracked** (`??`)
- No commit; no push (per operator charter)

## 22. Remaining Manual Checks

1. Operator review of v6 Commander XLSX and 28-sheet review workbook
2. Commander desktop dry-run (preview only) — record in dry-run template
3. Verify manual campaign settings post-import (strategy, budget, Metrika)
4. Landing pages not published — do not launch

## 23. Next Gate

**OPERATOR REVIEW OF V6 FILES AND COMMANDER DRY-RUN**

## 24. Stop Condition

| Status | Value |
|--------|-------|
| V5 QA Repair Gate v2 | PASSED |
| v5 Commander / Review | REJECTED AND SUPERSEDED |
| v6 semantic production | COMPLETE |
| v6 negative production | COMPLETE |
| v6 collision QA | PASSED |
| v6 ad QA | PASSED |
| v6 Commander XLSX | GENERATED AND VALIDATED |
| v6 Review XLSX | GENERATED AND VALIDATED |
| Commander dry-run | AUTHORIZED |
| Moderation | NOT AUTHORIZED |
| Campaign split | DEFERRED |
| Landing copy | NOT STARTED |
| Launch | NOT AUTHORIZED |

**V6 BLOCKED:** No — all gates passed.
