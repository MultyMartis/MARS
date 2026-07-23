# REPORT — SITE-002 Catalog Structure Forensic 01

**Operation:** `SITE-002-PROD-CATALOG-STRUCTURE-FORENSIC-01`  
**OCPilot run:** **4.289**  
**Date:** 2026-07-23  
**Environment:** PRODUCTION_CATALOG_STRUCTURE_FORENSIC_READONLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CATALOG-STRUCTURE-FORENSIC-01\`

**Final verdict:** `SITE-002 CATALOG STRUCTURE FORENSIC COMPLETE — 1C MAPPING REVIEW REQUIRED`

**Classifications (summary):**
- Product: `PRODUCT_JG210A_1C_DB_MISMATCH` + `PRODUCT_JG210A_LEGACY_PUBLIC_PATH_CONFIRMED`
- 1C: `ONE_C_SOURCE_PLACES_PRODUCT_IN_MYASOPERERABATYVAYUSHCHEE`
- DB: `DB_PRODUCT_IN_ELEKTROMEHANICHESKOE`
- Public: `PUBLIC_PRODUCT_ONLY_LEGACY_PATH` + `PUBLIC_EMPTY_TECH_ELEKTROMEHANICHESKOE_CONFIRMED`
- Sitemap: empty tech elektro + legacy elektro + legacy PDP present; live **1817** vs baseline **1737**
- Menu/tiles: `MENU_TILES_NEED_CLEANUP` (points to empty tech elektro)
- Legacy: `LEGACY_DEMO_CLEANUP_CANDIDATES_FOUND`
- Monitor: `MONITOR_ARTIFACT_CONFLICT` (operational truth = onboarding required)

---

## 1. Scope

Read-only forensic of SITE-002 catalog structure after operator report from Алексей:

- Product `Пила для мяса на кости JG 210A` should be under **Мясоперерабатывающее**, not legacy **Электромеханическое оборудование**
- Mega menu / tiles link to empty `.../tehnologicheskoe-oborudovanie/elektromehanicheskoe`
- Legacy `.../elektromehanicheskoe-oborudovanie` still holds products

No production mutation. Cleanup plan is dry-run only.

## 2. Operator request

Confirm 1C→DB→public placement for JG 210A; explain empty tech elektro vs legacy elektro; list legacy/empty cleanup candidates; prepare HITL-gated cleanup plan without applying changes.

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `af5f3fca` (= `origin/mars/canonical-post-recovery`) |
| Origin includes `af5f3fca` / `62d82eb6` | yes |
| Staged | empty |
| Untracked tools (authority) | 3 foreign verification `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority commit safety | **SAFE** for exact report/docs commit |

Evidence: Storage `preflight/`.

## 4. Recent state / reports read

| Item | State |
|------|--------|
| Checkpoint | `SITE-002-STABLE-PROD-POST-1C-MONITOR-BASELINE-1737-04` |
| Run 4.288 | baseline **1714→1737**; manual `2026-07-20_22-32-43` `NO_ACTION_REQUIRED` |
| Runs 4.285–4.287 | tech tiles + polish/images + mega children (empty tech hubs may show) |
| Run 4.282 / 4.283 | product routing hotfix / mega cache — **do not break** |
| Limitation | mega menu one-level; baseline frozen at 1737 until approved refresh |

Evidence: Storage `reports-read/`.

## 5. Standard SITE-002 healthcheck

| Field | Value |
|-------|--------|
| Latest scheduled monitor | `2026-07-23_12-30-03` |
| Latest 1C import | `mars_1c_import_2026-07-23_080010.txt` |
| Import status | **SUCCESS** · Step1/Step2 **PASS** · Duration **7.96s** (step1 4.2s / step2 3.75s) |
| Source files | `import0_1.xml`, `offers0_1.xml` |
| Live sitemap | **1817** URLs · HTTP 200 · duplicates 0 · public `БЗПМ` 0 |
| Brand / literal `\\n` on sampled pages | clean |

## 6. Monitor artifacts consistency

| Artifact | Classification / metric |
|----------|-------------------------|
| `monitor-classification.json` | `ONBOARDING_REQUIRED` (needs **4**) |
| `run.log` | `ONBOARDING_REQUIRED` |
| `run-summary.json` | **`NO_ACTION_REQUIRED`** ← conflict |
| Metrics (all agree) | baseline **1737** → current **1817**; added **80**; removed **0**; needs **4** |

**Classification:** `MONITOR_ARTIFACT_CONFLICT`  
**Operational truth:** treat as **ONBOARDING_REQUIRED** (prefer classification JSON + run.log + metrics).

Onboarding needs (4):
1. `/katalog/tehnologicheskoe-oborudovanie/elektromehanicheskoe` (empty tech elektro — also forensic target)
2. `/katalog/tehnologicheskoe-oborudovanie/hlebopekarnoe/testoraskatki`
3. `/katalog/tehnologicheskoe-oborudovanie/myasopererabatyvayuschee/slaysery-dlya-myasa`
4. `/katalog/nejtralnoe-oborudovanie/stellazhi/stellazhi-standart/stellazhi-standart-vysota-1600-reshetchatye-polki`

