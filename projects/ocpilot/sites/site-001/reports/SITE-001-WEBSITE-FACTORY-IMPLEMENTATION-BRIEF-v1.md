# SITE-001 — Website Factory Implementation Brief v1

**Type:** OCPilot execution brief — CSS-only visual direction  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Wave:** **W3WF-01** — Website Factory Visual Direction Implementation  
**Design authority:** [SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md)  
**Decision gate:** [SITE-001-WEBSITE-FACTORY-DECISION-v1.md](SITE-001-WEBSITE-FACTORY-DECISION-v1.md)

**Role split:**

| Role | Owner |
|------|-------|
| Visual direction, acceptance criteria | **Website Factory** |
| Charter, backup, rollback, FTP, verification | **OCPilot** |
| Design invention | **FORBIDDEN for OCPilot** |

---

## 1. Scope summary

Implement **«Graphite Salon»** atmosphere on TEST — **CSS-only**, **one append block** per file with marker `SITE-001 W3WF-01 Website Factory Visual Direction`.

If W3ATMOSPHERE-01 block exists: **replace or supersede** atmosphere selectors within W3WF-01 block per selector map below — do not leave conflicting rules. Preserve W3UX-C1 block **verbatim**.

---

## 2. Editable files

| File | Edit |
|------|------|
| `css/main.css` | **YES** — append W3WF-01 block at end |
| `css/media.css` | **YES** — append W3WF-01 responsive block at end |

---

## 3. Forbidden files / layers

| Layer | Edit |
|-------|------|
| All Twig templates | **NO** |
| PHP controllers | **NO** |
| JS (`/js/common.js`, libs) | **NO** |
| Database | **NO** |
| Admin templates | **NO** |
| `catalog/view/theme/auto/stylesheet/stylesheet.css` | **NO** (out of scope) |
| Images / fonts | **NO** |

---

## 4. Active blocks to preserve (do not modify rules inside)

| Block marker / scope | Preserve |
|---------------------|----------|
| Phase 1 branding | All copy, logos, URLs |
| `SITE-001 W3UX-C1` block | `.used_catalog` density — **copy verbatim** if re-saving files |
| Header/footer **structure** | DOM, columns, links, CTA count |
| PDP layout | No hero wrapper, no CTA reorder |
| W3VIS rollback state | No W3VIS selectors reintroduced |

**Allowed:** W3WF-01 may override **visual properties** on shared selectors if they do not change layout dimensions (color, background, shadow, border-color, border-radius, opacity).

---

## 5. Allowed CSS properties

| Property | Allowed | Notes |
|----------|---------|-------|
| `background` / `background-color` | **YES** | Canvas, surfaces, gradients |
| `background-image` | **YES** | Only overlay gradients on existing image bands |
| `linear-gradient` | **YES** | Nav, footer, dark bands |
| `box-shadow` | **YES** | Depth stack per WF tokens |
| `border-color` | **YES** | Soft graphite borders |
| `border` (width style) | **YES** | Only if width unchanged from computed layout |
| `color` | **YES** | Text, links, price accents |
| `opacity` | **YES** | Overlays |
| `border-radius` | **YES** | 12px card unification — no dimension change |
| `outline` / focus ring via box-shadow | **YES** | `--wf-shadow-focus` |
| `:hover` / `:focus` visual states | **YES** | Shadow/border/color only |
| `backdrop-filter` | **CAUTION** | Only on existing overlay selectors if already present — prefer opacity gradient |

---

## 6. Forbidden CSS properties

| Property | Forbidden | Reason |
|----------|-----------|--------|
| `margin` | **NO** | Layout / density |
| `padding` | **NO** | Layout / W3UX-C1 |
| `width` / `height` / `min-*` / `max-*` | **NO** | Layout |
| `flex` / `flex-order` / `order` | **NO** | CTA hierarchy |
| `display` / `position` / `float` / `grid-template-*` | **NO** | Structure |
| `font-size` / `line-height` / `font-weight` | **NO** | Typography hierarchy |
| `gap` | **NO** | Spacing |
| `transform` / `translate` | **NO** | Motion layout |
| `content` + new pseudo elements | **NO** except footer logo accent line on **existing** wrapper |

**Exception:** `border-radius`, `box-shadow`, `border-color`, `color`, `background-*` changes that do not alter box model dimensions.

---

## 7. Implementation phases (W3WF-01)

Execute in order within single CSS upload.

### Phase A — Token root

Append to `:root` (or create `--wf-*` block with bridges):

