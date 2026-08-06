# MANUAL-IMPORT-REPORT-CHAIN

## Identity

| Field | Value |
|-------|-------|
| run_id | `mars-20260806-160514-5d2cdb3b` |
| trigger_source | `ADMIN_MANUAL` |
| final_status | `ATTENTION_OFFERS_INPUT_MISSING` |
| report_class | `CATALOG_SUCCESS_OFFERS_INPUT_MISSING` |
| event_id | `a71c3991-74ca-5dac-952e-7eb51200c848` |
| n8n execution | `24268` |

## Chain (observed)

1. Admin POST `tool/mars_1c_exchange/run` → accepted async (~298 ms)
2. Canonical wrapper completed catalog PASS + offers PASS with zero `offers0_*.xml`
3. Terminal result written (`terminal.json`, schema `1b-d6g.1`)
4. Completion dispatcher built envelope for exact `run_id`
5. First webhook attempt HTTP 400 (envelope shape defect) — no Telegram
6. Envelope builder fixed to `mars.client_ops.report` v1.0
7. Re-dispatch HTTP 202 → n8n execution `24268` success
8. Data Table first-seen claim + delivery finalize SENT
9. Telegram message delivered (`telegram_outcome=SUCCESS`, message_id=22)
10. Local marker `*.delivered.json` prevents duplicate redispatch

## Latency notes

- Import duration: ~4.13 s
- Terminal completed_at (MSK+3): `2026-08-06T16:05:18+03:00`
- Successful Telegram finalize: `2026-08-06T13:06:49.488Z`
- Terminal→Telegram wall clock includes one failed dispatch + fix (~95 s), not a timer wait
- No 13:00 producer timer involved
