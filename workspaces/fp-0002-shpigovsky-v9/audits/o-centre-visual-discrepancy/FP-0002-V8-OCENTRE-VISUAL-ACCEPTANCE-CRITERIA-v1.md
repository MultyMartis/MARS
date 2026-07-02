# FP-0002 V8 O-Centre Visual Acceptance Criteria v1

## Composition

- Canonical visual order matched (see block-order reconciliation)
- Missing major regions = 0 (first CTA, who-we-treat visuals, clinic landscape, decorative backgrounds where required)
- Extra major regions = 0
- Founder placement inside institutional context
- Infrastructure semantic grouping matches Figma subgroups (not auto-collage)

## Desktop (1437px)

- Region order drift = 0 for major blocks
- Full-page height delta documented and explained by restored subregions (target: within 5% of 12830px after correction, excluding V8 header chrome delta)
- Container widths follow V8 canon (1170 content / 1422 bleed patterns)
- Decorative layers present at `1:2440` / mobile equivalent where audit marked required

## Mobile (390px frame / 380px content)

- Block order matches mobile Figma frames
- Mobile-only assets 19/20 visible; desktop-only assets hidden per map
- No horizontal overflow on 320–390px captures

## Content

- Lorem = 0 in rendered HTML
- Invented content = 0
- Typo `Шпиговсикй` unchanged unless operator explicitly authorizes fix against Figma
- No phantom Steps / no FAQ accordion

## Regression

- Shared components unchanged except page-scoped wrappers
- Home / services / manual polish regression = 0

## Operator review

- Visual gate PASS required before deployment, stable tag, or WordPress
