# FP-0002 V6 Production Pipeline

**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Factory pipeline:** [frontend-implementation-pipeline-v1.md](../../../projects/mars-website-factory/frontend-implementation-pipeline-v1.md)  
**Current state:** Foundation APPROVED; SECTION-001 (Header + Hero) IMPLEMENTED · REVIEWED; **Footer = next authorized production target**

---

## Current production order (operator-approved)

```text
CURRENT IMPLEMENTED:
  Header
  Hero

NEXT:
  Footer

NOT STARTED:
  Main content sections (SECTION-002+)
  Responsive layout
  JavaScript interactions
  SECTION-003 and further content implementation
```

**Correction (2026-06-22):** `intro-programs` was implemented out of order and removed from active build. Variable-First foundation verified on aborted noncanonical block attempt. No canonical post-Hero content section approved. Footer remains next production target.

---

## Aborted attempt (archived — not active)

| Field | Value |
|-------|-------|
| Semantic name | `intro-programs` |
| Status | **ABORTED · NOT ACTIVE · NOT CANONICAL** |
| Archive | `archive/aborted-section-attempts/intro-programs/` |
| Reason | Violated Footer-first production order after Header/Hero |

---

## Completed gates

| Gate | Status | Artefact |
|------|--------|----------|
| G-SRC Source Authority | PASS | JPG hash + v6 purity gate |
| G-AUD Visual Audit | PASS | `audit/jpg-visual-audit/` |
| G-GRD Grounding Review | **PARTIAL** (Header/Hero split estimate only) | `review/FP-0002-V6-JPG-AUDIT-GROUNDING-REVIEW.md` |
| G-EXT Design Foundation Extraction | PASS | `foundation/FP-0002-V6-DESIGN-FOUNDATION-EXTRACTION.md` |
| G-NRM Practical Value Normalization | PASS | `foundation/FP-0002-V6-PRACTICAL-VALUE-NORMALIZATION.md` |
| G-FND Site-Wide Style Foundation | **APPROVED** | `foundation/FP-0002-V6-SITE-WIDE-STYLE-FOUNDATION.md` |
| G-FND-REV Foundation operator approval | **CLOSED** | operator 2026-06-22 |
| G-1 Grounding architecture decision | **CLOSED** | composite SECTION-001 |
| G-3 SECTION-001 specification draft | **READY FOR OPERATOR REVIEW** | `specifications/section-001/` |
| G-VF CSS Variable First Law | **VERIFIED** (mechanics on aborted attempt; law active) | `reviews/foundation/FP-0002-V6-SCSS-CLEANUP-AND-TOKEN-NORMALIZATION.md` |

---

## Gate 1 — Grounding review operator decision

| Field | Value |
|-------|-------|
| **Status** | **CLOSED** — composite SECTION-001 |
| **Decision** | Header + Hero = one major section; internal groups GROUP-01 / GROUP-02 |
| **Y=174** | OBSERVED_JPG_ESTIMATE — CSS_USE_FORBIDDEN — NOT_AN_IMPLEMENTATION_BOUNDARY |

---

## Gate 2 — Site-Wide Style Foundation operator approval

| Field | Value |
|-------|-------|
| **Status** | **CLOSED** — `foundation_status: APPROVED` |
| **Approved by** | operator |
| **Date** | 2026-06-22 |
| **Approved tokens** | container-main 1220px; section-padding compact/standard/large; grid-gap-standard; heading-content-gap; card-padding-standard; accordion-row-spacing (margin); footer-gap 30px |
| **Deferred globally** | button-height-standard; container-padding-inline-desktop; typography px; font-family; HEX; radii; header internal height; Header/Hero split coordinate |

---

## Gate 3 — SECTION-001 Header/Hero Implementation Specification

| Field | Value |
|-------|-------|
| **Required inputs** | Approved foundation; composite architecture decision |
| **Outputs** | `specifications/section-001/FP-0002-V6-SECTION-001-*` |
| **Status** | **READY FOR OPERATOR REVIEW** |
| **Note** | Specification complete; does not authorize HTML |

---

## Authorization summary

```text
site_wide_style_foundation_approved: true
foundation_approved_by: operator
section_001_status: IMPLEMENTED_REVIEWED
footer_status: NEXT_AUTHORIZED_TARGET
intro_programs_status: ABORTED_NOT_ACTIVE
main_content_implementation_status: NOT_STARTED
css_variable_first_law_status: ACTIVE
foundation_verification_status: PASSED
javascript_changed: false
responsive_layout_implemented: false
```
