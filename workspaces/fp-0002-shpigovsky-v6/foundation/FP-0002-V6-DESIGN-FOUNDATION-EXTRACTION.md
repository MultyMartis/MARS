# FP-0002 V6 Design Foundation Extraction

**Project:** FP-0002 Shpigovsky — V6 CLEAN ROOM  
**Status:** OBSERVATION ONLY — no production values in this document  
**Verdict dependency:** Grounding review **PARTIAL**

## Source authority

| Field | Value |
|-------|-------|
| Visual source | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` |
| SHA-256 | `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |
| Grounding | `audit/jpg-visual-audit/review/FP-0002-V6-JPG-AUDIT-GROUNDING-REVIEW.md` |
| Structure | `audit/jpg-visual-audit/review/FP-0002-V6-JPG-GROUNDED-STRUCTURE.json` |

**Forbidden for values:** FIG, PDF, v1–v5 workspaces, v3 Production Standards, legacy audits.

---

## Major sections (grounded)

11 sections — see structure lock. SECTION-001 includes Header + Hero as one major section (internal split SAFE UNKNOWN).

---

## Spacing observations (observed ranges only)

### Section vertical extent (proxy for rhythm — not padding tokens)

| Section ID | Height (px) | Role | Notes |
|------------|-------------|------|-------|
| SECTION-001 | 904 | Header + hero | Full first screen; includes overlay panel |
| SECTION-002 | 3640 | Long content band | Multiple internal groups; same page wash |
| SECTION-003 | 448 | Full-width photo | Bleed band |
| SECTION-004 | 1072 | Cards + landscape photo | Mixed full-width + content |
| SECTION-005 | 3352 | Dense multi-group | CTA banner internal |
| SECTION-006 | 2920 | Programs + mosaic | Mosaic false-positive boundaries |
| SECTION-007 | 2032 | Video + specialists | |
| SECTION-008 | 368 | Articles | Short band |
| SECTION-009 | 672 | FAQ | |
| SECTION-010 | 368 | Contact form | Split panel |
| SECTION-011 | 567 | Footer | Light page |

### Internal group heights (selected)

| Group | Y range | Height (px) | Observation |
|-------|---------|-------------|-------------|
| SECTION-001-GROUP-01 header bar | 0–174 | ~174 | Top light strip |
| SECTION-001-GROUP-02 hero | 174–904 | ~730 | Photo + dark overlay ~Y344–872 |
| BLOCK-002 intro+grid | 904–1456 | 552 | 6-card grid region |
| BLOCK-015 CTA banner | 7504–7848 | 344 | Dark internal panel |

### Section padding / gaps (visual estimate from JPG — LOW–MEDIUM confidence)

| Pattern class | Observed range (px) | Evidence | Confidence |
|---------------|---------------------|----------|------------|
| Section top padding (light page sections) | ~40–80 | Vertical whitespace above H2 bands in SECTION-002, 005, 008 | MEDIUM |
| Section bottom padding (light page) | ~40–80 | Whitespace before next internal group or boundary | MEDIUM |
| Heading-to-content gap | ~20–40 | Red marker + H2 to body/cards | MEDIUM |
| Paragraph / text stack gap | ~15–25 | Body copy stacks in team sections | LOW |
| Card grid gap (3×2 service grid) | ~25–35 | CMP-004 BLOCK-002 | MEDIUM |
| Card grid gap (benefit grid) | ~25–35 | CMP-008 BLOCK-012 | MEDIUM |
| Card internal padding | ~20–30 | White cards on light wash | LOW |
| Column gap (3-col specialists/articles) | ~25–35 | CMP-016, CMP-017 | MEDIUM |
| Button group gap | ~15–25 | Multiple CTAs in hero overlay | LOW |
| Accordion row gap | ~10–20 | CMP-006 rows | MEDIUM |
| Form field gap | ~15–25 | CMP-019 contact band | LOW |
| Footer group gap | ~20–40 | Link columns SECTION-011 | LOW |

**Not measured with subpixel tooling in this pass** — ranges from audit geometry + component map notes.

---

## Container observations

| Pattern | Observed range | Evidence | Universal? |
|---------|----------------|----------|------------|
| Page width | 1398px | Image native width | Yes (source) |
| Repeated content horizontal bounds | X ~130–1267, width ~1138 | `_pixel-analysis.json` median | **No** — many full-bleed rows |
| Narrower content rows | width ~1093–1194 | Geometry map BLOCK-002, 022 | Section-specific |
| Full-width bleed | width 1398 | Photos SECTION-003, 004 landscape, hero | Yes (multiple) |
| Contact band | mixed panel + form | SECTION-010 BLOCK-033 | Exception |

