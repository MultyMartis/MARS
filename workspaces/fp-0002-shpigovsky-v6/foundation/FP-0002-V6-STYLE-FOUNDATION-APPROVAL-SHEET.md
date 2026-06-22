# FP-0002 V6 SITE-WIDE STYLE FOUNDATION — APPROVAL SHEET

**Project:** FP-0002 Shpigovsky V6  
**Date:** 2026-06-22  
**Visual authority:** `HOME-PAGE-FULL-MOCKUP.jpg` SHA-256 `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290`  
**Foundation status:** PROPOSAL  
**Review verdict:** READY FOR OPERATOR APPROVAL (internal consistency)

---

## A. Ready for approval

Items with sufficient evidence chain and no unresolved internal contradiction.

| Item | Value | Source | Confidence |
|------|-------|--------|------------|
| `container-main` max-width | **1220px** | APPROVED_OPERATOR_RULE — V6 zero skeleton | HIGH |
| OL-01 spacing scale as normalization basis | gap 5/10/20/30/40/50/70; padding/margin 5/10/15/20/25/30/40/50/70/90 | Factory OL-01 | HIGH |
| JPG content band (informational) | ~1138px median | OBSERVED_JPG_VALUE | MEDIUM |
| SECTION-001 outer height exception | 904px | CONFIRMED_SECTION_BOUNDARY Y=904 | HIGH |
| Section rhythm family split | compact / standard / large / feature / hero / custom | Extraction + normalization | MEDIUM |
| `accordion-row-spacing` 15px as margin | replaces invalid gap token | OL-01 compliance fix | MEDIUM |
| Header/Hero Y=174 demotion | observed estimate only; CSS forbidden | Grounding review SU-001 | HIGH |
| Single primary button family | FAM-BTN-PRIMARY CMP-001 ×8 | Component map | MEDIUM |
| Color roles (no HEX) | 9 roles identified | JPG family scans | MEDIUM |
| Foundation gate flags | all implementation locks false | Pipeline contract | HIGH |

---

## B. Requires revision (resolved in this review)

| Issue | Prior state | Resolution |
|-------|-------------|------------|
| Container contradiction | 1138px held as SAFE UNKNOWN; 1220px rejected as legacy | **1220px** = APPROVED_OPERATOR_RULE; **1138px** = OBSERVED only |
| Header Y=174 contradiction | EX-001 implementation exception while SU-001 SAFE UNKNOWN | EX-001 **removed**; 174px = OBSERVED_ESTIMATE; CSS forbidden |
| `accordion-row-gap: 15px` | Named as gap — OL-01 violation | Renamed `accordion-row-spacing`; property class **margin** |
| Single `section-padding-standard: 50px` | Collapsed 40–80px range | Split: compact 40 / standard 50 / large 70 |
| `button-height-primary` | Ambiguous naming | Renamed `button-height-standard` |

---

## C. Requires operator choice

| ID | Decision | Options | Recommendation |
|----|----------|---------|----------------|
| OC-01 | Approve `foundation_status: PROPOSAL` → `APPROVED` for spacing + container tokens | Approve all §F tokens / Approve partial / Revise | Approve §F spacing + container; defer typography/colors |
| OC-02 | Header/Hero architecture (SU-001) | Composite SECTION-001 single spec / Split header+hero blocks | Composite until split Y proven |
| OC-03 | `button-height-standard` | 30px / 32px / 35px | 30px (lower normalized bound) — confirm visually at Header block QA |
| OC-04 | `container-padding-inline-desktop` | 50px / other OL-01 value | 50px per factory convention |
| OC-05 | CMP-004 vs CMP-008 (SU-003) | One card component / Two families | Defer — block specs can share tokens either way |
| OC-06 | LOW-confidence tokens | Approve as-is / Revise values | See §F rows marked LOW |

---

## D. Deferred to Block Specification

| Area | Reason |
|------|--------|
| Typography px per role | JPG insufficient — exact sizes at block spec |
| All color HEX values | JPEG variance — operator brand samples or block extraction |
| `radius-card`, `radius-hero-panel` | Not stable across families |
| SECTION-010 contact band geometry | EX-003 custom-exception |
| Header internal layout (logo, nav, contacts) | Requires SECTION-001 spec after Gate 1 |
| Hero overlay panel exact radius/position | CMP-003 block spec |
| Program rows CMP-012 spacing | Not normalized |
| Numbered steps CMP-010 spacing | Not normalized |
| Review carousel CMP-009 | Layout SAFE UNKNOWN |
| Mobile responsive spacing | No mobile JPG |

