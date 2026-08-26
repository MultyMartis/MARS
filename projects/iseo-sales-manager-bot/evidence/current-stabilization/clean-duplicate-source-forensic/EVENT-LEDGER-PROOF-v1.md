# EVENT-LEDGER-PROOF-v1

## CLEAN creation

Fixture A: one logical CLEAN lead across 3 upserts. Fixture B: one additional distinct lead.

## DEDUP / ledger surface

Production path now upserts DEDUP by `dedup_key` (same SOURCE_EVENT_ID does not accumulate append-only index rows for the primary gmail key).

## Telegram / reminder side effects

Isolated harness did **not** emit moderator/customer Telegram (0). Fixtures archived out of pending selectors (`pending_fixture_rows_after_archive=0`).

## Retry telemetry vs creation

Multiple upsert executions may refresh `last_seen_at` / row cells; they must not create additional `lead_id` rows — proven for A.

## Limitation (honest)

Full end-to-end Ops Gmail→Telegram creation-event counter was not customer-safely re-fired; proof is Sheets idempotency of the patched write contract used by Ops.
