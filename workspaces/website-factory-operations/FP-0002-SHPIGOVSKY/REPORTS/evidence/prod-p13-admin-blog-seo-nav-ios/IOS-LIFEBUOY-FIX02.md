# iOS lifebuoy FIX02 forensic note

P12 `translate3d` / single-transform-on-mover **FAILED** on Olya’s physical iPhone. That hypothesis is rejected as sufficient.

FIX02 (implemented):

- Fixed root has **no** `transform`, **no** `contain`, **no** isolation freeze.
- Desktop/Android keep mover `transform` (scale + rotate + translate).
- iOS/iPadOS path: capability/UA-narrow (`iP(hone|ad|od)` or iPadOS desktop-mode `MacIntel` + `maxTouchPoints > 1`).
- iOS mover position uses `top`/`left` in CSS pixels; transform limited to scale/rotate.
- `visualViewport.pageTop` used when present (Safari toolbar).

Physical device acceptance is **not** claimed from Chromium emulation.

`PHYSICAL IPHONE QA = OLYA PENDING`
