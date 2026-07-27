# REPORT — SITE-002 Neutral New Categories Visibility Diagnostic 01

**Operation ID:** `SITE-002-PROD-NEUTRAL-NEW-CATEGORIES-VISIBILITY-DIAGNOSTIC-01`  
**OCPilot Run:** **4.310**  
**Date:** 2026-07-27  
**Environment:** PRODUCTION (`https://bzpm.ru/`) — **READ-ONLY**  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** untouched (read-only inspect only)

**Verdict:** `SITE-002 NEUTRAL NEW CATEGORIES VISIBILITY DIAGNOSTIC COMPLETE — ROOT CAUSE IDENTIFIED`

---

## 1. Scope

Diagnose why new/empty categories under `Нейтральное оборудование` (category_id **79**) exist in DB, sitemap, and public HTTP 200, but are not visible in the public site UI.

No production mutation. No template/controller/library changes. No cache clear. No sitemap/baseline change. No Client Ops / n8n / Telegram changes.

## 2. Operator question

«У нас же появились разделы уровня нейтралки новые? Я на сайте не вижу новых разделов.»

Interpretation: empty taxonomy leaves under neutral root 79 are present in data/SEO surfaces, but Launch Mode UI does not present them as browsable «разделы».

## 3. Client Ops boundary

Client Ops Telegram Reports, reporting bridge, Telegram bot, n8n, Hub Gateway — **untouched**. Monitor artifacts used as SITE-002 evidence only.

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `2a6f5823` (= `origin/mars/canonical-post-recovery`) |
| Staged | empty |
| Untracked tools (authority) | 3 pre-existing foreign WIP — **not committed** |
| Dirty main `X:\AI MARS` | foreign WIP — **read-only**; **0 mutations** |

Evidence: Storage `preflight/`.

## 5. Reports read / current state

| Run | Result used |
|-----|-------------|
| 4.307 Monitor Baseline Refresh 07 | Baseline **1836** accepted; 153 + 154–170 absent |
| 4.308 Ambiguous Empty Review Charter | 119 empties; operator review 97 |
| 4.309 Empty Categories HITL Triage | **60** Wait-1C candidates under root **79** |
| 4.285 / 4.287 Tile + megamenu automation | Tech 362 empty hubs shown; **neutral product gate preserved** |

Evidence: Storage `reports-read/`.

## 6. Input artifact ingest

| Metric | Value |
|--------|------:|
| HITL sheet rows | 97 |
| Neutral root 79 candidates | **60** (matches expected) |
| Source | Run 4.309 `operator-decision-sheet/operator-review-sheet.csv` |

Candidate IDs include deep leaves under Моечные ванны / related parents (e.g. 100–105, 259–264, 273+). **0** are direct children of 79. **0** are in the neutral tile whitelist.

Evidence: Storage `input-artifacts/`.

## 7. DB read-only neutral inventory

| Fact | Value |
|------|-------|
| Root 79 | status=1, name `Нейтральное оборудование` |
| Direct active children of 79 | **15** |
| Curated whitelist | 322, 331, 301, 326, 354, 358, 207, 80, 86, 360 |
| Whitelist subtree products | all **>0** (10/10 shown in UI policy) |
| HITL candidates | **60** empty leaves (0 products, 0 children) |
| Candidate depth from 79 | 31 @ depth 2; 29 @ depth 3 |
| 1C maps on candidates | **0** |
| Tech 362 direct children | 5 (364, 368, 369, 373, 375) |

Evidence: Storage `db-readonly/`.

## 8. Sitemap check

| Check | Result |
|-------|--------|
| Live sitemap count | **1836** |
| Neutral candidates in sitemap | **60 / 60** |
| Deleted 153/154–170 markers | **0** |
| Canonical tech URLs | **7 / 7** present |

Evidence: Storage `sitemap/`.

## 9. Public HTTP check

| Check | Result |
|-------|--------|
| Neutral candidates HTTP 200 | **60 / 60** |
| Empty/thin (0 product cards) | **60 / 60** |
| Controls (home, /katalog/, 79, 362, tech children, PDPs 4707–4712) | OK — see `public-controls.csv` |

Evidence: Storage `public-http/`.

## 10. UI visibility check

Exact normalized href match (no name/slug substring false positives):

| Surface | Visible among 60 |
|---------|-----------------:|
| Home catalog tiles | **0** |
| `/katalog/` tiles | **0** |
| Mega menu | **0** |
| Root 79 page | **0** |
| Parent category pages | **0** |
| Sitemap / direct URL only | **60** |

Visible neutral top-level tiles remain the **10 whitelist branches with products** (Моечные ванны, Столы, Стеллажи, …) — not the 60 empty deep leaves.

Evidence: Storage `ui-visibility/`.

## 11. Source code read-only diagnostic

Primary authority:

`system/library/zpm/category_visibility.php` (tools mirror inspected)

| Gate | Behavior |
|------|----------|
| `buildHubChildCards(79)` | Curated whitelist + `require_products=true` |
| `buildHubChildCards(362)` | DB direct children + `require_products=false` |
| `prepareMegamenuCategories` | Section hubs rebuild via `buildHubChildCards` (Run 4.287) |
| `category.php` non-hub children | `if ($totalsub > 0)` before appending to `$data['categories']` |

CSS `.category__view { display: none !important; }` exists in `assets/css/style.css` — **secondary only** (product view chrome). Primary absence of empty leaves is **not rendered** due to product-count gates.

Evidence: Storage `source-code-readonly/`.

