# Triumph Manipulator Landing V4 — Screen 01 Analysis

## 1. Scope

This document records the first clean Screen 01 reconstruction pass for V4.

Task boundary:

- Implement only layout shell, header system, first-screen shell, and hero system.
- Preserve **HEADER != HERO != SLIDER**.
- Treat V3 implementation as forbidden authority.
- Use V1 `01.png` and `full.png` only if visible on disk.
- Use approved shared asset `hero-bg-final.png` only as-is if visible on disk.

## 2. Source Re-Inspection Result

Re-read documents:

- `docs/V4-SOURCE-AUDIT.md`
- `docs/V4-FIRST-SCREEN-DECOMPOSITION.md`
- `docs/V4-SECTION-LANGUAGE.md`
- `docs/V4-EXECUTION-BOUNDARIES.md`
- `docs/V4-RECONSTRUCTION-PLAN.md`

Confirmed governance:

- V4 is a clean reconstruction workspace under `workspaces/triumph-manipulator-landing-v4/`.
- V3 implementation files, crops, DOM, SCSS, responsive fixes, and local overrides are not authority.
- First-screen systems must remain separate even when they visually coexist.
- Russian typography survivability is mandatory in HTML.
- Asset use must avoid renaming, recompression, resizing, derived replacements, and silent substitution.

## 3. Raster Inspection Status

Requested primary sources:

- `projects/triumph-manipulator-landing/design/v1/01.png`
- `projects/triumph-manipulator-landing/design/v1/full.png`

Repo-visible status in this pass:

- `design/v1/01.png` was opened and inspected.
- `design/v1/full.png` was opened and inspected.
- `01.png` shows the top viewport: header over dark shell, left conversion block, truck/environment background, red CTA rhythm, operational proof bullets, and bottom proof bar.
- `full.png` confirms that Screen 01 continues into a white pricing section, so the first-screen atmosphere must close cleanly rather than become a detached image card.

SAFE UNKNOWN:

- Pixel-perfect measurements.
- Exact responsive behavior.

## 4. Approved Asset Status

Requested background asset:

- `projects/triumph-manipulator-landing/design/shared-assets/hero-bg-final.png`

Repo-visible status:

- `hero-bg-final.png` was opened from `design/shared-assets/`.
- It matches the first-screen environmental truck/construction/sunset layer.
- No replacement raster was created.
- No V3 crop or reconstruction asset was used.

Implementation consequence:

- The first-screen shell owns the CSS background slot for `hero-bg-final.png`.
- The approved raster was copied into `src/img/hero-bg-final.png` as-is for the V4 build pipeline.
- Existing approved SVG assets copied as-is: `logo--white.svg`, `favicon.svg`, `WhatsApp-ico.svg`, `Telegram-ico.svg`.

## 5. Shell Boundaries

Implemented separation:

- Layout shell: `src/pages/index.html` and `.first-screen-shell`.
- Navigation shell: `src/partials/layout/header.html`.
- Hero content system: `src/partials/sections/hero-screen-01.html`.
- Hero environment system: `.first-screen-shell` background and atmospheric overlays.
- Overlay system: `.hero-screen-01__overlay`, separate from header and content.
- Atmospheric continuity layer: shell-level dark overlays and bottom fade.

Boundary finding:

- Background belongs to `.first-screen-shell`, not to a hero card.
- Header is a persistent navigation shell above the hero system.
- No slider behavior is implemented because no source-proven slider evidence is visible.

## 6. Header Ownership

Header owns:

- Logo.
- Navigation links.
- Phone.
- Restrained social contact entry points.
- CTA.
- Mobile navigation survivability.
- Readability over the atmospheric shell.

Header does not own:

- H1.
- Hero proof.
- Conversion copy.
- First-screen background asset.
- Slider behavior.

SAFE UNKNOWN:

- Exact pixel measurements for header vertical alignment and opacity.
- Whether social URLs are final production links.

## 7. Background Ownership

Implemented rule:

