# FP-0002 — Home Visual Style Baseline v1

**Audit ID:** `home-style-baseline-01`  
**Authority commit:** `f5a9ecd7` (`fp-0002-v7-home-operator-stable-before-style-audit-01`)  
**Workspace:** `workspaces/fp-0002-shpigovsky-v7/`  
**Date:** 2026-06-26  
**Mode:** Read-only documentation — operator-canonical source at tag HEAD

---

## 1. Scope and authority

| Source | Role |
|--------|------|
| `src/scss/style.scss` @ `f5a9ecd7` | Primary visual authority (single monolithic SCSS file) |
| `src/pages/index.html` @ `f5a9ecd7` | Section order and include parameters |
| `src/js/main.js` @ `f5a9ecd7` | Interaction and slider behavior |
| `dist/` (existing build) | Render inspection — rebuild blocked (dist locked by active `http-server` on `:4174`) |
| `Spig_v1.2.fig` | Design reference — drift noted where operator source differs |

**Working-tree note (not audited as canonical):** two unstaged deltas vs `f5a9ecd7` — typo fix in `home-recovery-intro.html`; `border-radius` on founder variant-b photo. Audit values reflect **committed** operator baseline.

---

## 2. Home section inventory

| Order | Section | Partial | Root class | Behavior | Current role |
| ----: | ------- | ------- | ---------- | -------- | ------------ |
| 0 | Hero | `partials/sections/hero.html` | `.hero.hero--home` | Modal CTA (`data-modal-open`) | Home-only viewport hero with frosted panel |
| 1 | Recovery intro | `partials/sections/home-recovery-intro.html` | `.home-recovery-intro` | Static | Brand positioning + 6-card value grid |
| 2 | Founder quote | `partials/sections/home-founder-quote.html` | `.home-founder-quote` (+ `--variant-b` on Home) | Modal CTA | Founder trust block; variant-b active on Home |
| 3 | Treatment & prevention | `partials/sections/home-treatment-prevention.html` | `.home-treatment-prevention` | Accordion (`data-accordion`) | Service category navigator |
| 4 | Gallery | `partials/sections/home-gallery.html` | `.home-gallery` | Swiper (`data-gallery-slider`) | Photo slider with captions |
| 5 | Why us | `partials/sections/home-why-us.html` | `.home-why-us` | Static (reuses treatment service-list markup) | Multidisciplinary pitch + link list |
| 6 | Staff photo | `partials/sections/home-staff-photo.html` | `.home-staff-photo` | Static bleed image | Full-width staff band |
| 7 | Feature grid | `partials/sections/home-feature-grid.html` | `.home-feature-grid` | Static 3-col cards | Value proposition cards |
| 8 | Clinic landscape | `partials/sections/home-clinic-landscape.html` | `.home-clinic-landscape` | Static bleed image | Environment photo band |
| 9 | Recovery life | `partials/sections/home-recovery-life.html` | `.home-recovery-life` | Static | Program stages with bg overlay |
| 10 | Reviews | `partials/sections/home-reviews.html` | `.home-reviews` | Swiper (`data-reviews-slider`) | Testimonial carousel |
| 11 | Rehab requirements | `partials/sections/home-rehabilitation-requirements.html` | `.home-rehabilitation-requirements` | Modal CTA in dark band | Intake steps + CTA band + support box |
| 12 | Rehab program | `partials/sections/home-rehabilitation-program.html` | `.home-rehabilitation-program` | Static direction cards | 4-direction program — **already on `uslugi.html`** |
| 13 | Genotyping | `partials/sections/home-genotyping.html` | `.home-genotyping` | Modal CTA | Genetics upsell block |
| 14 | Comfort | `partials/sections/home-comfort.html` | `.home-comfort` | Fancybox (`data-fancybox="home-comfort"`) | Photo grid — **already on `uslugi.html`** |
| 15 | Videos | `partials/sections/home-videos.html` | `.home-videos` | Fancybox video (`data-fancybox="home-videos"`) | 2-col video grid |
| 16 | Specialists | `partials/sections/home-specialists.html` | `.home-specialists` | Swiper (`data-specialists-slider`) | Team carousel |
| 17 | Articles | `partials/sections/home-articles.html` | `.home-articles` | Static 3-col grid | Blog teaser grid |
| 18 | FAQ | `partials/sections/home-faq.html` | `.home-faq` | Accordion (`data-accordion`) | FAQ — **already on `uslugi.html`** |
| 19 | Final form | `partials/sections/home-final-form.html` | `.home-final-form` | Lead form (`data-lead-form`) | Dark band form — **already on `uslugi.html`** |

