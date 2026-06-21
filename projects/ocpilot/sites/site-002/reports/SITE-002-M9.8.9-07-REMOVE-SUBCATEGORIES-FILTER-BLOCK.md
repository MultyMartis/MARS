# REPORT — M9.8.9-07 REMOVE SUBCATEGORIES FILTER BLOCK

**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`  
**Environment:** TEST — https://zpm.new-site.space/  
**Deployed:** 2026-06-19 UTC (`manifest-post-20260619-104018.json`)

---

## 1. Root Source

### Audit — where «Подкатегории» comes from

| Layer | File (live path) | Role |
|-------|------------------|------|
| **UI render** | `catalog/view/theme/default/template/sections/filterssidebar.twig` | Section `<!-- SUBCATEGORIES -->` — accordion `.flt__group` with `name="s[]"` checkboxes |
| **Controller data** | `catalog/controller/product/category.php` | `getCategories($category_id)` → `$data['filter_subcategories']`; reads `$custom_filters['s']` for checked state |
| **filter_custom** | `filters` query param (JSON) | Key `s` — array of child `category_id` values |
| **SQL** | `catalog/model/catalog/product.php` | `getProducts()` / `getTotalProducts()`: `if (!empty($f['s']))` → `product_to_category` IN clause |

**Conclusion:** Backend pipeline unchanged. Only Twig condition gates sidebar output.

### UI change (reversible)

```twig
{# M9.8.9-07: Subcategories filter group hidden (UI only). Restore: replace `false and filter_subcategories` with `filter_subcategories`. #}
{% if false and filter_subcategories %}
```

Markup, controller, `filter_custom['s']`, and SQL remain intact for easy restore.

**Not touched:** top subcategory chips (`category.twig` V2.3), megamenu, breadcrumbs, PDP, overlay, profile system, ajax filter JS.

---

## 2. Files Changed

| Action | Path |
|--------|------|
| **Live deploy** | `catalog/view/theme/default/template/sections/filterssidebar.twig` |
| FTP capture | `reports/m9.8.9-07-work/live-capture/catalog__view__theme__default__template__sections__filterssidebar.twig` |
| Backup | `backups/filterssidebar.twig.pre-m9.8.9-07-hide-subcategories.bak` |
| Patched copy | `reports/m9.8.9-07-work/catalog__view__theme__default__template__sections__filterssidebar.twig.patched` |
| Manifest (pre) | `reports/m9.8.9-07-work/manifest-pre-20260619-104018.json` |
| Manifest (post) | `reports/m9.8.9-07-work/manifest-post-20260619-104018.json` |
| Deploy script | `reports/m9.8.9-07-work/m9.8.9-07-deploy-run.py` |
| QA script | `reports/m9.8.9-07-work/m9.8.9-07-qa-run.py` |
| QA results | `reports/m9.8.9-07-work/qa-results.json` |
| Sidebar verify | `reports/m9.8.9-07-work/qa-sidebar-verify.txt` |

**SHA256:** pre `bcf9d1e9…` → post `fbec1b53…` · `deploy_ok: true`

---

## 3. What Was Removed

- **Removed from UI:** accordion group «Подкатегории» in left filter sidebar (`s[]` checkboxes).
- **Preserved:** `filter_subcategories` data in `category.php`; `filters.s[]` in URL/API; SQL branch for `f['s']`; subcategory chips above product grid; category tree / megamenu.

---

## 4. QA Results

### Sidebar — all 5 categories (`qa-sidebar-verify.txt`)

| Category | `s[]` in sidebar | «Подкатегории» title | Other groups |
|----------|------------------|----------------------|--------------|
| Столы (301) | **absent** | **absent** | 9 (Цена, L/W/H, attrs…) |
| Моечные ванны (80) | **absent** | **absent** | 6 |
| Подтоварники (322) | **absent** | **absent** | 9 |
| Тележки (326) | **absent** | **absent** | 4 |
| Зонты (207) | **absent** | **absent** | 4 |

### Functional probes (`qa-results.json`)

| Category | No subcat block | Attr / baseline | Price range | only_with_price | JS errors |
|----------|-----------------|-----------------|-------------|-----------------|-----------|
| Столы | ✓ | ✓ 15 cards (`attr[51]`) | ✓ 15 | ✓ 15 | ✓ |
| Моечные ванны | ✓ | ✓ 2 cards | ✓ 15 | ✓ 15 | ✓ |
| Подтоварники | ✓ | ✓ 1 card | ✓ 11 | ✓ 11 | ✓ |
| Тележки | ✓ | ✓ 3 baseline | ✓ 3 | ✓ 3 | ✓ |
| Зонты | ✓ | ⚠ probe `attr[construction]=разборная` → 0 cards (1 SKU category; baseline/price/owp ✓) | ✓ 1 | ✓ 1 | ✓ |

**Note:** «Подкатегории» may still appear in **top chips** (by design — out of scope). Sidebar filter block is gone on all tested branches.

**Overall task QA:** **PASS** for M9.8.9-07 scope (UI removal + filter regression on price/owp/attr where applicable).

---

## 5. Rollback

1. Restore backup → live:
   - `backups/filterssidebar.twig.pre-m9.8.9-07-hide-subcategories.bak` → `catalog/view/theme/default/template/sections/filterssidebar.twig`
2. Or edit live Twig: change `{% if false and filter_subcategories %}` back to `{% if filter_subcategories %}` and remove M9.8.9-07 comment.
3. Clear Twig template cache if needed (`system/storage/cache/template/`).

Pre-deploy SHA256 in `manifest-pre-20260619-104018.json`.

---

## 6. Risks

| Risk | Level | Notes |
|------|-------|-------|
| Users with bookmarked `filters.s[]` URLs | Low | Backend still honours `s[]`; only sidebar UI hidden |
| EC-01 (empty subcats branch 80) | N/A | Sidebar group removed; chips remain |
| Twig cache stale | Low | Post-deploy verify SHA matched; cache dir was empty |
| Accidental backend removal | None | Single-line Twig guard only |

---

**Git:** no commit · no push (per task).
