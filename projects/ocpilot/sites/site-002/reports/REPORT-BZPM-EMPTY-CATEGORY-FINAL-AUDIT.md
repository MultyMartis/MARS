# REPORT — BZPM EMPTY CATEGORY FINAL AUDIT

**Site:** SITE-002 (ЗПМ) TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` (LIVE TEST STATE AFTER MANUAL UI REFINEMENT)  
**Mode:** Audit only — **no code changes**  
**Execution UTC:** 2026-06-15

---

## Scope

Повторный аудит задачи: в root hub «Нейтральное оборудование» и megamenu показывать **только категории с активными товарами** (`status=1`, subtree count > 0).

Проверены:

- category cards root hub  
- megamenu (desktop)  
- `/katalog` tiles  
- вложенные блоки (subcategory chips, filter sidebar «Подкатегории»)  
- home catalog sections  
- footer / offcanvas  
- PHP/Twig data paths  

**Evidence:**  
`reports/empty-category-audit-data.json` · `reports/filter-subcategory-crosscheck.json`

---

## Executive summary

| Surface | Status | Empty categories visible? |
|---------|--------|---------------------------|
| Root hub cards (cat 79) | **CLEAN** | No — 5 branches with products |
| Megamenu neutral children | **CLEAN** | No — 5 tiles, all count > 0 |
| `/katalog` neutral tiles | **CLEAN** | No — 5 tiles |
| Subcategory chips (branch PLP) | **CLEAN** | No — filtered by `totalsub > 0` |
| Filter sidebar «Подкатегории» | **ISSUE** | **Yes — 13 on branch 80 (Моечные ванны)** |
| Home `catalogsections` | **CLEAN** | Root only (Launch Mode) |
| Footer / offcanvas | **CLEAN** | No empty branch links |
| Direct URL / DB | **By design** | Empty cats remain in DB; URLs still reachable |

**Root hub + megamenu:** requirement **met** on live TEST.  
**Remaining gap:** filter sidebar subcategories on branch PLP (especially Моечные ванны).

---

## 1. Live surface audit

### 1.1 Root hub — `/katalog/nejtralnoe-oborudovanie`

| Check | Result |
|-------|--------|
| Hub mode | `category--hub` present |
| Card count | **5** |
| Cards | Столы, Моечные ванны, Подтоварники и подставки, Зонты вытяжные, Тележки серvировочные |
| Empty branch slugs (polki, stellazhi, …) | **Not present** |

**Controller path:** `category.php` hub mode → `getNeutralHubBranchIds()` + `getTotalProducts()` → skip if `totalsub <= 0`.

### 1.2 Megamenu

| Check | Result |
|-------|--------|
| Neutral tile count | **5** |
| Zero-count tiles | **0** |
| Forbidden empty branches (Стеллажи, Полки, …) | **0** |

**Data path:** `cat-list-header` cache → `prepareMegamenuCategories()` in `header.php` / `katalog.php`.

### 1.3 `/katalog`

Same 5 neutral children as megamenu — filtered at cache build + runtime `prepareMegamenuCategories()`.

### 1.4 Subcategory chips (branch PLP header)

| Branch | Chips | Empty visible |
|--------|------:|-----------------|
| Столы (301) | 7 | **0** |
| Моечные ванны (80) | 18 | **0** |
| Подтоварники (322) | 3 | **0** |
| Зонты (207) | 0 | — |
| Тележки (326) | 0 | — |

**Controller path:** `category.php` branch mode lines 212–234 — `if ($totalsub > 0)` before adding to `$data['categories']`.

### 1.5 Filter sidebar «Подкатегории» — **PROBLEM**

| Branch | Filter checkboxes | Empty (0 active subtree) visible |
|--------|------------------:|----------------------------------:|
| Столы (301) | 7 | **0** |
| Моечные ванны (80) | 44 | **13** |
| Подтоварники (322) | 3 | **0** |
| Зонты (207) | 0 | **0** |
| Тележки (326) | 0 | **0** |

**13 empty subcategories still shown on Моечные ванны filter:**

1. Ванны с рабочей поверхностью ЛЮКС  
2. Ванны с рабочей поверхностью ПРЕМИУМ нестандарт  
3. Ванны с рабочей поверхностью ПРЕМИУМ-2 нестандарт  
4. Ванны с рабочей поверхностью ПРЕМИУМ-3 нестандарт  
5. Ванны с рабочей поверхностью СТАНДАРТ нестандарт  
6. Ванны сварные ПРЕМИУМ НЕСТАНДАРТ  
7. Ванны сварные ПРЕМИУМ-2 нестандарт  
8. Ванны сварные ПРЕМИУМ-3 нестандарт  
9. Ванны сварные ПРЕМИУМ-В  
10. Ванны цельнотянутые ПРЕМИУМ нестандарт  
11. Ванны цельнотянутые ПРЕМИУМ-2  
12. Ванны цельнотянутые ПРЕМИУМ-2 нестандарт  
13. Ванны цельнотянутые Премиум-3 Нестандарт  

---

## 2. Code path audit

| Layer | File | Filters empty? | Scope |
|-------|------|----------------|-------|
| PHP library | `category_visibility.php` → `prepareMegamenuCategories()` | **YES** | Megamenu / cat-list children |
| Controller | `header.php` | Uses prepareMegamenu | Megamenu |
| Controller | `katalog.php` | Filter on cache build + prepareMegamenu | `/katalog` + cache |
| Controller | `category.php` hub block | **YES** `totalsub <= 0` skip | Hub cards |
| Controller | `category.php` branch chips | **YES** `totalsub > 0` | Subcategory chips |
| Controller | `category.php` filter_subcategories | **NO** | **All direct children** — no product count |
| Twig | `megamenu.twig` | N/A (data pre-filtered) | Renders all `mainc.children` |
| Twig | `category.twig` | N/A | Hub uses `hub_categories`; chips use filtered `$data['categories']` |
| Twig | `filterssidebar.twig` | N/A | Renders all `filter_subcategories` |

**Root cause (remaining gap):**

```406:417:projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI/files/catalog/controller/product/category.php
			$data['filter_subcategories'] = [];
			$children = $this->model_catalog_category->getCategories($category_id);

			foreach ($children as $child) {
				$is_checked = in_array((string)$child['category_id'], $selected_subcategories);

				$data['filter_subcategories'][] = [
					'category_id' => $child['category_id'],
					'name'        => $child['name'],
					'checked'     => $is_checked,
					'keyword'     => $child['keyword'] ?? $child['category_id'] 
				];
			}
