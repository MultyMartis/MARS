# FP-0002 V6 JPG VISUAL AUDIT

> **RAW ALGORITHMIC SEGMENTATION — NOT IMPLEMENTATION STRUCTURE**
>
> The 35 `BLOCK-*` entries below are pixel-derived algorithmic segments (8px row scan, transition-score peaks, min distance ~320px). They are **preserved for audit history** only.
>
> **Visually grounded structure** for implementation planning: see `review/FP-0002-V6-JPG-GROUNDED-STRUCTURE.json` and `review/FP-0002-V6-JPG-AUDIT-GROUNDING-REVIEW.md` — **11 major sections**, internal groups, 10 confirmed section boundaries, 21 internal boundaries, 3 false positives.
>
> Grounding review verdict: **PARTIAL** (Header/Hero Y split SAFE UNKNOWN). `header_implementation_authorized`: false.

## Source authority

| Field | Value |
|-------|-------|
| Path | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` |
| SHA-256 | `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |
| File size | 8 107 632 bytes |
| Policy | JPG_ONLY — no FIG, PDF, legacy workspace, legacy audit |

## Image metadata

| Property | Value |
|----------|-------|
| Width | 1398 px |
| Height | 16343 px |
| Orientation | portrait (vertical scroll) |
| Color mode | RGB |
| Coordinate origin | top-left (0,0) |
| Y page top | 0 |
| Y page bottom (exclusive end) | 16343 |

## Coordinate system

- **X:** left → right, unit = source image pixel
- **Y:** top → bottom, unit = source image pixel
- **Block height:** Y end − Y start
- **Method:** PIL load at native resolution; 8px row luminance/classification scan; transition-score peak boundaries (min distance 320px)
- **Note:** No screen-preview scaling used

## Global page segmentation

35 **raw algorithmic** segments detected (BLOCK-001 … BLOCK-035). Boundaries are pixel-derived; grounding review confirmed most are **not** major page sections — see review artefact.

| Segment | Y start | Y end | Height | Dominant family | Proven role |
|---------|---------|-------|--------|-----------------|-------------|
| BLOCK-001 | 0 | 904 | 904 | visual-heavy | top navigation + hero (visually proven) |
| BLOCK-002 | 904 | 1456 | 552 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-003 | 1456 | 1904 | 448 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-004 | 1904 | 2232 | 328 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-005 | 2232 | 2824 | 592 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-006 | 2824 | 3312 | 488 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-007 | 3312 | 3912 | 600 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-008 | 3912 | 4544 | 632 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-009 | 4544 | 4992 | 448 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-010 | 4992 | 5480 | 488 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-011 | 5480 | 6064 | 584 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-012 | 6064 | 6776 | 712 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-013 | 6776 | 7136 | 360 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-014 | 7136 | 7504 | 368 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-015 | 7504 | 7848 | 344 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-016 | 7848 | 8408 | 560 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-017 | 8408 | 8824 | 416 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-018 | 8824 | 9416 | 592 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-019 | 9416 | 10008 | 592 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-020 | 10008 | 10368 | 360 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-021 | 10368 | 10880 | 512 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-022 | 10880 | 11248 | 368 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-023 | 11248 | 11592 | 344 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-024 | 11592 | 11984 | 392 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-025 | 11984 | 12336 | 352 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-026 | 12336 | 13136 | 800 | visual-heavy | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-027 | 13136 | 13456 | 320 | visual-heavy | post-video light page (NOT contact form — corrected) |
| BLOCK-028 | 13456 | 13776 | 320 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-029 | 13776 | 14368 | 592 | visual-heavy | specialists 3-card row (visually grounded) |
| BLOCK-030 | 14368 | 14736 | 368 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-031 | 14736 | 15064 | 328 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-032 | 15064 | 15408 | 344 | page | SAFE UNKNOWN — role not labeled on JPG |
| BLOCK-033 | 15408 | 15776 | 368 | visual-heavy | contact form band (SECTION-010) |
| BLOCK-034 | 15776 | 16152 | 376 | page | footer link columns (SECTION-011) |
| BLOCK-035 | 16152 | 16343 | 191 | page | footer region (light page strip) |

## Block audit

### BLOCK-001 — neutral segment 1

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 0–904.

#### 2. Height

904px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #a0abb1, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

MEDIUM

### BLOCK-002 — neutral segment 2

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1193 (width 1194); Y 904–1456.

#### 2. Height

552px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1194px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-003 — neutral segment 3

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1378 (width 1379); Y 1456–1904.