```css
/* SITE-001 W3WF-01 Website Factory Visual Direction — Phase A Tokens */
:root {
  --wf-canvas: #EEF1F5;
  --wf-surface-card: #FFFFFF;
  --wf-surface-raised: #FAFBFC;
  --wf-surface-sunken: #E4E8ED;
  --wf-surface-tint: #F4F6F9;
  --wf-graphite-main: #2F343E;
  --wf-graphite-secondary: #3A404C;
  --wf-graphite-deep: #1A1D24;
  --wf-graphite-gradient-top: #353A45;
  --wf-graphite-gradient-bottom: #272B33;
  --wf-brand-red: #9E0202;
  --wf-brand-red-hover: #BA0000;
  --wf-brand-red-soft: rgba(158, 2, 2, 0.08);
  --wf-brand-red-muted: #B82424;
  --wf-border: rgba(47, 52, 62, 0.10);
  --wf-border-hover: rgba(47, 52, 62, 0.16);
  --wf-border-on-dark: rgba(236, 238, 242, 0.10);
  --wf-text-main: #2A2F38;
  --wf-text-secondary: #5A6270;
  --wf-text-on-dark: #EDEFF3;
  --wf-text-on-dark-muted: #A8AEB8;
  --wf-success: #1F8A4C;
  --wf-whatsapp: #25A244;
  --wf-shadow-sm: 0 1px 2px rgba(42, 47, 56, 0.05), 0 2px 6px rgba(42, 47, 56, 0.04);
  --wf-shadow-md: 0 2px 8px rgba(42, 47, 56, 0.07), 0 6px 20px rgba(42, 47, 56, 0.05);
  --wf-shadow-lg: 0 4px 14px rgba(42, 47, 56, 0.08), 0 12px 32px rgba(42, 47, 56, 0.06);
  --wf-shadow-inset-highlight: inset 0 1px 0 rgba(255, 255, 255, 0.60);
  --wf-shadow-header: 0 2px 8px rgba(42, 47, 56, 0.06), 0 1px 0 rgba(42, 47, 56, 0.04);
  --wf-shadow-cta: 0 4px 14px rgba(158, 2, 2, 0.20);
  --wf-shadow-focus: 0 0 0 3px rgba(158, 2, 2, 0.18);
  /* Bridge legacy namespaces */
  --w3color-canvas: var(--wf-canvas);
  --w3v2-brand-red: var(--wf-brand-red);
}
```

### Phase B — Canvas

```css
body {
  background-color: var(--wf-canvas) !important; /* specificity over legacy */
}
```

### Phase C — Header shell

| Selector | Properties |
|----------|------------|
| `.singe_bar__wrap` | `box-shadow: var(--wf-shadow-header);` + inset highlight |
| `nav`, `.navbar`, `.offcanvas_nav` | `background: linear-gradient(180deg, var(--wf-graphite-gradient-top), var(--wf-graphite-main));` `border-color: var(--wf-border-on-dark);` |
| `.logo > span` | `color: var(--wf-text-secondary);` |
| `.callback_btn:hover`, `.home_slider_btn:hover`, `.phone_btn:hover` | `box-shadow: var(--wf-shadow-cta);` |

### Phase D — Footer shell

| Selector | Properties |
|----------|------------|
| `footer`, `.footer_top` | graphite gradient background |
| `footer` borders (top/bottom) | `1px solid var(--wf-border-on-dark)` — override `10px solid rgb(14,15,16)` |
| Footer legal text selectors | `color: var(--wf-text-on-dark-muted);` |
| Footer headings / primary links | `color: var(--wf-text-on-dark);` |
| Footer section title borders | `border-color: rgba(237,239,243,0.12);` |

### Phase E — Unified L2 card group

Apply shared recipe to:

```
.catalog_item > a,
.catalog_item > div,
.partner_banks__item,
.reviews__item > .inner,
.four_blocks > div,
.fancy_two_blocks__item,
.new_car_bonus__item,
.contacts_info_block > div,
.newcar_config__item_inner
```

```css
/* L2 rest */
background: var(--wf-surface-card);
border: 1px solid var(--wf-border);
border-radius: 12px;
box-shadow: var(--wf-shadow-sm), var(--wf-shadow-inset-highlight);
/* L2 hover */
:hover {
  box-shadow: var(--wf-shadow-md);
  border-color: var(--wf-border-hover);
}
```

**Exclude** from hover transform if present — do not add `translateY`.

### Phase F — Tool panels (L2-alt)

| Selector | Properties |
|----------|------------|
| `.search_form`, `.search_wrap .search_form`, filter panels | `background: var(--wf-surface-raised);` + L2 border/shadow |

### Phase G — Forms

| Selector | Properties |
|----------|------------|
| `input`, `textarea`, `select` (storefront forms) | `border-color: var(--wf-border);` |
| `input:focus`, `textarea:focus` | `box-shadow: var(--wf-shadow-focus);` — remove red neon glow |
| `.fancy_form_block` | graphite gradient overlay on existing background |

### Phase H — Legacy atmosphere purge (override layer)

Within W3WF-01 block, override with equal or higher specificity:

| Legacy pattern | WF replacement |
|----------------|----------------|
| `rgb(170, 3, 3)` on CTAs/prices | `var(--wf-brand-red)` / `var(--wf-brand-red-muted)` |
| `rgb(33, 36, 43)` on nav/footer/dark bands | graphite gradient tokens |
| `rgb(208, 208, 208)` borders | `var(--wf-border)` |
| `rgb(0, 170, 0)` stock | `var(--wf-success)` |
| `rgba(55, 76, 96, 0.4)` catalog hover | `var(--wf-shadow-md)` |
| `0 0 10px rgb(170, 3, 3)` focus | `var(--wf-shadow-focus)` |
| `rgb(14, 15, 16)` / `rgb(16, 18, 21)` seams | `var(--wf-border-on-dark)` |

