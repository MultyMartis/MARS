# FP-0002 — Services General Final Polish Content Audit

**Date:** 2026-06-26  
**Figma:** `Spig_v1.2.fig` @ `BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041`

## Visible text reconciliation

| Element | Source | Final polish action |
| ------- | ------ | ------------------- |
| Hero eyebrow | Figma `1:1355` | unchanged |
| Hero H1 | Figma `1:1356` | unchanged; visual order corrected via CSS `order` |
| Hero supporting | Figma `1:1357` | unchanged; downscoped to supporting typography |
| Addictions services | Figma visible copy | unchanged (4 items with body) |
| Mental health services | Figma names only | unchanged; lorem bodies excluded |
| Eating disorders services | Figma names only | unchanged; lorem bodies excluded |
| Genotyping lead | Figma lorem only | unchanged empty; SAFE_UNKNOWN preserved |
| Lower reuse headings | operator defaults | unchanged |

## Hidden lorem excluded

Confirmed: mental-health, eating-disorders, genotyping service bodies and genotyping leads remain omitted.

## Remaining SAFE_UNKNOWN

1. Genotyping hub lead paragraphs (Figma lorem only in `32:4586`)
2. Mental-health per-service descriptions (Figma lorem in `1:1474`)
3. Eating-disorders per-service descriptions (Figma lorem in `1:1569`)

## Content verdict

`COMPLETE_WITH_DOCUMENTED_SAFE_UNKNOWNS` — no invented copy added.
