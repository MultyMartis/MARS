# SITE-001 W2 Visual Specification v1

**Type:** Phase 2 visual refresh specification — **documentation only**  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Active theme:** `auto` — `catalog/view/theme/auto/`  
**Inputs:** [SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md](SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md) · [SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md](SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md)

**Explicit exclusions:** No site modifications · No FTP · No admin · No CSS/Twig edits in this document.

---

## Executive summary

Phase 2 visual refresh targets a **modernized, token-driven storefront** on the existing `auto` theme without structural re-platforming. Styling remains anchored in `/css/main.css` and `/css/media.css`; templates change only where markup duplication blocks CSS-only fixes (catalog cards, PDP sections, footer/forms).

**Scope boundary:** Storefront surfaces (homepage, `/cars/*`, `/auto/*`, PDP, about, contact, header/footer). Account/checkout OC `stylesheet.css` blues are **out of scope** for W3 unless operator adds **W3-G OC Legacy** later.

---

## 1. Visual goals

| ID | Goal | Success signal |
|----|------|----------------|
| VG-01 | **Unified brand surface** — one red/neutral palette via CSS custom properties | No hardcoded `rgb(170,3,3)` literals in changed rules; tokens referenced |
| VG-02 | **Scannable catalog** — vehicle cards readable at a glance (price, year, credit, stock) | Card grid passes 3-second scan test on desktop + mobile |
| VG-03 | **PDP conversion clarity** — price → key specs → primary CTA hierarchy on both PDP tracks | Used and new PDP share CTA/button/card token usage |
| VG-04 | **Reduced footer weight** — legal compliance preserved, visual noise lowered | Footer scroll depth ↓; compliance blocks still present |
| VG-05 | **Consistent interaction language** — buttons, radius, shadows, spacing follow one system | No mixed 0/4/12px radius without documented exception |
| VG-06 | **Maintain incremental rollback** — each W3 wave reversible per Phase 1 rollback tiers | Per-wave file list + backup before write |

**Non-goals (Phase 2 W3):** Full homepage redesign · new logo artwork · checkout skin · third-party widget removal (Callibri, SmartWidgets, DMP) · DB or SEO changes.

---

## 2. Design principles

| Principle | Application |
|-----------|-------------|
| **Automotive retail clarity** | Price, monthly payment, mileage/year, and stock state must dominate card and PDP hero zones. Decorative chrome secondary. |
| **Token-first, template-second** | Prefer `:root` + class updates in `main.css`/`media.css`; touch twig only when markup duplication prevents one CSS pass. |
| **Dual-track parity** | Used (`category.twig`, `product.twig`) and new (`categorynew.twig`, `productnew.twig`) share tokens and card/button rules; layout differences (`car-media`, trim blocks) remain intentional. |
| **Progressive density** | Catalog = compact; PDP = information-rich but sectioned; footer = collapsed legal tiers. |
| **Accessibility baseline** | Maintain contrast on red CTAs (white text); avoid reducing footer legal below 12px; preserve focus states on forms. |
| **TEST-safe iteration** | No production writes; bind to checkpoint before each wave; modification cache refresh after twig edits. |

---

## 3. Spacing rules

### 3.1 Base scale (recommended token set)

Introduce in `:root` during **W2-PRE** (no visual change until values applied):

| Token | Value | Usage |
|-------|-------|-------|
| `--space-2xs` | `4px` | Icon gaps, badge padding |
| `--space-xs` | `8px` | Inline label gaps, tag padding |
| `--space-sm` | `12px` | Card internal padding (compact) |
| `--space-md` | `16px` | Default block padding, form field gaps |
| `--space-lg` | `24px` | Section separation within PDP |
| `--space-xl` | `32px` | Catalog grid gutter (desktop) |
| `--space-2xl` | `48px` | Major section breaks (homepage blocks) |
| `--space-3xl` | `64px` | Hero / slider bottom margin |

**Current state (discovery):** Ad-hoc pixel values across 558 grid/layout rule hits; no documented scale.

