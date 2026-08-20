# REPORT — SITE-002 Monitor Baseline Metadata Fix 01

**Operation:** `SITE-002-MONITOR-BASELINE-METADATA-FIX-01`  
**OCPilot run:** **4.337**  
**Date:** 2026-08-20  
**Environment:** MONITOR_BASELINE_METADATA_FIX  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`  
**Dirty main:** `X:\AI MARS` (not touched)  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-MONITOR-BASELINE-METADATA-FIX-01\`

**Final verdict:** `SITE-002 MONITOR BASELINE METADATA FIX COMPLETE — STALE SUMMARY 1377 CORRECTED TO ACTIVE BASELINE 1887`

**Classifications:**

- `SITE_002_BASELINE_METADATA_FIX_COMPLETE`
- `ACTIVE_BASELINE_1887_CONFIRMED`
- `BASELINE_URL_LIST_UNCHANGED`
- `PRODUCTION_MUTATION_ZERO`

---

## 1. Scope

Cosmetic metadata-only alignment of MONITOR-01 `sitemap-current-summary.json` (stale **1377**) to the accepted active baseline **1887** after Refresh 09 and workspace closeout. Docs/report only in authority git; Storage metadata companion file update.

Not in scope: production DB/FTP, 1C import, categories/products/mapping/importer, monitor code logic, baseline URL list replacement/refresh, runtime checkout mutation, Client Ops/n8n/Telegram, docs-01/docs-02, dirty main, deletes.

## 2. Operator approval

Operator: `давай` — approved the small cosmetic metadata tail after closeout noted stale summary vs urls **1887**.

## 3. Client Ops boundary

- **Not touched:** Client Ops Telegram Reports, reporting bridge, n8n, Telegram bot, Hub Gateway, reporting envelope.
- SITE-002 Storage monitor baseline metadata + OCPilot docs/report only.
- Dirty main Client Ops / foreign WIP left untouched.

## 4. Authority preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority path | `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo` |
| Branch | `docs/site002-offers-recovery-healthcheck-03` tracking `origin/mars/canonical-post-recovery` |
| Start HEAD | `3f1f6595` (closeout) — **2 behind** origin (`0fbd25bd`, `445dce87` FP-0002 unrelated) |
| Sync | local `git merge --ff-only origin/mars/canonical-post-recovery` → `445dce87` |
| Status after FF | clean; HEAD = origin |
| Closeout commit present | yes (`3f1f6595` ancestor) |
| Refresh commit present | yes (`e0d297e6`) |
| Staged | empty |
| Authority unsafe | **NO** |

Evidence: Storage `preflight/`.

## 5. Metadata fix basis

- Refresh 09 accepted baseline **1887** and updated MONITOR-01 `sitemap-current-urls.json`.
- Closeout Run **4.336** recorded summary still **1377** as cosmetic open item #8.
- Monitor already runs against urls.json + constants **1887**; summary was stale companion metadata only.

Evidence: Storage `reports-read/metadata-fix-basis.md`.

## 6. Metadata file inventory

| Path | Role | Before count | Action |
|------|------|--------------|--------|
| MONITOR-01 `current/sitemap-current-summary.json` | **authoritative active companion** | 1377 | **fixed → 1887** |
| MONITOR-01 `current/sitemap-current-urls.json` | authoritative URL baseline | 1887 | **unchanged** |
| MONITOR-02 `current/sitemap-current-summary.json` | sibling already aligned | 1887 | untouched |
| DELTA-AUDIT / REFRESH-01 summaries | historical evidence | 1377 / 1530 | untouched |
| Authority git | no tracked summary | — | N/A |
| Runtime checkout | no summary copy found | — | no mutation |

Evidence: Storage `metadata-before/`.

## 7. Baseline verification

| Field | Value |
|-------|-------|
| URL file | MONITOR-01 `current/sitemap-current-urls.json` |
| Count / unique | **1887 / 1887** |
| `/katalog/` | **0** |
| SHA-256 | `e4c6c2f188a80cb0c938c15992b21f770c9c555434521eb038ebaa39ea374c84` |
| `/holodilnoe-oborudovanie` | present |
| `/hlebopekarnoe-oborudovanie` | present |
| `/barnoe-oborudovanie` | present |
| `/assum` | present |
| `/tehnologicheskoe-oborudovanie/posuda-i-inventar` | present |
| `/upakovochnoe-oborudovanie` | absent (accepted) |

Hard gate: **PASS** — baseline is 1887; no URL list change required or performed.

Evidence: Storage `baseline-verification/`.

## 8. Metadata fix plan

Update MONITOR-01 summary fields only: `url_count`, `unique_url_count`, `baseline_expected_count` → **1887**; `sha256` → accepted Refresh 09 sitemap XML hash (`9c43e15a…`, same as MONITOR-02); `captured_at` → `2026-08-20T14:00:00+00:00`. Preserve remaining schema fields.

Evidence: Storage `metadata-fix-plan/`.

## 9. Metadata apply

Applied metadata-only rewrite to MONITOR-01 `sitemap-current-summary.json`. URLs JSON not opened for write beyond hash/count verification.

Evidence: Storage `metadata-apply/`.

## 10. Metadata after verification

| Check | Result |
|-------|--------|
| summary counts | **1887 / 1887**, expected **1887** |
| summary sha256 | `9c43e15ad7ca9a7a704814fa6c299e2ab663f5d749d75241e580635eff897c7d` |
| urls.json unchanged | **yes** (count 1887, same SHA) |
| monitor code | unchanged |
| git diff (authority) | docs/report only (summary is Storage-only) |

Evidence: Storage `metadata-after/`.

## 11. Regression / mutation summary

| Surface | Mutated |
|---------|---------|
| Production DB/FTP | 0 |
| 1C import / cache / OCMOD | 0 |
| Categories/products/mapping/importer | 0 |
| Monitor code logic | 0 |
| Baseline URL list / refresh | 0 |
| Runtime checkout | 0 |
| Client Ops / n8n / Telegram | 0 |
| Dirty main / docs-01 / docs-02 / deletes | 0 |
| MONITOR-01 summary metadata | **yes** (allowed) |
| Docs/report + Storage artifacts | **yes** (allowed) |

Evidence: Storage `regression/`.

## 12. Git/worktree summary

| Tree | Role | State |
|------|------|-------|
| docs-03 authority | commit/push docs+report | clean @ `445dce87` before this op edits; then metadata-fix docs commit + FF push |
| `X:\AI MARS` | dirty main | untouched |
| runtime site-002-monitor | scheduled jobs | untouched |
| docs-01 / docs-02 | stale | untouched |

## 13. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-MONITOR-BASELINE-METADATA-FIX-01\` with `preflight/`, `reports-read/`, `metadata-before/`, `baseline-verification/`, `metadata-fix-plan/`, `metadata-apply/`, `metadata-after/`, `docs-update/`, `decision/`, `regression/`, `reports/`, `manifests/operation.json`, `logs/`.

## 14. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Blockers | **none** |
| Whether any scheduled job reads MONITOR-01 summary counts vs urls.json | SAFE UNKNOWN — monitor path historically uses urls.json; counts now consistent either way |
| Runtime absence of summary copy | confirmed for this inspect; no runtime mutation needed |

## 15. Final verdict

`SITE-002 MONITOR BASELINE METADATA FIX COMPLETE — STALE SUMMARY 1377 CORRECTED TO ACTIVE BASELINE 1887`

## 16. Next recommendation

1. Continue normal scheduled monitoring against baseline **1887**.
2. Observe next natural 1C import for `95`/`364` persistence.
3. Keep `upakovochnoe` as a separate decision.
4. docs-01/docs-02 cleanup only after separate approval.
