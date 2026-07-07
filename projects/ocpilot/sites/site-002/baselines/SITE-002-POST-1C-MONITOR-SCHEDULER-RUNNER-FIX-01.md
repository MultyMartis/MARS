# SITE-002-POST-1C-MONITOR-SCHEDULER-RUNNER-FIX-01

**Site:** SITE-002 (ЗПМ / bzpm.ru)  
**Environment:** LOCAL_SCHEDULER — workstation Windows Task Scheduler  
**Issued:** 2026-07-07  
**Operation:** `SITE-002-POST-1C-MONITOR-SCHEDULER-RUNNER-FIX-01` (OCPilot Run 4.216)  
**Type:** Local automation fix baseline — **not** a Production mutation checkpoint  
**Parent checkpoint:** `SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01`  
**Prior audit baseline:** `SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01`

---

## Summary

Fixed PowerShell runner quoting so Windows Task `MARS_SITE_002_Post_1C_Catalog_Monitor` passes monitor script path `X:\AI MARS\...` as a single argument. Operator manual task run had failed with LastTaskResult **2**.

| Field | Value |
|-------|-------|
| Root cause | `Start-Process -ArgumentList` + `py` launcher split path at space |
| Runner fixed | **yes** — call-operator `& $py.Path $MonitorScript @monitorArgs` |
| Dry-run | **PASS** |
| Direct runner | **PASS** (exit 0) |
| Scheduled task LastTaskResult after | **0** |
| Task enabled after | **yes** |
| NextRunTime | 2026-07-08 12:30:30 (Barnaul) |
| Production mutations | **0** |

Report: [SITE-002-POST-1C-MONITOR-SCHEDULER-RUNNER-FIX-01.md](../reports/SITE-002-POST-1C-MONITOR-SCHEDULER-RUNNER-FIX-01.md)  
Runbook: [SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md](../runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md)
