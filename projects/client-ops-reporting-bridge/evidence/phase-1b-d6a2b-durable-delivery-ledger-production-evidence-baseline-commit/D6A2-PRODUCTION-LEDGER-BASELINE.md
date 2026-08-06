# D6A2 Production Ledger Baseline

Workflow: **MARS Client Ops Bridge — bzpm.ru** (`tkM4H0G0gM3q9Foi`)

## Apply delta

| Field | Pre-D6A2 | Post-D6A2 |
|-------|----------|-----------|
| active | false | false (after re-containment) |
| nodes | 17 | 20 |
| executions | 32 | 34 |
| versionId | `3d2fd6fc-bc17-4e0f-b9e5-086c959afd29` | `dc8746bf-df9c-425d-9b3f-4ace452ac5ef` |
| Data Table columns | 15 | 15 (unchanged) |
| Data Table rows | 3 | 4 |
| Schema migrations | — | 0 |
| Rollback required | — | no |

## Conceptual workflow delta

Telegram → Classify Telegram Delivery Outcome → IF Delivery Finalize → Delivery Ledger Finalize Update

Telegram modified only as required for outcome classification: `continueOnFail=true` (+ accepted error-output behavior).

Finalizer writes **only** `delivery_state` and preserves `event_id`, `intake_state`, `event_status`, source identity, event fingerprint, schema identity.

## Temporary activation lifecycle (not Workstream C)

`active=false` → `active=true` → `active=false`
Activation changes: **2**
Token: `D6A2_WORKFLOW_RECONTAINED`
