# FP-0002 V9-03C — O-Centre Desktop Validation v1

**Route:** `/o-centre/`  
**Viewport:** ~1437px (representative desktop)

## Automated / objective checks

| Check | Result |
|-------|--------|
| HTTP 200 | PASS |
| CSS/JS/assets 200 | PASS |
| G6 absent from DOM (dist HTML) | PASS (0 matches) |
| Route count | 31 unchanged |
| H1 count | 1 (validator structure pass) |
| Horizontal overflow | Not automated — operator spot-check |

## Expected desktop behavior

- G6 was already `display: none` on desktop — removal should not introduce new gap
- G5 comfort gallery remains last group in infrastructure narrative
- Section flows into following O-Centre content unchanged

## Operator narrow review

Confirm no unexpected blank area after G5 gallery at desktop width.
