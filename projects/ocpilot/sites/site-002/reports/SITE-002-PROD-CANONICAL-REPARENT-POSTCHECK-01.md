# REPORT — SITE-002 Canonical Reparent Postcheck 01

**Operation:** `SITE-002-PROD-CANONICAL-REPARENT-POSTCHECK-01`  
**OCPilot run:** **4.291**  
**Date:** 2026-07-23  
**Environment:** PRODUCTION_CANONICAL_REPARENT_POSTCHECK_READONLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CANONICAL-REPARENT-POSTCHECK-01\`

**Final verdict:** `SITE-002 CANONICAL REPARENT POSTCHECK COMPLETE — CONFIRMED GROUP MOVED, PERSISTENCE NOT YET PROVEN`

**Classifications:**
- Reparent completeness: `CONFIRMED_GROUP_FULLY_REPARENTED`
- DB: `REPARENT_COMPLETE_FOR_CONFIRMED_GROUP`
- Persistence: `PERSISTENCE_NOT_YET_PROVEN` / `PERSISTENCE_NOT_TESTED_NO_NEW_IMPORT`
- Legacy cleanup readiness: `LEGACY_CLEANUP_READY_FOR_EMPTY_ONLY` (leaves 154/159/165) — **only after** importer persistence proven; root 153 still has 17 active children
- Monitor: `MONITOR_ONBOARDING_REQUIRED_EXPECTED` + `MONITOR_ARTIFACT_CONFLICT_STILL_PRESENT`

---

## 1. Scope

Read-only postcheck after Run **4.290** to verify that the full confirmed 1C canonical duplicate group was reparented (not only JG 210A), that legacy leaves are empty, that public/sitemap reflect the move, whether a newer 1C import already risked reverting relations, and to list remaining duplicate/legacy candidates plus next safe steps.

No production mutation in this run.

## 2. Operator clarification

JG 210A was only an example. Goal is order across the confirmed same-name collision pattern where 1C canonical placement differs from legacy/public DB placement.

Run 4.290 already moved four confirmed products; 4709 Слайсер intentionally untouched (already correct under 376).

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `a9bd825b` (= previous apply commit / expected origin tip at start) |
| Origin includes `a9bd825b` | yes (fetch performed) |
| Staged | empty |
| Untracked tools (authority) | 3 foreign verification `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority commit safety | **SAFE** for exact report/docs commit |

Evidence: Storage `preflight/`.

## 4. Reports read / baseline

### Did Run 4.290 include more than JG 210A?

**YES.** Full confirmed group of four products.

| product_id | name | from | to | moved? |
|------------|------|------|----|--------|
| 4707 | Мясорубка TC-12 | 154 | **373** | yes |
| 4708 | Мясорубка TC-22 | 154 | **373** | yes |
| 4710 | Пила JG 210A | 159 | **373** | yes |
| 4712 | Хлеборезка ТТ-D7C | 165 | **375** | yes |
| 4709 | Слайсер ТТ-М29С | 376 | 376 | **no** (already correct) |

### Risks carried from 4.290

1. Importer name-collision / missing category GUID may reattach to legacy leaves on next import.
2. Canonical leaves under 373/375 not created — products sit on hubs.
3. Legacy disable deferred.
4. Monitor baseline still **1737**.

Evidence: Storage `reports-read/`.

## 5. DB postcheck

**Classification:** `REPARENT_COMPLETE_FOR_CONFIRMED_GROUP`

| product_id | category_ids | path |
|------------|--------------|------|
| 4707 | **373** only | Технологическое → Мясоперерабатывающее |
| 4708 | **373** only | same |
| 4710 | **373** only | same |
| 4712 | **375** only | Технологическое → Электромеханическое |
| 4709 | **376** only | … → Слайсеры для мяса |

| category_id | direct | subtree | notes |
|-------------|--------|---------|-------|
| 154 / 159 / 165 | **0** | **0** | empty legacy leaves |
| 153 | **0** | **0** | no products; **17** active children remain |
| 373 | **3** | **4** | TC-12/TC-22/JG + child 376 |
| 375 | **1** | **1** | Хлеборезка |
| 376 | **1** | **1** | Слайсер OK |

- No moved product remains on legacy leaf.
- No evidence of import revert in current relations.

Evidence: Storage `db-readonly/`.

## 6. Latest 1C import / persistence check

| Field | Value |
|-------|--------|
| Latest report | `mars_1c_import_2026-07-23_080010.txt` |
| Dir | `storage/mars-tools/cron/reports/` |
| Status | **SUCCESS** |
| Local time | **2026-07-23 08:00:10** |
| Reparent apply ~ | **2026-07-23 18:37** |
| Import after reparent? | **NO** |
| Source XML | `public_html/1c_incoming/webdata/import0_1.xml` (products found) |

**Classification:** `PERSISTENCE_NOT_TESTED_NO_NEW_IMPORT` → **`PERSISTENCE_NOT_YET_PROVEN`**

Evidence: Storage `1c-artifacts/`, `persistence-risk/`.

## 7. Public HTTP postcheck

