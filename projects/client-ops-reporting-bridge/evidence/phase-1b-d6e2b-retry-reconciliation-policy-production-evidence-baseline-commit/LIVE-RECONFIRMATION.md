# LIVE-RECONFIRMATION — D6E2B (GET-only)

**Token:** `D6E2B_LIVE_BASELINE_RECONFIRMED`

Method: GET-only via `evidence/phase-1b-d6e-retry-and-concurrency-policy-binding/_get-precheck.mjs`.
No activation. No webhook. No Telegram. No Data Table mutation. No retry. No reconciliation mutation.

| Field | Expected | Observed |
|-------|----------|----------|
| active | false | false |
| nodes | 20 | 20 |
| executions | 34 | 34 |
| running | 0 | 0 |
| versionId | `dc8746bf-df9c-425d-9b3f-4ace452ac5ef` | match |
| Data Table columns | 15 | 15 |
| rows | 4 | 4 |
| historical `c84e29bf-…` | FIRST_SEEN / ATTENTION / PENDING | match |
| D6A2 `d6a2a001-…` | FIRST_SEEN / OK / SENT | match |

Verdict of underlying GET script: `D6E_LIVE_BASELINE_RECONFIRMED` → D6E2B maps to `D6E2B_LIVE_BASELINE_RECONFIRMED`.
