# SHEETS HEALTH PREFLIGHT v1

## Verdict

`SHEETS DELIVERY PATH HEALTHY` (isolated production-node probes)

## Caveat (full pipeline)

Subsequent dual-card full-path attempts still hit Google Sheets quota on `Read ACCESS_CONTROL` / `Upsert LEAD_DELIVERIES Claim` under multi-op load. Fail-closed preserved (`sendOk=0`).

## Operations (sanitized)

| Operation | ok | latencyMs | retry | quota | items | error |
|-----------|----|-----------|-------|-------|------:|-------|
| CONFIG read | true | 392 | 0 | false | 67 | none |
| RAW append | true | 3937 | 0 | false | 1 | none |
| RAW read | true | 1400 | 0 | false | 109 | none |
| CLEAN append | true | 1193 | 0 | false | 1 | none |
| CLEAN read | true | 432 | 0 | false | 101 | none |
| LEAD_DELIVERIES read | true | 429 | 0 | false | 51 | none |
| LEAD_DELIVERIES claim write | true | 822 | 0 | false | 1 | none |
| LEAD_DELIVERIES delivered stamp | true | 615 | 0 | false | 1 | none |
| CONFIG fallback write | true | 857 | 0 | false | 2 | none |
| CONFIG fallback read | true | 383 | 0 | false | 69 | none |

## Restore

- Ops active: true
- Probe nodes removed: true
- Admin active: true
- Sales-Manager-v2 active: false

## Telegram during preflight

**0**
