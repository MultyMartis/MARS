# REPORT — SITE-002 1C Category Mapping Backfill 01

**Operation:** `SITE-002-PROD-1C-CATEGORY-MAPPING-BACKFILL-01`  
**OCPilot run:** **4.296**  
**Date:** 2026-07-23  
**Environment:** PRODUCTION_1C_CATEGORY_MAPPING_BACKFILL  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-CATEGORY-MAPPING-BACKFILL-01\`

**Final verdict:** `SITE-002 1C CATEGORY MAPPING BACKFILL COMPLETE — READY FOR IMPORTER PATCH`

**Classifications:**
- Backfill: `MAPPING_TABLE_CREATED_AND_BACKFILLED`
- Verification: `MAPPING_BACKFILL_VERIFIED`
- Importer readiness: `READY_FOR_IMPORTER_GUID_PATH_PATCH`

---

## 1. Scope

Controlled Production apply after Run **4.295**:

1. Create mapping table `oc_mars_1c_category_map` (absent → created).
2. Backfill **7** confirmed 1C GUID/path → OpenCart `category_id` rows.
3. Do **not** move products; do **not** change categories/SEO; do **not** patch importer; do **not** refresh baseline.
4. Preserve rollback SQL by exact `source_group_id`.

## 2. Operator approval / GUID stability

- Operator approved mapping-layer backfill after Run **4.295**.
- Operator confirmed 1C group GUIDs are treated as stable (operators try to keep them stable).
- Goal: identity layer so next import does not return products to legacy categories by leaf-name collision.

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `f06dedd2` (= `origin/mars/canonical-post-recovery`) |
| Origin includes leaf apply `f06dedd2` | **yes** |
| Staged | empty |
| Untracked tools (authority) | 3 foreign verification `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority commit safety | **SAFE** for exact report/docs/SQL/tool commit |

Evidence: Storage `preflight/`.

## 4. Reports read / backfill baseline

Runs **4.292–4.295** summarized in Storage `reports-read/backfill-baseline-summary.md`.

Required scope (CSV): Storage `reports-read/target-mapping-scope.csv` — category IDs **362/373/375/376/378/379/380**.

## 5. XML evidence

Source: prior live XML from Run **4.293** (`import0_1.xml`, 10 637 418 bytes) copied into this operation Storage.

| GUID | Full path | OC ID |
|------|-----------|-------|
| `e0fd5c42-…c4f4` | ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ | **362** |
| `2adc2489-…362c` | … → Мясоперерабатывающее | **373** |
| `bac3dc26-…362c` | … → Электромеханическое | **375** |
| `e0b6bb6d-…362c` | … → Слайсеры для мяса | **376** |
| `7e43262d-…362c` | … → Мясорубки | **378** |
| `95003163-…362c` | … → Пилы для мяса | **379** |
| `41a86281-…362c` | … → Хлеборезки | **380** |

All **7/7** XML gates **PASS** (GUID present, parent matches, path contains expected leaf).

Evidence: Storage `xml-evidence/`.

## 6. DB before

| Gate | Result |
|------|--------|
| Table `oc_mars_1c_category_map` exists | **no** (create required) |
| Existing mapping conflicts | **none** |
| Targets 362/373/375/376/378/379/380 active | **PASS** |
| Legacy 154/159/165 present | yes — **not** used as active mapping targets |

Evidence: Storage `db-before/`.

## 7. Harness before

Critical products already on canonical leaves (post **4.295**). No DB GUID mapping yet.

| Product | Current category |
|---------|------------------|
| 4707 / 4708 | **378** |
| 4709 | **376** |
| 4710 | **379** |
| 4712 | **380** |

Evidence: Storage `harness-before/`.

## 8. Dry-run SQL

Generated:

- `CREATE TABLE IF NOT EXISTS oc_mars_1c_category_map` (proposed schema)
- `INSERT … ON DUPLICATE KEY UPDATE` for 7 GUIDs
- confidence `HIGH_GUID_AND_PATH`, status `active`
- No active legacy mappings for 154/159/165

Repo copies: `reports/artifacts/SITE-002-PROD-1C-CATEGORY-MAPPING-BACKFILL-01/`.

Marked: `DRY RUN ONLY — DO NOT APPLY MANUALLY OUTSIDE THIS OPERATION`.

## 9. HITL gates

All required gates **PASS** → decision **APPLY**.

| Gate | Pass |
|------|------|
| Operator approved backfill | yes |
| GUID stability confirmed | yes |
| Source GUIDs present | yes |
| Target categories active | yes |
| Exact rows | yes (7) |
| No GUID conflicts | yes |
| No wrong legacy mapping | yes |
| Rollback SQL | yes |
| Exact DB backup | yes |
| Health / authority safe | yes |

Evidence: Storage `hitl-gates/`.

## 10. DB backup

