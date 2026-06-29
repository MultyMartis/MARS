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

## New assets potentially required

- Decorative background raster `d3ac7d00af36` at 10% opacity (`1:2440`, mobile `1:5697`) — export pass before Phase 6

## Shared modifiers

- None required for shared families unless operator approves `founder-quote--o-centre-context` page wrapper (scoped HTML class only)

## JS

**Expected: 0** — infrastructure subgroups are CSS layout only; no Swiper/Fancybox added to infrastructure band.
