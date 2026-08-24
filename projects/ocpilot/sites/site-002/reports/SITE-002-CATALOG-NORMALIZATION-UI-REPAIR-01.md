# REPORT — SITE-002 Catalog Normalization UI Repair 01

**Operation:** `SITE-002-CATALOG-NORMALIZATION-UI-REPAIR-01`
**Site:** SITE-002 / ЗПМ Production — `https://bzpm.ru/`
**Run:** 4.344
**Applied:** 2026-08-25 (local +07) / 2026-08-24T18:30Z UTC
**Prior apply:** `b0447bc8` — [SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01.md](SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01.md)
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-CATALOG-NORMALIZATION-UI-REPAIR-01\`

---

## 1. Scope

Bounded production UI repair after catalog normalization DB apply (Run 4.343):

- Repair public catalog/root tile presentation on `/` and `/katalog/`
- Align Launch Mode visibility layer to **8 approved public roots**
- Stop rendering Neutral **children** as the main catalog block
- Single-file deploy: `category_visibility.php` only

Forbidden scope respected: no DB hierarchy change, no import, no baseline refresh, no header/footer edit, no product/mapping mutation.

---

## 2. Operator visual issue

After Run 4.343 apply, operator reported homepage/catalog still showed:

- Section title: **«Нейтральное оборудование»**
- Tiles: Neutral first-level children (Зонты вытяжные, Кондитерский инвентарь, Моечные ванны, …)

Expected: **8 approved public root categories** as main catalog tiles.

---

## 3. Production repair boundary

| Class | Allowed | Actual |
|-------|---------|--------|
| FTP `category_visibility.php` | Yes | **1 file** |
| OpenCart cache clear | Yes | `cache.*` + `cat-list-header` |
| DB writes | No | **0** |
| PHP other files / Twig | No | **0** |
| header.twig / footer.twig | No | **0** |
| Import / baseline / monitor | No | **0** |

---

## 4. Authority preflight

| Check | Result |
|-------|--------|
| Worktree | `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo` |
| Branch | `docs/site002-offers-recovery-healthcheck-03` |
| HEAD | `b0447bc8` (prior apply commit present) |
| Origin | 1 commit ahead of local at preflight — ff before push required |
| Staged | Empty |
| Foreign WIP | `?? site-002-catalog-normalization-apply-combined-01.py` (not staged) |

Artifacts: `preflight/authority-git-state.txt`, `preflight/authority-origin-state.txt`

---

## 5. DB root state verification

**Verdict:** `DB_ROOT_STATE_CONFIRMED`

All 8 approved roots: `parent_id=0`, `status=1`, keywords match apply report.

Tmp disabled (`362`, `93`, `171`, `205`, `206`): `status=0`.

`[96]` Запчасти: unchanged `status=0`.

Artifacts: `db-verify/root-state-after-apply.csv`, `db-verify/db-verify-summary.md`

---

## 6. Public before / page identification

| Page | Section title (before) | Main tiles (before) |
|------|--------------------------|---------------------|
| `/` | Нейтральное оборудование | 15 Neutral children |
| `/katalog/` | Нейтральное оборудование | 15 Neutral children |

Operator screenshot matches **homepage catalog block** and **`/katalog/`** — same stale Launch Mode tile builder.

Approved 8 roots were **not** in the main tile block (only elsewhere in page HTML / nav).

Artifacts: `public-before/public-before-summary.md`, `public-before/page-tile-inventory.csv`

---

## 7. Render source diagnostic

**Selected source:** `/public_html/system/library/zpm/category_visibility.php`

**Root cause:**

- Stale `$visible_root_category_ids = array(79, 362)` (362 disabled after apply)
- `$hidden_root_slugs` hid newly public roots
- `buildCatalogSectionTileBlocks()` called `buildNeutralFirstLevelBlockCards()` for root `79` → Neutral **children** as tiles

**Consumers (unchanged):** `home.php`, `katalog.php`, `header.php` via `CategoryVisibility`.

Artifacts: `render-source-diagnostic/render-source-summary.md`, `render-source-diagnostic/selected-source.txt`

---

## 8. Exact fix plan

1. `$visible_root_category_ids` → `[79, 95, 90, 186, 375, 373, 364, 381]`
2. `$visible_root_slugs` → 8 approved SEO keywords
3. `$hidden_root_slugs` → tmp/disabled + legacy slugs + `zapchasti`
4. `buildCatalogSectionTileBlocks()` → **single section** «Каталог оборудования» with **8 root cards**
5. `CATALOG_PRIMARY_ENTRY` → `/katalog/`
6. `isVisibleRootCategory()` → reject hidden slugs

Artifacts: `exact-fix-plan/exact-fix-plan.md`

---

## 9. Backup / rollback

| Path | SHA-256 before | Backup |
|------|----------------|--------|
| `/public_html/system/library/zpm/category_visibility.php` | recorded | `file-backups/category_visibility.php.before` |

Rollback: restore backup file + clear cache.

Artifact: `rollback/rollback-plan.md`, `file-backups/file-backup-inventory.csv`

---

## 10. Production apply

Deployed mirror: `projects/ocpilot/sites/site-002/tools/category_visibility.php`

Post-upload hash verified on production.

Artifacts: `production-apply/apply-summary.md`, `production-apply/changed-files.csv`

---

## 11. Cache action

Cleared via SSH:

- `/home/a/assum/bzpm.ru/storage/cache/cache.*`
- `cache.cat-list-header` if present

OCMOD/modification: **not touched** (no modification overlay for this file confirmed by immediate UI delta).

Artifact: `cache/cache-action-summary.md`

---

## 12. Public after smoke

| Path | Status | Section title | Main tiles |
|------|--------|---------------|------------|
| `/` | 200 | Каталог оборудования | 8 approved roots (A→Я) |
| `/katalog/` | 200 | Каталог оборудования | 8 approved roots |
| 8 root URLs | 200 | — | hub children where applicable |
| `/tehnologicheskoe-oborudovanie` | 404 | — | expected |
| `/inventar` | 404 | — | expected |
| `/zapchasti` | 404 | — | unchanged hold |

No PHP fatal; no forbidden `БЗПМ` in checked titles.

Neutral children remain on **`/nejtralnoe-oborudovanie`** hub page (correct).

Artifacts: `public-after/public-after-summary.md`, `public-after/page-tile-inventory-after.csv`, `public-after/public-http-smoke.csv`

---

## 13. Visual smoke

**SAFE UNKNOWN** — no browser screenshots captured; HTML tile extraction confirms fix on `/` and `/katalog/`.

Artifact: `visual-smoke/visual-smoke-summary.md`

---

## 14. Regression / mutation summary

| Item | Value |
|------|-------|
| Category hierarchy changed | 0 |
| Product changes | 0 |
| Mapping changes | 0 |
| Import runs | 0 |
| Baseline refresh | 0 |
| `[96]` changed | 0 |
| header/footer touched | 0 |
| Files deployed | 1 |

Artifact: `regression/mutation-summary.csv`

---

## 15. Git/worktree summary

Docs/report commit from authority worktree after ff-merge with origin.

Apply helper: `site-002-catalog-normalization-ui-repair-01.py` (not committed — foreign WIP pattern for apply scripts).

Mirror updated: `category_visibility.php` in tools (Launch Mode 8-root model).

---

## 16. Storage artifacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-CATALOG-NORMALIZATION-UI-REPAIR-01\`

Manifest: `manifests/operation.json`

---

## 17. SAFE UNKNOWN / blockers

- Visual browser screenshots not captured (HTML smoke only)
- Beget backup for this wave: not independently verified (operator backup from prior apply still referenced)
- Mega menu drill-down visual: not manually screenshot-verified; logic uses same `CategoryVisibility` roots filter

**No blockers.**

---

## 18. Final verdict

**`SITE-002 CATALOG NORMALIZATION UI REPAIR COMPLETE — PUBLIC CATALOG ROOT UI SHOWS APPROVED 8 ROOTS`**

Decision tags:

- `SITE_002_CATALOG_NORMALIZATION_UI_REPAIR_COMPLETE`
- `DB_ROOT_STATE_CONFIRMED`
- `WRONG_NEUTRAL_CHILD_UI_CONFIRMED` (before)
- `CATALOG_ROOT_UI_REPAIRED`
- `APPROVED_8_ROOTS_VISIBLE`
- `TMP_DISABLED_ROOTS_ABSENT` (404 on legacy public URLs)
- `ZAPCHASTI_UNCHANGED`
- `BASELINE_REFRESH_PENDING`
- `PRODUCTION_MUTATION_BOUNDED`

---

## 19. Next recommendation

1. Operator visual confirm homepage + `/katalog/` + mega menu on desktop/mobile
2. Run **Apply 07** baseline refresh when chartered (sitemap live **1861** vs baseline **1887**)
3. Next 1C import — verify Upakovochnoe product assignment under `[381]`
4. Optional: retire deprecated `TECHNOLOGICAL_HUB_CATEGORY_ID = 362` constant in a future cleanup wave (non-blocking)
