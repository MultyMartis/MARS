# FP-0002 V9-03G Mobile Scroll-to-Top Validation v1

**Phase:** V9-03G  
**Target viewport:** ~380px (operator confirmation pending)

## CSS mobile contract (@media max-width: 1024px)

| Property | Value |
|----------|-------|
| Size | 44×44px |
| Right offset | `var(--pad-gap-tight)` (10px) |
| Bottom offset | `calc(10px + env(safe-area-inset-bottom, 0px))` |
| Icon | 18×18px SVG |

## Checks (automated + operator)

| Check | Status |
|-------|--------|
| Hidden near top (`scrollY <= 500`) | Contract verified in JS/CSS |
| Visible after 500px scroll | Contract verified |
| Bottom-right fixed position | PASS (CSS) |
| No horizontal overflow from control | PASS (compact fixed size) |
| Tap target ≥ 44px | PASS |
| Safe-area inset respected | PASS (CSS) |
| Footer overlap risk | Low — corner placement with inset |
| Modal control overlap | z-index 900 below modal 1200 |

## Routes for operator mobile review

- Home `/`
- O-Centre `/o-centre/`
- Long service `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`
- Blog article `/blog/nazvanie-stati/`

**Preview:** http://127.0.0.1:8797/
