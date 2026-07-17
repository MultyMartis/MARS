# E58-VA-003 — notes

## Recommendation
RECOMMEND REJECT — FALSE POSITIVE — HIGH confidence

## Evidence
- CSS token --main-size-btns: 40px
- .btn { height: var(--main-size-btns); padding: 0 25px; line-height: calc(40px - 2px); box-sizing:border-box }
- Measured WP & V9 content buttons: height 40px (majority); occasional 50px variant buttons exist on both
- 44px is an external touch guideline, not Figma/V9 SoT
