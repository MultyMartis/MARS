# SITE-002-STABLE-PROD-CRON-BEGET-ACTIVE-01

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-06  
**Operation:** `SITE-002-PROD-CRON-BEGET-ACTIVE-CONFIRM-01` (OCPilot Run 4.183)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-CRON-MANUAL-RUN-01`

---

## Summary

Beget daily cron row for MARS 1C import wrapper **confirmed active** by operator panel evidence. Sergey legacy import flow **preserved**. No import executed in confirmation operation.

| Field | Value |
|-------|-------|
| Beget cron active | **Yes** — operator-created row |
| Cron row name | `SITE-002 MARS 1C Import Wrapper` |
| Schedule | `0 8 * * *` |
| Server time | **08:00 Europe/Moscow** |
| Business time | **12:00 Barnaul** |
| Channel | HTTP gateway |
| Command target | `mars_1c_http_gateway.php` |
| Token | **Present** — not recorded in repo |
| Manual import in this operation | **No** |
| Legacy Sergey import | **Preserved** |
| Token rotation | **Not performed** (operator decision) |

---

## Wrapper state (confirmation recheck)

| Check | Result |
|-------|--------|
| Wrapper version | **1.1.0** |
| dry-run HTTP 200 / mutation false | **PASS** |
| status HTTP 200 / mutation false | **PASS** |
| run without token HTTP 403 | **PASS** |
| `run_token_configured` | **true** |
| Lock held | **No** |
| Latest manual run report | `mars_1c_import_2026-07-05_205934.txt` |

---

## Beget cron row (sanitized)

| Field | Value |
|-------|-------|
| Name | SITE-002 MARS 1C Import Wrapper |
| Schedule | `0 8 * * *` |
| Query | `mode=run` · `token=<TOKEN_PRESENT>` |
| Stdout log | `/storage/mars-tools/cron/logs/beget_cron_stdout.log` |
| Active | **enabled** |

---

## Proven operational boundary

```text
MARS Beget daily 1C cron active — HTTP gateway — Sergey legacy preserved — next scheduled run monitoring pending
```

Does **not** prove: first scheduled cron run SUCCESS, live DB cron table state, or automated monitoring.

---

## Next natural verification

After next **08:00 Moscow / 12:00 Barnaul** scheduled run:

1. New TXT report under `/storage/mars-tools/cron/reports/mars_1c_import_YYYY-MM-DD_HHMMSS.txt`
2. Final status SUCCESS / PARTIAL / FAILED
3. Step statuses: `1c`, `1c_offers`
4. Lock removed
5. `beget_cron_stdout.log` append evidence
6. Site HTTP: https://bzpm.ru/ · https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly

If FAIL/PARTIAL: disable Beget row manually; preserve report/log.

---

## References

- [../reports/SITE-002-PROD-CRON-BEGET-ACTIVE-CONFIRM-01.md](../reports/SITE-002-PROD-CRON-BEGET-ACTIVE-CONFIRM-01.md)
- [../reports/SITE-002-PROD-CRON-BEGET-ACTIVATE-01.md](../reports/SITE-002-PROD-CRON-BEGET-ACTIVATE-01.md)
- [../reports/SITE-002-PROD-CRON-MANUAL-RUN-01.md](../reports/SITE-002-PROD-CRON-MANUAL-RUN-01.md)
- [SITE-002-STABLE-PROD-CRON-MANUAL-RUN-01.md](SITE-002-STABLE-PROD-CRON-MANUAL-RUN-01.md)
- Storage: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-BEGET-ACTIVE-CONFIRM-01\`
- Storage checkpoint: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-CRON-BEGET-ACTIVE-01\`
