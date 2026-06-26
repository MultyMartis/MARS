# FP-0002 — Services General Design-to-Source Map v1

**Planning ID:** `services-general-01`  
**Date:** 2026-06-26

---

## Classification key

| Type | Meaning |
|------|---------|
| EXACT_REUSE | Include partial unchanged |
| REUSE_WITH_CONTENT | Include + JSON params / copy swap |
| REUSE_PATTERN_WITH_NEW_WRAPPER | New section root; inner markup/CSS patterns copied |
| NEW_UNIQUE_BLOCK | New composition per mock |
| SHARED_LAYOUT_ONLY | Header/footer/modal/container/btn |
| SAFE_UNKNOWN | Insufficient evidence |

---

## Map

| Target section | Classification | Existing candidate | Required adaptation | Home regression risk |
| -------------- | -------------- | ------------------ | ------------------- | -------------------- |
| Header | SHARED_LAYOUT_ONLY | `layout/header.html` | Active nav params (already wired) | None |
| Inner hero | REUSE_WITH_CONTENT | `hero-inner.html` / `.hero--inner` | New hero image, tagline, title, CTA params; include in `uslugi.html` | Low — Home uses `.hero--home` only |
| Category hub ×4 | REUSE_PATTERN_WITH_NEW_WRAPPER | `.home-treatment-prevention__*` patterns | **New** partial(s) e.g. `services-category-hub.html`; expanded layout + 3-image gallery; not accordion | Low if scoped under `.page-uslugi` or new `.services-*` root |
| Program directions | REUSE_WITH_CONTENT | `home-rehabilitation-program.html` | `programHeading` + optional lead copy param; reposition in page | Low — already on `uslugi.html` |
| Founder quote | REUSE_WITH_CONTENT | `home-founder-quote.html` | Keep variant A (`founderQuoteModifierClass=""`); `modalSource=services-founder` | Low — variant-b stays Home-only |
| Comfort gallery | EXACT_REUSE | `home-comfort.html` | None for Pass 1 | None — proven |
| Mid CTA band | SAFE_UNKNOWN | `.home-rehabilitation-requirements__cta-band` pattern | Confirm presence/order vs PNG; may omit Pass 1 if ambiguous | Medium if requirements partial pulled whole |
| FAQ | REUSE_WITH_CONTENT | `home-faq.html` | Heading text swap; replace lorem answers when content ready | Low |
| Final form | REUSE_WITH_CONTENT | `home-final-form.html` | `leadSource=services-final` (already set) | None — proven |
| Footer / modal | SHARED_LAYOUT_ONLY | `footer.html`, `modal-consultation.html` | None | None |

---

## Deliberately not reused (whole sections)

| Home partial | Reason |
|--------------|--------|
| `hero.html` | Home-only `.hero--home` |
| `home-recovery-intro.html` | Home narrative + 6-card grid — not on Services mock |
| `home-treatment-prevention.html` (whole) | Accordion collapse UX ≠ expanded category hub blocks |
| `home-gallery`, `home-reviews`, `home-specialists`, etc. | Not on Services General mock |

---

*End of design-to-source map v1.*
