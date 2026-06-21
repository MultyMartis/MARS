# REPORT — M9.8.9-06I FILTER ZERO RESULTS FORENSIC

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Live URL:** https://zpm.new-site.space/  
**Audit date:** 2026-06-19  
**Mode:** AUDIT ONLY — no deploy, no FTP, no DB writes, no code fixes, no commit  
**Prior passes (context):** M9.8.9-06A (filter forensic), 06D (301 price index rebuild), 06F (1C price hook), 06H (exclude zero from price range)

**Evidence bundle:** `projects/ocpilot/sites/site-002/reports/m9.8.9-06i-work/`  
**Runner:** `m9.8.9-06i-filter-zero-forensic-run.py` → `forensic-results.json`

---

## 1. Reproduction

| Check | Result | Notes |
|-------|--------|-------|
| Operator claim: «любой фильтр → 0» на Столы / Подтоварники | **PARTIALLY CONFIRMED** | **PRIMARY `attr[51]`** и **`attr[47]`** стабильно дают **0**; slug-группы и подкатегории **часто работают** |
| Столы baseline | **15 cards** | `/katalog/nejtralnoe-oborudovanie/stoly/` |
| Подтоварники baseline | **11 cards** | `/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/` |
| Моечные ванны baseline | **15 cards** | control branch — slug PRIMARY работают |
| Зонты baseline | **15 cards** | control branch — slug PRIMARY работают |
| Гипотеза M9.8.9-06A (`attr[51]` / `attr[47]` vs `filter_name`) | **CONFIRMED** | live HTTP + live DB; **не закрыта** прошлыми price-passes |
| Регресс от 06D / 06F / 06H | **NOT CONFIRMED** | price-range fix не менял attr-SQL; симптом attr **идентичен 06A** |

**Типичный сценарий оператора:** в sidebar первым идёт **PRIMARY «Конструкция полки»** (`attr[51][]`) — клик → **0 товаров** → восприятие «фильтр сломан целиком».

**Контрпример (Столы, slug работает):**  
`attr[table-top-material][]=бук толщиной 40 мм` → **12 cards** (vs baseline 15).

---

## 2. Affected Categories

| Category | `category_id` | Profile | PLP URL | Scope of zero-result bug |
|----------|---------------|---------|---------|--------------------------|
| **Столы** | **301** | `301_stoly` | `/katalog/nejtralnoe-oborudovanie/stoly/` | **PRIMARY + часть SECONDARY** с numeric keys **47, 51**; slug-группы в основном OK |
| **Подтоварники и подставки** | **322** | `322_podtovarniki` | `/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/` | **PRIMARY `attr[51]`** → 0; slug-группы **работают** |
| Моечные ванны | 80 | `80_moechnye_vanny` | `/moechnye-vanny/` | Только **`attr[47]`** (SECONDARY); PRIMARY slug OK |
| Зонты вытяжные | 207 | `207_zonty` | `/zonty-vytyazhnye/` | **Не затронуты** attr-bug (нет 47/51 в UI) |
| Тележки | 326 | `326_telezhki` | `/telezhki-servirovochnye/` | Нет attr-групп; `only_with_price` → 0 (**data**: нет priced SKU) |

### Neutral branches without dedicated profile

M9 `FilterProfileResolver::$registered_branch_roots = [80, 207, 301, 322, 326]`.

**Полки** — отдельного profile-файла в репозитории **нет**; live URL ветки «Полки» в этом прогоне **не верифицирован** (SAFE UNKNOWN). Любая ветка, где в sidebar рендерятся attrs **47/51** с пустым `filter_name`, унаследует тот же SQL-дефект.

### Profile exposure (почему Столы / Подтоварники «более сломаны»)

| Attribute | Profile 301 Столы | Profile 322 Подтоварники | Profile 80 Моечные |
|-----------|-------------------|--------------------------|---------------------|
| **51** Конструкция полки | **PRIMARY** (верх sidebar) | **PRIMARY** (верх sidebar) | **hidden** |
| **47** Конструкция борта | SECONDARY | hidden | SECONDARY |