**Note:** Full base-layer literal deletion is **OUT OF CHARTER** — override cascade is required approach per W3ATMOSPHERE N-01.

### Phase I — PDP widgets (atmosphere only)

| Selector | Properties |
|----------|------------|
| `.car_main_info__discount` | L2 card recipe |
| `.used_car__credit`, `.car_vin_check` | graphite gradient — match nav/footer |
| `.car_main_info__photo`, `.car_main_info__main` | optional subtle border/shadow if no layout change |

**OUT OF SCOPE:** `.car_main_info` flex structure, `.car_main_info__btns` order, hero wrapper.

### Phase J — Mobile (`media.css`)

Mirror Phases B–I at existing breakpoints for:

- `nav` / offcanvas
- `.catalog_item` card group
- `footer`
- `.singe_bar__wrap`

**Preserve** W3UX-C1 mobile rules — append W3WF-01 **after** W3UX-C1 block.

---

## 8. OCPilot execution checklist (W3WF-01)

| Step | Action | Owner |
|------|--------|-------|
| 1 | Write charter `SITE-001-W3WF-01-WRITE-CHARTER-v1.md` | OCPilot |
| 2 | Change request `CR-SITE-001-W3WF-01-2026-06-09` | OCPilot |
| 3 | Rollback plan `SITE-001-W3WF-01-ROLLBACK-PLAN-v1.md` | OCPilot |
| 4 | Backup `css/main.css` + `css/media.css` → `pre-w3wf-01-YYYYMMDD-HHMM` | OCPilot |
| 5 | Implement CSS per §7 | OCPilot |
| 6 | Clear caches (system, modification, image) + modification refresh | OCPilot |
| 7 | Verify 7+ URLs (see §9) | OCPilot |
| 8 | Generate before/after screenshots → `qa/w3wf-01-screenshots/` | OCPilot |
| 9 | Operator acceptance per design checklist | Operator |

---

## 9. Verification URLs

| Label | URL | Required |
|-------|-----|----------|
| homepage | `/` | **YES** |
| about | `/about` | **YES** |
| contact | `/contact/` | **YES** |
| used_catalog | `/cars/` | **YES** |
| used_brand | `/cars/bmw/` | **YES** |
| new_catalog | `/auto/` | **YES** |
| new_brand | `/auto/haval/` | **YES** |
| used_pdp | first available `/cars/.../product` | **YES if available** |
| new_pdp | first available `/auto/.../product` | **YES if available** |

**Pass criteria:** HTTP 200 · live CSS contains `W3WF-01` marker · `--wf-canvas` + `#EEF1F5` present · W3UX-C1 marker preserved · W3VIS markers absent.

---

## 10. Design acceptance checklist (operator)

Implementation passes only if ordinary user can see **without A/B**:

| # | Criterion | Pass |
|---|-----------|------|
| 1 | Site looks less template-like | ☐ |
| 2 | Header looks more premium | ☐ |
| 3 | Footer looks more premium | ☐ |
| 4 | Cards/forms/banks belong to one visual system | ☐ |
| 5 | Canvas no longer feels like a white sheet | ☐ |
| 6 | Red feels branded, not aggressive | ☐ |
| 7 | Dark tones feel graphite, not flat black | ☐ |
| 8 | No PDP hero redesign happened | ☐ |
| 9 | No structure changed | ☐ |
| 10 | No content changed | ☐ |

**Scoring:** ≥ **7/10** true → **PASS** · &lt; 7/10 → **Design FAIL** → T1 rollback.

---

## 11. Rollback

| Tier | Action |
|------|--------|
| **T1** | Restore `css/main.css` + `css/media.css` from `pre-w3wf-01-*` backup |
| Cache | Clear all + modification refresh |

Do **not** use Beget global backup unless T1 package corrupt.

---

## 12. Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Invisible improvement (partial scope) | Mandatory full Phases A–J in one wave |
| W3UX-C1 regression | Charter exclusion + post-verify `/cars/` height probe |
| PDP operator rejection | No hero/CTA selectors in brief |
| Dual namespace conflict | Single `--wf-*` block with bridges |
| Legacy literals bleed through | Phase H specificity overrides |
| Operator expects «new site» | Set expectation: ~6–7/10 transformation |

---

## 13. Related documents

| Document | Role |
|----------|------|
| [SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md) | Visual spec |
| [SITE-001-WEBSITE-FACTORY-DECISION-v1.md](SITE-001-WEBSITE-FACTORY-DECISION-v1.md) | Authorization gate |
| [SITE-001-W3UX-C1-DECISION-v1.md](SITE-001-W3UX-C1-DECISION-v1.md) | Density preserve |
| [SITE-001-W3VIS-ROLLBACK-DECISION-v1.md](SITE-001-W3VIS-ROLLBACK-DECISION-v1.md) | PDP OUT OF SCOPE |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — Website Factory implementation brief for W3WF-01 |

*SITE-001 Website Factory Implementation Brief v1 — documentation only until OCPilot charter authorized.*