Added URLs include target PDP under **legacy** elektro path and empty tech elektro PLP.

Evidence: Storage `monitor-artifacts/`.

## 7. 1C import logs/files forensic

| Field | Value |
|-------|--------|
| Latest report | `mars_1c_import_2026-07-23_080010.txt` |
| Source XML | `public_html/1c_incoming/webdata/import0_1.xml` |
| Product | present — Артикул `JG 210A` · 1C id `56ccee94-e203-11ea-a988-a85e4515c4f4` |
| Product group id | `95003163-7c1a-11f1-aecc-581122cf362c` = **Пилы для мяса** |
| 1C nest | `ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ` → `Мясоперерабатывающее` → `Пилы для мяса` |
| Sibling under myaso | `Мясорубки`, `Слайсеры для мяса` |
| Tech `Электромеханическое` in 1C | present; child `Хлеборезки` |
| Legacy name `Электромеханическое оборудование` in 1C classifier | **not** found as current group name |

**Classification:** `ONE_C_SOURCE_PLACES_PRODUCT_IN_MYASOPERERABATYVAYUSHCHEE`

Evidence: Storage `1c-artifacts/`.

## 8. Target product DB forensic

| Field | Value |
|-------|--------|
| product_id | **4710** |
| name | Пила для мяса на кости JG 210A |
| model | JG 210A |
| xml_id | `56ccee94-e203-11ea-a988-a85e4515c4f4` (matches 1C) |
| status / qty | 1 / 7 |
| date_added | 2026-07-21 05:00:05 |
| date_modified | 2026-07-23 05:00:03 |
| categories | **only** `159` Пилы для мяса |
| path | `Электромеханическое оборудование (153) > Пилы для мяса (159)` |
| SEO keyword | `pila-dlya-myasa-na-kosti-jg-210a` |

`oc_category` has **no** xml_id/GUID column — category matching cannot use 1C group UUID directly.

**Classification:** `DB_PRODUCT_IN_ELEKTROMEHANICHESKOE`

Evidence: Storage `db-readonly/`, `product-forensic/`.

## 9. Target product public URL forensic

| URL | Status | Notes |
|-----|--------|-------|
| Legacy PDP (current) | **200** | canonical = legacy elektro path; H1 correct |
| Tech empty elektro | **200** | H1 Электромеханическое; **0** product cards |
| Legacy elektro PLP | **200** | products present; target link present |
| Myaso hub | **200** | cards present (slaysery branch); target PDP **not** listed there |
| Probed myaso PDP paths | **200** | **canonical still legacy elektro** |

**Classifications:** `PUBLIC_PRODUCT_ONLY_LEGACY_PATH`, `PUBLIC_EMPTY_TECH_ELEKTROMEHANICHESKOE_CONFIRMED`

Evidence: Storage `public-http/`.

## 10. Sitemap forensic

| Metric | Value |
|--------|--------|
| HTTP / valid XML | 200 / yes |
| URL count | **1817** (delta from baseline 1737 = **+80**) |
| Duplicates | 0 |
| Target legacy PDP | present |
| Empty tech elektro | present |
| Legacy elektro category | present |
| Myaso hub | present |
| Product under myaso path | **absent** |

**Classifications:** `SITEMAP_EMPTY_CATEGORY_PRESENT`, `SITEMAP_LEGACY_CATEGORY_PRESENT`, `SITEMAP_PRODUCT_LEGACY_URL_PRESENT`, `SITEMAP_CURRENT_DELTA_FROM_BASELINE`

Evidence: Storage `sitemap/`.

## 11. Menu/tile blocks forensic

Home / katalog / tech hub HTML contain links to:

- `.../tehnologicheskoe-oborudovanie/elektromehanicheskoe` (**empty**)
- tech hubs including Мясоперерабатывающее
- legacy elektro surfaces still reachable from catalog structure

Consistent with Run **4.287** policy: empty active tech hubs may show.

**Classifications:** `MENU_POINTS_TO_EMPTY_TECH_ELEKTROMEHANICHESKOE`, `TILES_POINT_TO_EMPTY_TECH_ELEKTROMEHANICHESKOE`, `MENU_TILES_NEED_CLEANUP`

Evidence: Storage `menu-tiles/`.

## 12. Category tree / legacy demo candidates

| ID | Name | Path | Products | Risk |
|----|------|------|----------|------|
| 153 | Электромеханическое оборудование | legacy root | subtree **4** | KEEP_HAS_PRODUCT_DESCENDANTS + NEEDS_1C_MAPPING_REVIEW |
| 159 | Пилы для мяса | under 153 | **1** (JG 210A) | KEEP_HAS_PRODUCTS + NEEDS_REDIRECT_PLAN |
| 154 / 165 | Мясорубки / Хлеборезки | under 153 | 2 / 1 | same collision pattern |
| 362 | Технологическое оборудование | tech root | subtree 17 | KEEP_STRUCTURAL_HUB |
| 373 | Мясоперерабатывающее | under 362 | subtree 1 (slaysery only) | KEEP_STRUCTURAL_HUB |
| 376 | Слайсеры для мяса | under 373 | 1 | KEEP_HAS_PRODUCTS (unique name — mapped correctly) |
| 375 | Электромеханическое | under 362 | **0 / 0** | SAFE_CANDIDATE_DISABLE **or** populate from 1C |