#### 2. Height

448px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e7f0f7, bottom-right #e4dfe6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1379px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-004 — neutral segment 4

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1396 (width 1397); Y 1904–2232.

#### 2. Height

328px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff4, bottom-right #dbe0e6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1397px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-005 — neutral segment 5

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 2232–2824.

#### 2. Height

592px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #dee8f1, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-006 — neutral segment 6

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 25–1397 (width 1373); Y 2824–3312.

#### 2. Height

488px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1373px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-007 — neutral segment 7

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 3–1397 (width 1395); Y 3312–3912.

#### 2. Height

600px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #eae5e9. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1395px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-008 — neutral segment 8

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 3912–4544.

#### 2. Height

632px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e5edf8, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-009 — neutral segment 9

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 4544–4992.

#### 2. Height

448px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #0e0e26, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-010 — neutral segment 10

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 4992–5480.

#### 2. Height

488px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e2eaed, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-011 — neutral segment 11

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 5480–6064.

#### 2. Height

584px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #576834, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `photo-dark` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-012 — neutral segment 12

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 17–1395 (width 1379); Y 6064–6776.

#### 2. Height

712px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1379px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-013 — neutral segment 13

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 3–1397 (width 1395); Y 6776–7136.

#### 2. Height

360px (Y end − Y start).

#### 3. Background

Samples: top-left #e3dee4, center #e6eff6, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1395px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light-mixed` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-014 — neutral segment 14

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 7136–7504.

#### 2. Height

368px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #dedbe2, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-015 — neutral segment 15

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 7504–7848.

#### 2. Height

344px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #535c79, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-016 — neutral segment 16

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 2–1397 (width 1396); Y 7848–8408.

#### 2. Height

560px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #372c28, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1396px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-017 — neutral segment 17

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1365 (width 1366); Y 8408–8824.

#### 2. Height

416px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e7ecf2. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1366px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-018 — neutral segment 18

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1394 (width 1395); Y 8824–9416.

#### 2. Height

592px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e4e9ed, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1395px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-019 — neutral segment 19

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–921 (width 922); Y 9416–10008.

#### 2. Height

592px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 922px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-020 — neutral segment 20

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 309–1420 (width 1112); Y 10008–10368.

#### 2. Height

360px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #f8f9fd. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1112px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-021 — neutral segment 21

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 10368–10880.

#### 2. Height

512px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e5eef3, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-022 — neutral segment 22

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1092 (width 1093); Y 10880–11248.

#### 2. Height

368px (Y end − Y start).

#### 3. Background

Samples: top-left #dedee6, center #e6eff6, bottom-right #dedce1. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1093px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-023 — neutral segment 23

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1358 (width 1359); Y 11248–11592.

#### 2. Height

344px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #ccd4bd, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1359px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-024 — neutral segment 24

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 11592–11984.

#### 2. Height

392px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #133848, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-025 — neutral segment 25

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1388 (width 1389); Y 11984–12336.

#### 2. Height

352px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1389px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-026 — neutral segment 26

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 84–1337 (width 1254); Y 12336–13136.

#### 2. Height

800px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e2e8f4. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1254px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-027 — neutral segment 27

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1396 (width 1397); Y 13136–13456.

#### 2. Height

320px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #edefee, bottom-right #6d6e72. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1397px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `photo-dark` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-028 — neutral segment 28

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1362 (width 1363); Y 13456–13776.

#### 2. Height

320px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1363px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-029 — neutral segment 29

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 13776–14368.

#### 2. Height

592px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e5eef3, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-030 — neutral segment 30

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 8–1397 (width 1390); Y 14368–14736.

#### 2. Height

368px (Y end − Y start).

#### 3. Background

Samples: top-left #e8edf3, center #e6eff6, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1390px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-031 — neutral segment 31

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 14736–15064.

#### 2. Height

328px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6e5ea, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-032 — neutral segment 32

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 15064–15408.

#### 2. Height

344px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-033 — neutral segment 33

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 6–1397 (width 1392); Y 15408–15776.

#### 2. Height

368px (Y end − Y start).

#### 3. Background

Samples: top-left #e7eef4, center #ffffff, bottom-right #e6eff6. Dominant scan family: visual-heavy. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1392px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `composite` across block. Detailed sub-groups: see structure lock; pixel family `visual-heavy`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-034 — neutral segment 34

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 15776–16152.

#### 2. Height

376px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

HIGH

### BLOCK-035 — neutral segment 35

#### 1. External boundaries

