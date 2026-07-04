# REPORT — Corvonero Campaign V2.1 Semantic Cleanup and Regeneration

Generated: 2026-06-30T12:55:31.000Z
Checkpoint: `eaac1e1e23a0e3a709cb5410357208928343e2b2`

## Environment

Volume AI WS; repo `X:\AI MARS`; checkpoint `eaac1e1e23a0e3a709cb5410357208928343e2b2`

## Sources inspected

V2 final phrase allocation (1593 slots), proposed allocation (833 rows), CT4 architecture, negatives, cross-negative proposals, V2 final package

## Confirmed defects

CA-01 junk examples removed; template negatives {'запчасти', 'ремонт', 'эвакуатор'} excluded; dangerous group negatives cleared

## Phrase audit methodology

Deterministic classifier: commercial keep, career/education/junk reject, geo reallocation, service routing CA-04→CA-05 marking

## Removed phrases by reason

{
  "REJECT_EDUCATION": 15,
  "REJECT_JOB": 11,
  "REJECT_COMPETITOR_OR_PERSON": 9,
  "REJECT_INFORMATIONAL": 16,
  "HOLD_OPERATOR": 5,
  "REJECT_DOWNLOAD_FREE": 2,
  "REJECT_PROVIDER_SIDE": 3,
  "REJECT_DOCUMENT_TEMPLATE": 12
}

## Geo reallocation

NSO→LOCAL; other cities→REMOTE; remote-explicit→REMOTE; local-service→LOCAL

## Service reallocation

Moved phrases: 10

## Group restructuring

Groups after cleanup: 40; splits: 0

## Campaign negatives

Rebuilt from layers; 0 conflicts

## Group negatives

Dangerous terms removed; 0 conflicts

## Cross-campaign negatives

0 APPROVE_SAFE / NOT APPLIED

## Ad copy corrections

Russian capitalization; separated LOCAL/REMOTE geo propositions

## Final package

X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.1-FINAL-2026-06-30

## Before/after totals

[
  {
    "campaign": "CA-01-LOCAL",
    "mode": "LOCAL",
    "v2_phrases": 311,
    "v21_phrases": 251,
    "removed": 60,
    "groups_before": 7,
    "groups_after": 7,
    "ads_before": 7,
    "ads_after": 7
  },
  {
    "campaign": "CA-01-REMOTE",
    "mode": "REMOTE",
    "v2_phrases": 316,
    "v21_phrases": 290,
    "removed": 26,
    "groups_before": 7,
    "groups_after": 7,
    "ads_before": 7,
    "ads_after": 7
  },
  {
    "campaign": "CA-02-LOCAL",
    "mode": "LOCAL",
    "v2_phrases": 143,
    "v21_phrases": 129,
    "removed": 14,
    "groups_before": 4,
    "groups_after": 4,
    "ads_before": 4,
    "ads_after": 4
  },
  {
    "campaign": "CA-02-REMOTE",
    "mode": "REMOTE",
    "v2_phrases": 143,
    "v21_phrases": 136,
    "removed": 7,
    "groups_before": 4,
    "groups_after": 4,
    "ads_before": 4,
    "ads_after": 4
  },
  {
    "campaign": "CA-03-LOCAL",
    "mode": "LOCAL",
    "v2_phrases": 76,
    "v21_phrases": 72,
    "removed": 4,
    "groups_before": 3,
    "groups_after": 3,
    "ads_before": 3,
    "ads_after": 3
  },
  {
    "campaign": "CA-03-REMOTE",
    "mode": "REMOTE",
    "v2_phrases": 76,
    "v21_phrases": 72,
    "removed": 4,
    "groups_before": 3,
    "groups_after": 3,
    "ads_before": 3,
    "ads_after": 3
  },
  {
    "campaign": "CA-04-LOCAL",
    "mode": "LOCAL",
    "v2_phrases": 48,
    "v21_phrases": 45,
    "removed": 3,
    "groups_before": 1,
    "groups_after": 1,
    "ads_before": 1,
    "ads_after": 1
  },
  {
    "campaign": "CA-04-REMOTE",
    "mode": "REMOTE",
    "v2_phrases": 48,
    "v21_phrases": 45,
    "removed": 3,
    "groups_before": 1,
    "groups_after": 1,
    "ads_before": 1,
    "ads_after": 1
  },
  {
    "campaign": "CA-05-LOCAL",
    "mode": "LOCAL",
    "v2_phrases": 216,
    "v21_phrases": 215,
    "removed": 1,
    "groups_before": 6,
    "groups_after": 5,
    "ads_before": 6,
    "ads_after": 5
  },
  {
    "campaign": "CA-05-REMOTE",
    "mode": "REMOTE",
    "v2_phrases": 216,
    "v21_phrases": 215,
    "removed": 1,
    "groups_before": 6,
    "groups_after": 5,
    "ads_before": 6,
    "ads_after": 5
  }
]

## Operator decisions

HOLD queue: 5 (non-blocking)

## UNKNOWN

Commander post-import phrase count reconciliation not re-run

## SECURITY RISK

None — offline generation only

## REQUIRED VERDICT

```
CORVONERO CAMPAIGN V2.1:
PASS — SEMANTICALLY CLEAN OPERATOR IMPORT PACKAGE GENERATED

Campaigns:
10

Commercial phrase audit:
PASS

Career / education / junk phrases:
REMOVED

LOCAL / REMOTE distribution:
PASS

Service routing:
PASS

Campaign negatives:
PASS — 0 conflicts

Group negatives:
PASS — 0 conflicts

Cross-campaign negatives:
0 SAFE / REMAINDER NOT APPLIED

Ad copy:
PASS

Commander import:
NOT PERFORMED

Server upload:
NOT PERFORMED
```
