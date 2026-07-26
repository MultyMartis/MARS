# Client Ops Live Reconfirmation (GET-only)

Method: GET-only. Mutations: **0**.

| Expected | Observed | Match |
|----------|----------|-------|
| active=false | false | YES |
| nodes=17 | 17 | YES |
| executions=32 | 32 | YES |
| running=0 | 0 | YES |
| versionId=`3d2fd6fc-bc17-4e0f-b9e5-086c959afd29` | same | YES |
| Data Table rows=3 | 3 | YES |
| selected event rows=1 | 1 | YES |
| event_id=`c84e29bf-79b1-5aea-98c4-9dc8d651fc96` | same | YES |
| intake_state=FIRST_SEEN | FIRST_SEEN | YES |
| event_status=ATTENTION | ATTENTION | YES |

`delivery_state=SENT` **not required** (durable SENT ledger DEFERRED; observed `PENDING`).

Latest execution id observed: `3416` / success.

See `CLIENT-OPS-LIVE-RECONFIRMATION.json`.
