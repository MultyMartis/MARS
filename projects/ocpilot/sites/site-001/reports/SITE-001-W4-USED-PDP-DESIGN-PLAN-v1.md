# SITE-001 W4 Used PDP Design Plan v1

**Type:** Pre-implementation design plan — structural-visual slice  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Target:** `https://sibcar.new-site.space/audi-a1-2012-s-probegom-149-000-km-799`  
**Template:** `catalog/view/theme/auto/template/product/product.twig` (925 lines) · body class `used_car_page`

**Discovery evidence:** FTP fetch 2026-06-09 · `.recovery-temp/site-001-w4-work/discovery-meta.json` · backup `pre-w4-20260609`

---

## 1. Problem statement

Prior waves (W3-V, W3V2, W3UX-C1, W3ATMOSPHERE-01) applied **CSS-only** incremental overrides. Technical audit confirmed CSS loads correctly. Root cause of invisible change: **deltas too weak** + **OpenCart-like anatomy unchanged** — 50/50 flex fragments, competing white cards, dark graphite bands cloned from nav/footer.

W4 addresses **composition**, not atmosphere tokens alone.

---

## 2. Current anatomy (before)

```
used_car__wrapper
├── short_btns                    ← loose text row
├── car_main_info                 ← NO outer shell
│   ├── car_main_info__photo 50%  ← pad 10, no edge-to-edge
│   └── car_main_info__main 50%     ← price + discount card + specs + CTAs stacked
├── car_vin_check                   ← dark graphite band (nav clone)
├── lcd_display.product
├── car_configuration               ← flat list, 3-col
└── (outside wrapper)
    used_car__credit                ← dark + bg image, cheap form inputs
```

**OpenCart widget stack signals:** four competing objects in hero column; discount white card; dashed spec rows; all CTAs same visual weight; VIN block = footer chrome clone.

---

## 3. Target anatomy (after)

```
used_car__wrapper
├── short_btns.w4-used-badges       ← pill status chips
├── w4-used-hero                    ← NEW wrapper — single L2 card
│   └── car_main_info               ← unified shell (radius, shadow, overflow hidden)
│       ├── car_main_info__photo.w4-used-hero__gallery
│       └── car_main_info__main.w4-used-hero__panel
│           ├── w4-used-hero__offer       ← price + credit + discount
│           ├── w4-used-hero__specs       ← 4-col card grid
│           └── w4-used-hero__actions     ← commercial CTA bar
├── car_vin_check.w4-used-trust-strip     ← light premium strip
├── lcd_display.product                   ← UNCHANGED
├── car_configuration.w4-used-equipment   ← card + 2-col scan grid
└── used_car__credit.w4-used-credit         ← premium conversion panel
```

---

## 4. Exact blocks to group

| Group ID | Wrapper class | Contains (existing elements) |
|----------|---------------|----------------------------|
| G-01 | `w4-used-badges` (class on `short_btns`) | `#viewers`, stock badge, condition badge |
| G-02 | `w4-used-hero` | entire `.car_main_info` |
| G-03 | `w4-used-hero__gallery` (class on photo) | Swiper main + thumbs — **all twig loops preserved** |
| G-04 | `w4-used-hero__panel` (class on main) | right column container |
| G-05 | `w4-used-hero__offer` | `.car_main_info__main__top_wrap` → price + discount |
| G-06 | `w4-used-hero__specs` | `.car_main_info__characteristics` (8 items) |
| G-07 | `w4-used-hero__actions` | `.car_main_info__btns` (3 modal links) |
| G-08 | `w4-used-trust-strip` (class on vin check) | title + 4 trust cells + VIN CTA |
| G-09 | `w4-used-equipment` (class on configuration) | complect HTML + toggle |
| G-10 | `w4-used-credit` (class on credit) | calculator + form + car image slider |

---

## 5. Exact existing elements to preserve

| Element | Twig variables / hooks | Preserve |
|---------|------------------------|----------|
| Breadcrumbs | `{% for breadcrumb in breadcrumbs %}` | **YES** — untouched |
| H1 desktop/mobile | `{{ heading_title }}` | **YES** |
| Gallery | `thumb`, `images`, `popup`, Fancybox `data-fancybox` | **YES** — zero hook changes |
| Swiper classes | `car_main_gallery`, `car_main_gallery__thumbs`, nav buttons | **YES** |
| Price | `{{ price }}`, `{{ oldprice }}`, credit note text | **YES** |
| Credit price | `{{ credit }}` | **YES** |
| Discount toggles | 3 rows, `data-amount`, `.active` class | **YES** — markup unchanged inside |
| Specs | `year`, `owners`, `kmrange`, `evolume`, `epower`, `nwd`, `engine`, `kpp` | **YES** |
| CTAs | `#credit__FORM_popup`, `#tradein__FORM_popup`, `#installment__FORM_popup` | **YES** |
| VIN block copy | static trust labels + `{{ kmrange }}` | **YES** |
| VIN CTA | `#VIN_lead_popup` Fancybox | **YES** |
| LCD marquee | both header + product blocks | **YES** |
| Equipment | `{{ complect }}`, `#toggleConfigBtn` | **YES** |
| Credit calc | hidden inputs, `#loanTerm`, `#monthlyPayment`, form POST | **YES** |
| Inline `<script>` | jQuery form handlers lines 825–924 | **YES** — verbatim |
| Popups | `#VIN_lead_popup`, `#VIN_report_popup` | **YES** |
| Reviews widget | `sw-app` | **YES** |
| Similar / offers sliders | `products_marka`, `products_offer` loops | **YES** |
| `{{ header }}`, `{{ footer }}` | includes | **YES** |