**Target:** New and refactored rules use tokens; legacy literals migrated opportunistically per wave (catalog → PDP → shell).

### 3.2 Surface-specific spacing

| Surface | Rule |
|---------|------|
| **Catalog grid** | Card gutter `--space-xl` desktop; `--space-md` mobile. Filter sidebar padding `--space-lg`. |
| **Catalog card interior** | Image-to-content `--space-sm`; price row to meta `--space-xs`. |
| **PDP hero** | Gallery-to-info column `--space-xl`; CTA stack gap `--space-sm`. |
| **PDP characteristics grid** | Cell padding `--space-sm`; row gap `--space-xs`. |
| **Footer** | Section stack `--space-lg` (reduced from current dense stack); legal micro-copy `--space-xs` between paragraphs. |
| **Lead forms** | Field vertical rhythm `--space-md`; submit button top margin `--space-lg`. |

### 3.3 Container

Retain existing `.container` behavior; do not change max-width without operator approval. Horizontal padding minimum `--space-md` on mobile breakpoints in `media.css`.

---

## 4. Border radius rules

### 4.1 Token set

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-none` | `0` | Full-bleed images, nav bars |
| `--radius-sm` | `4px` | **Default** — buttons, inputs, catalog cards (current dominant) |
| `--radius-md` | `8px` | Modals, popup forms, filter panels |
| `--radius-lg` | `12px` | `.car-media` tiles, new-car color swatches, gallery thumbs |
| `--radius-full` | `9999px` | Pills/badges only (if introduced) |

**Current state:** ~81 radius rule hits; mix of `0`, `4px`, `12px` (`.car-media`).

**Target policy:**

- **Buttons, inputs, catalog cards:** `--radius-sm` (4px) — preserves familiar automotive retail look.
- **Media mosaics / new-car gallery:** `--radius-lg` (12px) — keep differentiated new-car vocabulary.
- **No new arbitrary radii** — if a component needs change, map to nearest token.

---

## 5. Shadow rules

### 5.1 Token set

| Token | Value | Usage |
|-------|-------|-------|
| `--shadow-none` | `none` | Default card rest state (optional flatten) |
| `--shadow-sm` | `0 1px 3px rgba(33, 36, 43, 0.08)` | Subtle card elevation |
| `--shadow-md` | `0 4px 12px rgba(33, 36, 43, 0.12)` | Hover card, dropdown |
| `--shadow-focus` | `0 0 0 3px rgba(170, 3, 3, 0.25)` | Focus ring (forms, buttons) — replaces red glow scatter |
| `--shadow-cta` | `0 4px 4px -5px rgba(170, 3, 3, 0.35)` | Primary CTA hover (evolved from current red glow) |

**Current state:** ~20 shadow declarations; red-tinted `box-shadow: 0 0 10px …` on focus/hover.

**Target policy:**

- **Cards:** rest `--shadow-sm` or none; hover `--shadow-md` (reduce aggressive red glow).
- **Buttons:** rest flat or `--shadow-sm`; hover `--shadow-cta` on primary only.
- **Modals/popups:** `--shadow-md`.
- **Do not** add shadows to footer legal text blocks.

---

## 6. Button rules

### 6.1 Types

| Class family | Role | Spec |
|--------------|------|------|
| `.callback_btn`, `.home_slider_btn` | Primary lead CTA | Background `--color-primary`; text `--color-on-primary`; radius `--radius-sm`; padding `12px 24px`; font Inter 600 |
| `.phone_btn` | Click-to-call | Same primary fill; phone icon optional |
| `.whatsapp_btn` | WhatsApp | **Keep distinct** — green accent `#2CB741` / `rgb(44, 183, 65)` on hover; do not merge with primary red |
| `.car_main_info__btns` * | PDP action row | Primary + secondary pair; equal height; gap `--space-sm` |
| Secondary / ghost | Filter reset, "show more" | Border `1px solid --color-border`; background transparent; hover `--color-surface-muted` |