---

## E. SAFE UNKNOWN

| ID | Item |
|----|------|
| SU-001 | Exact Header/Hero Y split |
| SU-002 | Hero as separate block vs composite |
| SU-003 | CMP-004 vs CMP-008 identity |
| SU-007–009 | Typography family/sizes/mobile |
| SU-010–012 | Color HEX |
| SU-013–018 | Interaction + responsive |
| SU-021 | Header bar exact height |
| SU-022 | JPG 130px inset vs 50px container padding |
| SU-023 | Button height upper bound (37px observed) |

---

## F. Proposed final tokens

| Token | Purpose | Value | Property class | Source | Status |
| ----- | ------- | ----- | -------------- | ------ | ------ |
| `container-main` | Production max-width | 1220px | max-width | APPROVED_OPERATOR_RULE | APPROVE |
| `container-padding-inline-desktop` | Viewport side padding | 50px | padding-inline | APPROVED_OPERATOR_RULE | PROPOSE |
| `section-padding-compact` | Short section bands | 40px | padding | NORMALIZED_PROPOSAL | PROPOSE |
| `section-padding-standard` | Default section bands | 50px | padding | NORMALIZED_PROPOSAL | PROPOSE |
| `section-padding-large` | Band approach / reset | 70px | padding | NORMALIZED_PROPOSAL | PROPOSE |
| `section-gap-same-bg` | Same-wash continuation | 30px | padding | NORMALIZED_PROPOSAL | PROPOSE |
| `section-gap-band-inner` | Feature / diff-bg band | 70px | padding | NORMALIZED_PROPOSAL | PROPOSE |
| `heading-content-gap` | H2 to content | 30px | margin | NORMALIZED_PROPOSAL | PROPOSE |
| `text-stack-gap` | Paragraph stacks | 20px | margin | NORMALIZED_PROPOSAL | PROPOSE |
| `grid-gap-standard` | 3×2 card grids | 30px | gap | NORMALIZED_PROPOSAL | PROPOSE |
| `grid-gap-3col` | 3-col card rows | 30px | gap | NORMALIZED_PROPOSAL | PROPOSE |
| `card-padding-standard` | Card internal | 25px | padding | NORMALIZED_PROPOSAL | PROPOSE |
| `accordion-row-spacing` | Accordion rows | 15px | margin | NORMALIZED_PROPOSAL | PROPOSE |
| `button-height-standard` | Primary CTA height | 30px | height | NORMALIZED_PROPOSAL | PROPOSE |
| `radius-button` | Primary CTA radius | 5px | border-radius | NORMALIZED_PROPOSAL | PROPOSE |
| `form-field-gap` | Form vertical rhythm | 20px | gap | NORMALIZED_PROPOSAL | PROPOSE |
| `footer-column-gap` | Footer columns | 30px | gap | NORMALIZED_PROPOSAL | PROPOSE |

### Observed only — not tokens

| Item | Value | Status |
|------|-------|--------|
| JPG content band width | ~1138px | OBSERVED — NOT CSS |
| Header bar Y end estimate | ~174px | OBSERVED — CSS FORBIDDEN |

### Exceptions

| ID | Token | Value | Status |
|----|-------|-------|--------|
| EX-002 | `hero-band-height-desktop` | 904px | PROPOSE |
| EX-003 | `section-contact-band` | block spec | PROPOSE |

---

## G. Explicit operator decisions required

1. **Gate 2 — Foundation approval:** Confirm `foundation_status: APPROVED` for §F spacing + container tokens (yes/no/partial list).

2. **Gate 1 — SECTION-001 architecture:** Implement Header+Hero as one composite block spec, or require separate specs with operator-provided Y split (composite / split).

3. **Button height:** Confirm `button-height-standard: 30px` or specify alternative OL-adjacent value (30 / 32 / 35).

4. **Container padding:** Confirm `container-padding-inline-desktop: 50px` (yes / revise to: ___).

