# SITE-001 W3COLOR-01 Discovery v1

**Type:** Pre-execution discovery — global visual tone & brand atmosphere (read-only)  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** W3COLOR-01 — Global Palette & Atmosphere Refresh  
**Supersedes for direction:** W3VIS-01A / W3VIS-01B (rolled back — task drift)

**Methods:** Read-only HTTP probe · live `css/main.css` + `css/media.css` fetch · cross-reference W2/W3-V/W3V2/W3UX-C1/W3VIS rollback reports  
**Explicit exclusions:** No FTP · No CSS/Twig edits · No cache ops · No implementation

**Evidence (local, not in git):** `.recovery-temp/site-001-w3color-01-probe.json` · `.recovery-temp/site-001-w3color-01-probe.py`

---

## Executive summary

После отката **W3VIS-01A/01B** на TEST активны **W3-V**, **W3V2**, **W3UX-C1**. Маркеры W3VIS отсутствуют — подтверждено live probe.

**Диагноз оператора подтверждён:** предыдущие волны изменили токены и частично палитру, но сайт по-прежнему читается как **OpenCart-шаблон с белыми прямоугольниками, красными акцентами и тёмными полосами**. Причина — не отсутствие красного бренда, а **неполная атмосферная система**: слабый контраст уровней поверхностей, двойной CSS-слой (legacy literals + override block), неоднородная глубина, резкие white/red/black переходы.

**Scope W3COLOR-01:** только визуальный характер — палитра, поверхности, глубина, атмосфера header/footer/cards. **Без** изменения структуры, layout, DOM, Twig, CTA hierarchy, UX density.

| Active layer | Status |
|--------------|--------|
| W3-V (radius/shadow/spacing tokens) | **ACTIVE** |
| W3V2 (color/depth identity) | **ACTIVE** — partial override; legacy literals remain |
| W3UX-C1 (used catalog density) | **ACTIVE** |
| W3VIS-01A / 01B | **ROLLED BACK** |

**Live CSS baseline (2026-06-09):** `main.css` 118 851 bytes / 7 418 lines · `media.css` 31 485 bytes · 38 W3 tokens in `:root` · legacy literals: `rgb(170,3,3)` ×56, `rgb(33,36,43)` ×48, `rgb(208,208,208)` ×24, `border-radius: 4px` ×68.

---

## Scope boundary & OUT OF SCOPE

Следующее **не авторизовано** в W3COLOR-01 и фиксируется как OUT OF SCOPE, если execution потребует:

| ID | Topic | Reason |
|----|-------|--------|
| OOS-01 | PDP hero wrapper / unified hero surface | Структурная перегруппировка — был предмет W3VIS-01A |
| OOS-02 | CTA reorder, flex order, DOM order | Hierarchy change |
| OOS-03 | Catalog density, spacing compression | UX density — W3UX domain |
| OOS-04 | Typography hierarchy redesign (price sizes, heading tiers) | Hierarchy, not atmosphere |
| OOS-05 | Navigation / footer / header restructuring | Structure |
| OOS-06 | Block removal or relocation | Structure |
| OOS-07 | Content edits | Content |

W3COLOR **может** менять: `background-color`, `border-color`, `box-shadow`, `color`, `border-radius` (в рамках существующих элементов), градиенты, `backdrop-filter`, opacity — **без** изменения размеров, padding, margin, flex, order, display layout.

---

## 1. Global Palette — текущее состояние

### 1.1 Доминирующая триада white / red / near-black

| Роль | Текущее значение | Hits (live) | Визуальный эффект |
|------|------------------|-------------|-------------------|
| Surface white | `#FFFFFF` / `rgb(255,255,255)` | 73+ | Карточки, header bar, формы — «листы A4» |
| Brand red | `rgb(170, 3, 3)` + W3V2 `rgb(158, 2, 2)` | 56 legacy + token | Агрессивный discount-retail контраст |
| Dark chrome | `rgb(33, 36, 43)` | 48 legacy | Nav, footer, dark bands — плоский charcoal |
| Harsh seam | `rgb(14, 15, 16)` / `rgb(16, 18, 21)` | 6+ | Почти чёрные border-top/bottom — «дешёвый рез» |
| Flat grey border | `rgb(208, 208, 208)` | 24 | OpenCart-era card outline |
| Body canvas | W3V2 `#F7F8FA` | token | Δ luminance vs card ~1–2% — **незаметно** |

