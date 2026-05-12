# Frontend handoff — Triumph Manipulator Landing (v0)

**Contract SoT:** [Frontend Handoff Contract v0](../../frontend-handoff-contract-v0.md)  
**Philosophy:** [Frontend Prompt Discipline v0](../../frontend-prompt-discipline-v0.md), [frontend-production-model.md](../../frontend-production-model.md) (Gulp-oriented, static-first).

---

## 1. Sections → partials (suggested map)

| Section (block_id) | Suggested partial / component path | Notes |
|--------------------|-------------------------------------|--------|
| hero | `partials/sections/hero-manipulator.html` (example) | Single H1 |
| trust_block | `partials/sections/trust-block.html` | Logo strip |
| geo_trust | `partials/sections/geo-trust.html` | List or embed map **TBD** |
| process_steps | `partials/sections/process-steps.html` | Numbered steps |
| services_grid | `partials/sections/services-grid.html` | 3–6 tiles max |
| cases | `partials/sections/cases.html` | Image lazy-load |
| faq | `partials/sections/faq.html` | `details`/`summary` or JS accordion |
| lead_form | `partials/sections/lead-form.html` | POST endpoint **SAFE UNKNOWN** |
| final_cta | `partials/sections/final-cta.html` | Links to `#quote` |
| sticky_cta | `partials/ui/sticky-cta.html` | Injected once in layout |

**No** claim these paths exist in any repo build — **handoff vocabulary only**.

---

## 2. SCSS architecture

- **ITCSS-like** or BEM blocks per section file under `scss/sections/_hero-manipulator.scss` etc.
- **Variables:** colors, spacing, breakpoints in `_tokens.scss` (**SAFE UNKNOWN** real token file).
- **No** magic numbers in partials without named token where repeated.

---

## 3. JS expectations

- **Vanilla or minimal** bundle: FAQ accordion, sticky CTA show/hide on scroll, form client-side validation shell.
- **Progressive enhancement:** form works without JS if server handles POST (**policy TBD**).
- Use **`data-*`** hooks per discipline doc: e.g. `data-sticky-cta`, `data-faq-accordion`, `data-scroll="smooth"` for in-page anchors.

---

## 4. Responsive behavior

- **Breakpoints:** standard 375 / 768 / 1024 / 1280 test matrix in QA.
- **Hero:** stack image under copy on narrow screens if needed.
- **services_grid:** 1 col mobile, 2 col tablet, 3 desktop max.

---

## 5. `data-*` usage (examples)

| Hook | Behavior |
|------|----------|
| `data-sticky-cta` | Root for sticky bar attach / scroll listener |
| `data-primary-cta-label` | Optional: sync sticky label with hero (**single source** preferred in template) |
| `data-faq-item` | Per accordion row |

---

## 6. Frontend constraints

- **Do not** edit compiled `dist/` by hand — Gulp (or project build) is SoT for output.
- **Accessibility:** focus order matches visual order; skip link optional but recommended.
- **Third-party:** maps/reviews widgets — load only after consent if CMP exists (**SAFE UNKNOWN**).

---

*Frontend handoff v0 — reference execution only*
