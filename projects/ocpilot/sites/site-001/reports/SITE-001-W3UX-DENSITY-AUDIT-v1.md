# SITE-001 W3-UX Density Audit v1

**Type:** Pre-execution discovery — UX density & information efficiency audit  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** W3-UX — Density & Visual Effectiveness (Phase 2)  
**Post-W3-V context:** W3-V CSS refresh applied; operator review — **no meaningful UX gain** (cosmetic layer insufficient)

**Methods:** Read-only HTTP probe · CSS analysis (`css/main.css`, `css/media.css` post-W3-V) · W2 FTP template map cross-reference · structural proxy from `home.twig` card markup (duplicated in `category.twig` / `categorynew.twig` per W2 discovery)

**Explicit exclusions observed:** No FTP · No CSS/Twig/DB edits · No cache ops · No implementation

**Evidence (local, not in git):** `.recovery-temp/site-001-w3ux-density-probe.json` · `.recovery-temp/site-001-w3ux-density-probe.py` · `.recovery-temp/site-001-w3v-work/css__main.css` · `.recovery-temp/site-001-w2-visual-discovery.json`

**Companion decision:** [SITE-001-W3UX-DENSITY-DECISION-v1.md](SITE-001-W3UX-DENSITY-DECISION-v1.md)

---

## Executive summary

Root cause of weak post-W3-V perception: **vertical inflation and weak in-card hierarchy**, not color/radius/shadow. Catalog cards share one CSS system (`.catalog_item`) but **used cards carry ~80–120 px more dead space** than new cards due to image offset and credit block margins. PDP and homepage sections use **50 px section breaks** and **30–50 px interior padding** as defaults — appropriate for marketing landing, excessive for inventory browsing.

| Surface | Primary waste | Estimated recoverable height |
|---------|---------------|------------------------------|
| Used catalog cards | Image top margin, info padding, credit block | **~90–110 px/card** (−17–20%) |
| New catalog cards | Face padding 20 px, credit block, generic OC card rhythm | **~70–90 px/card** (−12–16%) |
| Used PDP | Discount widget, VIN block, credit calculator section margins | **~180–240 px** above fold extension |
| New PDP | Hero photo padding, bonus grid, gallery top margin | **~200–280 px** |
| Homepage | Hero min-height 600 px, section title margins 50 px | **~350–450 px** (first 2 screens) |

**TEST inventory caveat (N-W3UX-01):** HTTP probe 2026-06-09 shows **1** live listing on `/cars/` and `/auto/` vs **14** in W2 discovery (2026-06-09 morning). Density math uses **CSS + W2 structural baseline**; live card count may vary with TEST stock.

---

## TASK 1 — Catalog density audit

### 1.1 Surfaces

| Catalog | URL | Body class | Template (FTP) |
|---------|-----|------------|----------------|
| Used | `/cars/` | `used_catalog` | `product/category.twig` |
| New | `/auto/` | `new_catalog` | `product/categorynew.twig` |

Both use `.catalog_wrap` flex grid and `.catalog_item` card shell. Markup **duplicated** across templates (no shared partial — W2 confirmed).

### 1.2 Current state — grid & card geometry

**Desktop baseline (viewport ≥1281 px, container max 1620 px, `.row` padding 50 px):**

| Metric | Used `/cars/` | New `/auto/` | Source |
|--------|---------------|--------------|--------|
| Columns | **4** (25%) | **4** (25%) | `.catalog_item { width: 25% }` |
| Card outer padding | 10 px | 10 px | `.catalog_item` |
| Grid gutter (effective) | 20 px (margin −10 on wrap) | same | `.catalog_wrap { margin: -10px }` |
| Card inner width @1440 | **~315 px** | **~315 px** | (1440−100)/4 − 20 padding |
| Est. card height | **~520–580 px** | **~560–640 px** | CSS stack sum (see §1.3) |
| Items per page (W2 HTTP) | **14** | **14** | W2 discovery |
| Items above fold @900 px viewport | **~4 partial – 6** | **~4 partial – 5** | Header ~160 px + H1 ~90 px + filter ~100 px |
| White space inside card (est.) | **~32–38%** | **~34–40%** | Padding/margins vs content blocks |

