# BASELINE — SITE-002 Stable Prod Post-Parent-153-Delete Monitor Baseline 1836 07

**Checkpoint ID:** `SITE-002-STABLE-PROD-POST-PARENT-153-DELETE-MONITOR-BASELINE-1836-07`  
**Issued:** 2026-07-27  
**Operation:** `SITE-002-MONITOR-BASELINE-REFRESH-07`  
**OCPilot run:** 4.307  
**Environment:** https://bzpm.ru/ (Production sitemap observed; **local monitor hygiene only**)

## Scope and wording

Local post-1C monitor sitemap baseline refresh after approved parent **153** delete apply (Run 4.306). This checkpoint records that the monitor's comparison baseline was updated from **1837** to **1836** URLs.

This does **not** claim a new broad production content stability checkpoint. Ambiguous empty categories remain a separate charter. Categories **154–170** remain deleted from prior Run 4.303.

## Verified

| Area | Status |
|------|--------|
| Parent 153 delete apply (4.306) | **CONFIRMED** (reconfirmed this op) |
| Demo delete 154–170 (4.303) | **REMAIN ABSENT** |
| Live sitemap | **PASS** — 1836 URLs; valid XML |
| Baseline refresh | **UPDATED** — storage artifact + monitor expected-count constants |
| Production mutation | **0** |
| Scheduler mutation | **0** |
| Dirty main | **untouched** |
| Client Ops | **untouched** |

## Production mutation

**None** — monitor baseline/docs/runtime sync only.

## Reports

- [SITE-002-MONITOR-BASELINE-REFRESH-07.md](../reports/SITE-002-MONITOR-BASELINE-REFRESH-07.md)
- [SITE-002-PROD-PARENT-153-DELETE-APPLY-01.md](../reports/SITE-002-PROD-PARENT-153-DELETE-APPLY-01.md)

## Storage

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-MONITOR-BASELINE-REFRESH-07\`
