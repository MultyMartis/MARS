# FP-0002-PG-004 — GROUP 1 Implementation Plan v1

## Boundary

- **Start:** page shell open — `header`
- **End:** after `cta-01` band (before «Признаки алкогольной зависимости» heading)
- **Desktop Y (PNG):** ~Y0–1820 (crop evidence `SERVICE-LEAF-DESKTOP-GROUP1-*`)
- **Figma nodes:** `1:1749` hero, `1:1816` intro, `1:1847`/`1:1867` upper content + CTA

## Desktop crops (design authority)

1. `SERVICE-LEAF-DESKTOP-GROUP1-HEADER-HERO-NAV.png`
2. `SERVICE-LEAF-DESKTOP-GROUP1-UPPER-CONTENT-CTA.png` (truncate at CTA bottom for acceptance)
3. Runtime-before: N/A (page not created)
4. Runtime-after: `SERVICE-LEAF-G1-HEADER-HERO-1398.png`, `SERVICE-LEAF-G1-UPPER-CTA-1398.png`

## Mobile crops

1. `SERVICE-LEAF-MOBILE-GROUP1-HEADER-HERO-NAV.png`
2. `SERVICE-LEAF-MOBILE-GROUP1-UPPER-CONTENT-CTA.png`
3. Runtime-after: `SERVICE-LEAF-G1-HEADER-HERO-390.png`, `SERVICE-LEAF-G1-UPPER-CTA-390.png`

## Visible text regions

- Hero eyebrow, title, lead, CTA label (REAL_COPY)
- Breadcrumb trail + 6 anchor labels (REAL_COPY)
- Intro H2 + red-line quote (REAL_COPY)
- Bordered panel 3 subheads + bodies (REAL_COPY)
- CTA: Запишитесь на встречу / ЗАПИСАТЬСЯ / phone (REAL_COPY)
- **Exclude:** «Признаки…» heading and below

## Assets

- Hero image: **EXACT_EXPORT_REQUIRED** (`1:1753`)
- Lifebuoy in bordered block: visible in PNG — **REQUIRES_GROUP_INSPECTION** vs project lifebuoy policy (`FORBIDDEN_ZERO` on subdivision — leaf PNG shows decor; do not omit without operator ruling)

## Reuse

| Block | Partial | Decision |
| ----- | ------- | -------- |
| header | layout/header | REUSE_EXACT |
| hero | services-inner-hero-v2 | REUSE_WITH_CONTENT |
| breadcrumbs | breadcrumbs | REUSE_WITH_CONTENT |
| subnav | services-page-subnav | REUSE_WITH_CONTENT |
| intro-quote | NEW `service-leaf-intro-v1` | NEW |
| bordered-info | NEW `service-leaf-bordered-info-v1` | NEW |
| cta-01 | services-program-cta-band-v2 | REUSE_WITH_CONTENT |

## Source files (future — not created in pass opening)

- Page: `src/pages/usluga-konechnaya-v1.html`
- New partials: `service-leaf-intro-v1.html`, `service-leaf-bordered-info-v1.html`
- SCSS: additions in `src/scss/style.scss` only — scoped `.service-leaf-*` / page root `.page-service-leaf-v1`
- JS: existing modal hooks via `data-*` only

## Preview URL

`http://127.0.0.1:4174/usluga-konechnaya-v1.html` (after GROUP 1+ shell)

## Compiled checks

- `npm run build` exit 0
- dist contains `usluga-konechnaya-v1.html`
- no regressions: index, uslugi, uslugi-v2, usluga-podrazdel-v1

## Acceptance screenshots

- Desktop 1398px: hero + upper nav + intro + bordered + CTA
- Mobile 390px: same regions
- Text transcript PASS all visible strings

## Commit gate

Commit only if: backup exists, design crops PASS, runtime-after PASS, regression 0, build 0.

**Result:** READY
