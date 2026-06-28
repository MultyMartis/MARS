# REPORT — Corvonero Production Extensions Wave 1 v1

Date: 2026-06-28

## Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` |
| HEAD | `508837a02658e357ce18dca777a46231d2575b25` (tag `corvonero-final-p1-search-ads-2026-06`) |
| Descends from authority | YES |
| Final phrase allocation | `CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.json` — 895 deployable |
| Final group register | `CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.json` — 15 groups |
| Final primary ads | `CORVONERO-AD-WAVE-1-P1-FINAL-PRIMARY-ADS-v1.json` — unchanged |
| LP copy LP-01..LP-05 | Final copy artifacts present |
| LP URLs published | **NOT VERIFIED** — PROPOSED only |
| Excluded groups preserved | ca-02-specialist-search, ca-02-modification, ca-05-specialist-search |
| Deferred | CA-06 / LP-06 — 37 phrases |
| Unrelated WIP | Not modified |
| Commit / push | Not performed |

## Verdict

**CORVONERO PRODUCTION EXTENSIONS WAVE 1: PASS — EXTENSIONS AND IMPORT PROFILE READY FOR OPERATOR REVIEW**

| Component | Status |
|-----------|--------|
| Sitelink copy | CREATED |
| Sitelink URLs | PROVISIONAL UNTIL FINAL ANCHORS |
| Callouts | CREATED |
| Negative candidates | CREATED — NOT DEPLOYED |
| UTM policy | CREATED (PROPOSED_TEMPLATE) |
| Campaign settings | PARTIAL — OPERATOR DECISIONS REQUIRED |
| Commander import profile | CREATED |
| Commander XLSX | BLOCKED |
| Advertising | NOT STARTED |

## Validation

| Metric | Expected | Actual |
|--------|----------|--------|
| Campaigns | 5 | 5 |
| Deployable groups | 15 | 15 |
| Deployable phrases | 895 | 895 |
| LPs | 5 | 5 |
| Groups without display path | 0 | 0 |
| Campaigns without sitelink copy | 0 | 0 |
| Campaigns without callout pool | 0 | 0 |
| Negative candidates without source | 0 | 0 |
| UTM campaign slugs (unique) | 5 | 5 |
| Commander mandatory fields classified | 100% | 100% |

## Outputs

27 files under `projects/mars-search-ppc-production/pilots/corvonero/` (prefix `CORVONERO-EXT-W1-`) plus generator `tools/execute-ext-wave-1-v1.mjs`.

Report: `projects/mars-search-ppc-production/reports/REPORT-corvonero-production-extensions-wave-1-v1.md`

## Technical evidence

- Commander column contract: `projects/orca/projects/corvonero-yandex-direct/production/direct-commander-format-contract-v1.md`
- Display path: single field col 49, max 20 chars
- UTM: append to col 48 «Ссылка»; `{keyword}` macro REQUIRES_IMPORT_PROFILE_CONFIRMATION
- HTTP verification: not authorized in this task

## Git

No commit, no push. Final ads and LP authority untouched. No Commander XLSX created.
