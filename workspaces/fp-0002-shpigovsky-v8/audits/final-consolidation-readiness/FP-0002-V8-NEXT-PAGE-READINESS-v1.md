# FP-0002 V8 Next Page Readiness v1

**Date:** 2026-06-29  
**Status:** READ-ONLY recommendation — implementation **NOT AUTHORIZED**

---

## Next page

**«О центре» (O-Centre / About)** — next by canonical page inventory and reuse forecast documents.

**Confirmed by:** `FP-0002-HOME-COMPONENT-REUSE-MAP-v1.md`, `FP-0002-HOME-TO-SERVICES-REUSE-FORECAST-v1.md`, V8 operational roadmap deferral notes.

---

## Reusable canonical components (post CF-003–CF-012)

| Component | Partial | Notes |
|---|---|---|
| internal-page-nav | `internal-page-nav.html` | Breadcrumb + subnav |
| founder-quote | `founder-quote.html` | |
| specialists | `specialists.html` | |
| comfort | `comfort.html` | Gallery inside — separate Fancybox group |
| reviews | `reviews.html` | Swiper |
| faq | `faq.html` | Accordion |
| final-form | `final-form.html` | |
| clinic-landscape | `clinic-landscape.html` | CF-010 neutralized |
| program-cta-band | `program-cta-band.html` | |
| inner hero | existing shared partials | CF-013 HOLD — already on 3 templates |

---

## Blocks requiring fresh anatomy audit before O-Centre

| Block | Reason |
|---|---|
| home-gallery | HOLD — unique grid + Fancybox; audit deferred until O-Centre charter |
| home-staff-photo | Home-only today; similar structure to clinic-landscape but different role/dimensions |
| home-specific sequence blocks | Hero, approach, program, CTA — page composition not auto-reused |
| O-Centre unique copy sections | Content/assets not in V8 yet |

---

## Genuinely unique (expected on O-Centre)

- Page hero / intro specific to About narrative
- History/timeline blocks (if in design — **SAFE UNKNOWN** until design charter)
- Any About-only gallery or team presentation not matching existing partials

---

## Missing content/assets

- O-Centre design exports in `src/assets/design/` — **not verified in this pass**
- About-specific copy and IA — operations pack / Excel (**not imported in this task**)
- Gallery asset mapping for About — requires charter

---

## Gallery status

**HOLD** — `home-gallery` unchanged by CF-010; reuse decision deferred to O-Centre anatomy audit per operator plan.

---

## Recommended next charter

1. **FP-0002 V8 O-Centre page anatomy + reuse charter** (read-only plan approval before any HTML/CSS)
2. Per-block audit: gallery, staff-photo, hero, any About-only sections
3. Asset/content gap inventory against design source
4. Operator gate before first partial implementation

---

## Implementation authorized

**NO** — consolidation complete; next page implementation requires explicit operator charter.

**O-Centre readiness:** `READY_FOR_CHARTER`
