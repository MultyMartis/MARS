# FP-0002 V6 HOME SECTION 01 — CLEAN VISUAL AUDIT

**Audit date:** 2026-06-23  
**Auditor lane:** Clean restart after operator rejection  
**Implementation authorization:** NOT GRANTED

## Audit purpose

Re-establish Section 01 (first block after Hero on Home) using **only** `HOME-PAGE-FULL-MOCKUP.jpg`. Rejected implementation, archived GROUP sources, and prior specs are excluded from structural authority.

## Rejected implementation excluded

| Excluded source | Reason |
|-----------------|--------|
| Commit `0e5af79` / `home-intro-mission` | Operator rejected |
| `FP-0002-V6-HOME-SECTION-01-SPEC.md` | Archived GROUP-01 reuse |
| `FP-0002-V6-HOME-SECTION-01-REVIEW.md` | Pre-rejection pass |
| Old Y 904–1456 without re-proof | Superseded by pixel re-scan |
| `intro-programs` archive | Prohibited |

## Sole visual authority

```text
workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg
```

## Mockup identity and checksum

| Field | Value |
|-------|-------|
| Full path | `C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\HOME-PAGE-FULL-MOCKUP.jpg` |
| File size | 3,686,632 bytes |
| SHA-256 | `CDD1D5BCC512B617DCF93EFA97AF88CF4AD99A0895CFC27A63C07BC704945290` |
| Width | 1398 px |
| Height | 16343 px |
| Color mode | RGB |
| Aspect ratio | 0.085541 (1398÷16343) |
| Review reference copy | `reviews/main-content/visual-audit/FP-0002-V6-HOME-FULL-MOCKUP-REFERENCE.png` |

## Hero end boundary

| Field | Value |
|-------|-------|
| Pixel Y | **902** |
| Evidence | Row mean luma jump ~114→238 across central band at Y≈903 — transition from hero photo wash to page background |
| Confidence | **CONFIRMED** |

## Section 01 start boundary

| Field | Value |
|-------|-------|
| Pixel Y | **904** |
| Evidence | First full-width light page-background band immediately below hero bottom edge; heading band begins within +28 px |
| Confidence | **HIGH** |

## Section 01 end boundary

| Field | Value |
|-------|-------|
| Pixel Y | **1494** |
| Evidence | Last card-row / section padding band before Section 02 quote block; stable page-background luma until Y≈1496 |
| Confidence | **HIGH** |

## Section 02 start boundary

| Field | Value |
|-------|-------|
| Pixel Y | **1496** |
| Evidence | Large red opening quotation mark at left margin (R−max(G,B)>100) |
| Confidence | **CONFIRMED** |

### Boundary summary table

| Boundary | Pixel Y | Visual evidence | Confidence |
|----------|--------:|-----------------|------------|
| Hero end | 902 | Luma transition hero photo → page wash | CONFIRMED |
| Section 01 start | 904 | Page wash + heading band | HIGH |
| Section 01 end | 1494 | Padding after card band before quote | HIGH |
| Section 02 start | 1496 | Red quote mark | CONFIRMED |

**Section 01 height:** 590 px (904→1494).

## Canonical crop

| Field | Value |
|-------|-------|
| Path | `reviews/main-content/visual-audit/FP-0002-V6-HOME-SECTION-01-CANONICAL-CROP.png` |
| Crop box | X 0–1398, Y 854–1544 (48 px hero context above, 48 px Section 02 context below) |
| Generator | `reviews/main-content/visual-audit/_clean-section-01-audit.py` |

## Annotated boundaries

| Field | Value |
|-------|-------|
| Path | `reviews/main-content/visual-audit/FP-0002-V6-HOME-SECTION-01-BOUNDARIES.png` |
| Marks | Hero end, S01 start/end, S02 start, container L/R |

## Section composition

Observed composition (no archived structure assumed):

1. **Page-wash background** — light cool grey-blue (`--color-page-background` candidate).
2. **Left text column** — heading, lead paragraph, bulleted list (red dot markers).
3. **Right decorative zone** — partial photographic / ribbon-like element intruding from right edge (asymmetric).
4. **Lower card band** — bordered rounded rectangles; card titling uses **numbered** treatment (red numeral visible on card 1), **not** the rejected check-circle icon row.
5. **No CTA button** in this section band.
6. **No portrait / founder figure** in Section 01 (portrait belongs to Section 02 quote block).

## Element inventory

