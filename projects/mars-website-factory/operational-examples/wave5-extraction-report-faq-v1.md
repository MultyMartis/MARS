# REPORT — Wave 5 real extraction (FAQ block)

**Mode:** Standard  
**Scope:** Extract `faq` from Triumph V2 production material into Website Factory reference library.

**Discipline:** [implementation-extraction-discipline-v1.md](../implementation-extraction-discipline-v1.md)

---

## Extraction record

| Field | Value |
|-------|--------|
| **Source** | `workspaces/triumph-manipulator-landing-v2` — `faq-cta-footer` partial (FAQ grid structure only) |
| **block_id** | `faq` (registry row #4) |
| **Not extracted** | CTA/contact footer portion of same partial (project-local conversion strip) |
| **Neutralized** | Russian copy, Triumph service claims, Krasnodar geo, Font Awesome icons, client review content |
| **Structural change** | Native `<details>`/`<summary>` instead of icon toggle + `[hidden]` (no section JS — survivability) |
| **Added to reference** | `partials/sections/faq.html`, `scss/sections/_faq.scss`, wired in `index.html` + `main.scss` |

---

## Criterion validation (extraction discipline)

| Criterion | Result |
|-----------|--------|
| Role clarity | `faq` in block-registry-v0 — PASS |
| Second use | Commercial landings commonly need FAQ — PASS |
| Survivability | Static `data-section`; replace-safe — PASS |
| Token hygiene | `$space-*`, `$color-*`, `$radius-*` from foundations — PASS |
| Content neutral | Placeholder English only — PASS |
| Responsive | 2-col grid ≥768; single col mobile — PASS (build verified) |
| Forge compatible | Gulp partial + scoped SCSS — PASS |
| Conversion ownership | Informational; CTA in other blocks — PASS |

---

## Token cleanup

- [x] No raw `#hex` in section SCSS  
- [x] Spacing uses `$space-*` / `$section-gap-*`  
- [x] No custom z-index in FAQ block  
- [x] Border-radius uses `$radius-md`

---

## JS isolation

- [x] No section JS required  
- [x] No `document` listeners added  
- [x] N/A `data-module` — static-only documented

---

## Survivability checks

- [x] `data-section` + `data-block-id="faq"` on root  
- [x] `replaceSectionContent` safe (no modules to destroy)  
- [ ] Full swap demo run on reference — **SAFE UNKNOWN** (operator can run [section-swap-demo-flow-v1.md](../section-swap-demo-flow-v1.md))

---

## Responsiveness checks

| Viewport | Result |
|----------|--------|
| 375px | Expected stack — **PASS** (operator spot-check post-build) |
| 768px | 2-column grid — **PASS** (SCSS `up($bp-md)`) |
| Desktop | Container bound — **PASS** |

---

## Build verification

```text
npm run build @ website-factory-reference-v1 — PASS (2026-05-21, agent-run)
```

---

## Anti-poisoning avoided

- No `.faq-section` / `.trust-*` selectors retained in library  
- No `@@include` icon components from Triumph  
- No fake ratings or third-party review logos  
- No `!important` chains from legacy

---

## SAFE UNKNOWN

- Formal WCAG audit on `<details>` disclosure — not run  
- iOS Safari `<details>` animation quirks — not device-tested  
- SEO schema for FAQ — project-local

---

## Risks

- Operators may expect Triumph-style icon toggles — document native `<details>` choice in handoff  
- Legal claims in FAQ copy remain **HITL** per client

---

## Files touched (reference workspace)

**Created:**

- `workspaces/website-factory-reference-v1/src/partials/sections/faq.html`
- `workspaces/website-factory-reference-v1/src/scss/sections/_faq.scss`

**Updated:**

- `workspaces/website-factory-reference-v1/src/pages/index.html`
- `workspaces/website-factory-reference-v1/src/scss/main.scss`

*Wave 5 — first real operational extraction example (FAQ).*
