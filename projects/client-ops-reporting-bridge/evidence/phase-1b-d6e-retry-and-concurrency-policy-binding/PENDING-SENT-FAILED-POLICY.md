# PENDING-SENT-FAILED-POLICY

**Tokens:** `D6E_PENDING_NEVER_AUTO_RETRIED` · `D6E_SENT_TERMINAL_NO_RETRY` · `D6E_FAILED_TERMINAL_NO_AUTO_RETRY`

| `delivery_state` | Policy |
|------------------|--------|
| PENDING | Never auto-retry; reconcile / operator review |
| SENT | Terminal success; no retry |
| FAILED | Terminal for auto path; no auto-retry |

Workstream A semantics unchanged. New source runs create new `event_id` (not a retry).
