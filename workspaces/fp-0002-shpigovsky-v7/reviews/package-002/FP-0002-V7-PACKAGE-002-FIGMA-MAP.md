# FP-0002 V7 Package #002 — Figma Map

**Active Figma:** `Spig_v1.2.fig`  
**SHA-256:** `BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041`  
**Historical Figma used:** NO (`Шпиговский.fig` excluded)  
**Inspection:** openfig-core parse of active `.fig` + existing forensic reports cross-check

## External link icon

| Node ID | Layer | Type | Size | Mapping |
| ------- | ----- | ---- | ---- | ------- |
| `1:3609` | `arrow-up-right` | FRAME | 20×20 | `src/svg/external-link.svg` |
| `1:3610` | `Vector` | VECTOR stroke | 8.33×8.33 | SVG path 1 (diagonal) |
| `1:3611` | `Vector` | VECTOR stroke | 8.33×8.33 | SVG path 2 (corner) |

Stroke: `#475371` (`--color-text-primary` family) · weight 2 · rendered via `currentColor` in SVG.

## Recovery intro — `2 - Дом - вступление`

| Node ID | Visible text | HTML destination |
| ------- | ------------ | ---------------- |
| `1:929` | Шпиговский дом — восстановление с уважением к личности | `.home-recovery-intro__heading` |
| `1:931` | Lead paragraph | `.home-recovery-intro__lead` |
| `1:944`–`1:957` | Card titles + bodies | `.home-recovery-intro__card-*` |

Hidden/disabled nodes excluded per visible-content authority rule.
