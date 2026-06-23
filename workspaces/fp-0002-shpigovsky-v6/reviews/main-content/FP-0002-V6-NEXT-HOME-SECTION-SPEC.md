# FP-0002 V6 NEXT HOME SECTION SPEC

## Reviews stable release

`FP-0002-V6-REVIEWS-OPERATOR-STABLE-01` / tag `fp-0002-v6-reviews-operator-stable-01`

## Sole visual authority

`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`  
SHA-256: `CDD1D5BCC512B617DCF93EFA97AF88CF4AD99A0895CFC27A63C07BC704945290`

## Semantic identity

`home-rehabilitation-requirements` — «Что нужно для прохождения реабилитации и лечения» (Figma frame «С чего начать»)

## Boundaries

| Field | Y |
|-------|---:|
| Reviews end | 7136 |
| Next section start | 7136 |
| Content start | 7160 |
| Content end | 8448 |
| Next section end | 8824 |
| Following section start | 8824 (programs) |

Gate: **PASS**

## Canonical crop

`reviews/main-content/next-section-audit/FP-0002-V6-NEXT-SECTION-CANONICAL-CROP.png`

## Exact composition

1. H2 with red accent bar  
2. Intro paragraph  
3. Four numbered steps (01–04)  
4. Dark CTA band (lead + phone + button)  
5. Interior corridor photograph

## Exact content

Figma SECTION-06 texts + JPG-derived CTA lead; phone from approved project shell (`8 (925) 183-64-64`).

## Repeated item count

Steps: **4**

## Content assets

`src/img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp` (JPG crop BLOCK-017)

## Existing component mapping

| Needed role | Existing component/style | Reuse |
| ----------- | ------------------------ | ----- |
| Container | `.container` | YES |
| H2 | `.home-why-us__heading` pattern | YES |
| Accent bar | `.home-why-us__lead` border-left | YES |
| Step title | `--font-size-h3` | YES |
| Body | 16px/20px card body | YES |
| CTA button | `.btn.btn_dark.btn--primary` | YES |
| Dark band fill | `--color-text-primary` | YES |
| Photo bleed | `.home-clinic-landscape__*` | YES |
| Radius | `--radius-main`, `--radius-full` | YES |

## Existing typography

`--font-size-h2`, `--font-size-h3`, `--font-size-base`, `--font-size-small`, `--font-weight-heading`

## Existing colors

`--color-text-primary`, `--color-text-secondary`, `--color-text-inverse`, `--color-accent`

## Existing spacing

`--pad-gap`, `--pad-gap-line`, `--pad-gap-tight`

## Existing radii

`--radius-main`, `--radius-full`

## Existing buttons

`.btn`, `.btn_dark`, `.btn--primary`

## Unique geometry

| Value | Evidence |
|-------|----------|
| Step disc 48×48px | JPG CMP-010 |
| Interior height 388px desktop | JPG BLOCK-017 crop |
| Interior height 220px mobile | Scaled like clinic landscape |
| CTA phone 40px | Footer phone scale in dark band |

## HTML structure

`section.home-rehabilitation-requirements` → `.container` → H2, intro, `ol` steps, CTA band, figure photo

## SCSS placement

After Reviews (`10i`), before Footer (`11`) in `src/scss/style.scss`

## JS scope

None required

## Responsive scope

Mobile: CTA stack single column; photo height 220px. **Mobile status: BASIC RESPONSIVE SAFETY**

## Implementation gate

All gates **PASS**
