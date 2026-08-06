# OFFLINE-WORKFLOW-IMPLEMENTATION

**Token:** `D6A_OFFLINE_WORKFLOW_IMPLEMENTATION_READY`

## Production vs source

| Layer | State |
|-------|-------|
| Live workflow `tkM4H0G0gM3q9Foi` | 17 nodes; no delivery finalizer; **unchanged by D6A** |
| Repo compose D1 | Builds dedupe onto 10-node base |
| Repo compose D6A | `composeDeliveryLedgerPutFromLive` builds finalizer onto **17-node** live-shaped fixture |

## Implementation files

- `n8n/runners/lib/client-ops-delivery-ledger.mjs`
- `n8n/runners/lib/client-ops-delivery-ledger-compose.mjs`
- `n8n/harness/delivery-ledger-harness.mjs`
- `n8n/harness/delivery-ledger-cases/offline-live-workflow-17.json` (sanitized GET export)
- `n8n/runners/validate-client-ops-d6a-delivery-ledger.mjs`

## Deployability

Offline compose + validate prove a future PUT payload (20 nodes) with `applied=false`. Production apply requires separate D6A2 charter.