**Layout shell (all pages):** `partials/layout/head.html`, `header.html`, `footer.html`; `partials/components/modal-consultation.html`.

**Spacing modifiers on Home:** `no-top-padding`, `no-top-padding--30` on sections 5–8 to tighten vertical stack after operator polish.

---

## 3. Page foundation

| Property | Actual value | Authority |
|----------|--------------|-----------|
| Body background | `var(--color-page-background)` → `rgba(218, 229, 240, 0.7)` | `:root` |
| Primary text | `#475371` (`--color-text-primary`) | `:root` |
| Secondary/muted text | `#6d7b8f` (`--color-text-secondary`) | `:root` |
| Accent | `rgb(179, 38, 30)` / hover `rgb(197, 37, 28)` | `:root` |
| Inverse text | `#fff` | `:root` |
| Dark surfaces | `--color-text-primary` (#475371) used as dark band bg | CTA bands, final form |
| Light surfaces | `#fff` (`--color-surface`) | Header messenger pills, play buttons |
| Frosted surface | `rgba(255, 255, 255, 0.24)` + `backdrop-filter: blur(5px)` | Hero panel |
| Border color | `rgb(200, 210, 220)` | Cards, header divider |
| Card border (primary pattern) | `1px solid var(--color-text-primary)` | Outline card family |
| Shadow use | Minimal — no global card shadow system | Operator choice |
| Radius system | `--radius-main: 30px`, `--radius-input: 15px`, `--radius-full: 999px` | `:root` |
| Overflow | `overflow-x: clip` on `html`, `body`, `main`, `.intro-section` | Base |
| Base font | Inter 300/400/500 (local WOFF2) | `@font-face` |
| Base size/line | 18px / 24px, weight 300 | `:root` |
| Heading weight | 400 (not bold) | `:root` |

---

## 4. Container system

| Pattern | Selector | Desktop | Tablet (≤1024) | Mobile | Authority |
| ------- | -------- | ------: | -------------: | -----: | --------- |
| Main content container | `.container` | max-width **1230px**, gutters **30px** (`--pad-x`) | gutters **15px** (`--pad-gap-line`) | same as tablet | `style.scss` L352–360, L3713–3716 |
| Hero outer shell | `.hero` | max-width **1400px**, gutters **30px** | gutters **15px** | same | L862–874, L3718–3721 |
| Hero inner content | `.hero__container` | flex column, height **60%** of hero | height auto, min content **320px** | scaled type @930 | L914–925, L3729–3736 |
| Section contained | `section > .container` | 1230px + 30px pad | 1230px + 15px pad | same | All home sections |
| Full-bleed media | `*__bleed` wrappers | 100% width inside container | fixed heights reduced | e.g. staff 448→240px | Section-specific |
| Narrow text inset | `.home-recovery-intro__lead > span` etc. | `padding-left: 15px` | unchanged | unchanged | L641–647 |
| `--container-hero: 1380px` | Token only | **UNUSED in CSS** | — | — | LEGACY_OR_UNUSED |

**Invalidated assumption:** older docs citing 50px desktop container padding — actual desktop gutter is **30px** (`--pad-x`). At ≤1024 gutters become **15px**.

---

## 5. Breakpoints (actual)

| Breakpoint | Purpose | Affected patterns | Canonical status |
| ---------: | ------- | ----------------- | ---------------- |
| **1025+** | Desktop layout | Off-canvas disabled; multi-column grids; dotted service leaders visible | **Primary layout split** |
| **≤1024** | Tablet/mobile layout | Container/hero gutters 15px; hero height auto; grids → 1 col; mobile header | **Primary layout split** |
| 1560 | Hero height cap | `hero--home` max-height 670px | Hero-only cascade |
| 1440 | Hero height cap | max-height 620px | Hero-only |
| 1310 | Hero + header | max-height 530px; logo 70px; hero title 50px | Hero + header |
| 1190 | Header/footer squeeze | Logo 60px; footer stacks to 1 col | Header/footer |
| 930 | Hero typography | Tagline 24px; title 40px; panel padding | Hero-only |
| 767 | — | **Empty block** — no rules | Placeholder |
| 560 | Mobile header | Hide mobile messengers | Header-only |
| 390 | Small mobile | Primary phone font → 14px | Header-only |

**JS alignment:** off-canvas and desktop threshold = **1025px** (`DESKTOP_MIN` in `main.js`).

---

## 6. Typography reality

| Role | Selector / example | Desktop | Mobile (≤1024) | Classification |
| ---- | ------------------ | ------- | -------------- | -------------- |
| H1 (global token) | `h1`, `--font-size-h1` | 46/46 | unchanged token | GLOBAL — hero overrides |
| Hero H1 | `.hero__title` | **70/70** | 40/40 @930 | SECTION-SPECIFIC |
| Hero tagline | `.hero__tagline` | **38/38** | 24/28 @930; 28/28 @1310 | SECTION-SPECIFIC |
| H2 (global) | `h2`, section headings | **36/36**, weight 400 | unchanged | GLOBAL TYPOGRAPHY |
| H3 (global) | `h3` | 26/30 | unchanged | GLOBAL |
| Section lead (accent bar) | `.home-treatment-prevention__lead`, `.rehub-universal-decor` | 18/24, uppercase, 5px left accent | unchanged | **REPEATED PATTERN** |
| Body | `body`, `.home-*__intro` | 18/24, weight 300 | unchanged | GLOBAL |
| Card body | `.home-feature-grid__card-text`, step text | **16/20** | unchanged | REPEATED_LITERAL |
| Card title (uppercase) | `.home-feature-grid__card-title` | 18/24 uppercase | unchanged | CARD FAMILY |
| Button | `.btn` | 14/20, weight 500, **CSS uppercase** | unchanged | GLOBAL COMPONENT |
| Nav | `.site-header__nav-link` | 16/20, weight 400 | hidden ≤1024 | GLOBAL LAYOUT |
| Final form H2 | `.home-final-form__heading` | **30/34** | unchanged | SECTION-ONE-OFF |
| CTA phone (dark band) | `.home-rehabilitation-requirements__cta-phone` | **40/40** | 24/28 @1024 | SECTION-SPECIFIC |
| Article meta | `.home-articles__meta` | 14/20 uppercase accent | unchanged | SECTION-SPECIFIC |
| Small | `--font-size-small` | 14/20 | @390 phone | GLOBAL TOKEN |

**Lead paragraph inset pattern:** `.home-recovery-intro__lead > span`, `.home-founder-quote__text > span`, `.home-why-us__body > span`, `.home-recovery-life__intro-text > span` — `padding-left: 15px` (visual secondary column).

**`&nbsp;` rule:** Hard-coded non-breaking spaces in HTML copy for Russian typography (prepositions, dashes, brand name). Operator-canonical; not generated.

---

## 7. Vertical rhythm ladder

Repeating spacing values from `:root` and section rules:

| Value | Token / usage | Frequency |
|------:|---------------|-----------|
| 50px | `--pad-y` — `main` and every `main > section` top/bottom | Global section rhythm |
| 30px | `--pad-gap`, `--pad-x` (desktop gutter) | Grid gaps, card padding, section internal gaps |
| 30px | `no-top-padding--30` | Reduced bottom padding between stacked home sections |
| 25px | Hero panel padding-y; FAQ item padding | Component-local |
| 20px | `--pad-box` | Header top row gap |
| 15px | `--pad-gap-line` — mobile gutter, list gaps, pagination margin | High reuse |
| 10px | `--pad-gap-tight` | Minor gaps |
| 5px | `--pad-gap-mini` | Button icon gap, star gap |

**No mobile reduction of `--pad-y`:** section vertical rhythm stays 50px at all breakpoints (confirmed in Phase 4A rhythm authority doc).

---

## 8. Card and surface families

### Family A — Outline bordered card
- **Visual:** 1px `var(--color-text-primary)` border, `--radius-main`, transparent bg
- **Selectors:** `.home-recovery-intro__card`, `.home-feature-grid__card`, `.home-reviews__card`, `.home-recovery-life__stage`, `.home-rehabilitation-program__direction`, `.home-faq__item`, support box
- **Padding:** typically `var(--pad-gap)` (30px)
- **Hover:** link/service items → accent color; cards mostly static

### Family B — Dark CTA band
- **Visual:** bg `var(--color-text-primary)`, inverse text, `--radius-main`, 10% bg image overlay
- **Selectors:** `.home-rehabilitation-requirements__cta-band`, `.home-final-form__band`
- **Desktop:** 3-col grid (copy | phone | button) or 2-col (copy | form)

### Family C — Media bleed band
- **Visual:** full container width, fixed height, `object-fit: cover`, `--radius-main`
- **Selectors:** `.home-staff-photo__image`, `.home-clinic-landscape__image`, `.home-rehabilitation-requirements__photo`
- **Heights (desktop):** 448px, 584px, 388px — scaled down @1024

### Family D — Slider card
- **Reviews:** bordered card in swiper
- **Gallery:** image + caption below (operator correction vs earlier overlay)
- **Specialists:** photo 260px + underlined name

### Family E — Accent lead bar
- **Visual:** 5px left `var(--color-accent)`, uppercase optional
- **Selectors:** `.block-whith-red-line`, `.rehub-universal-decor`, section `__lead` variants

---

## 9. Hero rules (operator-canonical)

| Rule | Value |
|------|-------|
| Modifier | `.hero--home` |
| Max width | 1400px (not 1380 token) |
| Desktop height | `70vh`, max-height cascades 750→670→620→530 |
| Image | Full bleed in `.hero__media`, `object-fit: cover` |
| Panel | Frosted white 25% + blur 5px, padding 30×70px |
| CTA | `.btn.btn_dark.btn--primary.hero__button` |
| Mobile | Height auto, min 320px content, typography scales @930 |

Inner page hero: `.hero--inner` in `hero-inner.html` — fixed 628px desktop (Services planning candidate).

---

## 10. Buttons, icons, images

**Buttons:** `.btn` (outline) | `.btn_dark` (filled primary text color) | `.btn--primary` (accent fill). Height 40px, pill radius, uppercase via CSS.

**Icons:** Font Awesome Pro bridge; accent chevrons in section “all” links; external-link SVG for service rows; messenger SVGs in header.

**Images:** `border-radius: var(--radius-main)` default; founder variant-b uses gradient **mask** (operator calibration); gallery captions **below** image.

**Sliders:** Swiper with shared pagination bullets (10px circle, outline/active fill). Breakpoints in `main.js` — partial slides on mobile (e.g. reviews 1.35).

**Accordion:** Single-open per `[data-accordion]` root; `aria-expanded` + `hidden` on panels; circular accent toggle icon rotates (FAQ) or chevron (treatment).

**Fancybox:** Comfort photos + videos; toolbar infobar + close; scrollbar compensation disabled to match `scrollbar-gutter: stable`.

---

## 11. Operator rules (confirmed active)

```text
All SCSS in src/scss/style.scss (monolithic)
Main JS in src/js/main.js (IIFE modules)
Manual src edits are canonical
No invented design values without evidence (EXACT_GEOMETRY comments mark exceptions)
Buttons: .btn / .btn_dark / .btn--primary
Radii: --radius-main / --radius-full / --radius-input
Uppercase: CSS text-transform on buttons and selected leads
Behavior hooks: data-accordion, data-*-slider, data-fancybox, data-modal-*, data-lead-form, data-offcanvas
```

---

## 12. Drift and exceptions

| Item | Classification |
|------|----------------|
| `--container-hero` unused | DOCUMENTATION_DRIFT / LEGACY token |
| Founder variant-b photo `border-radius: 0` @ f5a9ecd7 | INTENTIONAL_OPERATOR_CALIBRATION (mask edge) |
| `home-why-us` embeds `home-treatment-prevention__*` classes | COMPOSITE_MIXED — cross-section markup reuse |
| `.UNIVERSAL-requirements__support` duplicate selector | EXPERIMENTAL — mirror of support box |
| `.home-recovery-life__stages` horizontal flex without @1024 stack | POSSIBLE_DEFECT or SECTION_EXCEPTION — needs Services planning verification |
| Committed typo «ШШпиговский» in recovery intro H2 @ f5a9ecd7 | POSSIBLE_DEFECT (WIP fixes in working tree) |

---

## 13. Updated FP-0002 style rules summary

### A. Confirmed global rules
- Inter 300 body / 400 headings; 18/24 base
- Container 1230px; desktop gutters 30px; ≤1024 gutters 15px
- Section rhythm 50px via `main > section`
- Accent #B3261E family; page bg blue-gray 70% opacity
- Radius 30px surfaces, 999px pills
- Button system as documented above

### B. Confirmed responsive rules
- Primary split 1024/1025
- Grids collapse to 1 column @1024 unless slider
- Hero becomes content-driven height @1024
- Media band heights scaled @1024

### C. Confirmed component rules
- Outline card family shared visual language
- Section head: H2 + uppercase “all” link with FA play icon
- Lead bar: 5px accent left border
- Slider pagination shared styling
- FAQ/treatment accordion behavior unified in JS

### D. Current exceptions
- Hero geometry SCSS variables ($hero-panel-width etc.)
- Fixed JPG-derived band heights
- Founder variant-b mask compositing
- `no-top-padding*` section stacking on Home

### E. Rules requiring operator approval
- Whether to tokenize repeated 16/20 card body literals
- Whether to extract `.rehub-universal-decor` as formal lead component
- Whether founder variant-b radius WIP should merge to baseline
- Horizontal recovery-life stages on narrow viewports

---

*End of visual baseline v1.*
