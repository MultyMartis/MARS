# SITE-001 W5-C Used PDP Commercial Stage Design Plan v1

**Type:** Pre-implementation design plan — commercial offer scene  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Target:** `https://sibcar.new-site.space/audi-a1-2012-s-probegom-149-000-km-799`  
**Template:** `catalog/view/theme/auto/template/product/product.twig` · body class `used_car_page`

**Inputs:** W4 Used PDP design plan · W5 First Impression Blueprint (Concept B §Used PDP) · W5-A stabilization state

---

## 1. Problem statement

W4 delivered **structural grouping** (hero shell, trust strip, equipment card, credit panel) but the page still reads as **OpenCart product record with styled widgets** — not a unified **dealership vehicle offer**. Remaining signals:

| Signal | Evidence |
|--------|----------|
| Hero fragments | Badges, gallery, price, specs, CTAs, trust strip feel like separate blocks |
| Price hierarchy weak | Monthly payment competes with list price; discount rows look like admin toggles |
| Trust strip CRM tone | Label/value rows resemble backend status table |
| Equipment admin list | Flat columns without dealership spec-sheet rhythm |
| Credit panel cheap inputs | Dark wrapper OK; form fields still generic |
| Modals 2014 popup | Dark `#credit__FORM_popup` in footer.twig — 70px padding, no structure |

W5-C elevates W4 anatomy into a **single commercial stage** without PHP/JS/DB/text changes.

---

## 2. Current anatomy (W4 baseline)

```
used_car__wrapper
├── short_btns.w4-used-badges
├── w4-used-hero
│   └── car_main_info (gallery + panel)
│       ├── w4-used-hero__offer (price + discount)
│       ├── w4-used-hero__specs
│       └── w4-used-hero__actions
├── car_vin_check.w4-used-trust-strip
├── lcd_display.product
├── car_configuration.w4-used-equipment
└── used_car__credit.w4-used-credit
(popups: credit/tradein/installment in footer.twig; VIN in product.twig)
```

---

## 3. Target anatomy (W5-C)

```
used_car__wrapper
├── w5c-commercial-stage          ← NEW — one offer deck
│   ├── short_btns.w4-used-badges
│   ├── w4-used-hero              ← fused to trust below
│   └── car_vin_check.w4-used-trust-strip
├── lcd_display.product           ← UNCHANGED
├── car_configuration.w4-used-equipment.w5c-equipment-grid
└── used_car__credit.w4-used-credit.w5c-credit-panel
(modals: body.used_car_page scoped CSS refresh — no footer.twig edit)
```

---

## 4. Block plan

| ID | Class / scope | Goal |
|----|---------------|------|
| W5-C-A | `w5c-commercial-stage` | Single gradient deck wrapping badges + hero + trust |
| W5-C-B | `.w5c-commercial-stage .w4-used-hero__gallery` | 480px showroom photo, stronger thumbs |
| W5-C-C | `.w5c-commercial-stage .w4-used-hero__offer` | Price 52px anchor; credit in side card; discount as 3 mini-cards |
| W5-C-D | `.w5c-commercial-stage .w4-used-hero__specs` | Spec cells on light panel inside stage |
| W5-C-E | `.w5c-commercial-stage .w4-used-hero__actions` | 3-col CTA grid; primary dominance |
| W5-C-F | `.w5c-commercial-stage .w4-used-trust-strip` | 4-col trust proof cards + solid VIN CTA |
| W5-C-G | `w5c-equipment-grid` | 3-col scan grid, accent title rule, pill toggle |
| W5-C-H | `w5c-credit-panel` | White inset form card on dark shell; premium inputs |
| W5-C-I | `body.used_car_page #credit__FORM_popup` etc. | Light modal shell, structured padding, readable legal |

---

## 5. Preserved elements (mandatory)

All W4 preserve list remains binding: twig variables, Swiper/Fancybox hooks, form POST routes, inline `<script>` verbatim, `#toggleConfigBtn`, discount `data-amount`, all static trust copy, all equipment HTML from `{{ complect }}`.

**Additional constraint:** credit/tradein/installment popups live in `footer.twig` — **no footer edit**; modal refresh via `body.used_car_page` CSS only.

---

## 6. Twig additions (minimal)

| Addition | Location |
|----------|----------|
| `<div class="w5c-commercial-stage">` | Wrap badges + hero + trust |
| `w5c-equipment-grid` | class on `.car_configuration` |
| `w5c-credit-panel` | class on `.used_car__credit` |
| `w5c-pdp-modal` | class on `#VIN_lead_popup` |

No new text. No SEO. No JS edits.

---

## 7. CSS strategy

- New block appended after W5-A-S end markers in `main.css` / `media.css`
- Scope: `.used_car_page` for page blocks; `body.used_car_page` for modals
- Overrides W4 visual tokens where W5-C specificity is higher (nested under `.w5c-commercial-stage`)
- Rollback: remove W5-C block + restore twig wrappers from backup

---

## 8. Safety assessment

| Risk | Mitigation | Verdict |
|------|------------|---------|
| New PDP leak | `product.twig` is used-car-only template | **LOW** |
| Header regression | header.twig not deployed | **NONE** |
| Modal global breakage | CSS scoped to `body.used_car_page` | **LOW** |
| JS dependency | No hook/class changes on form inputs | **SAFE** |
| Footer edit required | Avoided via body-scoped modal CSS | **SAFE** |

**Plan verdict:** **SAFE TO IMPLEMENT** on TEST.

---

## 9. Success criteria (visual)

Operator opens used PDP and within 3 seconds recognizes **vehicle offer**, not OpenCart record:

1. Hero + trust = one commercial scene (**w5c-commercial-stage**)
2. Price is unmistakable commercial center (52px)
3. Trust strip = proof cards, not CRM table
4. Equipment = dealership spec sheet (3-col)
5. Credit form = premium white inset panel
6. Modal = modern light dialog with readable legal
7. Header W5-A unchanged

**Target impact:** **≥7/10** on used PDP. Subtle delta = FAIL → rollback.

---

## 10. Verification URLs

Same 8-URL matrix as W5-A-S + modal interaction on target PDP.

---

## Status

**APPROVED FOR TEST EXECUTION** — safety gate passed 2026-06-10.

*SITE-001 W5-C Used PDP Commercial Stage Design Plan v1 — TEST only.*
