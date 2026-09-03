# JOB-TESTS-v1

**Result:** PASS  
**Function:** `app_iseo_sales.claim_jobs` (SKIP LOCKED)

| Assertion | Result |
|-----------|--------|
| Pending job with `available_at` | PASS |
| Retry / attempts fields usable | PASS |
| Lease fields (`locked_by` / `lease_until`) set on claim | PASS |
| Concurrent claim exclusivity (one worker wins a given job) | PASS |
| Completed / dead transitions per test harness | PASS |

Index sanity: `idx_jobs_status_available` used for pending/retry + `available_at` lookups (EXPLAIN Index Scan).
