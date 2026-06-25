# FP-0002 V7 Founder Quote SVG Audit

**Figma section:** `Слово спецу` (`1:1208`)  
**Decorative mark node:** `1:1217` (layer name `"`)

| Property | Figma value | Frontend decision |
| -------- | ----------- | ----------------- |
| Node ID | `1:1217` | Inline SVG path in `home-founder-quote.html` |
| Visible | YES | Rendered |
| Width | 70px | `width="70"` + CSS `width: 70px` |
| Height | 55px | `height="55"` + CSS `height: 55px` |
| Fill | `#B3261E` (solid) | `currentColor` on path; parent uses `var(--color-accent)` |
| Stroke | none | none |
| ViewBox | `0 0 70 55` | `viewBox="0 0 70 55"` |
| Decorative | YES | `aria-hidden="true"` `focusable="false"` |
| Export method | `fillGeometry.commandsBlob` decode from `Spig_v1.2.fig` | Source file `src/svg/founder-quote-mark.svg` (build copies to `dist/assets/svg/`) |

## Excluded nodes

| Node | Reason |
|------|--------|
| `1:1213` Vector 10 | Decorative background wash — not quote mark |
| Font Awesome `fa-quote-left` | Replaced — not Figma authority |

## Verdict

`FOUNDER QUOTE SVG` — **PASS**
