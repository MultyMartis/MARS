# REPORT — M9.8.9-06 FILTER BUG FORENSIC AUDIT

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Live URL:** https://zpm.new-site.space/  
**Audit date:** 2026-06-19  
**Mode:** AUDIT ONLY — no deploy, no FTP writes, no code fixes, no commit  
**Operator symptom:** фильтр на «Столы» не работает; на «Моечные ванны» работает; ползунок цены — правый двигает левый

---

## 1. Reproduction status

| Check | Result | Evidence |
|-------|--------|----------|
| Live pages fetch | **OK** | HTTP 200 for both PLP URLs |
| Filter AJAX transport | **Confirmed** | `updateProducts()` → `fetch(pathname + ?filters=…)` → replace `.category__grid` innerHTML (`assets/js/main.js`) |
| «Столы» — slug-атрибут с селективным значением | **PARTIAL** | `attr[table-top-material][]=бук толщиной 40 мм` → 12 cards vs baseline 15 |
| «Столы» — PRIMARY `attr[51][]` (Конструкция полки) | **FAIL** | `attr[51][]=Без полки` → **0 cards** (ожидалось сужение, не обнуление всего каталога) |
| «Столы» — `only_with_price=1` | **Works** | 1 card (подтверждает серверную фильтрацию в целом) |
| «Моечные ванны» — селективные slug-фильтры | **PASS** | `shell-size` → 2; `hole-for-mixer` → 1; `type-support` → 1; `eq-legs` → 4 |
| «Моечные ванны» — `attr[47][]` | **FAIL** | 0 cards (та же механика, что и `attr[51]` на столах) |
| Price slider «Столы» | **DEGENERATE** | live `min=51280` `max=51281` `step=1000` |
| Price slider «Моечные ванны» | **Healthy** | live `min=8500` `max=40375` `step=1000` |
| Подкатегории `s[]` | **Mixed** | Столы `s[]=304` → 12 cards; `s[]=312` → 0; Моечные `s[]=258` → 1 |

**Вывод по воспроизведению:** расхождение «работает / не работает» **подтверждено частично**. На «Столы» ломаются **критичные PRIMARY-группы с числовым ключом** и **ценовой диапазон**; на «Моечные ванны» большинство slug-групп сужают выдачу корректно.

---

## 2. Exact affected categories

| Категория | Branch root `category_id` | SEO URL (live) | Filter profile | Profile file |
|-----------|---------------------------|----------------|----------------|--------------|
| **Столы** | **301** | `/katalog/nejtralnoe-oborudovanie/stoly/` | **301** (`stoly`) | `system/library/zpm/filter_profiles/301_stoly.php` |
| **Моечные ванны** | **80** | `/katalog/nejtralnoe-oborudovanie/moechnye-vanny/` | **80** (`moechnye_vanny`) | `system/library/zpm/filter_profiles/80_moechnye_vanny.php` |

**Resolver (live-equivalent, repo):** `FilterProfileResolver::$registered_branch_roots = [80, 207, 301, 322, 326]` — обе категории на profile-enabled PLP (`filter_profile_active = true`, M9 layout в sidebar).

### Filter profile comparison (high-signal)

| Aspect | Profile 301 — Столы | Profile 80 — Моечные ванны |
|--------|---------------------|----------------------------|
| PRIMARY attrs | 22, **51**, 33, 20, 25 | **29**, 23, 25 |
| SECONDARY attrs | 21, 112, 26, 31, 115, 18, 47 | 28, 47, 18, 33, 26, 21, 31, 22, 17 |
| Hidden (cross-family) | 23, 28, 29 (sink cluster) | 51, 112, 115, 20 (table cluster) |
| Live attr form keys | **12 groups; numeric: `51`, `47`** | **12 groups; numeric: `47` only** |
| Broken numeric PRIMARY | **Yes — attr 51** | **No** |

