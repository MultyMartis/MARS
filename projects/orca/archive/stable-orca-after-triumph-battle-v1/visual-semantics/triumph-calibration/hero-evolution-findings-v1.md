# Hero Evolution Findings v1

**Source:** `calibration/.../ux-observations/hero-evolution-v1.md`, `hero-drift-analysis-v1.md`

## Three generations

| Gen | File | Character |
|-----|------|-----------|
| G0 | v4 `sections/screen-01-hero.html` | Generic index — broken semantics + layout |
| G1 | v4 `v5-ppc/zakaz/screen-01-hero.html` | PPC copy + form + qualification notice |
| G2 | v5 `v5-ppc/zakaz/screen-01-hero.html` | `hero--v5` + lower band proof + cargo |

## Why G0 failed (visual semantics)

| Problem | Field diagnosis |
|---------|-----------------|
| 6 feature lines + rate + CTA | `visual_density: overloaded` |
| Mixed fleet, NDС, hourly, geo | `semantic_focus` violated |
| Image placeholder vs H1 | `visual_noise_risk: critical` |
| Fake `от XXXX ₽/час` | destructive trust |
| «5–10 тонн», «Свой автопарк» | MODE 1 violation |
| CTA without inline form | `cta_priority` weak |
| Rate above features | price anxiety before fit |

## Why G2 improved

| Change | Field |
|--------|-------|
| H1 → lead → 5 specs → form | `hero_priority: capability_first` |
| Bg behind overlay | reduced image competition |
| Form aside | `cta_weight: primary_dominant` |
| Specs match ads | PPC continuity pass |
| Cargo cards | `use_case_fit` |
| No fake rate | productive recovery |
| `hero__lower` band | zoning — density manageable |

## G1 → G2 regressions

| Change | Class |
|--------|-------|
| Removed `hero__notice` | **destructive** (D1) |
| 4.9 ★ never in G1/G2 hero | ambiguous |

## Remaining G2 weaknesses

- Lower band 4+6 elements — `visual_noise_risk: high`
- Mobile form stack — `mobile_critical` at risk
- Six cargo micro-CTAs — `cta_weight` borderline
