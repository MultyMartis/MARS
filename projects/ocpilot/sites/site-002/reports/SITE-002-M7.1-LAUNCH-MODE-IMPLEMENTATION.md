# REPORT — BZPM M7.1 Launch Mode Implementation

**Project:** BZPM / SITE-002 (TEST)  
**Environment:** https://zpm.new-site.space/  
**Mode:** Implementation prepared locally — **NO deploy**, **NO commit**, **NO push**  
**Authority:** ROAD-001 · M7A · M7B · OP-001…OP-005 · `BZPM-PRODUCT-ROADMAP-v1.md`  
**Scope:** M7B Phase 1 + Phase 2 only (visibility layer + nav/menu cleanup)

---

## Git (pre-task)

| Parameter | Value |
|-----------|-------|
| Branch | `mars/post-cycle8-live-tests` |
| M7.1 work tree | `projects/ocpilot/sites/site-002/m7.1-launch-mode-work/` (untracked) |
| BZPM-related dirty tracked files | **none** — prior MARS dirty tree unrelated to SITE-002 |

---

## Files Modified (patch ready for FTP)

| Remote path (TEST FTP root) | Action |
|-----------------------------|--------|
| `catalog/controller/product/katalog.php` | modify |
| `catalog/controller/product/category.php` | modify |
| `catalog/controller/common/header.php` | modify |
| `catalog/controller/common/footer.php` | modify |
| `catalog/controller/common/home.php` | modify |
| `catalog/view/theme/default/template/common/megamenu.twig` | modify |
| `catalog/view/theme/default/template/common/footer.twig` | modify |
| `catalog/view/theme/default/template/sections/catalogsections.twig` | modify |
| `catalog/view/theme/default/template/sections/offcanvasmenu.twig` | modify |

**Local patch root:** `projects/ocpilot/sites/site-002/m7.1-launch-mode-work/patch/`

---

## Files Created

| Remote path | Purpose |
|-------------|---------|
| `system/library/zpm/category_visibility.php` | Unified Launch Mode visibility layer |

**Supporting artifacts (repo only):**

- `m7.1-launch-mode-work/backups/*.pre-m7.1-launch-mode.bak` — live pre-change snapshots
- `m7.1-launch-mode-work/backups/m7.1-launch-mode-manifest-*.json` — SHA256 deploy manifest
- `m7.1-launch-mode-work/m7.1-launch-mode-manifest.py` — manifest generator

---

## Visibility Layer

**Path:** `system/library/zpm/category_visibility.php`

| Constant / API | Value / role |
|----------------|--------------|
| `LAUNCH_MODE` | `true` |
| `CATALOG_PRIMARY_ENTRY` | `/katalog/nejtralnoe-oborudovanie` |
| `ACTIVE_LAUNCH_ROOT` | `nejtralnoe-oborudovanie` |
| `VISIBLE_ROOT_CATEGORY_ID` | `79` |
| `VISIBLE_ROOT_SLUGS` | `nejtralnoe-oborudovanie` |
| `HIDDEN_ROOT_SLUGS` | 8 empty peer roots (thermal, cold, inventory, electro-mechanical, bar, bakery, dishwashers, ventilation) |
| `isLaunchMode()` | feature flag |
| `getPrimaryCatalogEntry()` | primary CTA target |
| `isVisibleRootCategory()` | slug/id gate |
| `filterRootCategories()` | nav/list filter + first-tab `active` |
| `applyCatalogNavData()` | applies filter + exposes Twig vars |

**Design rule:** controllers filter; Twig only consumes `catalog_primary_entry` / filtered `categories` — no hardcoded visibility rules in templates.

---

## Catalog Changes

**`/katalog` (Phase 1)**

- URL unchanged, HTTP 200 unchanged, controller/template unchanged structurally.
- After product counts, `katalog.php` calls `CategoryVisibility::applyCatalogNavData()` → **`catlist` filtered to visible roots only**.
- Expected TEST result: **one card — «Нейтральное оборудование»** instead of nine root cards.
- Cache `cat-list-header` still stores **full** tree (DB unchanged); filtering is read-time for display.

**Out of scope (not implemented):** robots meta, noindex, empty-state for hidden categories, search/sitemap scoping.

---

## Megamenu Changes

**Controller:** `header.php` filters `categories` before `catDesktop` build.

**Template:** `megamenu.twig`

- Left tabs: only **Нейтральное оборудование** (+ its subcategory tiles).
- «Открыть страницу каталога» → `{{ catalog_primary_entry }}` (neutral hub).

Hidden root panes remain in DB/cache but are **not passed** to Twig during Launch Mode.

---

## Header Changes

**Controller:** `header.php` exposes `catalog_primary_entry`, filters megamenu data.

**Template:** `header.twig` — **unchanged**.

