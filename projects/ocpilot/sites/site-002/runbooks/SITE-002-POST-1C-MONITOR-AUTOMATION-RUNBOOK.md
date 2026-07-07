# SITE-002 Post-1C Monitor Automation Runbook

**Site:** SITE-002 (ЗПМ / https://bzpm.ru/)  
**Operation family:** read-only post-1C catalog onboarding monitor  
**Last updated:** 2026-07-07 (Run 4.216)

---

## Direct answer: is the monitor automatic?

| Component | Automatic? |
|-----------|------------|
| 1C import (Beget cron) | **YES** — daily 08:00 Moscow / 12:00 Barnaul |
| Sitemap (`/sitemap.xml`) | **YES** — OpenCart Google Sitemap feed (Run 4.214) |
| MARS post-1C monitor | **YES** (local) — after operator install + enable; verified Run 4.216 |

After scheduler readiness (Run 4.215) and runner fix (Run 4.216): operator-installed task verified; **LastTaskResult 0** on success; **LastTaskResult 2** indicates execution failure (e.g. path quoting before fix).

---

## What the monitor does (read-only)

1. Fetches live `https://bzpm.ru/sitemap.xml`
2. Compares against prior monitor baseline URL set
3. Classifies added/removed URLs (category PLP, hub, PDP, hygiene)
4. Reports category onboarding needs, PDP sanity, brand/test markers
5. **Does not** mutate Production (no FTP, admin, DB, cache, sitemap edit)

Monitor Python tool: `projects/ocpilot/sites/site-002/tools/site-002-prod-post-1c-catalog-onboarding-monitor-02.py`

---

## Manual run (one-off)

```powershell
cd "X:\AI MARS\projects\ocpilot\sites\site-002\tools"
powershell -NoProfile -ExecutionPolicy Bypass -File ".\site-002-post-1c-monitor-runner.ps1"
```

Dry-run (environment check + sitemap probe only):

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ".\site-002-post-1c-monitor-runner.ps1" -DryRun
```

---

## Install scheduled task (disabled by default)

```powershell
cd "X:\AI MARS\projects\ocpilot\sites\site-002\tools"
.\install-site-002-post-1c-monitor-task.ps1
```

Creates task `MARS_SITE_002_Post_1C_Catalog_Monitor` — **disabled** until you enable it.

Custom local time (example 13:00):

```powershell
.\install-site-002-post-1c-monitor-task.ps1 -At "13:00"
```

---

## Enable task

After reviewing install output and schedule:

```powershell
Enable-ScheduledTask -TaskName 'MARS_SITE_002_Post_1C_Catalog_Monitor'
```

Or install already enabled (explicit confirmation required):

```powershell
.\install-site-002-post-1c-monitor-task.ps1 -Enable -ConfirmEnable -Force
```

---

## Disable task (keep registered)

```powershell
Disable-ScheduledTask -TaskName 'MARS_SITE_002_Post_1C_Catalog_Monitor'
```

---

## Uninstall task

```powershell
cd "X:\AI MARS\projects\ocpilot\sites\site-002\tools"
.\uninstall-site-002-post-1c-monitor-task.ps1
```

Removes **only** task `MARS_SITE_002_Post_1C_Catalog_Monitor` — no wildcard deletion.

---

## Recommended schedule

| Zone | Time | Notes |
|------|------|-------|
| Moscow (UTC+3) | **08:30** | ~30 min after 1C import 08:00 |
| Barnaul (UTC+7) | **12:30** | Default in install script; matches typical operator workstation TZ |

Adjust with `-At "HH:mm"` on install if needed.

---

## Where logs are stored

**Per scheduled/local run:**

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c\YYYY-MM-DD_HH-mm-ss\`

Files: `run.log`, `run-summary.json`, `run-summary.md`, optional `run.stderr.log`

**Path with spaces:** runner uses PowerShell call-operator (`& $py.Path $MonitorScript ...`) so `X:\AI MARS\...` paths are passed as a single argument. If `LastTaskResult` is **2**, check `run.stderr.log` for `can't open file 'X:\\AI'` (historical quoting bug, fixed Run 4.216).

**Full monitor artefacts** (Python deployment output):

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-02\`

---

## If monitor finds onboarding tasks

1. Read `run-summary.md` in the latest scheduled run folder
2. Open full monitor report under deployments (delta, category-onboarding-needs, followup)
3. **Do not** auto-delete, hide, noindex, or hand-edit sitemap.xml
4. Charter a separate human-approved operation (e.g. category admin SEO onboarding)
5. Re-run monitor after onboarding or next 1C import

---

## Forbidden actions (monitor context)

- Delete/hide/noindex new 1C categories or products by default
- Manual edit of `sitemap.xml` on server
- Production FTP upload, admin save, DB write, cache clear
- Triggering 1C import from monitor runner
- Editing robots.txt, llms.txt, header/footer, Yandex blocks from monitor flow

---

## Server cron alternative

Running the monitor on Production server cron is **possible later** but requires a **separate operation** with server deployment approval. Not covered by this runbook.

---

## Related documents

- [SITE-002-POST-1C-MONITOR-SCHEDULER-RUNNER-FIX-01.md](../reports/SITE-002-POST-1C-MONITOR-SCHEDULER-RUNNER-FIX-01.md)
- [SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01.md](../reports/SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01.md)
- [SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-02.md](../reports/SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-02.md)
- [SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01.md](../reports/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01.md)
- [tools/README.md](../tools/README.md)
