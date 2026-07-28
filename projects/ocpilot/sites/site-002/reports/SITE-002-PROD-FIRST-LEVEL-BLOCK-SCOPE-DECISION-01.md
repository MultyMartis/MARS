# REPORT — SITE-002 First-Level Block Scope Decision 01

**Operation ID:** `SITE-002-PROD-FIRST-LEVEL-BLOCK-SCOPE-DECISION-01`  
**OCPilot Run:** **4.313**  
**Date:** 2026-07-28  
**Environment:** PRODUCTION (`https://bzpm.ru/`) — **READ-ONLY / DECISION-ONLY**  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-FIRST-LEVEL-BLOCK-SCOPE-DECISION-01\`

**Verdict:** `SITE-002 FIRST-LEVEL BLOCK SCOPE DECISION COMPLETE — HYBRID RECOMMENDED`

**Classifications:**
- Scope decision: `HYBRID_RECOMMENDED`
- Apply readiness: `READY_FOR_FIRST_LEVEL_BLOCK_APPLY_AFTER_OPERATOR_CONFIRMATION`
- Recommended next: `WAIT_FOR_OPERATOR_SCOPE_APPROVAL`

---

## 1. Scope

Read-only scope-decision pass after baseline refresh **08** and accepted 1C import. Fix exact Neutral first-level show/hide/wait IDs for a **future** UI apply. No production mutation. No UI apply.

## 2. Operator approval

Operator approved this read-only decision pass before UI apply. Goal: hybrid first-level block scope — clean cards without legacy duplicates; mega unchanged; deep leaves excluded; empty copy reserved for true future 1C-backed empty first-level sections.

## 3. Client Ops boundary

Client Ops Telegram Reports, reporting bridge, Telegram bot, n8n, Hub Gateway — **untouched**. Monitor artifacts read only as SITE-002 evidence.

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `32ffc27b` (= `origin/mars/canonical-post-recovery`) |
| Origin includes `32ffc27b` | **yes** |
| Staged | empty |
| Unpushed | none |
| Untracked foreign tools (authority) | 3 pre-existing `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority unsafe | **NO** |

Evidence: Storage `preflight/`.

## 5. Reports read / current state

| Source | Key fact |
|--------|----------|
| Run 4.311 | Post-1C first-level charter — scope decision needed; 15/5 composition; empty copy agreed |
| Run 4.312 | Baseline **1879**; checkpoint `…-1879-08`; monitor after **NO_ACTION_REQUIRED** |
| This task | Operator approved scope-decision; **no UI apply** |

Evidence: Storage `reports-read/`.

## 6. Latest import and monitor reconfirm

| Check | Result |
|-------|--------|
| Latest TXT | `mars_1c_import_2026-07-28_080011.txt` |
| Status | **SUCCESS** |
| Duration | `5.5 seconds` |
| Run ID | `mars-20260728-080001-24823ddf` |
| Later failed supersede | **False** |
| Newer SUCCESS import after baseline | **False** |
| Critical products canonical | **5/5** |
| Monitor after refresh 08 | `2026-07-28_15-23-10` / `NO_ACTION_REQUIRED` |
| Import/baseline gate for scope | **PASS** |

Evidence: Storage `latest-1c-import/`, `monitor-state/`.

## 7. Sitemap / public current check

| Metric | Value |
|--------|------:|
| Sitemap HTTP | **200** |
| Valid XML | **True** |
| Unique URL count | **1879** |
| Match baseline | **True** |
| Controls `/`, `/katalog/`, root 79, root 362 | HTTP **200** |
| Empty copy already live | **False** |
| Public `БЗПМ` / PHP Notice | none on controls |

First-level Neutral+Tech children: public HTTP **200** (see `public-http/first-level-children-http.csv`).

Evidence: Storage `sitemap/`, `public-http/`.

## 8. Neutral direct children inventory

Parent **79** — **15** active direct children.

### 10 curated / product-backed (SHOW)

| ID | Name | Subtree products |
|---:|------|-----------------:|
| 80 | Моечные ванны | 128 |
| 86 | Стеллажи | 600 |
| 207 | Зонты вытяжные | 67 |
| 301 | Столы | 520 |
| 322 | Подтоварники и подставки | 24 |
| 326 | Тележки сервировочные | 3 |
| 331 | Полки настенные и настольные | 160 |
| 354 | Тележки-шпильки и противни | 13 |
| 358 | Шкафы и лари | 8 |
| 360 | Кондитерский инвентарь | 10 |

Currently visible on home / `/katalog/` / mega (code authority): **yes** via `$neutral_hub_branch_ids` × products.

### 5 empty first-level candidates (HIDE/WAIT)

| ID | Name | Children | Subtree products | HTTP |
|---:|------|--------:|-----------------:|-----:|
| 82 | Подтоварники | 3 | 0 | 200 |
| 83 | Полки | 2 | 0 | 200 |
| 85 | Тележки | 4 | 0 | 200 |
| 87 | Столы производственные | 3 | 0 | 200 |
| 89 | Шкафы | 2 | 0 | 200 |

Currently visible on home / `/katalog/` / mega: **no**.

Evidence: Storage `neutral-direct-children/`.

## 9. Duplicate analysis

| Empty | Curated sibling(s) | Duplicate risk | all-15 show risk |
|------:|--------------------|----------------|------------------|
| 82 | 322 Подтоварники и подставки | **HIGH** | duplicate + empty misleading card |
| 83 | 331 Полки настенные и настольные | **HIGH** | duplicate + empty misleading card |
| 85 | 326 + 354 тележки… | **HIGH** | duplicate + empty misleading card |
| 87 | 301 Столы | **HIGH** | duplicate + empty misleading card |
| 89 | 358 Шкафы и лари | **HIGH** | duplicate + empty misleading card |