## 12. Mega menu diagnostic

- Root 79 is in Launch Mode mega cats (with 362).
- Mega children for 79 = whitelist ∩ products>0 only.
- Empty deep leaves never enter the mega child list.
- Not a stale-cache primary cause: runtime rebuild applies the same gates (cache not cleared this run).

Evidence: Storage `menu-diagnostic/`.

## 13. Tiles diagnostic

- Home and `/katalog/` use `buildCatalogSectionTileBlocks()`.
- Neutral block shows first-level curated branches with products — not deep leaves.
- Tech block can show empty first-level hubs — by design after 4.285/4.287.
- 60 candidates are **expected not** to appear as root tiles.

Evidence: Storage `tiles-diagnostic/`.

## 14. Parent page diagnostic

- Unique parents of the 60 empties inspected.
- Exact href links to empty children: **0**.
- `category.php` omits children with zero subtree products.
- `category__view` markup may exist (product list/grid UI) but is CSS-hidden; this does **not** create missing empty-leaf navigation by itself.

Evidence: Storage `parent-page-diagnostic/`.

## 15. Neutral vs tech comparison

| Aspect | Neutral 79 | Tech 362 |
|--------|------------|----------|
| Child source | Curated whitelist | All active direct children |
| Product gate | **ON** | **OFF** for first-level hubs |
| Empty first-level in UI | Hidden | Shown |
| Deep empty leaves | Sitemap/HTTP only | Same on non-hub parents (`$totalsub > 0`) |
| Intentional? | Yes — commercial Launch Mode | Yes — 1C growth visibility (4.285/4.287) |

Evidence: Storage `neutral-vs-tech-comparison/`.

## 16. Future options

| Option | Summary | Executed? |
|--------|---------|-----------|
| A Keep current | Empties DB+sitemap+HTTP; UI-hidden until products | **Recommended default** |
| B Parent-page children | Show empty leaves under parents only | Charter only if operator wants |
| C Mega menu empties | High clutter risk | Not recommended |
| D Document first-level policy | Already matches tiles/menu | Documentation |
| E Sitemap hide empties | Policy change; baseline impact | Not now |

Evidence: Storage `future-options/`. **Nothing applied.**

## 17. Monitor state

- Live sitemap **1836** = baseline **1836**.
- Prior HITL monitor: `NO_ACTION_REQUIRED`.
- This run did not execute the scheduled monitor; sitemap parity supports clean state.

Evidence: Storage `monitor-state/`.

## 18. Decision

| Field | Value |
|-------|-------|
| Classification | `NEUTRAL_VISIBILITY_DIAGNOSTIC_COMPLETE` |
| Root causes | `HIDDEN_BY_PRODUCT_COUNT_GATE`, `HIDDEN_BECAUSE_DEEP_LEAVES_NOT_ROOT_TILES`, `HIDDEN_BY_EXPECTED_UI_POLICY`, `HIDDEN_BY_PARENT_TEMPLATE` |
| CSS role | Secondary only |
| Next | `NEEDS_OPERATOR_DECISION` |
| Safe default | `KEEP_CURRENT_BEHAVIOR` |
| Optional charter | `PREPARE_PARENT_PAGE_CHILD_VISIBILITY_CHARTER` |

**Answer to operator:** новые пустые категории под нейтралкой **есть в данных и sitemap**, но **специально не показываются** в плитках / мегаменю / списках дочерних на родительских страницах, пока нет товаров. Это не баг импорта и не «пропажа» разделов — политика Launch Mode + product-count gate. Тех-корень 362 как раз исключение: пустые **первого уровня** там показываются намеренно.

## 19. Regression

All mutation checks **0** — see Storage `regression/regression-check.csv`.

## 20. Production mutation summary

- DB writes: **0**
- FTP writes: **0**
- source/code changes: **0**
- cache clear: **0**
- delete operations: **0**
- import runs: **0**
- scheduler changes: **0**
- monitor baseline changes: **0**
- category/product changes: **0**
- redirect changes: **0**
- `.htaccess` changes: **0**
- importer/source changes: **0**
- mapping changes: **0**
- image changes: **0**
- Client Ops changes: **0**
- n8n changes: **0**
- Telegram changes: **0**
- dirty main changes: **0**

## 21. Git/worktree summary

- Authority branch: `site-002-git-authority-realign-after-wave-e`
- Start HEAD: `2a6f5823`
- Commits this op: report + doc updates only (exact paths)
- Push target: `origin/mars/canonical-post-recovery` (fast-forward)
- Dirty main: untouched

## 22. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEUTRAL-NEW-CATEGORIES-VISIBILITY-DIAGNOSTIC-01\`

## 23. SAFE UNKNOWN / blockers

- Exact production `category.php` byte-for-byte vs tools mirror: tools snapshot from Run 4.285 used; behavior matches live parent pages (0 empty-child hrefs). Full FTP download of live `category.php` not required for verdict.
- Scheduled monitor runner folder not re-executed; sitemap live count used as monitor-parity proxy.

## 24. Final verdict

**SITE-002 NEUTRAL NEW CATEGORIES VISIBILITY DIAGNOSTIC COMPLETE — ROOT CAUSE IDENTIFIED**

## 25. Next recommendation

1. Operator decision: **KEEP_CURRENT_BEHAVIOR** (default) vs charter for **parent-page empty-child visibility**.
2. Do not auto-show empty categories in mega menu/tiles.
3. Continue Wait-1C HITL posture for the 60 empties unless marked obsolete.
4. No apply in this operation.
