# REPORT — Corvonero Production Extensions Wave 1 Operator Decisions v2

Date: 2026-06-28

## Task

CURSOR TASK — CORVONERO EXTENSIONS WAVE 1 — APPLY OPERATOR DECISIONS

## Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` |
| Authority commit | `508837a02658e357ce18dca777a46231d2575b25` |
| v1 artefacts modified | **NO** |
| Final ads / LP copy modified | **NO** |
| Commander XLSX created | **NO** |
| Commit / push | **NO** |

## Verdict

**CORVONERO PRODUCTION EXTENSIONS WAVE 1 V2: PASS — OPERATOR CONTENT DECISIONS APPLIED**

| Component | Status |
|-----------|--------|
| Sitelinks | APPROVED — URLS PROVISIONAL |
| Callouts | APPROVED |
| Shared negatives | APPROVED CONTROLLED SET |
| Campaign negatives | APPROVED CONTROLLED SET |
| Cross-negatives | NOT DEPLOYED |
| UTM base policy | APPROVED |
| Keyword macro | PENDING COMMANDER TEMPLATE CONFIRMATION |
| Commander XLSX | BLOCKED BY REMAINING OPERATOR, ROMAN AND TEMPLATE INPUTS |
| Advertising | NOT STARTED |

## Validation

| Metric | Expected | Actual | Pass |
|--------|----------|--------|------|
| Campaigns | 5 | 5 | YES |
| Deployable groups | 15 | 15 | YES |
| Deployable phrases | 895 | 895 | YES |
| Sitelink sets | 5 | 5 | YES |
| Sitelinks | 20 | 20 | YES |
| Callout sets | 5 | 5 | YES |
| Approved shared negatives | 9 | 9 | YES |
| License phrase negatives / campaign | 2 | 2 | YES |
| CA-05 additional phrase negative | 1 | 1 | YES |
| Cross-campaign negatives deployed | 0 | 0 | YES |
| UTM campaign slugs (unique) | 5 | 5 | YES |

## Safety checks

| Check | Result |
|-------|--------|
| No mixed-script `кassa` | PASS |
| No unsupported касса claim | PASS |
| No URL represented as published | PASS |
| No provisional anchor as final | PASS |
| No unsafe cross-negative deployed | PASS |
| No `{keyword}` in approved URL suffix | PASS |
| All sitelinks within char limits | PASS |
| All callouts within char limits | PASS |

## Commander blockers after v2

### ROMAN
- publish and verify five LP URLs
- supply final anchor IDs
- complete and verify forms/privacy publication

### OPERATOR
- set budgets
- set bid strategy
- set schedule
- provide Metrica counter
- provide conversion goals

### MARS
- instantiate and verify Corvonero Commander template
- confirm dynamic keyword macro support

**Note:** Final negative list blocker (B8) is **CLOSED** after this task.

## Outputs created

| Artefact | Path |
|----------|------|
| Sitelinks v2 | `pilots/corvonero/CORVONERO-EXT-W1-SITELINKS-v2.*` |
| Callouts v2 | `pilots/corvonero/CORVONERO-EXT-W1-CALLOUTS-v2.*` |
| Negative deployment v1 | `pilots/corvonero/CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1.*` |
| Cross-negatives v2 | `pilots/corvonero/CORVONERO-EXT-W1-CROSS-NEGATIVES-v2.*` |
| UTM policy v2 | `pilots/corvonero/CORVONERO-EXT-W1-UTM-POLICY-v2.*` |
| Campaign settings v2 | `pilots/corvonero/CORVONERO-EXT-W1-CAMPAIGN-SETTINGS-v2.*` |
| Commander gate v2 | `pilots/corvonero/CORVONERO-EXT-W1-COMMANDER-READINESS-GATE-v2.*` |
| Operator receipt v1 | `pilots/corvonero/CORVONERO-EXT-W1-OPERATOR-DECISION-RECEIPT-v1.*` |
| Result v2 | `pilots/corvonero/CORVONERO-EXT-W1-RESULT-v2.*` |
| Report | `reports/REPORT-corvonero-production-extensions-wave-1-operator-decisions-v2.md` |

Generator: `pilots/corvonero/tools/execute-ext-wave-1-v2-operator-decisions.mjs`

## Git

No commit, no push. v1 artefacts, final ads, and LP authority untouched.
