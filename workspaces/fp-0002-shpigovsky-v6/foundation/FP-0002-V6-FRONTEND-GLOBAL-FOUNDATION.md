# FP-0002 V6 Frontend Global Foundation

**Project:** FP-0002 Shpigovsky V6  
**Status:** READY FOR OPERATOR REVIEW (production typography restored)  
**Checkpoint before:** `c7453aa7f900cdc8e2322c26659e649483230cb6`

---

## Source order (`style.scss`)

```text
utils/variables
→ base/fonts
→ base/root
→ base/reset
→ base/base
→ base/typography
→ vendors/fontawesome
→ layout/header
→ sections/hero
```

## File responsibilities

| File | Role |
|------|------|
| `utils/_variables.scss` | Compile-time paths, spacing aliases, Sass→CSS var bridges |
| `base/_fonts.scss` | Project `@font-face` (empty until font files supplied) |
| `base/_root.scss` | `:root` CSS custom properties |
| `base/_reset.scss` | Global reset + `prefers-reduced-motion` |
| `base/_base.scss` | `html`/`body`, links, focus-visible, `.container`, `.visually-hidden` |
| `base/_typography.scss` | Heading scale, `p`/`small`/`strong`/`em`/`address` |
| `vendors/_fontawesome.scss` | FA Pro integration via `meta.load-css('fa-all')` |
| `layout/_header.scss` | SECTION-001-GROUP-01 (geometry locked) |
| `sections/_hero.scss` | SECTION-001-GROUP-02 (geometry locked) |

## Approved CSS variables

See `base/_root.scss` and `foundation/FP-0002-V6-FRONTEND-GLOBAL-FOUNDATION.json`.

## Font families

| Role | Value | Status |
|------|-------|--------|
| base / heading / display | **Inter** (Google Fonts, V1 production path) | CONNECTED |

**V1 source:** `workspaces/fp-0002-shpigovsky-frontend` — `desktop-shell.html` link tag.  
**URL:** `https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap`  
**Weights loaded:** 300, 400, 500, 600, 700  
**Weights used in SECTION-001:** 400, 500, 600

### V1 typography exception (operator-authorized)

V1 accessed **only** for typography recovery. Allowed: font sources, families, sizes, line-heights, weights, typography colors. Forbidden: layout, geometry, spacing, component structure, responsive behavior, Header/Hero positioning.

## Typography roles

| Role | Token / size | Status |
|------|--------------|--------|
| body | 16px / 1.25 / Inter 400 | APPROVED_JPG |
| small / meta | 14px / 1.2 / Inter 400 | APPROVED_JPG |
| phones | 18px / 600 | APPROVED_JPG |
| nav | 15px / 400 | APPROVED_JPG |
| H1 / display | 40px / 1.15 / Inter 400 | APPROVED_JPG |
| button label | 13px / 500 | APPROVED_JPG |
| H2 / H3 | 28px / 22px | PROPOSED |

## Container policy

- Universal `.container` → `--container-main` (1220px) + `--page-padding-inline` (40px).
- Header keeps `.site-header__container` with explicit 1220px / 40px — not switched to `.container`.
- Hero uses `--container-hero` (1360px).

## Spacing policy

OL-01 scale exposed as `--space-*` tokens; block SCSS may still use Sass spacing aliases from `utils/_variables.scss`.

## Color policy

SECTION-001 approved values mapped to `--color-*` tokens; block-specific frosted panel remains in `_hero.scss`.

## Radius policy

Global `--radius-small|medium|large|pill`; hero/header block radii remain block-level where not site-wide.

## Font Awesome integration

- **Source:** `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`
- **Gulp:** `prepareFaBridge` + `faWebfonts` → `dist/assets/webfonts/`
- **SCSS:** `vendors/_fontawesome.scss`
- **Styles:** Solid, Regular, Light, Duotone, Brands
- **Header search:** `fas fa-search` — eighth nav `<li>`, not standalone sibling block
- **Not in Git:** vendor package, `fa-all.css` bridge, `dist/`

## Prohibited patterns

- Global `outline: none` on `*`
- ~~Google Fonts / external font CDN~~ — **exception:** V1 production Inter via Google Fonts (operator-authorized typography recovery)
- Committing FA Pro vendor to workspace
- Responsive Header/Hero layout without separate task
- **Arbitrary production px** without token lookup per [css-variable-first-law-v1.md](../../../projects/mars-website-factory/css-variable-first-law-v1.md)
- **Hidden fallback literals** on required foundation tokens (`var(--token, 30px)`)

## CSS Variable First Law

```text
css_variable_first_law: enabled
arbitrary_production_values_allowed: false
required_token_lookup: true
visual_qa_magic_numbers_allowed: false
```

Component tokens registered in `base/_root.scss`: controls, buttons, icons, borders, surfaces, motion.

## Responsive boundary

`layoutImplemented: false`. Only `prefers-reduced-motion` accessibility rule in reset — not layout breakpoints.
