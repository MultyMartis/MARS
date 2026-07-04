# FP-0002 V9-06D.6 V9 Static Inventory v1

**Date:** 2026-07-04
**Phase:** V9-06D.6 (planning rerun)
**Workspace:** `workspaces/fp-0002-shpigovsky-v9/`

## Build

- Gulp + gulp-file-include
- SCSS entry: `src/scss/style.scss` (+ Font Awesome vendor CSS)
- JS entry: `src/js/main.js`
- Page scripts: Swiper, Fancybox, Inputmask CDN, `main.js`
- Dist asset paths: root-relative `/assets/...`
- Dist readability in agent: SAFE UNKNOWN (cursorignore)

## Pages

- Total page files: 33
- Full/template pages: home, uslugi, usluga-podrazdel-v1, usluga-konechnaya-v1, kontakty, otzyvy, o-centre, blog (+ article), uslugi-v2 alternate
- Placeholders: psych/RPP parents and children, genotyping, several o-centre leaves, etc.
- Legal demo: 4 documents

## First-wave sources

| Route | V9 file |
|---|---|
| `/` | `src/pages/index.html` |
| `/uslugi/` | `src/pages/uslugi.html` |
| `/uslugi/zavisimosti/` | `src/pages/usluga-podrazdel-v1.html` (template) |
| Alcohol child | `src/pages/usluga-konechnaya-v1.html` |
| Psych / RPP parents | placeholder pages under `src/pages/uslugi/` |
| `/kontakty/` | `src/pages/kontakty.html` |

## Shared

Header, footer, global consultation modal, breadcrumbs, internal page nav, program CTA band, scroll-to-top.

## Result

COMPLETE — planning inventory only.
