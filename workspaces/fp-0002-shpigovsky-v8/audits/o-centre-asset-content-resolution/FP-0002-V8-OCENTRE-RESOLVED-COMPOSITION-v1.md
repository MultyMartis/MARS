# FP-0002 V8 O-Centre Resolved Composition v1

**Based on:** Spig_v1.2 frame anatomy + resolution artifacts (2026-06-29)

| Order | Block | Content resolved | Asset resolved | Reuse source | Implementation status |
|---:|---|---:|---:|---|---|
| 1 | OC-B01 Hero | Yes | Yes | `services-inner-hero-v2.html` + new hero image | READY |
| 2 | OC-B02 Subnav | Yes | N/A | `internal-page-nav.html` (CF-003) | READY |
| 3 | OC-B03 Institutional | Yes | Partial | **Unique partial** | READY_WITH_KNOWN_GAP |
| 4 | OC-B04 Who we treat | Yes | N/A | `services-category-section-v2` modifier | READY |
| 5 | OC-B05 Steps BLK-018 | **No** | N/A | — | **BLOCKED** |
| 6 | OC-B06 Program | Partial (Lorem) | N/A | `services-program-v2` + CF-012 | READY_WITH_KNOWN_GAP |
| 7 | OC-B07 CTA (mid) | Yes | N/A | CF-011 if matches | READY |
| 8 | OC-B09 Founder quote | Partial | N/A | CF-004 | **BLOCKED** (quote body) |
| 9 | OC-B08 Infrastructure | Yes | Partial | **Unique partial** | READY_WITH_KNOWN_GAP |
| 10 | OC-B07 CTA (guest visit) | Yes | N/A | CF-011 program-cta-band | READY |
| 11 | OC-B11 Specialists | Yes | Reuse | CF-005 | READY |
| 12 | OC-B12 Reviews | Yes | Reuse | CF-007 | READY |
| 13 | OC-B13 Final form | Yes | N/A | CF-009 (not CF-008 faq) | READY |
| — | OC-B10 Comfort mobile | Probable | Pending | CF-006 pattern | READY_WITH_KNOWN_GAP |
| — | Footer | Inherited | Inherited | layout footer | READY |

## Removed from composition

- OC-B05 steps (not in Spig_v1.2 O-Centre)
- OC-B13 faq accordion (superseded by final form decision)
- `home-gallery`, `home-staff-photo` (prior charter rejection unchanged)

## Block count

**12 implementable sections + footer** (was 13 with steps/FAQ accordion).