| ID | Element | Count | Position | Size estimate | Content readable | Confidence |
|----|---------|------:|----------|---------------|------------------:|------------|
| S01-E01 | Section root / page wash | 1 | Y 904–1494 full width | 1398×590 px | N/A | CONFIRMED |
| S01-E02 | Main heading (H2-class) | 1 | Top-left in container | ~90% container width | YES | CONFIRMED |
| S01-E03 | Lead paragraph | 1 | Below heading | ~3 lines | YES | CONFIRMED |
| S01-E04 | Bulleted benefit list | 1 | Below lead | 4 unique lines + visual repeat of line 4 | PARTIAL | HIGH |
| S01-E05 | List marker (red dot) | 4+ | Per list item | ~8 px dot | N/A | CONFIRMED |
| S01-E06 | Decorative right image | 1 | Right edge, mid-section | Partial bleed | N/A | CONFIRMED |
| S01-E07 | Feature card | ≥3 | Bottom band, row 1 | ~⅓ container each | PARTIAL | HIGH |
| S01-E08 | Card border / radius | per card | Card shells | Rounded ~30 px candidate | N/A | ESTIMATED |
| S01-E09 | Card number accent | ≥1 | Card title row | Red numeral prefix | PARTIAL | HIGH |
| S01-E10 | Second card row | 0–3 | Below row 1 | NOT fully visible in crop | UNREADABLE | ESTIMATED |

## Geometry map

| Property | Value | Evidence class |
|----------|-------|----------------|
| Outer section bounds | Y 904–1494, full viewport width | CONFIRMED PIXEL EVIDENCE |
| Container left edge | X ≈ 48 px | CONFIRMED PIXEL EVIDENCE |
| Container right edge | X ≈ 1349 px | CONFIRMED PIXEL EVIDENCE |
| Text column | Left-weighted; not full symmetric center stack | CONFIRMED PIXEL EVIDENCE |
| Decorative column | Right edge overlap | CONFIRMED PIXEL EVIDENCE |
| Card columns | ≥3 in visible row | ESTIMATED FROM MOCKUP |
| Card rows | 1 confirmed visible; 2nd row | UNKNOWN |
| Section vertical padding | Generous top/bottom within 590 px band | ESTIMATED FROM MOCKUP |
| Card internal padding | Medium box padding | ESTIMATED FROM MOCKUP |
| Card radius | Large rounded corners | ESTIMATED FROM MOCKUP |
| Overlap | Decorative element overlaps section background | CONFIRMED PIXEL EVIDENCE |

Geometry map image: `reviews/main-content/visual-audit/FP-0002-V6-HOME-SECTION-01-GEOMETRY-MAP.png`

## Content readability map

| Element | Exact readable text | Partially readable | Unreadable | Source |
|---------|---------------------|--------------------|------------|--------|
| S01-E02 heading | Шпиговский дом — восстановление с уважением к личности | — | — | HOME-PAGE-FULL-MOCKUP.jpg |
| S01-E03 lead | Мы убеждены, боль может быть общей для многих, но путь восстановления всегда индивидуален. Каким бы ни был ваш опыт, через что бы вы ни проходили и какой бы образ жизни ни хотели сохранить — в «Шпиговский Дом» программа реабилитации выстраивается вокруг личности человека, его целей и его будущего. | — | — | HOME-PAGE-FULL-MOCKUP.jpg |
| S01-E04 item 1 | высокий уровень комфорта; | — | — | HOME-PAGE-FULL-MOCKUP.jpg |
| S01-E04 item 2 | анонимное лечение зависимостей; | — | — | HOME-PAGE-FULL-MOCKUP.jpg |
| S01-E04 item 3 | психотерапевтическая реабилитация; | — | — | HOME-PAGE-FULL-MOCKUP.jpg |
| S01-E04 item 4 | лечение зависимости без потери личности, статуса и связи с жизнью. | — | — | HOME-PAGE-FULL-MOCKUP.jpg |
| S01-E04 items 5–6 | Same string as item 4 repeated in mockup band | Duplicate lines visible | Whether intentional vs export artefact | HOME-PAGE-FULL-MOCKUP.jpg — **CONTENT AUTHORITY REQUIRED** |
| S01-E07 card 1 title | Starts with red **1.** prefix; body begins «В…» | Title full string | — | HOME-PAGE-FULL-MOCKUP.jpg |
| S01-E07 card 2 | — | Top border visible | Title/body | UNREADABLE |
| S01-E07 card 3 | — | Starts «В…» | Full title | PARTIAL |

