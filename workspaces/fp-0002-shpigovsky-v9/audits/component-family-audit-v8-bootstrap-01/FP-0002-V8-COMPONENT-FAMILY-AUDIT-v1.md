# FP-0002 V8 — Component Family Audit (Bootstrap Pass)

**Mode:** read-only bootstrap audit
**Authority baseline:** `fp-0002-v7-four-template-canonical-demo-baseline-01`

## Canonical template SHA-256

- `index.html` — `f861e28fcd94aee93f0c4243e38a23178d00b6ed67e49972713d6af3f99a91cd`
- `uslugi-v2.html` — `e0f7f8c8efb4aa5622418b1382442e8684152000a3330c5894ab07d0275eb9bc`
- `usluga-podrazdel-v1.html` — `fc32e6744f51ddd4a5b218baf253b80da6206f359dfb6161de3c0a769c76c49c`
- `usluga-konechnaya-v1.html` — `b24ba9f1f041fda50576df6f0fd9c8ba6aaa8fa18753cec9ae653f77dcd85e1a`

## Upper-nav CSS drift (wrapper only)

- `.page-uslugi-v2__upper-nav` — `display: flex; flex-direction: column; gap: 15px; padding-top: 0; padding-bottom:0;`
- `.page-service-subdivision-v1__upper-nav` — `display: flex; flex-direction: column; gap: 15px; padding-top: 0; padding-bottom: 0;`
- `.page-service-leaf-v1__upper-nav` — `display: flex; flex-direction: column; gap: 12px; padding-top: 16px; padding-bottom: 8px;`

## Page-scoped duplication of shared component CSS

- `breadcrumbs__` rescoped under: `page-service-leaf-v1`, `page-service-subdivision-v1`, `page-uslugi-v2`
- `services-inner-hero-v2__` rescoped under: `page-service-leaf-v1`, `page-service-subdivision-v1`
- `services-page-subnav__` rescoped under: `page-service-leaf-v1`, `page-service-subdivision-v1`, `page-uslugi-v2`
- `services-program-v2` rescoped under: `page-service-leaf-v1`, `page-service-subdivision-v1`, `page-uslugi-v2`

## Drift notes

- Upper-nav HTML composition differs by page wrapper class name only; shared partials are identical includes.
- Upper-nav wrapper CSS differs (gap/padding) across page-specific classes.

## Component families

### CF-001 — Site chrome (header/footer/modal/head)
- Partials: `partials/layout/head.html`, `partials/layout/header.html`, `partials/layout/footer.html`, `partials/components/modal-consultation.html`
- Pages: `index.html`, `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`, `uslugi-v2.html`

### CF-002 — Inner hero (services-inner-hero-v2)
- Partials: `partials/sections/services-inner-hero-v2.html`
- Pages: `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`, `uslugi-v2.html`

### CF-003 — Upper page nav band (breadcrumbs + local subnav + container)
- Partials: `partials/components/breadcrumbs.html`, `partials/components/services-page-subnav.html`
- Pages: `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`, `uslugi-v2.html`
- Page wrappers: `.page-uslugi-v2__upper-nav`, `.page-service-subdivision-v1__upper-nav`, `.page-service-leaf-v1__upper-nav`

### CF-004 — Category / hub content section
- Partials: `partials/sections/services-category-section-v2.html`
- Pages: `usluga-podrazdel-v1.html`, `uslugi-v2.html`

### CF-005 — Program block (4 directions + optional CTA band)
- Partials: `partials/sections/services-program-v2.html`, `partials/components/services-program-cta-band-v2.html`
- Pages: `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`, `uslugi-v2.html`

### CF-006 — Founder quote band
- Partials: `partials/sections/home-founder-quote.html`
- Pages: `index.html`, `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`, `uslugi-v2.html`

### CF-007 — Comfort gallery band
- Partials: `partials/sections/home-comfort.html`
- Pages: `index.html`, `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`, `uslugi-v2.html`

### CF-008 — FAQ accordion band
- Partials: `partials/sections/home-faq.html`
- Pages: `index.html`, `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`, `uslugi-v2.html`

### CF-009 — Final lead form band
- Partials: `partials/sections/home-final-form.html`
- Pages: `index.html`, `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`, `uslugi-v2.html`

### CF-010 — Reviews slider band
- Partials: `partials/sections/home-reviews.html`
- Pages: `index.html`, `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`

### CF-011 — Specialists slider band
- Partials: `partials/sections/home-specialists.html`
- Pages: `index.html`, `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`

### CF-012 — Clinic landscape bleed image
- Partials: `partials/sections/home-clinic-landscape.html`
- Pages: `index.html`, `usluga-konechnaya-v1.html`, `usluga-podrazdel-v1.html`

