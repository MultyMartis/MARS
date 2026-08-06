# STATUS DATA SOURCE MATRIX v1

## `/status` field authority (post Phase 3H.4)

| UI line / concept | Authoritative source | Must NOT use |
|---|---|---|
| Gmail poll last success | `last_poll_success_at` + `gmail_poll_heartbeat` from **scheduled** Operational poll | `/health` on-demand probe |
| Last production lead processed | `last_production_processed_at` + `last_production_processed_lead_id` | Synthetic test `msg_synth_*` stamps |
| Last any success (technical) | `last_success_at` / `last_lead_success_at` (labeled technical if shown) | As sole production truth |
| AI state | CONFIG `ai_enabled` | OpenRouter call history |
| Reminders | CONFIG reminder keys + active recipient count | REMINDER_DELIVERIES alone |
| Reporting sync | CONFIG `reporting_sync_state` | Assumed auto-sync |
| Parser / template versions | CONFIG allowlisted keys | Stale v2 keys |

## Production lead anchor (authoritative)

| Field | Value |
|---|---|
| lead_id | `lead_19fd2052066e18b7` |
| received_at_business | 2026-08-05 16:02:57 Europe/Moscow |
| lifecycle_status | processed |
| lifecycle_changed_at | 2026-08-05T14:22:55.186Z (= 05.08.2026 17:22 МСК) |
| is_real_lead | true |
| is_probable_test | false |
| archive_state | active |
| production_generation | v2 |

## Misleading pre-repair source

Synthetic test delivery `msg_synth_3g11d_t1_*` wrote `last_lead_success_at=2026-08-05T19:23:37.997Z` (= 22:23 МСК) — **not** production truth.

## Architecture reference

See `architecture/OPERATIONAL-STATUS-TRUTH-CONTRACT-v1.md`.
