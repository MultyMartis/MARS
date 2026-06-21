# REPORT — WAVE 1A IMPLEMENTATION MAP

**Site ID:** SITE-002 (ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Wave:** 1A — PDP Hero Alpha (prep only)  
**Date:** 2026-06-09  
**Mode:** Read-only analysis — **no site changes performed**

**Design references:**  
[BZPM-PDP-HIFI-ALPHA-v1](../../../../website-factory/execution-cases/bzpm-catalog-redesign/BZPM-PDP-HIFI-ALPHA-v1.md) ·  
[BZPM-PDP-WIREFRAME-ALPHA-v1](../../../../website-factory/execution-cases/bzpm-catalog-redesign/BZPM-PDP-WIREFRAME-ALPHA-v1.md)

**Evidence (local, not committed):** FTP/Twig/CSS snapshots in `.recovery-temp/site-002-w1a-prep/`  
**Baseline:** [SITE-002-BASELINE-v1.md](SITE-002-BASELINE-v1.md)

---

## 1. Current Hero Structure

### Template chain (live)

```
product/product.twig          (124 B — wrapper only)
  └── {{ producthero }}       → product/producthero.twig   (8562 B — LIVE)
  └── {{ producttabs }}       → product/producttabs.twig   (out of W1A scope)
  └── {{ relproducts }}       → product/relproducts.twig   (out of W1A scope)
```

Alternate on disk (not wired): `sections/producthero.twig` — static demo markup (6123 B).  
Backup on server: `producthero -backUp.twig`.

### DOM / IA map (current `producthero.twig`)

| Zone | CSS / markup | Content | USR-PDP map |
|------|--------------|---------|-------------|
| — | `header` → `breadcrumbs` | Category path (HTML from `document`) | USR-PDP-00 — **outside hero partial** |
| **Media** | `.product-hero__media` → `.product-gallery` | Swiper main + thumbs, Fancybox | USR-PDP-06 |
| **Identity** | `.product-hero__brand` | Demo logo `/assets/img/demo/assum_logo.png` | **Suppress in Alpha** |
| | `.product-hero__title` | `{{ heading_title }}` | USR-PDP-01 |
| | `.product-hero__subtitle` | `{{ heading_subtitle }}` — **hardcoded placeholder in controller** | **Suppress in Alpha** |
| | `.product-hero__meta` | Article `{{ model }}` + `.zpm-copy` (`data-copy=""` empty) | USR-PDP-01 |
| **Commercial** | `.product-hero__status` | `statusText`, optional `deliveryText` | USR-PDP-03 (partial) |
| | `.product-hero__price` | `price`, `priceold`, `priceproc` | USR-PDP-03 |
| | `.product-hero__actions` | Cart + qty (`data-cart-pdp`) or «Запросить цену» | USR-PDP-03 |
| | `.product-hero__other` | Wishlist / compare icon toggles | USR-PDP-07 |
| **Fit props** | `.product-hero__props` → `.product-hero__prop` | Loop `super_atts` — vertical key/value list | USR-PDP-04/05 (partial) |
| **Script** | inline `<script>` | Prefill ask-form fields from H1 | Out of hero IA |

### Layout (CSS)

- Grid: **50% / 50%** (`.product-hero__grid` — `1fr 1fr`, gap 40px).
- Gallery image height: **520px** desktop (`object-fit: contain`) — large visual dominance (~45% feel).
- Info column: two `<span>` stacks — identity+commercial top, props+actions bottom.
- Mobile (`max-width: 1024px`): single column; **no commercial-first reorder**.

### Data already rendered in hero

| Field | Twig variable | Source | Live example (стол SP-P-18/6) |
|-------|---------------|--------|-------------------------------|
| H1 | `heading_title` | `oc_product_description.name` | ✓ |
| Subtitle | `heading_subtitle` | **Literal placeholder in `product.php`** | Placeholder text |
| Article | `model` | `oc_product.model` | ✓ |
| Gallery main | `popup` | `oc_product.image` + resize | ✓ |
| Gallery extras | `images[]` | `oc_product_image` | ✓ if present |
| Thumbs | `thumb`, `images[].thumb` | image tool | ✓ |
| Status | `statusText`, `cancart` | Custom price-index logic in controller | «В наличии: N шт.» / «Под заказ» |
| Delivery hint | `deliveryText` | Controller when под заказ | Often empty on in-stock SKU |
| Price | `price`, `priceold`, `priceproc` | product + special | ✓ |
| Request price mode | `showrequest` | Controller | ✓ branch |
| Cart qty | `incart`, `product_id` | session cart | ✓ |
| Wishlist / compare state | `wishlisted`, `compared` | model helpers | ✓ |
| Hero attributes | `super_atts[]` | L/W/H/weight + `SUPER_ATTS` attribute IDs | **4 rows** on pilot стол (dims only) |

### Data available in `$data` but **not used** in hero Twig

| Variable | Available | Notes |
|----------|-----------|-------|
| `breadcrumbs[]` | ✓ (array `text`, `href`) | Rendered in header as HTML; **usable in hero without PHP edit** |
| `manufacturer`, `manufacturers` | ✓ | Not rendered; could support «ЗПМ · OEM» label |
| `description` | ✓ | Used in tabs only |
| `attribute_groups` | ✓ | Full spec — tabs only |
| `documents` | ✓ | Tabs only |
| `stock`, `options`, `minimum` | ✓ | Not in hero |
| `tags`, `products`, `recurrings` | ✓ | Not in hero |

### Data **missing** for Target Alpha (hero blocks)

| Target block | Gap | Backend needed? |
|--------------|-----|-----------------|
| USR-PDP-02 Series band — descriptor | No series copy field in Twig | **Yes** (category/series CMS slot) or content ops |
| USR-PDP-02 — sibling count «(10)» | Not computed | **Yes** |
| USR-PDP-02 — adjacent series links | Not in `$data` | **Yes** or manual nav |
| USR-PDP-05 — 8 category-critical attrs | `SUPER_ATTS` = IDs **12, 13, 15** only; often empty per SKU | Partially — attribute fill + maybe more IDs |
| USR-PDP-18 — dealer CTA | No hero variable; site has «Дилерам» in header | **No** — static URL in Twig |
| USR-PDP-18 — delivery summary | `deliveryText` exists but sparse | Content/controller tuning (later) |
| Copy article | `data-copy=""` empty — copy JS may fail | **No** — Twig fix only |

### Reusable blocks (keep / reshape)

| Block | Reuse |
|-------|-------|
| `.product-gallery` + Swiper/Fancybox hooks (`.js-product-gallery`, `.js-product-thumbs`) | **Keep** — resize column only |
| `.zpm-copy` + article row | **Keep** — fix `data-copy` value |
| `.p-card__status-*`, `.p-card__delivery` | **Keep** |
| Price row + discount | **Keep** |
| `data-cart-pdp` / `data-cart-add` / `zpm-qty` | **Keep** — buy box wrapper only |
| `data-fav-toggle`, `data-compare-toggle` | **Keep** — reposition; **no compare backend work** |
| `super_atts` loop | **Reshape** → 4×2 grid (cap 8 cells) |
| `container` wrapper | **Keep** |

---

## 2. Target Hero Structure

Per **Hi-Fi Alpha (70/30)** + **Wireframe Alpha Zone 1** — hero = **USR-PDP-00–07** + **USR-PDP-02 band** + **USR-PDP-18 preview row** (B2B links only, not full Zone 6).

### Desktop target composition

```text
USR-PDP-00  Breadcrumb          [header — unchanged in W1A]
USR-PDP-02  Series Context Band [NEW — full-width above hero card]
┌────────────────────────────────────────────────────────────── HERO CARD ──┐
│ ROW 1                                                                     │
│  USR-PDP-06 Media ~30%  │  USR-PDP-01 Identity (H1, article, OEM)        │
│                         │  USR-PDP-04/05 Fit grid 4×2 (8 cells)          │
│ ROW 2                                                                     │
│  USR-PDP-03 Buy box     │  USR-PDP-07 + USR-PDP-18 preview (actions row) │
└───────────────────────────────────────────────────────────────────────────┘
```

### Mobile target (P1 reorder — Wireframe §D)

```text
P1: USR-PDP-03 Commercial → USR-PDP-02 Band → USR-PDP-01 → USR-PDP-04/05
P2: USR-PDP-07 actions
P4: USR-PDP-06 Media (gallery deprioritized)
```

### Explicitly **out of W1A** (later waves)

USR-PDP-08–21 below hero: tabs/min spec/in-series/related/docs/consult block restructuring.

---

## 3. Delta Map

| Element | Current | Target | Action |
|---------|---------|--------|--------|
| Breadcrumb | Header only | Same | **Keep** |
| Series visibility | Terminal breadcrumb only | USR-PDP-02 band | **Create** (Twig from `breadcrumbs[]` heuristic) |
| Gallery width | ~50%, 520px tall | ~30%, 4:3 compact | **Move** + CSS |
| Demo brand logo | Shown | Hidden | **Remove** |
| Mini subtitle | Placeholder in hero | Suppressed | **Remove** from hero |
| H1 + article | In info column | Identity cluster + grid | **Keep** + reorder |
| Fit attributes | 4–7 vertical rows | 4×2 grid, max 8 | **Reshape** (same `super_atts`) |
| Status + price + CTA | Stacked in info column | Isolated buy box card | **Move** + new wrapper/CSS |
| Compare / favorites | Icon row below props | Labeled row beside B2B links | **Move** (same handlers) |
| Delivery / dealer | `deliveryText` only | Preview links row | **Create** (dealer link static; delivery conditional) |
| Tabs / specs / docs | Below hero | Unchanged in W1A | **Keep** (no touch) |
| Related products | `relproducts` | Unchanged | **Keep** (no touch) |
| `product.twig` wrapper | 3 partials | Same | **Keep** |
| Controller / DB | Current | No change in W1A | **Keep** (constraint) |

### Coverage vs Alpha (honest)

| Alpha requirement | W1A frontend-only |
|-------------------|-------------------|
| Series band name + link | **Partial** — from `breadcrumbs[n-2]` |
| Series descriptor + sibling count | **No** — deferred |
| 8 fit cells | **Partial** — only if CMS attrs populated |
| Buy box isolation | **Yes** |
| B2B preview links | **Partial** |
| Mobile commercial-first | **Yes** (CSS order) |
| Min spec visible | **No** — Wave 2 / tabs wave |
| In-series alternatives | **No** — Wave 3+ |

---

## 4. Required Files

### Must change (Wave 1A minimal)

| File | Change |
|------|--------|
| `catalog/view/theme/default/template/product/producthero.twig` | Markup restructure: band, hero card, grid, buy box, suppress brand/subtitle |
| `assets/css/style.css` | Hero grid ratios, band, buy box card, fit grid 4×2, mobile `order` |

### Should not change (W1A scope lock)

| File | Reason |
|------|--------|
| `product/product.twig` | Wrapper stable |
| `product/producttabs.twig`, `sections/producttabs.twig` | Tabs out of scope |
| `product/relproducts.twig`, `catalog/controller/product/relproducts.php` | Related out of scope |
| `catalog/controller/product/product.php` | Backend out of scope |
| `config.php` / DB | Backend out of scope |
| Category templates / filters | Out of scope |

### Optional / low risk

| File | When |
|------|------|
| `assets/js/main.js` | Only if DOM hooks break (prefer keeping existing gallery/cart selectors) |
| `assets/css/style.min.css` | **Not live** — header loads `style.css` only |
| `producthero -backUp.twig` | Pre-deploy FTP backup copy |

### Pre-deploy backup (operator)

1. FTP copy `producthero.twig` → `producthero.w1a-backup.twig`  
2. FTP copy `assets/css/style.css` → `style.w1a-backup.css`  
3. Clear `system/storage/cache/template/` after deploy (OC twig cache)

---

## 5. Risks

| ID | Risk | Severity | Mitigation |
|----|------|----------|------------|
| R-01 | **Series band from breadcrumbs** — depth varies by category (4–6 levels) | High | Pick explicit index or «parent of product» rule; document per taxonomy; full fix needs controller series DTO |
| R-02 | **< 8 grid cells** on many SKUs (live стол = 4) | High | Ship grid shell with «—» empties **or** gate pilot to sink series with filled `SUPER_ATTS` |
| R-03 | `heading_subtitle` placeholder visible today | Medium | Remove from hero in W1A |
| R-04 | `data-copy=""` — article copy broken | Low | Set `data-copy="{{ model }}"` in Twig |
| R-05 | Cart/qty JS tied to `.product-hero__actions[data-cart-pdp]` | Medium | Preserve attributes/classes on moved buy box |
| R-06 | Gallery JS scopes `.product-gallery` — markup change safe if class retained | Low | Keep wrapper classes |
| R-07 | OCMOD / twig cache stale after FTP | Medium | Refresh template cache; 3 enabled modifications untouched |
| R-08 | Admin blocked — no theme editor verification | Low | FTP + storefront visual QA |
| R-09 | Fold overflow on 1366×768 with band + grid + buy box | Medium | Hi-Fi V-01 — screenshot QA on TEST |
| R-10 | Mobile P1 stack length (commercial + band + identity + grid) | Medium | Wireframe OQ-09 — test 375px / 390px |

---

## 6. Rollback Scope

| Layer | Rollback |
|-------|----------|
| Twig | Restore `producthero.twig` from backup file |
| CSS | Restore `style.css` from backup |
| JS | No change expected — no rollback |
| Database | None — no W1A DB changes |
| Cache | Clear template cache after restore |

**Blast radius:** PDP hero presentation only. Tabs, related products, cart/compare/wishlist **endpoints unchanged**.

---

## 7. Ready For Implementation

### Decision: **YES — with scoped caveats**

| Gate | Status |
|------|--------|
| FTP / storefront access | ✓ Run 5 OK |
| Live templates identified | ✓ |
| Alpha IA mapped to existing Twig/CSS | ✓ |
| W1A scope bounded (hero only) | ✓ |
| Backend-free path defined | ✓ Partial Alpha |
| Admin access | Not required for FTP Twig/CSS path |
| Backup before write | **Operator action** — not verified at Run 5 |

### Recommended W1A implementation slices

1. **Slice A (safe):** Remove brand + subtitle; fix article copy; buy box card CSS; gallery 30/70 layout.  
2. **Slice B:** `super_atts` → 4×2 grid (existing data).  
3. **Slice C:** Series band from `breadcrumbs[]` + static dealer link.  
4. **Slice D:** Mobile commercial-first CSS order.

**Defer to Wave 1B+:** series descriptor, sibling count, min spec surfacing, in-series carousel, controller/`SUPER_ATTS` expansion.

### Pilot SKU suggestion

Use a **мoечные ванны / PREMIUM-3** SKU with populated attributes (reference: ВМЦ-П3-2/500) once URL confirmed on TEST — стол SP-P-18/6 proved **4-prop-only** hero today.

---

*Analysis only — no site modifications. Evidence in `.recovery-temp/site-002-w1a-prep/` (gitignored).*
