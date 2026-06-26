# FP-0002 — Services General Component Reuse Plan v1

**Planning ID:** `services-general-01`  
**Date:** 2026-06-26  
**Baseline audit:** `audits/home-style-baseline-01/`

---

## Candidate verdicts

| Candidate | Verdict | Notes |
|-----------|---------|-------|
| `hero-inner.html` | **PARAMETERIZE** | Services hero copy + image via include JSON |
| `home-treatment-prevention.html` | **DO_NOT_REUSE** (whole) | Accordion UX wrong; extract list/item/head patterns only |
| `home-rehabilitation-program.html` | **REUSE_DIRECTLY** | Proven on `uslugi.html`; heading param exists |
| `home-founder-quote.html` | **REUSE_DIRECTLY** | Variant A on Services; params `modalSource`, `founderQuoteModifierClass` |
| `home-comfort.html` | **REUSE_DIRECTLY** | Proven |
| `home-faq.html` | **PARAMETERIZE** | Needs heading (+ optional Q/A) params in future pass |
| `home-final-form.html` | **REUSE_DIRECTLY** | `leadSource` param proven |
| `home-feature-grid.html` | **DO_NOT_REUSE** | Not on Services General mock |
| `.rehub-universal-decor` | **ALIAS_WITH_NEW_CLASS** | Use for category hub lead accent if mock shows red-line bar |
| `.home-treatment-prevention__lead` | **COPY_STRUCTURE_NOT_CLASS** | Typography/spacing reference for category intro |
| `.home-treatment-prevention__service-item` | **COPY_STRUCTURE_NOT_CLASS** | Link row pattern inside new hub partial |
| `.home-treatment-prevention__service-list` | **COPY_STRUCTURE_NOT_CLASS** | List container in new hub |
| `.home-feature-grid__card-grid` | **DO_NOT_REUSE** | Program block uses direction cards, not outline cards |
| Section head + all-link | **COPY_STRUCTURE_NOT_CLASS** | From program/comfort/treatment head pattern |
| `.btn` / `.btn_dark` / `.btn--primary` | **REUSE_DIRECTLY** | Global button system |
| `.container` | **REUSE_DIRECTLY** | 1230px max, 30/15 gutters |

---

## Summary buckets

### Exact reuse
- `home-rehabilitation-program.html`
- `home-founder-quote.html` (variant A)
- `home-comfort.html`
- `home-faq.html` *(structure exact; copy parameterized later)*
- `home-final-form.html`
- Header, footer, modal

### Reuse with content
- `hero-inner.html` — title, tagline, image paths, dimensions
- `home-rehabilitation-program.html` — `programHeading` (already parameterized)
- `home-faq.html` — heading text (future param)

### Pattern reuse (new wrappers)
- Category hub block: head + lead + service list + 3-image gallery + CTA
- Optional mid-page CTA band: inner pattern from `.home-rehabilitation-requirements__cta-band`

### Shared layout only
- `.container`, `.btn*`, header/footer/modal, `data-accordion`, `data-lead-form`, `data-modal-open`

### New unique blocks
- Four `services-category-hub` instances (or one parameterized partial invoked 4×)
- Services hero wiring in `uslugi.html` (not a new partial — uses existing `hero-inner`)

### Do-not-reuse
- Whole `home-treatment-prevention` accordion
- Home hero, recovery intro, gallery, reviews, specialists, articles, genotyping, recovery-life

---

## Class strategy

| Proposed class | Type | Based on | Home? | Services? | Risk |
| -------------- | ---- | -------- | ----: | --------: | ---- |
| `.page-uslugi` | page root (existing) | body class | No | Yes | None |
| `.services-category-hub` | new section root | category block mock | No | Yes | Low if scoped |
| `.services-category-hub__head` | element | `.home-treatment-prevention__head` pattern | No | Yes | Low |
| `.services-category-hub__service-item` | element | copy structure from treatment item | No | Yes | Collision if `.home-*` reused — **avoid** |
| `.hero.hero--inner` | existing | `hero-inner.html` | No | Yes | Low |

**Mass rename:** **NOT permitted**  
**Universal classes proposed now:** **NONE** — dual-class only where pattern copied  
**Home `.home-*` retained:** **ALL** on Home unchanged

---

*End of component reuse plan v1.*
