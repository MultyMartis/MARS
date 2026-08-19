# REPORT — SITE-002 New Sections Wave C Monitor Diagnostic 01

**Operation:** `SITE-002-PROD-NEW-SECTIONS-WAVE-C-MONITOR-DIAGNOSTIC-01`  
**OCPilot run:** **4.330**  
**Date:** 2026-08-19  
**Environment:** `NEW_SECTIONS_WAVE_C_MONITOR_DIAGNOSTIC_READONLY`  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-WAVE-C-MONITOR-DIAGNOSTIC-01\`

**Final verdict:** `SITE-002 NEW SECTIONS WAVE C MONITOR DIAGNOSTIC COMPLETE — ROUTE CHURN AND CLASSIFICATION INCONSISTENCY EXPLAINED, BASELINE STILL BLOCKED`

**Classifications:**
- `WAVE_C_MONITOR_DIAGNOSTIC_COMPLETE`
- `MONITOR_ROUTE_CHURN_CONFIRMED`
- `MONITOR_CLASSIFICATION_ARTIFACT_BUG_CONFIRMED`
- `MONITOR_FIX_APPLY_REQUIRED`
- `BASELINE_REFRESH_STILL_BLOCKED`

**Next:**
- `READY_FOR_WAVE_C2_MONITOR_FIX_APPLY_AFTER_APPROVAL`
- `DO_NOT_REFRESH_BASELINE_YET`
- `OBSERVE_NEXT_1C_IMPORT_FOR_95_364_MAPPING`

---

## 1. Scope

Read-only monitor diagnostic after Wave A onboarding and Wave B1 mapping backfill. Explain monitor artifact inconsistency on scheduled run `2026-08-19_12-30-05`, separate route-normalization churn from real onboarding needs, and define Wave C2 monitor fix + baseline refresh gate.

**Not in scope:** baseline refresh, monitor code apply, production DB/FTP/import/mapping/category/product changes, Client Ops / n8n / Telegram.

## 2. Operator approval

Operator approved Wave C monitor diagnostic: `Ок, утверждаю. Жду промт.`

Interpretation honored:
- proceed with monitor diagnostic;
- do not refresh baseline;
- do not mutate production;
- do not change monitor code in this task;
- produce root-cause analysis and bounded future fix plan.

## 3. Client Ops boundary

**Not touched:** Client Ops Telegram Reports, reporting bridge, n8n, Telegram bot, Hub Gateway, reporting envelope.

Monitor artifacts read-only from Storage scheduled-monitors path and runtime checkout references only.

## 4. Preflight

| Check | Result |
|-------|--------|
| Worktree | `X:/AI MARS STORAGE/git-sync-site002-offers-recovery-docs-03/repo` |
| Branch | `docs/site002-offers-recovery-healthcheck-03` |
| HEAD | `e28903d23441df213c93aa85e186d4907e01863e` |
| `origin/mars/canonical-post-recovery` | `e28903d23441df213c93aa85e186d4907e01863e` |
| Ahead/behind | +0 / -0 |
| Working tree | clean |
| Latest commit | `e28903d2` — Wave B1 mapping apply |

Evidence: Storage `preflight/`.

## 5. Current state after B1

| Area | State |
|------|-------|
| Offers recovery | SUCCESS — `mars_1c_import_2026-08-19_080010.txt` |
| Wave A | Complete — bounded meta for `186` / `95` |
| Wave B charter | Complete — B1 narrowed to `95` + `364` |
| Wave B1 apply | Complete — `oc_mars_1c_category_map` 7→9 rows |
| Monitor baseline file | **1879** — unchanged |
| Live sitemap | **1887** |
| Monitor problem run | `2026-08-19_12-30-05` |

## 6. Reports read

Upstream reports confirm:
- offers recovered and new sections need onboarding/placement work ([healthcheck 4.325](SITE-002-PROD-POST-1C-OFFERS-RECOVERY-AND-NEW-SECTIONS-HEALTHCHECK-01.md));
- baseline refresh explicitly deferred pending monitor diagnostic ([charter 4.326](SITE-002-PROD-NEW-SECTIONS-ONBOARDING-PLACEMENT-CHARTER-01.md));
- Wave A/B1 completed without baseline refresh ([apply 4.327](SITE-002-PROD-NEW-SECTIONS-WAVE-A-ONBOARDING-APPLY-01.md), [apply 4.329](SITE-002-PROD-NEW-SECTIONS-WAVE-B1-MAPPING-BACKFILL-APPLY-01.md));
- baseline 1879 established 2026-07-28 with `/katalog/...` URL shape ([baseline refresh 4.312](SITE-002-MONITOR-BASELINE-REFRESH-08.md)).

Evidence: Storage `reports-read/`.

## 7. Monitor artifacts review

Run `2026-08-19_12-30-05`:

| Field | Value |
|-------|-------|
| Scheduler LastTaskResult | 0 |
| Duration | 35m 26s |
| Baseline → current | 1879 → 1887 |
| Exact added / removed | 1873 / 1865 |
| Unchanged exact URLs | 14 |
| Onboarding needs | 219 |
| `run-summary.json` classification | `NO_ACTION_REQUIRED` |
| `monitor-classification.json` classification | `ONBOARDING_REQUIRED` |
| delta_scale | `SUSPICIOUS_GROWTH` |
| Strict garbage / hygiene / brand | 0 / 0 / 0 |

Adjacent run `2026-08-18_12-41-39` shows the **same mismatch**, indicating a systemic runner bug rather than a one-off run anomaly.

Evidence: Storage `monitor-artifacts/`.

## 8. Monitor source review

Key findings from `site-002-prod-post-1c-catalog-onboarding-monitor-02.py`:

| Component | Behavior |
|-----------|----------|
| `phase3_delta()` | Exact URL string set diff only — no route-normalization pairing |
| `normalize_url()` | Used for duplicate detection, not delta classification |
| `phase5_category_onboarding()` | Flags added categories not in `ONBOARDED_CATEGORY_PATHS` |
| `classify_monitor_run()` | Returns `ONBOARDING_REQUIRED` when onboarding_needs_count > 0 |
| `export_scheduled_artifacts()` | Writes **both** artifacts with same classification |

Key findings from `site-002-post-1c-monitor-runner.ps1`:

| Component | Behavior |
|-----------|----------|
| `Finish-Summary` | Defaults `classification = NO_ACTION_REQUIRED` on exit 0 |
| Merge logic | Overwrites monitor-merged fields with runner `$summary` where not null |
| Result | Runner default wins → `run-summary.json` wrong; `monitor-classification.json` untouched |

Evidence: Storage `monitor-source-review/`.

## 9. Baseline review

| Field | Value |
|-------|-------|
| Checkpoint | `SITE-002-STABLE-PROD-POST-1C-IMPORT-20260728-MONITOR-BASELINE-1879-08` |
| Count | 1879 |
| `/katalog/` URLs | 1863 |
| `/brands/assum` | present |
| Root catalog slugs | 15 |
| Info/static unchanged | 14 URLs shared exactly with current sitemap |

Baseline predates site-wide removal of `/katalog/` prefix from sitemap emission.

Evidence: Storage `baseline-review/`.

## 10. Current sitemap snapshot

Diagnostic live fetch: HTTP **200**, loc count **1887**.

| Pattern | Current count |
|---------|---------------|
| `/katalog/` | 0 |
| `/brands/` | 0 |
| Root catalog slugs | 1672 |
| Other/info | 215 |

Target presence:
- `/holodilnoe-oborudovanie` — present
- `/tehnologicheskoe-oborudovanie/posuda-i-inventar` — present
- `/hlebopekarnoe-oborudovanie` — present
- `/barnoe-oborudovanie` — present
- `/upakovochnoe-oborudovanie` — absent (404 expected)
- `/assum` — present
- `/brands/assum` — absent
- `/katalog/barnoe-oborudovanie` — absent

Evidence: Storage `sitemap-current/`.

## 11. Diff analysis

| Metric | Value |
|--------|-------|
| Net count delta | +8 |
| Exact added | 1873 |
| Exact removed | 1865 |
| Simple migration pairs (`/katalog/x`→`/x`, `/brands/x`→`/x`) | 225 |
| True added after pair filter | ~1648 |
| True removed after pair filter | ~1640 |

The huge string diff is **not** +1873 new pages. It is almost entirely legacy `/katalog/...` baseline URLs vs current root pretty URLs, plus deeper path restructuring beyond simple prefix strip.

Evidence: Storage `diff-analysis/`.

## 12. Route normalization review

Confirmed: monitor currently compares raw URL strings without canonical route normalization.

Recommended Wave C2 semantics:
1. Keep exact diff as SEO audit artifact.
2. Add semantic diff layer for classification/onboarding.
3. Treat known migration pairs as `ROUTE_NORMALIZATION_REVIEW`, not onboarding.
4. Recompute delta scale from semantic net change (+8), not raw added count.

Evidence: Storage `route-normalization-review/`.

## 13. Classification review

### Answers to diagnostic questions

| # | Question | Answer |
|---|----------|--------|
| 1 | Authoritative artifact? | **`monitor-classification.json`** |
| 2 | Why disagree? | Runner merge bug overwrites monitor classification in `run-summary.json` |
| 3 | Why summary says NO_ACTION? | Runner default before merge, then runner keys win |
| 4 | Why added=1873 removed=1865 with +8 net? | Exact string diff across route migration; only 14 URLs unchanged |
| 5 | Route normalization cause? | **Yes — primary cause** |
| 6 | Raw string compare without normalization? | **Yes** |
| 7 | High churn treated correctly? | **No** — marked SUSPICIOUS_GROWTH and inflates onboarding |
| 8 | Are 219 onboarding needs real? | **No — inflated**; estimate ≤10 real category items |
| 9 | Distinguishes growth vs migration vs onboarding? | **No** — single exact-string pipeline |
| 10 | What needs fixing? | Runner merge + semantic diff layer + allowlist update |
| 11 | Monitor fix before baseline refresh? | **Yes** |
| 12 | One-time baseline refresh safe now? | **No — still blocked** |
| 13 | Future apply task? | `SITE-002-PROD-NEW-SECTIONS-WAVE-C2-MONITOR-FIX-APPLY-01` |
| 14 | Baseline refresh acceptance gate? | See §16 |

Evidence: Storage `classification-review/`.

## 14. Onboarding needs review

Raw monitor count: **219**. All include `newly added category branch not documented`.

Added URL mix from changed-summary:
- PRODUCT_PDP: 1647
- CATEGORY_PLP: 168
- CATEGORY_HUB: 47
- LEGACY_HUB: 10

After Wave A/B1 and route-normalization context:
- ~200+ flags are migration artifacts;
- real charter gaps remain: `barnoe`, `upakovochnoe`, `posuda` UI/placement, residual meta on already-handled branches;
- conservative real estimate: **≤10** category-level items.

Evidence: Storage `onboarding-needs-review/`.

## 15. Future fix plan

**Wave C2 (not executed):** `SITE-002-PROD-NEW-SECTIONS-WAVE-C2-MONITOR-FIX-APPLY-01`

1. Fix runner merge precedence in `site-002-post-1c-monitor-runner.ps1`.
2. Add semantic route-normalization diff in monitor-02 Python.
3. Split exact vs semantic artifacts in scheduled export.
4. Expand `ONBOARDED_CATEGORY_PATHS` with root-level equivalents.
5. Adjust `classify_delta_scale()` for semantic net delta.
6. Add fixture regression: baseline 1879 vs current 1887.
7. Validate one scheduled run with artifact agreement.

Evidence: Storage `future-fix-plan/`.

## 16. Baseline refresh gate

Baseline refresh remains **BLOCKED** until:

1. Wave C2 monitor fix verified.
2. `run-summary.json` == `monitor-classification.json` for ≥1 scheduled run.
3. Route migration semantics accepted.
4. Wave A + B1 accepted.
5. Live sitemap 1887 confirmed.
6. `upakovochnoe` 404 accepted.
7. Semantic diff reviewed; raw 219 inflation acknowledged.
8. Explicit operator approval for baseline refresh charter.

Future charter candidate: `SITE-002-MONITOR-BASELINE-REFRESH-09` (1879 → 1887 pretty-URL snapshot).

Evidence: Storage `baseline-refresh-gate/`.

## 17. Docs update

Updated in this task:
- `projects/ocpilot/OCPILOT-STATE.md`
- `projects/ocpilot/OPERATIONAL-INDEX.md`
- `projects/ocpilot/sites/site-002/production-profile.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`
- `projects/ocpilot/sites/site-002/tools/README.md`

Evidence: Storage `docs-update/` (implicit via repo commit).

## 18. Regression / mutation summary

| Forbidden mutation | Count |
|--------------------|------:|
| Baseline refresh | 0 |
| Monitor code changes | 0 |
| Production DB/FTP writes | 0 |
| Import runs | 0 |
| Mapping / category / product changes | 0 |
| Client Ops / n8n / Telegram | 0 |
| docs-01 / docs-02 touch | 0 |
| Dirty main mutation | 0 |

Allowed: docs/report + Storage diagnostic artifacts only.

Evidence: Storage `regression/`.

## 19. Git/worktree summary

| Field | Value |
|-------|-------|
| Worktree | clean at start |
| Branch | `docs/site002-offers-recovery-healthcheck-03` |
| Base commit | `e28903d2` |
| Commit in this task | docs/report only |

## 20. Storage artifacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-WAVE-C-MONITOR-DIAGNOSTIC-01\`

Key folders: `preflight/`, `monitor-artifacts/`, `monitor-source-review/`, `baseline-review/`, `sitemap-current/`, `diff-analysis/`, `route-normalization-review/`, `classification-review/`, `onboarding-needs-review/`, `future-fix-plan/`, `baseline-refresh-gate/`, `decision/`, `regression/`, `manifests/`.

Manifest: `manifests/operation.json`.

## 21. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Exact date `/katalog/` prefix disappeared from live sitemap | **SAFE UNKNOWN** — inferred between baseline refresh 4.312 (2026-07-28) and monitor run 2026-08-18; likely tied to sitemap controller / SEO URL evolution |
| Full semantic pairing for all 1863 legacy katalog URLs | Partial — 225 simple pairs proven; remainder likely deeper path restructuring |
| Whether post-C2 classification should be HYGIENE vs ROUTE_MIGRATION vs reduced ONBOARDING | Requires Wave C2 fixture run |

No production mutation blockers for diagnostic itself.

## 22. Final verdict

`SITE-002 NEW SECTIONS WAVE C MONITOR DIAGNOSTIC COMPLETE — ROUTE CHURN AND CLASSIFICATION INCONSISTENCY EXPLAINED, BASELINE STILL BLOCKED`

**Summary:**
- Effective monitor status = **`ONBOARDING_REQUIRED`** per `monitor-classification.json`.
- `run-summary.json` **`NO_ACTION_REQUIRED`** is a **runner artifact bug**, not monitor logic truth.
- Raw diff `1873/1865` is **route churn**, not +1873 new URLs; net growth is **+8**.
- Raw onboarding **219** is **inflated**; real charter gaps ≈ **≤10** categories.
- Baseline refresh **still blocked** until Wave C2 fix + explicit gate.

## 23. Next recommendation

1. Operator approve **`SITE-002-PROD-NEW-SECTIONS-WAVE-C2-MONITOR-FIX-APPLY-01`**.
2. **Do not refresh baseline yet.**
3. Observe next natural 1C import for `95` / `364` mapping behavior.
4. After C2 + gates, charter baseline refresh 1879→1887 with pretty-URL snapshot.
