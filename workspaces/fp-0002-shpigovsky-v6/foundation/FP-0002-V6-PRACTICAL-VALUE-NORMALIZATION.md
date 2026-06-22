# FP-0002 V6 Practical Value Normalization

**Project:** FP-0002 Shpigovsky V6  
**Status:** PROPOSAL — `REQUIRES OPERATOR APPROVAL`  
**Review:** Operator review preparation 2026-06-22  
**Scale authority:** [frontend-production-authority-order-v1.md](../../../projects/mars-website-factory/frontend-production-authority-order-v1.md) OL-01  
**Contract:** [practical-value-normalization-contract-v1.md](../../../projects/mars-website-factory/practical-value-normalization-contract-v1.md)

**Not approved as project SSOT until operator signs Site-Wide Style Foundation.**

---

## Value classification legend

| Class | Meaning |
|-------|---------|
| `APPROVED_OPERATOR_RULE` | Operator-authorized production rule (not JPG-derived) |
| `OBSERVED_JPG_VALUE` | Measured/estimated from JPG — informational |
| `NORMALIZED_PROPOSAL` | Nearest OL-01 value from observed range |
| `APPROVED_FOUNDATION_TOKEN` | Operator-approved after Gate 2 |
| `BLOCK_LEVEL_EXCEPTION` | Exact geometry deferred to Block Specification |
| `SAFE_UNKNOWN` | No production value — forbidden to invent |

---

## Traceability table — spacing tokens

| Token | JPG evidence | Observed range | Pattern family | Normalized value | Property class | OL-01 | Confidence | Verdict |
| ----- | ------------ | -------------- | -------------- | ---------------- | -------------- | ----- | ---------- | ------- |
| `section-padding-compact` | SECTION-008, SECTION-011 short bands | ~40–50px | section rhythm compact | **40px** | padding | Yes | MEDIUM | PROPOSE |
| `section-padding-standard` | SECTION-002, 004–007, 009 light bands | ~40–80px mid | section rhythm standard | **50px** | padding | Yes | MEDIUM | PROPOSE |
| `section-padding-large` | Pre/post full-bleed transitions | ~60–80px upper | section rhythm large | **70px** | padding | Yes | LOW | PROPOSE |
| `section-gap-same-bg` | SECTION-002 internal groups | ~20–40px | same-wash continuation | **30px** | padding (single boundary) | Yes | MEDIUM | PROPOSE |
| `section-gap-band-inner` | SECTION-003/005 band transitions | major band gap | feature / diff-bg | **70px** | padding | Yes | LOW | PROPOSE |
| `heading-content-gap` | REPEAT-005 H2→content | ~20–40px | heading-content | **30px** | margin | Yes | MEDIUM | PROPOSE |
| `text-stack-gap` | Body stacks SECTION-002, 005 | ~15–25px | paragraph stack | **20px** | margin | Yes | LOW | PROPOSE |
| `grid-gap-standard` | CMP-004, CMP-008 3×2 | ~25–35px | card grid | **30px** | gap | Yes | MEDIUM | PROPOSE |
| `grid-gap-3col` | CMP-016, CMP-017 | ~25–35px | 3-col cards | **30px** | gap | Yes | MEDIUM | PROPOSE |
| `card-padding-standard` | White cards CMP-004 | ~20–30px | card internal | **25px** | padding | Yes | LOW | PROPOSE |
| `accordion-row-spacing` | CMP-006 rows | ~10–20px | accordion list | **15px** | **margin** | Yes | MEDIUM | PROPOSE (revised) |
| `form-field-gap` | CMP-019 contact | ~15–25px | form vertical | **20px** | gap | Yes | LOW | PROPOSE |
| `footer-column-gap` | CMP-020 columns | ~20–40px | footer groups | **30px** | gap | Yes | LOW | PROPOSE |

### OL-01 revision — accordion

| Prior token | Issue | Resolution |
|-------------|-------|------------|
| `accordion-row-gap: 15px` | 15px ∉ gap scale | Renamed `accordion-row-spacing`; property class **margin** (15px ∈ padding/margin scale) |

---

## Traceability table — container

| Token / role | JPG evidence | Observed | Classification | Value | Verdict |
| ------------ | ------------ | -------- | -------------- | ----- | ------- |
| `container-main` | Operator V6 zero skeleton | N/A (operator rule) | APPROVED_OPERATOR_RULE | **1220px** max-width | APPROVE |
| `container-content-band-observed` | `_pixel-analysis.json` median | ~1138px content band | OBSERVED_JPG_VALUE | 1138px | NOT CSS container |
| `container-padding-inline-desktop` | Factory container convention | N/A | APPROVED_OPERATOR_RULE | **50px** proposal | PROPOSE |

**Rule:** Do **not** substitute `1138px` for `1220px`. JPG content band is narrower than production container — inner groups may be narrower still.

---

## Traceability table — component geometry

| Token | JPG evidence | Observed range | Normalized | Property class | OL-01 | Confidence | Verdict |
| ----- | ------------ | -------------- | ---------- | -------------- | ----- | ---------- | ------- |
| `button-height-standard` | CMP-001 ×8 | ~30–37px | **30px** | height (component) | N/A (geometry) | MEDIUM | PROPOSE |
| `radius-button` | CMP-001 corners | ~4–6px | **5px** | border-radius | N/A | LOW | PROPOSE |

### Button family review

