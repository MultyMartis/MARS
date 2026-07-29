# CONCURRENCY-FIXTURE-MATRIX (EC1–EC10)

**Token:** `D6E_CONCURRENCY_HARNESS_PASS`

| Id | Scenario | Expected |
|----|----------|----------|
| EC1 | Same-event concurrent attempts | both UNSAFE_TO_RETRY / rejected |
| EC2 | Second acquire while lock held | LIFECYCLE_LOCK_HELD |
| EC3 | Different event while lock held | UNSAFE_TO_RETRY + LIFECYCLE_LOCK_HELD |
| EC4 | Unresolved active session | rejected; concurrency remains 1 |
| EC5 | Request budget exhausted | REQUEST_BUDGET_EXHAUSTED |
| EC6 | PENDING must not consume attempt | rejected |
| EC7 | SENT cannot re-enqueue | rejected |
| EC8 | FAILED cannot auto-re-enqueue | rejected |
| EC9 | Stale cannot re-enqueue | rejected |
| EC10 | New event only after containment | blocked while session active; allowed sequentially after |

Verdict: `D6E_CONCURRENCY_REMAINS_ONE`.
