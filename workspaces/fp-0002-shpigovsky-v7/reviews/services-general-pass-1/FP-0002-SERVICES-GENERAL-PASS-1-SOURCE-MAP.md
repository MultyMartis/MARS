# FP-0002 — Services General Pass 1 Source Map

**Date:** 2026-06-26  
**Authority:** operator-canonical src @ `1072022b` planning base  
**Implementation commit target:** `feat(fp-0002): implement services general page pass 1`

## Changed files

| File | Action | Reason |
| ---- | ------ | ------ |
| `src/pages/uslugi.html` | Modified | Pass 1 page shell: inner hero, category hub comment, section order, `main.page-uslugi` |
| `src/scss/style.scss` | Modified | Scoped `.page-uslugi .hero__tagline:empty` — hide empty tagline (SAFE_UNKNOWN) |

## Unchanged (protected)

| Path | Status |
| ---- | ------ |
| `src/pages/index.html` | Untouched |
| `src/partials/sections/home-*.html` | Untouched |
| `src/js/main.js` | Untouched |
| `src/partials/sections/hero-inner.html` | Untouched (reuse via include) |
| `src/partials/sections/hero.html` | Untouched |

## Inner Hero wiring

| Field | Value |
| ----- | ----- |
| Partial | `partials/sections/hero-inner.html` *(operator path; task doc alias `layout/hero-inner.html` not present)* |
| Modifier | `.hero--inner` |
| `heroImage` | `assets/img/hero/hero-main.png` |
| `heroWidth` / `heroHeight` | `2230` / `1246` |
| `heroTitle` | `Лечение и&nbsp;профилактика` |
| `heroTagline` | `""` (empty — SAFE_UNKNOWN) |
| CTA | **Not wired** — partial has no CTA slot; header/footer modal hooks remain |

## Page root

| Hook | Location |
| ---- | -------- |
| `body.page-uslugi` | Pre-existing operator scope |
| `main.page-uslugi` | Added Pass 1 |
| `data-page="uslugi"` | Pre-existing |

## Section order (Pass 1)

1. `hero-inner.html`
2. HTML comment — category hubs reserved Pass 2
3. `home-rehabilitation-program.html` — `programHeading`: «Наша программа включает 4&nbsp;направления»
4. `home-founder-quote.html` — variant A (`founderQuoteModifierClass=""`), `modalSource=services-founder`
5. `home-comfort.html`
6. `home-faq.html`
7. `home-final-form.html` — `leadSource=services-final`

## Category hubs

| Item | Status |
| ---- | ------ |
| Visible placeholders | **Zero** |
| HTML marker | `<!-- SERVICES CATEGORY HUBS WILL BE INSERTED HERE IN PASS 2 -->` |
| `services-category-hub.html` | Not created |

## Hero asset status

| Item | Status |
| ---- | ------ |
| Services-specific Figma export | **Not performed** (Pass 1 rule) |
| Temporary asset | `assets/img/hero/hero-main.png` (existing neutral hero fallback) |
| Final Services interior hallway | **Pending Pass 2+ export** |

## Reused partials (includes only)

- `layout/header.html`, `layout/footer.html`
- `components/modal-consultation.html`
- All five `home-*` sections listed above — parameters only

---

*End of Pass 1 source map.*