---

## 6. Exact markup additions

| Addition | Type | Location |
|----------|------|----------|
| `w4-used-badges` | class | `short_btns` |
| `<div class="w4-used-hero">` | wrapper open | before `.car_main_info` |
| `</div>` | wrapper close | after `.car_main_info` |
| `w4-used-hero__gallery` | class | `.car_main_info__photo` |
| `w4-used-hero__panel` | class | `.car_main_info__main` |
| `<div class="w4-used-hero__offer">` | wrapper | around `__main__top_wrap` |
| `<div class="w4-used-hero__specs">` | wrapper | around `__characteristics` |
| `<div class="w4-used-hero__actions">` | wrapper | around `__btns` (removes extra empty `<div>`) |
| `w4-used-trust-strip` | class | `.car_vin_check` |
| `w4-used-equipment` | class | `.car_configuration` |
| `w4-used-credit` | class | `.used_car__credit` |

**No new text content. No SEO/meta changes. No PHP/JS edits.**

---

## 7. Exact CSS goals (scoped `.used_car_page`)

| Zone | Selector root | Visual goal |
|------|---------------|-------------|
| Badges | `.w4-used-badges > div` | White pill chips, red icon accent, subtle shadow |
| Hero shell | `.w4-used-hero .car_main_info` | 16px radius, 14px shadow, 1px border, overflow hidden |
| Gallery | `.w4-used-hero__gallery` | Dark backdrop, 440px object-fit cover, thumb active red ring |
| Offer | `.w4-used-hero__offer` | Gradient band, price **42px/700**, credit in red tint pill |
| Discount | `.w4-used-hero__offer .car_main_info__discount` | Demoted to `#f3f5f8` inset strip — no competing white card |
| Specs | `.w4-used-hero__specs` | CSS grid 4→3→2 cols; card cells; uppercase muted labels |
| CTA | `.w4-used-hero__actions` | Primary flex 1.35, 52px, red shadow; secondaries outline |
| Trust | `.w4-used-trust-strip` | **Light** white card; green pill status; red outline VIN btn |
| Equipment | `.w4-used-equipment` | White card shell; 2-col items with red checkmarks |
| Credit | `.w4-used-credit` | Dark gradient panel; inset main; white form inputs; styled submit |

**CSS placement:** append after `/* END W3ATMOSPHERE-01 */` in `main.css`; responsive block in `media.css`.

**Tokens:** `--w4-hero-radius`, `--w4-hero-shadow`, `--w4-surface-muted`, `--w4-trust-accent` in `:root` inside W4 block.

---

## 8. What will visually change

| Area | Before | After |
|------|--------|-------|
| Status row | Plain text | Pill badges |
| Hero | Two padded halves, no shell | **Single showroom card** |
| Gallery | Small padded slides | **Full-bleed 440px crop** |
| Price | 34px in column | **42px commercial headline** |
| Discount | White bordered card | Nested grey strip |
| Specs | Dashed underline rows | **Card grid cells** |
| CTAs | Three equal graphite/red buttons | **Primary + outline secondaries** |
| VIN block | Dark nav clone | **Light trust strip** |
| Equipment | Plain 3-col list | **Card + 2-col scan tiles** |
| Credit form | Dark cheap inputs | **White inputs, styled CTA** |

**Expected impact:** **7–8/10** on used PDP (operator immediate notice without A/B).

---

## 9. What will NOT change

| Area | Status |
|------|--------|
| Header / footer / navigation | **Frozen** |
| Breadcrumbs, H1 text | **Frozen** |
| All copy, prices, spec values | **Frozen** |
| Form fields, POST targets, AJAX | **Frozen** |
| Swiper / Fancybox / modal IDs | **Frozen** |
| New car PDP (`productnew.twig`) | **Out of scope** |
| Used/new catalog pages | **Out of scope** |
| Homepage, about, contact | **Out of scope** |
| PHP controllers, DB, routes | **Out of scope** |
| SEO meta tags | **Out of scope** |
| Reviews, similar cars, banks sliders | **Frozen markup** — inherit global card CSS only |

---

## 10. Regression guard

All W4 CSS selectors **prefixed** with `.used_car_page`. New twig wrappers exist only in `product.twig` (used-car template). Verification matrix post-deploy:

| URL | Check |
|-----|-------|
| Target used PDP | `w4-used-hero` present; visual zones PASS |
| `/cars/` | No `w4-used-*` in HTML |
| `/cars/bmw/` | HTTP 200; catalog renders |
| `/` | HTTP 200 |
| `/about` | HTTP 200 |
| `/contact/` | HTTP 200 |

---

## 11. Screenshot checklist (operator)

| Viewport | Shots |
|----------|-------|
| Desktop | Full PDP before/after; hero crop; equipment; credit form |
| Tablet (991px) | Hero stack; trust strip |
| Mobile (767px) | Hero; CTA column; credit form stack |

---

## 12. Implementation gate

| Prerequisite | Status |
|--------------|--------|
| Write charter | **DONE** |
| Change request | **DONE** |
| Rollback plan | **DONE** |
| Backup `pre-w4-20260609` | **DONE** |
| Design plan (this doc) | **DONE** |
| PHP/JS/DB required? | **NO** — safe to implement |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W4 used PDP design plan from FTP discovery + live HTML probe |

*SITE-001 W4 Used PDP Design Plan v1 — pre-implementation; implementation follows this spec.*
