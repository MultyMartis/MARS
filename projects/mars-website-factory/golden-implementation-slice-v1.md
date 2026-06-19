# Golden implementation slice v1

**Status:** canonical reference for Website Factory frontend implementation quality.  
**Workspace:** [workspaces/website-factory-reference-v1/](../../workspaces/website-factory-reference-v1/).

**Not:** a client deliverable; **not** Triumph production proof. **Not** typography/overflow authority — see [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md).

**RU commercial landings:** use [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md).

**Wave 5:** `faq` block added via real extraction — [operational-examples/wave5-extraction-report-faq-v1.md](operational-examples/wave5-extraction-report-faq-v1.md). Client starter: [workspaces/_template-client-v1/](../../workspaces/_template-client-v1/).

**Wave 6:** `pricing` re-extracted (commercial cards) — [operational-examples/wave6-extraction-report-pricing-v1.md](operational-examples/wave6-extraction-report-pricing-v1.md); `cases` added — [operational-examples/wave6-extraction-report-cases-v1.md](operational-examples/wave6-extraction-report-cases-v1.md). Library surface: [curated-library-index-v1.md](curated-library-index-v1.md).

---

## What this slice demonstrates

| System | Where to look |
|--------|----------------|
| **Tokens + layers** | `src/scss/foundations/_tokens.scss`, `_layers.scss` |
| **Responsive + container** | `_breakpoints.scss`, `.wf-container`, section padding in `_utilities.scss` |
| **Forms** | `partials/sections/lead_form.html` + `_forms.scss` + `js/core/form.js` |
| **Modal** | `partials/layout/modal_callback.html` + `_modal.scss` + `js/core/modal.js` |
| **JS lifecycle** | `js/core/lifecycle.js`, `js/main.js` |
| **Motion** | `_motion.scss`, modal keyframes |
| **Conversion blocks** | `hero`, `benefits`, `process`, `testimonials`, `trust`, `lead_form`, `cta_band`, `pricing`, `cases`, `faq`, `contact_block` + `sticky_cta` (orphan module) |
| **Shell blocks** | `header-nav` (HEADER_NAV), `footer` (FOOTER) + nested `legal-links` (LEGAL_LINKS) |

**WF-R01.3.2 G1:** Full LANDING golden slice stack documented in [REFERENCE-COMPOSITION-v1.md](../../workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md). Shell order: HEADER_NAV → MAIN → FOOTER (LEGAL_LINKS nested).

---

## Page entry

- **Source:** `src/pages/index.html`
- **Output:** `dist/index.html` after `npm run build`
- **Scripts order:** lifecycle → modal → form → sticky_cta → header_nav → main (fixed in page template)
- **Shell order:** `layout/header.html` (HEADER_NAV) → `<main>` (content sections) → `sections/footer.html` (FOOTER + LEGAL_LINKS nested) → modal → sticky_cta

---

## Patterns to copy into client workspaces

1. Copy `scss/foundations/` + `js/core/` wholesale; adjust `_tokens.scss` brand colors only.
2. Copy section partial **structure** (wrapper `data-section` + `data-block-id`), not necessarily visual design.
3. Keep `@@include` graph: sections never pasted into page entries.
4. Wire `data-form-endpoint` for real leads; remove mock delay in `form.js` or override endpoint attribute.

---

## Quick verification

```powershell
cd workspaces/website-factory-reference-v1
npm install
npm run build
```

Open `dist/index.html` — exercise: modal, form, sticky after scroll, pricing CTA, contact links, 375px QA ([reference-workspace-qa-flow-v1.md](reference-workspace-qa-flow-v1.md)). **Supplementary generic responsive validation only.** **For RU commercial landings use:** [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md).

Record outcome in REPORT; **SAFE UNKNOWN** if npm unavailable.

---

## Related docs

- [foundation-systems/README.md](foundation-systems/README.md) — Wave 2 standards
- [section-survivability-implementation-v1.md](foundation-systems/section-survivability-implementation-v1.md) — destroy/swap/init
- [agents/mars-forge/foundation-lite-checklist.md](../../agents/mars-forge/foundation-lite-checklist.md) — Lite QA slice
- [onboarding-flow-v1.md](onboarding-flow-v1.md) · [section-swap-demo-flow-v1.md](section-swap-demo-flow-v1.md) · [operational-examples/golden-report-examples-v1.md](operational-examples/golden-report-examples-v1.md) — Wave 4

*Wave 3–4 — golden slice pointer.*
