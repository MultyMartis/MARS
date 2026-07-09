# REPORT — SITE-002 Parent Category Tiles Lari Removal

**Operation:** `SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01`  
**OCPilot run:** 4.236  
**Date:** 2026-07-09  
**Environment:** PRODUCTION controlled mutation — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01`  
**Checkpoint after:** `SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01`

---

## 1. Scope

Remove standalone **Лари** (category ID **88**) from **Parent Category Tiles / Витрина родительских категорий** on homepage and catalog surfaces, while keeping **Шкафы и лари** (ID **358**) and all nested **Лари** category/page/redirect behaviour from Run 4.235.

| Surface | Action |
|---------|--------|
| Homepage `zpm-cat-card` grid | Remove **Лари** tile; keep **Шкафы и лари** |
| Neutral hub `/katalog/nejtralnoe-oborudovanie` | Remove **Лари** tile; keep **Шкафы и лари** |
| `/katalog` | No standalone **Лари** in page tiles/megamenu; **Шкафы и лари** in megamenu |
| `/shkafy-i-lari` child list | **Лари** remains as child card |
| Nested `/shkafy-i-lari/lari` | **Unchanged** — 200, canonical nested |
| DB / SEO / redirects | **No changes** |

---

## 2. Terminology

**Parent Category Tiles / Витрина родительских категорий** — visual block of image card-buttons for neutral parent categories on homepage and catalog entry surfaces. Authority: `$neutral_hub_branch_ids` in `category_visibility.php` via `buildHomepageCategoryCards()` and neutral hub `hub_categories` loop.

**Not in scope:** megamenu-only structural nav (filtered separately), category deletion, reparent rollback, sitemap edits.

---

## 3. Pre-flight

| Check | Result |
|-------|--------|
| Workspace `X:\AI MARS` | PASS |
| Volume `X:` label `AI WS` | PASS |
| Branch `mars/canonical-post-recovery` | PASS |
| Staged files before task | empty — PASS |
| Foreign WIP | not staged / not touched |

---

## 4. Before snapshot

| Surface | HTTP | Parent tiles | Лари standalone | Шкафы и лари |
|---------|------|--------------|-----------------|--------------|
| Homepage | 200 | **11** `zpm-cat-card` | **yes** | yes |
| Neutral hub | 200 | **11** | **yes** | yes |
| `/katalog` | 200 | 1 root `zpm-cat-card` + megamenu | **no** (not on page content) | megamenu yes |
| `/shkafy-i-lari` | 200 | — | child **yes** | hub page |

**Before whitelist IDs:** `322, 331, 301, 326, 354, 358, 207, 80, 86, 88, 360`

Artefacts: `AI MARS STORAGE/.../SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01/entrypoints-before/`, `http-before/`

---

## 5. Source authority

| File | Role | Modify |
|------|------|--------|
| `/public_html/system/library/zpm/category_visibility.php` | `$neutral_hub_branch_ids` whitelist; homepage + hub tiles | **yes** |
| `/public_html/catalog/controller/common/home.php` | Calls `buildHomepageCategoryCards()` | no |
| `/public_html/catalog/controller/product/category.php` | Hub `hub_categories` via `getNeutralHubBranchIds()` | no |
| `/public_html/catalog/controller/common/header.php` | Megamenu prep | no |

**Verdict:** Source authority **unambiguous** — single whitelist controls parent tile membership; child tiles on `/shkafy-i-lari` use OpenCart category tree, not whitelist.

Artefacts: `manifests/source-authority-map.*`

---

## 6. Patch plan and rollback

**Patch:** Remove `88` from `$neutral_hub_branch_ids`.

```php
// before
array(322, 331, 301, 326, 354, 358, 207, 80, 86, 88, 360)
// after
array(322, 331, 301, 326, 354, 358, 207, 80, 86, 360)
```

**Rollback:** Re-upload `source-before/category_visibility.php`; verify SHA256; optional scoped cache clear if tiles stale.

Artefacts: `manifests/patch-plan.*`, `rollback/rollback-plan.md`, `rollback/source-before-manifest.json`

---

## 7. Dry-run gates

All 16 gates **PASS** before upload (manifest `manifests/dry-run-gates.json`).

---

## 8. Applied changes

### FTP upload (1 file)

| Remote path | Change |
|-------------|--------|
| `/public_html/system/library/zpm/category_visibility.php` | Removed ID **88** from `$neutral_hub_branch_ids` |

Upload SHA verified — local patched file matches production re-download.

**No DB writes. No redirect/SEO changes. No admin saves. No import/monitor runs.**

---

## 9. After verification

| Surface | HTTP | Parent tiles | Лари standalone | Шкафы и лари |
|---------|------|--------------|-----------------|--------------|
| Homepage | 200 | **10** | **absent** | **present** |
| Neutral hub | 200 | **10** | **absent** | **present** |
| `/katalog` | 200 | 1 root card | **absent** | megamenu **present** |
| `/shkafy-i-lari` | 200 | — | child **present** | hub |
| Nested `/shkafy-i-lari/lari` | 200 | — | page OK | canonical nested |

**Redirect:** old flat `/katalog/nejtralnoe-oborudovanie/lari` → **301** nested — unchanged.

Artefacts: `http-after/`, `entrypoints-after/`, `verification/after-verification.json`

---

## 10. Regression verification

| URL | Status | Notes |
|-----|--------|-------|
| `/` | 200 | layout OK |
| `/katalog` | 200 | OK |
| `/katalog/.../stoly` | 200 | Load More present |
| `/custom-equipment` | 200 | OK |
| `/sitemap.xml` | 200 | nested lari URLs present |
| `/robots.txt` | 200 | OK |
| `/llms.txt` | 200 | 0 **БЗПМ** |

---

## 11. Cache actions

**None required.** PHP whitelist is read directly from `category_visibility.php`; tiles updated immediately after upload.

Record: `cache/cache-actions.json` — `actions: []`

---

## 12. Rollback status

Rollback bundle captured: `source-before/category_visibility.php` + `rollback/source-before-manifest.json`. **Not executed.**

---

## 13. Production mutation summary

| Metric | Value |
|--------|-------|
| Remote uploads | **1** exact file |
| Remote overwrites | **1** |
| Remote deletes | 0 |
| FTP writes | **1** |
| Admin saves | 0 |
| DB SELECTs | 0 |
| DB direct writes | 0 |
| Category data changes | 0 |
| Category path changes | 0 |
| SEO URL changes | 0 |
| Redirect changes | 0 |
| Product data changes | 0 |
| Mail sends | 0 |
| Form submits | 0 |
| Cron/import runs | 0 |
| Monitor runs triggered | 0 |
| Cache clears | **0** |
| Header/footer changes | 0 |
| Yandex changes | 0 |
| public БЗПМ introduced | **no** |

---

## 14. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01\`

Checkpoint storage: `...\production\baselines\SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01\`

---

## 15. Authority updates

Updated: `OCPILOT-STATE.md`, `OPERATIONAL-INDEX.md`, `production-profile.md`, `site-passport.md`, `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`, `tools/README.md`, baseline `SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01.md`

---

## 16. Git status

Selective commit of operation docs/tool only (no Storage, no secrets).

---

## 17. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Post-1C import persistence (Run 4.235 pending item) | **Still pending** — unrelated to this whitelist patch |
| `/katalog` root page shows 1 launch-mode root card only | **By design** — parent branch tiles live on homepage + neutral hub |

---

## 18. Final verdict

**SITE-002 PARENT CATEGORY TILES LARI REMOVAL COMPLETE — LARI REMOVED FROM PARENT TILES**

---

## 19. Next task recommendation

Observe next scheduled 1C import for Run 4.235 `parent_id` / `category_path` persistence (existing pending item). No further parent-tile work unless new neutral branches are onboarded to whitelist.
