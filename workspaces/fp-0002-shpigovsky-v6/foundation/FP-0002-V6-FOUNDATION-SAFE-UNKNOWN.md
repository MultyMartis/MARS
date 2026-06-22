# FP-0002 V6 Foundation — SAFE UNKNOWN

**Purpose:** Items that must not be invented during implementation. Route to operator or future audit.

---

## Structural / grounding

| ID | Unknown | Why | Needed from operator |
|----|---------|-----|----------------------|
| SU-001 | Exact Y boundary between header bar and hero within SECTION-001 | Header overlays hero; no reliable major boundary on JPG | Approve split Y or keep composite SECTION-001 spec |
| SU-002 | Whether hero is separate implementation block from header | Grounding keeps one major section | Architecture decision for block specs |
| SU-003 | CMP-004 vs CMP-008 — one card component or two | Visually similar (REPEAT-001) not proven identical | Component taxonomy decision |

---

## Layout / container

| ID | Unknown | Why | Needed |
|----|---------|-----|--------|
| SU-004 | Universal `container-main` max-width | Median 1138px not universal; full-bleed rows differ | Approve max-width token or per-section rules |
| SU-005 | Side inset ~130px — padding vs margin vs grid | Derived from median X | Container model decision |
| SU-006 | Relationship 1138px JPG vs any CSS max-width | Audit JSON lists as unknown | Explicit production width |

---

## Typography

| ID | Unknown | Why |
|----|---------|-----|
| SU-007 | All font-family choices | Not readable from JPG |
| SU-008 | All font-size px per role | Estimation insufficient for production |
| SU-009 | Mobile type scale | No mobile art |

---

## Color

| ID | Unknown | Why |
|----|---------|-----|
| SU-010 | Exact HEX for accent red | JPEG COLOR VARIANCE |
| SU-011 | Exact HEX for page wash | Multiple #e6eff6 family samples |
| SU-012 | Dark CTA banner exact color | BLOCK-015 scan variance |

---

## Interaction / responsive

| ID | Unknown | Why |
|----|---------|-----|
| SU-013 | Sticky header intent | Not visible in static JPG |
| SU-014 | Accordion expanded state | Collapsed only |
| SU-015 | Review carousel mechanics | Dots visible; behavior unknown |
| SU-016 | Video play behavior | Thumb only |
| SU-017 | Form validation / submit | Static form |
| SU-018 | Mobile/tablet layout ≤1024px | No source |

---

## Rules requiring operator approval

| ID | Item | Status |
|----|------|--------|
| SU-019 | Entire Site-Wide Style Foundation proposal | `foundation_status: PROPOSAL` |
| SU-020 | Normalization rows marked REQUIRES OPERATOR APPROVAL | See normalization doc |
| SU-021 | OL-01 scale as V6 rank-1 until foundation approved | Factory default vs project SSOT promotion |

---

## Legacy provenance (unverified for V6)

| Item | Status |
|------|--------|
| FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3 | **Not used** — legacy; do not import px |
| frontend-section-spacing-rule-v1.md §4 | **Superseded for V6** by this foundation chain |
