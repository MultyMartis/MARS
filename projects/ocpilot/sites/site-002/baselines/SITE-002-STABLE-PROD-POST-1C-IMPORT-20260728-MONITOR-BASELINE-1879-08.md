# BASELINE — SITE-002 Stable Prod Post-1C-Import-20260728 Monitor Baseline 1879 08

**Checkpoint ID:** `SITE-002-STABLE-PROD-POST-1C-IMPORT-20260728-MONITOR-BASELINE-1879-08`  
**Issued:** 2026-07-28  
**Operation:** `SITE-002-MONITOR-BASELINE-REFRESH-08`  
**OCPilot run:** 4.312  
**Environment:** https://bzpm.ru/ (Production sitemap observed; **local monitor hygiene only**)

## Scope and wording

Local post-1C monitor sitemap baseline refresh after successful natural 1C import 2026-07-28 (`mars_1c_import_2026-07-28_080011.txt`, id `mars-20260728-080001-24823ddf`). This checkpoint records that the monitor's comparison baseline was updated from **1836** to **1879** URLs.

This does **not** claim a new broad production content stability checkpoint. UI first-level category block apply was **not** performed. Categories **153** and **154–170** remain deleted from prior cleanup runs.

## Verified

| Area | Status |
|------|--------|
| Latest 1C import 2026-07-28 | **CONFIRMED SUCCESS** (reconfirmed this op) |
| Critical products canonical | **5/5** |
| Parent 153 + demo 154–170 | **REMAIN ABSENT** |
| Live sitemap | **PASS** — 1879 URLs; valid XML |
| Baseline refresh | **UPDATED** — storage artifact + monitor expected-count constants |
| Production mutation | **0** |
| Scheduler mutation | **0** |
| Dirty main | **untouched** |
| Client Ops | **untouched** |

## Production mutation

**None** — monitor baseline/docs/runtime sync only.

## Reports

- [SITE-002-MONITOR-BASELINE-REFRESH-08.md](../reports/SITE-002-MONITOR-BASELINE-REFRESH-08.md)
- [SITE-002-PROD-POST-1C-NEUTRAL-FIRST-LEVEL-BLOCK-CHARTER-01.md](../reports/SITE-002-PROD-POST-1C-NEUTRAL-FIRST-LEVEL-BLOCK-CHARTER-01.md)

## Storage

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-MONITOR-BASELINE-REFRESH-08\`
