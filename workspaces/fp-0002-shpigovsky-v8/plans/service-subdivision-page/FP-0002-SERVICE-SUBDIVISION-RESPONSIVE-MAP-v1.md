# FP-0002 Service Subdivision — Responsive Map v1

## Desktop architecture

Single column content flow inside `.container`; program directions 2×2 or stacked pairs; specialists horizontal swiper; comfort gallery grid.

## Mobile architecture

Separate frame `1:7096` — not DOM-only shrink. Key differences:

| Block | Desktop | Mobile | Strategy |
|-------|---------|--------|----------|
| Hero | split copy/CTA | stacked in `Моби` | REUSE_WITH_SCOPED_VARIANT |
| Breadcrumbs/subnav | inline row | wrapped / scroll | CSS wrap |
| Intro | side-by-side optional | single column | same DOM |
| Service list | dotted leaders + link row | column stack | existing V2 mobile rules |
| Info cards | 2-column | stack | CSS grid → 1 col |
| Rehab stages | horizontal/row cards | stack | mobile variant likely |
| Program grid | 2×2 media cards | vertical stack | same DOM, CSS |
| Center/team stats | side-by-side | stack | different content order |
| Supporting block | `Программа центра` | `Подход` | mobile-specific section naming |
| Specialists | swiper | swiper (fewer visible) | same DOM |
| Reviews | swiper | swiper | same DOM |
| FAQ | accordion | accordion | same DOM |
| Final form | 2-col form | stack | home responsive rules |

## DOM reorder requirements

- Mobile `Подход` block may require different section order vs desktop — **do not assume single page template order**; use scoped page wrapper + mobile-specific includes only if Figma proves different architecture

## Horizontal-scroll components

- Specialists swiper: overflow contained
- Reviews swiper: overflow contained
- Subnav: verify at 320px (Services V2 probe pattern)

## Result

`RESPONSIVE_MAP_COMPLETE`