\* Includes new-car `.new_car_main_info` button row — align tokens, not necessarily class rename in W3.

### 6.2 States

| State | Rule |
|-------|------|
| Default | `--color-primary` (`#aa0303` / token) |
| Hover | `--color-primary-hover` (`#c80000` / token) |
| Active | Darken 8% from hover |
| Focus | `--shadow-focus` outline |
| Disabled | Opacity 0.5; no hover shadow |

### 6.3 Sizing

| Context | Min height | Notes |
|---------|------------|-------|
| Header/footer CTAs | `40px` | Maintain tap target |
| PDP hero CTAs | `48px` | Prominent conversion |
| Card inline CTAs | `36px` | If present |

**Current state:** 44 button rule hits; hardcoded fills; 4px radius dominant.

---

## 7. Card rules

### 7.1 Vehicle catalog card (`.catalog_item`)

**Applies to:** `category.twig`, `categorynew.twig`, homepage catalog blocks in `home.twig`.

| Element | Spec |
|---------|------|
| Container | Background `--color-surface`; radius `--radius-sm`; overflow hidden |
| Image | Aspect ratio preserved; no radius on image top if full-bleed |
| Price (`.catalog_item__price`) | Largest type on card; `--color-text-primary` |
| Credit line | Secondary size; `--color-text-muted` |
| Tags (`.catalog_item__tags`) | `--space-2xs` padding; stock green `--color-success` |
| Hover | `--shadow-md`; subtle translate optional (`translateY(-2px)`) — **one** motion max |
| Swiper inside card | Pagination uses `--swiper-theme-color: var(--color-primary)` |

**Duplication constraint:** Markup exists in 3+ templates — W3-A must either (a) align HTML structure across files, or (b) document intentional deltas with shared CSS only.

### 7.2 PDP summary card (inline blocks)

Used PDP info panel and new-car trim blocks should reuse `--color-surface`, `--radius-sm`, `--space-md` padding for visual kinship with catalog cards.

---

## 8. Typography recommendations

### 8.1 Font stack (retain)

| Role | Family | Source |
|------|--------|--------|
| Body | **Exo 2** | Google Fonts (loaded in `header.twig`) |
| Accent / buttons / labels | **Inter 600** | Google Fonts |

**Do not** add a third family in W3.

### 8.2 Recommended scale

| Token | Size | Line height | Usage |
|-------|------|-------------|-------|
| `--text-xs` | `12px` | 1.4 | Footer legal, badges |
| `--text-sm` | `14px` | 1.5 | Meta labels, filter labels |
| `--text-base` | `16px` | 1.5 | Body, form inputs |
| `--text-lg` | `18px` | 1.4 | Card subtitles |
| `--text-xl` | `24px` | 1.3 | Section headings |
| `--text-2xl` | `32px` | 1.2 | PDP price |
| `--text-3xl` | `40px` | 1.1 | Homepage H1 (when visible) |

**Current gap:** No documented scale; heading sizes vary by block.

**Implementation:** Define tokens in `:root`; migrate catalog price, PDP price, and footer legal first.

### 8.3 Hierarchy rules

- **One H1 per page** — already Phase 1 compliant; preserve.
- **PDP:** Price = `--text-2xl`; characteristics labels = `--text-sm` uppercase or muted; values = `--text-base`.
- **Catalog:** Price = `--text-lg`/`--text-xl`; vehicle title = `--text-base` semibold.
- **Footer:** Section titles `--text-sm` bold; legal `--text-xs`.

---

## 9. Footer reduction strategy

**Problem (discovery):** `footer.twig` (410 lines) — legal wall, 6+ callback forms, manufacturer lists, duplicated phone blocks; visually heavy.

**Objectives:** Preserve legal compliance; reduce scroll depth and repeated CTAs; centralize form embed pattern.

### 9.1 Tiers

