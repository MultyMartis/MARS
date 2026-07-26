# D6A Offline Ledger Baseline

**Schema decision:** `D6A_EXISTING_SCHEMA_SUFFICIENT` (15 columns; no migration required)

## States

`PENDING` | `SENT` | `FAILED`

## Accepted transitions

| Transition | Rule |
|------------|------|
| PENDING → SENT | accepted terminal success |
| PENDING → FAILED | accepted terminal failure |
| SENT → SENT | idempotent |
| FAILED → FAILED | idempotent |
| SENT → FAILED | reject |
| FAILED → SENT | reject / separate recovery authority |

Ambiguous delivery → remain `PENDING` (no automatic resend).
Telegram success + ledger-write failure → remain `PENDING` (reconcile first; no automatic resend).

## Invariants

- `INTAKE_STATE_IMMUTABLE_DURING_DELIVERY_FINALIZATION`
- `EVENT_STATUS_IMMUTABLE_DURING_DELIVERY_FINALIZATION`
- Finalizer update model: `D6A_FINALIZER_UPDATE_MODEL=LOOKUP_VALIDATE_UPDATE_SEQUENTIAL_ONLY`
- Concurrency: 1 · Retries: 0
- HTTP 202 = intake accepted / FIRST_SEEN (**not** terminal delivery completion)

## Offline proof

| Suite | Result |
|-------|--------|
| Delivery ledger harness | **11/11 PASS** |
| D6A validator | **48/48 PASS** |

`PENDING → FAILED` remains **offline authoritative**.
