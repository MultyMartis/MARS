# FP-0002 V6 Production Pipeline

**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Factory pipeline:** [frontend-implementation-pipeline-v1.md](../../../projects/mars-website-factory/frontend-implementation-pipeline-v1.md)  
**Current state:** Grounding PARTIAL; Foundation PROPOSAL; HTML/SCSS locked

---

## Completed gates

| Gate | Status | Artefact |
|------|--------|----------|
| G-SRC Source Authority | PASS | JPG hash + v6 purity gate |
| G-AUD Visual Audit | PASS | `audit/jpg-visual-audit/` |
| G-GRD Grounding Review | **PARTIAL** | `review/FP-0002-V6-JPG-AUDIT-GROUNDING-REVIEW.md` |
| G-EXT Design Foundation Extraction | PASS (proposal) | `foundation/FP-0002-V6-DESIGN-FOUNDATION-EXTRACTION.md` |
| G-NRM Practical Value Normalization | PASS (proposal) | `foundation/FP-0002-V6-PRACTICAL-VALUE-NORMALIZATION.md` |
| G-FND Site-Wide Style Foundation | **PROPOSAL** | `foundation/FP-0002-V6-SITE-WIDE-STYLE-FOUNDATION.md` |

---

## Gate 1 — Grounding review operator decision

| Field | Value |
|-------|-------|
| **Required inputs** | Grounding review, grounded structure JSON |
| **Outputs** | PASS / PARTIAL / FAIL verdict; Header/Hero decision |
| **Forbidden** | HTML, SCSS, Header block spec |
| **Approval** | Operator |
| **Status** | **PARTIAL — awaiting decision on SU-001** |
| **Rollback** | Re-open audit segmentation only with new evidence |

---

## Gate 2 — Site-Wide Style Foundation operator approval

| Field | Value |
|-------|-------|
| **Required inputs** | Foundation MD + JSON + normalization table |
| **Outputs** | `foundation_status: APPROVED` or revised PROPOSAL |
| **Forbidden** | Block HTML/SCSS; promoting v3 standards px |
| **Approval** | Operator (Андрей) |
| **Status** | **BLOCKED on Gate 1 clarity for SECTION-001** (may approve non-header tokens in scoped PARTIAL) |
| **Rollback** | Re-run normalization from extraction |

---

## Gate 3 — SECTION-001 Header/Hero Implementation Specification

| Field | Value |
|-------|-------|
| **Required inputs** | Approved foundation (or scoped waiver); grounding Header/Hero decision; Group Decomposition; Layout Spec |
| **Outputs** | `FP-0002-V6-SPEC-SECTION-001-HEADER.md` (and hero if split) |
| **Forbidden** | HTML until spec approved |
| **Approval** | Operator |
| **Status** | **NOT STARTED** — `header_implementation_authorized: false` |
| **Rollback** | Foundation or grounding |

---

## Gate 4 — Header HTML only

| Field | Value |
|-------|-------|
| **Required inputs** | Approved block spec; `html_structure_authorized: true` |
| **Outputs** | Header partial structure only |
| **Forbidden** | SCSS; hero unless spec includes |
| **Status** | **LOCKED** |

---

## Gate 5 — Header HTML review

| Field | Value |
|-------|-------|
| **Required inputs** | Header HTML |
| **Outputs** | HTML review PASS |
| **Forbidden** | SCSS |
| **Status** | **LOCKED** |

---

## Gate 6 — Header SCSS

| Field | Value |
|-------|-------|
| **Required inputs** | HTML review PASS; foundation tokens; [frontend-pre-scss-validation-checklist-v1.md](../../../projects/mars-website-factory/frontend-pre-scss-validation-checklist-v1.md) |
| **Outputs** | Header SCSS bound to tokens |
| **Forbidden** | Arbitrary px |
| **Status** | **LOCKED** |

---

## Gate 7 — Header screenshot QA

| Field | Value |
|-------|-------|
| **Required inputs** | Build + JPG crop compare |
| **Outputs** | QA report + OPERATOR VISUAL REVIEW |
| **Status** | **LOCKED** |

---

## Gate 8 — Hero specification

| Field | Value |
|-------|-------|
| **Required inputs** | Gate 1 Header/Hero boundary decision; foundation |
| **Outputs** | Hero block spec (or combined SECTION-001 spec) |
| **Forbidden** | Hero HTML if boundary SAFE UNKNOWN unresolved |
| **Status** | **BLOCKED on SU-001** |

---

## Subsequent sections (summary)

| Section | Block spec gate | After foundation APPROVED |
|---------|-----------------|---------------------------|
| SECTION-002 … SECTION-011 | One spec per major section or internal group batch | Sequential: spec → HTML → review → SCSS → QA |

**Order recommendation:** SECTION-002 intro grid after SECTION-001 complete; full-bleed SECTION-003 as separate spec.

---

## Correction loop routing

| Defect class | Fix in |
|--------------|--------|
| Wrong px in CSS | Block spec or foundation token — not ad-hoc patch |
| Wrong section boundary | Grounding review / audit |
| Wrong component family | Extraction + component map |
| Missing token | Normalization + foundation approval |

---

## Authorization summary

```text
implementation_authorized: false
header_implementation_authorized: false
html_structure_authorized: false
scss_authorized: false
```

**HTML / SCSS / JS remain NOT STARTED** in `src/pages/index.html` skeleton.
