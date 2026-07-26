# D6A-SOURCE-REVALIDATION

**Token:** `D6A2_ACCEPTED_D6A_SOURCE_REVALIDATED`

## Commands

```text
node projects/client-ops-reporting-bridge/n8n/harness/delivery-ledger-harness.mjs
node projects/client-ops-reporting-bridge/n8n/runners/validate-client-ops-d6a-delivery-ledger.mjs
```

## Results

| Suite | Result |
|-------|--------|
| Delivery ledger harness | **11/11 PASS** — `D6A_OFFLINE_LEDGER_HARNESS_PASS` |
| D6A validator | **48/48 PASS** |

## Accepted D6A decision retained

- Schema: `D6A_EXISTING_SCHEMA_SUFFICIENT`
- States: PENDING / SENT / FAILED
- Finalizer: `LOOKUP_VALIDATE_UPDATE_SEQUENTIAL_ONLY`
- Intake/event_status immutable during finalization
- HTTP 202 = intake only
- retries=0; concurrency=1
- No live apply in D6A (`live_apply_performed=false`)

## Drift

No material source drift vs accepted D6A report. Compose still expects 17→20 nodes.