**Ключевое отличие:** на «Столы» атрибут **51 (Конструкция полки)** — **PRIMARY** и рендерится как `name="attr[51][]"`. На «Моечные ванны» attr 51 скрыт профилем и в sidebar не участвует.

---

## 3. Filter profile comparison — HTML / AJAX / payloads

### 3.1 Generated HTML (live capture 2026-06-19)

Обе категории используют один шаблон `filterssidebar.twig` (M9 profile branch):

- `data-filters` + `data-filters-form`
- Блоки: Цена → switches → L/W/H ranges → PRIMARY `filter_groups` → «Дополнительные параметры» → **Подкатегории** → actions
- **4 range-блока** на PLP (цена + длина + ширина + высота)

**Столы — аномалии в range:**

```html
<!-- Цена -->
<input data-range-min min="51280" max="51281" step="1000" value="51280" />
<input data-range-max min="51280" max="51281" step="1000" value="51281" />
<!-- Высота -->
<input data-range-min min="850" max="850" step="1" value="850" />
<input data-range-max min="850" max="850" step="1" value="850" />
```

**Моечные ванны — нормальные диапазоны:**

```html
<input data-range-min min="8500" max="40375" step="1000" … />
<input data-range-max min="8500" max="40375" step="1000" … />
```

### 3.2 AJAX endpoint

Отдельного API нет. Клиент:

1. `getReadableState(form)` → сериализация `FormData` в строку `filters=…` (`;` вместо `&`)
2. `GET` текущего PLP URL
3. PHP `category.php`: `parse_str(str_replace(';','&', filters), $custom_filters)`
4. `product.php` → `filter_custom` в SQL

### 3.3 Request / response payloads (live probes)

| Request | Столы cards | Моечные cards |
|---------|-------------|---------------|
| baseline | 15 | 15 |
| `attr[table-top-material][]=<common>` | 15 | 15 |
| `attr[table-top-material][]=бук…` | **12** | — |
| `attr[51][]=Без полки` | **0** | n/a |
| `attr[shell-size][]=<first value>` | — | **2** |
| `attr[47][]=<value>` | **0** | **0** |
| `only_with_price=1` | **1** | 15 |
| `s[]=<first subcat>` | 12 (id 304) | 1 (id 258) |

**Интерпретация:** серверный пайплайн жив; поломка локализована в **ключах атрибутов** и **ценовом индексе**, а не в AJAX-слое.

### 3.4 JS handlers (live `main.js`)

| Component | Behavior |
|-----------|----------|
| Library | **Native `<input type="range">` × 2** — не noUiSlider |
| Init | `initRanges()` → `bindOneRange()` per `[data-range]` |
| Coupling | `normalizePair()` **swap** if `from > to`; оба thumb на `input` синхронизируются |
| Filter apply | `change` на checkboxes/switches → `updateBrowserUrl()` → debounced `updateProducts()` |
| Submit button | Desktop: **только закрытие mobile overlay**, не отдельный apply |

### 3.5 Category ↔ profile mapping

`FilterProfileResolver::resolveForCategory($category_id)`:

- `301` → `301_stoly.php`
- `80` → `80_moechnye_vanny.php`
- Descendants inherit branch root via `oc_category_path`

---

## 4. Price slider findings

| Item | Finding |
|------|---------|
| **Library** | Native dual-range (два overlapping `<input type="range" class="flt__range-thumb">`) |
| **CSS** | Оба thumb `position:absolute; width:100%`; **нет z-index** layering на live CSS |
| **JS** | `bindOneRange`: `input` → `syncFromRanges`; `change` → URL + AJAX |
| **Category-specific** | **Столы:** degenerate price band (1 ₽) + height band (0 мм) → slider non-functional |
| **Root cause (slider)** | **(A)** Data: `getCategoryPriceRange()` для 301 возвращает почти одинаковые min/max (51280–51281) при том что карточки показывают более широкий ценовой разброс → вероятный разрыв **`product_price_index` vs отображаемая цена** для guest group 2. **(B)** UI logic: при `max - min < step` (1000) оба ползунка коллапсируют; `normalizePair` при движении «правого» пересчитывает пару и визуально двигает «левый». **(C)** При `min === max` (высота 850) `updateProgress` делит на ноль → `NaN%` progress. |

