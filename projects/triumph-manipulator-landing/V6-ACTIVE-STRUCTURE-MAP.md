# V6 — Active structure map

**Status:** human-operated audit snapshot (2026-05-28).  
**Workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Build entry:** `src/pages/index.html` only (`npm run build` → `dist/index.html`).

This map lists **only** what the current V6 build actually composes. For dead inventory see [`V6-LEGACY-AND-DEAD-AUDIT.md`](V6-LEGACY-AND-DEAD-AUDIT.md).

---

## A. Active page entry

| Item | Path / value |
|------|----------------|
| **Page** | `src/pages/index.html` |
| **`data-page-type`** | `ppc-zakaz-manip` |
| **Head include** | `partials/layout/head-v5-page01.html` |
| **Scripts include** | `partials/layout/scripts-v5-page01.html` |
| **Footer** | `partials/sections/v5-page01/landing-footer.html` → `partials/components/polygon-copyright.html` |
| **Modal** | `partials/components/callback-modal.html` (`@@prefix`: `zakaz`) |

### Active section order (`<main>`)

| # | Partial | Section root / anchor |
|---|---------|------------------------|
| 1 | `v5-ppc/zakaz/screen-02-specs.html` | `.machine-showcase--ops-panel`, `#specs` |
| 2 | `v5-ppc/zakaz/screen-02-tasks.html` | `.machine-transport--ops-grid`, `#tasks` |
| 3 | `v5-ppc/zakaz/screen-02b-order-steps.html` | `.order-steps--process` |
| 4 | `v5-ppc/zakaz/screen-02c-pricing-factors.html` | `.pricing-factors--system`, `#pricing` |
| 5 | `v5-page01/screen-03-trust-reviews.html` | `.trust`, `#reviews` |
| 6 | `v5-page01/screen-03b-b2b.html` | B2B notes block |
| 7 | `v5-page01/dark-proof-strip.html` | `.dark-proof-strip` |
| 8 | `v5-ppc/zakaz/screen-04-faq.html` | `.faq--split-cta`, `#faq` + embedded `#contacts` |

### First screen (outside `<main>`)

| Partial | Notes |
|---------|--------|
| `partials/layout/header-v5-page01.html` | `@@prefix`: `zakaz` |
| `v5-ppc/zakaz/screen-01-hero.html` | `.first-screen` wrapper in `index.html`; `#hero` |

### Canonical zakaz stack

- **PPC folder:** `src/partials/sections/v5-ppc/zakaz/` (8 section partials; 7 in build + 1 legacy orphan `final-contact-cta.html`)
- **Shared blocks:** `src/partials/sections/v5-page01/` (trust, B2B, proof strip, footer)
- **Not in build:** standalone `final-contact-cta.html` (any slug) — contact lives inside `screen-04-faq.html`

---

## B. Active partials (15 files in include closure)

### Layout

| Partial | Role |
|---------|------|
| `partials/layout/head-v5-page01.html` | Meta, Font Awesome vendor CSS, `style.css` |
| `partials/layout/header-v5-page01.html` | Site header + drawer |
| `partials/layout/scripts-v5-page01.html` | JS bundle tags |

### Hero

| Partial | Role |
|---------|------|
| `v5-ppc/zakaz/screen-01-hero.html` | Hero, inline hero form, cargo cards (`hero__cargo-action`) |

### Machine showcase / tasks

| Partial | Role |
|---------|------|
| `v5-ppc/zakaz/screen-02-specs.html` | Spec panel, `.machine-showcase__spec-panel` |
| `v5-ppc/zakaz/screen-02-tasks.html` | Tasks cluster (`.machine-transport--ops-grid`; legacy wrapper class `.prices`) |

### Order steps / pricing

| Partial | Role |
|---------|------|
| `v5-ppc/zakaz/screen-02b-order-steps.html` | `.order-steps--process` |
| `v5-ppc/zakaz/screen-02c-pricing-factors.html` | `.pricing-factors--system` |

### Proof strip / trust

| Partial | Role |
|---------|------|
| `v5-page01/screen-03-trust-reviews.html` | Reviews |
| `v5-page01/screen-03b-b2b.html` | B2B block |
| `v5-page01/dark-proof-strip.html` | Dark proof strip |

### FAQ / contact (canonical)

| Partial | Role |
|---------|------|
| `v5-ppc/zakaz/screen-04-faq.html` | `.faq--split-cta` + `aside.contact-cta.contact-cta--embedded#contacts` + inline form |

### Footer / modal / forms

| Partial | Role |
|---------|------|
| `v5-page01/landing-footer.html` | Footer nav + legal links |
| `partials/components/polygon-copyright.html` | Copyright line |
| `partials/components/callback-modal.html` | Callback modal form (`data-form-id="zakaz-callback"`) |

