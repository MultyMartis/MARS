# FP-0002 V6 HOME SECTION 02 SPEC

## Sole visual authority

`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`  
SHA-256: `CDD1D5BCC512B617DCF93EFA97AF88CF4AD99A0895CFC27A63C07BC704945290`

## Section boundaries

| Edge | Y (1398 canvas) | Confidence |
|------|----------------:|------------|
| Section 01 end | 2120 | CONFIRMED — after operator 3×2 card grid |
| Section 02 start | 2130 | CONFIRMED |
| Section 02 content start | 2154 | HIGH |
| Section 02 content end | 2586 | HIGH |
| Section 02 end | 2610 | CONFIRMED |
| Section 03 start | 2610 | HIGH |

Evidence: `reviews/main-content/section-02-audit/FP-0002-V6-SECTION-02-BOUNDARY-META.json`

## Canonical crop

`reviews/main-content/section-02-audit/FP-0002-V6-SECTION-02-CANONICAL-CROP.png`

## Exact composition

Two-column desktop layout inside `.container`:

- Left: large red opening quote mark + 4 quote paragraphs
- Right: founder portrait (content image) + overlapping author card (name, role, outline CTA)

## Exact content

| Element | Text |
|---------|------|
| Quote p1 | Мы создавали «Шпиговский Дом» как место, где человек может получить профессиональную помощь, не теряя связь с собственной жизнью. |
| Quote p2 | Многие боятся обратиться за лечением, потому что опасаются потерять семью, работу и привычный уклад жизни. |
| Quote p3 | Мы считаем, что современная реабилитация должна помогать человеку восстанавливать себя, сохраняя то, что для него действительно важно. |
| Quote p4 | «Наша цель — создать безопасное пространство для изменений. Наша задача — не изолировать человека от жизни, а помочь ему вернуть контроль над ней.» |
| Name | Сергей Юрьевич Шпиговский |
| Role | Основатель центра. Аддиктолог, интервенционист |
| CTA | Записаться на консультацию |

Authority: canonical JPG readable text; cross-checked against operator project copy for BLK-022.

## Content images

| Asset | Path | Role |
|-------|------|------|
| Founder portrait | `src/img/content/founder-sergey-shpigovsky.png` | Semantic content image cropped from canonical JPG portrait zone |

## Decorative images excluded

| Item | Decision |
|------|----------|
| Background red cross watermark | DO NOT IMPLEMENT DECORATIVE IMAGE |

## Container usage

Standard `.container` only.

## Existing colors

`--color-page-background`, `--color-text-primary`, `--color-text-secondary`, `--color-accent`, `--color-surface`, `--color-text-inverse`

## Existing typography

`--font-size-base`, `--line-height-base`, `--font-size-small`, `--line-height-small`, `--font-weight-heading`

## Existing spacing tokens

`--pad-y`, `--pad-gap`, `--pad-gap-line`, `--pad-gap-tight`

## Existing radius tokens

`--radius-main`, `--radius-full`

## Existing button system

`.btn` outline variant scoped with `--color-accent` border

## Unique geometry

| Value | Role | Evidence |
|------:|------|----------|
| 24px | column gap | mockup split 696→720 |
| 72px | quote mark size | mockup quote_mark zone height |
| 630px | author card max-width | mockup author_block width 720→1350 |

## HTML structure

```text
section.home-founder-quote
└── div.container
    └── div.home-founder-quote__layout
        ├── blockquote.home-founder-quote__quote
        └── figure.home-founder-quote__figure
            ├── img.home-founder-quote__photo
            └── figcaption.home-founder-quote__author
```

Partial: `src/partials/sections/home-founder-quote.html`

## SCSS placement

`src/scss/style.scss` block `10b. Home founder quote` after Section 01, before Footer.

## JS scope

NONE

## Responsive scope

Desktop pixel-perfect target viewport 1398. Mobile: BASIC RESPONSIVE SAFETY — single column stack, static author card.

## Acceptance criteria

- [x] Section 02 fully visible in crop
- [x] Boundaries confirmed against canonical JPG
- [x] Exact text authority sufficient
- [x] Content portrait identified
- [x] Decorative watermark excluded
- [x] No placeholders
- [x] No archived visual authority used
- [x] Section 01 untouched
