# FP-0002 V8 O-Centre Correction Architecture v1

## Files to keep (no shared rewrite)

- `src/partials/layout/header.html`, `footer.html`, `modal-consultation.html`
- `src/partials/components/internal-page-nav.html`
- `src/partials/sections/founder-quote.html` (base only)
- `src/partials/sections/specialists.html`, `reviews.html`, `final-form.html`
- `src/partials/sections/services-program-v2.html` (canonical program)
- `src/partials/components/program-cta-band.html`

## Files to restructure

| File | Action |
|---|---|
| `src/pages/o-centre.html` | Reorder includes; add clinic-landscape; split who-we-treat visuals |
| `institutional-narrative.html` | Optional wrapper for founder context; no shared base change |
| `infrastructure-narrative.html` | Replace flat gallery with semantic subgroups (7 groups) |
| Inline `program-approach-band` | Keep content; fix order relative to CTAs and landscape |
| `src/scss/style.scss` | Page-scoped subgroup layouts + decorative backgrounds only |

## Additional canonical reuse

| Component | Evidence | Decision |
|---|---|---|
| `clinic-landscape.html` | Missing bleed after approach; asset `shpigovsky-clinic-landscape.webp` approved CF-010 | **`DIRECT_REUSE_CLINIC_LANDSCAPE`** |

## New assets — export status

- **OC-DEC-01** decorative background `d3ac7d00af36` — **APPROVED_EXPORTED** at `src/img/content/o-centre/decorative/o-centre-infrastructure-background.webp` (953×988 WebP, alpha preserved). Figma node opacity 0.1 — apply in CSS, not baked into bitmap. Phase 6: CSS integration only.

## Shared modifiers

- None required for shared families unless operator approves `founder-quote--o-centre-context` page wrapper (scoped HTML class only)

## JS

**Expected: 0** — infrastructure subgroups are CSS layout only; no Swiper/Fancybox added to infrastructure band.