X 0–1397 PAGE WIDTH; content X 0–1397 (width 1398); Y 16152–16342.

#### 2. Height

190px (Y end − Y start).

#### 3. Background

Samples: top-left #e6eff6, center #e6eff6, bottom-right #e6eff6. Dominant scan family: page. JPEG COLOR VARIANCE.

#### 4. Container width

CONTENT WIDTH 1398px; PAGE WIDTH 1398px. Centered when margins symmetric — SAFE UNKNOWN per row.

#### 5. Internal structure

Dominant row class `page-light` across block. Detailed sub-groups: see structure lock; pixel family `page`.

#### 6. Columns

SAFE UNKNOWN at block level without sub-segment OCR; see component map for grid blocks.

#### 7. Element order

Top-to-bottom per visible stacking; left-to-right within rows — block-specific extraction in structure lock.

#### 8. Visual accents

Red accent elements present where red pixel clusters intersect block Y range — see component map.

#### 9. Repeating patterns

See repetition map if patterns span this Y range.

#### 10. Separate components

See component map entries whose first occurrence matches this block ID.

#### 11. Unique components

Single-instance components listed in component map with repeat count 1 for this Y range.

#### 12. SAFE UNKNOWN

font-family; line-height; interaction; hidden states; exact HEX; mobile order.

#### Evidence confidence

LOW

## Typography observations

Pixel-estimated levels only; **no font-family asserted**.

| Role | Example (visible Russian) | Cap height px | Weight category | Color | Alignment |
|------|---------------------------|---------------|-----------------|-------|-----------|
| hero-heading | Центр реабилитации и восстановительной медицины Шпиговского… | 34-42 | bold | #ffffff on dark overlay | left |
| section-heading-primary | Наши услуги… | 28-34 | bold | #1a1a1a to #2a2a2a | left |
| section-heading-secondary | subhead under primary headings… | 18-22 | regular | #4a4a4a | left |
| card-title | card bold lines… | 16-20 | semibold | #222 | left |
| body | paragraph lines in cards and lists… | 12-16 | regular | #444-#666 | left |
| nav-link | header navigation labels… | 12-14 | medium | #333 | left |
| footer-link | footer column links… | 12-14 | regular | #c8d0e0 on dark | left |

Line-height, letter-spacing: SAFE UNKNOWN (JPEG anti-aliasing).

## Spacing observations

| Measurement | Value | Confidence |
|-------------|-------|------------|
| Page side margin (light rows) | ~130px to content start | approximate |
| Content width consensus | ~1138px (X 130–1267) | HIGH on page-family rows |
| BLOCK-001 height | 904px | HIGH |
| Inter-block gaps | embedded in boundary transitions | MEDIUM |
| Card grid gap | SAFE UNKNOWN | — |
| Section vertical padding | SAFE UNKNOWN per block | — |

## Image and decor observations

- Hero facility photograph: BLOCK-001, full content width, photographic composite.
- Portrait and clinical photos: multiple blocks; rounded corners observed ~4-8px — approximate.
- Red circular icons on cards: raster/vector origin SAFE UNKNOWN.
- Dark blue full-width bands: contact section ~Y13136–13776; footer ~Y15420–16152 — JPEG COLOR VARIANCE on blues.

## Repetition summary

See `FP-0002-V6-JPG-COMPONENT-MAP.md` and repetition table in geometry artefact.

## Global SAFE UNKNOWN

- font-family for all text levels
- exact HEX for red accent and dark blue backgrounds (JPEG COLOR VARIANCE)
- hover/focus/active states
- accordion expanded content
- carousel/slider mechanics for reviews
- form field validation and submit endpoint
- video playback behavior
- mobile/tablet layout at 1024px and below
- whether sticky header is intended
- z-index stacking order
- semantic HTML mapping
- SVG vs raster for icons
- relationship between JPG content width 1138px and future CSS container 1220px

## Validation

| Check | Result |
|-------|--------|
| Single JPG source | PASS |
| SHA-256 | PASS |
| Forbidden sources | not accessed |
| Blocks cover Y=0..16342 | PASS (sum heights = 16342) |
| Coordinates within image | PASS |
| HTML/SCSS/JS unchanged | PASS (audit-only) |
| JSON valid | PASS |

## Final audit status

**PASS — JPG VISUAL AUDIT COMPLETE** with documented MEDIUM/LOW boundary confidence on short segments (<380px).

Coordinate method is reproducible from `_major-blocks.json` scan (internal helper, not implementation).
