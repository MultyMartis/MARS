# Delivery / outbox tests

Preferred path:

business transaction → enqueue delivery → claim → (send) → mark result

Candidate behavior:

1. Commit enqueues Telegram lead_card intents (payload `dry_run: true`)
2. `claim_pending_deliveries` claims pending rows (SKIP LOCKED)
3. Telegram Dry-Run node does **not** call Telegram API
4. `mark_delivery_result(...,'sent')` finalizes dry-run

| Check | Result |
|---|---|
| Duplicate delivery intent on repeated source | 0 |
| Live Telegram to Olya/customers/moderators | 0 |
| Synthetic Telegram messages | 0 |
| Outbox durable before “send” | YES |

Shadow dataset delivery count (read-only smoke after cleanup): see `pg_tests_stdout.txt` (`shadow_deliveries`).
