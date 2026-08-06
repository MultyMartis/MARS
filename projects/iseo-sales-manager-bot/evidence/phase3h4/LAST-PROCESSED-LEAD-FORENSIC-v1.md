# LAST PROCESSED LEAD FORENSIC v1

## Symptom

`/status` displayed last processed lead at **22:23 МСК** — inconsistent with known production epoch (05.08.2026 17:22 МСК processed lifecycle).

## Root cause

Status renderer used `last_lead_success_at` / `last_success_at` stamped by **synthetic test delivery** `msg_synth_3g11d_t1_*`:

| Key | Misleading value | Display (MSK) |
|---|---|---|
| `last_lead_success_at` | 2026-08-05T19:23:37.997Z | 22:23 МСК |

## Authoritative production lead

| Field | Value |
|---|---|
| lead_id | `lead_19fd2052066e18b7` |
| received_at_business | 2026-08-05 16:02:57 Europe/Moscow |
| lifecycle_status | processed |
| lifecycle_changed_at | 2026-08-05T14:22:55.186Z (= **05.08.2026 17:22 МСК**) |
| is_real_lead | true |
| is_probable_test | false |
| archive_state | active |
| production_generation | v2 |

## Repair

1. Status Code node: prefer `last_production_processed_*` keys for operator-facing production line
2. CONFIG backfill: `last_production_processed_at=2026-08-05T14:22:55.186Z`, `last_production_processed_lead_id=lead_19fd2052066e18b7`
3. Operational Runtime State: stamp production keys only on non-test successful processing

## Verdict

`LAST PROCESSED LEAD TRUTH REPAIRED — SYNTHETIC STAMP DECOUPLED FROM PRODUCTION DISPLAY`