**Почему на моечных ваннах слайдер «лучше»:** диапазон 8500–40375 даёт физическое пространство для двух thumb; баг coupling менее заметен.

---

## 5. Subcategory filter («Подкатегории») findings

| Question | Answer |
|----------|--------|
| **Как генерируется** | `category.php`: `getCategories($category_id)` → `filter_subcategories[]`; Twig: `name="s[]" value="{{ subcat.category_id }}"` |
| **Участвует в запросе** | **Да** — `product.php` `filter_custom['s']` → `EXISTS … product_to_category … category_id IN (…)` |
| **Может ломать фильтрацию** | **Иногда** — при выборе подкатегории без прямых `product_to_category` привязок (только leaf IDs) → **0 товаров** при корректном UI state (`checked` есть, grid пуст) |
| **Вклад в bug Столы vs Моечные** | **Вторичный** — не объясняет PRIMARY attr 51; воспроизводится на обеих ветках для «неудачных» subcat ID (напр. Столы 312 → 0, но 304 → 12) |

**Связанный backlog:** M9.8.9-07 (удалить группу из sidebar), EC-01 / M9.8.7 (пустые подкатегории на branch 80).

**UI note:** live «Подкатегории» panel часто `hidden` при `flt__group is-open` — косметика accordion, не корень фильтрации.

---

## 6. Most probable root cause

### Primary (объясняет «Столы сломаны, моечные OK»)

**Slug / SQL mismatch для атрибутов без `filter_name` в БД.**

В `getAttributesByCategory()` ключ группы:

```php
$key = $result['filter_name'] ?: $result['attribute_id'];
```

В `product.php` фильтрация:

```php
AND ad.filter_name = '" . $this->db->escape($attr_slug) . "'
```

Если `filter_name` пустой, форма шлёт `attr[51][]`, а SQL ищет `filter_name = '51'` (строка), **не** `attribute_id = 51`. Результат — **0 товаров**.

| Attribute | Столы exposure | Моечные exposure |
|-----------|----------------|------------------|
| **51** Конструкция полки | **PRIMARY** — operator-visible | Hidden by profile |
| **47** Конструкция борта | SECONDARY | SECONDARY |

На моечных ваннах оператор чаще тестирует **slug-группы** (`shell-size`, `washing`, …) — они работают. На столах **обязательный PRIMARY** `51` — сломан → восприятие «фильтр не работает».

### Secondary (price slider)

**Degenerate bounds на Столы** из `getCategoryPriceRange()` + dual-thumb JS без z-index / без guard для `min >= max` и `max - min < step`.

### Tertiary (not branch-specific)

- `$filter_attributes` используется в `getCategoryPriceRange()` **до присвоения** в `category.php` (latent bug, влияет на обе ветки одинаково).
- `only_with_price` на Столы → 1 товар: индикация проблем **price index coverage** для category 301.

---

## 7. Risk assessment

| Risk | Level | Notes |
|------|-------|-------|
| False filtering (0 results) | **HIGH** | attr 51 on Столы — core commerce filter |
| Price filter unusable on Столы | **HIGH** | degenerate slider + index gap |
| Regression on other M9 branches | **MEDIUM** | any attr with empty `filter_name` |
| Subcategory false empty | **MEDIUM** | data model (leaf-only assignments) |
| AJAX / M9.8.5 limit selector | **LOW** | transport works; limits 15/25/50 — manual polish, not root cause |
| Security | **LOW** | audit read-only |

---

## 8. Recommended fix strategy (NO IMPLEMENTATION)

