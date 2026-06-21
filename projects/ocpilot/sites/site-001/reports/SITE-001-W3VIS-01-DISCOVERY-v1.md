# SITE-001 W3VIS-01 Discovery v1

**Type:** Pre-execution discovery — visual hierarchy & surface system (read-only)  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** W3VIS-01 — Visual Hierarchy & Surface System (Phase 2)  
**Supersedes:** W3V2 as perceptual target (W3V2 remains technically valid; operator Visual Impact ≈ **2/10**)

**Methods:** Read-only HTTP probe · live CSS fetch · post-W3V2 `css/main.css` analysis (7 146 lines) · cross-reference W2/W3-V/W3V2/W3UX-C1 reports  
**Explicit exclusions:** No FTP · No CSS/Twig edits · No cache ops · No implementation

**Evidence (local, not in git):** `.recovery-temp/site-001-w3vis-01-probe.json` · `.recovery-temp/site-001-w3vis-01-probe.py`

**Companion decision:** [SITE-001-W3VIS-01-DECISION-v1.md](SITE-001-W3VIS-01-DECISION-v1.md)

---

## Executive summary

Prior waves (**W3-V**, **W3V2**, **W3UX-C1**) successfully changed **palette, radius, shadow tokens, and used-catalog density** — but did **not** change how the eye parses **primary vs secondary vs supportive** content. Every major block still reads as the same OpenCart pattern: **white rectangle + 1px grey border + optional soft shadow**, sitting on a slightly tinted body (`--w3v2-surface`).

**Root cause of “still the same website”:** absence of a **surface level system** and **typographic/action hierarchy**, not absence of color refresh.

| Layer | What changed (W3-V → W3V2 → W3UX-C1) | What did **not** change (W3VIS gap) |
|-------|----------------------------------------|-------------------------------------|
| Color | Graphite footer, richer red, neutral body | Same fill for cards, forms, widgets, hero fragments |
| Depth | Token shadows on cards | No nested depth; hero fragments float separately |
| Density | Used catalog card height −24% | New catalog, PDP hero, homepage sections unchanged |
| Hierarchy | Price 24px on used cards only | PDP, new cards, CTAs, sections still equal weight |

**Operator diagnosis confirmed:** palette changed; perception did not.

---

## Task 1 — Surface inventory (HTTP 2026-06-09)

| Surface | URL | HTTP | Body class | Key blocks present |
|---------|-----|------|------------|-------------------|
| Homepage | `/` | 200 | *(empty)* | `home_slider`, `four_blocks`, `fancy_form`, `partner_banks`, 4× `page_sub_title` |
| Used catalog | `/cars/` | 200 | `used_catalog` | `search_wrap`, 14× `catalog_item`, `partner_banks`, `home_slider` |
| New catalog | `/auto/` | 200 | `new_catalog` | `search_wrap`, 14× `catalog_item`, `partner_banks`, `home_slider` |
| Used brand | `/cars/bmw/` | 200 | `used_catalog` | `search_wrap`, 0 listings (TEST stock), `partner_banks` |
| New brand | `/auto/haval/` | 200 | `new_catalog` | `search_wrap`, 0 listings, `partner_banks` |
| About | `/about` | 200 | *(empty)* | `four_blocks`, `fancy_form`, `partner_banks` |
| Contact | `/contact/` | 200 | *(empty)* | contacts blocks only |
| Used PDP (sample) | `/audi-a1-2012-s-probegom-149-000-km-799` | 200 | `used_car_page` | `car_main_info`, discount widget, VIN, credit calculator |
| New PDP (W3UX baseline) | `/baic-bj40-new` | *(W3UX audit sample)* | `new_car_page` | `new_car_main_info`, bonus grid, `car-media` gallery |

**Live CSS confirmation:** W3V2 block active — 66 `--w3v2-*` tokens, 118 KB `main.css`.

---

## Task 2 — Top 20 hierarchy failures (ranked)