| Tier | Content | Action |
|------|---------|--------|
| **Keep visible** | Logo, primary phone, WhatsApp (if C-04 resolved), main nav links, copyright, primary legal entity line | Restyle with spacing tokens; no content removal without legal review |
| **Collapse** | Long loan-term / compliance paragraphs | Accordion or "Подробнее" expander — **one** block, default collapsed on mobile |
| **Consolidate** | Duplicate callback forms (6+ embeds) | Single footer form + link to modal; remove redundant inline duplicates where AJAX handler allows |
| **Relocate** | Manufacturer lists (if duplicated from catalog) | Link to `/cars/` and `/auto/` instead of full inline lists — **operator approval required** |
| **Defer** | Third-party script blocks (Callibri, SmartWidgets) | No removal in W3-C |

### 9.2 CSS-first steps (before twig surgery)

1. Increase section spacing tokens; reduce visual borders between legal blocks.
2. Mute legal body text to `--color-text-muted`; keep entity name `--color-text-primary`.
3. Hide redundant phone strip if identical to header (mobile) — **verify** with operator.

### 9.3 Twig touch points

| File | Expected change level |
|------|------------------------|
| `template/common/footer.twig` | **HIGH** — form consolidation, accordion markup |
| `css/main.css` | **MEDIUM** — footer-specific tokens |
| `css/media.css` | **MEDIUM** — collapsed legal on mobile |

**Risk:** Inline styles in `footer.twig` (8 hits) — migrate to classes during W3-C.

---

## 10. Catalog density strategy

**Problem:** High information value but uneven spacing; no breadcrumbs on listing pages; empty manufacturer categories on TEST show shell-only UX.

### 10.1 Grid density targets

| Viewport | Columns | Cards visible above fold (target) |
|----------|---------|-----------------------------------|
| Desktop ≥1200px | 4 | 8 (2 rows) |
| Tablet 768–1199px | 2–3 | 4–6 |
| Mobile <768px | 1–2 | 3–4 |

**Levers:** Reduce card vertical padding `--space-sm`; tighten image height cap if CSS-controlled; filter sidebar width fixed — do not squeeze grid below 280px card min-width.

### 10.2 Filter / sort bar

- Sticky filter header on mobile (CSS `position: sticky`) — optional W3-A stretch goal.
- Sort controls align to `--text-sm`; primary filter actions use secondary button style.

### 10.3 Breadcrumbs on listings

**Add** breadcrumb row to `category.twig` and `categorynew.twig` matching PDP pattern (Home → Б/У or Новые → category). Centralize markup pattern; fix known `</a></a>` typo on used PDP in same pass or W3-B.

### 10.4 Empty states

When manufacturer category has zero listings (TEST data gap): show muted message + link to parent catalog — requires minimal twig + CSS; does not block W3-A if TEST inventory populated later.

### 10.5 Files

| File | Role |
|------|------|
| `template/product/category.twig` | Used catalog |
| `template/product/categorynew.twig` | New catalog |
| `template/common/home.twig` | Homepage catalog blocks (card parity) |
| `css/main.css`, `css/media.css` | Grid, card, filter |
| `js/common.js` | Model filter lists — **class names must remain stable** unless JS updated |

---

## 11. PDP used-car improvement strategy

**Template:** `template/product/product.twig` (925 lines) · body class `used_car_page`

### 11.1 Layout priorities

| Zone | Current | Target |
|------|---------|--------|
| Gallery + thumbs | Swiper + Fancybox | Keep; unify thumb radius `--radius-lg`; lazy-load unchanged |
| Price + credit | Dense block | Price `--text-2xl`; credit secondary; CTA row `--space-sm` gap |
| Characteristics grid | `.car_main_info__characteristics_*` | Zebra or bordered cells with `--space-sm` padding; label/value contrast |
| VIN block | Present | Collapse behind "Показать VIN" on mobile if height excessive |
| Credit calculator | JS-driven | Style inputs to form tokens; do not change calc logic in W3 |
| Viewer count | JS placeholder | Style muted; consider hiding until JS hydrates — **optional** |

