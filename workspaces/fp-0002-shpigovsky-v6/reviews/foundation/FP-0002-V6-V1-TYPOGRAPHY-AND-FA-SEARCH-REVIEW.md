# FP-0002 V6 V1 TYPOGRAPHY AND FONT AWESOME SEARCH REVIEW

**Task:** Production typography recovery from V1 + Font Awesome search integration  
**Checkpoint before:** `c7453aa7f900cdc8e2322c26659e649483230cb6`  
**Visual authority:** `HOME-PAGE-FULL-MOCKUP.jpg` SHA-256 `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290`

## Scope

Restore V1 production font (Inter) and typography colors/scale where reconciled with JPG; integrate FA Pro search as eighth nav item; preserve Header/Hero geometry; no JS; no responsive.

## Operator exception

V1 accessed **only** for typography recovery.

**Allowed:** font sources, font files, font-family, font sizes, line-height, weights, typography colors.  
**Forbidden:** layout, geometry, spacing, component structure, responsive behavior, Header/Hero positioning and section composition.

## V1 sources inspected

| Source | Type | Relevant typography data | Used |
| ------ | ---- | ------------------------ | ---- |
| `workspaces/fp-0002-shpigovsky-frontend/src/pages/desktop-shell.html` | HTML head | Google Fonts Inter `wght@300;400;500;600;700`, `display=swap` | YES |
| `workspaces/fp-0002-shpigovsky-frontend/src/scss/utils/_tokens.scss` | SCSS tokens | `$font-family-primary: 'Inter'…`, global type scale, weights | YES (family/weights; sizes reconciled with JPG) |
| `workspaces/fp-0002-shpigovsky-frontend/src/scss/base/_base.scss` | SCSS base | body 18px/300, heading scale | PARTIAL (family only; V6 JPG sizes kept) |
| `workspaces/fp-0002-shpigovsky-frontend/src/scss/sections/_site-header.scss` | SCSS block | Inter on contacts/nav; nav 16px; phones 20px/500 | PARTIAL (family; V6 JPG block sizes kept) |
| `workspaces/fp-0002-shpigovsky-frontend/src/scss/sections/_hero.scss` | SCSS block | tagline Inter 36/700; H1 Libertinus Serif 70px | REJECTED for scale (JPG: 16px tagline, 40px H1 Inter) |
| `workspaces/fp-0002-shpigovsky-frontend/src/pages/desktop-ui-demo.html` | HTML head | Inter `wght@300;400;500` subset | NO (superseded by shell production URL) |
| `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` | Doc | Inter approved, Google Fonts | CONFIRMATION |
| `workspaces/fp-0002-shpigovsky-v2/src/pages/index.html` | HTML | Inter Google Fonts 300;400;500 | NO (not V1 production workspace) |
| `workspaces/fp-0002-shpigovsky-v5/src/partials/layout/head.html` | HTML | Open Sans | NO (wrong family) |

## V1 font identification

| Role | Family |
| ---- | ------ |
| base | Inter |
| headings | Inter (global); Libertinus Serif in V1 hero only |
| display | Inter (V1 tokens); Libertinus Serif in V1 hero H1 |

**Connection:** Google Fonts `<link>` — no local webfont files in V1 workspace.

## Font connection method

**Variant B — Google Fonts from V1 production shell.**

## Font files or external URLs

```
https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap
```

Preconnect: `fonts.googleapis.com`, `fonts.gstatic.com` (crossorigin).

## Font weights

**Loaded:** 300, 400, 500, 600, 700  
**SECTION-001 used:** 400 (body, nav, meta, hero tagline/H1), 500 (CTAs), 600 (phones)

## V1 typography inventory

| Role | Font family | Size | Line-height | Weight | Color | Source |
| ---- | ----------- | ---: | ----------: | -----: | ----- | ------ |
| body | Inter | 18px | 28px | 300 | #475371 | V1 `_base.scss` |
| small/meta | Inter | 14px | 20px | 400 | #475471 | V1 header region |
| Header address | Inter | 14px | 1.4 | 300 | #475471 | V1 `_site-header.scss` |
| Header schedule | Inter | 14px | 1.4 | 300 | #475471 | V1 `_site-header.scss` |
| Header phones | Inter | 20px | 1.4 | 500 | #475471 | V1 `_site-header.scss` |
| navigation | Inter | 16px | 22px | 400 | #475471 | V1 `_site-header.scss` |
| Header CTA | Inter | 15px | 1.4 | 500 | #fff | V1 `_site-header.scss` |
| Hero tagline | Inter | 36px | 1 | 700 | #fff | V1 `_hero.scss` |
| Hero H1 | Libertinus Serif | 70px | 1 | 600 | #fff | V1 `_hero.scss` |
| Hero CTA | Inter | 16px | 20px | 500 | #fff | V1 tokens |
| H1 global | Inter | 70px | 84px | 500 | #475371 | V1 tokens |
| H2 global | Inter | 36px | 44px | 500 | #475371 | V1 tokens |
| H3 global | Inter | 30px | 36px | 500 | #475371 | V1 tokens |

## V6 typography decisions

Priority applied: **JPG → V1 production → V6 proposals**.

