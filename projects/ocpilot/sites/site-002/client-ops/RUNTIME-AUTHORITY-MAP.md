# SITE-002 — Runtime Authority Map

Classification vocabulary (exact):

- `AUTHORITATIVE_PRODUCTION`
- `SUPPORTING_PRODUCTION`
- `OPTIONAL_HYGIENE`
- `RETIRED`
- `HISTORICAL_EVIDENCE`
- `LOCAL_TEST_ONLY`

| Component | Classification | Notes |
|-----------|----------------|-------|
| Beget import cron | AUTHORITATIVE_PRODUCTION | Scheduled import entry |
| Beget watchdog cron | AUTHORITATIVE_PRODUCTION | Operator-created; `0 9 * * *` Europe/Moscow historically |
| OpenCart / ocStore importer | AUTHORITATIVE_PRODUCTION | Catalog/offers processing |
| Canonical import runner + wrapper | AUTHORITATIVE_PRODUCTION | Shared scheduled + admin |
| Terminal run state | AUTHORITATIVE_PRODUCTION | Run truth |
| `mars_1c_completion_dispatch.php` | AUTHORITATIVE_PRODUCTION | Outbound when enabled |
| `mars_1c_no_import_watchdog.php` + HTTP gateway | AUTHORITATIVE_PRODUCTION | No-import path |
| n8n workflow `tkM4H0G0gM3q9Foi` | AUTHORITATIVE_PRODUCTION | Delivery orchestration |
| n8n Data Table `H6VYhwz7RXZCBMmu` | AUTHORITATIVE_PRODUCTION | Current dedupe/state |
| Telegram bot «Монитор bzpm.ru — MetaCODE» | AUTHORITATIVE_PRODUCTION | Operator channel |
| Admin manual trigger | AUTHORITATIVE_PRODUCTION | Same runner |
| `CLIENT_OPS_DISPATCH_ENABLED` kill switch | SUPPORTING_PRODUCTION | Blocks outbound only |
| OpenCart admin dispatch status UI | SUPPORTING_PRODUCTION | Read-only visibility |
| Windows completion poller task | RETIRED | Disabled; not authority |
| Old local Client Ops producer task | RETIRED | Disabled; not authority |
| Post_1C Catalog Monitor task | OPTIONAL_HYGIENE | Hidden/noninteractive; keep for now |
| Local STORAGE harnesses / PS1 wrappers | LOCAL_TEST_ONLY / RETIRED (see inventory) | Cleanup later |
| Historical Scheduled Tasks (disabled) | RETIRED | Manifest candidates |
| D6G* evidence / reports | HISTORICAL_EVIDENCE | Proof, not live mutation surface |
| Google Sheets | HISTORICAL_EVIDENCE / NOT AUTHORITY | Not current BZPM memory |

## Workstation independence

Normal production reporting **does not** require the operator workstation.

## Post_1C monitor

See `workstation-cleanup/POST-1C-MONITOR-DECISION.md` — **OPTIONAL_HYGIENE**, not DELETE in this phase.
