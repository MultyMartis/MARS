# MINIMAL-WORKFLOW-DELTA

**Token:** `D6A2_MINIMAL_PRODUCTION_DELTA_DEFINED`

## Before → after

| Metric | Before | After |
|--------|--------|-------|
| nodes | 17 | 20 |
| versionId | `3d2fd6fc-bc17-4e0f-b9e5-086c959afd29` | `dc8746bf-df9c-425d-9b3f-4ace452ac5ef` |
| active | false | false |
| Data Table columns | 15 | 15 |

## Topology (Workstream A only)

```text
Respond Accepted
  → Telegram Notify Accepted   (continueOnFail=true)
    → Classify Telegram Delivery Outcome
      → IF Delivery Finalize
          [true]  → Delivery Ledger Finalize Update  (delivery_state only; filter event_id + PENDING)
          [false] → (end; remain PENDING; no resend)
```

## Nodes added

1. `Classify Telegram Delivery Outcome` — SUCCESS / DEFINITE_FAILURE / AMBIGUOUS
2. `IF Delivery Finalize` — `should_finalize`
3. `Delivery Ledger Finalize Update` — Data Table update

## Nodes modified

- `Telegram Notify Accepted`: `continueOnFail=true`, `onError=continueRegularOutput`
  WHY: definite Telegram failure must reach classifier for PENDING→FAILED

## Explicitly unchanged

- webhook path / Header Auth credential
- Telegram credential / chat binding
- dedupe claim / FIRST_SEEN logic
- Respond Accepted 202 semantics
- event mapping / status mapping
- producer contract

See also `DELTA-ALLOWLIST.json`.
