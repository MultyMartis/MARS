# O-centre — reuse-first implementation v2

**Status:** `REUSE_FIRST_V2_IMPLEMENTED`  
**Updated:** 2026-06-27  
**Authority:** `o-centre-reuse-first-blueprint-v1.md`  
**Page:** `src/pages/o-centre-v1.html` → `dist/o-centre-v1.html`

## Reuse contract table

| Order | Figma block | Canonical partial | Root class | HTML changes | New CSS | Decision |
| ----: | ----------- | ----------------- | ---------- | -----------: | ------: | -------- |
| 1 | Header | `partials/layout/header.html` | `site-header` | 0 | 0 | EXACT_REUSE |
| 2 | Hero | `partials/sections/services-inner-hero-v2.html` | `services-inner-hero-v2` | 0 | 0 | EXACT_REUSE_WITH_CONTENT |
| 3 | Breadcrumbs | `partials/components/breadcrumbs.html` | `breadcrumbs` | 0 | 0 | EXACT_REUSE_WITH_CONTENT |
| 4 | Anchor nav | `partials/components/services-page-subnav.html` | `services-page-subnav` | 0 | 0 | EXACT_REUSE_WITH_CONTENT |
| 5 | Upper nav wrapper | page assembly (`uslugi-v2` pattern) | `page-uslugi-v2__upper-nav` | 0 | 0 | EXACT_REUSE |
| 6 | «Кто мы» narrative | page composition (`home-recovery-intro__*`) | `home-recovery-intro` | 0* | 0 | COMPOSITION_OF_EXISTING_CLASSES |
| 7 | Expert quote | `partials/sections/home-founder-quote.html` | `home-founder-quote` | 0 | 0 | EXACT_REUSE |
| 8 | «Кого мы лечим» | `partials/sections/services-category-section-v2.html` | `services-category-section-v2` | 0 | 0 | EXACT_REUSE_WITH_CONTENT |
| 9 | CTA встреча | `partials/sections/service-subdivision-first-cta-v1.html` | `service-subdivision-first-cta-v1` | 0 | 0 | EXACT_REUSE |
| 10 | Approach | `partials/sections/service-leaf-approach-v1.html` | `service-leaf-approach-v1` | 0 | 0 | EXACT_REUSE |
| 11 | Program | `partials/sections/services-program-v2.html` | `services-program-v2` | 0 | 0 | EXACT_REUSE_WITH_CONTENT |
| 12 | Landscape | `partials/sections/home-clinic-landscape.html` | `home-clinic-landscape` | 0 | 0 | EXACT_REUSE |
| 13 | Brand typography | `partials/sections/o-centre-brand-typography-v1.html` | `o-centre-brand-typography` | 1 | 1 | GENUINELY_NEW_BLOCK |
| 14 | Home comfort | `partials/sections/home-comfort.html` | `home-comfort` | 0 | 0 | EXACT_REUSE_WITH_CONTENT |
| 15 | Guest CTA | `partials/components/services-program-cta-band-v2.html` in `container` | `services-program-v2__cta-band` | 0 | 0 | EXACT_REUSE_WITH_CONTENT |
| 16 | Specialists | `partials/sections/home-specialists.html` | `home-specialists` | 0 | 0 | EXACT_REUSE_WITH_CONTENT |
| 17 | Reviews | `partials/sections/home-reviews.html` | `home-reviews` | 0 | 0 | EXACT_REUSE_WITH_CONTENT |
| 18 | Final form | `partials/sections/home-final-form.html` | `home-final-form` | 0 | 0 | EXACT_REUSE_WITH_CONTENT |
| 19 | Footer | `partials/layout/footer.html` | `site-footer` | 0 | 0 | EXACT_REUSE |

\*Page file contains composition markup only — no new partial for narrative column.

## Per-block contracts (reused)

### home-founder-quote

- **Partial:** `src/partials/sections/home-founder-quote.html`
- **Root:** `home-founder-quote` (+ `home-founder-quote--variant-b`)
- **Children:** `home-founder-quote__layout`, `__quote`, `__mark`, `__text`, `__figure`, `__photo`, `__author`, `__name`, `__role`, `__cta`
- **Allowed:** `modalSource`, `founderQuoteModifierClass`
- **Forbidden:** eyebrow, about modifier, hide CTA branch, duplicate labels

### home-comfort

- **Partial:** `src/partials/sections/home-comfort.html`
- **Root:** `home-comfort`
- **Children:** `home-comfort__head`, `__heading`, `__all-link`, `__lead`, `__gallery`, `__gallery-item`, `__gallery-item_decor`, `__gallery-image`
- **Allowed:** `sectionId`, `headingId`, `headingText`, `sectionModifierClass`
- **Forbidden:** new gallery namespace; decor tile removal

### services-category-section-v2 (who we treat)

- **Allowed:** heading, intro, lead, bodyHtml, galleryHtml, hideCta, empty servicesHtml
- **Forbidden:** `about-who-we-treat*` namespace; banner slot (not in partial — visual delta registered)

## Content limitations

| Block | Desired | Used | Reason | Future |
| ----- | ------- | ---- | ------ | ------ |
| Approach H2/copy | About-specific | Canonical leaf alcohol copy | `CONTENT_SUBSTITUTION_BLOCKED_BY_EXACT_REUSE` | Data-parameterization pass |
| First CTA copy | About-specific | Canonical subdivision copy | Partial hardcoded | Future param or accept canonical |
| Program intro/lead | About-specific | Lorem (canonical leaf pattern) | Partial supports params — lorem retained from Figma/canonical | Copy pass |
| home-comfort lead | About house lead | Canonical comfort lead | Lead not parameterized in partial | Partial param pass |
| Who-we-treat banner | Large banner image | Absent | Partial has no banner slot | Operator decision / composition |
| Compact CTA desktop-only | Desktop-only wrapper | Always visible container | No confirmed desktop-only wrapper without new CSS | Operator visual review |

## Visual deltas registered

1. Who-we-treat large banner image absent (category partial has gallery grid only).
2. Approach section retains service-leaf alcohol-specific heading/link target.
3. home-comfort lead copy is canonical, not about-house Figma copy.
4. Compact guest CTA not desktop-only (no new wrapper/CSS per reuse rule).

## Forbidden patterns

All rejected namespaces verified absent in source and built output post-build.
