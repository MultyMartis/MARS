# FP-0002 V7 — CSS Cleanup Map (Final Polish)

**Date:** 2026-06-24

| Selector/property | Usage | Classification | Action |
| ----------------- | ----- | -------------- | ------ |
| `.home-gallery__slide` `position: relative` | overlay caption anchor only | LEGACY_CSS | REMOVED — replaced with flex column |
| `.home-gallery__caption` `position: absolute` | overlay on image | LEGACY_CSS | REMOVED |
| `.home-gallery__caption` `right/bottom/left: 0` | overlay box | LEGACY_CSS | REMOVED |
| `.home-gallery__caption` `border-radius: 0 0 …` | image overlay corner | LEGACY_CSS | REMOVED |
| `.home-gallery__caption` `color: --color-text-inverse` | on-image contrast | LEGACY_CSS | REMOVED |
| `.home-gallery__caption` `pointer-events: none` | overlay click-through | LEGACY_CSS | REMOVED |
| `.home-gallery__caption` `padding: tight + line` | overlay bar | LEGACY_CSS | REMOVED |
| All other selectors | active HTML/JS | OPERATOR_CANONICAL | KEEP |

**Lines removed:** 8 property declarations in gallery block only.  
**No** global reformat, BEM rename, or unrelated selector deletion.
