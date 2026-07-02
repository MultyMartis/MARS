# FP-0002 V9-04 Component-to-Template-Part Map v1

**Date:** 2026-07-02

| ID | V9 partial | WP target | Static/Dynamic | JS | Acceptance |
|----|------------|-----------|----------------|-----|------------|
| CMP-HEAD | `layout/head.html` | `template-parts/layout/head.php` | static structure | — | meta parity |
| CMP-HEADER | `layout/header.html` | `template-parts/layout/header.php` | menus dynamic | offcanvas | active states |
| CMP-FOOTER | `layout/footer.html` | `template-parts/layout/footer.php` | mixed | — | legal links |
| CMP-MODAL | `layout/global-consultation-modal.html` | `template-parts/layout/global-consultation-modal.php` | mixed | Triumph runtime | one per page, no scroll jump |
| CMP-SCROLL-TOP | `components/scroll-to-top.html` | `template-parts/components/scroll-to-top.php` | static | threshold 500 | z-index 900 |
| CMP-BREADCRUMBS | per-template | `template-parts/components/breadcrumbs.php` | dynamic | — | label parity |
| CMP-REVIEW-CARD | `components/review-archive-card.html` | `template-parts/components/review-archive-card.php` | dynamic | — | repeater render |
| CMP-BLOG-CARD | `components/blog-archive-card.html` | `template-parts/components/blog-archive-card.php` | dynamic | — | featured image |
| CMP-LEGAL-WRAPPER | `sections/legal-document-page.html` | `template-parts/sections/legal-document-page.php` | mixed | — | DEMO banner |
| CMP-INFRA-NARRATIVE | `sections/infrastructure-narrative.html` | `template-parts/sections/infrastructure-narrative.php` | mixed | accordion | **G6 absent** |

## Section partials (page-specific)

Map `src/partials/sections/*.html` to `template-parts/sections/` preserving BEM classes. Home-only sections load only on `front-page.php`. Service sections load per template family.

## Excluded components

- `home-genotyping.html` — unpublished route; do not emit in WP theme
- Preloader partials — none active
- O-Centre G6 blocks — must not be recreated
