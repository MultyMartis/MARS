# FP-0002 V6 JPG AUDIT GROUNDING REVIEW

## Source authority

| Field | Value |
|-------|-------|
| Visual source | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` |
| SHA-256 | `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |
| Dimensions | 1398 × 16343 px |
| Policy | JPG_ONLY — FIG/PDF/v1–v5/legacy not opened during this review |

## Audit under review

| Checkpoint | Hash | Status |
|------------|------|--------|
| Source Purity Gate | `2df20406fecb8e31d5041ff1fa17a620d3214e79` | Verified (`2df2040`) |
| JPG Visual Audit HEAD (start) | `4c3b5c43bf3c79e3949538a9c65227782368e35` | Verified (`4c3b5c4`) |
| Branch | `mars/post-cycle8-live-tests` | Verified |

Raw algorithmic output: 35 blocks (`BLOCK-001` … `BLOCK-035`) from 8px row scan, luminance classification, transition-score peaks, min boundary distance ~320px.

## Review method

1. Phase 0 preflight (git, JPG hash/size, audit JSON, no HTML/SCSS/JS/`src/partials/` changes).
2. Generated review images from JPG + existing block Y coordinates only.
3. Manual classification of all 34 internal boundaries against JPG (contact sheet + full-page boundary map + row luminance samples).
4. Built two-level structure: 11 major sections + internal groups.
5. Corrected coordinate model (`y_end` exclusive; last row `16343`).
6. Component map corrections (contact form, footer, specialists).
7. Helper provenance review.

## Existing segmentation risk

**Confirmed:** 35 algorithmic blocks ≠ 35 major page sections. Most boundaries (21/34) are internal sub-block transitions within shared light-blue page bands. Three boundaries are algorithmic false positives inside the facility mosaic and post-video area. Only 10 boundaries mark visually grounded major section edges.

**Critical mis-assignments found:**

- `BLOCK-027` was labeled contact form — JPG shows light page continuation after video; contact form is at `SECTION-010` / `BLOCK-033` (Y 15408–15776).
- `CMP-020` footer described as sitewide dark blue — JPG footer (`SECTION-011`) is light page with link columns.

## Boundary-by-boundary review

