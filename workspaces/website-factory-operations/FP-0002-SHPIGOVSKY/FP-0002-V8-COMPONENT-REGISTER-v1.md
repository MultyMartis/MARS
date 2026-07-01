# FP-0002 V8 — Component Register v1

**Date:** 2026-07-01  
**Baseline:** `eb47ebb` · `workspaces/fp-0002-shpigovsky-v8/`

**Rule:** Visual similarity alone does not make two blocks the same shared component.

---

## Layout (shared)

| Name | Path | Type | Consumers | WP mapping |
|------|------|------|-----------|------------|
| head | `partials/layout/head.html` | shared | All pages | Theme `header.php` meta partial |
| header | `partials/layout/header.html` | shared | All pages | Theme header; menu-driven |
| footer | `partials/layout/footer.html` | shared | All pages | Theme footer |

**Header:** Desktop nav + mobile offcanvas (`data-offcanvas`). Active states via include JSON params (`activeNavBlogClass`, etc.).

---

## Global components (shared)

| Name | Path | Type | Consumers | Desktop/mobile | Notes |
|------|------|------|-----------|----------------|-------|
| breadcrumbs | `components/breadcrumbs.html` | shared | Inner pages | One DOM | Up to 3 crumbs via params |
| modal-consultation | `components/modal-consultation.html` | shared | Most pages | One DOM | `data-modal` hooks |
| program-cta-band | `components/program-cta-band.html` | shared | Services, blog article, others | One DOM | Parametric heading/phone/source |
| internal-page-nav | `components/internal-page-nav.html` | shared | Service pages | One DOM | Breadcrumbs + subnav + optional CTA |
| services-page-subnav | `components/services-page-subnav.html` | family-shared | Service v2 family | One DOM | Anchor list HTML param |
| services-program-v2-item | `components/services-program-v2-item.html` | family-shared | `services-program-v2` | One DOM | Repeated program row |
| comfort-gallery | `components/comfort-gallery.html` | shared | comfort section | One DOM | Swiper |
| comfort-gallery-decor | `components/comfort-gallery-decor.html` | shared | comfort section | One DOM | Decorative layer |

---

## Button system (content element)

| Element | Classes | Type | Rule |
|---------|---------|------|------|
| Base button | `.btn` | shared | Single base system |
| Dark CTA | `.btn_dark` | modifier | Approved combination |
| Primary emphasis | `.btn--primary` | modifier | Often with `.btn_dark` |
| Approved combo | `.btn.btn_dark.btn--primary` | modifier stack | Do not invent parallel systems |

No `--button-letter-spacing` token in V8.

---

## Founder quote

| Name | Path | Type | Consumers | WP |
|------|------|------|-----------|-----|
| founder-quote (section) | `sections/founder-quote.html` | shared | Home, others | Template block + ACF optional |
| blog-article-founder-quote | `components/blog-article-founder-quote.html` | page-owned variant | Blog article only | Article meta + author profile |

**Exception:** Blog uses `founder-quote--variant-b` anatomy; related cards differ from archive cards — not merged.

---

## Cards

| Name | Path | Type | Consumers | WP |
|------|------|------|-----------|-----|
| blog-archive-card | `components/blog-archive-card.html` | family-shared | blog archive, home-articles | Query loop item |
| blog-related-card | `components/blog-related-card.html` | page-owned | Blog article related grid | Related posts query |
| review-archive-card | `components/review-archive-card.html` | family-shared | reviews archive | Query loop item |
| blog-article-author-card | `components/blog-article-author-card.html` | page-owned | Available; article uses inline author meta | Author profile |

---

## Blog article blocks

| Name | Path | Type | WP ownership |
|------|------|------|--------------|
| blog-article-content | `sections/blog-article-content.html` | page-owned | Hero + body stream shell |
| blog-article-lower-stack | `sections/blog-article-lower-stack.html` | page-owned | Conclusion, sources, related, CTA wrapper |
| TOC | Inside hero | content element | Auto from H2 in `the_content()` |
| excerpt block | `.blog-article-hero__excerpt` | content element | Post excerpt field — not body |
| article body | `.blog-article-body__content` | content element | Single `the_content()` stream |
| inline images | `<figure><img>` in body | content element | Editor content |
| sources | `blog-article-sources` | template-managed | Custom field / repeater |
| related grid | `blog-article-related` | template-managed | Query-driven |

---

## Blog archive blocks

| Name | Path | Type | Notes |
|------|------|------|-------|
| blog-archive-list | `sections/blog-archive-list.html` | page-owned | Card grid |
| blog-lower-stack | `sections/blog-lower-stack.html` | page-owned | Expert quote + CTA below archive |
| blog-expert-quote | `sections/blog-expert-quote.html` | family-shared | Distinct from founder quote |

---

## Home sections (page-owned composition)

| Section | Path | Shared? |
|---------|------|---------|
| hero | `sections/hero.html` | Home-owned |
| home-recovery-intro | `sections/home-recovery-intro.html` | Home-owned |
| home-treatment-prevention | `sections/home-treatment-prevention.html` | Home-owned |
| home-gallery | `sections/home-gallery.html` | Home-owned |
| home-why-us | `sections/home-why-us.html` | Home-owned |
| home-articles | `sections/home-articles.html` | Home-owned; reuses card anatomy |
| home-videos | `sections/home-videos.html` | Home-owned |
| clinic-landscape | `sections/clinic-landscape.html` | Reused on home + service leaf |

---

## Service family sections

| Section | Path | Template |
|---------|------|----------|
| services-inner-hero-v2 | `sections/services-inner-hero-v2.html` | v2 family |
| services-category-section-v2 | `sections/services-category-section-v2.html` | Hub v2 |
| services-category-hub | `sections/services-category-hub.html` | Legacy hub |
| service-subdivision-*-v1 | `sections/service-subdivision-*-v1.html` | Subdivision |
| service-leaf-*-v1 | `sections/service-leaf-*-v1.html` | Leaf |

**Safe reuse:** Use parametric includes within same family.  
**Prohibited:** Changing shared header/footer/CTA to satisfy one page without operator approval.

---

## Accordions

Implemented in `faq.html` and similar via `data-accordion` in `main.js`. One-open behavior per group; accessible `aria-expanded`.

---

## Forms

| Name | Path | Functional |
|------|------|------------|
| final-form | `sections/final-form.html` | Visual only |
| contacts sections | `contacts-map-body.html`, etc. | Visual / static map |

---

## Content element: red-line block

| Class | Purpose | Exception |
|-------|---------|-----------|
| `.block-whith-red-line` | Red accent bar blocks | **Misspelling retained** — do not rename silently |

---

*Component register — V8 approved baseline.*