**Note:** desktop «Каталог» control remains `data-catalog-open` (opens filtered megamenu). Direct URL entry points (footer, mobile, megamenu footer link, home CTA, breadcrumbs) → neutral per OP-004.

---

## Footer Changes

**Controller:** `footer.php` filters footer catalog column via visibility layer.

**Template:** `footer.twig`

- Column title «Каталог» → `catalog_primary_entry`
- Root links: only **Нейтральное оборудование** + «Оборудование на заказ»

---

## Mobile Menu Changes

**Template:** `sections/offcanvasmenu.twig`

- «Каталог» link → `catalog_primary_entry`
- `catalog_primary_entry` passed via `footer.php` (offcanvas partial render chain)

---

## Breadcrumb Changes

**Controller:** `category.php`

- «Каталог» crumb `href`: `/katalog/nejtralnoe-oborudovanie` when `LAUNCH_MODE`, else `/katalog`
- PDP `product.php` unchanged (no explicit «Каталог» crumb in live chain)

---

## Home / Hero CTA

**Controller:** `home.php` filters homepage category cards + passes `catalog_primary_entry`.

**Template:** `sections/catalogsections.twig` — «Перейти в каталог» → neutral.

**Hero slider:** already points to `/katalog/nejtralnoe-oborudovanie/` on slide 1 (live) — **no change**.

---

## QA Checklist

| # | Check | Expected |
|---|-------|----------|
| 1 | `/katalog` | 200, **no redirect**, **1** root card (neutral) |
| 2 | `/katalog/nejtralnoe-oborudovanie` | 200, subcategories/products normal |
| 3 | Neutral leaf PLP e.g. `/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/` | 200, Category V2.2 unaffected |
| 4 | Sample PDP (SP-P-18/6) | 200, PDP V5.1 unaffected |
| 5 | Header megamenu | Only neutral tab + subcategory tiles |
| 6 | Footer catalog column | Only neutral root link |
| 7 | Mobile menu «Каталог» | href → `/katalog/nejtralnoe-oborudovanie` |
| 8 | Category breadcrumb «Каталог» | href → neutral |
| 9 | Direct hidden root URL e.g. `/katalog/teplovoe-oborudovanie` | 200 (unchanged DB page — **not** empty-state; out of M7.1 scope) |
| 10 | View source `/katalog` | No 301/302/meta refresh |

---

## URLs To Test

- https://zpm.new-site.space/
- https://zpm.new-site.space/katalog
- https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie
- https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/
- https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/
- https://zpm.new-site.space/katalog/teplovoe-oborudovanie (direct access regression)
- Sample PDP: https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850

---

## Rollback Procedure

1. Restore files from `m7.1-launch-mode-work/backups/*.pre-m7.1-launch-mode.bak` to matching FTP paths.
2. Delete `system/library/zpm/category_visibility.php` on TEST (or set `LAUNCH_MODE = false` and redeploy controllers only).
3. Clear Twig cache: `system/storage/cache/template/`.
4. Verify: megamenu 9 tabs, footer 9 roots, `/katalog` shows 9 cards, breadcrumb «Каталог» → `/katalog`.
5. Record rollback in operator report with manifest SHA256.

**Manifest:** `backups/m7.1-launch-mode-manifest-20260614-171412.json`

---

## Risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R-01 | Patch not yet on TEST — QA blocked until deploy | Medium | Operator deploy + cache clear |
| R-02 | `cat-list-header` cache empty on cold start → empty megamenu until `/katalog` visited | Low | Pre-existing; visit `/katalog` once or warm cache |
| R-03 | Hidden root URLs still reachable (no empty-state in M7.1 scope) | Medium | Phase 3+ or operator acceptance; nav no longer exposes them |
| R-04 | Header «Каталог» button opens overlay, not direct URL | Low | Documented; megamenu content = neutral-only |
| R-05 | `category_id` 79 assumption | Low | M6/W1B evidence; re-verify on deploy |
| R-06 | PDP / filter / search regression | Medium | QA matrix above; `productcard.twig` / filters untouched |

---

## UNKNOWN

| Topic | Notes |
|-------|-------|
| M6/M7A/M7B formal markdown in repo | Exist in agent transcripts only; not committed under `bzpm-roadmap/` |
| Post-deploy live QA | Not run — deploy explicitly excluded this pass |
| Production `bzpm.ru` parity | TEST-only implementation |

---

## Git status (post-task)

```
?? projects/ocpilot/sites/site-002/m7.1-launch-mode-work/
?? projects/ocpilot/sites/site-002/reports/SITE-002-M7.1-LAUNCH-MODE-IMPLEMENTATION.md
```

**Commit:** NO · **Push:** NO · **Deploy:** NO

---

## Operator next step

1. Review patch under `m7.1-launch-mode-work/patch/`.
2. Approve FTP deploy to TEST.
3. Clear `system/storage/cache/template/`.
4. Run QA checklist on https://zpm.new-site.space/.