На **Моечных** оператор чаще кликает **slug PRIMARY** (`shell-size`, `washing`, `available-board`) — они работают. На **Столах / Подтоварниках** первый кликабельный блок — сломанный **`attr[51]`**.

---

## 3. Working Filters

### Столы (301) — работают

| Filter param | Example | Cards |
|--------------|---------|-------|
| Baseline | — | 15 |
| `in_stock=1` | switch | 15 |
| `only_with_price=1` | switch | 1 |
| `only_discount=1` | switch | 1 |
| `attr[table-top-material][]` | бук толщиной 40 мм | **12** |
| `attr[construction][]` | сварная (неразборная) | 15* |
| `attr[material-polki][]` | slug | 15* |
| `s[]` | subcat 304 | **12** |
| `price_from` / `price_to` | 5405–72630 | **1** |

\*15 = совпадает с baseline на первой странице (значение слишком частое или полное совпадение выборки); **не** признак SQL-fail.

### Подтоварники (322) — работают

| Filter param | Example | Cards |
|--------------|---------|-------|
| `attr[max-load][]=200` | slug | **8** |
| `attr[table-top-material][]` | нерж. сталь AISI 430 0.7 мм | **8** |
| `attr[construction][]=разборная` | slug | **8** |
| `attr[section-size][]=GN 1/1` | slug | **2** |
| `s[]=325` | subcat | **3** |

### Control branches

| Branch | Example | Cards |
|--------|---------|-------|
| Моечные | `attr[shell-size][]=1100х500х400` | **2** |
| Моечные | `attr[hole-for-mixer][]=2 отверстия` | **1** |
| Зонты | `attr[construction][]=угловая, купольная` | **1** |

---

## 4. Broken Filters

### Always zero (SQL key mismatch)

| Category | HTML `name` | URL sends | SQL expects | Live cards | DB products (by `attribute_id`) |
|----------|-------------|-----------|-------------|------------|--------------------------------|
| Столы | `attr[51][]` | `attr[51][]=Без полки` | `ad.filter_name = '51'` | **0** | **420** in subtree 301 |
| Столы | `attr[47][]` | `attr[47][]=Цельный борт` | `ad.filter_name = '47'` | **0** | **44** in subtree 301 |
| Подтоварники | `attr[51][]` | `attr[51][]=600х400х300` | `ad.filter_name = '51'` | **0** | **11** in subtree 322 |
| Моечные | `attr[47][]` | `attr[47][]=Объемный борт` | `ad.filter_name = '47'` | **0** | (SECONDARY; не блокирует PRIMARY UX) |

**DB proof (`filter_name` empty):**

| `attribute_id` | `name` | `filter_name` (live) |
|----------------|--------|----------------------|
| 47 | Конструкция борта | **'' (EMPTY)** |
| 51 | Конструкция полки | **'' (EMPTY)** |

**SQL resolution probe:**

| Query | Столы 301 | Подтоварники 322 |
|-------|-----------|------------------|
| `WHERE ad.filter_name = '51'` | **0** products | **0** products |
| `WHERE pa.attribute_id = 51` | **420** products | **11** products |
| `WHERE ad.filter_name = '47'` | **0** products | 0 (no data in branch) |
| `WHERE pa.attribute_id = 47` | **44** products | 0 |

### Secondary / data-driven zeros (not attr-SQL bug)

| Category | Filter | Cards | Cause |
|----------|--------|-------|-------|
| Столы | `price_from=5405;price_to=20000` | **0** | Only **1** SKU with `effective_price > 0` in index; that SKU **> 20000** |
| Подтоварники | `only_with_price=1` | **0** | No non-zero priced SKU in branch 322 |
| Тележки | `only_with_price=1` | **0** | Same — data / index coverage |

### Data note — Подтоварники attr 51

Profile 322 labels attr **51** as «Конструкция полки», but live values are **dimensions** (`600х400х300`, `1200х600х300`, …). Even after SQL fix, **UX label vs data semantics** need review (separate from key-resolution bug).

---

## 5. URL Parameters

### Transport chain (all profile PLPs)

```
User change → FormData → getReadableState() → ?filters=... (; separator)
→ category.php: parse_str(str_replace(';','&', filters))
→ $custom_filters → product.php getProducts(['filter_custom' => ...])
```