| Rank | ID | Failure | Severity | Surfaces | Evidence |
|------|-----|---------|----------|----------|----------|
| 1 | **HF-01** | **PDP hero fragments unrelated** — photo column, price block, discount widget, specs grid, CTA row share no unified container; only 10px padding between 50/50 flex children | **Critical** | Used PDP | `.car_main_info { display:flex; margin:-10px }` — no wrapper surface |
| 2 | **HF-02** | **Primary buy CTA does not dominate** — `.car_main_info__btns > a` graphite 50px equals secondary; red only on `.car_main_info__btns_main`; hover turns **all** buttons red | **Critical** | Used + new PDP | Base fill `rgb(33,36,43)` on non-main buttons; shared hover red |
| 3 | **HF-03** | **Catalog card CTA invisible at rest** — `.catalog_item__btn` graphite; red only on `.catalog_item__info:hover` | **Critical** | Used + new catalog | Weak conversion signal until hover |
| 4 | **HF-04** | **Price vs title equal weight on new catalog** — `.catalog_item__price_main` 20px/500 vs `.catalog_item__name` 20px; W3UX-C1 hierarchy **scoped to `.used_catalog` only** | **Critical** | `/auto/`, new PDP cards on home | W3UX block ends before new-catalog rules |
| 5 | **HF-05** | **Single surface recipe everywhere** — cards, banks, advantages, forms, discount widget all: white + `#D5DAE2` border + `--w3v2-shadow-sm` | **Critical** | Sitewide | W3V2-C applies identical treatment to 8+ component families |
| 6 | **HF-06** | **Body vs card contrast too low** — `--w3v2-surface` `#F7F8FA` vs `--w3v2-surface-card` `#FFFFFF` — ~1–2% luminance delta | **High** | Sitewide | W3V2-A body/card tokens |
| 7 | **HF-07** | **Header CTA triad competes with page CTAs** — callback + phone + WhatsApp repeat at equal visual weight in `singe_bar__wrap` on every page | **High** | All probed URLs | Probe: 12–20 CTA samples per page, mostly header duplicates |
| 8 | **HF-08** | **VIN block uses conversion-competing green CTA** — `.car_vin_check__btn` green 50px banner competes with red buy path | **High** | Used PDP | Full-width dark band + green button |
| 9 | **HF-09** | **Credit calculator reads as second hero** — `.used_car__credit` full graphite + background image + 30px title = same visual language as nav/footer | **High** | Used PDP | Dark L1 chrome reused for in-content widget |
| 10 | **HF-10** | **Discount toggle widget is isolated white island** — `.car_main_info__discount` white card with 30px pad inside hero column; breaks hero continuity | **High** | Used PDP | Nested card without parent surface |
| 11 | **HF-11** | **Catalog filter form collapses into grid** — `.search_form` white bordered box same weight as `.catalog_item` cards | **High** | `/cars/`, `/auto/` | Identical border/shadow vocabulary |
| 12 | **HF-12** | **Stock/status tags low contrast** — `.catalog_item__tags > div` on `--w3v2-surface-alt`; green stock only color signal; max-width 80px | **High** | Catalog | Tags compete with title, not price |
| 13 | **HF-13** | **VIN micro-box competes with price row** — `.catalog_item__vin` bordered 80×80 column beside price (used cards post-W3UX-C1: 72px — still equal row weight) | **High** | Used catalog | Price + VIN flex row |
| 14 | **HF-14** | **Homepage sections equally loud** — all `.page_sub_title` 30px/500, `margin: 50px 0 20px`; hero 600px min-height same importance as advantages | **High** | `/` | No section tier tokens |
| 15 | **HF-15** | **Credit strip separates price from CTA** — `.catalog_item__credit` border-top + 20px margins creates third horizontal band | **Medium** | Catalog | Three-band card: meta / price+credit / CTA |
| 16 | **HF-16** | **New PDP photo box floats alone** — `.new_car_main_info__photo` white bordered box with 50px padding; info/trim blocks not visually grouped | **Medium** | New PDP | No hero wrapper |
| 17 | **HF-17** | **Partner banks on every page including empty brand filters** — same card slider below empty grids | **Medium** | Brand pages | Visual noise without inventory |
| 18 | **HF-18** | **Characteristics grid mimics spec table, not summary** — dashed underlines, hover red; same weight as price block above | **Medium** | Used PDP | `.car_main_info__characteristics_item` |
| 19 | **HF-19** | **Lead forms decorative, CTA buried** — `.fancy_form_block` large decor; submit same red as header callback — no form-as-primary-surface | **Medium** | `/`, `/about` | Form competes with section title |
| 20 | **HF-20** | **Typography plateau** — dominant sizes cluster 16–30px / weight 500; no display tier for price, no muted tier for legal/meta | **Medium** | Sitewide | W3-V price bump (22px catalog) partially overridden/scoped |

---

## Task 3 — Top 10 blocks that visually disappear

