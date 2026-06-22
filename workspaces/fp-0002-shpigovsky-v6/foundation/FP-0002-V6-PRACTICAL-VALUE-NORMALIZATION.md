# FP-0002 V6 Practical Value Normalization

**Project:** FP-0002 Shpigovsky V6  
**Status:** PROPOSAL — `REQUIRES OPERATOR APPROVAL`  
**Scale authority:** [frontend-production-authority-order-v1.md](../../../projects/mars-website-factory/frontend-production-authority-order-v1.md) OL-01  
**Contract:** [practical-value-normalization-contract-v1.md](../../../projects/mars-website-factory/practical-value-normalization-contract-v1.md)

**Not approved as project SSOT until operator signs Site-Wide Style Foundation.**

---

## Traceability table

| Rule ID | Evidence | Observed range | Proposed production value | Factory token | Delta | Reason | Confidence | Exception |
| ------- | -------- | -------------- | ------------------------- | ------------- | ----- | ------ | ---------- | --------- |
| NRM-001 | SECTION-002+ light page vertical band | section padding ~40–80px | **50px** | `section-padding-standard` | mid-band | OL-01 anchor; cadence M | MEDIUM | No |
| NRM-002 | SECTION-003 photo / SECTION-005 CTA band transitions | major band gap | **70px** | `section-gap-band-inner` | — | diff-bg / bleed approach | LOW | REQUIRES OPERATOR APPROVAL |
| NRM-003 | Same-wash internal groups SECTION-002 | continuation ~20–40px | **30px** | `section-gap-same-bg` | — | single-boundary rhythm | MEDIUM | No |
| NRM-004 | H2 to content (REPEAT-005) | ~20–40px | **30px** | `heading-content-gap` | — | repeated pattern | MEDIUM | No |
| NRM-005 | Body text stacks | ~15–25px | **20px** | `text-stack-gap` | — | tight copy rhythm | LOW | REQUIRES OPERATOR APPROVAL |
| NRM-006 | CMP-004 / CMP-008 card grids | grid gap ~25–35px | **30px** | `grid-gap-standard` | — | 3×2 grids | MEDIUM | No |
| NRM-007 | CMP-016 / CMP-017 3-col rows | column gap ~25–35px | **30px** | `grid-gap-3col` | — | same semantic as NRM-006 | MEDIUM | No |
| NRM-008 | Card internal padding | ~20–30px | **25px** | `card-padding-standard` | — | between 20 and 30 anchors | LOW | REQUIRES OPERATOR APPROVAL |
| NRM-009 | CMP-006 accordion rows | ~10–20px | **15px** | `accordion-row-gap` | — | compact list | MEDIUM | No |
| NRM-010 | CMP-001 button height | ~30–37px | **30px** | `button-height-primary` | — | component intrinsic | MEDIUM | No |
| NRM-011 | CMP-001 button radius | ~4–6px | **5px** | `radius-button` | — | OL gap scale minimum decorative | LOW | REQUIRES OPERATOR APPROVAL |
| NRM-012 | Header bar GROUP-01 height | ~174px | **exception** | `header-bar-height-observed` | — | geometric constraint | HIGH | **YES — exception** |
| NRM-013 | Content column width median | ~1138px | **SAFE UNKNOWN** | `container-main-max` | — | not universal; full-bleed rows | HIGH unknown | HOLD |
| NRM-014 | SECTION-001 hero total | 904px | **exception** | `hero-band-height-desktop` | — | first-screen composite | HIGH | **YES — SECTION-001** |
| NRM-015 | Footer column gap | ~20–40px | **30px** | `footer-column-gap` | — | link columns | LOW | REQUIRES OPERATOR APPROVAL |
| NRM-016 | Form field vertical gap | ~15–25px | **20px** | `form-field-gap` | — | standard form rhythm | LOW | REQUIRES OPERATOR APPROVAL |

---

## Typography normalization (proposal only)

| Rule ID | Role | Observed | Proposed | Token | Confidence | Exception |
| ------- | ---- | -------- | -------- | ----- | ---------- | --------- |
| NRM-T01 | Button label | small bold | **SAFE UNKNOWN** | `type-button` | LOW | HOLD |
| NRM-T02 | Section H2 | large | **SAFE UNKNOWN** | `type-h2` | LOW | HOLD |
| NRM-T03 | Body | regular | **SAFE UNKNOWN** | `type-body` | LOW | HOLD |

**Line-height rule when sizes approved:** `font-size + 4px` per Factory precision governance.

---

## Color normalization

No HEX tokens proposed — JPEG COLOR VARIANCE. Color **roles** only in Site-Wide Style Foundation; values **SAFE UNKNOWN** until operator supplies approved samples or higher-confidence extraction.

---

## Container normalization

| Rule ID | Pattern | Proposal | Status |
| ------- | ------- | -------- | ------ |
| NRM-C01 | Main content column | median 1138px observed | **SAFE UNKNOWN** — do not ship `max-width: 1220px` from legacy |
| NRM-C02 | Full-bleed media | width 100% of viewport layer | `container-full-bleed` role |
| NRM-C03 | Page horizontal padding | ~(1398−1138)/2 ≈ **130px** side margin | **SAFE UNKNOWN** — may be content inset not padding token |

---

## Operator approval flags

All rows marked `REQUIRES OPERATOR APPROVAL` must be confirmed or revised before `foundation_status: APPROVED`.

**Global flag:** `normalization_status: PROPOSAL`

---

## Next step

[FP-0002-V6-SITE-WIDE-STYLE-FOUNDATION.md](FP-0002-V6-SITE-WIDE-STYLE-FOUNDATION.md)
