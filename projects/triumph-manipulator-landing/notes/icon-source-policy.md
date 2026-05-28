# Icon source policy — Triumph Manipulator landing

This note applies to **Triumph Manipulator** frontend work under `workspaces/triumph-manipulator-landing/` and to **AI agents** assisting with that project.

## Canonical icon library

**Default icon source:** Font Awesome **Pro 5.15.4**, installed locally at:

`C:\AI MARS\shared\assets\icon-libraries\Font Awesome Pro 5.15.4`

Registry and usage details:

`C:\AI MARS\shared\assets\icon-libraries\fontawesome-pro-5.15.4-usage.md`

Governance layer for semantic matching, family/style consistency, optical rhythm, and drift reporting:

[`../../mars-website-factory/font-awesome-governance-layer.md`](../../mars-website-factory/font-awesome-governance-layer.md)

This library is **licensed and local-only**. Do not publish, sync to public artifact stores, or attach the full folder to chats or tickets.

## Rules for AI agents and contributors

1. **Do not invent icons.** Do not redraw, approximate, or generate substitute glyphs from scratch when a Font Awesome Pro icon exists for the metaphor.
2. **Do not import the whole library** into the workspace (no bulk copy of `webfonts/`, no wholesale `all.min.css` in `src/` or `dist/`).
3. **Selected icons only:** export or extract **individual SVG files** (or a deliberately small hand-built sprite) and add them under the project’s established asset paths.
4. **Normalize SVGs only when safe:** prefer `currentColor`, remove editor cruft, align viewBox; avoid destructive path simplification that breaks small-size legibility.
5. **Consistency:** use **light** or **regular** for large marketing blocks; **solid** for small/dense UI; **duotone** only with a deliberate visual system. Do not mix arbitrary weights inside one component without design intent.
6. **Browser verification:** after `gulp`/build steps, open the built page and confirm stroke weight, alignment, and hover/focus states.
7. **Governance reporting:** when icons affect trust strips, specification rows, CTA/support, prohibition/transport lists, or social/contact areas, record semantic / style / optical drift using the Website Factory FA governance vocabulary.

## Triumph-specific implementation context (read-only reference)

- Inline UI symbols use `partials/components/icon.html` with `<use href="#i-…">` backed by `src/svg/` merged into `sprite.svg` (see `src/scss/components/_icon.scss`).
- Social buttons use raster-style SVGs under `src/img/social/`.
- Brand marks live under `src/img/brand/`.
- Review platform marks and star artwork live under `src/img/reviews/`.

When replacing or adding icons, **match the existing integration** (sprite vs `<img>`) rather than introducing a second parallel system without a task-specific decision.

## Exceptions

- **Third-party brand assets** (e.g. marketplace logos) must follow those brands’ guidelines; Font Awesome may not include them.
- **Messenger “MAX”** and similar marks may require **project-supplied** SVGs if no suitable licensed glyph exists in Font Awesome Brands.

## After changes

Run a production build, load the page in Chrome (and one secondary browser if available), and spot-check **hero**, **trust**, **equipment cards**, **FAQ**, **CTA**, and **footer** at mobile and desktop widths.
