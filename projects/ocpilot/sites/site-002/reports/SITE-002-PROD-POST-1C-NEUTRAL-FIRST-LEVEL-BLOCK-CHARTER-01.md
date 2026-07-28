# REPORT — SITE-002 Post-1C Neutral First-Level Block Charter 01

**Operation ID:** `SITE-002-PROD-POST-1C-NEUTRAL-FIRST-LEVEL-BLOCK-CHARTER-01`  
**OCPilot Run:** **4.311**  
**Date:** 2026-07-28  
**Environment:** PRODUCTION (`https://bzpm.ru/`) — **READ-ONLY**  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-POST-1C-NEUTRAL-FIRST-LEVEL-BLOCK-CHARTER-01\`

**Verdict:** `SITE-002 POST-1C FIRST-LEVEL BLOCK CHARTER ATTENTION — OPERATOR SCOPE DECISION NEEDED`

**Classifications:**
- Post-import: `LATEST_1C_IMPORT_SUCCESS_CONFIRMED`
- Block readiness: `NEEDS_OPERATOR_DECISION_ON_BLOCK_SCOPE`
- Recommended next: `PREPARE_BLOCK_SCOPE_DECISION`

---

## 1. Scope

Read-only post-1C-import pass and future implementation charter for restoring a **first-level category sections** block (including empty 1C-present sections with copy `Ожидайте, товары скоро поступят.`).

No UI apply. No production mutation. No mega-menu / importer / sitemap / baseline change.

---

## 2. Operator decision

Earlier: parent/first-level sections block existed, then was replaced by curated product branches.

Now operator wants:

- restore a block of **first-level** sections;
- include sections that exist in current 1C / live taxonomy even if empty;
- empty card text: `Ожидайте, товары скоро поступят.`;
- do **not** globally expose deep empty leaves;
- do **not** clutter mega menu;
- re-check latest natural 1C import before planning apply.

---

## 3. Client Ops boundary

Client Ops Telegram Reports, reporting bridge, Telegram bot, n8n, Hub Gateway — **untouched**.  
Monitor artifacts read only as SITE-002 evidence.

---

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `fe2daa66` (= `origin/mars/canonical-post-recovery`) |
| Origin includes `fe2daa66` | **yes** |
| Staged | empty |
| Unpushed | none |
| Untracked foreign tools (authority) | 3 pre-existing `.py` — **not committed** |
| Dirty main | foreign WIP (incl. Client Ops) — **read-only**; **0 mutations** |

Evidence: Storage `preflight/`.

---

## 5. Reports read / current state

| Run | Used fact |
|-----|-----------|
| 4.306 / 4.307 | Parent **153** + demo **154–170** deleted; baseline **1836** accepted; monitor clean |
| 4.308 / 4.309 | Empty review + HITL; **60** Wait-1C under root **79** |
| 4.310 | Deep empty leaves under 79 are sitemap/HTTP-only; hidden by Launch Mode + product gate; tech **362** already shows empty hubs |
| 4.285–4.287 | Catalog Section Tiles + megamenu automation; neutral whitelist + `require_products` |

New operator UX direction **overrides** Run 4.310 default `KEEP_CURRENT_BEHAVIOR` for a **future** apply charter — this run plans only.

Evidence: Storage `reports-read/`.

---

## 6. Latest 1C import check

| Field | Value |
|-------|-------|
| Classification | `LATEST_1C_IMPORT_SUCCESS_CONFIRMED` |
| New import after Run 4.310 | **yes** |
| Latest TXT | `mars_1c_import_2026-07-28_080011.txt` |
| Timestamp (filename local) | 2026-07-28 08:00:11 |
| Final status | **SUCCESS** |
| Duration | 5.5 seconds |
| Run ID | `mars-20260728-080001-24823ddf` |
| Critical products canonical | **5/5** (4707/4708→378, 4709→376, 4710→379, 4712→380) |
| Critical `date_modified` | 2026-07-28 05:00:0x (touched by today's import) |

Hard gate: import SUCCESS + critical persistence OK → UI planning **allowed** (apply still blocked on operator scope).

Evidence: Storage `latest-1c-import/`.

---

## 7. Current sitemap and monitor check

| Metric | Value |
|--------|------:|
| Live sitemap count | **1879** |
| Previous baseline (Run 4.307) | **1836** |
| Delta vs baseline | **+43** net (monitor: +49 / −6) |
| Latest monitor run | `2026-07-28_13-31-41` |
| Monitor classification | `HYGIENE_REVIEW_REQUIRED` |
| Added page types | PRODUCT_PDP × 49 |
| Onboarding needs | 0 |
| Baseline refresh this op | **not done / forbidden** |

First-level block planning uses **live** DB/sitemap. Baseline refresh / hygiene review remain **separate** ops.

Evidence: Storage `sitemap/`, `monitor-state/`.

---

## 8. DB read-only first-level inventory

Definitions:

| Def | Meaning | Count now |
|-----|---------|----------:|
| A | Site roots `parent_id=0` status=1 | **9** |
| B | Launch roots **79**, **362** | **2** |
| C | Direct children of **79** | **15** |
| D | Direct children of **362** | **5** |

Launch-visible roots remain **79** + **362**. Other site roots stay hidden by Launch Mode (`hidden_root_slugs`).

Evidence: Storage `first-level-inventory/`.

---

## 9. Neutral analysis

Direct children of **79** (15):

| Class | IDs / names | Notes |
|-------|-------------|-------|
| Curated whitelist with products (shown today) | 207, 360, 80, 322, 331, 86, 301, 326, 354, 358 | current Catalog Section Tiles |
| Empty first-level (not in whitelist) | **82** Подтоварники; **83** Полки; **85** Тележки; **87** Столы производственные; **89** Шкафы | candidates for empty copy |

Deep empty leaves under 79: **62** (was ~60 in Run 4.310). **0** of them are direct children of 79.

### Critical scope finding (operator decision)

Empty first-level names largely **overlap conceptually** with curated product branches:

| Empty first-level | Curated sibling (has products) |
|-------------------|--------------------------------|
| 82 Подтоварники | 322 Подтоварники и подставки |
| 83 Полки | 331 Полки настенные и настольные |
| 85 Тележки | 326 / 354 тележки… |
| 87 Столы производственные | 301 Столы |
| 89 Шкафы | 358 Шкафы и лари |

Showing **all 15** may restore “first-level” look but create **duplicate section cards**. Safer apply needs operator pick:

1. **All active direct children of 79** (including empty legacy names + copy); or  
2. **Whitelist-only + empty message never applies** (status quo); or  
3. **Hybrid:** keep curated branches; add only empty first-level that are true 1C hubs without curated sibling (none clear today without extra 1C XML path proof).

`oc_mars_1c_category_map` hits on these neutral first-level rows: **0** (map historically tech-focused). “1C-present” for planning = **active live taxonomy after today's SUCCESS import**, not GUID map proof. Exact GUID/path presence for empty 82/83/85/87/89 = **SAFE UNKNOWN** until apply charter parses latest `import0_1.xml` groups.

Evidence: Storage `neutral-analysis/`.

---

## 10. Tech analysis

Direct children of **362** (5): 373, 364, 369, 368, 375.

- Empty already shown: **364** Посуда и инвентарь (`require_products=false`).
- Recommendation: **keep tech special behavior unchanged** in the first apply.

Evidence: Storage `tech-analysis/`.

---

## 11. Public/UI current state

| Surface | Current behavior |
|---------|------------------|
| Home / `/katalog/` | Catalog Section Tiles via `buildCatalogSectionTileBlocks` — neutral = whitelist × products; tech = DB children incl. empty |
| Mega menu | Same helper gates for section hubs |
| Root 79 page | Section hub tiles (same helper) |
| Root 362 page | Empty hubs already visible |
| Empty copy `Ожидайте…` | **not** present on checked pages |
| Deep empty leaves | Reachable by URL; not intended as home/katalog tiles |

Note: automated href substring matching over-reports empty-child links on home; treat **code gates + Run 4.310** as authority for “currently shown” (whitelist only for neutral).

Evidence: Storage `ui-current-state/`, `public-http/`.

---

## 12. Source code read-only

Primary authority: `system/library/zpm/category_visibility.php` (repo mirror `tools/category_visibility.php`).

| Gate | Effect |
|------|--------|
| `LAUNCH_MODE` + `visible_root_category_ids = [79,362]` | Only two Launch roots |
| `$neutral_hub_branch_ids` whitelist | Curated neutral tiles |
| `require_products=true` (neutral) | Hides empty whitelist cards |
| `require_products=false` (tech 362+) | Shows empty first-level hubs |
| `prepareMegamenuCategories` | Parity with tiles |

Future touchpoints (not executed): helper ± tile Twig for `empty_message`; **not** mega by default; **not** importer/sitemap/baseline.

Evidence: Storage `source-code-readonly/`.

---

## 13. Future block plan

**Recommended interpretation:** restore **neutral first-level = direct children of 79** on **home + `/katalog/`** (and optionally neutral root page via same helper).

**Empty behavior:** if eligible and `subtree_product_count==0`, still show card linking to category URL with caption:

`Ожидайте, товары скоро поступят.`

**Do not change:** mega menu (default), deep leaves, sitemap, importer, monitor baseline, product assignment, CSS `.category__view` hide unless separately approved.

**Future apply phases:** preflight → reconfirm import/DB → helper/Twig change → cache if needed → public smoke → sitemap/monitor expectation (UI-only) → rollback previous helper/Twig.

**Blocked on:** operator scope decision (all 15 vs hybrid vs keep curated-only), especially duplicate legacy/curated pairs.

Evidence: Storage `future-block-plan/`.

---

## 14. Future copy plan

| Rule | Value |
|------|-------|
| Exact text | `Ожидайте, товары скоро поступят.` |
| When | `count` / subtree products == 0 on eligible first-level card |
| Placement | card caption under title (recommended) |
| Plural variants | not needed |
| Meta/title | **no** |

Evidence: Storage `future-copy-plan/`.

---

## 15. Future regression plan

Must cover: home, `/katalog/`, root 79, root 362 unchanged, mega unchanged, critical PDPs, no PHP errors, no `БЗПМ`, no literal `\n`, mobile smoke if practical, sitemap/monitor expectations (baseline refresh separate).

Evidence: Storage `future-regression-plan/`.

---

## 16. Decision

| Axis | Classification |
|------|----------------|
| Post-import status | `LATEST_1C_IMPORT_SUCCESS_CONFIRMED` |
| Block readiness | `NEEDS_OPERATOR_DECISION_ON_BLOCK_SCOPE` |
| Recommended next | `PREPARE_BLOCK_SCOPE_DECISION` |

Operator must confirm before apply charter:

1. Scope = **all direct children of 79** vs **hybrid avoiding curated duplicates** vs **status quo**.  
2. Placements = home + `/katalog/` (recommended); mega **unchanged**.  
3. Exact empty copy string (already provided).  
4. Tech 362 = leave as-is (recommended).

---

## 17. Regression

All mutation counters **0**. See Storage `regression/`.

---

## 18. Production mutation summary

- DB writes: 0  
- FTP writes: 0  
- source/code changes: 0  
- cache clear: 0  
- import runs: 0  
- scheduler changes: 0  
- monitor baseline changes: 0  
- category/product changes: 0  
- redirect changes: 0  
- `.htaccess` changes: 0  
- importer/source changes: 0  
- mapping changes: 0  
- image changes: 0  
- Client Ops changes: 0  
- n8n changes: 0  
- Telegram changes: 0  
- dirty main changes: 0  

---

## 19. Git/worktree summary

| Item | Value |
|------|-------|
| Authority | `X:\AI MARS STORAGE\git-sync-e01\repo` @ `fe2daa66` (pre-commit) |
| Dirty main | inspected only; not mutated |
| Commit scope | report + OCPilot docs only (this wave) |

---

## 20. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-POST-1C-NEUTRAL-FIRST-LEVEL-BLOCK-CHARTER-01\`

Subfolders populated: preflight, reports-read, latest-1c-import, db-readonly, sitemap, monitor-state, public-http, first-level-inventory, neutral-analysis, tech-analysis, ui-current-state, source-code-readonly, future-block-plan, future-copy-plan, future-regression-plan, decision, regression, reports, manifests, logs.

---

## 21. SAFE UNKNOWN / blockers

- Exact CommerceML GUID/path presence for empty neutral first-level **82/83/85/87/89** (map table 0; XML not re-parsed this run).  
- Whether operator wants duplicate legacy+curated cards or hybrid.  
- Monitor `HYGIENE_REVIEW_REQUIRED` / baseline **1836→1879** needs separate ops — not a UI-block blocker.  
- Home href auto-match for empty children is noisy; UI “shown” authority remains code gates.

**Blockers for apply:** operator scope decision (required). Import recovery: **not** required.

---

## 22. Final verdict

`SITE-002 POST-1C FIRST-LEVEL BLOCK CHARTER ATTENTION — OPERATOR SCOPE DECISION NEEDED`

---

## 23. Next recommendation

1. Operator answers scope questions in §16.  
2. Then prepare `SITE-002-PROD-*-FIRST-LEVEL-BLOCK-APPLY-01` (helper ± Twig only).  
3. Separately: monitor hygiene / baseline refresh for sitemap **1879** (not part of UI apply).  
4. Do **not** expose deep empty leaves; do **not** change mega menu in the first apply.
