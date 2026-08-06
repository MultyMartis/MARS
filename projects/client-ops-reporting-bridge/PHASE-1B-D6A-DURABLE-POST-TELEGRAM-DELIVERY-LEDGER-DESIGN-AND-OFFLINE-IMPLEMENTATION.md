# PHASE-1B-D6A — Durable Post-Telegram Delivery Ledger Design and Offline Implementation

**Phase:** 1B-D6A
**Date:** 2026-07-27
**Live apply:** NO
**Scope:** Workstream A only (durable post-Telegram SENT/FAILED ledger)

## Objective

Close the architecture gap proven by D5R2A / D6: Telegram can succeed while Data Table `delivery_state` remains `PENDING` forever. Implement and prove **offline** a durable terminal delivery ledger so FIRST_SEEN claim → PENDING → Telegram → SENT|FAILED.

## Accepted D6 order

`A → B → C → E → D` — this phase implements **A only**.

## Gates (pre)

- `D6A_LIVE_BASELINE_RECONFIRMED`
- `D6A_RUNTIME_BASELINE_RECONFIRMED`
- `D6A_EXISTING_SCHEMA_SUFFICIENT`
- `D6A_DELIVERY_STATE_MACHINE_DEFINED`
- `D6A_FINALIZATION_PLACEMENT_SELECTED`
- `D6A_TELEGRAM_SUCCESS_AUTHORITY_DEFINED`
- `D6A_FAILURE_SEMANTICS_DEFINED`
- `D6A_POST_TELEGRAM_LEDGER_WRITE_FAILURE_POLICY_DEFINED`
- `D6A_DUPLICATE_SUPPRESSION_PRESERVED`
- `D6A_FINALIZER_CONTRACT_DEFINED`
- `D6A_LEDGER_SECURITY_MODEL_PASS`

## Gates (post)

- `D6A_OFFLINE_WORKFLOW_IMPLEMENTATION_READY`
- `D6A_OFFLINE_SCHEMA_MODEL_READY`
- `D6A_HTTP_202_SEMANTICS_PRESERVED`
- `D6A_RETRY_POLICY_UNCHANGED`
- `D6A_MAX_SAFE_CONCURRENCY=1`
- `D6A_OFFLINE_LEDGER_HARNESS_PASS`
- `D6A_REGRESSION_PASS`
- `D6A_NO_LIVE_MUTATIONS`

## Implementation artifacts

| Path | Role |
|------|------|
| `n8n/runners/lib/client-ops-delivery-ledger.mjs` | Pure state machine + finalizer |
| `n8n/runners/lib/client-ops-delivery-ledger-compose.mjs` | Offline workflow compose delta |
| `n8n/harness/delivery-ledger-harness.mjs` | Offline harness |
| `n8n/harness/delivery-ledger-cases/` | Fixtures |
| `n8n/runners/validate-client-ops-d6a-delivery-ledger.mjs` | Offline validator |
| `evidence/phase-1b-d6a-durable-post-telegram-delivery-ledger/` | Evidence pack |

## Schema decision

`D6A_EXISTING_SCHEMA_SUFFICIENT` — terminal persistence uses existing `delivery_state` only. Optional observability columns (`telegram_message_id`, `delivery_finished_at`, `delivery_error_class`) deferred; reconciliation uses n8n execution evidence.

## Finalization placement

**B** — Telegram (continue on fail) → Classify → IF finalize → Data Table update (`delivery_state` only), filters `event_id` + `delivery_state=PENDING`.

## Invariants

- `INTAKE_STATE_IMMUTABLE_DURING_DELIVERY_FINALIZATION`
- `EVENT_STATUS_IMMUTABLE_DURING_DELIVERY_FINALIZATION`
- HTTP 202 remains intake-only (`FIRST_SEEN`)
- Duplicate intake never re-sends Telegram
- `max_retries=0`, concurrency=1

## Historical live event

`c84e29bf-79b1-5aea-98c4-9dc8d651fc96` remains `delivery_state=PENDING` in production — intentional evidence; not mutated by D6A.

## Readiness

`READY_FOR_D6A_CONTROLLED_PRODUCTION_APPLY_CHARTER`

Does **not** authorize production apply. Next separately chartered phase: **1B-D6A2**.

## Evidence

See `evidence/phase-1b-d6a-durable-post-telegram-delivery-ledger/`.
