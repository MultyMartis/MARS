# TEST-RESULTS

## D6A offline ledger harness

```
node n8n/harness/delivery-ledger-harness.mjs
```

| Metric | Value |
|--------|-------|
| Cases | 11 |
| Passed | 11 |
| Failed | 0 |
| Verdict | `D6A_OFFLINE_LEDGER_HARNESS_PASS` |

Network: none. Telegram: none. n8n mutation: none.

## D6A offline validator

```
node n8n/runners/validate-client-ops-d6a-delivery-ledger.mjs
```

| Metric | Value |
|--------|-------|
| Gates | 48 |
| Pass | 48 |
| Fail | 0 |
| Verdict | PASS |

## Covered requirements (harness)

1. PENDING→SENT
2. PENDING→FAILED
3. intake_state unchanged
4. event_status unchanged
5. event_id unchanged
6. duplicate SENT no resend
7. duplicate PENDING no resend
8. duplicate FAILED no auto-retry
9. SENT→FAILED rejected
10. finalizer double-call idempotent
11. Telegram success + ledger write failure → no second Telegram
12. HTTP 202 intake-only
13. no secrets in terminal metadata
14. concurrency=1 constant
15. max_retries=0 constant
16. compose validates offline 20-node workflow