### Rendered HTML keys (live 2026-06-19)

**Столы — 12 attr groups:**

| Tier | Param type | Keys |
|------|------------|------|
| PRIMARY | **numeric (broken)** | `51` |
| PRIMARY | slug (OK) | `table-top-material`, `type-support`, `max-load`, `available-board` |
| SECONDARY | slug (OK) | `construction`, `material-polki`, `eq-legs`, `height-adjustment`, `usilenie`, `side-height` |
| SECONDARY | **numeric (broken)** | `47` |

**Подтоварники — 12 attr groups:**

| Tier | Param type | Keys |
|------|------------|------|
| PRIMARY | **numeric (broken)** | `51` |
| PRIMARY | slug (OK) | `max-load` |
| SECONDARY | slug (OK) | `table-top-material`, `type-support`, `construction`, `qty`, `eq-legs`, `height-adjustment`, `usilenie`, `section-size`, `section-assignment`, `number-guide-levels` |

**Non-attr params (all branches):** `price_from`, `price_to`, `len_from/to`, `w_from/to`, `h_from/to`, `in_stock`, `preorder_only`, `only_with_price`, `only_discount`, `s[]`.

### attribute_id vs filter_name — rule

| Layer | Resolution |
|-------|------------|
| `getAttributesByCategory()` | `$key = $result['filter_name'] ?: $result['attribute_id'];` → empty `filter_name` → **numeric key in HTML** |
| `filterssidebar.twig` | `name="attr[{{ group.group_slug }}][]"` → propagates numeric key |
| `getProducts()` / `getTotalProducts()` SQL | **Always** `AND ad.filter_name = '<attr_slug>'` — **never** `attribute_id` for `filter_custom['attr']` |

**Mismatch:** HTML/URL use `51` as slug string; SQL searches `filter_name = '51'`; DB has `filter_name = ''`.

---

## 6. SQL Chain

### Attribute filter (broken path)

```sql
-- URL: filters=attr[51][]=Без полки
-- Parsed: $f['attr']['51'] = ['Без полки']

AND EXISTS (
  SELECT 1 FROM oc_product_attribute pa
  LEFT JOIN oc_attribute_description ad ON (pa.attribute_id = ad.attribute_id)
  WHERE pa.product_id = p.product_id
    AND ad.filter_name = '51'          -- ← never matches (filter_name is EMPTY)
    AND (pa.text = 'Без полки')
    AND ad.language_id = 1
)
```

### Attribute filter (working slug path)

```sql
-- URL: filters=attr[table-top-material][]=бук толщиной 40 мм

AND ad.filter_name = 'table-top-material'  -- ← matches DB
AND pa.text = 'бук толщиной 40 мм'
```

### Price filter (post-06H; separate issue)

```sql
-- effective_price in listing:
IFNULL(ppi.special, ppi.price)

-- getCategoryPriceRange (06H): excludes effective_price <= 0
AND IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) > 0
```

06H **fixed** sidebar min (5405 on Столы, 5553 on Моечных). It **did not** change attr EXISTS logic. Столы still have **14/15** «по запросу» SKUs → price slider often **zeros** grid when narrowed.

---

## 7. Root Cause

### Primary root cause (P0)

**Single structural bug — unresolved from M9.8.9-06A:**  
`filter_name` empty for attributes **47** and **51** → UI falls back to **numeric group key** → SQL filters only by **`ad.filter_name`**, not **`pa.attribute_id`**.

| Field | Value |
|-------|-------|
| **Classification** | **SQL resolution bug** (not profile 301 logic per se, not AJAX) |
| **Confidence** | **HIGH** — HTTP probes + DB counts + code path |
| **Introduced by 06D/06F/06H?** | **No** — attr path unchanged; price passes addressed different layer |
| **Why Столы vs Моечные differ in UX** | Profile **301/322** promote broken **51** to **PRIMARY**; profile **80** hides **51** and uses working slug PRIMARYs |

### Secondary factors (not «any filter»)

