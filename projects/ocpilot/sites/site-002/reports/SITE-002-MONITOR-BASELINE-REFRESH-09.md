# REPORT — SITE-002 Monitor Baseline Refresh 09

**Operation:** `SITE-002-MONITOR-BASELINE-REFRESH-09`  
**OCPilot run:** **4.335**  
**Date:** 2026-08-20  
**Environment:** MONITOR_BASELINE_REFRESH_AFTER_C2_VALIDATION  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-MONITOR-BASELINE-REFRESH-09\`

**Final verdict:** `SITE-002 MONITOR BASELINE REFRESH 09 COMPLETE — POST-C2 PRETTY-URL SITEMAP ACCEPTED, ROUTE CHURN BASELINE BLOCKER RESOLVED`

**Classifications:**

- `SITE_002_MONITOR_BASELINE_REFRESH_09_COMPLETE`
- `POST_C2_PRETTY_URL_BASELINE_ACCEPTED`
- `ROUTE_CHURN_BASELINE_BLOCKER_RESOLVED`
- `UPAKOVOCHNOE_REMAINS_SEPARATE`
- `OBSERVE_NEXT_1C_IMPORT_FOR_95_364_MAPPING`

---

## 1. Scope

Refresh SITE-002 post-1C catalog monitor baseline from **1879** (mostly `/katalog/...`) to the current accepted pretty-URL sitemap **1887** after operator approval. Monitor/baseline hygiene + docs/report only.

Not in scope: production DB/FTP, 1C import, category/product/mapping/importer, monitor classification logic, Client Ops/n8n/Telegram, dirty main, docs-01/docs-02.

## 2. Operator approval

Operator text: `всё давай сделаем`.

Interpreted as explicit approval for `SITE-002-MONITOR-BASELINE-REFRESH-09`: accept post-C2 pretty-URL sitemap as monitor baseline; do not mutate production; do not run 1C import.

Evidence: Storage `approval/operator-approval.md`.

## 3. Client Ops boundary

- **Not touched:** Client Ops Telegram Reports, reporting bridge, n8n, Telegram bot, Hub Gateway, reporting envelope.
- SITE-002 monitor artifacts read/written only under SITE-002 monitor deployment / this operation Storage tree.
- Dirty main Client Ops WIP left foreign and untouched.

## 4. Authority preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority path | `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo` |
| Branch | `docs/site002-offers-recovery-healthcheck-03` tracking `origin/mars/canonical-post-recovery` |
| HEAD before edits | `9865413c` (= `origin/mars/canonical-post-recovery`) |
| Staged | empty |
| Dirty main | foreign WIP — **read-only**; **0** mutations by this op |
| Authority unsafe | **NO** |

Evidence: Storage `preflight/`.

## 5. Refresh basis

Scheduled validation (Run 4.334, commit `9865413c`) already confirmed:

- scheduled run `2026-08-20_13-29-44` exit 0 from C2 runtime;
- artifact agreement;
- semantic diff vs exact route churn;
- classification `ONBOARDING_REQUIRED` while baseline was still 1879;
- baseline status `READY_FOR_BASELINE_REFRESH_APPROVAL`.

Refresh is now allowed because operator approval exists and live sitemap still matches accepted **1887**. Remaining out of scope: `upakovochnoe` 404 (accepted absent), mapping persistence `95`/`364` (observe next natural import).

Evidence: Storage `reports-read/baseline-refresh-basis.md`.

## 6. Current sitemap read-only

| Field | Value |
|-------|-------|
| HTTP | **200** |
| Valid XML | **yes** |
| Unique count | **1887** (matches expected) |
| Duplicates | **0** |
| `/katalog/` | **0** |
| `/brands/` | **0** |
| SHA-256 (XML) | `9c43e15ad7ca9a7a704814fa6c299e2ab663f5d749d75241e580635eff897c7d` |
| `/holodilnoe-oborudovanie` | present |
| `/hlebopekarnoe-oborudovanie` | present |
| `/barnoe-oborudovanie` | present |
| `/assum` | present |
| `/brands/assum` | absent |
| `/upakovochnoe-oborudovanie` | absent (accepted 404) |
| `/posuda-i-inventar` root | **absent** |
| `/tehnologicheskoe-oborudovanie/posuda-i-inventar` | **present** (accepted nested pretty-URL; Wave B DB child of Tech 362) |

Hard gate: **PASS**. Root `/posuda-i-inventar` missing is explained and accepted; not a stop.

Evidence: Storage `current-sitemap/`.

## 7. Previous baseline snapshot

| Field | Value |
|-------|-------|
| Path | MONITOR-01 `current/sitemap-current-urls.json` (pre-refresh) |
| Count | **1879** |
| `/katalog/` | **1863** |
| `/brands/` | **1** (`/brands/assum`) |
| SHA-256 | `c460d889a4f446a8259120aa9a339644cf0989fccacad6ee0da934ac1fcc6294` |
| Frozen copies | operation `previous-baseline/` + MONITOR-01 sibling `sitemap-current-urls-1879-pre-refresh-09.json` |

Previous baseline **not deleted**. C2 `--fixture-route-churn-test` now points at the frozen 1879 file.

Evidence: Storage `previous-baseline/`.

## 8. Baseline refresh plan

New baseline = current accepted pretty-URL sitemap (~1887), `/katalog/` = 0, `upakovochnoe` absent, exact old→new route churn accepted as migrated, semantic monitor no longer a blocker after refresh.

Evidence: Storage `baseline-refresh-plan/`.

## 9. Baseline refresh apply

Local Storage JSON replacement of MONITOR-01 `sitemap-current-urls.json` (+ CSV). Production DB/FTP/import **not** invoked. Monitor classification/semantic logic **not** changed.

| Field | Value |
|-------|-------|
| Old → new | **1879 → 1887** |
| Exact added / removed vs old JSON | **1873 / 1865** |
| New SHA-256 | `e4c6c2f188a80cb0c938c15992b21f770c9c555434521eb038ebaa39ea374c84` |
| Checkpoint | `SITE-002-STABLE-PROD-POST-C2-PRETTY-URL-MONITOR-BASELINE-1887-09` |
| Monitor constants | expected **1887**; `BASELINE_BEFORE` / `AUDIT_BASELINE_BEFORE` updated; fixture path = frozen 1879 |
| Runtime sync | **yes** — same script copied to runtime checkout |

Evidence: Storage `baseline-refresh-apply/`.

## 10. New baseline verification

| Field | Value |
|-------|-------|
| Count / unique | **1887 / 1887** |
| `/katalog/` | **0** |
| `/holodilnoe-oborudovanie` | present |
| `/hlebopekarnoe-oborudovanie` | present |
| `/barnoe-oborudovanie` | present |
| `/upakovochnoe-oborudovanie` | absent |
| `/assum` | present |
| `/brands/assum` | absent |
| `/posuda-i-inventar` root | absent (nested tech path present) |

Evidence: Storage `new-baseline/`.

## 11. Post-refresh monitor check

Bounded Python on runtime checkout: `--skip-removed-crawl --scheduled-run-dir` under this operation. No import. No production mutation.

| Field | Value |
|-------|-------|
| exit_code | **0** |
| duration | **17 seconds** |
| baseline → current | **1887 → 1887** |
| exact added / removed | **0 / 0** |
| semantic added / removed | **0 / 0** |
| route_migration_pair_count | **0** |
| classification | **`NO_ACTION_REQUIRED`** |
| artifact agreement | **yes** (`run-summary.json` = `monitor-classification.json`) |
| C2 fixture vs frozen 1879 | **PASS** |

Old 1873/1865 route churn is **not** reported against the new baseline.

Evidence: Storage `post-refresh-monitor-check/`.

## 12. Baseline transition summary

| Field | Old | New |
|-------|-----|-----|
| Count | 1879 | 1887 |
| Net | — | +8 |
| `/katalog/` | 1863 | 0 |
| Brand URL | `/brands/assum` | `/assum` |
| Wave A roots | not in old baseline | `hlebopekarnoe`, `holodilnoe` present |
| Wave B posuda | — | nested under tech |
| Route migration | active blocker vs 1879 | **resolved** |

Evidence: Storage `diff-summary/`.

## 13. Open items after refresh

- Observe next natural 1C import for `95`/`364` mapping persistence.
- `upakovochnoe` remains separate (XML exists; public 404; absent from this baseline).
- `hlebopekarnoe` root mapping remains separate.
- `barnoe` XML identity remains SAFE UNKNOWN.
- D6G1A console-hide patch not re-applied remains a separate runtime UX topic.

Evidence: Storage `open-items/`.

## 14. Regression / mutation summary

Forbidden mutation classes **0** (production DB/FTP, import, cache, OCMOD, category/product, mapping, importer, monitor logic, site source/template/JS/image, Client Ops/n8n/Telegram, local cleanup, dirty main, docs-01/docs-02).

Allowed: baseline artifacts, monitor metadata constants, docs/report/checkpoint, Storage operation tree, runtime copy of the same script.

Evidence: Storage `regression/`.

## 15. Git/worktree summary

| Worktree | Role |
|----------|------|
| `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo` | authority | baseline checkpoint + monitor constants + report/docs (this commit) |
| `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` | runtime | monitor script constant sync + bounded after-run |
| `X:\AI MARS` | dirty main | **read-only**; **0** mutations |

## 16. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-MONITOR-BASELINE-REFRESH-09\`

Subfolders: preflight, reports-read, approval, current-sitemap, previous-baseline, baseline-refresh-plan, baseline-refresh-apply, new-baseline, post-refresh-monitor-check, diff-summary, open-items, docs-update, decision, regression, reports, manifests, logs.

## 17. SAFE UNKNOWN / blockers

- None blocking this refresh.
- Mapping persistence for `95`/`364` after next natural 1C import remains **unobserved** (does not block).
- `barnoe` XML identity remains SAFE UNKNOWN (does not block).
- Natural scheduled post-refresh monitor run is **not** claimed from this manual Python after-run alone.

## 18. Final verdict

`SITE-002 MONITOR BASELINE REFRESH 09 COMPLETE — POST-C2 PRETTY-URL SITEMAP ACCEPTED, ROUTE CHURN BASELINE BLOCKER RESOLVED`

## 19. Next recommendation

- `OBSERVE_NEXT_1C_IMPORT_FOR_95_364_MAPPING`
- `UPAKOVOCHNOE_SEPARATE_DECISION_REQUIRED`
- continue normal scheduled monitoring against the 1887 pretty-URL baseline
