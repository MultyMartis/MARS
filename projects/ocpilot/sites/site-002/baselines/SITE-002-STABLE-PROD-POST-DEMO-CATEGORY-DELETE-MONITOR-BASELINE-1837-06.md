# BASELINE — SITE-002 Stable Prod Post-Demo-Category-Delete Monitor Baseline 1837 06

**Checkpoint ID:** `SITE-002-STABLE-PROD-POST-DEMO-CATEGORY-DELETE-MONITOR-BASELINE-1837-06`  
**Issued:** 2026-07-27  
**Operation:** `SITE-002-MONITOR-BASELINE-REFRESH-06`  
**OCPilot run:** 4.304  
**Environment:** https://bzpm.ru/ (Production sitemap observed; **local monitor hygiene only**)

## Scope and wording

Local post-1C monitor sitemap baseline refresh after approved demo category delete apply (Run 4.303 — categories **154–170** removed). This checkpoint records that the monitor's comparison baseline was updated from **1854** to **1837** URLs.

This does **not** claim a new broad production content stability checkpoint. Parent **153** remains pending review. Ambiguous empty categories outside 153 remain a separate charter.

## Verified

| Area | Status |
|------|--------|
| Demo delete apply (4.303) | **CONFIRMED** (reconfirmed this op) |
| Live sitemap | **PASS** — 1837 URLs; valid XML |
| Baseline refresh | **UPDATED** — storage artifact + monitor expected-count constants |
| Production mutation | **0** |
| Scheduler mutation | **0** |
| Dirty main | **untouched** |
| Client Ops | **untouched** |

## Production mutation

**None** — monitor baseline/docs/runtime sync only.

## Reports

- [SITE-002-MONITOR-BASELINE-REFRESH-06.md](../reports/SITE-002-MONITOR-BASELINE-REFRESH-06.md)
- [SITE-002-PROD-DEMO-CATEGORY-DELETE-APPLY-01.md](../reports/SITE-002-PROD-DEMO-CATEGORY-DELETE-APPLY-01.md)

## Storage

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-MONITOR-BASELINE-REFRESH-06\`
