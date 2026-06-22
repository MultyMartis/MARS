# FP-0002 V6 Production Pipeline

**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Factory pipeline:** [frontend-implementation-pipeline-v1.md](../../../projects/mars-website-factory/frontend-implementation-pipeline-v1.md)  
**Current state:** Foundation APPROVED; SECTION-001 implemented; SECTION-002 variable-first pilot **PARTIAL · ASSET REQUIRED**

---

## SECTION-002 pilot (2026-06-22)

| Field | Value |
|-------|-------|
| Semantic name | `intro-programs` |
| Status | PARTIAL · ASSET REQUIRED (founder portrait, 4 clinical photos) |
| Variable-first pilot | **COMPLETE** (gates: arbitrary 0, hidden fallback 0) |
| Spec | `specifications/section-002/` |
| Review | `reviews/section-002/` |

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

## Gate 4 — Header HTML only

| Field | Value |
|-------|-------|
| **Status** | **LOCKED** — `header_implementation_authorized: false` |

---

## Gate 5 — Header HTML review

| Field | Value |
|-------|-------|
| **Status** | **LOCKED** |

---

## Gate 6 — Header SCSS

| Field | Value |
|-------|-------|
| **Status** | **LOCKED** — `scss_authorized: false` |

---

## Gate 7 — Header screenshot QA

| Field | Value |
|-------|-------|
| **Status** | **LOCKED** |

---

## Gate 8 — Hero specification

| Field | Value |
|-------|-------|
| **Status** | **MERGED into SECTION-001 composite spec** — not a separate major section |

---

## Authorization summary

```text
site_wide_style_foundation_approved: true
foundation_approved_by: operator
implementation_authorized: false
header_implementation_authorized: false
hero_implementation_authorized: false
section_001_specification_status: READY_FOR_OPERATOR_REVIEW
html_structure_authorized: false
scss_authorized: false
```

**HTML / SCSS / JS remain NOT STARTED** in `src/pages/index.html` skeleton.
