# MIG Landing Analysis v2 — Migration Notes

**Status:** implemented in `projects/mig/lib/landing-analysis/` (schema `0.2`).

## Version detection

| Signal | v1 | v2 |
|--------|----|----|
| `schema_version` | `0.1` | `0.2` |
| `analysis_phase` | `landing_analysis_v1` | `landing_analysis_v2` |
| Index primary UX | `offer_count`, `cta_count`, … | `observation_summary` |
| Detail SoT | legacy arrays only | `observations[]` + `_legacy` mirror |

## Backward compatibility

- **Detail JSON:** v1 arrays (`offers[]`, `trust_patterns[]`, …) remain populated for one regression window; v2 adds `observations[]`, `observation_summary`, `_legacy`, `_processing.excluded_offers[]`.
- **Index:** v1 count fields move to `_derived` when `analysis_phase = landing_analysis_v2`.
- **Research pack:** `build-research-pack.js` selects v1 flat sections vs v2 intelligence cards by `landingIndex.analysis_phase`.
- **Re-run:** `runLandingPass(sessionDir)` only reads `website_snapshots.json` — no new HTTP fetch.

## Operator migration

1. Re-run landing pass on existing sessions (pilot: `tools/backtest-landing-analysis-v2-pilot.mjs`).
2. Review `research_pack.draft.md` per-domain cards instead of global count-first sections.
3. Audit nav exclusions via `landings/*/landing_observation.json` → `_processing.excluded_offers[]`.

## Config

- Nav-noise exclusions: `projects/mig/config/landing-nav-noise-exclusions-v2.json`

## Related contracts

- [mig-landing-analysis-v2.md](mig-landing-analysis-v2.md)
- [mig-landing-observation-families-v2.md](mig-landing-observation-families-v2.md)