### 11.2 CTA hierarchy

1. **Primary:** Callback / "Заказать звонок" — primary button token  
2. **Secondary:** Phone — `phone_btn`  
3. **Tertiary:** WhatsApp — green token  

### 11.3 Markup fixes (W3-B)

- Fix breadcrumb `</a></a>` nesting.
- Migrate inline styles (6+ hits) to classes.
- Preserve Swiper/Fancybox class hooks.

### 11.4 CSS focus

- `.car_main_info*` family → token migration
- Gallery + characteristics section spacing `--space-lg`

**Out of scope W3-B:** Review system (`product/review.twig`) — low live exposure.

---

## 12. PDP new-car improvement strategy

**Template:** `template/product/productnew.twig` (671 lines) · body class `new_car_page`

### 12.1 Layout priorities

| Zone | Current | Target |
|------|---------|--------|
| Trim / variant blocks | Unique to new cars | Card-like containers; shared button tokens with used PDP |
| Color gallery | Hidden slides + visible swatches | Swatch `--radius-lg`; active state `--shadow-focus` |
| `car-media` mosaic | `--radius` 12px local vars | Bind to `--radius-lg` token |
| Configuration toggles | `.car_configuration__toggle` | Align to secondary button + active primary fill |
| Breadcrumbs | Present | Parity with used PDP fixes |

### 12.2 Parity with used PDP

| Shared | Separate |
|--------|----------|
| Color tokens, buttons, typography, shadows | Trim selector, color gallery, `car-media` layout |

### 12.3 Dual-track scheduling

**W3-E runs after W3-B** so used PDP establishes shared PDP tokens; new-car-specific blocks extend without redefining base.

### 12.4 Files

| File | Role |
|------|------|
| `template/product/productnew.twig` | Primary |
| `css/main.css` | `.new_car_main_info*`, `.car-media`, `.car_configuration*` |
| `css/media.css` | Mosaic responsive |

**Inactive backups** (`productnew_Backup.twig`) — do not edit; confirm not referenced by controller.

---

## 13. Color tokens (reference)

To be added in **W2-PRE** `:root` block:

| Token | Initial value | Notes |
|-------|---------------|-------|
| `--color-primary` | `#aa0303` | Maps existing brand red |
| `--color-primary-hover` | `#c80000` | Existing hover red |
| `--color-text-primary` | `#21242b` | `rgb(33, 36, 43)` |
| `--color-text-muted` | `#374c60` | Secondary labels |
| `--color-surface` | `#ffffff` | Cards, modals |
| `--color-surface-muted` | `#f6f8fa` | Section backgrounds |
| `--color-border` | `#d0d0d0` | Inputs, dividers |
| `--color-success` | `#00aa00` | Stock markers |
| `--color-whatsapp` | `#2cb741` | WhatsApp hover accent |
| `--color-on-primary` | `#ffffff` | Button text |

**W2-COLORS wave:** Operator may adjust `--color-primary` only via token swap — no literal hunt across 6k lines after PRE migration.

---

## 14. Stylesheet load order (unchanged)

Per discovery — do not reorder without cause:

1. `normalize.css` → Google Fonts → vendor CSS → OC `styles` loop → **`main.css`** → **`media.css`**

Phase 2 edits concentrate on **`main.css`** and **`media.css`**.

---

## 15. Related documents

| Document | Role |
|----------|------|
| [SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md](SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md) | Evidence base |
| [SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md](SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md) | W3 execution sequence |
| [SITE-001-W2-DECISION-v1.md](SITE-001-W2-DECISION-v1.md) | W2.1 specification gate |
| [SITE-001-W1-BACKUP-PROCEDURE-v1.md](SITE-001-W1-BACKUP-PROCEDURE-v1.md) | Pre-write backup |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | Rollback tiers |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W2.1 visual specification v1 |

*SITE-001 W2 Visual Specification v1 — documentation only; no site modifications.*
