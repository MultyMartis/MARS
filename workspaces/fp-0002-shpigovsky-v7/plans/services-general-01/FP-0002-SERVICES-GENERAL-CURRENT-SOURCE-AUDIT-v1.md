# FP-0002 — Services General Current Source Audit v1

**Planning ID:** `services-general-01`  
**Date:** 2026-06-26  
**Authority:** operator-canonical source @ post-reconciliation working tree  
**Page:** `src/pages/uslugi.html`  
**Body class:** `page-uslugi` (`data-page="uslugi"`)

---

## Page shell

| Element | Include | Root / hook | Notes |
|---------|---------|-------------|-------|
| `<head>` | `partials/layout/head.html` | — | TEMPORARY_SEO_COPY placeholders |
| Header | `partials/layout/header.html` | `.site-header` | Active nav wired: `activeNavUslugiClass`, offcanvas |
| Footer | `partials/layout/footer.html` | `.site-footer` | Shared |
| Modal | `partials/components/modal-consultation.html` | `[data-modal-open]` | Shared |
| Scripts | vendor Swiper, Fancybox, Inputmask + `assets/js/main.js` | `data-*` hooks | Same stack as Home |

---

## Main content order (current)

| Order | Current include | Root class | Current content / role | Planned action |
| ----: | --------------- | ---------- | ---------------------- | -------------- |
| — | *(absent)* | — | No inner hero | **Add** `hero-inner.html` at top |
| 1 | `home-rehabilitation-program.html` | `.home-rehabilitation-program` | 4 program directions; param `programHeading` | **Reposition** — after service category blocks |
| 2 | `home-founder-quote.html` | `.home-founder-quote` | Founder quote variant A; `modalSource=services-founder` | **Keep** — order matches mock mid-page |
| 3 | `home-comfort.html` | `.home-comfort` | Comfort gallery + Fancybox | **Keep** |
| 4 | `home-faq.html` | `.home-faq` | Accordion FAQ (temporary lorem answers) | **Keep** — heading/content swap TBD |
| 5 | `home-final-form.html` | `.home-final-form` | Lead form; `leadSource=services-final` | **Keep** |

---

## Missing vs design (confirmed gap)

| Expected block (PNG / Figma `Услуги хаб`) | Current source | Status |
|-------------------------------------------|----------------|--------|
| Inner hero «Лечение и профилактика» | Not included | **Missing** |
| Service category hub blocks (×4) | Not included | **Missing** |
| `home-treatment-prevention` accordion | Not on `uslugi.html` (exists on Home only) | **Not wired** — mock uses expanded category sections, not Home accordion |

---

## Shared layout already correct

- Header active state for `/uslugi/` — wired.
- No Home-only sections erroneously included (recovery intro, gallery, reviews, etc.).
- No unique Services-only partials in repo yet.

---

## Regression boundary

Current stub does **not** render target mock order. Implementation must **replace page assembly** without editing Home-only partial internals unless parameterized content is explicitly required.

---

*End of current source audit v1.*
