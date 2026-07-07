# REPORT — SITE-002 Post-1C Monitor Scheduler Readiness

**OCPilot run:** 4.215  
**Operation ID:** SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01  
**Date:** 2026-07-07  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Parent checkpoint:** SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01  
**Audit baseline before:** SITE-002-POST-1C-CATALOG-MONITOR-02  
**Mode:** Scheduler readiness — local automation prep — **no Production mutation**

---

## 1. Scope

Prepare safe local automation for daily read-only post-1C catalog onboarding monitor:

1. Document current automation state (1C import, sitemap, MARS monitor).
2. Compare scheduler options; recommend local Windows Task Scheduler first.
3. Create reusable local runner + install/uninstall scripts (not silently executed).
4. Dry-run validation; operator runbook; OCPilot doc updates.

**Forbidden:** Production/server mutation, silent OS task registration, FTP, admin, DB, cache, sitemap edit, import trigger.

---

## 2. Operator question

> «Автоматически будет запускаться?» (post-1C MARS monitor after daily 1C import)

---

## 3. Direct answer

| Question | Answer |
|----------|--------|
| Sitemap automatic? | **YES** — OpenCart Google Sitemap feed (Run 4.214) |
| 1C import automatic? | **YES** — Beget cron daily **08:00 Moscow** / **12:00 Barnaul** |
| MARS post-1C monitor automatic **right now**? | **NO** — manual prompt-driven (Runs 4.212, 4.213) |
| After this task? | **Scheduler package ready**; automatic execution only after operator **installs and enables** Windows Task |
| Server-side automation? | **Separate future operation** — not in scope |

---

## 4. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` — **PASS** |
| Volume X label | `AI WS` — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD (start) | `f451ae3ea65abd4c959ae8f4a8985d4820199cc8` |
| Staged files before task | **empty** — **PASS** |
| Foreign WIP | FP-0002 / forge-wordpress / `.recovery-temp` — **not staged, not touched** |

---

## 5. Current automation state

| Layer | Automatic | Authority |
|-------|-----------|-----------|
| 1C catalog import | **YES** | Beget server cron `0 8 * * *` Moscow |
| Sitemap XML | **YES** | `extension/feed/google_sitemap`; live per request; no physical file |
| MARS post-1C monitor | **NO** | Local Python tool; prior runs manual |

Storage: `deployments/.../design/current-automation-state.md`

---

## 6. Scheduler options

| Option | Summary | Selected for readiness |
|--------|---------|------------------------|
| **A** Local Windows Task | No server mutation; logs under Storage; disabled-by-default install | **YES — recommended** |
| **B** Production server cron | Near import; requires deployment + cron edit | Documented; deferred |
| **C** Manual prompt only | Safest; not automatic | Status quo until enable |

Storage: `deployments/.../design/scheduler-options.md`

---

## 7. Selected readiness path

**Option A** — local Windows Task Scheduler on operator workstation (UTC+7 detected).

- Recommended daily time: **12:30 Barnaul** / **08:30 Moscow** (30 min after import)
- Task name: `MARS_SITE_002_Post_1C_Catalog_Monitor`
- Install creates task **disabled** unless `-Enable -ConfirmEnable`

---

## 8. Runner script

**Path:** `projects/ocpilot/sites/site-002/tools/site-002-post-1c-monitor-runner.ps1`