| Rank | Block | Selector / region | Why it disappears | Severity |
|------|-------|-------------------|-------------------|----------|
| 1 | Catalog card CTA | `.catalog_item__btn` | Graphite on white; red only on card hover | **Critical** |
| 2 | Secondary PDP actions | `.car_main_info__btns > a` (non-main) | Same size/fill as primary until class inspect | **Critical** |
| 3 | Credit line under price | `.catalog_item__credit`, `.car_main_info__credit_price` | 14–16px secondary color; bordered strip | **High** |
| 4 | Filter/search form | `.search_wrap` / `.search_form` | Same card chrome as product tiles | **High** |
| 5 | Stock badge | `.catalog_item__tags__in_stock` | Small pill, muted alt surface | **High** |
| 6 | Breadcrumbs | `.breadcrumbs` | `--w3v2-text-secondary`; no surface | **Medium** |
| 7 | Brand chip row | `.brand_catalog` | No elevation; sits on body | **Medium** |
| 8 | Section “view all” links | `.page_sub_title > a` | 14px text link vs 30px section title | **Medium** |
| 9 | Trade-in / secondary form fields | `.fancy_form__wrap` inputs | Same input chrome as catalog filters | **Medium** |
| 10 | New-car trim/configuration rows | `.car_configuration__*` | White on white within hero column | **Medium** |

---

## Task 4 — Top 10 blocks that should become surfaces/cards

| Rank | Block | Proposed surface level | Rationale |
|------|-------|------------------------|-----------|
| 1 | **Used PDP hero** (photo + price + specs + CTAs) | **L2 — Primary product surface** | Single bordered/shadowed hero shell; internal L3 zones |
| 2 | **New PDP hero** (photo + trim + price + CTAs) | **L2 — Primary product surface** | Same system as used; preserves layout |
| 3 | **Catalog filter bar** | **L2 — Tool surface** | Elevate above grid; distinct from product cards |
| 4 | **Catalog product card** | **L2 — Inventory tile** | Keep; add stronger internal zones (image / offer / action) |
| 5 | **Discount/trade-in widget** | **L3 — Nested widget inside hero** | Demote from standalone island |
| 6 | **VIN check band** | **L3 — Support widget** (or L2 below hero fold) | Stop competing with buy CTA |
| 7 | **Credit calculator** | **L2 — Conversion section** | Differentiate from nav/footer graphite |
| 8 | **Homepage hero slider** | **L2 — Marketing hero** | Strongest section weight on `/` |
| 9 | **Advantages / four_blocks** | **L2 — Trust grid** | Slightly lower elevation than hero/catalog |
| 10 | **Lead capture form** | **L2 — Form surface** | Full-width tinted panel behind form |

---

## W3VIS-01A — PDP hero surface analysis

### Used PDP (`product.twig` · `.car_main_info`)

**Current structure (CSS-driven, layout frozen):**

```
┌──────────────────────────────┬──────────────────────────────┐
│ .car_main_info__photo (50%)  │ .car_main_info__main (50%)   │
│  pad 10, no shared border    │  pad 10                      │
│  gallery thumbs              │  price row (30px red)          │
│                              │  credit price (20px)           │
│                              │  ┌ discount widget ────────┐ │
│                              │  │ white card, pad 30      │ │
│                              │  └─────────────────────────┘ │
│                              │  characteristics grid          │
│                              │  [CTA row — graphite + red]    │
└──────────────────────────────┴──────────────────────────────┘
        ↑ no wrapper                     ↑ fragments
```

**Problem:** Four perceived objects (gallery, pricing, discount island, action/spec stack) — not one product hero.

**Goal (layout unchanged):** Perceive as **one L2 hero surface** via:

| Mechanism | Proposal |
|-----------|----------|
| Wrapper | Apply unified background + border + radius + shadow to `.car_main_info` (not children) |
| Internal dividers | Replace outer child padding with internal 1px `--vis-border-subtle` vertical split |
| Price zone | L3 inset panel or top-of-column emphasis band (price + credit on `--vis-surface-3`) |
| Discount widget | Remove standalone white card chrome; nest as L3 strip inside hero |
| CTA row | Pin to bottom of hero column with `--vis-surface-action` band (full-width within column) |
| Gallery | Edge-to-edge within left half; radius only on hero outer corners |

**Question answered:** Existing 50/50 flex **can** read as one hero if the **parent** carries surface chrome and children lose competing borders/backgrounds.

### New PDP (`productnew.twig` · `.new_car_main_info`)

