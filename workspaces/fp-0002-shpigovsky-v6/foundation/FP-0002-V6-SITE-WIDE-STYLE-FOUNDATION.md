# FP-0002 V6 Site-Wide Style Foundation

**Project:** FP-0002 Shpigovsky V6 CLEAN ROOM  
**Template:** [site-wide-style-foundation-contract-v1.md](../../../projects/mars-website-factory/site-wide-style-foundation-contract-v1.md)  
**Status:** PROPOSAL — `REQUIRES OPERATOR APPROVAL`  
**Review:** Operator review preparation 2026-06-22

```text
foundation_status: PROPOSAL
site_wide_style_foundation_approved: false
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
| Approval sheet | [FP-0002-V6-STYLE-FOUNDATION-APPROVAL-SHEET.md](FP-0002-V6-STYLE-FOUNDATION-APPROVAL-SHEET.md) |
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

### Operator-authorized production container

| Token | Value | Classification | Status |
|-------|-------|----------------|--------|
| `container-main` | **max-width: 1220px** | APPROVED_OPERATOR_RULE | Active — V6 zero-skeleton authorization |
| `container-padding-inline-desktop` | **50px** | APPROVED_OPERATOR_RULE | PROPOSAL — factory container convention |

### JPG observed content band (not CSS)

| Field | Value | Classification |
|-------|-------|----------------|
| Median content band | ~**1138px** | OBSERVED_JPG_VALUE — **NOT CSS CONTAINER** |

### Container bindings

| Token / role | Binding | Status |
|--------------|---------|--------|
| `container-viewport` | 100% / full-bleed layer | ACTIVE |
| `container-main` | max-width **1220px**, centered | APPROVED_OPERATOR_RULE |
| `container-narrow` | Quote / form side panels — per-block spec | PARTIAL |
| `container-bleed-media` | SECTION-003, 004 landscape, hero photo | ACTIVE |
| `container-exception-contact` | SECTION-010 split band | EXCEPTION |

**Rules:**

1. Production CSS uses **1220px** — not 1138px.
2. Inner content groups narrower than 1220px remain valid — do not stretch every block to full container width.
3. JPG side inset ~(1398−1138)/2 ≈ 130px is **observed image geometry** — relationship to 1220px + 50px padding is SAFE UNKNOWN (SU-022).

---

## 5. Spacing scale

**Base scale (OL-01):** gap `5·10·20·30·40·50·70`; padding/margin `5·10·15·20·25·30·40·50·70·90`

| Token | Value | Property class | Rhythm / role | Approval |
|-------|-------|----------------|---------------|----------|
| `section-padding-compact` | 40px | padding | compact sections | PROPOSAL |
| `section-padding-standard` | 50px | padding | standard sections | PROPOSAL |
| `section-padding-large` | 70px | padding | large / band approach | PROPOSAL |
| `section-gap-same-bg` | 30px | padding (single boundary) | same-wash continuation | PROPOSAL |
| `section-gap-band-inner` | 70px | padding | feature / diff-bg band | PROPOSAL |
| `heading-content-gap` | 30px | margin | H2 → content | PROPOSAL |
| `text-stack-gap` | 20px | margin | paragraph stacks | PROPOSAL |
| `grid-gap-standard` | 30px | gap | 3×2 card grids | PROPOSAL |
| `grid-gap-3col` | 30px | gap | 3-col rows | PROPOSAL |
| `card-padding-standard` | 25px | padding | card internal | PROPOSAL |
| `accordion-row-spacing` | 15px | **margin** | accordion rows | PROPOSAL |
| `form-field-gap` | 20px | gap | form fields | PROPOSAL |
| `footer-column-gap` | 30px | gap | footer columns | PROPOSAL |

**Removed:** `accordion-row-gap` — OL-01 gap-scale violation; replaced by `accordion-row-spacing` (margin).

**Same-bg rule:** [frontend-section-spacing-rule-v1.md](../../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md) §2.1 — single boundary only.

---

## 6. Section rhythm

| Class | Cadence tier | Token(s) | Typical sections |
|-------|--------------|----------|------------------|
| `compact` | S | `section-padding-compact` 40px | SECTION-008, SECTION-011 |
| `standard` | M | `section-padding-standard` 50px | SECTION-002, 004–007, 009 |
| `large` | L | `section-padding-large` 70px | Pre/post full-bleed transitions |
| `feature` | L–XL | `section-gap-band-inner` 70px | CTA banner, band inner gaps |
| `hero` | XL | EX-002 composite 904px | SECTION-001 outer boundary only |
| `custom-exception` | — | EX-003 | SECTION-010 contact |

Same-wash internal groups: `section-gap-same-bg` 30px.

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
| navigation | SAFE UNKNOWN | SAFE UNKNOWN | — | +4px | primary-text | HOLD |

**Site-wide tokens:** none approved. **Block exceptions:** required per Block Specification.

---

## 8. Color roles

| Role | Evidence family | HEX in foundation |
|------|-----------------|-------------------|
| page-background | light blue wash #e6eff6 family | VALUE PENDING / SAFE UNKNOWN |
| surface | white cards | VALUE PENDING / SAFE UNKNOWN |
| primary-text | dark on light | VALUE PENDING / SAFE UNKNOWN |
| secondary-text | muted body | VALUE PENDING / SAFE UNKNOWN |
| accent | red CTA | VALUE PENDING / SAFE UNKNOWN |
| inverse | white on dark overlay/CTA | VALUE PENDING / SAFE UNKNOWN |
| border | accordion / panels | VALUE PENDING / SAFE UNKNOWN |
| muted | footer secondary | VALUE PENDING / SAFE UNKNOWN |
| interactive | links, buttons | VALUE PENDING / SAFE UNKNOWN |

Implementers must not invent HEX.

---

## 9. Radius system

| Token | Proposed | Status |
|-------|----------|--------|
| `radius-button` | 5px | PROPOSAL |
| `radius-card` | SAFE UNKNOWN | HOLD |
| `radius-hero-panel` | SAFE UNKNOWN | HOLD |
| `radius-field` | SAFE UNKNOWN | HOLD |
| `radius-image` | SAFE UNKNOWN | HOLD |

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
| FAM-BTN-PRIMARY | `button-height-standard` 30px, `radius-button` 5px, colors SAFE UNKNOWN | PROPOSAL partial |
| FAM-BTN-HEADER | SAFE UNKNOWN | HOLD |

One primary button family observed (CMP-001 ×8). Height 30px = normalized lower bound of 30–37px observed range.

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

- Accordion: `accordion-row-spacing` 15px margin
- Program rows: SAFE UNKNOWN
- Numbered steps CMP-010: SAFE UNKNOWN

---

## 18. Responsive rules

**Desktop-first** from JPG 1398px width. Mobile: **SAFE UNKNOWN** — separate audit required.

---

## 19. Allowed exceptions

| ID | Value | Classification | Reason |
|----|-------|----------------|--------|
| EX-002 | SECTION-001 total 904px height | BLOCK_LEVEL_EXCEPTION | CONFIRMED major boundary Y=904 |
| EX-003 | SECTION-010 contact band | BLOCK_LEVEL_EXCEPTION | Split panel — block spec |

### Observed estimates — NOT for CSS

| Item | Value | Status |
|------|-------|--------|
| Header bar Y end estimate | ~174px | OBSERVED_JPG_ESTIMATE — CSS forbidden |
| JPG content band width | ~1138px | OBSERVED — not max-width |

**Removed:** EX-001 header 174px implementation exception — unproven exact boundary.

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
site_wide_style_foundation_approved: false
implementation_authorized: false
header_implementation_authorized: false
scss_authorized: false
html_structure_authorized: false
```

**Machine-readable:** [FP-0002-V6-STYLE-FOUNDATION.json](FP-0002-V6-STYLE-FOUNDATION.json)

---

## Local styling prohibition

Until approval: **no block-level invented spacing, typography, container max-width, or hex** outside this foundation and exception register.
