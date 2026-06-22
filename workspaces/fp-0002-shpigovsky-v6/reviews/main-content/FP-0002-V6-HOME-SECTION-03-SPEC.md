# FP-0002 V6 HOME SECTION 03 SPEC

## Sole visual authority

`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`  
SHA-256: `CDD1D5BCC512B617DCF93EFA97AF88CF4AD99A0895CFC27A63C07BC704945290`

## Boundaries

| Edge | Y (1398 canvas) | Confidence |
|------|----------------:|------------|
| Section 02 end | 2610 | CONFIRMED |
| Section 03 start | 2610 | CONFIRMED |
| Section 03 content start | 2634 | HIGH |
| Section 03 content end | 3747 | HIGH |
| Section 03 end | 3740 | CONFIRMED |
| Section 04 start | 3740 | CONFIRMED — «Нас выбирают» heading band |

Evidence: `reviews/main-content/section-03-audit/FP-0002-V6-SECTION-03-BOUNDARY-META.json`

## Canonical crop

`reviews/main-content/section-03-audit/FP-0002-V6-SECTION-03-CANONICAL-CROP.png`

## Composition

Desktop block inside `.container`:

1. Header row — H2 + «Смотреть все» link with accent arrow
2. Lead paragraph with 3px left accent bar
3. Vertical accordion — 4 category rows; first row expanded with 4 service sub-lines (dotted leader + arrow)
4. Bottom photo-card row in mockup — **excluded** (decorative policy; no exact approved content assets)

## Exact content

| Element | Text |
|---------|------|
| H2 | Лечение и профилактика |
| View-all | Смотреть все |
| Lead | Мы работаем с зависимостью не как с проступком, а как с состоянием, у которого есть биологические, психологические и социальные причины. |
| Category 1 | Зависимости и пристрастия |
| Sub 1 | Алкогольная зависимость |
| Sub 2 | Наркотическая зависимость |
| Sub 3 | Лекарственная зависимость |
| Sub 4 | Поведенческие зависимости |
| Category 2 | Психическое здоровье |
| Category 3 | Расстройства пищевого поведения |
| Category 4 | Генотипирование |

Authority: canonical JPG readable text; lead cross-check FIG node `1:971`.

## Repeated item count

| Item | Count |
|------|------:|
| Accordion categories | 4 |
| Expanded sub-service lines | 4 |
| View-all links | 1 |

## Content assets

NONE — text + Font Awesome UI icons only.

## Decorative images excluded

| Item | Decision |
|------|----------|
| Section background lifebuoy watermark | DO NOT IMPLEMENT |
| Bottom 4 photo cards | DO NOT IMPLEMENT — no exact approved assets; decorative JPG row |
| Service sub-line arrows | Font Awesome icon — UI chrome, not raster decor |

## Container

Standard `.container` only.

## Existing typography

`--font-size-h2`, `--line-height-h2`, `--font-size-base`, `--line-height-base`, `--font-size-small`, `--line-height-small`, `--font-size-nav`, `--font-weight-heading`, `--font-weight-button`

## Existing colors

`--color-text-primary`, `--color-text-secondary`, `--color-accent`, `--color-border-subtle`

## Existing spacing

`--pad-gap`, `--pad-gap-line`, `--pad-gap-tight`

## Existing radii

`--radius-full`

## Existing buttons

Not used — accordion toggles only; view-all is text link.

## Unique geometry

| Value | Role | Evidence |
|------:|------|----------|
| 15px | view-all link size | FIG `1:962` / mockup header link |
| 3px | lead accent bar | mockup lead left rule |
| 26px | accordion chevron circle | FIG `1:1216` 26×26 |

## HTML structure

```text
section.home-treatment-prevention
└── div.container
    ├── div.home-treatment-prevention__head
    ├── p.home-treatment-prevention__lead
    └── div.home-treatment-prevention__accordion[data-accordion]
        └── 4 × div.home-treatment-prevention__item[data-accordion-item]
```

Partial: `src/partials/sections/home-treatment-prevention.html`

## SCSS placement

`src/scss/style.scss` block `10c. Home treatment prevention` after Section 02, before Footer.

## JS scope

Minimal accordion toggle in `src/js/main.js` — single-open, `data-accordion*` hooks.

## Responsive scope

Desktop pixel-perfect target viewport 1398. Mobile: BASIC RESPONSIVE SAFETY — stacked header, simplified service rows without dotted leaders.

## Acceptance gate

```text
PASS — accordion text authority sufficient; decorative image row excluded by policy
```
