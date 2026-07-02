# CF-012 — Pre-implementation inventory (program modifier family)

**Wave:** CF-012 PROGRAM MODIFIER FAMILY CONSOLIDATION  
**Date:** 2026-06-28  
**HEAD at inventory:** `497c51c5fe088bb203b0c93486c3ee0f9f925afa`

## Candidate table

| Candidate | Partial | Consumers | Root class | Modifier(s) | Structure signature | Visual signature | CSS source | Status |
|---|---|---:|---|---|---|---|---|---|
| services-program-v2 hub | `services-program-v2.html` | `uslugi-v2.html` | `.services-program-v2` | _(none — page-scoped `.page-uslugi-v2` CSS)_ | `section>container>head+lead+intro[*]+grid>item(body+media)+cta?+foot-link` | external-link icon; grid gap line; cover images; title padded | `.page-uslugi-v2 .services-program-v2*` | SAME_STRUCTURE_DUPLICATE_MODIFIER |
| services-program-v2 subdivision | `services-program-v2.html` | `usluga-podrazdel-v1.html` | `.services-program-v2` | `services-program-v2--subdivision`, `service-subdivision-program-v1` | same as hub | play icon; grid gap pad; contain images; intro stacked; title block | `.page-service-subdivision-v1 .service-subdivision-program-v1*` | SAME_STRUCTURE_DUPLICATE_MODIFIER |
| services-program-v2 leaf | `services-program-v2.html` | `usluga-konechnaya-v1.html` | `.services-program-v2` | `services-program-v2--subdivision`, `service-leaf-program-v1` | same as hub | play icon; grid gap line; cover images; intro stacked; body spaced | `.page-service-leaf-v1 .service-leaf-program-v1*` | SAME_STRUCTURE_DUPLICATE_MODIFIER |
| program item atom | `services-program-v2-item.html` | via `itemsHtml` param | `.services-program-v2__item` | — | `article>body+media` | card border | inherited | CANONICAL_BASE |
| program CTA embed | `program-cta-band.html` | inside program partial | `.program-cta-band` | CF-011 canonical | nested include | dark band | CF-011 block | EXCLUDED (CF-011 protected) |
| home rehabilitation | `home-rehabilitation-program.html` | `index.html`, `uslugi.html` | `.home-rehabilitation-program` | — | `section>container>head+lead+intro+directions>article(img+wrapper)` | row direction cards | `.home-rehabilitation-program*` | REAL_VISUAL_VARIANT |
| subdivision stages | `service-subdivision-stages-v1.html` | `usluga-podrazdel-v1.html` | `.service-subdivision-stages-v1` | page-scoped | steps timeline | distinct | page-scoped | EXCLUDED (stages family) |
| leaf stages | `service-leaf-stages-v1.html` | `usluga-konechnaya-v1.html` | `.service-leaf-stages-v1` | page-scoped | steps timeline | distinct | page-scoped | EXCLUDED (stages family) |

## Totals

- Total candidates: 8
- Active program card partials: 1 (`services-program-v2.html`)
- Active consumers (card grid family): 3
- Page-named modifiers: 3 (`service-subdivision-program-v1`, `service-leaf-program-v1`, dead `services-program-v2--subdivision`)
- Functional modifiers (post-CF-012): 6 planned
- Duplicate CSS groups: 3 (hub / subdivision / leaf page stacks)
- Inline copies: 0
- Orphans: 0
- Unresolved: 0

## Canonical model decision

- **Base partial:** `services-program-v2.html`
- **Base root:** `.services-program-v2`
- **Real modifiers:** `--play-link`, `--intro-stacked`, `--grid-compact`, `--media-contain`, `--title-block`, `--title-flush`, `--item-body-spaced`
- **Excluded:** `home-rehabilitation-program` (different DOM), stages partials, `program-cta-band` (CF-011)
