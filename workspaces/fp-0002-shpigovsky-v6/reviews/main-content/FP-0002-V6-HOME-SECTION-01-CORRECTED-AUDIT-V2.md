# FP-0002 V6 HOME SECTION 01 — CORRECTED AUDIT V2

**Audit date:** 2026-06-23  
**Status:** CROP V2 COMPLETE — IMPLEMENTATION AUTHORIZED BY TASK

## Reason for re-audit

Operator rejected V1 clean visual audit and prior `home-intro-mission` implementation. V1 crop ended at Y=1494/1496, cutting through card row; boundaries, content map, and geometry map were invalid.

## Rejected V1 crop

| Field | V1 (REJECTED) | V2 (CORRECTED) |
|-------|---------------|----------------|
| Section 01 end Y | 1494 | **1491** |
| Section 02 start Y | 1496 (through cards) | **1491** (quote block top) |
| Card rows in crop | Partial / cut | **1 full row (3 cards)** |
| Card count assumed | 6 (3×2 estimated) | **3 measured** |
| Decorative object | Cut / missing asset | **Full height in crop** |

## Sole visual authority

```text
workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg
```

## Mockup identity

| Field | Value |
|-------|-------|
| SHA-256 | `CDD1D5BCC512B617DCF93EFA97AF88CF4AD99A0895CFC27A63C07BC704945290` |
| Width | 1398 px |
| Height | 16343 px |
| Match prior canonical | YES |

## Wide context crop

| Field | Value |
|-------|-------|
| Path | `reviews/main-content/visual-audit-v2/FP-0002-V6-HOME-SECTION-01-WIDE-CONTEXT.png` |
| Y range | 842–1841 |
| Includes | Hero tail, full Section 01, quote block start |

## Canonical crop V2

| Field | Value |
|-------|-------|
| Path | `reviews/main-content/visual-audit-v2/FP-0002-V6-HOME-SECTION-01-CANONICAL-CROP-V2.png` |
| Y range | 854–1539 |
| Crop gate | **PASS** |

## Hero end

| Field | Value |
|-------|-------|
| Y | **902** |
| Evidence | Luma jump hero photo wash → page background |
| Confidence | **CONFIRMED** |

## Section 01 start

| Field | Value |
|-------|-------|
| Y | **904** |
| Evidence | First full-width light page-background band below hero |
| Confidence | **HIGH** |

## Section 01 content zones

| Zone | Y range | Confidence |
|------|---------|------------|
| Heading | 932–1041 | CONFIRMED |
| Intro paragraph | 1049–1150 | CONFIRMED |
| Benefits list | 1089–1194 | CONFIRMED |
| Decorative (right) | 924–1395 | CONFIRMED |

## Card zone start

| Field | Value |
|-------|-------|
| Y | **1195** |
| Evidence | Top border of first (and only) card row |
| Confidence | **CONFIRMED** |

## Card zone end

| Field | Value |
|-------|-------|
| Y | **1415** |
| Evidence | Bottom padding after card bodies |
| Confidence | **CONFIRMED** |

## Section 01 end

| Field | Value |
|-------|-------|
| Y | **1491** |
| Evidence | Last page-wash padding row before quote composition |
| Confidence | **CONFIRMED** |

## Section 02 start

| Field | Value |
|-------|-------|
| Y | **1491** |
| Evidence | Red opening quotation mark at x≈175 |
| Confidence | **CONFIRMED** |

## Heading

**Text (CONFIRMED):** Шпиговский дом — восстановление с уважением к личности

## Intro paragraph

**Text (CONFIRMED):** Мы убеждены, боль может быть общей для многих, но путь восстановления всегда индивидуален. Каким бы ни был ваш опыт, через что бы вы ни проходили и какой бы образ жизни ни хотели сохранить — в «Шпиговский Дом» программа реабилитации выстраивается вокруг личности человека, его целей и его будущего.

## List

Four unique items (CONFIRMED). Mockup band shows six lines with items 5–6 duplicating item 4 — treated as export duplication; implementation uses four unique lines only.

1. высокий уровень комфорта;
2. анонимное лечение зависимостей;
3. психотерапевтическая реабилитация;
4. лечение зависимости без потери личности, статуса и связи с жизнью.

## Decorative object

| Field | Value |
|-------|-------|
| Role | Right-edge ribbon / lifebuoy-style graphic |
| Crop | `visual-audit-v2/decor-crop/section-01-decor-right.png` |
| Active asset | `src/img/decor/home-recovery-intro-decor.png` (JPG-derived) |
| Confidence | **HIGH** |

## Card count

**3** — one full row visible; no second row in canonical JPG band Y 904–1491.

## Card columns

**3**

## Card rows

**1**

## Card content readability

| Card | Title | Body | Confidence |
|------|-------|------|------------|
| 1 | Реабилитация без изоляции | Full paragraph readable | CONFIRMED |
| 2 | Участие семьи и близких | Full paragraph readable | CONFIRMED |
| 3 | Выявление и устранение причины зависимости | Full paragraph readable | CONFIRMED |

Card chrome: red checkmark icon (not numbered prefix). V1 clean audit numbered-card claim **REJECTED**.

## Exact texts

All heading, lead, list (×4), card titles and bodies recorded in this audit and HTML partial — sourced from canonical JPG diagnostic crops.

## Unreadable texts

NONE for implemented elements.

## Asset mapping

| Role | Path |
|------|------|
| Decorative right | `src/img/decor/home-recovery-intro-decor.png` |
| Card icon | Font Awesome `fa-check-circle` (project vendor bridge) |

## Existing token mapping

```text
--pad-x, --pad-y, --pad-gap, --pad-gap-line, --pad-gap-tight, --pad-gap-mini, --pad-box
--radius-main, --radius-full
--color-page-background, --color-text-primary, --color-text-secondary, --color-accent, --color-surface
--border-color-subtle, --font-size-h2, --font-size-base, --font-size-small
```

## Unique geometry evidence

| Value | Evidence |
|-------|----------|
| Section padding-top 28px | Y 904→932 |
| Section padding-bottom 76px | Y 1415→1491 |
| Card grid gap 16px | Card box x gaps in JPG |
| Card min-height ~200px | Card box height 200px @ 1398 mockup |
| Decor width 382px | Decor crop width |

## Implementation blockers

NONE — all required facts confirmed.

## Implementation authorization

```text
IMPLEMENTATION AUTHORIZATION — GRANTED BY TASK
```

Maps: `visual-audit-v2/FP-0002-V6-HOME-SECTION-01-BOUNDARIES-V2.png`, `CONTENT-MAP-V2.png`, `GEOMETRY-MAP-V2.png`, meta `FP-0002-V6-HOME-SECTION-01-BOUNDARY-META-V2.json`.
