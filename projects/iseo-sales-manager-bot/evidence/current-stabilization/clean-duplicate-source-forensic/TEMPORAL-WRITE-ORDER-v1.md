# TEMPORAL-WRITE-ORDER-v1

## Incident pattern (cluster `lead_19fcce0e42028e45`)

Representative reconstructed order (row timestamps ~30s apart):

| T | Event |
|---|--------|
| T0 | SOURCE_EVENT_ID received (Gmail id `19fcce0e42028e45`) |
| T1 | RAW append (same event) |
| T2 | Classify → often `new` (DEDUP miss/race) |
| T3 | CLEAN **append** row #1 (`lead_19fcce0e42028e45`) |
| T4 | DEDUP **append** (or miss) |
| T5 | Workflow ends / Telegram path |
| T6 | Same SOURCE_EVENT_ID processed again (~30s) |
| T7 | CLEAN **append** row #2 (same lead_id) |
| … | Repeats → 16 CLEAN rows by 13:13:12 |

## Earliest missing barrier

Pre-write idempotency on CLEAN: **appendOrUpdate by `lead_id`** (and DEDUP upsert by `dedup_key`) — not a downstream cleanup.

## Post-patch expected order for same SOURCE_EVENT_ID

| T | Event |
|---|--------|
| T0 | source event |
| T1 | RAW (per existing design) |
| T2 | Classify → `reprocessed` if DEDUP hit |
| T3 | CLEAN **upsert** same `lead_id` (no second row) |
| T4 | DEDUP **upsert** same `dedup_key` |
| T5+ | Replay → additional CLEAN logical leads = **0** |
