# IDEMPOTENCY-REPLAY-A-v1

**Fixture A:** `lead_synth_cleandup_a01` / SOURCE_EVENT_ID `msg_synth_cleandup_a01`  
**Marker:** `CLEAN_DUP_FORENSIC_20260826`  
**Method:** isolated TMP Sheets upsert cloning Ops CLEAN schema (`appendOrUpdate` / `lead_id`); ADMIN_A-only route; 0 moderator/customer Telegram.

## Results

| Pass | Logical CLEAN count for A |
|-----:|--------------------------:|
| baseline (prior debug leftover) | 1 |
| upsert 1 | 1 |
| upsert 2 | 1 |
| upsert 3 | 1 |

| Metric | Value |
|--------|------:|
| same-event executions tested | 3 |
| additional CLEAN leads from same-event replay | **0** |

## Archive

After proof: `manager_status=processed`, `close_reason=legacy_synthetic_fixture_cleanup`. Pending fixture rows after archive = **0**.
