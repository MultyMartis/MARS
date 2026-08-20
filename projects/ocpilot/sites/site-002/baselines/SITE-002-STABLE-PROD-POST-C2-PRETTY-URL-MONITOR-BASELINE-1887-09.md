# BASELINE — SITE-002 Stable Prod Post-C2 Pretty-URL Monitor Baseline 1887 09

**Checkpoint ID:** `SITE-002-STABLE-PROD-POST-C2-PRETTY-URL-MONITOR-BASELINE-1887-09`  
**Issued:** 2026-08-20  
**Operation:** `SITE-002-MONITOR-BASELINE-REFRESH-09`  
**OCPilot run:** 4.335  
**Environment:** https://bzpm.ru/ (Production sitemap observed; **local monitor hygiene only**)

## Scope and wording

Local post-1C monitor sitemap baseline refresh after Wave A/B1 onboarding, Wave C2 monitor fix, runtime checkout sync, and scheduled validation `2026-08-20_13-29-44` (commit `9865413c`). This checkpoint records that the monitor's comparison baseline was updated from **1879** (mostly `/katalog/...`) to **1887** pretty-URL sitemap URLs.

This does **not** claim a new broad production content stability checkpoint. Production DB/FTP/import/category/product/mapping were **not** mutated in this operation.

## Verified

| Area | Status |
|------|--------|
| Live sitemap | **PASS** — 1887 unique URLs; HTTP 200; valid XML; `/katalog/` **0** |
| Previous baseline | **PRESERVED** — frozen `sitemap-current-urls-1879-pre-refresh-09.json` |
| Baseline refresh | **UPDATED** — MONITOR-01 `sitemap-current-urls.json` + monitor expected-count constants |
| Post-refresh monitor | **NO_ACTION_REQUIRED** — 1887→1887; exact/semantic **0/0** |
| `/upakovochnoe-oborudovanie` | **ABSENT** — accepted 404; not in this baseline |
| Production mutation | **0** |
| Scheduler mutation | **0** |
| Dirty main | **untouched** |
| Client Ops | **untouched** |

## Production mutation

**None** — monitor baseline/docs/runtime script-constant sync only.

## Reports

- [SITE-002-MONITOR-BASELINE-REFRESH-09.md](../reports/SITE-002-MONITOR-BASELINE-REFRESH-09.md)
- Parent 1879 checkpoint: [SITE-002-STABLE-PROD-POST-1C-IMPORT-20260728-MONITOR-BASELINE-1879-08.md](SITE-002-STABLE-PROD-POST-1C-IMPORT-20260728-MONITOR-BASELINE-1879-08.md)

## Storage

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-MONITOR-BASELINE-REFRESH-09\`