| URL / target | Status | Result |
|--------------|--------|--------|
| myaso hub | 200 | lists JG 210A, TC-12, TC-22 |
| tech elektro hub | 200 | lists Хлеборезка ТТ-D7C |
| PDP 4707/4708/4710 | 200 | canonical under myaso hub |
| PDP 4712 | 200 | canonical under tech elektro |
| PDP 4709 | 200 | under slaysery leaf |
| legacy elektro + leaves 154/159/165 | 200 | **0** product cards / needles absent |
| `/katalog/`, `/` | 200 | OK |
| `Товар не найден` | — | **0** on sampled PDPs |
| public `БЗПМ` / literal `\n` | — | **0** on sampled pages |

Evidence: Storage `public-http/`.

## 8. Sitemap postcheck

| Metric | Value |
|--------|-------|
| Count | **1817** |
| Duplicates | **0** |
| Baseline | **1737** (not refreshed) |
| 4707/4708/4710/4712 URLs | tech paths present; legacy elektro PDP paths for these products **absent** |
| Legacy category URLs | still present (categories not deleted) |
| Canonical hubs | present |

Evidence: Storage `sitemap/`.

## 9. Monitor artifacts

| Field | Value |
|-------|--------|
| Latest run | `2026-07-23_12-30-03` (**before** reparent) |
| classification JSON / run.log | `ONBOARDING_REQUIRED` |
| run-summary.json | `NO_ACTION_REQUIRED` ← **conflict** |
| baseline → current | **1737 → 1817** (+80 / −0) |
| needs | **4** (elektro tech, testoraskatki, slaysery, stellazhi-1600) |

**Classification:** `MONITOR_ONBOARDING_REQUIRED_EXPECTED` + `MONITOR_ARTIFACT_CONFLICT_STILL_PRESENT`

Note: next scheduled monitor may change need #1 now that **375** has a product.

Evidence: Storage `monitor-artifacts/`.

## 10. Remaining duplicates / legacy candidates

Active same-name pair count under both 153 and 362 paths: **0** (tech leaves for Пилы/Мясорубки/Хлеборезки were never created).

Collision pattern remains: 1C wants those leaf names under tech, while empty legacy leaves **154/159/165** still exist as name-match targets.

| Candidate | Risk |
|-----------|------|
| 154 / 159 / 165 empty | `ALREADY_FIXED_CONFIRMED_GROUP` + `LEGACY_EMPTY_DISABLE_CANDIDATE` + `NEEDS_IMPORTER_IDENTITY_FIX` |
| 373 / 375 hubs holding products | `CANONICAL_LEAF_MISSING_PRODUCTS_ON_HUB` |
| 376 Слайсеры | `KEEP_STRUCTURAL` |
| 153 root (0 products, 17 children) | empty of products but not ready for blunt disable |

Evidence: Storage `remaining-duplicates/`.

## 11. Persistence risk

**HIGH until next successful post-reparent import preserves 373/375 relations.**

Root cause unchanged: `oc_category` has no GUID/`xml_id`; importer likely matches by leaf name → legacy 154/159/165 remain collision targets.

## 12. Recommended next plan

1. **Importer category identity fix** (GUID mapping / path-aware match / explicit collision map) — highest priority.
2. Optional controlled wave: create canonical leaves under 373/375 and move products hub→leaf.
3. After persistence proven: disable empty legacy leaves 154/159/165; optional 301; never delete with descendants.
4. Monitor: no baseline refresh yet; fix artifact conflict separately; re-check onboarding after next monitor.

Evidence: Storage `next-plan/`.

## 13. Production mutation summary

| Item | Value |
|------|-------|
| FTP writes | **0** |
| DB writes | **0** |
| Admin saves | **0** |
| Import runs | **0** |
| Scheduler changes | **0** |
| Monitor baseline changes | **0** |
| Category deletes/disables | **0** |
| Product/category relation changes | **0** |
| Cache clears | **0** |
| OCMOD refresh | **0** |
| Dirty main changes | **0** |

## 14. Git/worktree summary

| Item | Value |
|------|--------|
| Authority | report/docs commit intended on authority worktree |
| Dirty main | inspected read-only only |
| Storage collector scripts | under deployment `logs/` only — not committed |

## 15. Storage artifacts

Root: `...\deployments\SITE-002-PROD-CANONICAL-REPARENT-POSTCHECK-01\`

Populated: `preflight`, `reports-read`, `db-readonly`, `1c-artifacts`, `public-http`, `sitemap`, `monitor-artifacts`, `remaining-duplicates`, `persistence-risk`, `next-plan`, `reports`, `manifests`, `logs`.

## 16. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Exact Beget backup ID from 4.290 | SAFE UNKNOWN (unchanged) |
| Broader same-name collisions outside 153↔362 | SAFE UNKNOWN without wider audit |
| Post-reparent scheduled monitor | not yet observed |
| Snippet parent-path proximity in raw XML | weak in light extract; rely on Run 4.289/4.290 forensic mapping |

## 17. Final verdict

**SITE-002 CANONICAL REPARENT POSTCHECK COMPLETE — CONFIRMED GROUP MOVED, PERSISTENCE NOT YET PROVEN**

Run 4.290 handled the full confirmed group (not only JG 210A). DB/public/sitemap confirm canonical placement. No newer 1C import has tested persistence. Importer identity fix remains required before safe legacy cleanup.

## 18. Next recommendation

Charter **`SITE-002-PROD-1C-CATEGORY-GUID-MAPPING-REVIEW-01`** (or equivalent importer identity fix). Optionally plan leaf create under 373/375. Defer legacy disable until post-import persistence is proven. Keep monitor baseline at **1737**.