```

No `getTotalProducts()` guard — unlike hub cards and subcategory chips in the same file.

---

## 3. Database state (informational)

**Direct children of neutral root (79) with zero active subtree** — remain in DB, **hidden from hub/megamenu**:

| category_id | Name | subtree_active |
|------------:|------|---------------:|
| 82 | Подтоварники | 0 |
| 83 | Полки | 0 |
| 85 | Тележки | 0 |
| 86 | Стеллажи | 0 |
| 87 | Столы производственные | 0 |
| 88 | Лари | 0 |
| 89 | Шкафы | 0 |

These are **not** UI defects for hub/megamenu (correctly excluded). Direct URLs may still resolve if known.

Under branch 80: **13** direct child categories with `subtree_active = 0` — **visible in filter sidebar** (see §1.5).

---

## 4. Problem register (for future implementation)

| ID | Severity | Surface | Issue | Suggested fix locus |
|----|----------|---------|-------|---------------------|
| **EC-01** | **High** | Filter sidebar «Подкатегории» on branch 80 | 13 subcategories with 0 active products shown as checkboxes | `category.php` — add `getTotalProducts()` filter before pushing to `filter_subcategories` (mirror chips logic) |
| **EC-02** | Low | Direct URL access | Empty categories remain addressable if slug/ID known | Out of scope for nav-only requirement; optional 404/redirect policy |
| **EC-03** | Info | DB hygiene | 7 empty neutral root children + many empty nested cats under 80 | Data cleanup optional; not required for nav if code filters |

**Not problems (verified clean):**

- Root hub 5 cards  
- Megamenu 5 neutral tiles  
- `/katalog` page tiles  
- Subcategory chips on all tested branches  
- M9.7C megamenu fix still active on live TEST  

---

## 5. Classification (original M9.7C model)

| Surface | Class | Status |
|---------|-------|--------|
| Hub + megamenu + `/katalog` | B) Controller + C) Query — **fixed** M9.7C | **Clean** |
| Subcategory chips | B) Controller — filtered in `category.php` | **Clean** |
| Filter subcategories | B) Controller — **unfiltered** | **EC-01 open** |
| Twig layers | A) Presentational — rely on controller data | OK where data pre-filtered |

---

## 6. Recommended next step (not executed)

1. Implement **EC-01** only: filter `filter_subcategories` by active product count (same `filter_sub_category => true` semantics as hub/chips).  
2. Re-run `filter-subcategory-crosscheck.py` on branch 80 — expect **0** empty in filter.  
3. Visual HITL on hub/megamenu unchanged (manual UI baseline preserved).

---

## UNKNOWN / SECURITY RISK

**UNKNOWN:** Why filter sidebar on branch 80 lists **44** checkbox names while DB reports **25** direct children with `parent_id=80` — may include naming duplicates, inactive rows in `getCategories()`, or PMA column parsing variance; **13 empty names cross-check confirmed** regardless.

**SECURITY RISK:** none.

---

## Stop

Audit complete. **No code changed.** Awaiting authorization to implement EC-01.
