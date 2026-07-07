# SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01

**Site:** SITE-002 (ЗПМ / bzpm.ru)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-07  
**Operation:** `SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01` (OCPilot Run 4.215)  
**Type:** Read-only automation-readiness baseline — **not** a Production mutation checkpoint  
**Parent checkpoint:** `SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01`  
**Prior audit baseline:** `SITE-002-POST-1C-CATALOG-MONITOR-02`

---

## Summary

Local Windows Task Scheduler package prepared for daily read-only post-1C catalog monitor. **Task not installed** during this operation unless operator runs install script separately.

| Field | Value |
|-------|-------|
| 1C import automatic | **yes** (Beget cron 08:00 Moscow) |
| Sitemap automatic | **yes** (OpenCart feed, Run 4.214) |
| MARS monitor automatic before | **no** |
| MARS monitor automatic after (without enable) | **no** |
| Runner script | `site-002-post-1c-monitor-runner.ps1` |
| Recommended schedule | 12:30 Barnaul / 08:30 Moscow |
| Windows task installed | **no** |
| Production mutations | **0** |

Report: [SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01.md](../reports/SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01.md)  
Runbook: [SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md](../runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md)