**Breakpoints (`media.css`):**

| Breakpoint | Columns |
|------------|---------|
| ≤1280 px | 3 (33.33%) |
| ≤880 px | 2 (50%) |
| ≤620 px | 1 (100%) |

**Catalog page chrome (above grid):**

| Block | Vertical cost | Notes |
|-------|---------------|-------|
| `.search_wrap` | margin-bottom **50 px** | Filter/search form |
| H1 `.page_sub_title` | margin **50+20 px** | Title row |
| `.brand_catalog` (if visible) | ~50 px × rows | Manufacturer chips on category pages |

### 1.3 Current state — card interior stack

**Used card (`.catalog_item` — structural proxy from `home.twig` + CSS):**

| Zone | CSS drivers | Est. height |
|------|-------------|-------------|
| Tags overlay | `.catalog_item__tags { padding: 15px }` | ~40 px (absolute) |
| Image face | `.catalog_item__img { margin-top: 30px }` + slide image | **~210–240 px** |
| Info pad | `.catalog_item__info { padding: 15px }` | 30 px vertical |
| Name | 20 px + `margin-bottom: 15px` | ~35 px |
| Specs list | 14 px × ~2 rows + `margin-bottom: 15px` | ~45 px |
| Price row | price + VIN column | ~55–70 px |
| Credit strip | `margin-top/bottom: 20px`, `padding-top: 15px` | ~55 px |
| CTA | `.catalog_item__btn { margin-top: 15px; padding: 9px }` | ~38 px |

**New card deltas (`.new_catalog` / `.new_auto`):**

| Delta | Effect |
|-------|--------|
| `.new_auto .catalog_item__img { margin-top: 0 }` | **−30 px** vs used (already better) |
| `.new_catalog .catalog_item__face { padding: 20px }` | **+40 px** vs used face |
| Swiper nav hidden on new | Neutral density |
| Same info/credit/CTA stack | Shared inflation |

**Net:** New cards **taller per face padding** despite better image offset; both feel like **OpenCart product tiles** because price, specs, and CTA share equal visual weight (20 px price, 20 px title, 15 px gaps).

### 1.4 Target state — catalog

| Metric | Target | Mechanism |
|--------|--------|-----------|
| Card height | **−15–20%** used; **−12–16%** new | CSS spacing + image max-height |
| White space ratio (in-card) | **~22–26%** | Padding scale `--w3ux-space-*` |
| Visible cards above fold @1440×900 | **7–9** (full row 2) | Card height ↓ only (no column increase at 1440) |
| Visible cards above fold @1920×1080 | **10–12** | Same |
| Grid columns @1440 | **4** (unchanged) | Readability guard — density via height not width |
| Grid columns @≥1680 (optional phase) | **5** (20%) | **Optional W3UX-C2** — operator approval required |
| Per-page count | **14** (unchanged) | Pagination logic untouched |

### 1.5 Expected UX gain — catalog

| Signal | Expected change |
|--------|-----------------|
| Catalog feels richer | **High** — +1 full row visible without scroll on desktop |
| Vehicle cards feel more valuable | **Medium–High** — price/CTA dominance |
| Site feels less empty | **High** on `/cars/`, `/auto/` |
| Scan speed (3-second test) | **+25–35%** more cards parsed per glance |

---

## TASK 2 — Used car card optimization plan

**Templates:** `catalog/view/theme/auto/template/product/category.twig` (+ homepage/slider duplicates in `home.twig`)

**Constraint:** No new data fields — reorder/hierarchy via CSS only; twig touch only if wrapper classes needed (prefer CSS).

### 2.1 Before (current)

```
┌─────────────────────────────┐
│ [tags pad 15px]             │
│     ↓ margin-top 30px       │  ← largest single waste
│  ┌─────────────────────┐    │
│  │      image          │    │  ~210px, unconstrained height
│  └─────────────────────┘    │
├─────────────────────────────┤
│ pad 15 │ name 20px          │
│        │ specs (14px)       │
│        │ price 20px = VIN   │  ← equal weight
│        │ ─── credit ───     │  ← 55px block
│        │ [CTA btn]          │
└─────────────────────────────┘
~520–580px total
```