| Role | V6 decision | Status |
| ---- | ----------- | ------ |
| All SECTION-001 text | Inter family | APPROVED_V1_PRODUCTION |
| body | 16px / 1.25 / 400 | APPROVED_JPG |
| Header meta | 14px / 1.2 / 400 | APPROVED_JPG (size over V1 1.4 LH) |
| phones | 18px / 600 | APPROVED_JPG (size over V1 20px/500) |
| nav | 15px / 1.2 / 400 | APPROVED_JPG (size over V1 16px) |
| Header CTA | 12px / 500 | APPROVED_JPG |
| Hero tagline | 16px / 1.25 / 400 | APPROVED_JPG (over V1 36/700) |
| Hero H1 | 40px / 1.15 / 400 Inter | APPROVED_JPG (over V1 Libertinus 70px) |
| Hero CTA | 13px / 500 | APPROVED_JPG |
| H2 / H3 tokens | 28px / 22px | PROPOSED (no DOM on index yet) |

## Color decisions

V6 SECTION-001 colors retained (JPG authority): `#475471` primary, `#6d7b8f` secondary, `#fff` inverse, `rgb(149, 47, 43)` accent. V1 `#475371` / `#8d9097` not substituted.

## Root token changes

| Token | Before | After | Status |
| ----- | ------ | ----- | ------ |
| `--font-family-base` | system-ui stack | `'Inter', system-ui…` | APPROVED_V1_PRODUCTION |
| `--font-weight-medium` | — | 500 | APPROVED_V1_PRODUCTION |
| `--font-weight-semibold` | — | 600 | APPROVED_V1_PRODUCTION |
| Size tokens | unchanged | unchanged | APPROVED_JPG |

## Header typography

Inter applied via tokens on address, schedule, phones, nav, CTA, search control. Geometry unchanged (`max-width: 1220px`, `padding-top: 18px`, `padding-inline: 40px`).

## Hero typography

Inter on tagline, H1, CTA. `max-width: 1360px` and intrinsic image ratio unchanged.

## Font Awesome search icon selection

| Variant | Assessment |
| ------- | ---------- |
| `fas fa-search` | Solid glyph — matches prior `search.svg` extracted from `fa-solid-900.svg`; JPG Header QA PASS |
| `far fa-search` | Regular outline — thinner than prior approved asset |
| `fal fa-search` | Light — too thin for JPG icon weight |

**Selected:** `fas` — class `fas fa-search`. Reason: continuity with approved JPG visual QA and solid FA Pro source used for prior SVG extraction.

## Search navigation structure

**Before:** 7 nav `<li>` + sibling `button.site-header__search` with `img.search.svg`  
**After:** 8 nav `<li>`; eighth is `site-header__nav-item--search` > `button.site-header__search` > `i.fas.fa-search`

Navigation item count: **8**. Search index: **8** (last).

## Old SVG status

`src/img/icons/search.svg` — **DELETED** (only Header usage; no other references).

## Computed styles

Captured: `reviews/foundation/visual/_typography-computed-styles.json`

| Element | Expected family | Computed family | Size | Line-height | Weight | Status |
| ------- | --------------- | --------------- | ---: | ----------: | -----: | ------ |
| body | Inter | Inter, system-ui… | 16px | 20px | 400 | PASS |
| Header address | Inter | Inter… | 14px | 16.8px | 400 | PASS |
| Header schedule | Inter | Inter… | 14px | 16.8px | 400 | PASS |
| nav link | Inter | Inter… | 15px | 18px | 400 | PASS |
| phone | Inter | Inter… | 18px | 21.6px | 600 | PASS |
| Header CTA | Inter | Inter… | 12px | 12px | 500 | PASS |
| Hero tagline | Inter | Inter… | 16px | 20px | 400 | PASS |
| Hero H1 | Inter | Inter… | 40px | 46px | 400 | PASS |
| Hero CTA | Inter | Inter… | 13px | 13px | 500 | PASS |
| global H2 | Inter | missing (no h2 in DOM) | — | — | — | SAFE_UNKNOWN |
| global H3 | Inter | missing (no h3 in DOM) | — | — | — | SAFE_UNKNOWN |

## Visual regression

Screenshot: `reviews/foundation/visual/FP-0002-V6-PRODUCTION-TYPOGRAPHY-SECTION-001.png` @ 1398×1000.

Header/Hero geometry metrics match pre-task foundation QA (`header_container` 1220×186, `hero_root` 1360×759.891).

## Correction pass

**None required.** Inter loading confirmed; no text overlap or geometry shift observed.

## Header geometry lock

**PRESERVED** — container 1220px, padding 18px/40px, row structure unchanged.

## Hero geometry lock

**PRESERVED** — max-width 1360px, intrinsic image height, panel/CTA dimensions unchanged.

## JS lock

**UNCHANGED** — no JS files modified.

## Responsive lock

**UNCHANGED** — desktop-only; no layout breakpoints added.

## SAFE UNKNOWN

- `header-search-action` — search behavior not implemented
- Global H2/H3 computed validation deferred until content sections exist
- V1 hero Libertinus Serif display face not restored (JPG authority uses Inter for hero H1)

## Build result

`npm run build` — **SUCCESS**

## Final verdict

**READY FOR OPERATOR REVIEW** — Production typography restored (Inter connected), FA search integrated as last nav item, Header/Hero geometry preserved.
