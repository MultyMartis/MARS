# STATUS EXECUTION FORENSIC v1

## Path traced

1. Telegram Trigger
2. Normalize Command (`/status`)
3. Read Authorization Config (CONFIG sheet)
4. Collapse Authorization Context → `config_map`
5. Check User Authorization (propagates `config_map`)
6. Route Command → Status
7. Status Code (Phase 3H.4 body pre-repair)
8. Capture Admin Reply / Safe Telegram Reply

## Live CONFIG interest (pre-repair probe)

| Key | Present | Value |
|---|---|---|
| last_production_processed_at | key yes | **empty string** |
| last_production_processed_lead_id | key yes | **empty string** |
| last_processed_at | key yes | **empty string** |
| last_lead_success_at | yes | 2026-08-05T19:23:37.997Z (synthetic 22:23) |
| production_stats_epoch | yes | 2026-08-05T13:02:57.000Z |
| environment | yes | production |

## Pre-3H.4 Telegram sample (exec 24195)

- Used legacy synthetic stamp → displayed 22:23 МСК
- `last_production_processed_*` absent/empty

## Post-3H.4 / pre-3H.4.1 behavior

Status Code correctly refused synthetic `last_lead_success_at` and, with empty production cache, fail-closed to `нет данных`.
