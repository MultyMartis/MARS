# FP-0002 — Home Component Reuse Map v1

**Audit ID:** `home-style-baseline-01`  
**Authority:** `f5a9ecd7`  
**Date:** 2026-06-26

---

## Classification key

| Status | Meaning |
|--------|---------|
| HOME_ONLY | Not recommended whole on other pages |
| REUSABLE_AS_IS | Include partial unchanged; swap copy/params only |
| REUSABLE_WITH_CONTENT | Same structure; content via include JSON |
| REUSABLE_PATTERN_REQUIRES_EXTRACTION | Section-specific root; inner pattern universal |
| COMPOSITE_MIXED | Multiple reuse statuses inside one section |

---

## Root section classification

| Root selector | Section | Status | Evidence | Potential pages | Risk |
| ------------- | ------- | ------ | -------- | --------------- | ---- |
| `.hero.hero--home` | Hero | HOME_ONLY | Home H1, tagline, hero-main.png, 70vh geometry | Home only | High if copied — use `.hero--inner` for inner pages |
| `.home-recovery-intro` | Recovery intro | HOME_ONLY | Brand narrative + 6 value cards unique to Home story | Home | Medium — card grid pattern extractable |
| `.home-founder-quote` | Founder quote | REUSABLE_WITH_CONTENT | Already on `uslugi.html`; params: `modalSource`, `founderQuoteModifierClass` | Services, About, Landing | Low — variant-b Home-specific |
| `.home-treatment-prevention` | Treatment accordion | REUSABLE_WITH_CONTENT | Accordion + service links; content-heavy | Services hub, category pages | Medium — home-specific headings |
| `.home-gallery` | Gallery slider | REUSABLE_WITH_CONTENT | Swiper + captions; needs gallery assets | About, Results | Medium — JS + assets coupling |
| `.home-why-us` | Why us | COMPOSITE_MIXED | Reuses treatment `__service-list` inside; home copy | Home primarily | High cross-namespace coupling |
| `.home-staff-photo` | Staff band | REUSABLE_WITH_CONTENT | Single bleed image pattern | About, Team | Low |
| `.home-feature-grid` | Feature grid | REUSABLE_PATTERN_REQUIRES_EXTRACTION | 3-col outline cards — generic visually | Services, About | Low extraction risk |
| `.home-clinic-landscape` | Landscape band | REUSABLE_WITH_CONTENT | Bleed image only | About, Services | Low |
| `.home-recovery-life` | Recovery life stages | HOME_ONLY | Home program narrative + bg + 3 stages | Home | Medium — stage flex layout niche |
| `.home-reviews` | Reviews slider | REUSABLE_WITH_CONTENT | Swiper cards; already standard pattern | Home, Services footer | Low |
| `.home-rehabilitation-requirements` | Requirements | REUSABLE_WITH_CONTENT | Steps + dark CTA + support + photo | Services intake pages | Medium — long section |
| `.home-rehabilitation-program` | Program directions | **REUSABLE_AS_IS** | **Live on `uslugi.html`**; param `programHeading` | Services (active) | **Proven** |
| `.home-genotyping` | Genotyping | REUSABLE_WITH_CONTENT | Lead + list + CTA | Services specialty | Low |
| `.home-comfort` | Comfort gallery | **REUSABLE_AS_IS** | **Live on `uslugi.html`**; Fancybox grid | Services (active) | **Proven** |
| `.home-videos` | Videos | REUSABLE_WITH_CONTENT | 2-col video + Fancybox | Media, About | Low |
| `.home-specialists` | Specialists | REUSABLE_WITH_CONTENT | Swiper team cards | About, Services | Low |
| `.home-articles` | Articles | REUSABLE_WITH_CONTENT | 3-col blog grid | Home, Blog index | Low |
| `.home-faq` | FAQ | **REUSABLE_AS_IS** | **Live on `uslugi.html`** | Services (active) | **Proven** |
| `.home-final-form` | Final form | **REUSABLE_AS_IS** | **Live on `uslugi.html`**; param `leadSource` | Site-wide footer CTA | **Proven** |

**Note:** Task list referenced `.final-form` — **no such root class exists**. Canonical root is `.home-final-form`.

---

## Proven cross-page reuse (existing)

`src/pages/uslugi.html` @ `f5a9ecd7` already includes:

1. `home-rehabilitation-program.html`
2. `home-founder-quote.html` (variant A default — no `--variant-b`)
3. `home-comfort.html`
4. `home-faq.html`
5. `home-final-form.html`

Plus shared layout: header, footer, modal, vendor scripts.

**Conclusion:** `.home-*` naming is **historical**, not a hard home scope boundary — five blocks already serve Services.

---

## Universalization strategy by candidate

| Candidate | Recommended strategy | Notes |
|-----------|---------------------|-------|
| Program, comfort, FAQ, final form | **D — Keep page-specific class names** | Already reused via includes; rename deferred |
| Founder quote | **B — Shared partial with parameters** | Active pattern |
| Section head (H2 + all link) | **C — Shared internal pattern** | Alias `.section-head` later if needed |
| Outline card grid | **C — Shared internal pattern** | Strategy A alias optional |
| Dark CTA band | **C — Shared internal pattern** | Two instances share visual system |
| Lead accent bar | **A — Modifier/alias** | `.rehub-universal-decor` already started |
| Hero | **D — Keep page-specific** | Use `hero-inner.html` for non-home |
| Treatment accordion | **B — Shared partial** | Parameterize categories |
| Slider sections | **B — Shared partial** | Pass slider data-* id + breakpoints |

**Not recommended now:** mass rename `.home-*` → global; global search/replace; delete legacy classes.

---

## Safe extraction order (for Services General planning)

1. **Document** — reuse map (this file) ✓  
2. **Inner hero** — `hero-inner.html` for Services page top  
3. **Lead bar** — formalize `.rehub-universal-decor` usage in new sections  
4. **Section head pattern** — copy existing head markup before abstracting  
5. **Outline card grid** — only if Services mock shows 3-col cards matching feature-grid  
6. **Treatment accordion** — if Services hub needs category list (high confidence from mock)  
7. **Optional sliders** — reviews/specialists if mock includes carousels  
8. **Rename pass** — only after Services page stable (operator gate)

---

## Home-only (do not port whole)

- `.hero.hero--home`
- `.home-recovery-intro` (whole section)
- `.home-recovery-life` (whole section)
- `.home-why-us` (whole — prefer refactor of embedded list first)
- `.home-staff-photo` / `.home-clinic-landscape` as Home sequence (optional elsewhere with new copy)

---

## Classes not to rename (stability)

All existing `.home-*` roots and BEM elements on Home and `uslugi.html`; `.hero*`, `.btn*`, `.container`, `.site-header*`, `.site-footer*`, `.modal-consultation*`, `.rehub-universal-decor`, `.block-whith-red-line`.

---

*End of component reuse map v1.*
