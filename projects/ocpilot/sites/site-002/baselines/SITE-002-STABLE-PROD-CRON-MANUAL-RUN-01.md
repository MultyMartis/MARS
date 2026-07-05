# SITE-002-STABLE-PROD-CRON-MANUAL-RUN-01

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-06  
**Operation:** `SITE-002-PROD-CRON-MANUAL-RUN-01` (OCPilot Run 4.181)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-01`

---

## Summary

First controlled manual 1C import executed through MARS wrapper on Production. Sergey legacy import flow **preserved** — wrapper orchestrates `cron.active` and invokes existing `common/cronjob` route.

| Field | Value |
|-------|-------|
| Manual import executed | **Yes** — once, **SUCCESS** |
| Run ID | `mars-20260705-205929-df82e686` |
| Channel | HTTP gateway (CLI PHP incompatible on SSH) |
| Catalog step | **PASS** |
| Offers step | **PASS** |
| Beget cron activated | **No** |
| Cron activation | **Ready** — pending operator approval |

---

## Remote files (MARS only — unchanged)

| FTP path | Role |
|----------|------|
| `/storage/mars-tools/cron/mars_1c_import_wrapper.php` | CLI wrapper v1.1.0 |
| `/storage/mars-tools/cron/mars_1c_wrapper.local.php` | Local token config (Storage secrets — not in Git) |
| `/storage/mars-tools/cron/reports/` | Human-readable TXT reports |
| `/public_html/mars-tools/cron/mars_1c_http_gateway.php` | HTTP gateway |

**Latest run report:** `mars_1c_import_2026-07-05_205934.txt`  
**Technical log:** `mars_1c_import_20260705.log`

---

## Verification (2026-07-06)

| Check | Result |
|-------|--------|
| Wrapper dry-run/status before run | **PASS** |
| Run without token blocked | **PASS** |
| Exactly one wrapper run | **PASS** |
| TXT run report | **PASS** — no secrets |
| Lock removed after run | **PASS** |
| Site HTTP 200 (home + catalog) | **PASS** |
| Legacy Sergey files modified | **0** |

---

## Proven operational boundary

```text
MARS wrapper manual 1C import on Production — SUCCESS — Sergey legacy preserved — Beget cron not activated
```

Does **not** prove: Beget cron activation, automated daily schedule, or live DB SELECT via SSH.

---

## Beget cron recommendation (not activated)

| Field | Value |
|-------|-------|
| Schedule (Moscow) | `0 8 * * *` |
| HTTP command (proved) | `wget -q -O - "https://bzpm.ru/mars-tools/cron/mars_1c_http_gateway.php?mode=run&token=<TOKEN>" >> .../beget_cron_stdout.log 2>&1` |
| Activation gate | Operator reviews Run 4.181 report |

---

## References

- [../reports/SITE-002-PROD-CRON-MANUAL-RUN-01.md](../reports/SITE-002-PROD-CRON-MANUAL-RUN-01.md)
- [../reports/SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01.md](../reports/SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01.md)
- [../reports/SITE-002-PROD-CRON-RUN-REPORTS-01.md](../reports/SITE-002-PROD-CRON-RUN-REPORTS-01.md)
- Storage: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-MANUAL-RUN-01\`
