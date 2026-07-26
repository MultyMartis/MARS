# POST-TELEGRAM-LEDGER-WRITE-FAILURE

**Token:** `D6A_POST_TELEGRAM_LEDGER_WRITE_FAILURE_POLICY_DEFINED`

## Scenario

1. Row claimed `PENDING`
2. Telegram succeeds (message delivered)
3. Data Table terminal update fails

## Durable observation

- Actual customer notification: occurred once
- Data Table: may remain `PENDING`

## Policy (fail-closed against duplicate)

1. **No automatic Telegram resend** while PENDING after a FIRST_SEEN claim that may have notified.
2. Duplicate producer intake remains suppressed (dedupe) — no second Telegram.
3. Reconciliation evidence: n8n execution history for `Telegram Notify Accepted` (sanitized message_id) is sufficient GET-only proof to infer SENT for operator repair under a **separate** charter.
4. Future recovery may retry **finalizer-only** (ledger update) without invoking Telegram — not implemented as automatic in D6A; design-compatible.
5. Automatic FAILED→PENDING or PENDING replay send is forbidden (workstream E not in scope).

## Why PENDING is the safe unresolved state

Marking FAILED would be false (message delivered). Marking SENT without durable write is the gap we are fixing — if write fails, PENDING + no-resend is safer than inventing success in memory only.
