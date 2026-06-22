# FP-0002 V6 Frontend Global Foundation

**Project:** FP-0002 Shpigovsky V6  
**Status:** READY FOR OPERATOR REVIEW (font binding PARTIAL)  
**Checkpoint before:** `684e1690a9883ee4f716937a126cbde3ffd91182`

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
| base / heading / display | system UI stack | PARTIAL — no project font files in INCOMING |

## Typography roles

| Role | Token / size | Status |
|------|--------------|--------|
| body | 16px / 1.25 | PROPOSED |
| small / meta | 14px / 1.2 | APPROVED (Header) |
| phones | 18px / 600 | APPROVED (Header) |
| nav | 15px | APPROVED (Header) |
| H1 / display | 40px / 1.15 | APPROVED (Hero) |
| button label | 13px | APPROVED (Hero CTA) |
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
- **Not in Git:** vendor package, `fa-all.css` bridge, `dist/`

## Prohibited patterns

- Global `outline: none` on `*`
- Google Fonts / external font CDN
- Committing FA Pro vendor to workspace
- Responsive Header/Hero layout without separate task
- Replacing Header `search.svg` without operator decision

## Responsive boundary

`layoutImplemented: false`. Only `prefers-reduced-motion` accessibility rule in reset — not layout breakpoints.