### 2.2 After (planned)

```
┌─────────────────────────────┐
│ [tags compact 8px]          │
│  ┌─────────────────────┐    │
│  │ image max-h ~180px  │    │  object-fit: cover
│  └─────────────────────┘    │
├─────────────────────────────┤
│ pad 10│ NAME 18px semibold   │
│       │ specs 13px tight    │
│       │ PRICE 24px/600       │  ← dominant
│       │ credit inline 14px    │  ← demoted, no top border gap
│       │ [CTA full-width 40px] │
└─────────────────────────────┘
~430–480px target
```

### 2.3 Change map (CSS-first)

| # | Selector / block | Current | Target | Savings |
|---|------------------|---------|--------|---------|
| U-01 | `.catalog_item__img { margin-top }` | 30 px | **8 px** | ~22 px |
| U-02 | `.catalog_item__tags { padding }` | 15 px | **8 px** | ~14 px overlay |
| U-03 | `.catalog_item__info { padding }` | 15 px | **10 px** | 10 px |
| U-04 | `.catalog_item__name { margin-bottom }` | 15 px | **6 px** | 9 px |
| U-05 | `.catalog_item__specific { margin-bottom }` | 15 px | **6 px** | 9 px |
| U-06 | `.catalog_item__specific > ul > li` | 14 px, wide gaps | **13 px**, tighter wrap gap | ~6 px |
| U-07 | `.catalog_item__price_main` | 20 px / 500 | **24 px / 600** | hierarchy ↑ (0 px) |
| U-08 | `.catalog_item__vin` | column beside price | **compact row** under price | ~15 px |
| U-09 | `.catalog_item__credit` | mt/mb 20, pt 15, border-top | **mt 8, mb 0, pt 8**, lighter border | ~35 px |
| U-10 | `.catalog_item__btn` | mt 15, pad 9 | **mt 8**, h **40 px** | ~10 px |
| U-11 | `.catalog_item__face .swiper-slide img` | height auto | **max-height 180px; object-fit: cover** | ~20–40 px |

**Twig (only if CSS insufficient):** Wrap price+credit in existing container — **defer**; CSS flex order may suffice.

**W3-V interaction:** W3-V override block at EOF — W3UX edits append **after** W3-V markers or extend `--w3v-*` spacing tokens.

---

## TASK 3 — New car card optimization plan

**Templates:** `categorynew.twig` — class hooks `.new_catalog`, `.new_auto`

### 3.1 Current issue

Cards inherit generic `.catalog_item` e-commerce rhythm: bordered box, centered image, equal-weight title/price, credit strip identical to used inventory. **Face padding 20 px** adds luxury whitespace without information gain. Reads as **OpenCart catalog item**, not **configured vehicle offer**.

### 3.2 Before / after

| Aspect | Before | After |
|--------|--------|-------|
| Face padding | 20 px all sides | **10 px** |
| Image presentation | Floating in padded box | **Edge-to-edge** in face, 4 px radius bottom only |
| Title | 20 px, same as price | **18 px/600** manufacturer+model |
| Trim / year line | Secondary span | **13 px muted**, same line if fits |
| Price | 20 px | **26 px/600** + credit **14 px** subline |
| Credit block | Bordered section 55 px | **Inline subline** under price |
| CTA | Dark bar at bottom | **Primary red full-width 40 px** — single obvious action |
| Stock badge | Same as used | Keep; reduce badge **max-width 80→64 px**, font **12 px** |

### 3.3 CSS selectors (new-car scoped)

```css
.new_catalog .catalog_item__face { padding: 10px; }
.new_catalog .catalog_item__price_main { font-size: 26px; font-weight: 600; }
.new_catalog .catalog_item__credit { border-top: none; margin-top: 8px; padding-top: 0; }
.new_catalog .catalog_item__info { padding: 10px; }
```

**No new blocks** — hierarchy via typography and spacing only.

### 3.4 Expected gain