| Feature | Detail |
|---------|--------|
| Invokes | `site-002-prod-post-1c-catalog-onboarding-monitor-02.py` (`--skip-removed-crawl`) |
| Python detection | `.venv`, `py`, `python` |
| Logs | `X:\AI MARS STORAGE\...\scheduled-monitors\post-1c\YYYY-MM-DD_HH-mm-ss\` |
| Outputs | `run.log`, `run-summary.json`, `run-summary.md` |
| `-DryRun` | Environment check + public sitemap probe only |
| Credentials | None printed or stored |

---

## 9. Windows Task Scheduler install/uninstall scripts

| Script | Purpose |
|--------|---------|
| `install-site-002-post-1c-monitor-task.ps1` | Register task; **disabled** by default; `-Enable -ConfirmEnable` for enabled install |
| `uninstall-site-002-post-1c-monitor-task.ps1` | Unregister exact task name only |

**This operation:** scripts created; **not executed** for registration.

Preview: `deployments/.../scheduler/task-install-preview.md`

---

## 10. Runbook

**Path:** `projects/ocpilot/sites/site-002/runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md`

Covers: manual run, install (disabled), enable, disable, uninstall, log locations, onboarding follow-up policy, forbidden actions.

---

## 11. Dry-run validation

| Check | Result |
|-------|--------|
| Runner `-DryRun` | **PASS** exit 0 |
| Python | `py` 3.14.6 |
| Sitemap probe | HTTP 200, **1377** URLs |
| Full monitor in dry-run | **not run** |
| Task installed | **no** |

Artifacts: `deployments/.../dry-run/runner-dry-run.md`

Example run folder: `scheduled-monitors/post-1c/2026-07-07_19-39-02/`

---

## 12. Production mutation summary

| Category | Count |
|----------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| Remote renames | 0 |
| Admin saves | 0 |
| DB direct operations | 0 |
| Product PDP changes | 0 |
| Product generator changes | 0 |
| Category meta changes | 0 |
| Category structure changes | 0 |
| Category status changes | 0 |
| Category URL/slug changes | 0 |
| llms.txt changes | 0 |
| Header/footer changes | 0 |
| Yandex.Metrika/Webmaster changes | 0 |
| Robots changes | 0 |
| Sitemap changes | 0 |
| Cron/import runs | 0 |
| Mail changes | 0 |
| Cache clears | 0 |
| Manual sitemap edits | 0 |
| Windows scheduled task installed | **no** |
| Windows scheduled task enabled | **no** |

---

## 13. Storage artefacts

**Deployment root:**

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01\`

| Area | Contents |
|------|----------|
| `design/` | current-automation-state, scheduler-options |
| `manifests/` | operation.json |
| `dry-run/` | runner-dry-run evidence |
| `scheduler/` | task-install-preview |
| `scheduled-monitors/post-1c/` | dry-run run log (not in git) |

---

## 14. Authority updates

| Document | Update |
|----------|--------|
| OPERATIONAL-INDEX.md | Run 4.215 entry |
| OCPILOT-STATE.md | Scheduler readiness state |
| production-profile.md | Monitor automation readiness |
| site-passport.md | Automation status row |
| SITE-002-TECHNICAL-KNOWLEDGE-MAP.md | Scheduled monitor section |
| tools/README.md | Runner + install scripts |
| runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md | **created** |
| baselines/SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01.md | **created** |

---

## 15. Git status

Selective stage of operation-scoped repository paths only. Storage logs and foreign WIP excluded.

---

## 16. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Workstation uptime at 12:30 daily | Operator responsibility — monitor skips if PC off |
| `Register-ScheduledTask` permissions | May need interactive user; documented in runbook — not tested (task not installed) |
| Full monitor runtime on schedule | **UNKNOWN** duration at scale when delta large; 2h task limit set |
| Server cron monitor path | **Not evaluated** — separate operation |
| Python 3.14 compatibility | Dry-run OK; full scheduled run not executed this operation |

---

## 17. Final verdict

**SITE-002 POST-1C MONITOR SCHEDULER READINESS COMPLETE — LOCAL TASK PACKAGE READY**

---

## 18. Next task recommendation

1. Operator: run `install-site-002-post-1c-monitor-task.ps1` (disabled), review schedule, then `Enable-ScheduledTask`.
2. After first scheduled run: review `scheduled-monitors/post-1c/` latest folder.
3. If onboarding tasks found: charter `SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-03` or hygiene review — **no auto-mutation**.
4. Optional future: `SITE-002-POST-1C-MONITOR-SERVER-CRON-01` — only with explicit server deployment charter.

---

**Brand policy:** ЗПМ correct · БЗПМ forbidden in public content · domain bzpm.ru
