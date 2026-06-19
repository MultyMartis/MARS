# LANDING Reference Composition v1

**Site type:** LANDING  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Composition version:** v1  
**Status:** PUBLISHED  
**Page type:** `LANDING_PAGE`  
**Scaffold:** `src/pages/index.html`  
**Authority:** [wf-r01-3-2-landing-completion-charter-v1.md](../../projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md) · [wf-r01-3-1-coverage-model-charter-v1.md](../../projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md)

**Honesty boundary:** Reference composition documentation only. **Not** production acceptance. **Not** pixel-perfect verified. **Not** CMS-bound.

---

## Site-level shell

```text
HEADER_NAV
MAIN
FOOTER
└── LEGAL_LINKS
```

**Implementation:**

| Shell zone | Include path | DOM role |
|------------|--------------|----------|
| HEADER_NAV | `src/pages/index.html` → `partials/layout/header.html` → `partials/sections/header-nav.html` | Site-level `<header>` |
| MAIN | `src/pages/index.html` → `<main id="main">` | Single `<main>` |
| FOOTER | `src/pages/index.html` → `partials/sections/footer.html` (after `</main>`) | Site-level `<footer>` |
| LEGAL_LINKS | nested in FOOTER → `partials/components/legal-links.html` | `<nav>` inside FOOTER bottom slot |

**Auxiliary (outside MAIN, not site shell):**

| Artifact | Path | Role |
|----------|------|------|
| Modal callback | `partials/layout/modal_callback.html` | Layout overlay |
| STICKY_CTA module | `partials/sections/sticky_cta.html` | Floating conversion module |

---

## MAIN order

```text
HERO
BENEFITS
PROCESS
TESTIMONIALS
TRUST
CASES
PRICING
LEAD_FORM
CTA
FAQ
CONTACTS
```

**Source:** `src/pages/index.html` include order (post–G1 shell correction).

---

## Composition relationships

| Rule | Status |
|------|--------|
| HEADER_NAV ≠ HERO | **Preserved** — header shell only; hero is first MAIN section |
| TESTIMONIALS ≠ TRUST | **Preserved** — separate partials (Wave A3 split) |
| FOOTER ≠ LEGAL_LINKS | **Preserved** — LEGAL_LINKS is nested composition inside FOOTER |
| FOOTER contains LEGAL_LINKS | **Yes** — `data-composition-slot="legal_links"` in FOOTER bottom |
| CONTACTS ≠ footer contact placeholders | **Preserved** — `contact_block` is MAIN section; footer has separate contact zone |
| CTA section ≠ header action element | **Preserved** — `cta_band` is MAIN section; header may have compositional CTA button only |

---

## Block implementation mapping