| Boundary | Y | Previous block | Next block | Classification | Visual evidence | Confidence |
| -------- | - | -------------- | ---------- | -------------- | --------------- | ---------- |
| 1 | 904 | BLOCK-001 | BLOCK-002 | CONFIRMED_SECTION_BOUNDARY | Hero ends; light-blue intro + 6-card grid begins | HIGH |
| 2 | 1456 | BLOCK-002 | BLOCK-003 | INTERNAL_SUBBLOCK_BOUNDARY | Grid ends; quote block; same page band | HIGH |
| 3 | 1904 | BLOCK-003 | BLOCK-004 | INTERNAL_SUBBLOCK_BOUNDARY | Quote to accordion list | HIGH |
| 4 | 2232 | BLOCK-004 | BLOCK-005 | INTERNAL_SUBBLOCK_BOUNDARY | Accordion to photo row | HIGH |
| 5 | 2824 | BLOCK-005 | BLOCK-006 | INTERNAL_SUBBLOCK_BOUNDARY | Photos to team copy | MEDIUM |
| 6 | 3312 | BLOCK-006 | BLOCK-007 | INTERNAL_SUBBLOCK_BOUNDARY | Internal team section rows | MEDIUM |
| 7 | 3912 | BLOCK-007 | BLOCK-008 | INTERNAL_SUBBLOCK_BOUNDARY | Continuous light-blue team area | MEDIUM |
| 8 | 4544 | BLOCK-008 | BLOCK-009 | CONFIRMED_SECTION_BOUNDARY | Page to full-width staff photo (#0e0e26) | HIGH |
| 9 | 4992 | BLOCK-009 | BLOCK-010 | CONFIRMED_SECTION_BOUNDARY | Photo ends; light page resumes | HIGH |
| 10 | 5480 | BLOCK-010 | BLOCK-011 | INTERNAL_SUBBLOCK_BOUNDARY | Card grid to landscape photo | HIGH |
| 11 | 6064 | BLOCK-011 | BLOCK-012 | CONFIRMED_SECTION_BOUNDARY | Landscape photo to benefit grid | HIGH |
| 12 | 6776 | BLOCK-012 | BLOCK-013 | INTERNAL_SUBBLOCK_BOUNDARY | Benefit grid to reviews | HIGH |
| 13 | 7136 | BLOCK-013 | BLOCK-014 | INTERNAL_SUBBLOCK_BOUNDARY | Reviews to process steps | MEDIUM |
| 14 | 7504 | BLOCK-014 | BLOCK-015 | INTERNAL_SUBBLOCK_BOUNDARY | Steps to dark CTA banner | HIGH |
| 15 | 7848 | BLOCK-015 | BLOCK-016 | INTERNAL_SUBBLOCK_BOUNDARY | CTA to interior photo band | HIGH |
| 16 | 8408 | BLOCK-016 | BLOCK-017 | INTERNAL_SUBBLOCK_BOUNDARY | Photo band to documents list | HIGH |
| 17 | 8824 | BLOCK-017 | BLOCK-018 | INTERNAL_SUBBLOCK_BOUNDARY | Documents to hallway gallery | MEDIUM |
| 18 | 9416 | BLOCK-018 | BLOCK-019 | CONFIRMED_SECTION_BOUNDARY | Gallery to program list | HIGH |
| 19 | 10008 | BLOCK-019 | BLOCK-020 | INTERNAL_SUBBLOCK_BOUNDARY | Program row split | HIGH |
| 20 | 10368 | BLOCK-020 | BLOCK-021 | INTERNAL_SUBBLOCK_BOUNDARY | Program rows to bordered panel | MEDIUM |
| 21 | 10880 | BLOCK-021 | BLOCK-022 | INTERNAL_SUBBLOCK_BOUNDARY | Panel to comfort heading | MEDIUM |
| 22 | 11248 | BLOCK-022 | BLOCK-023 | INTERNAL_SUBBLOCK_BOUNDARY | Heading to mosaic grid | HIGH |
| 23 | 11592 | BLOCK-023 | BLOCK-024 | ALGORITHMIC_FALSE_POSITIVE | Mosaic tile luminance spike | HIGH |
| 24 | 11984 | BLOCK-024 | BLOCK-025 | ALGORITHMIC_FALSE_POSITIVE | Dark tile inside mosaic | HIGH |
| 25 | 12336 | BLOCK-025 | BLOCK-026 | CONFIRMED_SECTION_BOUNDARY | Mosaic ends; video section | HIGH |
| 26 | 13136 | BLOCK-026 | BLOCK-027 | INTERNAL_SUBBLOCK_BOUNDARY | Video to post-video light page | HIGH |
| 27 | 13456 | BLOCK-027 | BLOCK-028 | ALGORITHMIC_FALSE_POSITIVE | ~54px local dark band | HIGH |
| 28 | 13776 | BLOCK-028 | BLOCK-029 | INTERNAL_SUBBLOCK_BOUNDARY | Specialists heading to cards | HIGH |
| 29 | 14368 | BLOCK-029 | BLOCK-030 | CONFIRMED_SECTION_BOUNDARY | Specialists to articles | HIGH |
| 30 | 14736 | BLOCK-030 | BLOCK-031 | CONFIRMED_SECTION_BOUNDARY | Articles to FAQ | HIGH |
| 31 | 15064 | BLOCK-031 | BLOCK-032 | INTERNAL_SUBBLOCK_BOUNDARY | FAQ continuation | MEDIUM |
| 32 | 15408 | BLOCK-032 | BLOCK-033 | CONFIRMED_SECTION_BOUNDARY | FAQ to contact band (dark left panel) | HIGH |
| 33 | 15776 | BLOCK-033 | BLOCK-034 | CONFIRMED_SECTION_BOUNDARY | Contact to footer columns | HIGH |
| 34 | 16152 | BLOCK-034 | BLOCK-035 | INTERNAL_SUBBLOCK_BOUNDARY | Footer columns to bottom strip | HIGH |

**Counts:** CONFIRMED 10 | INTERNAL 21 | FALSE POSITIVE 3 | SAFE UNKNOWN 0 (at boundaries; see below for Header/Hero).

## Major sections

| ID | Y start | Y end | Height | Role |
|----|---------|-------|--------|------|
| SECTION-001 | 0 | 904 | 904 | Header + hero |
| SECTION-002 | 904 | 4544 | 3640 | Intro, quote, programs, team copy |
| SECTION-003 | 4544 | 4992 | 448 | Full-width staff group photo |
| SECTION-004 | 4992 | 6064 | 1072 | Second card grid + landscape photo |
| SECTION-005 | 6064 | 9416 | 3352 | Benefits, reviews, process, CTA, documents, interior gallery |
| SECTION-006 | 9416 | 12336 | 2920 | Program list, philosophy, facility mosaic |
| SECTION-007 | 12336 | 14368 | 2032 | Video + specialists |
| SECTION-008 | 14368 | 14736 | 368 | Articles |
| SECTION-009 | 14736 | 15408 | 672 | FAQ accordion |
| SECTION-010 | 15408 | 15776 | 368 | Contact form band |
| SECTION-011 | 15776 | 16343 | 567 | Site footer |

## Internal groups

Key groups (full list in `FP-0002-V6-JPG-GROUNDED-STRUCTURE.json`):

- `SECTION-001-GROUP-01` Y 0–174 — header top bar
- `SECTION-001-GROUP-02` Y 174–904 — hero photo + overlay
- `SECTION-002-GROUP-01` … `GROUP-07` — intro grid, quote, accordion, photos, team copy blocks
- `SECTION-005-GROUP-04` — dark-blue CTA banner (internal panel)
- `SECTION-006-GROUP-05` — facility mosaic (includes false-positive BLOCK-024/025 split)
- `SECTION-007-GROUP-01` — video thumbs; `GROUP-04` — specialist cards
- `SECTION-011-GROUP-01/02` — footer link columns + bottom strip

## Old-to-new block mapping

See `FP-0002-V6-JPG-GROUNDED-STRUCTURE.json` → `old_to_new_mapping`. Summary: 7 blocks map to standalone major sections or internal section anchors; 28 merge into parent major sections; 3 block boundaries flagged FALSE_POSITIVE (BLOCK-024 split, BLOCK-027 mis-role, mosaic/video artifact).

## Header and Hero review

- `BLOCK-001` (Y 0–904) contains both header and hero in one algorithmic block.
- Header: light strip Y ~0–174 with logo, nav, contacts (CMP-002).
- Hero: full-width building photo with dark rounded overlay panel (CMP-003).
- Header visually overlays hero — no reliable standalone major-section boundary between them on JPG.
- **SAFE UNKNOWN:** exact Header/Hero Y split for implementation.
- Hero is not a separate major section from Header in grounded map; both are internal groups of SECTION-001.

## BLOCK-027–029 review

| Block | Prior audit claim | Grounded finding |
|-------|-------------------|------------------|
| BLOCK-027 | Contact form dark section | **Incorrect.** Light page after video; short dark artifact at Y 13130–13186 is local image edge, not contact form. |
| BLOCK-028 | Unknown | Specialists section heading row (internal). |
| BLOCK-029 | Specialists (after role fix commit) | **Confirmed.** 3-column specialist profile cards (CMP-016). Prior BLOCK-029 role fix was correct for specialists; contact form assignment to BLOCK-027 was wrong. |

Contact form relocated to `BLOCK-033` / `SECTION-010` at Y 15408–15776 (dark left panel + form fields; mixed row luminance Y~15420).

## Footer review

- Footer is **one** major section (`SECTION-011`), Y 15776–16343.
- `BLOCK-033` is contact form, not footer.
- `BLOCK-034` + `BLOCK-035` are internal footer groups (link columns + bottom strip).
- Footer background is **light page** (`#e6eff6` family), not sitewide dark blue.
- Top footer edge: Y 15776 (CONFIRMED boundary after contact).
- Page bottom: Y end = **16343** (inclusive rows 0…16342).

## Coordinate consistency

| Check | Result |
|-------|--------|
| Model | `y_start` inclusive, `y_end` exclusive |
| Height | `y_end - y_start` |
| Page range | `0 ≤ Y < 16343` |
| Prior gap | `BLOCK-035` ended at 16342 — **1px gap fixed** to 16343 |
| Overlaps | None after fix |
| Gaps | None after fix |

## Container review

| Field | Value | Verdict |
|-------|-------|---------|
| Median content width | 1138 px | Statistical result from page-row analysis |
| Median X | 130–1267 | Matches many text/card rows |
| Universal container? | **No** | Full-width photos, contact band, and mosaic exceed or split bounds |
| Visually confirmed ~1138px | ~6 major section text areas | SECTION-002 in part, SECTION-005 in part, SECTION-008, SECTION-009, portions of SECTION-007 |
| Full-width elements | SECTION-003 photo, SECTION-004 landscape, SECTION-010 contact band background |

Do not equate 1138px median with future CSS `max-width: 1220px`.

## Component review

| Metric | Count |
|--------|-------|
| Total components | 20 |
| Repeating (shared) | 13 |
| Unique | 7 |

**Corrections:**

- `CMP-019` contact form: `BLOCK-027` → `SECTION-010` / `BLOCK-033`
- `CMP-020` footer: `BLOCK-033` → `SECTION-011` / `BLOCK-034–035`; notes corrected to light footer
- `CMP-016` specialists: remains `BLOCK-029` (confirmed)
- `CMP-014` mosaic: BLOCK-024/025 boundaries are false positives inside one component

All 20 components retain independent visual identity on JPG; none should be split into multiple components for algorithmic block artifacts.

## Helper provenance

| Path | Purpose | Creates audit data | Forbidden refs | Keep |
|------|---------|-------------------|----------------|------|
| `_analyze_jpg.py` | Pixel row analysis | `_pixel-analysis.json` | None (JPG path only) | Yes |
| `_major_blocks.py` | 35-block segmentation | `_major-blocks.json` | None | Yes |
| `_generate_audit.py` | Audit MD/JSON generator | Audit artefacts | None | Yes |
| `_pixel-analysis.json` | Intermediate pixel data | — | None | Yes |
| `_major-blocks.json` | Raw block boundaries | — | None | Yes |
| `generate_grounding_review_images.py` | Review contact sheet | Review JPGs | None | Yes |
| `review/build_grounded_structure.py` | Grounded JSON builder | Grounded JSON | None | Yes |

No FIG/PDF/v1–v5 path contamination in helpers.

## SAFE UNKNOWN

1. Exact Y boundary between header bar and hero within SECTION-001.
2. Whether CMP-004 and CMP-008 are one component or two similar instances.
3. Universal content container width vs 1138px median on mixed full-width sections.
4. Header bar exact pixel height (estimated ~174px).

## Violations

None. No forbidden sources opened. No HTML/SCSS/JS changes.

## Final verdict

**PARTIAL — OPERATOR REVIEW REQUIRED**

Major sections and internal groups are visually grounded on JPG. Header/Hero exact split remains ambiguous. Raw 35-block map preserved as algorithmic reference only — not implementation structure.

`header_implementation_authorized`: **false**