**Fix order after operator approval:**

1. **Attribute key resolution (P0)**  
   - Option A (code): в `product.php` если `attr_slug` numeric → filter by `pa.attribute_id`; иначе by `ad.filter_name`.  
   - Option B (data): заполнить `filter_name` в админке для attrs **47, 51** (и audit остальных numeric keys).  
   - **Verify:** `attr[51][]=Без полки` на Столы → non-zero selective count.

2. **Price range / slider (P0)**  
   - Audit `product_price_index` coverage for category **301** / customer group **2**.  
   - Align `getCategoryPriceRange()` source with card price source.  
   - JS guards: if `max <= min` or `max - min < step` → disable slider / hide block / expand max to `min + step`.  
   - CSS: z-index `data-range-min` < `data-range-max` (или proven dual-range pattern).

3. **Physical dimension ranges (P1)**  
   - If `min_height === max_height`, collapse or disable height range (Столы: 850).

4. **Subcategories (P2)**  
   - Filter sidebar: join through `category_path` (descendants), not only exact `category_id`.  
   - Or proceed with planned **M9.8.9-07** removal + keep top chips only.  
   - EC-01: hide empty subcats (M9.8.7).

5. **category.php cleanup (P2)**  
   - Define `$filter_attributes` before `getCategoryPriceRange()` or remove dead parameter.

6. **QA matrix post-fix**  
   - Столы: attr 51, 47, price range, subcat 304/312.  
   - Моечные: regression on shell-size, washing, attr 47.  
   - Both: mobile apply, copy-link, reset, pagination after filter.

---

## 9. Timeline hypothesis (recent SITE-002 passes)

| Pass | Could introduce bug? | Assessment |
|------|----------------------|------------|
| **M9 Filter Profile System** | **LIKELY (latent since Phase 1)** | Profile 301 elevated attr **51** to PRIMARY; QA M9 Phase 1 verified **visibility**, not **filter apply** for each attr key type |
| **Category Images** | Unlikely | No filter logic |
| **Subcategory Chips (V2.3)** | Unlikely for attr bug | Top chips separate from sidebar `s[]`; subcat empty-edge case older |
| **M9.8.5 Products Per Page** | Unlikely | `category.php` limit plumbing; filters unchanged |
| **Manual UI / Filter Compact / CSS / Twig polish** | **Possible amplifier** | May worsen slider UX (compact layout); **did not create** slug/SQL mismatch |
| **M9.8 UX polish checkpoint** | N/A | Documents manual live drift; no file capture |

**Hypothesis:** баг **не новый hotfix M9.8.9**, а **структурный дефект custom filter + empty filter_name**, **раз uncovered** на Столы из-за profile 301 (PRIMARY attr 51) и **ужесточён** degenerate price index на этой ветке. Operator report после manual polish — **совпадение по времени**, не доказанная причинно-следственная связь.

**SAFE UNKNOWN:** точная дата, когда `product_price_index` для 301 стал давать 51280–51281 — не верифицирована без DB read (вне scope read-only HTML/HTTP audit).

---

## 10. Artifacts (audit session)

| Artifact | Path |
|----------|------|
| Live HTML Столы | `.recovery-temp/m989-audit-stoly.html` |
| Live HTML Моечные | `.recovery-temp/m989-audit-sinks.html` |
| Live main.js | `.recovery-temp/m989-audit-main.js` |
| Probe scripts | `.recovery-temp/m989-filter-probe*.py` |

---

## Status

| Field | Value |
|-------|--------|
| Implementation | **NO** — audit only |
| Deploy / FTP | **NO** |
| Git commit | **NO** |
| Next step | Operator approval → M9.8.9-06 fix pass per §8 |

---

*Evidence: live HTTP probes + repo references (`m9-phase3-remaining-work/patch/`, `m9.8.5-products-per-page-work/`). Live file hashes not captured — per `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` metadata-only checkpoint.*
