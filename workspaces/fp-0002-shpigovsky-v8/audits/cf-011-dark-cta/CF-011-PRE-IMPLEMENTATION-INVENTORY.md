# CF-011 PRE-IMPLEMENTATION INVENTORY

**Wave:** FP-0002 V8 CF-011 DARK CTA WRAPPER CONSOLIDATION  
**HEAD at inventory:** `db0c3ec78a83d0b06574cbb935394d284112f929`

## Family boundary decision

### CF-011 INCLUDED

| Candidate | Partial | Consumers | Classification |
|---|---|---:|---|
| Program CTA band (core) | `services-program-cta-band-v2.html` | uslugi-v2, services-program-v2, wrappers | SAME_CF011_FAMILY |
| Subdivision first CTA wrapper | `service-subdivision-first-cta-v1.html` | usluga-podrazdel-v1.html | SAME_CF011_FAMILY |
| Leaf CTA wrapper | `service-leaf-cta-01-v1.html` | usluga-konechnaya-v1.html | SAME_CF011_FAMILY |
| Stages embedded CTA (inline copy) | inline in stages partials | usluga-podrazdel-v1, usluga-konechnaya-v1 | SAME_CF011_FAMILY |

### CF-011 EXCLUDED

| Candidate | Reason |
|---|---|
| `services-mid-cta-v2` | Different HTML composition (important label block, different phone, no shared band) |
| Hero / category hub / category section CTAs | Button-only or different layout families |
| `service-subdivision-second-cta-v1` | Orphan wrapper (no page consumer); same band but unused |

## Totals

- Total CTA candidates scanned: 12
- Confirmed CF-011 partials: 4 (+ 2 inline copies in stages)
- Confirmed consumers: 3 page-level + program embed + stages embed
- Duplicate wrapper partials: 3 (2 active + 1 orphan)
- Duplicate CSS blocks: 6 page-scoped copies of band styles

## Broken ARIA root cause

- **Page:** `usluga-podrazdel-v1.html`
- **Source:** `service-subdivision-first-cta-v1.html`
- **Broken reference:** `aria-labelledby="service-subdivision-start-heading"`
- **Root cause:** Section referenced heading ID never assigned (no `h2`/`id` in wrapper; title only inside band `p`)
- **Repair:** Add visually-hidden `h2` with `id="service-subdivision-start-heading"` via canonical include parameters

## Canonical decision

- **Name:** `program-cta-band`
- **Partial:** `src/partials/components/program-cta-band.html`
- **Root class:** `.program-cta-band`
- **Model:** A — reuse existing shared band structure, collapse wrappers into parameterized canonical include
