# Retry / defer tests

| Mechanism | Implementation | Result |
|---|---|---|
| Sheets Quota Defer Gate | Not present in v3 | N/A (removed) |
| Application job | `enqueue_job(..., available_at=now()+60s, dedupe_key=...)` | PASS (`JOB_OK`) |
| Delivery retry status | `mark_delivery_result(...,'retry', retry_after_seconds)` supported by contract | Contract present |
| Hammer loops | Not used | PASS |
| Bounded backoff | `available_at` / job claim lease | PASS |

No 30-second source hammer loops. Retries are durable and claimable, not Sheets-quota specific.