**Inventory note:** 117 HTML partials exist under `src/partials/`; **102 are outside** this closure (scaffolds + V2/V3/V4 orphans).

---

## C. Active SCSS (`src/scss/style.scss`)

### Base / layout / components (canonical)

| Import | Status |
|--------|--------|
| `base/reset`, `base/base`, `base/typography-protection`, `base/radius-zero` | canonical |
| `layout/header` | canonical |
| `components/clickable`, `components/interactions`, `components/button`, `components/modal`, `components/forms` | canonical |

### Sections (canonical for index)

| Import | File | Status |
|--------|------|--------|
| `sections/screen-01-hero` | `_screen-01-hero.scss` | canonical |
| `sections/screen-02-prices` | `_screen-02-prices.scss` | **legacy filename** — supplies `.machine-showcase` base |
| `sections/screen-03-trust-reviews` | `_screen-03-trust-reviews.scss` | canonical |
| `sections/dark-proof-strip` | `_dark-proof-strip.scss` | canonical |
| `sections/screen-04-faq` | `_screen-04-faq.scss` | canonical (`.faq--split-cta`) |
| `sections/final-contact-cta` | `_final-contact-cta.scss` | **legacy filename** — active for `.contact-cta--embedded` |
| `sections/landing-footer` | `_landing-footer.scss` | canonical |

### V5 extensions (canonical)

| Import | File | Status |
|--------|------|--------|
| `sections/v5-hero-extensions` | `_v5-hero-extensions.scss` | canonical |
| `sections/v5-order-steps` | `_v5-order-steps.scss` | canonical |
| `sections/v5-pricing-factors` | `_v5-pricing-factors.scss` | canonical |
| `sections/v5-b2b-notes` | `_v5-b2b-notes.scss` | canonical |
| `sections/v5-page01-overrides` | `_v5-page01-overrides.scss` | canonical |
| `sections/v5-machine-showcase` | `_v5-machine-showcase.scss` | canonical (`body[data-page-type='ppc-zakaz-manip']`) |

### Reserved / low-use on index

| Import | File | Status |
|--------|------|--------|
| `sections/legal-pages` | `_legal-pages.scss` | **legacy-but-imported** — no legal page HTML in build; footer links to `/privacy-policy/` etc. |

### Utils (transitive)

`_tokens.scss`, `_container.scss`, `_layers.scss`, `_section-headings.scss`, `_variables.scss` — canonical support.

### Dead CSS candidates (do not purge in this pass)

Selectors such as `.faq__grid` in `_screen-04-faq.scss` have **no** match in active HTML — **risky-remove** until scoped audit per selector.

---

## D. Active JS

Loaded by `scripts-v5-page01.html` (all copied to `dist/assets/js/`):

| File | Role | Status |
|------|------|--------|
| `header-menu.js` | Drawer / burger / anchor nav | active, rollout-sensitive |
| `modal.js` | Modal open/close, focus trap; desktop breakpoint **1025px** | active, rollout-sensitive |
| `form.js` | Mailer POST `backend/send-lead.php`, validation, honeypot | active, rollout-sensitive |
| `faq-accordion.js` | Single-open `<details class="faq-item">` | active |
| `main.js` | Boots header, modals, forms | active |

**Legacy candidate:** none identified as unused on index build.

---

## E. Active breakpoints (actual usage)

| Breakpoint | Where used | Role |
|------------|------------|------|
| **1024px** / **1025px** | Hero extensions, machine showcase, order steps, pricing factors, FAQ split, footer, modal, final-contact-cta SCSS | **Canonical section layout law** |
| **1490px** | `$header-nav-break` in `_header.scss`; also `_screen-03-trust-reviews.scss`, `_v5-machine-showcase.scss` | Header nav collapse + selective section tweaks |
| **1380px** | `$header-nav-compact` in `_header.scss` | Header-only compact nav |
| **810px** | `$header-drawer-mid` in `_header.scss` | Header drawer mid layout |
| **760px** / **761–1180px** | `_container.scss` padding mixins | Page horizontal padding |
| **980px** | `max-width: 980px` **property values** in `_v5-pricing-factors.scss`, `_v5-order-steps.scss`, `_screen-02-prices.scss` | **Legacy content width cap** — not a global breakpoint token; still active on index |
| **981px** | — | **Not found** in V6 `src/scss` (2026-05-28 scan) |

**Rule for rollout:** new section SCSS should use **1024 / 1025** only; do not add new **980 / 981** media queries.

---

## Verification snapshot (post-build)

| Check | Result |
|-------|--------|
| `id="contacts"` in `dist/index.html` | **1** |
| `faq--split-cta` | present |
| `data-form-id` values | `zakaz-hero-quote`, `zakaz-contact-quote`, `zakaz-callback` |

---

*Human-maintained — not automated topology enforcement.*
