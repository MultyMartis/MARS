# Implementation extraction discipline v1 (Wave 4)

**Status:** **documented** — rules for promoting **real project** patterns into the shared block library.  
**Registry:** [block-registry-v0.md](block-registry-v0.md).  
**Blocks contract:** [foundation-systems/conversion-blocks-v2.md](foundation-systems/conversion-blocks-v2.md).

**Not:** automated extraction tooling.

---

## When a block is reusable

Promote to reference / Factory library only if **all** pass:

| Criterion | Question |
|-----------|----------|
| **Role clarity** | Maps to existing `block_id` or new row approved in registry |
| **Second use** | Another client or page would plausibly need same structure |
| **Survivability** | `data-section` + destroy/init safe (or static-only with no leaked listeners) |
| **Token hygiene** | No hardcoded client brand in SCSS — uses foundation tokens |
| **Content neutral** | Copy is placeholder/demo — no client PII, trademarks, fake metrics |
| **Responsive** | 375 / 768 / desktop checked — no mandatory horizontal scroll |
| **Forge compatible** | Fits Gulp partial + scoped SCSS + optional `data-module` |
| **Conversion ownership** | Primary CTA path documented per conversion-blocks-v2 |

If any fail → keep in **project workspace only**; log gap in REPORT.

---

## Extraction workflow

```text
1. Identify  — section that survived production QA on client site
2. Classify   — block_id + blast radius (local vs touched globals)
3. Strip      — client content, images, endpoints, analytics
4. Isolate JS — move listeners into WfLifecycle module or data-module
5. Token pass — replace hex/spacing with _tokens.scss variables
6. Port       — partial + _section.scss (+ js/sections if needed)
7. Reference  — add to website-factory-reference-v1 + golden slice doc
8. REPORT     — extraction record: source project (name only), files added, checks run
```

---

## Anti-project-poisoning rules

| Do not import into shared layer | Why |
|----------------------------------|-----|
| Client-specific selectors (`.triumph-*`, BEM from one brand) | Couples library to one site |
| WPBakery / page-builder markup | Breaks include graph |
| Global resets that fight foundations | Critical blast radius |
| Third-party slider/carousel deps | Scope creep — HITL per dependency |
| Fake social proof numbers | Trust violation |
| `!important` chains from legacy fixes | Hides token debt |

---

## Token cleanup checklist

- [ ] No raw `#hex` in section SCSS except documented exceptions
- [ ] Spacing uses `$space-*` or `$section-gap-*`
- [ ] z-index uses `_layers.scss` tokens only
- [ ] Border-radius uses `$radius-*`

---

## Content neutralization

| Replace | With |
|---------|------|
| Client name, product strings | "Plan A", "Service title", lorem discipline |
| Real phone/email | `+1 (555)…`, `hello@example.com` |
| Client logos | Text placeholders or generic SVG boxes |
| Analytics IDs | Remove — wire per project |
| Form endpoint | `data-form-endpoint` placeholder or mock |

---

## JS isolation checks

- [ ] No `$(document).on` without teardown
- [ ] Module has `destroy` mirroring `init`
- [ ] No inline `<script>` in partial
- [ ] `data-module` name registered before `initPage`

---

## Survivability checks

- [ ] `destroySection` clears module state flags (`__wf*Bound`)
- [ ] `replaceSectionContent` tested on block or documented static-only
- [ ] Modal/sticky/form cross-test if block touches CTAs

---

## Responsiveness checks

- [ ] 375px — primary CTA visible; cards stack
- [ ] 768px — grid breakpoints intentional
- [ ] Desktop — max-width container; no runaway line length

---

## Forge compatibility checks

- [ ] Partial path: `partials/sections/{block_id}.html`
- [ ] SCSS: `scss/sections/_{block_id}.scss` imported in `main.scss`
- [ ] `data-block-id` matches registry snake_case
- [ ] REPORT uses Standard mode for first library commit

---

## Extraction record (REPORT snippet)

```markdown
## Extraction record
- Source: <workspace slug> — block_id `pricing` (structure only)
- Neutralized: copy, logos, endpoint
- Added to reference: partial + scss + (js if any)
- Checks: 375/768/desktop PASS | SAFE UNKNOWN
- Not promoted: <reason if declined>
```

**Wave 6 examples:** [wave6-extraction-report-pricing-v1.md](operational-examples/wave6-extraction-report-pricing-v1.md) · [wave6-extraction-report-cases-v1.md](operational-examples/wave6-extraction-report-cases-v1.md). **Quality tiers:** [block-quality-tiers-v1.md](block-quality-tiers-v1.md).

*Wave 4 — implementation extraction discipline; Wave 6 — tier + report linkage.*