- `.first-screen-shell` owns the environmental background stack.
- CSS references `../img/hero-bg-final.png` as the approved asset slot.
- Background rendering uses `auto` sizing to avoid declaring a transformed/recompressed derivative.
- Labels, callouts, numbers, arrows, technical marks, and annotations already visible inside `hero-bg-final.png` are owned by the background asset.
- Screen 01 must not duplicate those baked annotations through `hero-screen-01__annotations`, `hero-screen-01__annotation`, or equivalent HTML/CSS overlay.

Baked annotation rule:

- If labels, callouts, numbers, arrows, technical marks, or annotations are baked into an approved background/image asset, do not duplicate them as HTML/CSS overlay.
- Create HTML annotations only when source evidence shows independent UI/text elements, they are not already baked into the image, they are needed for accessibility/content reasons, and the decision is documented.

SAFE UNKNOWN:

- Exact crop/alignment across all breakpoints.
- Whether future sections should reuse any part of this environment is not decided.

## 8. Atmosphere Transitions

Implemented approximation:

- Header reads over a dark translucent navigation band.
- First-screen shell uses dark atmospheric overlays.
- Hero content participates in the same shell atmosphere rather than floating as an isolated card.
- Bottom fade keeps continuity for future screen 02.

Approximation disclosure:

- Overlay weight and background alignment are provisional because this pass is survivability reconstruction, not pixel perfection.

## 9. Pressure and Density Rhythm

Implemented approximation:

- Dense commercial-industrial rhythm through compact header, large uppercase H1, price badge, primary CTA, proof bullets, and bottom proof bar.
- Avoided sterile SaaS spacing and decorative card-first composition.
- Replaced the temporary secondary panel with source-like price badge, CTA callback note, benefit grid, and bottom proof bar.
- Truck/background annotation labels are not reconstructed in HTML because they are baked into `hero-bg-final.png`.

SAFE UNKNOWN:

- Exact dimensions, offsets, and typography weights remain approximate.

## 10. Typography and Font Awesome

Russian typography applied in user-visible HTML:

- `в&nbsp;Краснодаре`
- `по&nbsp;Краснодару`
- `от&nbsp;30&nbsp;минут`
- `до&nbsp;10&nbsp;тонн`
- `с&nbsp;НДС`
- `для&nbsp;юр.&nbsp;лиц`

Font Awesome:

- Font Awesome is not integrated in V4 Screen 01.
- FA remains pending technical debt if future source review requires FA-specific icons.
- Existing approved social SVG assets cover operational contact affordances without icon spam.

## 11. Responsive Survivability

Desktop-first assumptions:

- Header uses a three-column desktop shell.
- Tablet collapses nav into a second row while keeping brand and contacts visible.
- Mobile keeps brand, phone, social entry, CTA, and horizontal nav access.
- Hero content, proof grid, and bottom bar collapse without making the background an image card.

SAFE UNKNOWN:

- Exact V1 mobile behavior is not source-proven.
- Rendered breakpoint accuracy remains approximate until visual QA is performed.

## 12. QA Checklist

Checked by implementation review:

- Shell survivability: present as `.first-screen-shell`.
- Background ownership: shell-level, not hero-card level.
- Commercial density: preserved through compact conversion structure.
- Atmosphere continuity: shell overlays and bottom fade present.
- Section language: uses `hero-screen-01`, not V3 section names.
- Anti-beautification: no modernization-only sections or cinematic replacement assets.
- V3 contamination: no V3 files copied or referenced.
- Stale bootstrap residue: `.gitkeep` files remain harmless; source files now define actual V4 bootstrap surface.

Required command:

- `npm run build` passed.

## 13. Remaining SAFE UNKNOWN

- Pixel-perfect offsets and dimensions.
- Exact production contact URLs.
- Exact responsive source behavior.

## 14. Remaining Risks

- This pass approximates measured spacing and typography from raster inspection rather than extracting exact design tokens.
- Header/hero/mobile breakpoints need rendered visual review against `01.png` and `full.png`.
- The current build stack reports npm audit vulnerabilities inherited from the Gulp dependency set; no security fix was attempted in this reconstruction pass.
