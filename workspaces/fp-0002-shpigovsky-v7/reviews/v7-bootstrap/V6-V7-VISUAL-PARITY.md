# FP-0002 V6 ↔ V7 Visual Parity

**Date:** 2026-06-24  
**Capture method:** Playwright full-page screenshots from independent `dist/` builds (V6 frozen tag state, V7 fresh bootstrap).

## Screenshots

| Viewport | V6 | V7 |
|----------|----|----|
| Home desktop 1398 | `V6-HOME-DESKTOP.png` | `V7-HOME-DESKTOP.png` |
| Home mobile 390 | `V6-HOME-MOBILE-390.png` | `V7-HOME-MOBILE-390.png` |
| Services desktop 1398 | `V6-SERVICES-DESKTOP.png` | `V7-SERVICES-DESKTOP.png` |
| Services mobile 390 | `V6-SERVICES-MOBILE-390.png` | `V7-SERVICES-MOBILE-390.png` |

Width-suffixed duplicates (`*-1398.png`) retained for traceability.

## Checks reviewed

- Page order
- Text content
- Images
- Layout and section spacing
- Header / Footer
- Forms, modal, FAQ blocks (static render)
- Swiper / Fancybox markup presence
- Horizontal overflow (0 at 1398 and 390)

## Pixel comparison

| Pair | Unexpected pixel differences |
|------|---------------------------|
| Home desktop | 0 |
| Home mobile | 0 |
| Services desktop | 0 |
| Services mobile | 0 |

## Verdict

```text
Unexpected visual differences = 0
VISUAL PARITY = PASS
```

Allowed differences: none observed in page render. Dev `file://` origin is identical methodology for both workspaces.