| Signal | Impact |
|--------|--------|
| “Real offer” perception | **High** |
| Cards per screen | **+1 row** equivalent |
| Parity with used track | **Medium** — intentional new-car face padding removed |

---

## TASK 4 — Used PDP density audit (`product.twig`)

**Sample URL (HTTP 2026-06-09):** `https://sibcar.new-site.space/audi-a1-2012-s-probegom-149-000-km-799`  
**Body class:** `used_car_page`  
**Template:** `product/product.twig` (925 lines, FTP)

### 4.1 Vertical budget map (desktop)

| Section | Key CSS | Est. height | Waste / opportunity |
|---------|---------|-------------|---------------------|
| Breadcrumbs | inline | ~40 px | Low — keep |
| Hero `.car_main_info` | 50/50 split, pad 10 | ~480–560 px | Gallery thumbs padding |
| Gallery `.car_main_info__photo` | width 50%, pad 10 | ~50% of hero | Thumb strip gap |
| Price block | price 30 px, gap 20 | ~90 px | Credit price could inline |
| Discount widget `.car_main_info__discount` | **pad 30, mt 20, gap 20** | **~120–160 px** | **−40–60 px** |
| Characteristics grid | mt 20, item pad 10×25 | ~200–320 px | Item pad **→ 8×16** |
| CTA `.car_main_info__btns` | mt 20, gap 20, h 50 | ~70 px | h **→ 44**, gap **→ 12** |
| VIN check `.car_vin_check` | **mt 50, pad 30, gap 50** | **~140–180 px** | **−50–70 px** |
| Credit `.used_car__credit` | **mt 50, pad 30, gap 50** | **~280–350 px** | **−60–80 px** |
| Benefits / similar | varies | ~200+ px | Section mt **50→24** |

### 4.2 Optimization opportunities (no content removal)

| ID | Area | Change | Est. save |
|----|------|--------|-----------|
| P-U-01 | Gallery | Reduce thumb gutter; main slide **max-height** cap with object-fit | 20–30 px |
| P-U-02 | Discount toggle | padding **30→16**, gap **20→12** | 40 px |
| P-U-03 | Characteristics | cell padding **10×25 → 8×16**, margin-top **20→12** | 30–50 px |
| P-U-04 | CTA row | button height **50→44**, gap **20→12** | 10 px |
| P-U-05 | VIN block | margin-top **50→24**, padding **30→20**, gap **50→24** | 50 px |
| P-U-06 | Credit calculator | margin-top **50→24**, padding **30→20**, gap **50→24** | 60 px |
| P-U-07 | Section rhythm | Global `.used_car_page` section `margin-top: 50px` pattern → **24 px** token | 25 px × N sections |

**Total PDP above-the-fold extension recoverable:** **~180–240 px** without hiding specs, gallery, or forms.

---

## TASK 5 — New PDP density audit (`productnew.twig`)

**Sample URL:** `https://sibcar.new-site.space/baic-bj40-new`  
**Body class:** `new_car_page`  
**Template:** `product/productnew.twig` (671 lines)

### 5.1 Section map

| Section | Key CSS / markup | Issue | Opportunity |
|---------|------------------|-------|-------------|
| Hero `.new_car_main_info__photo` | **padding: 0 50 50 50** | Excessive box padding | **→ 24 px** |
| Color swatches `.new_car__photo_color` | gap 15×20 | Acceptable | gap **→ 10×12** |
| Trim / configuration blocks | `.car_configuration__*` | Vertical stack gaps | tighten row gap |
| Gallery `.car-media` | grid gap **20 px** | Large mosaic gutters | **→ 12 px** |
| Gallery wrapper `.new_car_gallery` | **margin-top: 50 px** | Late fold push | **→ 24 px** |
| Bonuses `.new_car_bonus__item` | **padding 30**, gap 20, 4-col | Tall advantage cards | **pad 16**, gap **12**, 4-col keep |
| CTA `.new_car_main_info__btns` | mt 20, h 48 | OK | mt **→ 12** |
| Hidden slides `.car-media__hidden` | off-screen DOM | No visual cost | **No change** (SEO/DOM preserved) |

### 5.2 Optimization map

