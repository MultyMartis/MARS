# FP-0002 v3 — Header Geometry Rebuild Plan v1

**Date:** 2026-06-22  
**Phase:** HB-GEOMETRY-PLAN  
**Authority:** PDF PRIMARY · FIG geometry secondary · JPG visual check  
**Target files:** `src/partials/layout/header.html` · `src/scss/layout/_header.scss`

---

## Layout law (rebuild)

| Rule | Implementation |
|------|----------------|
| Outer shell | `<header class="header">` — `width: 100%`, full-bleed background |
| Inner track | `.header__container.container` — max **1170px**, pad-x **40px** desktop (existing tokens) |
| Row count | **2** explicit rows — no collapse |
| Layout engine | **CSS Grid** per row — **no** `li + li` · **no** magic margins · **no** absolute positioning |
| Column model | Shared **3-column** grid both rows: **`205px` \| `1fr` \| `auto`** |

### Column semantics

```text
Column 1 (205px):  Row1 Region  |  Row2 Logo (logo.svg only)
Column 2 (1fr):    Row1 Hours+Utility (inner flex)  |  Row2 Nav (centered)
Column 3 (auto):   Row1 Phones  |  Row2 CTA
```

Left anchor: Region aligns vertically with Logo.  
Right anchor: Phones align vertically with CTA.

---

## Row 1 — TOP ROW geometry

| Zone | Grid cell | Content | Type scale |
|------|-----------|---------|------------|
| Region | Col 1 | `Москва,` / `Московская область` | 14px UI — **weak** |
| Hours + Utility | Col 2 | Wrapper `.header__row-top-center` — flex `space-between` | Hours 14px weak · Utility 14px medium |
| Phones | Col 3 | Stacked `tel:` links | 20px medium — **strong** |

| Property | Value |
|----------|-------|
| `min-height` | **40px** |
| `column-gap` | `$space-6` (24px) token |
| Inner center gap | `$space-6` between hours and utility |

**Excluded:** logo · nav · CTA · 800 · socials · search · «режим работы»

---

## Row 2 — MAIN ROW geometry

| Zone | Grid cell | Content | Type scale |
|------|-----------|---------|------------|
| Logo | Col 1 | **`logo.svg` only** — remove duplicate brand text (SVG contains wordmark paths) | 205×46 display box |
| Nav | Col 2 | 5 links, flex center, gap `$space-8` (40px) | 16px — **strong group** |
| CTA | Col 3 | `<button>` «Заказать звонок» | 190×44 — **dominant** |

| Property | Value |
|----------|-------|
| `min-height` | **72px** (~1.8× TOP ROW — toward 2× band dominance) |
| CTA box | 190×44px; override global `.btn { min-width: 280px }` via `.header__cta.btn` |
| Logo | `object-fit: contain; object-position: left center` |

**Excluded:** phones · utility in row 2 · extra nav · search · socials

---

## Envelope targets (FIG + Visual Scale)

| Metric | Target | Rationale |
|--------|--------|-----------|
| Container inner | 1170px | FIG header width · Production Standards v3 |
| Header envelope | ~124–143px total | FIG 1170×143 · PDF proxy top_bar ~180px hint |
| Row 2 : Row 1 height ratio | ~1.8–2.5× | Visual Scale Spec §5.2 |
| Logo slot | 205×46 | FIG `1:880` / layout lock |
| CTA | 190×44, radius 30px (engineering token) | FIG `1:900` hint · SU-11 |

---

## HTML structure (rebuild)

```html
<header>
  <div class="header__container container">
    <div class="header__row header__row--top">
      [region]
      <div class="header__row-top-center">[hours][utility]</div>
      [phones]
    </div>
    <div class="header__row header__row--main">
      [logo.svg only]
      [nav 5 links]
      [cta button]
    </div>
  </div>
</header>
```

---

## Explicit prohibitions

- No centered tiny header island (grid fills full container track)
- No separate brand text if `logo.svg` already includes wordmark
- No utility/nav redistribution across rows
- No `margin-left: auto` chains on every sibling
- No invented copy beyond PDF text lock

---

## Verification after patch

1. `npm run build` exit 0  
2. `dist/index.html` — header present; footer/hero absent  
3. Operator visual compare vs JPG + PDF screenshot  

---

**STOP — HB-GEOMETRY-PLAN complete.**