Content map image: `reviews/main-content/visual-audit/FP-0002-V6-HOME-SECTION-01-CONTENT-MAP.png`

**Note:** Rejected implementation used different card chrome (`fa-check-circle`) and different card titles (`Реабилитация без изоляции`, etc.). Clean audit does **not** treat rejected card copy as mockup authority.

## Asset candidates

| Visual role | Exact matching asset | Candidate asset | Missing | Decision |
|-------------|---------------------|-----------------|---------:|----------|
| Logo / brand | N/A in section | — | N/A | NOT IN SECTION |
| Card check icon (rejected) | NOT in mockup band | — | YES | **REJECT** — mockup shows numbered cards |
| Red list dot | CSS pseudo-element | `--color-accent` dot | NO | CANDIDATE |
| Decorative right image | — | UNREADABLE crop | YES | **MISSING** — operator asset gate |
| Card border/radius | — | `--radius-main`, `--border-color-subtle` | NO | CANDIDATE tokens |
| Section photo / portrait | — | — | N/A | NOT IN SECTION 01 |

## Color roles

| Role | Mockup observation | Existing token candidate |
|------|---------------------|-------------------------|
| Section background | Light cool grey-blue wash | `--color-page-background` |
| Heading | Dark blue-grey | `--color-text-primary` |
| Body / lead | Medium grey | `--color-text-secondary` |
| Accent (dots, card numbers) | Red | `--color-accent` |
| Card surface | White / near-white | `--color-surface` |
| Card border | Subtle grey | `--border-color-subtle` |

## Typography roles

| Role | Observation | Token candidates |
|------|-------------|------------------|
| Section heading | Large bold sans | `--font-size-h2`, `--font-weight-heading`, `--line-height-h2` |
| Lead | Base size, regular | `--font-size-base`, `--line-height-base` |
| List items | Base size | `--font-size-base`, `--line-height-base` |
| Card titles | Bold, numbered prefix | `--font-size-base`, `--font-weight-heading` |
| Card body | Small / secondary | `--font-size-small`, `--line-height-small` |

## Existing token candidates

Likely applicable (not final binding):

```text
--pad-y
--pad-gap
--pad-gap-line
--pad-gap-tight
--pad-gap-mini
--pad-box
--pad-x
--container-main
--radius-main
--radius-full
```

## Confirmed facts

- Sole JPG checksum matches recorded identity.
- Hero ends Y=902; Section 01 occupies Y 904–1494; Section 02 begins Y=1496.
- Section contains heading + lead + bulleted list + lower card band.
- Asymmetric right-side decorative element present.
- Rejected 3×2 check-icon card grid is **not** visually confirmed as mockup structure.
- No CTA in Section 01.

## Estimated facts

- Container edges ≈ 48 px / 1349 px at 1398 px mockup width.
- ≥3 cards in one visible row; second row count unknown.
- Card radius aligns with `--radius-main` (~30 px).
- Vertical rhythm uses existing pad tokens.

## Unknowns

- Exact card count (3 vs 6 vs other).
- Full card titles and bodies (partially cropped / small type).
- Whether list items 5–6 duplicates are intentional in design source.
- Exact decorative right asset (file, crop, positioning).
- Mobile layout for Section 01 (not in this JPG crop authority).
- Final column ratio text vs decorative zone.

## Prohibited assumptions

- 3×2 grid with six cards.
- Row-2 duplication to fill card slots.
- Font Awesome check-circle card icons.
- Archived GROUP-01 structure.
- Rejected commit as design reference.
- Old spec text for card titles.

## Implementation blockers

1. Operator approval of canonical crop and boundaries.
2. Card count and row structure confirmation.
3. Full card copy authority (partially unreadable).
4. Decorative right asset identification.
5. List duplicate lines (items 5–6) — operator content decision.
6. New Block Implementation Specification after approval.

## Questions requiring operator decision

1. Are list lines 5–6 intentional in design or export duplication?
2. What is the authoritative card count and row layout?
3. Provide or approve decorative right-edge asset.
4. Confirm numbered card treatment vs any icon system.
5. Approve boundary Y values (902 / 904 / 1494 / 1496) for implementation spec.

## Implementation authorization status

```text
IMPLEMENTATION AUTHORIZATION — NOT GRANTED
AWAITING OPERATOR REVIEW
NEW SECTION 01 HTML — NOT STARTED
NEW SECTION 01 SCSS — NOT STARTED
SECTION 02 — BLOCKED
```
