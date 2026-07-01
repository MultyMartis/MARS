# FP-0002 V8 — Implementation Guide v1

**Document type:** Developer onboarding — approved V8 frontend  
**Date:** 2026-07-01  
**Baseline:** [FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01.md](FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01.md)  
**Commit:** `eb47ebb4066252373e02d9e1095403d0ce6b6b22`  
**Tag:** `fp-0002-v8-operator-approved-frontend-stable-01`

---

## 1. Project identity

| Field | Value |
|-------|-------|
| Factory project | FP-0002 — Shpigovsky.ru |
| Workspace | `X:\AI MARS\workspaces\fp-0002-shpigovsky-v8\` |
| Stack | Gulp 4 + gulp-file-include + single SCSS + vanilla JS |
| Production domain (target) | `https://shpigovsky.ru/` |
| Visual protocol | [FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md](FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md) |

---

## 2. Build and preview

```bash
cd workspaces/fp-0002-shpigovsky-v8
npm ci
npm run build
```

| Command | Purpose |
|---------|---------|
| `npm run build` | **Canonical** — `cleanDist` + full pipeline |
| `npm run watch` | Local dev with rebuild |
| `npm run watch:dev` | Watch without full clean |

**Output:** `dist/` — generated artifact; never hand-edit.

**Recovery pack:** `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\FP-0002-V8-OPERATOR-APPROVED-FRONTEND-STABLE-01\`

---

## 3. Source structure

```text
src/
├── pages/           # 10 HTML entry points (Gulp pages glob)
├── partials/
│   ├── layout/      # head, header, footer
│   ├── sections/    # Page blocks
│   └── components/  # Reusable UI fragments
├── scss/
│   └── style.scss   # ALL styles — single file (no partial architecture)
├── js/
│   └── main.js      # Init: offcanvas, accordions, modals, sliders, masks
├── img/             # Raster assets → dist/assets/img/
├── svg/             # SVG → dist/assets/svg/
├── fonts/           # WOFF2 → dist/assets/fonts/
└── favicon/
```

**Font Awesome:** bridged from `shared/assets/icon-libraries/Font Awesome Pro 5.15.4` via `src/scss/vendors/fa-all.css`.

**Vendors (CDN + local):** Swiper, Fancybox (bundled to `dist/assets/vendor/`); Inputmask via jsDelivr CDN on pages.

---

## 4. Page shell model

Every page follows:

1. `partials/layout/head.html` — meta, OG, favicon, CSS
2. `partials/layout/header.html` — nav + offcanvas (active state via include params)
3. `<main>` — page sections
4. `partials/layout/footer.html`
5. `partials/components/modal-consultation.html` (most pages)
6. Deferred scripts: Swiper, Fancybox, Inputmask, `main.js`

Nested pages (e.g. blog article) set `<base href="../">` for asset resolution.

---

## 5. Routing

Gulp mirrors `src/pages/**/*.html` → `dist/` preserving paths.

| Source | Dist output | Notes |
|--------|-------------|-------|
| `src/pages/index.html` | `dist/index.html` | Home |
| `src/pages/blog.html` | `dist/blog.html` | Flat filename; canonical URL `/blog/` |
| `src/pages/blog/nazvanie-stati.html` | `dist/blog/nazvanie-stati.html` | Article fixture |

**Canonical URLs** are set in `head.html` params (`canonical`, `ogUrl`); static filenames may differ from production permalinks until WordPress or demo assembly.

---

## 6. Composition model

- **Sections** (`partials/sections/`) — large page blocks; may accept JSON include params.
- **Components** (`partials/components/`) — smaller reusable fragments.
- **Include syntax:** `@@include('partials/...', {"key": "value"})` — JSON on one line.

Page-owned sections exist where CMS ownership or visual anatomy differs (e.g. `service-leaf-*-v1.html` vs `services-*-v2.html`).

---

## 7. SCSS architecture (V8 exception)

**All production styles live in one file:** `src/scss/style.scss`.

- No `@import` partial tree for production (V8 consolidation decision).
- Canonical radius token: `--radius-main: 30px` on `:root`.
- No `--radius-small`, `--radius-medium`, `--radius-large` in V8.
- Breakpoint policy: desktop `min-width: 1025px`; mobile/tablet `max-width: 1024px`.

See [FP-0002-V8-FRONTEND-RULES-AND-EXCEPTIONS-v1.md](FP-0002-V8-FRONTEND-RULES-AND-EXCEPTIONS-v1.md).

---

## 8. JavaScript architecture

Single bundle: `src/js/main.js` (IIFE modules inlined).

| Feature | Hook pattern |
|---------|--------------|
| Offcanvas menu | `data-offcanvas`, `data-offcanvas-open`, `data-offcanvas-close` |
| Accordions | `data-accordion`, `data-accordion-button`, `data-accordion-panel` |
| Modal consultation | `data-modal`, `data-modal-open`, `data-modal-close` |
| Phone mask | `data-mask` |
| Swiper galleries | `data-slider` |
| Fancybox | `data-fancybox` |

Desktop offcanvas disabled at `1025px+`.

---

## 9. Desktop / mobile model

- **One semantic DOM** per page — no duplicate mobile markup.
- Mobile layout via SCSS (`max-width: 1024px`) and safe reordering (flex/grid `order`).
- Blog Article mobile hero order: image → H1 → meta → TOC → excerpt (documented in blog architecture).

---

## 10. Implemented pages (10)

See [FP-0002-V8-PAGE-AND-ROUTE-REGISTER-v1.md](FP-0002-V8-PAGE-AND-ROUTE-REGISTER-v1.md).

---

## 11. Shared vs page-owned components

See [FP-0002-V8-COMPONENT-REGISTER-v1.md](FP-0002-V8-COMPONENT-REGISTER-v1.md).

**Globally shared:** header, footer, breadcrumbs, modal, program CTA band, founder quote (with modifiers), FAQ, comfort, specialists, reviews carousel, etc.

**Family-shared:** services v2 blocks, service leaf/subdivision blocks, blog archive/article families.

**Rule:** Visual similarity ≠ automatic component merge.

---

## 12. Forms and modal

- `final-form.html` — home bottom lead form (visual only; no backend).
- `modal-consultation.html` — site-wide consultation modal; opened via `data-modal-open`.
- Forms use Inputmask for phone fields when `data-mask` present.

---

## 13. Blog

See [FP-0002-V8-BLOG-ARCHITECTURE-v1.md](FP-0002-V8-BLOG-ARCHITECTURE-v1.md).

---

## 14. Known project exceptions

- Class `.block-whith-red-line` — intentional misspelling retained for compatibility.
- Services hub (`uslugi.html`) vs v2 (`uslugi-v2.html`) — both exist; v2 is canonical template for new service work.
- Some service leaf content uses placeholder Lorem ipsum in program block.
- `robots: noindex, nofollow` on most non-home pages (demo posture).

---

## 15. Deferred phases

| Phase | Scope |
|-------|-------|
| **07C** | Excel-driven static client demo assembly |
| **Later** | Operator manual polish (spacing, copy, images) |
| **Later** | Animation and interaction polish |
| **Later** | Forge WordPress integration |

---

## 16. Related documents

- [FP-0002-V8-FRONTEND-RULES-AND-EXCEPTIONS-v1.md](FP-0002-V8-FRONTEND-RULES-AND-EXCEPTIONS-v1.md)
- [FP-0002-V8-FORGE-WORDPRESS-HANDOFF-MAP-v1.md](FP-0002-V8-FORGE-WORDPRESS-HANDOFF-MAP-v1.md)
- [FP-0002-V8-KNOWN-LIMITATIONS-AND-DEFERRED-WORK-v1.md](FP-0002-V8-KNOWN-LIMITATIONS-AND-DEFERRED-WORK-v1.md)
- [FP-0002-V8-OPERATOR-POLISH-BOUNDARY-v1.md](FP-0002-V8-OPERATOR-POLISH-BOUNDARY-v1.md)

---

*FP-0002 V8 implementation guide — operator-approved baseline.*