5. **LOW-confidence spacing:** Approve `section-gap-band-inner` 70px, `text-stack-gap` 20px, `card-padding-standard` 25px, `footer-column-gap` 30px as proposed (yes / revise).

---

## H. Implementation gate status

```text
site_wide_style_foundation_approved: false
implementation_authorized: false
header_implementation_authorized: false
html_structure_authorized: false
scss_authorized: false
```

---

## Phase 1 — Full token traceability

| Token | JPG evidence | Observed range | Normalized value | OL-01 compliant | Confidence | Verdict |
| ----- | ------------ | -------------- | ---------------- | --------------- | ---------- | ------- |
| `container-main` | Operator V6 rule | N/A | 1220px | N/A (max-width) | HIGH | APPROVE |
| `container-padding-inline-desktop` | Factory convention | N/A | 50px | Yes (padding) | MEDIUM | PROPOSE |
| `section-padding-compact` | SECTION-008, 011 | ~40–50px | 40px | Yes | MEDIUM | PROPOSE |
| `section-padding-standard` | SECTION-002+ light | ~40–80px | 50px | Yes | MEDIUM | PROPOSE |
| `section-padding-large` | Bleed transitions | ~60–80px | 70px | Yes | LOW | PROPOSE |
| `section-gap-same-bg` | SECTION-002 groups | ~20–40px | 30px | Yes | MEDIUM | PROPOSE |
| `section-gap-band-inner` | Band transitions | major gap | 70px | Yes | LOW | PROPOSE |
| `heading-content-gap` | REPEAT-005 | ~20–40px | 30px | Yes (margin) | MEDIUM | PROPOSE |
| `text-stack-gap` | Body stacks | ~15–25px | 20px | Yes (margin) | LOW | PROPOSE |
| `grid-gap-standard` | CMP-004, 008 | ~25–35px | 30px | Yes (gap) | MEDIUM | PROPOSE |
| `grid-gap-3col` | CMP-016, 017 | ~25–35px | 30px | Yes (gap) | MEDIUM | PROPOSE |
| `card-padding-standard` | Cards | ~20–30px | 25px | Yes | LOW | PROPOSE |
| `accordion-row-spacing` | CMP-006 | ~10–20px | 15px margin | Yes | MEDIUM | PROPOSE |
| `button-height-standard` | CMP-001 | ~30–37px | 30px | N/A geometry | MEDIUM | PROPOSE |
| `radius-button` | CMP-001 | ~4–6px | 5px | N/A | LOW | PROPOSE |
| `form-field-gap` | CMP-019 | ~15–25px | 20px | Yes (gap) | LOW | PROPOSE |
| `footer-column-gap` | CMP-020 | ~20–40px | 30px | Yes (gap) | LOW | PROPOSE |

---

## Phase 11 — Foundation completeness matrix

| Foundation area | Status | Approved now | Requires block spec | Blocks implementation |
| --------------- | ------ | ------------ | ------------------- | --------------------- |
| container | PARTIAL | 1220px operator rule | narrow groups, inset math | No — sufficient for gate |
| spacing | PROPOSED | OL-01 scale + tokens §F | program/step gaps | No |
| section rhythm | PROPOSED | 3 padding families | SECTION-010 exception | No |
| typography | SAFE UNKNOWN | — | all roles | Yes for typed blocks |
| colors | SAFE UNKNOWN | roles only | all HEX | Yes for colored blocks |
| radius | PARTIAL | button 5px | card, hero, field | Partial |
| borders | SAFE UNKNOWN | — | accordion separators | Partial |
| buttons | PROPOSED | height + radius | colors, header variant | Partial |
| forms | PARTIAL | field gap | validation, labels | Partial |
| cards | PROPOSED | padding + grid gap | CMP-004/008 identity | No |
| images | OBSERVED | bleed patterns | per-component crop | No |
| grids | PROPOSED | 4 patterns | mosaic irregular | No |
| responsive | SAFE UNKNOWN | — | mobile audit | Yes for mobile |
| exceptions | PROPOSED | EX-002, EX-003 | — | No |

---

## Review sign-off (operator)

| Field | Value |
|-------|-------|
| Reviewed by | _________________ |
| Date | _________________ |
| Decision | APPROVE / PARTIAL / REVISE |
| Notes | |
