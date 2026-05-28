# V4 Full Mockup Audit

## Source Scope

- Primary V1 sources reinspected: `projects/triumph-manipulator-landing/design/v1/01.png`, `02.png`, `03.png`, `04.png`, `full.png`.
- Continuity sources reinspected: `projects/triumph-manipulator-landing/design/frontend-section-map.md`, `mockups-index.md`.
- Approved shared assets reinspected: `projects/triumph-manipulator-landing/design/shared-assets/`.
- Reset boundary applied: prior V4 implementation files in `src/pages/`, `src/partials/layout/`, `src/partials/sections/`, `src/partials/components/`, `src/scss/`, and `src/js/` were removed before rebuild.

## Confirmed Section Order

1. Screen 01: persistent header shell plus hero content inside first-screen shell.
2. Screen 02: manipulators and prices, three commercial cards for 5, 7 and 10 tonne machines.
3. Screen 03: trust statement, four operational trust cards, review/rating panel.
4. Screen 03 continuation: dark proof strip with four operational metrics.
5. Screen 04: FAQ with six common objections/questions.
6. Screen 04 continuation: final CTA/contact section with form and messengers.
7. Compact landing footer: brand, navigation, contacts, CTA and legal placeholder line.

## Cadence and Rhythm

- Dark/light cadence: dark first-screen -> light pricing -> light trust/reviews -> dark proof strip -> light FAQ -> dark final CTA -> compact dark footer.
- Same-background light transition from pricing to trust uses lower rhythm; it should feel like one commercial/proof chapter, not two isolated pages.
- Different-background transitions use stronger rhythm: first-screen to pricing, trust to proof strip, FAQ to final CTA.
- CTA pressure rises progressively: hero primary CTA, pricing order CTAs, review proof, final high-pressure contact form.
- Footer stays compact because final CTA carries the commercial pressure and footer only closes context.

## Header / Hero / Slider Separation

- HEADER is the persistent navigation shell only.
- HERO is copy, CTA, feature list and proof content.
- FIRST-SCREEN shell owns `hero-bg-final.png`, overlays and focal protection.
- There is no slider implementation in V1 evidence; no slider was introduced.

## Background Ownership and Focal Points

- `src/img/hero/hero-bg-final.png` is restored from approved `design/shared-assets/hero-bg-final.png` and belongs to the first-screen shell.
- The hero background preserves the truck/sunset energy and baked technical annotations; those annotations are not duplicated in DOM.
- The overlay is left-heavy for text readability and lighter toward the truck/sunset focal area.
- `src/img/reconstruction/v1-04-contact-truck.png` is used only as final CTA atmosphere and avoids the baked form region.
- Product photo crops stay inside pricing media zones and do not carry duplicated card text.

## Safe Zones

- Text-safe zone: left side of Screen 01 and left/middle of final CTA receive the strongest overlay protection.
- Media-safe zone: truck and crane focal areas remain visible; overlays avoid flattening the industrial energy.
- Review and FAQ sections remain DOM-native because baked raster text would duplicate visible content.

## Asset Usage

- Approved shared assets used as-is: `brand/logo--white.svg`, `brand/favicon.svg`, `social/Telegram-ico.svg`, `social/WhatsApp-ico.svg`, `social/MAX-ico.svg`, `reviews/yandex_logo.svg`, `reviews/avito_logo.svg`, `reviews/rate_star.svg` available.
- Approved background authority: `design/shared-assets/hero-bg-final.png` copied to `src/img/hero/hero-bg-final.png`.
- Font Awesome bootstrap: local icon map uses codepoints verified against `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/css/free.css`; V4 solid webfonts `free-fa-solid-900.woff2` / `free-fa-solid-900.woff` are generated from the approved local `free-fa-solid-900.svg` source and must be present in built `dist`.

## Temporary Reconstruction Assets