- `oc_mars_1c_category_map` hits for 82/83/85/87/89: **0**
- Full CommerceML GUID/path proof after latest import: **SAFE UNKNOWN** (XML full group parse not conclusive this run; map table empty)
- Would `all-15` produce duplicate cards: **YES**

Evidence: Storage `duplicate-analysis/`.

## 10. Tech controls

Direct children of **362**: **5** — 373, 364, 369, 368, 375.  
Empty **364** already shown. Recommendation: **KEEP_CURRENT_TECH_BEHAVIOR** — no scope change.

Evidence: Storage `tech-controls/`.

## 11. UI current state

| Surface | Current |
|---------|---------|
| Home / `/katalog/` | Catalog Section Tiles — Neutral whitelist×products; Tech DB children incl. empty |
| Mega menu | Same `buildHubChildCards` gates |
| Root 79 | Whitelist×products hub tiles |
| Root 362 | Includes empty hubs |
| Empty copy | Not present |

Evidence: Storage `ui-current-state/`.

## 12. Source code read-only

Touchpoints for **future** apply (not modified):

- `CategoryVisibility::$neutral_hub_branch_ids`
- `buildHubChildCards` / `buildCatalogSectionTileBlocks`
- Twig tile caption for empty copy
- Mega via `prepareMegamenuCategories` — **must stay unchanged** in hybrid apply
- Cache: `cache.*` minimal; `storage/modification/` only if OCMOD requires

Evidence: Storage `source-code-readonly/`.

## 13. Scope options

| Option | Result | Recommend |
|--------|--------|-----------|
| A all-15 | 15 cards; **HIGH** duplicate risk | No |
| B **hybrid** | Show 10 curated; hide 5 legacy empties | **Yes** |
| C status quo | Same 10 shown; no first-level restore path | No (does not satisfy operator) |

Evidence: Storage `scope-options/`.

## 14. Operator decision pack

**Recommended: HYBRID**

| Action | IDs |
|--------|-----|
| `SHOW_IN_FIRST_LEVEL_BLOCK` | **80, 86, 207, 301, 322, 326, 331, 354, 358, 360** |
| `HIDE_AS_LEGACY_DUPLICATE` / wait 1C proof | **82, 83, 85, 87, 89** |
| `KEEP_CURRENT_TECH_BEHAVIOR` | Tech children of **362** |
| Empty copy (future proven empties only) | `Ожидайте, товары скоро поступят.` |

Should any empty Neutral first-level be shown **now**? **No.**

Apply **not** performed. Requires explicit operator confirmation.

Evidence: Storage `operator-decision-pack/`.

## 15. Future apply charter draft

Draft only under `future-apply-charter/`:

- home + `/katalog/` only
- mega unchanged; deep leaves unchanged; tech unchanged
- Neutral uses approved show list; suppress 82/83/85/87/89
- empty copy only for future proven empty first-level
- no sitemap/baseline/importer changes expected
- cache clear only if deploy requires it

**Not executed.**

## 16. Future regression plan

Plan ready: home/`/katalog`/roots/mega/deep leaves/empty copy/critical PDPs/canonical cats/sitemap 1879/no PHP errors/no `БЗПМ`/mobile smoke.

Evidence: Storage `future-regression-plan/`.

## 17. Decision

| Field | Value |
|-------|-------|
| Scope decision | `HYBRID_RECOMMENDED` |
| Apply readiness | `READY_FOR_FIRST_LEVEL_BLOCK_APPLY_AFTER_OPERATOR_CONFIRMATION` |
| Recommended next | `WAIT_FOR_OPERATOR_SCOPE_APPROVAL` |
| Verdict | `SITE-002 FIRST-LEVEL BLOCK SCOPE DECISION COMPLETE — HYBRID RECOMMENDED` |

## 18. Regression

All mutation checks **0**. See Storage `regression/`.

## 19. Production mutation summary

- production DB writes: **0**
- production FTP writes: **0**
- source/code changes: **0**
- template changes: **0**
- cache clear: **0**
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

## 20. Git/worktree summary

| Item | Value |
|------|-------|
| Authority | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| HEAD at start | `32ffc27b` |
| Dirty main | inspected read-only; not mutated |
| Commit/push | report/docs only (this closeout) |

## 21. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-FIRST-LEVEL-BLOCK-SCOPE-DECISION-01\`

Subfolders populated: preflight, reports-read, latest-1c-import, db-readonly, sitemap, monitor-state, public-http, neutral-direct-children, duplicate-analysis, tech-controls, ui-current-state, source-code-readonly, scope-options, operator-decision-pack, future-apply-charter, future-regression-plan, decision, regression, reports, manifests, logs.

## 22. SAFE UNKNOWN / blockers

- Exact CommerceML GUID/path presence for empty **82/83/85/87/89** after latest import: **SAFE UNKNOWN** (map table **0**; full XML group parse not conclusive).
- CSV `in_sitemap` column in this run may under-match SEO URL forms; authority for presence remains live sitemap count **1879** + HTTP **200** + prior Run 4.311 inventory.
- No blockers to **scope decision**. Apply still waits operator confirmation.

## 23. Final verdict

`SITE-002 FIRST-LEVEL BLOCK SCOPE DECISION COMPLETE — HYBRID RECOMMENDED`

## 24. Next recommendation

1. Operator confirms HYBRID show/hide lists (or marks overrides in decision CSV).  
2. Then charter/execute **first-level block apply** from `future-apply-charter/` (separate operation).  
3. Do **not** show 82/83/85/87/89 until 1C proof or explicit override.
