# FP-0002 V9-06E15 — Baseline Corrective Audit

See `validation/v9-06e15-service-mini-description-source-subdivision-sliders-regression-repair/baseline-corrective-audit.json`.

## Root causes
1. Subdivision sliders: Swiper gated to home/alcohol only.
2. Mini-description: EXACT_V9 seeded admin text identical to V9 static — operator could not distinguish admin vs HTML; hardened post_meta fallback added.