- `src/img/reconstruction/v1-02-manipulator-5t.png`: source `design/v1/02.png`, documented crop 503 x 271 px. Reason: no approved standalone 5 tonne product photo exists.
- `src/img/reconstruction/v1-02-manipulator-7t.png`: source `design/v1/02.png`, documented crop 491 x 271 px. Reason: no approved standalone 7 tonne product photo exists.
- `src/img/reconstruction/v1-02-manipulator-10t.png`: source `design/v1/02.png`, documented crop 503 x 271 px. Reason: no approved standalone 10 tonne product photo exists.
- `src/img/reconstruction/v1-04-contact-truck.png`: source `design/v1/04.png`, documented crop 346 x 353 px. Reason: final CTA needs right-side industrial atmosphere without baked form duplication.
- No new temporary crops were created in this pass.

## Baked Image Content Warnings

- Source PNGs contain baked labels, callouts, product captions, review texts, rating stars, form fields and section headings.
- HTML must not overlay duplicate baked labels on the same raster content.
- Hero callouts remain part of the approved background asset and are not recreated.
- Product and contact crops are used only where no approved standalone asset exists.

## Font Awesome / Icon Needs

- FA is semantically justified for operations, specs, timing, routing, invoices, equipment and contact.
- Social and review providers use approved SVG assets, not FA substitutes.
- No playful SaaS icons or decorative icon spam are required.
- FA readiness is not complete from CSS/webfont presence alone. V4 requires built `dist` verification that used classes map to real codepoints in the selected font and render as icons, not tofu/broken squares.
- Generated or unknown subsets must not be accepted unless their class/codepoint/font mapping is verified; if mapping is uncertain, prefer inline SVG or a local sprite extracted from approved FA source.
- Duotone is currently **BLOCKED** for V4: the approved local FA source does not provide usable duotone `woff2` / `woff` delivery. Do not fake duotone with SVG-font-only mapping; use verified solid webfonts until matching duotone webfonts or an approved inline SVG/sprite source exists.
- Current V4 FA style is **CSS-softened solid fallback**, not active duotone output. Visual softening of solid icons does **not** equal duotone.
- When true duotone is unavailable, do not fake font delivery. Use verified solid icons and visually soften via controlled SCSS: opacity, outline, background restraint, sizing balance, and container pressure.
- Duotone may only be considered active when verified duotone webfonts exist and render correctly, or when approved inline SVG duotone assets are used. Absent verified assets, the project must declare honest solid fallback / verified solid delivery.
- On light backgrounds, operational icons should usually render as clean red glyphs without artificial containers unless the source/design explicitly requires badges. Containerized icon treatment is mainly for dark/contrast sections or when readability requires it.
- Final FA build acceptance requires every `@font-face` referenced webfont to exist in `dist` at the path declared by CSS.
- SAFE UNKNOWN: exact icon library used by the original V1 raster is not proven beyond current approved FA bootstrap.

## Footer Context

- Footer is compact by design because the final CTA already asks for action.
- No V1 evidence supports a map-heavy, sitemap-heavy or inflated footer.
- Footer role: brand closure, navigation reinforcement, contact fallback, legal placeholder display.

## Responsive Survivability

- Pricing cards collapse to one column below tablet widths.
- Trust/reviews two-column split collapses with trust content first.
- FAQ two-column layout collapses to one column.
- Final CTA hides the decorative truck crop on mobile to protect form readability.
- Header hides long navigation on narrower screens to avoid page overflow.

## SAFE UNKNOWN

- Exact V1 type scale, spacing tokens and original implementation values are not available as structured design tokens.
- Exact original source photos for pricing and final CTA are not available in `shared-assets`; existing reconstruction crops remain temporary aids.
- Exact review provider integration state is unknown; V1 only states future connection from Yandex, Avito and 2GIS.
- Exact legal values for INN/OGRN are not provided; placeholders remain visible and must be replaced by verified company data before production.
