# INTENT RESOLUTION v1 — Phase 3E.1

**Research:** [CLIENT-INTENT-RESOLUTION-v1.md](../../research/parser-3.3/CLIENT-INTENT-RESOLUTION-v1.md) — **implemented**  
**Harness:** H16–H18

## Precedence

1. explicit client comment  
2. structured fields  
3. explicit selected service  
4. source-page context  
5. email subject / form title  

Weaker sources do not overwrite stronger. Conflicts set `intent_conflict=true`. No signal → Other/unknown.

## Taxonomy (machine → RU label)

Audit · SEO · WebsiteDevelopment · WebsiteDevelopmentSEO · AISearch · Other

## Fixture anchors (sanitized)

| Case | Expectation |
|------|-------------|
| «хочу сайт» | WebsiteDevelopment |
| «сайт потом» + SEO signal | WebsiteDevelopmentSEO |
| «seo» + valid site | SEO |

Reply must follow resolved intent (see FIRST-REPLY-CONSISTENCY).
