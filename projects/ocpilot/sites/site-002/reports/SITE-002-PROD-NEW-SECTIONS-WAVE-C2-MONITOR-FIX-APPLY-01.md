# REPORT — SITE-002 New Sections Wave C2 Monitor Fix Apply 01

**Operation:** `SITE-002-PROD-NEW-SECTIONS-WAVE-C2-MONITOR-FIX-APPLY-01`  
**OCPilot run:** **4.331**  
**Date:** 2026-08-20  
**Environment:** `NEW_SECTIONS_WAVE_C2_MONITOR_FIX_APPLY`  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-WAVE-C2-MONITOR-FIX-APPLY-01\`

**Final verdict:** `SITE-002 NEW SECTIONS WAVE C2 MONITOR FIX COMPLETE — RUNTIME VALIDATION PENDING, BASELINE STILL BLOCKED`

**Classifications:**
- `WAVE_C2_MONITOR_FIX_COMPLETE`
- `ROUTE_CHURN_SEMANTIC_LAYER_ADDED`
- `MONITOR_ARTIFACT_AGREEMENT_CONFIRMED`
- `BASELINE_REFRESH_STILL_BLOCKED`
- `READY_FOR_MONITOR_VALIDATION_RUN`

**Next:**
- `READY_FOR_MONITOR_VALIDATION_RUN`
- `DO_NOT_REFRESH_BASELINE_YET`
- `OBSERVE_NEXT_1C_IMPORT_FOR_95_364_MAPPING`
- Later (after gate): `SITE-002-MONITOR-BASELINE-REFRESH-09`

---

## 1. Scope

Apply Wave C2 monitor tooling fixes only:
- runner classification merge precedence;
- semantic route-normalization diff layer;
- onboarding inflation filter;
- regression fixture;
- docs/report.

**Not in scope:** baseline refresh, production DB/FTP/import/mapping/category/product changes, Client Ops / n8n / Telegram.

## 2. Operator approval

Operator approved Wave C2 after Wave C diagnostic: `Ок, утверждаю. Жду промт.`

## 3. Client Ops boundary

**Not touched:** Client Ops Telegram Reports, reporting bridge, n8n, Telegram bot, Hub Gateway.

## 4. Preflight

| Check | Result |
|-------|--------|
| Worktree | `X:/AI MARS STORAGE/git-sync-site002-offers-recovery-docs-03/repo` |
| Branch | `docs/site002-offers-recovery-healthcheck-03` |
| HEAD (start) | `29707aeb` |
| Origin (start) | `3aa0d6c8` (1 behind — fast-forwarded) |
| HEAD (after sync) | `3aa0d6c8` |
| Working tree | clean |

Evidence: Storage `preflight/`.

## 5. Wave C root cause basis

From [Wave C diagnostic 4.330](SITE-002-PROD-NEW-SECTIONS-WAVE-C-MONITOR-DIAGNOSTIC-01.md):

1. **Runner bug:** `Finish-Summary` defaulted `NO_ACTION_REQUIRED`, then runner keys overwrote monitor merge → `run-summary.json` wrong while `monitor-classification.json` correct.
2. **Route churn:** baseline 1879 `/katalog/` vs current 1887 root pretty URLs → exact diff 1873/1865 inflated; net +8; raw onboarding 219 inflated (≤10 real).

## 6. Source before

| File | Role |
|------|------|
| `site-002-post-1c-monitor-runner.ps1` | Runner merge bug |
| `site-002-prod-post-1c-catalog-onboarding-monitor-02.py` | Exact-only delta, stale allowlist, inflated onboarding |

Evidence: Storage `source-before/`.

## 7. Fix plan

See Storage `fix-plan/fix-plan.md`. Summary:

- **A.** `monitor-classification.json` wins over runner default in `Finish-Summary`
- **B.** `compute_semantic_delta()` + artifacts `semantic-delta-summary.json`, `route-migration-pairs.json`
- **C.** `is_onboarded_path()` + baseline semantic filter in `phase5_category_onboarding`
- **D.** `classify_delta_scale` / `classify_monitor_run` use semantic counts; exact scale preserved as `delta_scale_exact`
- **E.** `--fixture-route-churn-test` against baseline 1879 artifact

## 8. Source apply

| File | Change |
|------|--------|
| `site-002-post-1c-monitor-runner.ps1` | Fixed merge precedence; diagnostic fields |
| `site-002-prod-post-1c-catalog-onboarding-monitor-02.py` | Semantic delta layer, onboarding filter, expanded allowlist, fixture test |
| `tools/fixtures/wave-c2-route-churn-regression.json` | Fixture metadata |

Evidence: Storage `source-apply/`.

## 9. Tests

| Check | Result |
|-------|--------|
| Python compile | PASS |
| PowerShell parse (runner) | PASS |
| `--fixture-route-churn-test` | **PASS** — all checks true |
| Mock artifact agreement | PASS |

**Fixture highlights:**
- exact_added/removed: **1871 / 1864**
- semantic_added/removed: **7 / 0**
- route_migration_pair_count: **1864**
- delta_scale_exact: `SUSPICIOUS_GROWTH`
- delta_scale_semantic: `SMALL_EXPECTED_GROWTH`
- onboarding_needs_count: **2** (vs raw 219 pre-fix)

Evidence: Storage `tests/`.

## 10. Dry-run / artifact validation

- Runner `-DryRun`: PASS (environment + sitemap probe only; no full monitor crawl)
- Mock merge validation: final classification preserved from `monitor-classification.json`
- **Runtime scheduled validation pending** — next Task Scheduler run should confirm live artifact agreement

Evidence: Storage `dry-run-validation/`, `artifact-validation/`.

## 11. Baseline refresh gate

**Status:** `DO_NOT_REFRESH_BASELINE_YET`

Gate for future `SITE-002-MONITOR-BASELINE-REFRESH-09` unchanged — see Storage `baseline-gate/baseline-refresh-gate.md`.

## 12. Regression / mutation summary

| Forbidden mutation | Count |
|--------------------|------:|
| Baseline refresh | 0 |
| Production DB/FTP | 0 |
| Import runs | 0 |
| Mapping / category / product | 0 |
| Client Ops / n8n / Telegram | 0 |
| docs-01 / docs-02 | 0 |
| Dirty main | 0 |

Evidence: Storage `regression/`.

## 13. Git/worktree summary

| Field | Value |
|-------|--------|
| Worktree | clean at start (after ff sync) |
| Branch | `docs/site002-offers-recovery-healthcheck-03` |
| Base | `3aa0d6c8` |
| Commit | monitor tooling + docs/report |

## 14. Storage artifacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-WAVE-C2-MONITOR-FIX-APPLY-01\`

Key folders: `preflight/`, `reports-read/`, `fix-plan/`, `source-apply/`, `tests/`, `dry-run-validation/`, `artifact-validation/`, `baseline-gate/`, `decision/`, `regression/`, `manifests/`.

## 15. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Live scheduled run artifact agreement post-C2 | **Pending** — await next monitor run |
| Full semantic pairing beyond simple prefix strip | Partial — deeper path restructuring may remain |
| Post-C2 live classification with real crawl | **SAFE UNKNOWN** until scheduled validation |

No production mutation blockers.

## 16. Final verdict

`SITE-002 NEW SECTIONS WAVE C2 MONITOR FIX COMPLETE — RUNTIME VALIDATION PENDING, BASELINE STILL BLOCKED`

**Summary:**
- Runner artifact bug **fixed** in code
- Semantic route-churn layer **added**; exact diff **preserved**
- Fixture regression **PASS**
- Baseline refresh **still blocked**
- Next: **scheduled monitor validation run**

## 17. Next recommendation

1. Observe next scheduled post-1C monitor run — verify `run-summary.json` classification == `monitor-classification.json`.
2. **Do not refresh baseline yet.**
3. Observe next natural 1C import for `95` / `364` mapping behavior.
4. After validation + operator approval, charter `SITE-002-MONITOR-BASELINE-REFRESH-09`.