Empty active categories overall: **158** (many are structural/neutral; do not mass-disable).

**Classification:** `LEGACY_DEMO_CLEANUP_CANDIDATES_FOUND`

Evidence: Storage `legacy-demo-candidates/`, `category-forensic/`.

## 13. Root cause analysis

1. **1C says Myaso → Пилы для мяса; DB/public say legacy Elektro → Пилы для мяса.**
2. Public SEO path follows assigned category **159** under **153**.
3. Dominant mechanism: **category name collision / name-based import matching** to pre-existing leaf **159**. Supporting pattern: uniquely named `Слайсеры для мяса` landed under tech **373**, while reused names (`Пилы для мяса`, `Мясорубки`, `Хлеборезки`) stayed under legacy **153**.
4. Tech **375** is empty because 1C child products were not attached under the new tech elektro branch.
5. Menu/tiles/sitemap expose both empty **375** and live legacy **153** simultaneously.
6. Safest sequence: confirm with Алексей → fix GUID mapping or controlled reparent → redirects → only then disable empties → never delete **153/159** while products/URLs remain.

Evidence: Storage `risks/`.

## 14. Cleanup plan

Levels 0–4 documented in Storage `cleanup-plan/cleanup-plan.md` and `operator-decision-table.csv`.

**Do not apply in this run.** Prefer fixing 1C→OC category identity (GUID) before mass relation edits.

## 15. Dry-run artifacts

| File | Purpose |
|------|---------|
| `dry-run/proposed-category-disable.sql` | optional disable **375** (commented) |
| `dry-run/proposed-product-category-relation-review.sql` | review/reparent **4710** (commented) |
| `dry-run/proposed-redirects.csv` | 301 candidates after reparent |
| `dry-run/no-apply-confirmation.md` | mutation = 0 |

All marked **DRY RUN ONLY — DO NOT APPLY**.

## 16. Risks and HITL gates

| Gate | Required before |
|------|-----------------|
| HITL-1 | Accept 1C/DB mismatch reading |
| HITL-2 | Choose importer GUID fix vs manual reparent |
| HITL-3 | Approve redirect map |
| HITL-4 | Approve any category disable (esp. **375** vs empty-hub policy 4.287) |
| HITL-5 | Approve any delete |
| Safety | Do not break Run 4.282 product routing / 4.283 mega cache; no admin cache cleaner / OCMOD; no baseline refresh here |

SEO risk: indexed legacy PDP/PLP URLs; soft-404 empty **375** in sitemap/menu.

## 17. Production mutation summary

- FTP writes: **0**
- DB writes: **0**
- Admin saves: **0**
- Import runs: **0**
- Scheduler changes: **0**
- Monitor baseline changes: **0**
- Form/mail changes: **0**
- Cache clears: **0**
- OCMOD refresh: **0**
- Dirty main changes: **0**

## 18. Git/worktree summary

| Item | Value |
|------|--------|
| Authority branch | `site-002-git-authority-realign-after-wave-e` @ `af5f3fca` |
| Dirty main | inspected read-only only |
| This commit | report + docs only (exact paths) |

## 19. Storage artifacts

Root: `...\deployments\SITE-002-PROD-CATALOG-STRUCTURE-FORENSIC-01\`

Subfolders populated: `preflight`, `reports-read`, `monitor-artifacts`, `1c-artifacts`, `db-readonly`, `product-forensic`, `category-forensic`, `public-http`, `sitemap`, `menu-tiles`, `legacy-demo-candidates`, `cleanup-plan`, `dry-run`, `risks`, `reports`, `manifests`, `logs`.

## 20. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Exact Sergey importer PHP name-match code path on Production | SAFE UNKNOWN (behavior inferred from schema + outcomes; FTP source map not fully traced this run) |
| Whether next import would recreate wrong link after manual reparent without GUID fix | HIGH RISK / needs verification charter |
| Authority commit | not blocked |
| Production mutation | none |

## 21. Final verdict

**SITE-002 CATALOG STRUCTURE FORENSIC COMPLETE — 1C MAPPING REVIEW REQUIRED**

Cleanup plan is ready as dry-run, but product placement cannot be corrected safely without HITL decision on **1C category identity mapping** (GUID) and/or controlled reparent + redirects.

## 22. Next recommendation

1. HITL with Алексей: confirm XML path is authoritative (evidence already strong).
2. Charter **SITE-002-PROD-1C-CATEGORY-GUID-MAPPING-REVIEW-01** (or equivalent): inspect `import_1C.php` category match logic; propose GUID persistence on categories.
3. Parallel charter candidate: controlled reparent of **4710** (+ review **154/165**) under **373**, then redirects, then revisit empty **375**.
4. Separate onboarding charter for the other 3 monitor needs (meta), without baseline refresh until placement wave settles.
5. Do **not** delete legacy **153** while subtree products remain.