| block_id | Partial path | SCSS path | Include location | Registry state | Build evidence | Composition role |
|----------|--------------|-----------|------------------|----------------|----------------|------------------|
| `HEADER_NAV` | `partials/sections/header-nav.html` | `scss/sections/_header-nav.scss` | Before `<main>` via `layout/header.html` | PARTIAL (Wave C2) | `dist/index.html` site `<header>` | Global shell — primary navigation |
| `HERO` | `partials/sections/hero.html` | `scss/sections/_hero.scss` | MAIN — first section | PARTIAL (G0) | `dist/index.html` | Conversion — primary value proposition |
| `BENEFITS` | `partials/sections/benefits.html` | `scss/sections/_benefits.scss` | MAIN | PARTIAL (Wave A1) | `dist/index.html` | Conversion — outcome/value props |
| `PROCESS` | `partials/sections/process.html` | `scss/sections/_process.scss` | MAIN | PARTIAL (Wave A2) | `dist/index.html` | Trust/narrative — step flow |
| `TESTIMONIALS` | `partials/sections/testimonials.html` | `scss/sections/_testimonials.scss` | MAIN | PARTIAL (Wave A3) | `dist/index.html` | Trust — curated quotes |
| `TRUST` | `partials/sections/trust.html` | `scss/sections/_trust.scss` | MAIN | PARTIAL, narrowed (Wave A3) | `dist/index.html` | Trust — metrics/logos/badges |
| `CASES` | `partials/sections/cases.html` | `scss/sections/_cases.scss` | MAIN | PARTIAL (G0/W6) | `dist/index.html` | Trust — case highlights |
| `PRICING` | `partials/sections/pricing.html` | `scss/sections/_pricing.scss` | MAIN | PARTIAL (G0/W6) | `dist/index.html` | Conversion — offer cards |
| `LEAD_FORM` | `partials/sections/lead_form.html` | `scss/sections/_lead_form.scss` | MAIN | PARTIAL (G0) | `dist/index.html` | Conversion — lead capture |
| `CTA` | `partials/sections/cta_band.html` | `scss/sections/_cta_band.scss` | MAIN | PARTIAL (`cta_band` hook) | `dist/index.html` | Conversion — band CTA |
| `FAQ` | `partials/sections/faq.html` | `scss/sections/_faq.scss` | MAIN | PARTIAL (Wave 5) | `dist/index.html` | Trust — objections |
| `CONTACTS` | `partials/sections/contact_block.html` | `scss/sections/_contact_block.scss` | MAIN | PARTIAL (G0) | `dist/index.html` | Contact — NAP block |
| `FOOTER` | `partials/sections/footer.html` | `scss/sections/_footer.scss` | After `</main>` | PARTIAL (Wave B1) | `dist/index.html` site `<footer>` | Global shell — site footer |
| `LEGAL_LINKS` | `partials/components/legal-links.html` | `scss/components/_legal-links.scss` | Nested in FOOTER | PARTIAL (Wave B2) | `dist/index.html` inside FOOTER | Legal — policy links cluster |
| `STICKY_CTA` | `partials/sections/sticky_cta.html` | `scss/sections/_sticky_cta.scss` | After FOOTER (body level) | PARTIAL (G0 module) | `dist/index.html` + `dist/js/sections/sticky_cta.js` | Conversion — floating CTA module |

**Optional at G1 (absent, allowed):** `MAP` — not included.

---

## JavaScript mapping

| Module | Path | Hook | Behavior |
|--------|------|------|----------|
| Lifecycle | `js/core/lifecycle.js` | `WfLifecycle` | Module registration bootstrap |
| Modal | `js/core/modal.js` | `data-modal` | Callback modal open/close |
| Form | `js/core/form.js` | `data-form` | Lead form mock submit |
| Sticky CTA | `js/sections/sticky_cta.js` | `data-module="sticky-cta"` | Scroll-reveal sticky bar |
| Header nav | `js/sections/header_nav.js` | `data-module="header-nav"` | Mobile menu toggle (`aria-expanded`) |
| Main | `js/main.js` | — | `DOMContentLoaded` init |

**No** runtime orchestration product. **No** FILTERS/SEARCH modules.

---

## Validation state

| Layer | Status |
|-------|--------|
| **BUILT** | Yes — `npm run build` PASS in reference workspace |
| **STRUCTURALLY VALIDATED** | Yes — G1 exit pass shell order verified (`HEADER_NAV` → `MAIN` → `FOOTER` → nested `LEGAL_LINKS`) |
| **NOT PIXEL-PERFECT VERIFIED** | Reference partials are Template-Art baselines, not pixel targets |
| **NOT PRODUCTION PASS** | Placeholder copy; no operator visual approval; no live endpoints |

---

## Known limitations

- Placeholder neutral English copy throughout — not client delivery content
- No production URL or canonical domain binding
- No CMS / data binding — static reference only
- No production legal pages behind LEGAL_LINKS hrefs (`#` placeholders)
- No pixel-perfect design target — reference quality ≠ production acceptance
- HEADER_NAV is minimal LANDING depth — not BZPM megamenu
- `MAP` optional block absent at G1
- Curated library v0 snake_case labels remain operational view only — coverage truth uses v1 `block_id`
- STICKY_CTA lives outside MAIN by design (floating module)

---

*Published: 2026-06-19 — WF-R01.3.2 Gate G1 exit pass*