| ID | Focus | Target | Est. save |
|----|-------|--------|-----------|
| P-N-01 | Hero photo box | padding **50→24** | 50 px |
| P-N-02 | car-media grid | gap **20→12** | 15–25 px |
| P-N-03 | Bonus grid | item pad **30→16** | 28 px × row |
| P-N-04 | Gallery section break | mt **50→24** | 26 px |
| P-N-05 | Trim blocks | inter-block margin **→ 16** | 20–40 px |
| P-N-06 | CTA cluster | consolidate vertical gaps | 15 px |

**Total new PDP recoverable (first 2 screens):** **~200–280 px**.

---

## TASK 6 — Homepage density audit (`home.twig`)

**URL:** `/` · Template: `common/home.twig` (453 lines)

### 6.1 Section stack (typical)

| Section | Key CSS | Est. height | Reducible? |
|---------|---------|-------------|------------|
| Header (fixed + top) | header ~105–180 px | 105–180 px | **Frozen** |
| Hero slider `.home_slider_content__wrap` | **min-height: 600 px** | **~600 px** | **→ 420–480 px** (−120–180) |
| Slider content pad | `.home_slider_content { padding: 50px }` | included | **→ 32 px** (−36 vertical) |
| Page sub-title margins | `.page_sub_title { margin: 50px 0 20px }` | 70 px × **~4 sections** | **→ 32px 0 16px** (−38 × 4 = **152**) |
| Catalog block (latest arrivals) | same `.catalog_item` | ~560 px / row | defers to Task 2 |
| Special offers slider `.block_slider__wrap` | horizontal — card height | ~560 px | card CSS pass |
| Advantages `.four_blocks.short > div` | **padding 30** | ~180–220 px / row | **→ 16 px** (−28 × 4 = **112**) |
| Partner banks `.partner_banks__item` | **padding 30×10** | ~120 px / slide | **→ 16×8** (−28) |
| Lead form `.fancy_form_block` | large decor + pad | ~400–500 px | pad **−20%** (not structure) |
| Map embed (twig) | **height=500** inline | 500 px | **→ 380** via twig height attr only if authorized |

### 6.2 Vertical reduction estimate (content preserved)

| Scope | Current (est. first 2 viewports) | Target | Reduction |
|-------|----------------------------------|--------|-----------|
| Hero + first catalog title | ~750 px | ~580 px | **~170 px (−23%)** |
| Through advantages + banks | ~2200 px | ~1750 px | **~450 px (−20%)** |
| Full homepage to map | ~4500 px | ~3600 px | **~900 px (−20%)** |

**Question answered:** **~350–450 px** removable in **first two screens** without removing any block; **~900 px** over full homepage scroll through spacing alone.

---

## Cross-cutting findings

| Finding | Severity | W3-UX implication |
|---------|----------|-------------------|
| W3-V changed radius/shadows but not spacing scale | **Root cause** | W3UX must target `--w3ux-space-*` not `--w3v-radius-*` |
| Card markup duplicated in 3+ templates | **Medium** | CSS-only pass covers all; twig sync only if class hooks added |
| Inline styles in PDP/home (6–17 attrs) | **Medium** | Map in execution; do not rely on CSS alone for map height |
| Footer frozen | **Info** | Out of scope — W3-C rollback lesson |
| Header frozen | **Info** | Out of scope |
| TEST sparse inventory | **Low** | Verify density on staging with full grid before sign-off |

---

## Related documents

| Document | Role |
|----------|------|
| [SITE-001-W3V-DECISION-v1.md](SITE-001-W3V-DECISION-v1.md) | Prior wave — cosmetic pass insufficient |
| [SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md](SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md) | Template map · component registry |
| [SITE-001-W2-VISUAL-SPECIFICATION-v1.md](SITE-001-W2-VISUAL-SPECIFICATION-v1.md) | Spacing token baseline |
| [SITE-001-W3UX-DENSITY-DECISION-v1.md](SITE-001-W3UX-DENSITY-DECISION-v1.md) | Gate · top 10 · roadmap |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3-UX density discovery audit (Tasks 1–6) |

*SITE-001 W3-UX Density Audit v1 — discovery only; no site modifications.*
