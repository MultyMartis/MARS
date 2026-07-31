# PRODUCTION-MONITORING-BASELINE-v1

**Phase:** 3D  
**Window:** rolling **7 days** via Admin `/stats` (+ Operational execution health)  
**No new monitoring workflow**

## Minimum metrics

| Metric | Primary signal |
|--------|----------------|
| Gmail polls | Operational schedule executions; `last_poll_success_at` |
| Eligible messages | Lead-route executions / intake_route=lead |
| Leads processed | Terminal success with PROCESSED + incoming remove |
| Telegram delivery success/failure | `telegram_ok` / `last_delivery_status` |
| RAW writes | RAW append runs (expect ≥1 per process attempt) |
| CLEAN writes | CLEAN write runs |
| Duplicate / reprocessed counts | `duplicate_status` distribution in CLEAN / cards |
| Bad-quality leads | `quality_status=bad` / unusable |
| AI provider calls | Must remain **0** while AI OFF |
| Processing errors | `/last_error`, ERRORS sheet, failed executions |
| Last poll success | CONFIG / `/status` |
| Last lead success | CONFIG / `/status` |

## Operating cadence

1. Daily glance: `/status` `/health` `/ai_status`.  
2. After any incident: `/last_error` + capture window.  
3. Weekly: `/stats` 7-day bounded summary.  
4. Confirm Sales-Manager-v2 still inactive; sole intake = Operational.dev.

## Exclusions

- SYNTHETIC_TEST rows excluded from production stats.  
- No third workflow for metrics.  
- No PII in exported monitoring notes.
