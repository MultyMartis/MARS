# FP-0002 V8 O-Centre Reconciled Composition v1

**Task:** Content blocker resolution
**Date:** 2026-06-29
**Authority:** Spig_v1.2.fig + resolution pack + this reconciliation

| Final order | Block ID | Block | Present | Content status | Asset status | Reuse source | Implementation status |
|---:|---|---:|---|---|---|---|---|
| 1 | OC-B01 | Hero | Yes | CONFIRMED | PASS | `services-inner-hero-v2.html` + o-centre hero | READY |
| 2 | OC-B02 | Subnav | Yes | CONFIRMED | N/A | CF-003 `internal-page-nav.html` | READY |
| 3 | OC-B03 | Institutional narrative | Yes | CONFIRMED (typo preserved) | N/A | Unique partial | READY |
| 4 | OC-B04 | Who we treat | Yes | CONFIRMED | N/A | `services-category-section-v2` modifier | READY |
| 5 | OC-B06 | Program + approach | Yes | CONFIRMED (Lorem omitted) | N/A | CF-012 + `services-program-v2.html` | READY |
| 6 | OC-B07 | Mid CTA | Yes | CONFIRMED | N/A | CF-011 | READY |
| 7 | OC-B09 | Founder quote | Yes | CONFIRMED (CF-004 reuse) | N/A | CF-004 `founder-quote.html` | READY |
| 8 | OC-B08 | Infrastructure | Yes | CONFIRMED | PASS | Unique partial + 20 WebP | READY |
| 9 | OC-B07b | Guest visit CTA | Yes | CONFIRMED | N/A | CF-011 program-cta-band | READY |
| 10 | OC-B11 | Specialists | Yes | REUSE | REUSE | CF-005 | READY |
| 11 | OC-B12 | Reviews | Yes | REUSE | REUSE | CF-007 | READY |
| 12 | OC-B13 | Final form | Yes | CONFIRMED | N/A | CF-009 (not CF-008 accordion) | READY |
| — | OC-B10 | Comfort (mobile) | Probable | REUSE | REUSE | CF-006 pattern | READY_WITH_KNOWN_GAP |
| — | — | Footer | Yes | INHERITED | INHERITED | layout footer | READY |

## Removed / excluded (unchanged)

| Item | Reason |
|---|---|
| **OC-B05 / BLK-018 Steps** | **NOT in canonical Figma** — inventory label error |
| OC-B13 faq accordion | Resolved — final form only |
| `home-gallery` | Charter rejection |
| `home-staff-photo` | Charter rejection |

## Block count

| Metric | Value |
|---|---:|
| Previous anatomy count (with phantom steps) | 13 |
| **Final implementable sections** | **12** |
| Removed phantom blocks | 1 (OC-B05) |

**Pack location:** `audits/o-centre-content-blocker-resolution/` (this file supersedes pre-resolution composition for content gate).
