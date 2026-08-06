# WORKFLOW-FINALIZATION-PLACEMENT

**Token:** `D6A_FINALIZATION_PLACEMENT_SELECTED`

## Selected design: B

Telegram branch + success/failure classify + conditional Data Table update.

```
… → Dedupe Claim Insert → Prepare Accepted → Respond Accepted (HTTP 202)
  → Telegram Notify Accepted  (continueOnFail / continueRegularOutput)
  → Classify Telegram Delivery Outcome
  → IF Delivery Finalize
       [true]  → Delivery Ledger Finalize Update  (delivery_state only; filter event_id + PENDING)
       [false] → end (leave PENDING)
```

## Alternatives considered

| Option | Verdict |
|--------|---------|
| A. Update immediately after Telegram success only | Incomplete — misses FAILED path if node aborts |
| B. Branch + success/failure update | **Selected** — minimal + covers definite failure |
| C. Subworkflow finalizer | Overkill for current topology |
| D. Other | Not required |

## Why continue-on-fail

Live Telegram currently `continueOnFail=false`, so definite failure aborts before any post-node. Offline compose enables continue-on-fail so FAILED persistence can run in-band.
