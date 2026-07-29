# CURRENT-RETRY-FLOW

**Token:** `D6E_CURRENT_RETRY_AND_FAILURE_FLOW_MAPPED`

End-to-end observation map (policy binding only; D6E does not execute retries):

1. **Source** — SITE-002 monitor/producer emits event identity (`event_id` / fingerprint).
2. **Preflight** — freshness (`delivery_eligibility`), containment, lifecycle lock, concurrency=1 gates.
3. **Activation** — Workstream C controlled lifecycle (inactive → activate → readiness → window).
4. **POST** — webhook request construction / transmission / HTTP observation.
5. **n8n intake / claim** — workflow intake; durable Data Table first-seen claim.
6. **Telegram** — customer delivery attempt (SUCCESS / DEFINITE_FAILURE / UNKNOWN).
7. **Ledger** — durable `delivery_state` PENDING / SENT / FAILED (Workstream A).
8. **HTTP observation** — status + body class (202 / 200 duplicate / 4xx / 5xx / lost).
9. **Reconciliation** — authority-ordered read-only plan when outcome is ambiguous (`RECONCILE_BEFORE_RETRY`).

Principle: **NO PROOF OF NON-DELIVERY ≠ SAFE TO RETRY**.