1. **Profile 301/322** place broken attrs at top → operator hits zero first.
2. **Price index coverage** on Столы (1 priced of 15) → price range feels broken when narrowed.
3. **Подтоварники attr 51 data** = dimensions under wrong semantic label (data/merch review after SQL fix).

### Bug count

| # | Bug | Scope |
|---|-----|-------|
| 1 | `filter_name` / `attribute_id` mismatch in attr SQL | **Global** — any attr with empty `filter_name` |
| 2 | Price slider usability on low-priced-index branches | **Data + UX** — Столы, частично Подтоварники |
| 3 | Attr 51 semantics on branch 322 | **Data / catalog** — label vs values |

**Answer:** это **один основной баг** (#1) + **сопутствующие** data/UX эффекты; **не** отдельный регресс price-hotfix.

---

## 8. Recommended Fix

**NO IMPLEMENTATION in this pass.** Suggested order after operator approval:

### P0 — Attribute key resolution (closes 06A + 06I)

**Option A (code, preferred):** In `catalog/model/catalog/product.php`, inside `filter_custom['attr']` loop:

- If `$attr_slug` is numeric → `AND pa.attribute_id = (int)$attr_slug`
- Else → `AND ad.filter_name = ...` (current)

Apply in **both** `getProducts()` and `getTotalProducts()`.

**Option B (data):** Set `filter_name` in admin for attrs **47**, **51** (e.g. `board-construction`, `shelf-construction`) and align `getAttributesByCategory` keys.

**Verify:**

- `attr[51][]=Без полки` on Столы → **> 0** selective count  
- `attr[51][]=600х400х300` on Подтоварники → **> 0**  
- Regression: `attr[shell-size][]` on Моечные unchanged

### P1 — Price filter on Столы

- Audit why **14/15** SKUs lack guest-group index price (06D rebuilt subtree but coverage still thin for filters).  
- Optional JS: do not send default `price_from`/`price_to` until user moves slider.

### P2 — Подтоварники attr 51 semantics

- Confirm intended attribute for dimension values; update profile or attribute assignment.

### P3 — Full numeric-key audit

- Scan all attrs with `filter_name = ''` exposed in any M9 profile.

| Fix | Confidence in resolution | Risk if skipped |
|-----|------------------------|-----------------|
| P0 code/data | **HIGH** | PRIMARY filters remain unusable on 301/322 |
| P1 price | MEDIUM | Price slider continues to zero grid |
| P2 data | MEDIUM | Misleading filter labels post-fix |

---

## 9. Risk Assessment

| Risk | Level | Notes |
|------|-------|-------|
| False empty results on PRIMARY filters (301, 322) | **CRITICAL** | Core commerce path; operator-visible daily |
| False perception «вся ветка сломана» | **HIGH** | PRIMARY placement amplifies single bug |
| Regression on slug attrs after P0 fix | **LOW** | If branch: numeric only when `ctype_digit($slug)` |
| Price filter empty grid | **MEDIUM** | Data/index; worsened UX after 06H fixed min≠0 |
| 06D/06F/06H rollback as attr fix | **NONE** | Wrong layer — would not restore attr[51] |
| Security | **LOW** | Read-only audit |

---

## Artifacts

| File | Purpose |
|------|---------|
| `reports/m9.8.9-06i-work/forensic-results.json` | Full HTTP probe matrix (5 branches) |
| `reports/m9.8.9-06i-work/m9.8.9-06i-filter-zero-forensic-run.py` | Reproducible runner |
| `reports/m9.8.9-06i-work/supplement-probe.py` | Selective slug + attr key extraction |
| `reports/SITE-002-M9.8.9-06-FILTER-BUG-FORENSIC-AUDIT.md` | Prior 06A analysis (still valid) |

---

## Status

| Field | Value |
|-------|-------|
| Implementation | **NO** |
| Deploy / FTP / DB | **NO** |
| Git commit | **NO** |
| Next step | Operator approval → **P0 attr key fix** (M9.8.9-06J or reopen 06A fix scope) |

---

*Evidence: live HTTP 2026-06-19 ~06:55 UTC, live DB read via phpMyAdmin (read-only SELECT), repo live-capture `catalog/model/catalog/product.php` (06H), filter profiles 301/322/80/207.*
