# SITE-002-STABLE-PROD-CRON-WRAPPER-01

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-06  
**Operation:** `SITE-002-PROD-CRON-WRAPPER-01` (OCPilot Run 4.178)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-SORT-MENU-ORDER-01`

---

## Summary

Parallel MARS 1C cron wrapper files uploaded to Production under isolated `mars-tools` namespace. Sergey legacy import flow **preserved** — no edits to `cronjob.php`, `import_1C*.php`, or existing cron route.

| Field | Value |
|-------|-------|
| Real import executed | **No** |
| DB mutated | **No** |
| Beget cron activated | **No** |
| Cron activation | **Pending operator approval** |

---

## Remote files (MARS only)

| FTP path | Role |
|----------|------|
| `/storage/mars-tools/cron/mars_1c_import_wrapper.php` | CLI wrapper (primary) |
| `/public_html/mars-tools/cron/mars_1c_http_gateway.php` | HTTP gateway (dry-run/status/gated run) |
| `/storage/mars-tools/index.html` | Directory listing guard |
| `/storage/mars-tools/cron/index.html` | Directory listing guard |
| `/public_html/mars-tools/index.html` | Directory listing guard |
| `/public_html/mars-tools/cron/index.html` | Directory listing guard |

**Hosting CLI path (from dry-run):** `/home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_import_wrapper.php`

---

## Verification (2026-07-06)

| Check | Result |
|-------|--------|
| HTTP dry-run | **PASS** — 200, `mutation: false` |
| HTTP status | **PASS** — 200 |
| HTTP run without token | **PASS** — 403, no mutation |
| Legacy Sergey files modified | **0** |

---

## Proven operational boundary

```text
parallel MARS-only wrapper upload under mars-tools — no legacy import mutation
```

Does **not** prove: Beget cron activation, real 1C import, DB cron table changes, or Sergey flow replacement.

---

## Rollback

Delete MARS files listed above. Do not touch Sergey legacy import files.

---

## References

- [../reports/SITE-002-PROD-CRON-WRAPPER-01.md](../reports/SITE-002-PROD-CRON-WRAPPER-01.md)
- Storage: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-WRAPPER-01\`
- Storage baseline copy: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-CRON-WRAPPER-01\`
