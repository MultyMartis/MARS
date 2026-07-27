# Phase 1B-D6C2 — Controlled Activation Lifecycle Production Apply and Synthetic Dry-Window Verification

**Status:** COMPLETE (production dry-window verified)
**Date (UTC evidence):** 2026-07-26
**Readiness:** `READY_FOR_D6C2_EVIDENCE_BASELINE_COMMIT`
**Final verdict:** COMPLETE — CONTROLLED ACTIVATION LIFECYCLE VERIFIED IN PRODUCTION WITH ZERO-REQUEST DRY WINDOW; WORKFLOW RE-CONTAINED WITHOUT WEBHOOK, TELEGRAM OR DATA MUTATION

## Scope

Workstream **C** only. Narrow controlled production verification of the accepted D6C activation lifecycle using a **DRY / NO-REQUEST** bounded window against the real Client Ops control plane.

Does **not** implement E (retry/concurrency) or D (unattended). Does **not** mutate A/B semantics. Does **not** reconcile historical D5R2A PENDING.

## Accepted baselines

| Stream | Commit / state |
|--------|----------------|
| Order | A → B → C → E → D |
| A | `12e4c6ad1f4199458b6f091d084f33ca5f8a965d` — COMMITTED / DEPLOYED (ancestor) |
| B | `94d06c05ea79eb22780588d91064006c3edf2a05` — COMMITTED (ancestor) |
| C | Offline implemented in D6C; **this phase** = production dry lifecycle proof |
| E / D | NOT STARTED |

Accepted D6C model: HYBRID C1→C3 bounded; request window fail-closed; re-containment GET-verified.

## Production surface

`D6C2_PRODUCTION_SURFACE_CONTROL_TOOL_ONLY`

No n8n workflow content/config mutation. Operator-side orchestrator + activation API only.

## Dry charter (sanitized)

See `evidence/phase-1b-d6c2-controlled-activation-lifecycle-production-dry-window/D6C2-CHARTER.json`.

- `max_requests=1`, `planned_requests=0`, `allow_webhook_requests=false`
- `max_retries=0`, `max_concurrency=1`, `max_activation_changes=2`
- `window_seconds=30` (bounded; window closed immediately after dry proof — no idle wait)
- `dry_control=true`, `operation_type=DRY_CONTROL_NO_REQUEST`
- No customer payload / no SITE-002 fabricated event

## Production execution (observed)

1. Live baseline GET: inactive, nodes=20, executions=34, running=0, version pin match, table 15×4
2. Lifecycle lock acquired (activation attempts before lock = 0)
3. Dry preflight PASS
4. Zero-request invariant armed
5. Activate once: active false→true
6. Readiness GET: active=true, version/nodes/webhook/auth structural OK, running=0
7. Request window opened; local reject `WEBHOOK_REQUEST_PROHIBITED_BY_CHARTER`; requests=0
8. Window closed
9. Deactivate once: active true→false (emergency=0)
10. Recontainment GET: active=false; lock released

Activation changes: **2**. Executions: **34→34**. Rows: **4→4**. Telegram: **0**.

## Regressions (post)

- D6A harness 11/11 + validator 48/48
- D6B harness 20 pass, threshold 93600, operator `>`
- D6C harness 30/30

## Production readiness (unchanged)

```
CLIENT_OPS_UNATTENDED_PRODUCTION_READY=NO
CLIENT_OPS_AUTOMATIC_SITE002_CONNECTION_AUTHORIZED=NO
D6E_NOT_STARTED
D6D_NOT_STARTED
HISTORICAL_D5R2A_ROW_RECONCILIATION_AUTHORIZED=NO
```

## Git policy

No staging / commit / push by this phase. `MAIN_INDEX_UNTOUCHED_BY_D6C2`.

## Next (do not begin automatically)

**Phase 1B-D6C2B — Controlled Activation Lifecycle Production Evidence Baseline Commit**

After evidence acceptance/commit, architectural next is **Phase 1B-D6E — Retry and Concurrency Policy Binding** (not started here).

## Evidence

`evidence/phase-1b-d6c2-controlled-activation-lifecycle-production-dry-window/`
