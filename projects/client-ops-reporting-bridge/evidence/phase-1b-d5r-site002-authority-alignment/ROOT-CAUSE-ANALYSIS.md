# ROOT-CAUSE-ANALYSIS

## Primary classification

`MONITOR_ARTIFACT_GENERATION_BUG`

## Confirmation

`ROOT_CAUSE_CONFIRMED`

## Why not other classes

| Class | Why rejected as primary |
|-------|-------------------------|
| `EXPECTED_DIFFERENT_SEMANTIC_LAYERS` | Python writes one shared classification variable into both artifacts |
| `LEGACY_FIELD` | Field is actively written and documented as operator classification, not a leftover unused field |
| `PRE_FINALIZATION_SNAPSHOT` | Conflict appears in completed scheduled folders after runner finish, not mid-run temps |
| `ADAPTER_PRECEDENCE_BUG` | Client Ops correctly fail-closes; papering over would hide emitter defect |
| `DOCUMENTATION_CONTRACT_BUG` | Docs already require fail-closed on mismatch; incomplete runner docs are secondary |
| `UNKNOWN_REQUIRES_SEPARATE_REPAIR` | Code path + artifact evidence + docs reconciliation complete |

## Secondary contributing factors

1. Runner merge prefers non-null runner keys after defaulting classification on success.
2. Quiet runs mask the bug (default equals true classification).
3. Freshness/BLOCKED client wording for stale truthful sources is a separate semantic issue (not the D5 conflict root cause).

## Evidence triad

1. **Source code:** `Finish-Summary` default + overwrite after monitor export.
2. **Artifacts:** candidate1 incoherent `NO_ACTION_REQUIRED` with onboard=7; candidate3 without runner merge matches; candidate2 accidental match with runner-default next_action.
3. **Docs:** ARTIFACT-AUTHORITY already freezes mismatch → BLOCKED and points to monitor tooling fix.

## Client Ops implication

Do **not** change adapter precedence to ignore `run-summary.classification` while the emitter still claims a duplicated classification field. Keep fail-closed. Repair SITE-002 runner (and verify Python export unchanged).
