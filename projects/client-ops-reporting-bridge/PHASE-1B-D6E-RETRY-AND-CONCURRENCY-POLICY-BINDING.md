# PHASE-1B-D6E — Retry and Concurrency Policy Binding

## Status

Offline retry/concurrency policy binding designed and implemented. Production apply **not** authorized. Live mutations by D6E: **0**.

`READY_FOR_D6E_READ_ONLY_PRODUCTION_POLICY_VERIFICATION_CHARTER`

## Model

Canonical roadmap order: **A → B → C → E → D**.

Workstreams **A / B / C** semantics preserved. Workstream **D** not started.

Defaults:

- `AUTOMATIC_RETRIES_ENABLED=NO`
- `MAX_AUTOMATIC_RETRIES=0`
- `MAX_SAFE_CONCURRENCY=1`
- Ambiguity → `RECONCILE_BEFORE_RETRY`
- Verdict: `D6E_CONCURRENCY_REMAINS_ONE` (D1 `DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN` not overturned)

## Four decision states

| State | Role |
|-------|------|
| `SAFE_TO_RETRY` | Positive non-delivery proof; still requires new explicit charter; D6E does **not** execute |
| `UNSAFE_TO_RETRY` | Replay unsafe / duplicate risk / invariant violation |
| `RECONCILE_BEFORE_RETRY` | Ambiguous outcome; durable state must be queried first |
| `FINAL_FAILURE` | Terminal for current charter/event |

## Baselines

- Workstream A: `12e4c6ad1f4199458b6f091d084f33ca5f8a965d`
- Workstream B: `94d06c05ea79eb22780588d91064006c3edf2a05`
- Workstream C: `79c2071dd8ae8096506d45bc189e1f732b310d35`

## Implementation

Evidence: `evidence/phase-1b-d6e-retry-and-concurrency-policy-binding/`

- `n8n/runners/lib/client-ops-retry-policy.mjs`
- `n8n/runners/lib/client-ops-retry-reason-codes.mjs`
- `n8n/runners/lib/client-ops-reconciliation-planner.mjs`
- `n8n/runners/lib/client-ops-retry-charter.mjs`
- `n8n/runners/lib/client-ops-concurrency-policy.mjs`
- `n8n/harness/d6e-retry-concurrency-policy-harness.mjs`
- `src/client_ops_reporting_bridge/retry_policy_binding.py`
- `tests/test_retry_policy_d6e.py`

## Gates (offline)

- `D6E_OFFLINE_POLICY_HARNESS_PASS` — E1–E40 + invariants
- `D6E_CONCURRENCY_HARNESS_PASS` — EC1–EC10
- Harness total **54/54**
- `D6E_NO_LIVE_MUTATIONS`
- `D6D_NOT_STARTED`

## Explicit non-goals

- No automatic retry loops
- No production webhook / activation / Telegram / Data Table mutation
- No historical D5R2A row reconciliation apply
- No unattended / Workstream D integration

## Next

Phase 1B-D6E2 — Retry and Reconciliation Policy Production Read-Only Verification (separate charter; not started).
