# FP-0002 Services V2 Founder Anatomy Map v1

**Figma node:** `1:1649` (Слово спецу)  
**Partial:** `src/partials/sections/services-founder-v2.html`  
**Root:** `.services-founder-v2`

| Region | Figma node | Runtime component | Copy type | Status |
|--------|------------|-------------------|-----------|--------|
| Quote mark | decor | `.services-founder-v2__mark` SVG | — | COMPLETE |
| Quote body | `1:1655` | `.services-founder-v2__text` | TEMPORARY_MOCKUP_COPY (Lorem) | COMPLETE |
| Photo | founder asset | `.services-founder-v2__photo` | — | COMPLETE (reuse) |
| Expert label | label | `.services-founder-v2__expert-label` «мнение эксперта» | REAL | COMPLETE |
| Name | text | `.services-founder-v2__name` | REAL | COMPLETE |
| Role | text | `.services-founder-v2__role` | REAL | COMPLETE |
| CTA | button instance | `.services-founder-v2__cta` | REAL | COMPLETE |

## Layout

- Desktop: 2-column grid (quote | figure+card)
- Mobile: stack; card static below photo

## Empty slots

0

## Verdict

`COMPLETE_PENDING_OPERATOR_REVIEW`