**Do not equate 1138px median with CSS `max-width` without operator approval.**

---

## Typography observations (families — no px production)

| Role | Visual evidence | Repeat count | Confidence |
|------|-----------------|--------------|------------|
| Display / hero headline | Large white on dark overlay SECTION-001 | 1 | MEDIUM |
| Section H2 + red marker | REPEAT-005 pattern ~15× | HIGH pattern, LOW px |
| Card title | Service/benefit cards | 12+ | MEDIUM |
| Body text | Paragraphs in SECTION-002, 005 | many | MEDIUM |
| Nav links | Header bar CMP-002 | 1 row | MEDIUM |
| Button label | CMP-001 red CTA | 8 | HIGH visual match |
| Accordion title | CMP-006 | 12+ | MEDIUM |
| Footer links | CMP-020 | 1 section | MEDIUM |
| Form labels | CMP-019 | 1 | LOW |

**SAFE UNKNOWN:** font-family, exact sizes, line-heights, weights for all levels.

---

## Color role observations (families — JPEG variance)

| Role | Observed family | Example scan | HEX exact? |
|------|-----------------|--------------|------------|
| Page wash | Light blue-grey | #e6eff6 family | NO — variance |
| Hero photo | Neutral grey-green | #a0abb1 composite | NO |
| Dark photo band | Near black | #0e0e26 SECTION-003 | MEDIUM |
| Dark CTA banner | Blue-grey dark | #535c79 BLOCK-015 | NO |
| Accent / CTA | Red | ~#d32f2f CMP-001 | NO |
| Card surface | White on wash | cards CMP-004 | MEDIUM |
| Footer | Light page (not dark blue) | SECTION-011 | HIGH (grounding correction) |

---

## Radius observations

| Element | Observed range | Source |
|---------|----------------|--------|
| Primary CTA button | ~4–6px | CMP-001 component map |
| Hero overlay panel | large rounded rect | CMP-003 — exact radius SAFE UNKNOWN |
| Cards | subtle corner | CMP-004 — LOW confidence |
| Accordion row ends | pill-like caps | CMP-006 — MEDIUM |

---

## Component families (grounded map)

| Family ID | Components | Shared? | Notes |
|-----------|------------|---------|-------|
| FAM-BTN-PRIMARY | CMP-001 | 8× | Red fill, white label |
| FAM-HEADER | CMP-002 | unique | Y~0–174 |
| FAM-HERO | CMP-003 | unique | Overlay on photo |
| FAM-CARD-6GRID | CMP-004, CMP-008 | similar not proven identical | REPEAT-001 |
| FAM-ACCORDION-ROW | CMP-006, CMP-018 | shared pattern | REPEAT-002 |
| FAM-CARD-3COL | CMP-016, CMP-017 | similar layout | REPEAT-004 |
| FAM-REVIEW | CMP-009 | 2× | pagination dots |
| FAM-STEP-NUMBERED | CMP-010 | 5× | |
| FAM-CTA-BANNER-DARK | CMP-011 | unique | internal SECTION-005 |
| FAM-PROGRAM-ROW | CMP-012 | 4× | |
| FAM-MOSAIC | CMP-014 | 5 tiles | non-uniform grid |
| FAM-VIDEO-THUMB | CMP-015 | 2× | |
| FAM-CONTACT-BAND | CMP-019 | unique | SECTION-010 |
| FAM-FOOTER | CMP-020 | unique | light page |

**SAFE UNKNOWN:** CMP-004 vs CMP-008 — one component or two instances.

---

## Image behavior

- Full-bleed horizontal photos: SECTION-003, SECTION-004 landscape, hero background
- Square clinical thumbs: CMP-007 (4×)
- Mosaic non-uniform grid: CMP-014
- Video thumbs with play affordance: CMP-015

---

## Alignment patterns

- Centered content column on light page sections (median ~1138px)
- Left-aligned text blocks with right portraits (quote CMP-005)
- 3-column card rows repeated

---

## Extraction limitations

1. Header/Hero internal Y boundary not proven — no separate hero section ID.
2. Mobile/tablet layout not in source JPG.
3. Interaction states not visible.
4. Exact spacing requires higher-confidence measurement pass or operator markup.

**Next step:** [FP-0002-V6-PRACTICAL-VALUE-NORMALIZATION.md](FP-0002-V6-PRACTICAL-VALUE-NORMALIZATION.md)
