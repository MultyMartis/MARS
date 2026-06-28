# FP-0002 — Services Desktop / Mobile Node Map v1

**Date:** 2026-06-26  
**Desktop root:** `1:1310` · **Mobile root:** `1:4624`

| Component | Desktop node | Mobile node | Same instance/family | Structural changes | Content changes |
| --------- | ------------ | ----------- | -------------------- | ------------------ | --------------- |
| Inner Hero | `1:1311` | `1:4625` | Same page role | Header compressed; banner shorter; breadcrumbs/tabs stack | Same copy |
| Breadcrumbs | `1:1363` | SAFE UNKNOWN | Likely shared component | Width 660→~322; font smaller | Truncation/wrap |
| Page submenu | `1:1367` | SAFE UNKNOWN | Tag component family | Horizontal scroll/wrap vs desktop row | Same labels |
| Category 1 | `1:1405` | `1:4676` | Pattern family | Gallery stacks below list | Same |
| Category 2 | `1:1474` | `1:4744` | Pattern family | Taller stack | Same |
| Category 3 | `1:1569` | `1:4832` | Compact variant | No gallery desktop → no gallery mobile | Same |
| Category 4 | `32:4586` | SAFE UNKNOWN | Compact | Desktop last; mobile placement unclear | Same |
| Program | `1:1610` | `1:4880` | Content shared | 2×2 grid → vertical cards | Same |
| Founder | `1:1649` | `1:4913` | Reused home block | Image/text stack | Same |
| Comfort | `1:1665` | `1:4932` | Reused home block | Mosaic → vertical gallery | Same |
| Mid-page CTA | `1:1715` | `1:4981` | Services-specific | Full-width strip; button stack | Same |
| FAQ | `1:1720` | `1:4985` | Reused home block | Accordion full width | Same |
| Final form | PNG only | PNG only | Reused home partial | Field stack | Same |
| Footer | `1:1747` | `1:5011` | Footer mobile variant | Multi-column → stacked | Same |

## Mobile-specific notes

- Genotyping section node on mobile: **SAFE UNKNOWN** — not listed as top-level child of `1:4624`; may be embedded or omitted in mobile frame export.
- Category order preserved: addictions → mental → eating → (genotyping TBD) → program → …
- No evidence of simple “desktop stack” without node reordering — each section has distinct mobile frame IDs.

## Missing MCP confirmation

Live `get_metadata` on mobile nodes pending cloud file access.
