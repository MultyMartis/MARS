# REPORT — SITE-002 1C Canonical Leaf Apply 01

**Operation:** `SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01`  
**OCPilot run:** **4.295**  
**Date:** 2026-07-23  
**Environment:** PRODUCTION_1C_CANONICAL_LEAF_APPLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01\`

**Final verdict:** `SITE-002 1C CANONICAL LEAF APPLY COMPLETE — LEAVES CREATED AND PRODUCTS MOVED`

**Classifications:**
- Leaf apply: `LEAF_APPLY_COMPLETE`
- Products: `PRODUCTS_MOVED_TO_CANONICAL_LEAVES`
- Future importer: `READY_FOR_MAPPING_BACKFILL_NEXT`

---

## 1. Scope

Controlled Production apply after Run **4.294**:

1. Create **3** missing canonical tech leaf categories.
2. Move **4** products from temporary hub placement to those leaves.
3. Do **not** delete/disable legacy categories **153/154/159/165**.
4. Do **not** patch importer; do **not** baseline refresh.
5. Preserve rollback SQL with concrete new category IDs.

## 2. Operator approval / GUID stability

- Operator approved controlled apply after Run **4.294**.
- Operator confirmed 1C group GUIDs are treated as stable (operators try to keep them stable).
- Goal: OpenCart structure aligned to 1C canonical leaf paths; later importer automation by GUID/path.

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `009a150b` (= `origin/mars/canonical-post-recovery`) |
| Origin includes charter `009a150b` | **yes** |
| Staged | empty |
| Untracked tools (authority) | 3 foreign verification `.py` — **not committed**; apply helper **is** in scope |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority commit safety | **SAFE** for exact report/docs/SQL commit |

Evidence: Storage `preflight/`.

## 4. Reports read / apply baseline

Charter Run **4.294** verdict: `READY FOR LEAF APPLY`.

| Leaf | Parent | SEO keyword | Products |
|------|--------|-------------|----------|
| Мясорубки | 373 | `myasorubki-tehnologicheskoe` | 4707, 4708 |
| Пилы для мяса | 373 | `pily-dlya-myasa-tehnologicheskoe` | 4710 |
| Хлеборезки | 375 | `hleborezki-tehnologicheskoe` | 4712 |

4709 stays on **376**. Legacy **154/159/165** not deleted. Same leaf slugs as legacy rejected (keywords taken).

Evidence: Storage `reports-read/`.

## 5. DB before

Fresh SSH MySQL SELECT gates:

| Gate | Result |
|------|--------|
| Parents 373/375 active | **PASS** |
| Proposed SEO keywords free | **PASS** |
| Products in expected hubs | **PASS** (4707/4708/4710→373; 4712→375; 4709→376) |
| Canonical leaves absent under 373/375 | **PASS** (only child of 373 was 376) |
| Max `category_id` before | **377** |

Evidence: Storage `db-before/`.

## 6. Public before

Hub/product/home/katalog/sitemap sampled. No hard health failure for apply gate.

Evidence: Storage `public-before/`.

## 7. Sitemap before

Live sitemap sampled before apply. New leaf URLs absent (as expected). Product URLs still under hub paths.

Evidence: Storage `sitemap-before/`.

## 8. Dry-run SQL

Dry-run apply + rollback generated (transaction; `LAST_INSERT_ID` vars; includes `oc_category_to_store` for store visibility).

Marked: `DRY RUN ONLY — DO NOT APPLY MANUALLY OUTSIDE THIS OPERATION`.

Repo copies: `reports/artifacts/SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01/`.

## 9. HITL gates

All required gates **PASS** → decision **APPLY**.

| Gate | Pass |
|------|------|
| Operator approved apply | yes |
| GUID stability confirmed | yes |
| Parents active | yes |
| SEO keywords free | yes |
| Products in hubs | yes |
| Leaves absent | yes |
| Exact DB backup | yes (before apply) |
| Rollback SQL | yes |
| SQL scope exact | yes |
| Health / authority safe | yes |

Evidence: Storage `hitl-gates/`.

## 10. DB backup

Exact row snapshots before apply (categories/parents/legacy/products/relations/seo/path/max ids). Credentials not stored.

Evidence: Storage `db-backup/`.

## 11. DB apply

Applied in transaction via remote SQL batch.

### New category IDs

| ID | Name | Parent | SEO keyword |
|----|------|--------|-------------|
| **378** | Мясорубки | 373 | `myasorubki-tehnologicheskoe` |
| **379** | Пилы для мяса | 373 | `pily-dlya-myasa-tehnologicheskoe` |
| **380** | Хлеборезки | 375 | `hleborezki-tehnologicheskoe` |

### Product moves

| Product | From | To |
|---------|------|----|
| 4707 | 373 | **378** |
| 4708 | 373 | **378** |
| 4710 | 373 | **379** |
| 4712 | 375 | **380** |
| 4709 | 376 | **376** (unchanged) |

Tables touched: `oc_category`, `oc_category_description`, `oc_category_to_store`, `oc_category_path`, `oc_seo_url`, `oc_product_to_category`.

Row counts: **3** new categories; **main_ok=true**.

Evidence: Storage `db-apply/`.

## 12. Cache actions

Cleared only `/home/a/assum/bzpm.ru/storage/cache/cache.*` (16→0).  
`storage/modification/` **not** touched. OCMOD refresh **0**.

Evidence: Storage `cache/`.

## 13. Public after

| URL class | Status |
|-----------|--------|
| New leaf PLPs (3) | **200** |
| Product PDPs under leaf paths | **200**, no «Товар не найден» |
| Hub paths rewrite to leaf product paths | **200** (seo_pro path rebuild) |
| Parent hubs 373/375 | **200** |
| Legacy 154/159/165 URLs | **200** (still present, empty) |
| `/`, `/katalog/`, `/blog/`, sitemap | **200** |
| PHP notices / `БЗПМ` | **none** on sampled pages |

Evidence: Storage `public-after/`.

## 14. Sitemap after

- Count: **1820** unique (no duplicates).
- New leaf category + product URLs present under canonical leaf paths.
- Example: `.../myasorubki-tehnologicheskoe/myasorubka-tc-12`, `.../pily-dlya-myasa-tehnologicheskoe/pila-dlya-myasa-na-kosti-jg-210a`, `.../hleborezki-tehnologicheskoe/hleborezka-tt-d7c`.

Baseline refresh: **not performed**.

Evidence: Storage `sitemap-after/`.

## 15. Monitor after

Baseline refresh forbidden. ONBOARDING_REQUIRED may remain (baseline **1737** vs live sitemap growth). Not a leaf-apply failure.

Evidence: Storage `monitor-after/`.

## 16. Regression

| Channel | Result |
|---------|--------|
| FTP writes | **0** |
| Admin saves | **0** |
| Import runs | **0** |
| Scheduler changes | **0** |
| Monitor baseline | **0** |
| Forms/mail | untouched |
| OCMOD refresh | **0** |
| Category deletes/disables | **0** |
| Importer code | **0** |
| Dirty main mutations | **0** |

Evidence: Storage `regression/`.

## 17. Production mutation summary

- **DB writes:** yes — exact creates/moves listed above
- **new category_ids:** **378**, **379**, **380**
- **product moves:** 4707/4708→378; 4710→379; 4712→380; 4709 unchanged
- **FTP writes:** 0
- **Admin saves:** 0
- **Import runs:** 0
- **Scheduler changes:** 0
- **Monitor baseline changes:** 0
- **Category deletes/disables:** 0
- **Source deploys:** 0
- **Cache clears:** `/home/a/assum/bzpm.ru/storage/cache/cache.*`
- **OCMOD refresh:** 0
- **Dirty main changes:** 0

## 18. Rollback plan

Concrete rollback: Storage + repo `rollback.sql` / `reports/artifacts/.../rollback.sql`.

Restores hub relations (373/375) and deletes category/description/path/store/seo rows for **378/379/380**.

Do **not** run unless operator charters rollback.

## 19. Git/worktree summary

- Authority used for all report/docs commits.
- Dirty main inspected read-only only.
- Runtime checkout not mutated for baseline.

## 20. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01\` with all required subfolders + `manifests/operation.json`.

Tool: `projects/ocpilot/sites/site-002/tools/site-002-prod-1c-canonical-leaf-apply-01.py`.

## 21. SAFE UNKNOWN / blockers

- Beget full-backup ID from prior operator statement: **SAFE UNKNOWN** (not supplied); exact operation DB backup created.
- Whether next scheduled 1C import would re-attach products to legacy **154/159/165** until importer patch: **still a residual risk** (known; mapping backfill + importer patch next).
- Monitor artifact conflict / ONBOARDING_REQUIRED: may remain — not blockers for this apply.

## 22. Final verdict

`SITE-002 1C CANONICAL LEAF APPLY COMPLETE — LEAVES CREATED AND PRODUCTS MOVED`

## 23. Next recommendation

1. **Mapping backfill** — GUID → category_id for new leaves **378/379/380** (+ hubs already known).
2. **Importer patch** — GUID/path resolution; never tech-leaf → legacy **154/159/165** by name.
3. Keep baseline refresh deferred until operator charters it (live sitemap now **1820** vs baseline **1737**).
4. Legacy empty leaves **154/159/165** cleanup remains deferred.
