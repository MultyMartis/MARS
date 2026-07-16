# Operator diff inventory — V9-06E56-FU02

## Pre-wave source/runtime drift
- v9-style.css: MATCH (both SHA256 0E1D29F169A386127E07D5C844DAD0281192E77C80D27AF6CA8C3EA9EAA143E9)
- assets.php: MATCH
- hero.php: MATCH
- Conclusion: no promote required; operator FU01 version already canonical in both trees

## Protected CSS baseline (pre-wave)
- SHA256: 0E1D29F169A386127E07D5C844DAD0281192E77C80D27AF6CA8C3EA9EAA143E9

## Additive changes only
- Inserted one @font-face block after Inter faces
- Added font-family only on .hero__title and .services-inner-hero-v2__title
- Operator media-query overrides (incl. .hero__title 30px @550px) preserved
- services-inner-hero-v2__media aspect-ratio cascade preserved

## Unresolved drift
- None for in-scope files
