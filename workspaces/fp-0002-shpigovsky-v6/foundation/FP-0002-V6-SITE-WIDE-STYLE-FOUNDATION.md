# FP-0002 V6 Site-Wide Style Foundation

**Project:** FP-0002 Shpigovsky V6 CLEAN ROOM  
**Template:** [site-wide-style-foundation-contract-v1.md](../../../projects/mars-website-factory/site-wide-style-foundation-contract-v1.md)  
**Status:** PROPOSAL — `REQUIRES OPERATOR APPROVAL`

```text
foundation_status: PROPOSAL
implementation_authorized: false
header_implementation_authorized: false
```

---

## 1. Source authority

| Field | Value |
|-------|-------|
| JPG | `HOME-PAGE-FULL-MOCKUP.jpg` SHA-256 `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |
| Extraction | [FP-0002-V6-DESIGN-FOUNDATION-EXTRACTION.md](FP-0002-V6-DESIGN-FOUNDATION-EXTRACTION.md) |
| Normalization | [FP-0002-V6-PRACTICAL-VALUE-NORMALIZATION.md](FP-0002-V6-PRACTICAL-VALUE-NORMALIZATION.md) |
| Grounding verdict | **PARTIAL** |
| Forbidden | FIG, PDF, v1–v5, v3 Production Standards px |

---

## 2. Foundation scope

- **In scope:** Home page desktop patterns from JPG; 11 grounded sections; 20 component families
- **Out of scope:** Mobile/tablet responsive values; Header/Hero internal split; exact HEX; font files
- **Deferred:** Inner pages until Home foundation approved

---

## 3. Evidence inputs

Listed in extraction + normalization documents. Factory OL-01 applies unless this foundation is operator-approved as project rank-1 SSOT.

---

## 4. Container system

| Token / role | Binding | Status |
|--------------|---------|--------|
| `container-viewport` | 100% / full-bleed layer | ACTIVE |
| `container-main` | Repeated ~1138px content — **max-width SAFE UNKNOWN** | HOLD |
| `container-narrow` | Quote / form side panels — per-block spec | PARTIAL |
| `container-bleed-media` | SECTION-003, 004 landscape, hero photo | ACTIVE |
| `container-exception-contact` | SECTION-010 split band | EXCEPTION |

**Rule:** Implementers use bindings from Block Implementation Specification — not legacy 1220px.

---

## 5. Spacing scale

**Base scale (OL-01):** gap `5·10·20·30·40·50·70`; padding/margin `5·10·15·20·25·30·40·50·70·90`

| Token | Proposed value | Rhythm class | Approval |
|-------|----------------|--------------|----------|
| `section-padding-standard` | 50px | standard | PROPOSAL |
| `section-gap-same-bg` | 30px | compact continuation | PROPOSAL |
| `section-gap-band-inner` | 70px | feature / band | PROPOSAL |
| `heading-content-gap` | 30px | text | PROPOSAL |
| `text-stack-gap` | 20px | text | PROPOSAL |
| `grid-gap-standard` | 30px | layout | PROPOSAL |
| `grid-gap-3col` | 30px | layout | PROPOSAL |
| `card-padding-standard` | 25px | component | PROPOSAL |
| `accordion-row-gap` | 15px | component | PROPOSAL |
| `form-field-gap` | 20px | form | PROPOSAL |
| `footer-column-gap` | 30px | footer | PROPOSAL |

**Same-bg rule:** [frontend-section-spacing-rule-v1.md](../../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md) §2.1 — single boundary only.

---

## 6. Section rhythm

| Class | Cadence tier | Proposed token | Typical sections |
|-------|--------------|----------------|------------------|
| `compact` | S | `section-gap-same-bg` 30px | Internal groups in SECTION-002 |
| `standard` | M | `section-padding-standard` 50px | Most light page bands |
| `large` | L | 70px band | Pre/post full-width photo |
| `feature` | L–XL | `section-gap-band-inner` | CTA banner CONTEXT |
| `hero` | XL | exception SECTION-001 | First screen composite |
| `custom-exception` | — | per register | SECTION-010 contact |

---

## 7. Typography hierarchy

| Role | Desktop | Mobile | Weight | Line-height | Color role | Status |
|------|---------|--------|--------|-------------|------------|--------|
| display | SAFE UNKNOWN | SAFE UNKNOWN | — | +4px rule | inverse-on-dark | HOLD |
| H1 | SAFE UNKNOWN | SAFE UNKNOWN | — | +4px | primary-text | HOLD |
| H2 | SAFE UNKNOWN | SAFE UNKNOWN | — | +4px | primary-text | HOLD |
| H3 | SAFE UNKNOWN | SAFE UNKNOWN | — | +4px | primary-text | HOLD |
| body-large | SAFE UNKNOWN | SAFE UNKNOWN | — | +4px | primary-text | HOLD |
| body | SAFE UNKNOWN | SAFE UNKNOWN | — | +4px | primary-text | HOLD |
| small | SAFE UNKNOWN | SAFE UNKNOWN | — | +4px | secondary-text | HOLD |
| label | SAFE UNKNOWN | SAFE UNKNOWN | — | +4px | secondary-text | HOLD |
| button | SAFE UNKNOWN | SAFE UNKNOWN | — | +4px | inverse | HOLD |

---

## 8. Color roles

| Role | Evidence family | HEX in foundation |
|------|-----------------|-------------------|
| page-background | light blue wash #e6eff6 family | **SAFE UNKNOWN** |
| surface | white cards | **SAFE UNKNOWN** |
| primary-text | dark on light | **SAFE UNKNOWN** |
| secondary-text | muted body | **SAFE UNKNOWN** |
| accent | red CTA | **SAFE UNKNOWN** |
| inverse | white on dark overlay/CTA | **SAFE UNKNOWN** |
| border | accordion / panels | **SAFE UNKNOWN** |
| muted | footer secondary | **SAFE UNKNOWN** |
| interactive | links, buttons | **SAFE UNKNOWN** |

---

## 9. Radius system

| Token | Proposed | Status |
|-------|----------|--------|
| `radius-button` | 5px | PROPOSAL |
| `radius-card` | SAFE UNKNOWN | HOLD |
| `radius-hero-panel` | SAFE UNKNOWN | HOLD |

---

## 10. Border system

Accordion rows — subtle horizontal separators; exact width/color SAFE UNKNOWN.

---

## 11. Shadow system

Cards — minimal or none on JPG; **SAFE UNKNOWN** default none until evidenced.

---

## 12. Button system

| Family | Token bindings | Status |
|--------|----------------|--------|
| `btn-primary` | CMP-001 — height 30px, radius 5px, colors SAFE UNKNOWN | PROPOSAL partial |
| `btn-in-header` | SAFE UNKNOWN | HOLD |

---

## 13. Form system

CMP-019 — field gap 20px proposal; validation colors SAFE UNKNOWN.

---

## 14. Card system

| Family | Components | Grid | Gap token |
|--------|------------|------|-----------|
| `card-service-6` | CMP-004 | 3×2 | `grid-gap-standard` |
| `card-benefit-6` | CMP-008 | 3×2 | `grid-gap-standard` |
| `card-specialist-3` | CMP-016 | 3×1 | `grid-gap-3col` |
| `card-article-3` | CMP-017 | 3×1 | `grid-gap-3col` |
| `card-review` | CMP-009 | 2 + dots | SAFE UNKNOWN |

---

## 15. Image behavior

- Hero: full-width background + overlay panel (CMP-003)
- Staff photo: full-bleed SECTION-003
- Clinical squares: 4-up row CMP-007
- Mosaic: non-uniform CMP-014

---

## 16. Grid and column rules

| Pattern ID | Columns | Evidence |
|------------|---------|----------|
| `grid-3x2-cards` | 3×2 | CMP-004, CMP-008 |
| `grid-3col-cards` | 3 | CMP-016, CMP-017 |
| `grid-4-square-photos` | 4 | CMP-007 |
| `grid-mosaic-5` | irregular | CMP-014 |

---

## 17. Shared component rhythm

- Accordion: `accordion-row-gap` 15px
- Program rows: SAFE UNKNOWN
- Numbered steps CMP-010: SAFE UNKNOWN

---

## 18. Responsive rules

**Desktop-first** from JPG 1398px width. Mobile: **SAFE UNKNOWN** — separate audit required.

---

## 19. Allowed exceptions

| ID | Value | Reason |
|----|-------|--------|
| EX-001 | header bar ~174px height | NRM-012 geometric |
| EX-002 | SECTION-001 total 904px | NRM-014 first-screen composite |

---

## 20. SAFE UNKNOWN

See [FP-0002-V6-FOUNDATION-SAFE-UNKNOWN.md](FP-0002-V6-FOUNDATION-SAFE-UNKNOWN.md)

---

## 21. Operator approval

| Field | Value |
|-------|-------|
| `foundation_status` | **PROPOSAL** |
| `approved_by` | pending |
| `approval_date` | pending |

---

## 22. Implementation authorization

```text
implementation_authorized: false
header_implementation_authorized: false
scss_authorized: false
html_structure_authorized: false
```

**Machine-readable:** [FP-0002-V6-STYLE-FOUNDATION.json](FP-0002-V6-STYLE-FOUNDATION.json)

---

## Local styling prohibition

Until approval: **no block-level invented spacing, typography, container max-width, or hex** outside this foundation and exception register.
