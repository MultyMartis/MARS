# REPORT — M9.8.9-08 FILTER GROUP RESET FORENSIC

**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`  
**Environment:** TEST — https://zpm.new-site.space/  
**Mode:** Read-only forensic — **no deploy, no code changes**  
**Run UTC:** 2026-06-19  
**Evidence:** repo live-captures + pass reports (06K, 06M, 07, 04A/04B); **live FTP not re-captured in this pass**

---

## 1. PRE-TASK compliance

| Step | Status |
|------|--------|
| Read `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | **done** |
| Read `baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md` | **done** |
| Verify Authority State | **matches** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01` |
| Read `site-passport.md`, `README.md` | **done** |
| Code changes | **none** (forensic only) |

---

## 2. Executive summary

Sidebar filter на PLP — **Twig + vanilla JS** в `assets/js/main.js`. Состояние фильтра сериализуется из формы `[data-filters-form]` в query-параметр `filters` (semicolon-separated `parse_str` payload). Любое изменение чекбокса → `updateBrowserUrl()` → debounced `updateProducts()` (AJAX fetch полной страницы, замена `.category__grid` + `.pagination`).

**Глобальный сброс** уже есть: `[data-filter-reset]` («Сбросить всё») в `initReset()`.

**Групповой сброс** отсутствует. Безопасная точка внедрения — **только UI/JS/CSS sidebar**: снять inputs внутри одной `.flt__group` (attribute checkbox groups), затем вызвать существующий `updateBrowserUrl(form)`.

**Radio / select в sidebar сейчас не используются** — только checkbox, switch, range. Range (цена, габариты) **в scope M9.8.9-08 не входят**.

**Active filter chips над grid отсутствуют** (зафиксировано в CATEGORY-AUDIT-V1). «Текущее состояние» = checked + `.active` в sidebar + URL `?filters=…`.

---

## 3. Architecture map

### 3.1 Layer inventory

| Layer | Live path (canonical) | Role |
|-------|----------------------|------|
| **Category layout** | `catalog/view/theme/default/template/product/category.twig` | Embeds `{{ filter }}` in `[data-filter-sidebar]` (mobile offcanvas) + desktop sidebar |
| **Filter sidebar Twig** | `catalog/view/theme/default/template/sections/filterssidebar.twig` | Renders `[data-filters]` / `[data-filters-form]`, groups, ranges, switches, footer actions |
| **Filter JS** | `assets/js/main.js` | Accordion, ranges, checks, switches, URL sync, AJAX grid update, global reset |
| **Filter CSS** | `assets/css/style.css` | `.flt__*` layout, `.flt__check.active`, accordion chevron |
| **Controller** | `catalog/controller/product/category.php` | Parses `?filters=`, builds `$custom_filters`, renders checked state in Twig |
| **Model / SQL** | `catalog/model/catalog/product.php` | `filter_custom` → SQL (**out of scope**) |
| **Profiles** | `system/library/zpm/filter_profiles/*.php` | Which attribute groups appear per branch (**out of scope**) |

### 3.2 DOM structure (attribute group)

```html
<div class="flt" data-filters>
  <form class="flt__form" data-filters-form>
    <section class="flt__group" data-acc>
      <button class="flt__group-head" type="button" data-acc-btn>
        <span class="flt__group-title">Конструкция полки</span>
        <span class="flt__chev"></span>
      </button>
      <div class="flt__group-body" data-acc-panel>
        <label class="flt__check">
          <input class="flt__check-input" type="checkbox"
                 name="attr[51][]" value="Без полки" />
          ...
        </label>
      </div>
    </section>
  </form>
</div>
```

**HTML constraint:** `.flt__group-head` — это `<button>`. Кнопку «Сбросить» **нельзя** вкладывать внутрь него. Нужен wrapper (например `.flt__group-headbar`) с соседними элементами: accordion-head + group-reset.

### 3.3 Group types in sidebar

| Block | Selector / name | Input types | Group reset in M9.8.9-08? |
|-------|-----------------|-------------|---------------------------|
| Цена | `price_from`, `price_to` | range + text | **NO** (explicitly excluded) |
| Commerce switches | `in_stock`, `preorder_only`, `only_with_price`, `only_discount` | checkbox switches, not in `.flt__group` | **NO** |
| Габариты | `len_from/to`, `w_from/to`, `h_from/to` | range | **NO** (range deferred) |
| Primary attrs | `attr[{slug|id}][]` | checkbox | **YES** |
| Secondary attrs (nested) | same, inside «Дополнительные параметры» | checkbox | **YES** (per nested group) |
| Подкатегории | `s[]` | checkbox | **NO** — hidden on live since **M9.8.9-07** (`{% if false and filter_subcategories %}`) |
| Footer | `[data-filter-reset]`, `[data-filter-apply]`, `[data-filter-copy]` | — | global reset only |

**Radio / select:** CSS hooks `.flt__select` exist; **no markup in current `filterssidebar.twig`**. Implementation should still handle `.flt__check-input` only; radio/select hooks reserved for future.

---

## 4. Filter pipeline (JS)

**Source:** live capture `reports/m9.8.9-04a-work/live-capture/assets__js__main.js` (filter block ~L4188–4817). Operator manual JS (04B) may differ on live — **re-capture required before deploy**.

### 4.1 Init chain (`onReady`)

```
initAccordions → initShowMore → initRanges → initBrandSearch
→ initSwitches → initChecks → initCopyLink → initReset
→ syncChoiceClasses → initPaginationAJAX
```

Separate block **§5 Filters sidebar (popup manager)** (~L2313): mobile offcanvas via `registerPopup`, duplicate lightweight handler on `[data-filter-reset]` (only `form.reset()` — incomplete vs `initReset`).

### 4.2 User change → AJAX

```
checkbox/switch change
  → syncChoiceClasses(root)
  → updateBrowserUrl(form)
       → getReadableState(form)  // FormData → URLSearchParams → decode + ; separator
       → history.replaceState(?filters=…)
       → debouncedUpdate(root)   // 800ms debounce
            → updateProducts(root)
```

### 4.3 `updateProducts(root)`

1. Read `window.location.search` (preserves `sort`, `order`, `limit`, `page`, `path` via SEO URL).
2. Set/replace/delete `filters` from current form state.
3. `fetch(pathname + query)` → parse HTML.
4. Replace `.category__grid` innerHTML.
5. Replace/remove `.pagination`.
6. `scrollToCategorySection()` (closes mobile filter if open).
7. Re-bind pagination AJAX.

**Does NOT replace:** sidebar form, sort/limit UI, subcategory chips, product count header (if any).

### 4.4 Form serialization

| Function | Behaviour |
|----------|-----------|
| `collectFormState(form)` | `FormData` → skip empty values → `URLSearchParams` |
| `getReadableState(form)` | decode + `[`/`]` unescape + `&` → `;` for readable URL |

**Price always submitted with attr clicks:** `initRanges` → `bindOneRange` → `syncFromRanges()` on init writes min/max into `price_from`/`price_to`. Group reset must **not** clear price fields — other groups' values and switches remain in FormData.

### 4.5 Global reset (`initReset`)

Clears: all checks, all ranges to min/max, switches, search inputs, URL to pathname, then `updateProducts(root)`.

**Duplicate handler risk (known):** early `fReset` listener (~L2394) calls `fForm.reset()` only; `initReset` does full pipeline. Both fire on «Сбросить всё». **Out of scope** for M9.8.9-08 unless group reset work touches same code area — use **distinct hook** `data-filter-group-reset`.

---

## 5. Server-side filter parsing

**Source:** `m9-phase1-tables-work/patch/catalog/controller/product/category.php` (structure confirmed by 06K/06M reports; live assumed aligned post-recovery).

```
GET filters → html_entity_decode → ; → & → parse_str → $custom_filters
```

| Key pattern | Example | Checked state in Twig |
|-------------|---------|----------------------|
| `attr[slug][]` | `attr[construction][]=…` | `$custom_filters['attr'][$slug]` |
| `attr[numeric][]` | `attr[51][]=Без полки` | same (slug = `51`) |
| `s[]` | subcategory IDs | hidden in UI (07) |
| `price_from/to`, dims | numeric, spaces stripped | range selected values |
| switches | `only_with_price=1` | switch checked |

Controller sets `expanded: true` on groups present in `$selected_attributes` — **full page reload only**; AJAX does not refresh sidebar.

---

## 6. Current filter state / «chips»

| Mechanism | Present? | Notes |
|-----------|----------|-------|
| Active filter chips above grid | **NO** | CATEGORY-AUDIT-V1 open item |
| Checkbox visual state | **YES** | `.flt__check.active` via `syncChoiceClasses` |
| URL share link | **YES** | `?filters=attr[51][]=…;only_with_price=1;price_from=…` |
| Top subcategory chips | **YES** | `zpm-sub-cat-chips` in `category.twig` — **navigation links**, not filter state; **do not touch** |
| Server-rendered `checked` | **YES** | On full reload from URL |

**Implication for group reset:** after AJAX, sidebar DOM is authoritative. Group reset must update local inputs + classes; no chip bar to update.

---

## 7. Category branch inventory (QA targets)

| Category | Branch ID | Profile | Attribute groups | Range groups | Notes |
|----------|-----------|---------|------------------|--------------|-------|
| Столы | 301 | `301_stoly` | Many (incl. `attr[51][]`, `attr[47][]`) | price + L/W/H | Primary QA branch |
| Моечные ванны | 80 | `80_moechnye_vanny` | `shell-size`, `washing`, etc. | price + dims | EC-01 open (empty subcats) — unrelated |
| Подтоварники | 322 | `322_podtovarniki` | `51`, `max-load`, … | price + dims | |
| Тележки | 326 | `326_telezhki` | **none** (profile empty) | price + dims only | Group reset N/A for attrs |
| Зонты | 207 | `207_zonty` | minimal / data gap | price | 1 SKU; attr filters may not render |

Numeric keys **47**, **51**: empty `filter_name` in DB → sidebar uses numeric slug; SQL fixed in **06J**.

---

## 8. Recommended implementation approach (for approval phase)

### 8.1 Files in scope

| File | Change |
|------|--------|
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | Add group reset control to attribute group loops only (primary + secondary nested) |
| `assets/js/main.js` | `initGroupReset(root)`, visibility sync, reuse `updateBrowserUrl` |
| `assets/css/style.css` | Minimal `.flt__group-headbar` / `.flt__group-reset` layout |

**Not in scope:** `category.php`, `product.php`, overlay, megamenu, PDP, price index.

### 8.2 Reset algorithm (per group)

1. Click `[data-filter-group-reset]` → `preventDefault` + `stopPropagation` (do not toggle accordion).
2. Scope = closest `[data-acc].flt__group` (attribute groups only; mark with `data-filter-group` if needed).
3. Within `.flt__group-body` / `[data-acc-panel]`:
   - uncheck all `.flt__check-input`
   - remove `.active` from `.flt__check` labels
   - (future) radio → uncheck; select → first/default option
4. **Do not** touch inputs outside this group (price, switches, other attrs, ranges).
5. `syncChoiceClasses(root)` → `updateBrowserUrl(form)` → existing debounced AJAX.

### 8.3 Reset button visibility

| Option | Pros | Cons |
|--------|------|------|
| **A — show only when group has selection** | Cleaner UX; matches task spec | Needs `updateGroupResetVisibility()` on init, check change, group reset, global reset |
| **B — always visible** | Simpler JS | Noise on empty groups; mis-clicks |

**Recommendation: Option A** — function checks `:checked` within group body; toggle `hidden` on reset button. Low risk if wired into existing `syncChoiceClasses` / check handlers.

### 8.4 Header layout (Twig)

Introduce wrapper for attribute groups:

```twig
<div class="flt__group-headbar">
  <button class="flt__group-head" type="button" data-acc-btn …>
    <span class="flt__group-title">{{ group.name }}</span>
    <span class="flt__chev"></span>
  </button>
  <button type="button" class="flt__group-reset" data-filter-group-reset hidden>
    Сбросить
  </button>
</div>
```

Apply to: `{% for group in filter_groups %}`, nested `{% for group in filter_secondary_groups %}`.  
**Skip:** price, dims, switches, subcategories, outer «Дополнительные параметры» container (only inner nested groups).

### 8.5 Interaction with sort / price / only_with_price

| Scenario | Expected |
|----------|----------|
| Reset one attr group | `filters` loses that `attr[key][]`; **price_from/to unchanged**; switches unchanged |
| With `only_with_price=1` | Remains in URL after group reset |
| With `sort=p.price&order=ASC` | Preserved (`updateProducts` reads full `location.search`) |
| With active price range | Unaffected by attr group reset |
| After AJAX | Grid updates; sidebar stays; reset buttons visibility refreshed |
| After full reload | Server renders checked state from URL; reset buttons visibility from init |

---

## 9. QA checklist (implementation phase)

Test on branches: **301, 80, 322, 326, 207**.

1. Reset single attribute group (e.g. `attr[51][]` on Столы).
2. Reset multiple groups sequentially.
3. Reset after AJAX filter change (grid already updated).
4. Reset after full page reload with `?filters=…` in URL.
5. Reset + `only_with_price=1` active.
6. Reset + price sort active (`sort=p.price`).
7. Reset attr group while price range narrowed — price filter still applied, products still filtered by price.

**Тележки (326):** verify no JS errors when no attribute groups exist.  
**Зонты (207):** limited attr UI — smoke test only.

---

## 10. Risks and UNKNOWN

| Item | Level | Notes |
|------|-------|-------|
| Live `main.js` may differ from 04A capture | **MEDIUM** | Operator manual JS canonical — **FTP capture mandatory before deploy** |
| Duplicate global reset handlers | **LOW** | Pre-existing; do not reuse `data-filter-reset` for group reset |
| Accordion + reset click collision | **MEDIUM** | Mitigated by wrapper + `stopPropagation` |
| Sidebar not refreshed on AJAX | **LOW** | Existing behaviour; group reset updates DOM locally |
| Product count element not in AJAX swap | **LOW** | Same as today — count may only update on full navigation |
| `flt__group-head` CSS assumes full-width button | **LOW** | Needs `.flt__group-headbar` flex adjustment |
| M9.8.9-07 subcategories hidden on live | **INFO** | Live capture in 07-work folder predates patch; patched copy has `false and filter_subcategories` |

**SAFE UNKNOWN:** exact live SHA of `filterssidebar.twig` / `main.js` / `style.css` at forensic time — not re-fetched in this pass.

---

## 11. Rollback (implementation phase preview)

1. Restore pre-pass `.bak` files (`backups/*.pre-m9.8.9-08-*`).
2. Or revert three files from `reports/m9.8.9-08-work/live-capture/`.
3. Clear Twig cache on hosting after Twig rollback.

---

## 12. Git status

Forensic pass: **no repository file changes** except this report.

---

## 13. Approval gate

**Awaiting operator approval** before implementation pass:

- `REPORT — M9.8.9-08 FILTER GROUP RESET IMPLEMENTATION`
- Live FTP capture → patch → deploy → QA → SHA manifest

---

*Documentation only — no runtime claimed. No live FTP verification in this forensic pass.*