Backup schema/row snapshot + target/legacy category reference + focus product relations fingerprint.

Evidence: Storage `db-backup/`, `rollback/rollback.sql`.

## 11. DB apply

Applied via SSH MySQL batch transaction.

| Field | Value |
|-------|-------|
| Table created | **yes** (`oc_mars_1c_category_map`) |
| Target rows | **7** |
| Table total | **7** |
| Confidence | `HIGH_GUID_AND_PATH` |
| Status | `active` |

Note: first apply batch **succeeded**; immediate post-apply `mysql -e` verification hit bash backtick expansion (`command not found` on table name). Tool escaping fixed; `--resume-verify` confirmed all 7 rows and completed phases 10–13 without re-mutation.

Evidence: Storage `db-apply/`.

## 12. Harness after

Classification: **`MAPPING_BACKFILL_VERIFIED`**

| Check | Result |
|-------|--------|
| 362/373/375/376/378/379/380 GUID maps | **PASS** |
| 4707/4708 source → 378 | **PASS** |
| 4710 source → 379 | **PASS** |
| 4712 source → 380 | **PASS** |
| 4709 source → 376 | **PASS** |
| Tech GUID → legacy 154/159/165 | **none** |

Evidence: Storage `harness-after/`.

## 13. Public read-only check

10 URLs (home, katalog, leaves 378/379/380, sitemap, critical products): HTTP **200**; 0 `БЗПМ`; 0 PHP Notice/Warning/Fatal; 0 `Товар не найден`.

Evidence: Storage `public-readonly/`.

## 14. Monitor read-only

| Field | Value |
|-------|-------|
| Baseline | still **1737** (not refreshed) |
| Live sitemap `<url>` count | **1820** |
| Import triggered | **no** |
| ONBOARDING_REQUIRED / artifact conflict | may remain (expected) |

Evidence: Storage `monitor-readonly/`.

## 15. Regression

| Check | Result |
|-------|--------|
| DB writes limited to mapping table | **PASS** |
| Product/category relations unchanged | **PASS** (0 changes) |
| No FTP/admin/import/scheduler/baseline/source/cache | **PASS** |
| Dirty main untouched | **PASS** |

Evidence: Storage `regression/`.

## 16. Production mutation summary

| Item | Value |
|------|-------|
| DB writes | **yes** — table `oc_mars_1c_category_map` + **7** rows |
| Created table | **yes** |
| Backfilled rows | **7** |
| Product/category relation changes | **0** |
| Category creates/updates/deletes/disables | **0** |
| SEO URL changes | **0** |
| FTP writes | **0** |
| Admin saves | **0** |
| Import runs | **0** |
| Scheduler changes | **0** |
| Monitor baseline changes | **0** |
| Source deploys | **0** |
| Cache clears | **0** |
| OCMOD refresh | **0** |
| Dirty main changes | **0** |

## 17. Rollback plan

1. `DELETE FROM oc_mars_1c_category_map WHERE source_group_id IN (<7 GUIDs>);`
2. If table empty and created only by this operation: optional `DROP TABLE oc_mars_1c_category_map;`

SQL: Storage `rollback/rollback.sql` and repo `reports/artifacts/.../dry-run-rollback.sql`.

## 18. Git/worktree summary

- Authority HEAD before commit: `f06dedd2`
- Dirty main: inspect-only
- Commit scope: report + docs + tool + dry-run/rollback SQL artifacts (exact paths)

## 19. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-CATEGORY-MAPPING-BACKFILL-01\`

Subfolders populated: preflight, reports-read, xml-evidence, db-before, harness-before, dry-run, hitl-gates, db-backup, db-apply, rollback, harness-after, public-readonly, monitor-readonly, regression, reports, manifests, logs.

## 20. SAFE UNKNOWN / blockers

- Broader high-confidence tech/neutral GUID backfill beyond the **7** confirmed rows: **not** applied (deferred; REVIEW_REQUIRED for ambiguous cases).
- Harness tool still primarily path/leaf based; it does not yet consume `oc_mars_1c_category_map` as primary GUID lookup (importer patch is the consumer).
- Persistence of product placement after next natural 1C import: **not yet proven** until importer GUID/path patch lands.
- Monitor baseline still **1737** vs live **1820** — expected ONBOARDING_REQUIRED until separate baseline refresh charter.

No blockers for this backfill verdict.

## 21. Final verdict

**SITE-002 1C CATEGORY MAPPING BACKFILL COMPLETE — READY FOR IMPORTER PATCH**

## 22. Next recommendation

1. Patch 1C importer to: **GUID map → full path → create under parent → collision guard → leaf-name only as review**.
2. Never map tech source groups to legacy **154/159/165**.
3. After importer patch: observe one natural import; then consider baseline refresh + optional broader mapping backfill for remaining HIGH_FULL_PATH rows.
