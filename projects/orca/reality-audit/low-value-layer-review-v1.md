# Low-Value Layer Review v1

## Classification Rule

If a document does not improve operator speed, review clarity, or PPC decision quality, classify it as LOW VALUE or PRUNE CANDIDATE.

## Keep In Starter Core

- `fast-review/mobile-serp-review-v1.md` - strong first review for query and market pressure.
- `fast-review/landing-mismatch-review-v1.md` - directly supports ad, landing, semantic, and hold decisions.
- `fast-review/mobile-friction-review-v1.md` - useful when mobile traffic or first-screen friction matters.
- `essential-signals/semantic-contamination-v1.md` - directly supports negatives, grouping, and mismatch decisions.
- `reports/orca-live-session-report-template-v1.md` - useful if kept short.

## Support Only

- `fast-review/cta-pattern-review-v1.md` - useful when ad or landing action is unclear; not always primary.
- `essential-signals/trust-patterns-v1.md` - useful when proof is a visible market pressure; otherwise easy to over-document.
- `essential-signals/aggregator-pressure-v1.md` - useful when aggregators dominate; otherwise support-only.
- `governance/*` - useful as boundaries, not live-session reading.
- `reports/orca-mvp-readiness-report-template-v1.md` - useful after several sessions, not during one.

## LOW VALUE For Live Sessions

- `fast-review/fast-review-workflow-v1.md` - mostly duplicated by `OPERATIONAL-INDEX.md` and `live-pilot/README.md`.
- `essential-signals/essential-signals-model-v1.md` - mostly duplicates priority rules.
- `essential-signals/signal-priority-rules-v1.md` - useful concept, but redundant in live flow.
- `essential-signals/low-value-noise-rules-v1.md` - redundant with stop cues and anti-fatigue rules.

## PRUNE CANDIDATES

- `fast-review/rapid-landing-review-v1.md` - overlaps heavily with `landing-mismatch-review-v1.md` and `mobile-friction-review-v1.md`.
- `fast-review/rapid-semantic-review-v1.md` - overlaps with `semantic-contamination-v1.md`.
- `fast-review/rapid-trust-review-v1.md` - overlaps with `trust-patterns-v1.md`.
- `fast-review/15-minute-serp-review-v1.md` - overlaps with `mobile-serp-review-v1.md`.
- `essential-signals/high-value-serp-signals-v1.md` - overlaps with mobile SERP and aggregator checks.
- `essential-signals/high-value-trust-signals-v1.md` - overlaps with trust patterns.
- `essential-signals/high-value-semantic-signals-v1.md` - overlaps with semantic contamination.

## Do Not Delete Yet

No files are deleted in this pass. Prune candidates need one live session comparison before removal or merge.