**Current:** Photo in bordered white box (`padding: 0 50px 50px`); trim/price/CTA likely adjacent without shared shell (same class family as used).

**Same treatment:** Wrap `.new_car_main_info` as L2; photo box loses outer border (inherits hero); trim blocks become L3 rows.

---

## W3VIS-01B — CTA hierarchy analysis

### Inventory (live + CSS)

| CTA | Selector / context | Current visual tier | Competes with |
|-----|-------------------|---------------------|---------------|
| Buy / reserve | `.car_main_info__btns_main` | Primary red — **only labeled primary** | Secondary buttons same row |
| Trade-in / callback (PDP) | `.car_main_info__btns > a` | Graphite filled — **reads secondary but same size** | Buy |
| Catalog “details” | `.catalog_item__btn` | Graphite → red on hover | Price |
| Header callback | `.callback_btn` | Primary red | Page-level primary |
| Header phone | `.phone_btn` | Primary red | Page-level primary |
| Header WhatsApp | `.whatsapp_btn` | Green accent | Both reds |
| VIN check | `.car_vin_check__btn` | Green 50px | Buy |
| Credit apply | `.used_car__credit` form submit | Red in dark section | Hero buy |
| Filter submit | `.search_form` / `.form_item > .submit` | Red | Card CTAs |
| Lead form submit | `.fancy_form__wrap > div > button` | Red | Section content |

### Proposed hierarchy (no copy/routing change)

| Tier | Role | Visual treatment |
|------|------|------------------|
| **Primary** | Buy / reserve / catalog “view car” | Full red fill, 48px PDP / 40px card, `--vis-shadow-cta`, min-width dominance in row |
| **Secondary** | Trade-in, callback on PDP, credit pre-qual | Outline or ghost: white/transparent + red border, 44px, no fill at rest |
| **Supportive** | VIN check, phone text links, WhatsApp | Text + icon or soft green outline **smaller** than primary; never full-width 50px bar |
| **Tertiary** | Filter reset, “show all”, breadcrumbs | Text link or muted button; `--w3v2-text-secondary` |

**Critical fix:** Stop `.car_main_info__btns > a:hover` from turning **all** buttons red — breaks primary/secondary distinction.

---

## W3VIS-01C — Surface system proposal

### Three elevation levels (+ canvas)

| Level | Token (proposed) | Fill | Border | Shadow | Use |
|-------|------------------|------|--------|--------|-----|
| **Canvas** | `--vis-canvas` | `#F7F8FA` (existing `--w3v2-surface`) | none | none | Page background |
| **L1 — Flush** | `--vis-surface-1` | transparent / canvas | none | none | Breadcrumbs, inline text sections, legal prose |
| **L2 — Section** | `--vis-surface-2` | `#FFFFFF` | `1px --vis-border` | `--vis-shadow-md` | Hero, filter bar, catalog cards, form panels, credit section |
| **L3 — Widget** | `--vis-surface-3` | `#EFF1F4` (`--w3v2-surface-alt`) | none or hairline | `--vis-shadow-sm` | Discount strip, spec clusters, tags, nested calculator rows |

**Dark conversion sections** (credit, VIN): use **`--vis-surface-dark-panel`** — graphite distinct from nav/footer via inset border + inner padding, not full-bleed chrome clone.

### Block → level mapping

| Block | Current | Target |
|-------|---------|--------|
| `body` | L0 tinted | Canvas |
| `.car_main_info` | none | **L2 hero** |
| `.car_main_info__discount` | competing L2 white card | **L3 nested** |
| `.search_form` | L2-card clone | **L2 tool** (tinted `--vis-surface-3` background to differ from cards) |
| `.catalog_item` | L2 | **L2** (stronger hover → L2+shadow-lg) |
| `.four_blocks > div` | L2 | **L2** (lower shadow than hero) |
| `.partner_banks__item` | L2 | **L3** (logos shouldn’t outrank cars) |
| `.used_car__credit` | dark chrome | **L2 dark panel** (inset, not nav clone) |
| `.car_vin_check` | dark chrome + green CTA | **L3 support** or post-hero L2 |
| `.fancy_form_block` | mixed | **L2 form** on `--vis-surface-3` band |
| Footer/nav | dark | **Frozen** — out of W3VIS scope |

---

## W3VIS-01D — Catalog visual hierarchy

### Used catalog (post-W3UX-C1)

**Improvements already live:** price 24px/600, tighter spacing, image cap.

**Remaining gaps:**