| Family | Components | Heights equal? | Border in height? | Families needed |
|--------|------------|----------------|-------------------|-----------------|
| FAM-BTN-PRIMARY | CMP-001 (8×) | Yes (visual match) | Unknown — treat as content box | **One** standard family |
| FAM-BTN-HEADER | header CTA | Not separately measured | — | SAFE UNKNOWN |

**Decision:** Single `button-height-standard: 30px` — observed lower bound; 37px upper may include JPEG anti-aliasing. Operator may revise to 32–35px at Block Specification if measurement proves taller primary family.

---

## Header/Hero — demoted from implementation exception

| Item | Prior status | Review verdict |
|------|--------------|----------------|
| Y=174 header bar end | EX-001 implementation exception | **REMOVED** — demoted to `header-bar-y-end-estimate` |
| Evidence | SECTION-001-GROUP-01 algorithmic row scan | Approximate observed estimate only |
| Grounding | SAFE UNKNOWN exact Header/Hero split | CSS use of 174px **forbidden** until operator approves |
| Y=904 SECTION-001 end | EX-002 | **RETAINED** — CONFIRMED_SECTION_BOUNDARY HIGH confidence |

---

## Section rhythm mapping (major sections)

| Section | Observed top (est.) | Observed bottom (est.) | Rhythm family | Proposed token | Confidence |
| ------- | ------------------- | ---------------------- | ------------- | -------------- | ---------- |
| SECTION-001 | hero composite | hero composite | hero | EX-002 904px | HIGH (outer only) |
| SECTION-002 | ~50 | ~50 | standard | `section-padding-standard` | MEDIUM |
| SECTION-003 | ~70 (photo bleed) | ~70 | large / feature | `section-padding-large` | LOW |
| SECTION-004 | ~50 | ~50 | standard | `section-padding-standard` | MEDIUM |
| SECTION-005 | ~50 | ~50 | standard | `section-padding-standard` | MEDIUM |
| SECTION-006 | ~50 | ~50 | standard | `section-padding-standard` | MEDIUM |
| SECTION-007 | ~50 | ~50 | standard | `section-padding-standard` | MEDIUM |
| SECTION-008 | ~40 | ~40 | compact | `section-padding-compact` | MEDIUM |
| SECTION-009 | ~50 | ~50 | standard | `section-padding-standard` | MEDIUM |
| SECTION-010 | split panel | split panel | custom-exception | EX-003 block spec | HIGH |
| SECTION-011 | ~40 | ~40 | compact | `section-padding-compact` | MEDIUM |

Internal same-wash groups within SECTION-002+ use `section-gap-same-bg` 30px per Factory same-bg rule.

---

## Component spacing families

| Pattern family | Occurrences | Observed range | Token | Value | Shared/Exceptional |
| -------------- | ----------- | -------------- | ----- | ----- | ------------------ |
| heading-content | REPEAT-005 ~15× | 20–40px | `heading-content-gap` | 30px | Shared |
| paragraph stack | many body blocks | 15–25px | `text-stack-gap` | 20px | Shared |
| card internal padding | CMP-004, CMP-008 | 20–30px | `card-padding-standard` | 25px | Shared |
| 3×2 card grid gap | CMP-004, CMP-008 | 25–35px | `grid-gap-standard` | 30px | Shared |
| 3-col card gap | CMP-016, CMP-017 | 25–35px | `grid-gap-3col` | 30px | Shared (same value) |
| accordion row spacing | CMP-006, CMP-018 | 10–20px | `accordion-row-spacing` | 15px margin | Shared |
| form field gap | CMP-019 | 15–25px | `form-field-gap` | 20px gap | Exceptional (form) |
| footer column gap | CMP-020 | 20–40px | `footer-column-gap` | 30px gap | Exceptional (footer) |
| button group gap | hero overlay CTAs | 15–25px | — | SAFE UNKNOWN | Deferred block spec |
| program row spacing | CMP-012 | — | — | SAFE UNKNOWN | Deferred block spec |
| numbered step spacing | CMP-010 | — | — | SAFE UNKNOWN | Deferred block spec |

---

## Typography normalization (proposal only)

| Rule ID | Role | Observed | Proposed | Token | Confidence | Verdict |
| ------- | ---- | -------- | -------- | ----- | ---------- | ------- |
| NRM-T01 | Button label | small bold white | SAFE UNKNOWN | `type-button` | LOW | HOLD |
| NRM-T02 | Section H2 | large + red marker | SAFE UNKNOWN | `type-h2` | LOW | HOLD |
| NRM-T03 | Body | regular | SAFE UNKNOWN | `type-body` | LOW | HOLD |
| NRM-T04 | Display/hero | large white on dark | SAFE UNKNOWN | `type-display` | LOW | HOLD |
| NRM-T05 | Navigation | header links | SAFE UNKNOWN | `type-nav` | LOW | HOLD |

**Line-height rule when sizes approved:** `font-size + 4px` per Factory precision governance.

---

## Color normalization

No HEX tokens proposed — JPEG COLOR VARIANCE. Color **roles** only; values `VALUE PENDING BLOCK EXTRACTION` or SAFE UNKNOWN.

---

## Operator approval flags

All `PROPOSE` rows require operator confirmation before `foundation_status: APPROVED`.

**Global flag:** `normalization_status: PROPOSAL`

---

## Next step

[FP-0002-V6-SITE-WIDE-STYLE-FOUNDATION.md](FP-0002-V6-SITE-WIDE-STYLE-FOUNDATION.md) · [FP-0002-V6-STYLE-FOUNDATION-APPROVAL-SHEET.md](FP-0002-V6-STYLE-FOUNDATION-APPROVAL-SHEET.md)
