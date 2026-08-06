# PHASE 1B-D6B — Source Status vs Delivery Freshness Semantics Separation

**Status:** OFFLINE COMPLETE — production apply NOT authorized  
**Roadmap order:** A → **B** → C → E → D  
**Workstream A baseline commit:** `12e4c6ad1f4199458b6f091d084f33ca5f8a965d`

## Objective

Separate:

1. **source_status** (factual SITE-002 / Client Ops mapped status)
2. **delivery_eligibility** (whether automatic/live notification is safe now)

so that artifact age alone never rewrites factual `ATTENTION` / `OK` / `FAILED` into `BLOCKED`.

## Tokens

| Token | Result |
|-------|--------|
| `D6B_CANONICAL_BASELINE_RECONFIRMED` | PASS |
| `D6B_LIVE_BASELINE_RECONFIRMED` | PASS (GET-only) |
| `D6B_RUNTIME_BASELINE_RECONFIRMED` | PASS |
| `D6B_CURRENT_FRESHNESS_FLOW_MAPPED` | PASS |
| `D6B_SOURCE_STATUS_AUTHORITY_DEFINED` | PASS |
| `D6B_DELIVERY_ELIGIBILITY_MODEL_DEFINED` | PASS |
| `D6B_FRESHNESS_THRESHOLD_UNCHANGED` | PASS (`93600`) |
| `D6B_THRESHOLD_BOUNDARY_EXPLICIT` | PASS (`>` → 93600 fresh, 93601 stale) |
| `D6B_OFFLINE_SEMANTICS_HARNESS_PASS` | PASS (B1–B15) |
| `D6B_REGRESSION_PASS` | PASS |
| `D6B_NO_LIVE_MUTATIONS` | PASS |
| `D6B_PRODUCTION_APPLY_AUTHORIZED` | **NO** |

## Contract surface

`D6B_INTERNAL_MODEL_ONLY`

- No Data Table schema change
- No envelope schema_version bump
- Envelope retains `freshness.age_seconds` + `freshness.stale`
- New fields live on `ProcessResult` / preview (evaluation-time)

## Production readiness

```
CLIENT_OPS_UNATTENDED_PRODUCTION_READY=NO
CLIENT_OPS_AUTOMATIC_SITE002_CONNECTION_AUTHORIZED=NO
D6B_PRODUCTION_APPLY_AUTHORIZED=NO
D6C_NOT_STARTED
D6E_NOT_STARTED
D6D_NOT_STARTED
```

## Next

`READY_FOR_D6B_CONTROLLED_PRODUCTION_APPLY_CHARTER`

Recommend: **Phase 1B-D6B2 — Controlled Freshness Semantics Production Apply and Synthetic Verification** (do not begin without charter).

Evidence: `evidence/phase-1b-d6b-source-status-vs-delivery-freshness-semantics/`
