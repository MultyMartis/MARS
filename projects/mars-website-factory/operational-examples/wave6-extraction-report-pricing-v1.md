# REPORT — Wave 6 real extraction (pricing block)

**Mode:** Standard  
**Scope:** Re-extract `pricing` from Triumph V2 `equipment-prices` into reference library (replaces Wave 4 synthetic SaaS cards).

**Discipline:** [implementation-extraction-discipline-v1.md](../implementation-extraction-discipline-v1.md) · **Tier:** validated — [block-quality-tiers-v1.md](../block-quality-tiers-v1.md)

---

## Extraction record

| Field | Value |
|-------|--------|
| **Source** | `workspaces/triumph-manipulator-landing-v2` — `equipment-prices.html` + `_equipment-prices.scss` (structure) |
| **block_id** | `pricing` (registry row #7) |
| **Replaces** | Wave 4 synthetic three-column SaaS tier partial |
| **Neutralized** | Russian copy, RUB rates, equipment images, icon `@@include`, Triumph CTAs, service claims |
| **Structural kept** | Split header (intro + estimate CTA), spec `<dl>` rows per card, media badge, footer price + order + note |
| **Structural removed** | Product photos, Font Awesome spec icons, multi-line Russian titles |
| **Added to reference** | `partials/sections/pricing.html`, `scss/sections/_pricing.scss` (in-place replace) |

---

## Criterion validation

| Criterion | Result |
|-----------|--------|
| Role clarity | `pricing` in block-registry-v0 — PASS |
| Second use | Commercial landings / service pricing — PASS |
| Survivability | Static `data-section`; no section JS — PASS |
| Token hygiene | `$space-*`, `$color-*`, `$radius-*`, `$shadow-*` — PASS |
| Content neutral | English placeholders; USD demo rates — PASS |
| Responsive | 3-col ≥768; featured first on mobile stack — PASS (SCSS) |
| Forge compatible | Gulp partial + scoped SCSS — PASS |
| Conversion ownership | Featured tier → modal; others → `#lead-form` / `#contact` — PASS |

---

## Token cleanup

- [x] No raw `#hex` in section SCSS (gradients use neutral tokens)  
- [x] Spacing uses `$space-*` / `$section-gap-*`  
- [x] No custom z-index  
- [x] Border-radius uses `$radius-*`

---

## JS isolation

- [x] No section JS  
- [x] Uses existing `data-modal-open` only — no new listeners

---

## Survivability checks

- [x] `data-section` + `data-block-id="pricing"`  
- [x] Static-only replacement safe  
- [ ] Full swap demo — **SAFE UNKNOWN**

---

## Responsiveness checks

| Viewport | Result |
|----------|--------|
| 375px | Stacked cards; featured order -1 — **PASS** (SCSS intent) |
| 768px | 3-column grid — **PASS** |
| Desktop | Container bound — **PASS** |

---

## Build verification

```text
npm run build @ website-factory-reference-v1 — PASS (2026-05-21, agent-run)
```

---

## Anti-poisoning avoided

- No `.equipment-prices` / `.price-card` selectors  
- No Triumph image paths  
- No fake “15 minute callback” production promises in library copy

---

## SAFE UNKNOWN

- Formal WCAG on spec `<dl>` grid — not audited  
- Real currency/tax display rules — project-local  
- Featured tier modal vs anchor — operator verifies per client

---

## Risks

- Operators may expect SaaS-style simple tiers — curated index marks commercial card pattern  
- Replacing Wave 4 partial may break client copies that forked old `wf-pricing__grid` — migration via pilot REPORT

---

## Files touched

**Updated (replace):**

- `workspaces/website-factory-reference-v1/src/partials/sections/pricing.html`
- `workspaces/website-factory-reference-v1/src/scss/sections/_pricing.scss`

*Wave 6 — second real operational extraction (pricing re-extract).*