| Element | Issue | Target |
|---------|-------|--------|
| Price | Better but CTA still dominates on hover only | Price = red 24px; old price muted 14px |
| CTA | Graphite at rest | **Primary red at rest**, graphite only for secondary link-style actions |
| Stock | Green text in small tag | Badge with fill `--vis-success-subtle` adjacent to title |
| Credit | Bordered strip between price and CTA | Inline under price, 13px muted, no border-top |
| VIN box | Box competes with price | Icon+label inline row under price, demote border |

### New catalog (no W3UX pass yet)

| Element | Issue | Target |
|---------|-------|--------|
| Price vs name | Both 20px/500 | Price **26px/600**; name **18px/600** |
| Face padding | 20px inflates tile | Edge-to-edge image; offer zone L3 |
| CTA | Same graphite pattern | Match used primary-at-rest rule |
| Stock | Same as used | Shared badge system |

---

## W3VIS-01E — Homepage section hierarchy

**Current stack:** Header → 600px hero → catalog block → offers slider → advantages (`four_blocks`) → banks → form → map — all separated by **identical** `.page_sub_title` (30px, 50px top margin).

| Section | Current weight | Target weight |
|---------|----------------|---------------|
| Hero slider | High size, weak surface (no L2 shell) | **Highest** — L2 full-bleed or contained hero card |
| First catalog teaser | Same title style as hero follow-ups | **High** — L2 grid on canvas |
| Special offers slider | Equal title | **Medium-high** |
| Advantages (`four_blocks.short`) | Same card recipe as catalog | **Medium** — L2 low shadow |
| Partner banks | Same as cards | **Low** — L3 logo strip |
| Lead form | Competes with catalog | **Medium** — L2 tinted band |
| Map | Inline 500px | **Low** — flush L1 |

**Section title system (proposed):**

| Token | Size / weight | Use |
|-------|---------------|-----|
| `--vis-type-display` | 36–40px / 600 | Hero H1 only |
| `--vis-type-section` | 28px / 600 | Primary section (`page_sub_title`) |
| `--vis-type-subsection` | 22px / 600 | In-card / in-hero labels |
| `--vis-type-meta` | 13–14px / 400 | Specs, credit, legal |

Reduce **advantages/banks** top margin from 50px → 32px; increase **hero bottom** separation to 48px — asymmetric rhythm creates hierarchy without removing content.

---

## Why the site still feels old

1. **Same card recipe everywhere** — W3V2 unified appearance without differentiating **importance**.
2. **Hero zones are layout columns, not designed objects** — automotive retail expects a single “vehicle offer” panel.
3. **CTAs don’t rank** — graphite-default buttons and green VIN compete with red buy.
4. **Canvas vs card contrast too weak** — eye sees flat white field.
5. **Section typography flat** — homepage reads as stacked OC modules.
6. **Dark widgets clone header/footer** — credit/VIN feel like site chrome, not product story.
7. **New catalog track lagging** — W3UX-C1 improved used only; `/auto/` still OC-default hierarchy.
8. **Hover-dependent hierarchy** — catalog CTA only shouts after mouse-over.

---

## Cross-wave interaction notes

| Active wave | W3VIS must preserve |
|-------------|---------------------|
| W3UX-C1 | `.used_catalog` density selectors — hierarchy layers **append after** U-01–U-11 |
| W3V2 | Token names `--w3v2-*` — extend with `--vis-*`, do not replace |
| W3-V | Radius/spacing tokens — compatible |
| W3-C rollback lesson | **CSS-only** — no twig unless operator authorizes class hooks on hero wrapper |

---

## Related documents

| Document | Role |
|----------|------|
| [SITE-001-W3V2-DECISION-v1.md](SITE-001-W3V2-DECISION-v1.md) | Superseded for perceptual goal |
| [SITE-001-W3UX-DENSITY-AUDIT-v1.md](SITE-001-W3UX-DENSITY-AUDIT-v1.md) | Density vs hierarchy distinction |
| [SITE-001-W2-VISUAL-SPECIFICATION-v1.md](SITE-001-W2-VISUAL-SPECIFICATION-v1.md) | Original VG-03 PDP clarity goal |
| [SITE-001-W3VIS-01-DECISION-v1.md](SITE-001-W3VIS-01-DECISION-v1.md) | Execution gate |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3VIS-01 discovery (Tasks 1–4, W3VIS-01A–E) |

*SITE-001 W3VIS-01 Discovery v1 — discovery only; no site modifications.*
