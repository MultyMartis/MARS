# ORCA Production Method Improvements — v3

## Defects corrected

1. **Collision false negatives** — direction/group negatives treated as warnings in v2 while blocking active phrases.
2. **Dangerous stem cross-negatives** — bare stems (`синхрон`, `не работает`, `печатная форма`, `сайт`) removed from owner groups.
3. **Inline-minus repair** — informational phrases excluded at classifier v3 instead of long inline tails.
4. **Global «бесплатно»** — removed from global layer (over-blocking risk).

## Reusable components

| Module | Path |
|--------|------|
| Collision engine | `tools/lib/collision-engine-v3.mjs` |
| Classifier v3 | `tools/lib/keyword-classifier-v3.mjs` |
| Safe negatives | `tools/lib/negatives-config-v3.mjs` |
| Regression tests | `tools/regression-tests-v3.mjs` |

## Triumph method retained

- JSON dataset as meaning SoT
- Triumph template v1 sheet1-patch export
- Cross-negative matrix mandatory pre-export
- Human Commander dry-run gate
