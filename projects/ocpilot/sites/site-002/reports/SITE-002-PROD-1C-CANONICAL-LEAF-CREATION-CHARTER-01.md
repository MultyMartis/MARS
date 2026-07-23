# REPORT — SITE-002 1C Canonical Leaf Creation Charter 01

**Operation:** `SITE-002-PROD-1C-CANONICAL-LEAF-CREATION-CHARTER-01`  
**OCPilot run:** **4.294**  
**Date:** 2026-07-23  
**Environment:** PRODUCTION_1C_CANONICAL_LEAF_CREATION_CHARTER_READONLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-CANONICAL-LEAF-CREATION-CHARTER-01\`

**Final verdict:** `SITE-002 1C CANONICAL LEAF CREATION CHARTER COMPLETE — READY FOR LEAF APPLY`

**Classifications:**
- Leaf readiness: `LEAF_CREATION_PLAN_READY`
- Automation plan: `AUTOMATIC_CATEGORY_CREATION_DESIGN_READY`
- Next phase: `READY_FOR_LEAF_CREATION_APPLY`
- Previous harness: Run **4.293** / commit `90b7005c`

---

## 1. Scope

Documentary / planning charter for:

1. Creating three missing canonical tech leaf categories under 1C structure.
2. Moving critical products from interim hubs to those leaves.
3. Designing future importer automatic category creation (GUID/path, not leaf-name).
4. Ordering later mapping-table backfill and importer patch **after** leaves exist.

No production mutation. No category create. No product moves. No importer code change.

## 2. Operator approval

After Run **4.293**, operator approved preparing this charter so structure can be brought to 1C canon and future automation can create/assign categories by GUID/path — avoiding legacy same-name collisions (154/159/165).

## 3. Strategic automation requirement

Manual leaf maintenance is interim only. Final direction:

- read 1C group GUID + parent GUID + full path;
- map GUID → `category_id` when known;
- else full-path match;
- else create under correct parent with deterministic SEO keyword;
- never attach tech-tree source leaf to legacy 154/159/165 by name alone;
- emit import report (created / matched / collisions / review).

Design: Storage `future-automation/` + repo artifacts under `reports/artifacts/SITE-002-PROD-1C-CANONICAL-LEAF-CREATION-CHARTER-01/`.

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `90b7005c` (= `origin/mars/canonical-post-recovery`) |
| Origin includes harness commit `90b7005c` | **yes** |
| Staged | empty |
| Untracked tools (authority) | 3 foreign verification `.py` — **not committed** |
| Dirty main | foreign WIP (~583 short-status lines) — **read-only**; **0 mutations** |
| Authority commit safety | **SAFE** for exact report/docs/dry-run commit |

Evidence: Storage `preflight/`.

## 5. Evidence base

From Runs **4.289–4.293**:

| Fact | Status |
|------|--------|
| Leaf-name collision | **CONFIRMED** |
| 1C GUIDs + full paths | **AVAILABLE** |
| Run 4.290 moved products to hubs | **DONE** (4707/4708/4710→373; 4712→375; 4709→376) |
| Run 4.293: canonical leaves missing | **CONFIRMED** |
| Old importer risk | **REMAINS** (→154/159/165) |
| Mapping backfill before leaf create | **RISKY** (would encode hub interim) |
| Future automation | **REQUIRED** |

Evidence: Storage `reports-read/`.

## 6. XML evidence for missing leaves

| Leaf | Source GUID | Parent GUID | Parent OC | Products |
|------|-------------|-------------|-----------|----------|
| Мясорубки | `7e43262d-7c1a-11f1-aecc-581122cf362c` | `2adc2489-…` | **373** | 4707, 4708 |
| Пилы для мяса | `95003163-7c1a-11f1-aecc-581122cf362c` | `2adc2489-…` | **373** | 4710 |
| Хлеборезки | `41a86281-7c1b-11f1-aecc-581122cf362c` | `bac3dc26-…` | **375** | 4712 |

Path root: `ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ` (`e0fd5c42-…` → OC **362**).  
Canonical leaf **Слайсеры для мяса** already exists as **376**.  
Legacy same-name: **154 / 159 / 165** under **153**.

Evidence: Storage `xml-evidence/` (harness-derived; raw XML not committed).

## 7. DB readonly / SEO inputs

Fresh SSH `mysql` SELECT-only (9 queries). DB writes: **0**.

| ID | Role | SEO keyword | Direct / subtree products | Children |
|----|------|-------------|---------------------------|----------|
| 373 | hub | `myasopererabatyvayuschee` | 3 / 4 | only **376** |
| 375 | hub | `elektromehanicheskoe` | 1 / 1 | none |
| 376 | leaf OK | `slaysery-dlya-myasa` | 1 / 1 | — |
| 154/159/165 | legacy | `myasorubki` / `pily-dlya-myasa` / `hleborezki` | **0 / 0** | empty after 4.290 |

Critical relations still hub-placed: 4707/4708/4710→373; 4712→375; 4709→376.

Evidence: Storage `db-readonly/`.

## 8. SEO URL plan

Legacy leaf keywords are **taken**. `oc_seo_url.keyword` index is non-unique, but reusing the same keyword risks ambiguous decode.

**Recommended unique keywords:**

| Leaf | Keyword | Expected URL |
|------|---------|--------------|
| Мясорубки | `myasorubki-tehnologicheskoe` | `/katalog/tehnologicheskoe-oborudovanie/myasopererabatyvayuschee/myasorubki-tehnologicheskoe` |
| Пилы для мяса | `pily-dlya-myasa-tehnologicheskoe` | `/katalog/tehnologicheskoe-oborudovanie/myasopererabatyvayuschee/pily-dlya-myasa-tehnologicheskoe` |
| Хлеборезки | `hleborezki-tehnologicheskoe` | `/katalog/tehnologicheskoe-oborudovanie/elektromehanicheskoe/hleborezki-tehnologicheskoe` |

Clean same-slug reuse **rejected** while legacy keywords remain active.  
Redirects legacy→tech: **deferred**.

Evidence: Storage `seo-url-plan/`; conflict check CSV shows candidates free.

## 9. Leaf creation plan

Create **3** active categories:

| Logical key | Name | Parent | Sort | Image | Meta |
|-------------|------|--------|------|-------|------|
| `NEW_LEAF_MYASORUBKI` | Мясорубки | 373 | 10 | empty OK | minimal stub |
| `NEW_LEAF_PILY` | Пилы для мяса | 373 | 20 | empty OK | minimal stub |
| `NEW_LEAF_HLEBOREZKI` | Хлеборезки | 375 | 10 | empty OK | minimal stub |

Do **not** delete legacy. Tables on future apply: `oc_category`, `oc_category_description`, `oc_category_to_store`, `oc_category_path`, `oc_seo_url`.

Evidence: Storage `leaf-plan/`; repo `reports/artifacts/.../new-leaves.csv`.

## 10. Product hub-to-leaf move plan

| Product | From | To |
|---------|------|----|
| 4707, 4708 | 373 | `NEW_LEAF_MYASORUBKI` |
| 4710 | 373 | `NEW_LEAF_PILY` |
| 4712 | 375 | `NEW_LEAF_HLEBOREZKI` |
| 4709 | 376 | **KEEP** |

Strategy: replace single hub relation with leaf `main_category=1`. Rollback: restore hub rows from backup.

**Persistence warning:** without importer fix, next 1C import can still revert to legacy by leaf name.

## 11. Sitemap / menu / tile policy

| Surface | Expectation |
|---------|-------------|
| Sitemap | New leaves after products assigned; baseline still **1737** until refresh |
| Mega menu | One-level under 362 — new leaves are grandchildren; hubs remain anchors |
| Parent child tiles | Yes on 373/375 PLP; empty image fallback OK |
| Hub product list | Likely via subtree — confirm on apply postcheck |
| Legacy empty leaves | Defer cleanup |

## 12. Future automatic category creation design

Precedence:

1. GUID mapping table  
2. Full-path match  
3. Create under resolved parent  
4. Collision guard (block tech→legacy name match)  
5. Leaf-name-only → review only (no auto-assign)

Auto-create writes category + path + unique SEO keyword + mapping row + `CATEGORY_CREATED_REVIEW_REQUIRED`.  
Product assign uses GUID/path map; uncertain → hold or hub + review.  
Report fields documented in Storage `future-automation/import-report-fields.md`.

**Recommended order:** leaf apply → product move → mapping backfill (including new leaf ids) → importer patch → later legacy/redirects.

## 13. Dry-run examples

Commented SQL/CSV templates only (all files start with `DRY RUN ONLY — DO NOT APPLY`):

- `reports/artifacts/SITE-002-PROD-1C-CANONICAL-LEAF-CREATION-CHARTER-01/dry-run-create-leaves.sql`
- `dry-run-move-products.sql`
- `dry-run-rollback.sql`
- `dry-run-mapping-backfill.csv`
- `no-apply-confirmation.md`

**Not applied.**

## 14. Risks

- SEO conflict if legacy keywords reused  
- Wrong path rows  
- Importer still unbroken → next import revert  
- Meta/image polish backlog  
- Legacy redirects deferred  
- Monitor baseline stale  
- GUID confirm HITL before durable map  

Full list: Storage `risks/risks.md`.

## 15. HITL gates

Before future apply:

1. Operator confirms leaves/parents  
2. Алексей/1C GUID/path stability  
3. Exact SEO keywords/URLs  
4. Exact product moves  
5. Backup  
6. Dry-run SQL reviewed  
7. Rollback reviewed  
8. Importer fix order / import-hold policy  
9. Legacy cleanup deferred  

## 16. Production mutation summary

- FTP writes: **0**
- DB writes: **0**
- Admin saves: **0**
- Import runs: **0**
- Scheduler changes: **0**
- Monitor baseline changes: **0**
- Category creates/updates/deletes/disables: **0**
- Product/category relation changes: **0**
- Source deploys: **0**
- Cache clears: **0**
- OCMOD refresh: **0**
- Dirty main changes: **0**

## 17. Git/worktree summary

| Item | Value |
|------|--------|
| Authority | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Start HEAD | `90b7005c` |
| Dirty main | inspected only; not mutated |
| Commit scope | report + docs + dry-run planning artifacts only |

## 18. Storage artifacts

Root: `.../deployments/SITE-002-PROD-1C-CANONICAL-LEAF-CREATION-CHARTER-01/`

Subfolders: `preflight`, `reports-read`, `xml-evidence`, `db-readonly`, `seo-url-plan`, `leaf-plan`, `product-move-plan`, `sitemap-menu-policy`, `future-automation`, `dry-run`, `risks`, `reports`, `manifests`, `logs`.

## 19. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Live `seo_url.php` path-decode proof for duplicate keywords | SAFE UNKNOWN — unique keywords chosen to avoid risk |
| Parent hub PLP exact descendant product inclusion | SAFE UNKNOWN — confirm on apply postcheck |
| Alexey formal GUID sign-off | HITL gate (not charter evidence block — live XML GUIDs present) |
| Blockers for charter completeness | **none** |

## 20. Final verdict

`SITE-002 1C CANONICAL LEAF CREATION CHARTER COMPLETE — READY FOR LEAF APPLY`

## 21. Next recommendation

1. HITL approve names/URLs/moves (+ Alexey GUID confirm).  
2. Controlled **leaf creation apply** wave (3 categories + SEO + path).  
3. Controlled **product hub→leaf move** for 4707/4708/4710/4712.  
4. Mapping-table backfill including new leaf GUIDs.  
5. Importer identity + auto-create patch.  
6. Defer legacy cleanup/redirects and monitor baseline refresh.
