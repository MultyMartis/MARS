# FP-0002 V9-03B — Button Interaction Validation v1

**Method:** Source audit + build/HTTP regression + operator checklist  
**Automated:** PASS (no `.btn:hover` translateY in SCSS)

## Matrix

| Control | Movement | Lift/scale | Color transition | Focus | Active | Disabled |
|---------|----------|------------|------------------|-------|--------|----------|
| Primary CTA (`.btn--primary`) | None | None | ~0.3s accent hover | Outline | opacity 0.92 | opacity 0.5 |
| Dark button (`.btn_dark`) | None | None | ~0.3s surface hover | Outline | opacity 0.92 | opacity 0.5 |
| Outline/default `.btn` | None | None | ~0.3s fill hover | Outline | opacity 0.92 | opacity 0.5 |
| Header modal trigger | None | None | Via `.btn` | Yes | Stable | N/A |
| Form submit (modal/final) | None | None | Via `.btn` | Yes | Stable | loading state |
| «Все отзывы» / «Все статьи» | None | None | Via `.btn` | Yes | Stable | N/A |
| Mobile menu buttons | None | None | Color/background | Yes | Stable | N/A |

## Operator re-check required

Desktop + mobile ~380px hover/tap on representative CTAs listed in phase brief.