**Почему выглядит дёшево:** палитра бинарна — либо чистый белый, либо тёмный graphite, либо насыщенный красный. Нет промежуточных **noble neutrals** (warm/cool stone, soft blue-grey), нет атмосферных переходов между уровнями.

### 1.2 W3V2 vs legacy — двойной слой

W3V2 добавил `--w3v2-*` и override block (~272 строки), но **базовые правила сохраняют legacy literals**. Примеры из live CSS:

- `.catalog_item > a` — border `rgb(208, 208, 208)` в base + override на `--w3v2-border-strong` — cascade зависит от специфичности
- `.car_main_info__price_main` — `color: rgb(170, 3, 3)` в base, token только в override (если есть)
- `footer` base — `rgb(33, 36, 43)`; W3V2-E переопределяет на `--w3v2-dark-main` (#2B2F38) — но `#2B2F38` в файле всего **2 hits**

**Вывод:** визуальная система **не атомарна** — часть страницы рендерится «до W3V2», часть «после».

### 1.3 Graphite migration map (рекомендация discovery)

| Surface | Сейчас | W3COLOR target |
|---------|--------|----------------|
| `body` canvas | `#F7F8FA` (слишком близко к white) | Cool stone canvas (см. palette) |
| `nav`, `.offcanvas_nav` | Legacy `#21242B` + harsh borders | Unified graphite + soft seam |
| `footer`, `.footer_top` | Legacy dark + 10px near-black borders | Layered graphite gradient |
| `.fancy_form_block`, `.used_car__credit` | Flat `rgb(33,36,43)` + bg image | Refined graphite + subtle gradient overlay |
| `.home_slider_content::after` | `rgba(33,36,43,0.9)` flat | Frosted graphite glass |
| `.popup__FORM_wrap` (dark variant) | `rgb(14, 15, 16)` | `--w3color-dark-deep` |
| Card borders | `#D5DAE2` / `rgb(208,208,208)` mix | Single refined border token |

**Бренд красный СИБКАР сохраняется** — меняется **окружение**, не логотип и не primary CTA fill.

---

## 2. Surface System — inventory

| Surface | Selector / region | Current L-level | Depth | Problem |
|---------|-------------------|-----------------|-------|---------|
| **Canvas** | `body` | Canvas | none | Near-white; sections don't recede |
| **Header bar** | `.singe_bar__wrap` | L2 card | shadow-sm | White island; nav below is dark — sharp jump |
| **Nav** | `nav`, `.offcanvas_nav` | L1 dark | box-shadow harsh | Flat dark band |
| **Catalog cards** | `.catalog_item > a/div` | L2 | sm + legacy hover | Dual border/shadow recipes |
| **Filter form** | `.search_wrap`, `.search_form` | L2 (same as cards) | minimal | Indistinguishable white box |
| **Partner banks** | `.partner_banks__item` | L2 | sm | Empty white pad 30px — flat |
| **Advantages** | `.four_blocks > div` | L2 (legacy) | **none** | 4px radius, grey border — pre-W3V2 |
| **Reviews** | `.reviews__item > .inner` | L2 | sm/md | OK in W3V2 group |
| **Lead form band** | `.fancy_form_block` | L1 dark | bg image | Same dark language as nav |
| **Home slider panel** | `.home_slider_content::after` | L1 overlay | blur 4px | Heavy opaque panel |
| **PDP photo column** | `.car_main_info__photo` | unlayered | none | No surface — fragments float |
| **PDP info column** | `.car_main_info__main` | unlayered | none | Same |
| **Discount widget** | `.car_main_info__discount` | L2 nested | border | White island inside column |
| **Credit block** | `.used_car__credit` | L1 dark | image | Reads as second footer |
| **VIN block** | `.car_vin_check` | L2 | sm (W3V2) | Dark band + card mix |
| **Footer** | `footer` | L1 dark | none | Flat; heavy legal text same white |
| **Popups** | `.popup__FORM_wrap` | L2/L1 mix | md | Dark vs white variants inconsistent |

**Pattern:** 8+ component families share **один рецепт** (white + 1px border + shadow-sm), но **four_blocks**, **search_form**, **PDP fragments**, **homepage sections** остаются в legacy — отсюда ощущение «OpenCart collage».

---

## 3. Depth System — текущее состояние

### 3.1 Active tokens (W3V2)

| Token | Current value |
|-------|---------------|
| `--w3v2-shadow-sm` | `0 1px 2px rgba(43,47,56,0.06), 0 2px 4px rgba(43,47,56,0.04)` |
| `--w3v2-shadow-md` | `0 2px 8px rgba(43,47,56,0.08), 0 4px 16px rgba(43,47,56,0.05)` |
| `--w3v2-shadow-lg` | `0 4px 12px rgba(43,47,56,0.10), 0 8px 28px rgba(43,47,56,0.07)` |

**47** `box-shadow` rules in live CSS; W3V2 applied to card group, header, forms — **но**:

- Legacy catalog hover: `0px 0px 5px -1px rgba(55, 76, 96, 0.4)` — другой hue (blue-grey), конкурирует с graphite shadows
- `.four_blocks` — **no shadow**
- `.search_form` — **no elevation**
- Footer — **no depth** (flat dark mass)
- PDP hero fragments — **no nested layering**

### 3.2 Depth gaps (visual only)

| Gap | Where |
|-----|-------|
| Cards flat at rest on some breakpoints | Legacy hover-only elevation |
| Forms merge with canvas | Filter/search same fill as body-adjacent white |
| Dark sections flat | Nav, footer, fancy_form — no inner highlight |
| No inset highlights | Premium cards often use 1px top highlight — absent |
| Red glow legacy | `0 0 10px rgb(170,3,3)` on focus — cheap neon vs soft focus ring |

---

## 4. Footer Atmosphere

**Structure frozen.** Только визуальные рекомендации.

| Aspect | Current | Recommendation |
|--------|---------|----------------|
| Background | Flat `--w3v2-dark-main` / legacy `#21242B` | Vertical gradient: `#2F343E` → `#252932` (top lighter — «потолок») |
| Top/bottom seam | `10px solid rgb(14,15,16)` (legacy) | Replace with `1px solid rgba(255,255,255,0.06)` + optional 4px `--w3color-dark-deep` accent |
| Section dividers | `border-bottom: 1px solid rgba(255,255,255,0.7)` on titles | Softer `rgba(236,238,242,0.12)` — less chalky |
| Text | Pure `#fff` on dark | `--w3color-text-on-dark` primary; legal → muted `#A8AEB8` |
| CTA buttons in footer | Same red as header | Keep red; add subtle `shadow-cta` for depth on dark bg |
| Brand presence | Logo white | Optional faint red accent line under logo zone (`2px`, 40px width, `--w3color-brand-red`) |
| Depth | None | Very subtle inner shadow `inset 0 1px 0 rgba(255,255,255,0.04)` on `.footer_top` |

**OUT OF SCOPE:** accordion legal, form consolidation, link removal.

---

## 5. Header Atmosphere

**Structure frozen.** Расположение logo / phone / callback / nav без изменений.

| Aspect | Current | Recommendation |
|--------|---------|----------------|
| `.singe_bar__wrap` | White card + bottom border | Keep white L2; add **hairline** top highlight `inset 0 1px 0 rgba(255,255,255,0.8)` |
| Shadow | `--w3v2-shadow-sm` | Slightly stronger `--w3color-shadow-header`: md-sm hybrid for separation from canvas |
| Nav transition | White header → dark nav — hard cut | Nav top border: `rgba(255,255,255,0.05)` instead of `rgb(16,18,21)` |
| Nav background | Flat graphite | Subtle gradient `#2F343E` → `#2B2F38` |
| Scroll header | Duplicate bars | Same token treatment (visual parity only) |
| Logo subtitle | `.logo > span` | Muted `--w3color-text-secondary` — less competing with red CTAs |

**OUT OF SCOPE:** reduce CTA count, reorder buttons, change nav items.

---

## 6. Card Language — unified system

**Structure frozen.** Единый визуальный язык для всех card-like surfaces:

| Card family | Include in W3COLOR | Proposed treatment |
|-------------|-------------------|-------------------|
| Catalog | `.catalog_item > a/div` | L2: white fill, `--w3color-border`, `shadow-sm`, radius `--w3v-radius-lg` (10–12px) |
| Banks | `.partner_banks__item` | Same L2 recipe |
| Reviews | `.reviews__item > .inner` | Same |
| Advantages | `.four_blocks > div` | **Migrate into L2 group** (currently legacy 4px) |
| Service / two-col | `.fancy_two_blocks__item` | Same |
| New car bonus | `.new_car_bonus__item` | Same |
| Form panels | `.search_form`, filter panels | **L2-alt**: `--w3color-surface-raised` (#FAFBFC) — distinct from product cards |
| Config / trim | `.newcar_config__item_inner` | L2 white |
| Contact blocks | `.contacts_info_block > div` | L2 |

**Card micro-language (all L2):**

- Rest: `background: --w3color-surface-card`, `border: 1px solid --w3color-border`, `box-shadow: --w3color-shadow-sm`, `border-radius: 12px`
- Hover: `box-shadow: --w3color-shadow-md`, `border-color: --w3color-border-hover` — **no** translateY if density wave forbids motion change; if motion already in W3-V, preserve
- Optional premium cue: `inset 0 1px 0 rgba(255,255,255,0.65)` on card top edge

---

## Top 20 Visual Problems

**Только визуальные.** Без UX, conversion, hierarchy.

| Rank | ID | Problem | Severity | Surfaces |
|------|-----|---------|----------|----------|
| 1 | **VP-01** | **Canvas vs card contrast negligible** — `#F7F8FA` vs `#FFFFFF` ~1–2% luminance | Critical | Sitewide |
| 2 | **VP-02** | **Dual CSS layer** — 56× legacy red, 48× legacy dark, 24× legacy grey borders coexist with W3V2 overrides | Critical | Sitewide |
| 3 | **VP-03** | **White/red/black triad** — no intermediate noble neutrals; reads discount retail | Critical | Sitewide |
| 4 | **VP-04** | **Identical white rectangles** — cards, filters, four_blocks, forms share same flat fill | Critical | Catalog, home, about |
| 5 | **VP-05** | **four_blocks stuck in pre-W3V2** — 4px radius, `rgb(208,208,208)` border, no shadow | High | `/`, `/about` |
| 6 | **VP-06** | **Harsh near-black seams** — `rgb(14,15,16)` / `rgb(16,18,21)` nav/footer borders | High | Header, footer |
| 7 | **VP-07** | **Footer flat dark mass** — no gradient, no depth, heavy white text | High | Footer |
| 8 | **VP-08** | **Header-to-nav hard cut** — white bar then instant dark band | High | Header |
| 9 | **VP-09** | **Legacy catalog hover shadow** — blue-grey `rgba(55,76,96,0.4)` vs graphite W3V2 system | High | Catalog |
| 10 | **VP-10** | **Inconsistent border radius** — 68× `4px` legacy vs `--w3v-radius-lg` on subset | High | Cards, forms |
| 11 | **VP-11** | **Search/filter form visually equals product card** — same white+border, no alt surface | High | `/cars/`, `/auto/` |
| 12 | **VP-12** | **PDP columns lack surface treatment** — photo and info float without shared atmosphere | High | Used + new PDP |
| 13 | **VP-13** | **Dark content bands reuse nav/footer chrome** — fancy_form, credit, VIN same flat `#21242B` | High | PDP, home, about |
| 14 | **VP-14** | **Home slider overlay opaque** — `rgba(33,36,43,0.9)` panel feels heavy not premium | Medium | `/` |
| 15 | **VP-15** | **Popup dark variant near-black** — `rgb(14,15,16)` colder than graphite system | Medium | Modals |
| 16 | **VP-16** | **Stock green neon** — `rgb(0,170,0)` tags clash with refined palette | Medium | Catalog |
| 17 | **VP-17** | **Red focus glow legacy** — `0 0 10px rgb(170,3,3)` on inputs | Medium | Forms |
| 18 | **VP-18** | **Partner bank cards empty white** — large padding, no inner structure | Medium | Sitewide slider |
| 19 | **VP-19** | **Body text color split** — base `rgb(18,18,43)` vs token `#2B2F38` | Medium | Sitewide |
| 20 | **VP-20** | **Inline styles bypass tokens** — 9–17 inline styles per page | Medium | All probed URLs |

---

## New Palette Proposal

**Namespace:** `--w3color-*` (new wave; bridges from `--w3v2-*` where compatible)

### Brand (preserve СИБКАР red)

| Token | Hex / RGB | Usage |
|-------|-----------|-------|
| `--w3color-brand-red` | `#9E0202` / `rgb(158, 2, 2)` | Primary CTA, swiper, key accents — **retain W3V2** |
| `--w3color-brand-red-hover` | `#BA0000` / `rgb(186, 0, 0)` | Hover |
| `--w3color-brand-red-soft` | `rgba(158, 2, 2, 0.08)` | Tint bands, subtle highlights |
| `--w3color-brand-red-muted` | `#B82424` | Large text accents (price) — slightly desaturated vs CTA |

### Graphite / dark atmosphere

| Token | Hex | Usage |
|-------|-----|-------|
| `--w3color-dark-main` | `#2F343E` | Nav, footer base — **warmer/lighter than W3V2** |
| `--w3color-dark-secondary` | `#3A404C` | Elevated dark panels |
| `--w3color-dark-deep` | `#1A1D24` | Seam accents (replaces near-black) |
| `--w3color-dark-gradient-top` | `#353A45` | Footer/header gradient start |
| `--w3color-dark-gradient-bottom` | `#272B33` | Footer/header gradient end |

### Surfaces / neutrals

| Token | Hex | Usage |
|-------|-----|-------|
| `--w3color-canvas` | `#EEF1F5` | **Body** — stronger separation from cards (~5% Δ) |
| `--w3color-surface-card` | `#FFFFFF` | L2 cards |
| `--w3color-surface-raised` | `#FAFBFC` | L2-alt: filters, tool panels |
| `--w3color-surface-sunken` | `#E4E8ED` | L3 inset: tags, chip backgrounds |
| `--w3color-surface-tint` | `#F4F6F9` | Section bands (optional homepage) |

### Borders

| Token | Value | Usage |
|-------|-------|-------|
| `--w3color-border` | `rgba(47, 52, 62, 0.10)` | Default card border |
| `--w3color-border-strong` | `#CDD3DC` | Emphasis border |
| `--w3color-border-hover` | `rgba(47, 52, 62, 0.16)` | Hover state |
| `--w3color-border-on-dark` | `rgba(236, 238, 242, 0.10)` | Footer/header dividers |

### Text

| Token | Hex | Usage |
|-------|-----|-------|
| `--w3color-text-main` | `#2A2F38` | Body |
| `--w3color-text-secondary` | `#5A6270` | Labels |
| `--w3color-text-muted` | `#8B939F` | Meta, legal |
| `--w3color-text-on-dark` | `#EDEFF3` | Footer/nav primary |
| `--w3color-text-on-dark-muted` | `#A8AEB8` | Footer legal |

### Semantic

| Token | Hex | Usage |
|-------|-----|-------|
| `--w3color-success` | `#1F8A4C` | Stock badges — replace neon green |
| `--w3color-whatsapp` | `#25A244` | Preserve distinct green |

---

## Surface Levels

| Level | Token fill | Border | Shadow | Examples |
|-------|------------|--------|--------|----------|
| **Canvas** | `--w3color-canvas` | none | none | `body`, page background between sections |
| **L1** | `--w3color-dark-main` (+ gradient) | `--w3color-border-on-dark` | optional inset highlight | `nav`, `footer`, `.fancy_form_block`, `.used_car__credit` shell |
| **L2** | `--w3color-surface-card` | `--w3color-border` | `--w3color-shadow-sm` | `.catalog_item`, banks, reviews, four_blocks, bonus items |
| **L2-alt** | `--w3color-surface-raised` | `--w3color-border` | `--w3color-shadow-sm` | `.search_form`, filter panels — **visually distinct tool layer** |
| **L3** | `--w3color-surface-sunken` | subtle or none | none | tags, chips, nested cells, discount inner strip |

**Elevation rule:** each level must be **visually distinguishable at arm's length** without changing element sizes.

---

## Depth System

| Token | Value | Usage |
|-------|-------|-------|
| `--w3color-shadow-sm` | `0 1px 2px rgba(42, 47, 56, 0.05), 0 2px 6px rgba(42, 47, 56, 0.04)` | L2 rest — catalog, banks, forms |
| `--w3color-shadow-md` | `0 2px 8px rgba(42, 47, 56, 0.07), 0 6px 20px rgba(42, 47, 56, 0.05)` | L2 hover, dropdowns, popups |
| `--w3color-shadow-lg` | `0 4px 14px rgba(42, 47, 56, 0.08), 0 12px 32px rgba(42, 47, 56, 0.06)` | Modals, elevated marketing panels |
| `--w3color-shadow-inset-highlight` | `inset 0 1px 0 rgba(255, 255, 255, 0.60)` | Premium card top edge |
| `--w3color-shadow-header` | `0 2px 8px rgba(42, 47, 56, 0.06), 0 1px 0 rgba(42, 47, 56, 0.04)` | Header bar separation |
| `--w3color-shadow-cta` | `0 4px 14px rgba(158, 2, 2, 0.20)` | Primary buttons — soft red depth |
| `--w3color-shadow-focus` | `0 0 0 3px rgba(158, 2, 2, 0.18)` | Replace red glow |

**Policy:** layered graphite shadows only; **no** aggressive red outer glow on forms; **no** neon focus rings.

---

## Header Recommendations (structure unchanged)

1. **Canvas contrast** — body `#EEF1F5` makes white header bar read as floating L2.
2. **Header bar** — keep white; add `--w3color-shadow-header` + hairline inset highlight.
3. **Nav graphite** — gradient `#353A45` → `#2F343E`; replace `rgb(16,18,21)` borders with `--w3color-border-on-dark`.
4. **Logo subtitle** — `--w3color-text-secondary` on light; no layout change.
5. **Offcanvas** — match nav gradient tokens for visual continuity.
6. **CTA buttons** — keep current fills/positions; refine hover to `--w3color-shadow-cta` only.

---

## Footer Recommendations (structure unchanged)

1. **Graphite gradient background** — `--w3color-dark-gradient-top` → `--w3color-dark-gradient-bottom`.
2. **Remove heavy 10px near-black borders** — replace with 1px `--w3color-border-on-dark`.
3. **Legal text** — `--w3color-text-on-dark-muted`; entity names stay `--w3color-text-on-dark`.
4. **Section title dividers** — lower contrast `rgba(237,239,243,0.12)`.
5. **Subtle brand accent** — 2px red line under logo area (decorative, no markup change — CSS pseudo on existing wrapper).
6. **Footer CTA depth** — soft shadow on red buttons against dark bg.

---

## Card System Recommendations (structure unchanged)

1. **Unify L2 recipe** across catalog, banks, reviews, four_blocks, bonus, fancy_two_blocks.
2. **Migrate four_blocks** into W3V2 card group — highest-impact missing piece.
3. **L2-alt for filters** — `--w3color-surface-raised` distinguishes tool UI from merchandise cards **visually only**.
4. **Radius** — standardize visible cards to `12px` (`--w3v-radius-lg`); legacy `4px` purged in override pass.
5. **Kill dual hover shadows** — remove legacy `rgba(55,76,96,0.4)` catalog hover.
6. **Tags/chips** — `--w3color-surface-sunken` background; success `--w3color-success`.
7. **Inset highlight** — optional top edge on L2 for premium feel.

---

## Top 10 Changes By Visual Impact

**Только визуальное влияние.** Порядок execution-friendly.

| Rank | Change | Impact | Scope |
|------|--------|--------|-------|
| 1 | **Strengthen canvas** `#F7F8FA` → `#EEF1F5` | Immediate sitewide depth | `body` token |
| 2 | **Complete legacy literal purge** to `--w3color-*` | Eliminates patchy dual-layer look | Full override pass |
| 3 | **Unify four_blocks + search_form** into card/L2-alt system | Homepage/about/catalog stop looking legacy | 3 selector groups |
| 4 | **Footer + nav atmospheric upgrade** (gradient, soft seams) | Premium brand shell | Dark L1 surfaces |
| 5 | **Single shadow language** — remove blue-grey legacy hovers | Cohesive depth | Catalog + cards |
| 6 | **Header floating bar** — stronger separation shadow | Cleaner top | `.singe_bar__wrap` |
| 7 | **Refined dark bands** — fancy_form, credit, slider overlay | Less «second footer» | Dark L1 content |
| 8 | **Border radius harmonization** 4px → 12px on card families | Modern vs OC template | Card selectors |
| 9 | **Success/tag color refinement** | Less neon | Tags, stock |
| 10 | **Popup/modal surface alignment** | Consistent modals | `.popup__FORM_wrap` |

---

## Implementation notes (for future charter — NOT authorized)

| File | Role |
|------|------|
| `css/main.css` | Append `--w3color-*` block + comprehensive override; bridge `--w3v2-*` → `--w3color-*` |
| `css/media.css` | Responsive shadow/radius parity |

**Preserve:** W3UX-C1 density rules (`.used_catalog` scoped) · layout/spacing literals · Twig/PHP/JS untouched.

**Rollback tier:** T1 — CSS file restore from pre-w3color backup.

---

## Финальный вопрос Discovery

### Насколько изменится визуальное восприятие?

**Шкала 1–10** (10 = сайт выглядит как другой продукт, 1 = без изменений):

| Scenario | Score | Rationale |
|----------|-------|-----------|
| Текущее состояние (post-W3V2, post-W3VIS rollback) | **3/10** | Токены есть; ощущение «тот же OC-шаблон» сохраняется |
| **Только W3COLOR visual pass** (palette + surfaces + depth, без structure) | **6/10** | Заметно дороже/чище/объёмнее; узнаваемый СИБКАР; layout тот же |
| W3COLOR + hierarchy waves (OUT OF SCOPE) | 8/10 | Not authorized |

**Вывод:** CSS-only атмосферный refresh **без** structural changes может поднять восприятие с ~**3/10** до ~**6/10**. Полная трансформация «не OpenCart» без layout changes **недостижима** — DOM structure itself signals template origin.

### 5 изменений с максимальным результатом

1. **Canvas uplift** — `#EEF1F5` body vs white L2 cards (instant layered feel).
2. **Full token purge** — zero legacy `rgb(170,3,3)` / `rgb(208,208,208)` / `rgb(33,36,43)` in rendered rules.
3. **Footer + nav premium graphite** — gradients + soft seams instead of near-black cuts.
4. **Card system completion** — four_blocks, filters, all card families one L2 language.
5. **Unified depth** — single shadow stack; remove legacy hover shadows and red glow focus.

---

## Authorization state

| Gate | Status |
|------|--------|
| W3COLOR-01 discovery | **DONE** — this document |
| W3COLOR-01 write charter | **NOT AUTHORIZED** |
| W3COLOR-01 execution | **NOT AUTHORIZED** |
| W3VIS-01A / 01B re-execution | **NOT AUTHORIZED** (rolled back) |
| Production | **FORBIDDEN** |

---

## Related documents

| Document | Role |
|----------|------|
| [SITE-001-W3VIS-ROLLBACK-DECISION-v1.md](SITE-001-W3VIS-ROLLBACK-DECISION-v1.md) | Rollback context; Global Palette Refresh = next |
| [SITE-001-W3V2-EXECUTION-v1.md](SITE-001-W3V2-EXECUTION-v1.md) | Active baseline partially superseded by W3COLOR proposal |
| [SITE-001-W3VIS-01-DISCOVERY-v1.md](SITE-001-W3VIS-01-DISCOVERY-v1.md) | Hierarchy findings — **OUT OF SCOPE** for W3COLOR |
| [SITE-001-W2-VISUAL-SPECIFICATION-v1.md](SITE-001-W2-VISUAL-SPECIFICATION-v1.md) | Phase 2 token reference |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3COLOR-01 discovery; live HTTP probe; no site modifications |

*SITE-001 W3COLOR-01 Discovery v1 — discovery only; no FTP, CSS, or Twig changes.*
