# O-centre — visual donor map v3

**Status:** COMPLETE  
**Updated:** 2026-06-28  
**Page:** `src/pages/o-centre-v1.html`  
**Authority:** FP-0002 operator rebuild v3 brief

## Block-to-donor map

| Order | O-CENTRE block | Visual donor page | Exact donor partial/block | Reuse mode | New CSS |
| ----: | -------------- | ----------------- | ------------------------- | ---------- | ------: |
| 01 | Header + hero + breadcrumbs + subnav | `uslugi-v2.html` | `services-inner-hero-v2` + `page-uslugi-v2__upper-nav` + `breadcrumbs` + `services-page-subnav` | EXACT_REUSE_WITH_CONTENT | 0 |
| 02 | «Шпиговский дом — место, где видят человека…» | `usluga-konechnaya-v1.html` | `service-leaf-intro-v1` + `service-subdivision-nature-v1__text` body | COMPOSITION_FROM_EXISTING | 0 |
| 03 | Founder quote | `index.html` | `home-founder-quote` | EXACT_REUSE_WITH_CONTENT | 0 |
| 04 | «Разные люди, разные истории» | `uslugi-v2.html` | `services-category-section-v2` (text + `galleryHtml` three-image row) | EXACT_REUSE_WITH_CONTENT | 0 |
| 05 | Dark CTA band #1 | `usluga-podrazdel-v1.html` | `service-subdivision-first-cta-v1` | EXACT_REUSE | 0 |
| 06 | «Наш подход к лечению» | `usluga-konechnaya-v1.html` | `service-leaf-approach-v1` | EXACT_REUSE | 0 |
| 07 | Exterior / landscape | `index.html` / service pages | `home-clinic-landscape` | EXACT_REUSE | 0 |
| 08 | «Наша программа включает 4 направления» | `uslugi-v2.html` | `services-program-v2` | EXACT_REUSE_WITH_CONTENT | 0 |
| 09 | «Место, где лечение начинается с ощущения безопасности» | `index.html` | `home-comfort` gallery bricks (inline composition) | COMPOSITION_FROM_EXISTING | 0 |
| 10 | Dark CTA band #2 | `uslugi-v2.html` | `services-program-cta-band-v2` in `container` | EXACT_REUSE_WITH_CONTENT | 0 |
| 11 | Specialists | `index.html` | `home-specialists` | EXACT_REUSE_WITH_CONTENT | 0 |
| 12 | Reviews | `index.html` | `home-reviews` | EXACT_REUSE_WITH_CONTENT | 0 |
| 13 | Final form | `index.html` | `home-final-form` | EXACT_REUSE_WITH_CONTENT | 0 |
| 14 | Footer | canonical | `footer.html` | EXACT_REUSE | 0 |

## Per-block contracts

### Block 01 — upper shell

- **Source page:** `src/pages/uslugi-v2.html`
- **Root classes:** `page-uslugi-v2`, `page-uslugi-v2__main`, `page-uslugi-v2__upper-nav`
- **Hero root:** `services-inner-hero-v2`
- **Subnav root:** `services-page-subnav`
- **Allowed:** hero image/title/lead/CTA, breadcrumbs, anchor labels/targets
- **Forbidden:** `page-o-centre-v1__upper-nav`, new wrapper, new CSS

### Block 02 — first text

- **Donor structure:** `service-leaf-intro-v1` (`service-leaf-intro-v1__heading`, `service-leaf-intro-v1__lead block-whith-red-line`)
- **Body donor class:** `service-subdivision-nature-v1__text` (from `service-subdivision-nature-v1.html`)
- **Allowed:** heading, red-line lead, paragraph copy, anchor id `about-who-we-are`
- **Forbidden:** `home-recovery-intro`, `about-narrative*`, new root namespace

### Block 03 — founder quote

- **Partial:** `partials/sections/home-founder-quote.html`
- **Root:** `home-founder-quote`, `home-founder-quote--variant-b`
- **Allowed:** `modalSource`, `founderQuoteModifierClass`
- **Forbidden:** eyebrow, about branch, partial/CSS changes

### Block 04 — who we treat

- **Partial:** `partials/sections/services-category-section-v2.html`
- **Root:** `services-category-section-v2`
- **Gallery:** `services-category-section-v2__gallery` + `__gallery-item` + `__gallery-image` (three-image row from `uslugi-v2` addictions section)
- **Allowed:** heading, intro, lead, bodyHtml, galleryHtml, hideCta, empty servicesHtml
- **Forbidden:** `about-who-we-treat*`, new grid/CSS

### Block 05 — dark CTA

- **Partial:** `partials/sections/service-subdivision-first-cta-v1.html`
- **Root:** `service-subdivision-first-cta-v1` → `services-program-v2__cta-band`
- **Allowed:** none (hardcoded canonical copy)
- **Forbidden:** new CTA variant/CSS

### Block 06 — approach

- **Partial:** `partials/sections/service-leaf-approach-v1.html`
- **Root:** `service-leaf-approach-v1`
- **Limitation:** `CONTENT_SUBSTITUTION_BLOCKED` — canonical alcohol-specific heading/copy retained

### Block 07 — landscape

- **Partial:** `partials/sections/home-clinic-landscape.html`
- **Root:** `home-clinic-landscape`

### Block 08 — program

- **Partial:** `partials/sections/services-program-v2.html`
- **Root:** `services-program-v2`
- **Limitation:** intro/lead lorem retained where partial params used; `hideCtaBand: true`

### Block 09 — media / house

- **Composition roots:** `home-comfort`, `home-comfort__head`, `home-comfort__heading`, `home-comfort__lead`, `home-comfort__gallery`, `home-comfort__gallery-item`, `home-comfort__gallery-item_decor`, `home-comfort__gallery-item--wide`, `home-comfort__gallery-image`
- **Fancybox:** `data-fancybox="home-comfort"` (canonical hook)
- **Allowed:** section/heading ids, heading text, lead text, asset paths in page assembly only
- **Forbidden:** whole `@@include('home-comfort.html')`, `about-house*`, `o-centre-brand-typography`, new gallery namespace/CSS
- **Note:** decor tile position follows canonical `home-comfort` gallery order; Figma-specific reorder requires operator decision

### Block 10 — second CTA

- **Component:** `partials/components/services-program-cta-band-v2.html` in `container` (same as `uslugi-v2.html` secondary CTA)

## Asset decisions

| Figma asset | Runtime asset | Match | Action |
| ----------- | ------------- | ----- | ------ |
| Hero exterior | `assets/img/content/services/services-hero.webp` | canonical uslugi-v2 | EXACT_REUSE |
| Who-we-treat row | `services-addictions-01/02/03.webp` | canonical uslugi-v2 gallery | EXACT_REUSE |
| Approach team | `shpigovsky-staff-group.webp` | canonical approach partial | EXACT_REUSE |
| Landscape | `home-clinic-landscape` partial assets | canonical | EXACT_REUSE |
| Program cards | rehabilitation-program/*.webp | canonical | EXACT_REUSE |
| House gallery | `home-comfort/*.webp` + `logo.svg` decor | canonical home-comfort | EXACT_REUSE |

## Registered limitations

1. **Block 06** — approach heading/copy: `CONTENT_SUBSTITUTION_BLOCKED`
2. **Block 05** — first CTA copy: canonical subdivision partial hardcoded
3. **Block 09** — `home-comfort__lead` not parameterized in partial; inline composition uses canonical lead unless operator supplies copy pass
4. **Block 09** — gallery order follows canonical `home-comfort` brick layout; Figma-specific tile order delta registered for operator review
