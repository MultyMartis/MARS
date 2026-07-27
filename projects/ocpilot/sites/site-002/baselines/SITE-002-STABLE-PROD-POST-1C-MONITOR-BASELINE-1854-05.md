# BASELINE — SITE-002 Stable Prod Post-1C Monitor Baseline 1854 05

**Checkpoint ID:** `SITE-002-STABLE-PROD-POST-1C-MONITOR-BASELINE-1854-05`  
**Issued:** 2026-07-27  
**Operation:** `SITE-002-MONITOR-BASELINE-REFRESH-05`  
**OCPilot run:** 4.300  
**Environment:** https://bzpm.ru/ (Production sitemap observed; **local monitor hygiene only**)

## Scope and wording

Local post-1C monitor sitemap baseline refresh after confirmed 1C post-import persistence (Runs 4.297–4.299). This checkpoint records that the monitor's comparison baseline was updated from **1737** to **1854** URLs.

This does **not** claim a new broad production content stability checkpoint. Parent production checkpoint remains `SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01` unless a separate production charter supersedes it. Legacy cleanup remains a separate charter.

## Verified

| Area | Status |
|------|--------|
| Post-import persistence | **CONFIRMED** (reconfirmed this op) |
| Live sitemap | **PASS** — 1854 URLs; valid XML |
| Baseline refresh | **UPDATED** — storage artifact + monitor expected-count constants |
| Production mutation | **0** |
| Scheduler mutation | **0** |
| Dirty main | **untouched** |
| Client Ops | **untouched** |

## Production mutation

**None** — monitor baseline/docs/runtime sync only.

## Reports

- [SITE-002-MONITOR-BASELINE-REFRESH-05.md](../reports/SITE-002-MONITOR-BASELINE-REFRESH-05.md)
- [SITE-002-PROD-1C-POST-IMPORT-PERSISTENCE-CHECK-01.md](../reports/SITE-002-PROD-1C-POST-IMPORT-PERSISTENCE-CHECK-01.md)

## Storage

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-MONITOR-BASELINE-REFRESH-05\`
