# FP-0002 V6 Foundation — SAFE UNKNOWN

**Purpose:** Items that must not be invented during implementation. Route to operator or future audit.

**Review:** Operator review preparation 2026-06-22

---

## Structural / grounding

| ID | Unknown | Why | Needed from operator |
|----|---------|-----|----------------------|
| SU-001 | Exact Y boundary between header bar and hero within SECTION-001 | Y=174 is OBSERVED_JPG_ESTIMATE — CSS forbidden; element bounds in SECTION-001 spec |
| SU-003 | CMP-004 vs CMP-008 — one card component or two | Visually similar (REPEAT-001) not proven identical | Component taxonomy decision |
| SU-021 | Header bar exact pixel height | Y~174 is algorithmic estimate only — **not** implementation boundary | Approve height at Block Specification or accept composite SECTION-001 |

---

## Layout / container

| ID | Unknown | Why | Needed |
|----|---------|-----|--------|
| SU-004 | ~~Universal container-main max-width~~ | **RESOLVED** — `container-main: 1220px` APPROVED_OPERATOR_RULE | — |
| SU-005 | Side inset ~130px on JPG vs container padding model | Derived from median X on 1398px image; not same as 1220px + 50px padding math | Container inset decision at block spec |
| SU-006 | ~~Relationship 1138px JPG vs CSS max-width~~ | **RESOLVED** — 1138px = OBSERVED only; 1220px = production | — |
| SU-022 | JPG side inset vs `container-padding-inline-desktop` 50px | 130px observed band margin ≠ 89px implied by (1398−1220)/2 | Confirm padding token or per-block inset |

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
| SU-019 | Entire Site-Wide Style Foundation proposal | **RESOLVED** — `foundation_status: APPROVED` operator 2026-06-22 |
| SU-002 | Whether hero is separate implementation block from header | **RESOLVED** — composite SECTION-001; internal groups only |
| SU-020 | Normalization rows marked PROPOSE / LOW confidence | See approval sheet §B |
| SU-023 | `button-height-standard` 30px vs taller observed upper bound | Confirm 30px or revise at block spec |

---

## CSS-forbidden observed values

| Value | Classification | Rule |
|-------|----------------|------|
| Y = 174px | OBSERVED_JPG_ESTIMATE | Do not use in CSS for header height or Header/Hero split until operator approves |
| width = 1138px | OBSERVED_JPG_VALUE | Do not use as `max-width` |

---

## Legacy provenance (unverified for V6)

| Item | Status |
|------|--------|
| FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3 | **Not used** — legacy; do not import px |
| frontend-section-spacing-rule-v1.md §4 | **Superseded for V6** by this foundation chain |
