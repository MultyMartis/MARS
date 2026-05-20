# Reusable conversion blocks v1 (v2 wave)

**Status:** structure normalization — **not** full block implementations.

**Registry:** [block-registry-v0.md](../block-registry-v0.md). **Survivability:** [section-replacement-contract-v1.md](../section-replacement-contract-v1.md).

---

## 1. Block kit (Wave 2 priority)

| block_id | Operational role | Conversion ownership |
|----------|------------------|----------------------|
| `hero` | First-screen value + primary path | Primary CTA / orientation |
| `lead_form` | Lead capture | Form module + submit success |
| `cta_band` | Mid-page push | Secondary/repeated CTA |
| `pricing` | Offer comparison | Plan selection → CTA |
| `social_proof` | Trust (logos, metrics, quotes) | Supports CTA — does not replace it |
| `sticky_cta` | Persistent mobile/desktop bar | Repeat primary action |
| `contact_block` | Direct contact (phone, map, hours) | Call/click conversions |

*Note:* registry may use `trust_block` — map `social_proof` intent to registry row when instantiating.

---

## 2. Partial structure direction

Each block ships as:

```text
html/partials/sections/{block_id}.html
scss/sections/_{block_id}.scss
js/sections/{block_id}.js   # optional — only if not covered by data-module in partial
```

**Section wrapper contract:**

```html
<section class="wf-section wf-section--hero" data-section data-block-id="hero">
  <!-- content -->
</section>
```

---

## 3. Per-block expectations

### `hero`

| Aspect | Rule |
|--------|------|
| Structure | H1 once; primary CTA; optional proof line |
| Responsive | Stack media below copy on mobile; CTA full-width optional |
| Hooks | `data-module` only if carousel/video — else static |
| Replacement | HEADER partial separate — [layout-shell-governance](../layout-shell-governance.md) |

### `lead_form`

| Aspect | Rule |
|--------|------|
| Structure | Uses [form-system-v2.md](form-system-v2.md) |
| Responsive | Single column mobile; no horizontal field pairs |
| Conversion | Min fields for offer; HITL on legal checkboxes |
| Replacement | Re-bind `data-module="form"` after swap |

### `cta_band`

| Aspect | Rule |
|--------|------|
| Structure | Short copy + 1–2 actions; no competing primaries |
| Cadence | Often `section-gap-l` above/below |
| Responsive | Buttons stack; equal min-height |

### `pricing`

| Aspect | Rule |
|--------|------|
| Structure | Cards with featured tier; aria for comparison |
| Responsive | Stack cards; sticky footer CTA optional |
| Replacement | Critical if pricing tokens global |

### `social_proof`

| Aspect | Rule |
|--------|------|
| Structure | Logos grid or metric row — no fake metrics |
| Responsive | 2-col → 1-col; logo max-height token |
| Conversion | Supports hero/pricing — no orphan proof |

### `sticky_cta`

| Aspect | Rule |
|--------|------|
| Structure | Fixed bar; `data-module="sticky-cta"` |
| z-index | `$z-sticky-cta` — below modal |
| Mobile | Show after hero exit (IntersectionObserver) |
| Replacement | destroy sticky module before section swap |

### `contact_block`

| Aspect | Rule |
|--------|------|
| Structure | tel: links; clickable map; hours text |
| Accessibility | Real links, not JS-only phone display |
| Responsive | Click-to-call prominent |

---

## 4. Responsive expectations (shared)

- `mobile_priority: high` blocks: spot-check 375px first.
- No block hides primary CTA on mobile without HITL.
- Images lazy-load below fold; hero LCP image excluded from lazy if handoff requires.

---

## 5. Replacement compatibility checklist

Before re-freeze:

- [ ] `data-block-id` matches registry
- [ ] `data-section` root present
- [ ] Section SCSS scoped (`.wf-section--{id}`)
- [ ] No global token edits without REPORT
- [ ] `destroySection` → swap → `initSection` executed
- [ ] Adjacent cadence tiers documented if changed
- [ ] CTA IDs unique page-wide

---

## 6. Implementation status (reference workspace)

See [curated-library-index-v1.md](../curated-library-index-v1.md) for tiers and extraction sources.

| Wave | Blocks |
|------|--------|
| Wave 3 | `hero`, `lead_form`, `cta_band` |
| Wave 4 | `social_proof`, `sticky_cta` (+ `js/sections/sticky_cta.js`), `contact_block` |
| Wave 5 | `faq` (Triumph extract) |
| Wave 6 | `pricing` (Triumph re-extract), `cases` (Triumph extract) |

Path: [workspaces/website-factory-reference-v1/](../../../workspaces/website-factory-reference-v1/).

*Wave 2 — conversion block normalization; Wave 6 — curated status in library index.*
