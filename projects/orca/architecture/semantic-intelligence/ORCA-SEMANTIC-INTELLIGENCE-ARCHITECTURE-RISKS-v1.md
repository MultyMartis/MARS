# ORCA Semantic Intelligence — Architecture Risks v1

**Register ID:** `orca-semantic-intelligence-architecture-risks`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

Probability: `LOW` | `MEDIUM` | `HIGH`  
Impact: `LOW` | `MEDIUM` | `HIGH` | `CRITICAL`  
Blocking: `NONE` | `PILOT` | `PRODUCTION` | `ARCHITECTURE`

---

## Risk register

| ID | Risk | Probability | Impact | Prevention | Detection | Recovery | Owner | Blocking |
|----|------|-------------|--------|------------|-----------|----------|-------|----------|
| R-01 | Over-admission (topical → ACCEPT) | HIGH | CRITICAL | Hierarchical gates; D3 precision; CONSERVATIVE mode | Protected-strata FPR; blind audit | Freeze core; rerun admission | Operator + QA | PRODUCTION |
| R-02 | Excessive abstention | MEDIUM | MEDIUM | Risk mode tuning; guideline clarity | Abstention rate monitoring | Balanced mode after P0-G | Operator | PILOT |
| R-03 | Hidden recall loss | MEDIUM | HIGH | Per-intent recall on benchmark | Stratified eval reports | Lower threshold in charter only | QA | PILOT |
| R-04 | Rule conflict | MEDIUM | HIGH | Exception registry; conflict → ABSTAIN | Regression anchors | Rule version bump | Rules maintainer | PILOT |
| R-05 | Benchmark bias | MEDIUM | HIGH | Strata design; blind split; dual annotation | Disagreement analysis | Re-annotate strata | QA | PRODUCTION |
| R-06 | Annotation inconsistency | MEDIUM | HIGH | P0-C guideline; double annotation | Inter-annotator agreement | Adjudication protocol | Annotation lead | PRODUCTION |
| R-07 | LLM instability | MEDIUM | HIGH | Versioned prompts; structured output; human final | Output schema validation failures | Fallback to human queue | ML engineer | PILOT |
| R-08 | Model drift | LOW | HIGH | Version binding; periodic re-eval | Calibration error spike | Model retrain + P0-G re-gate | ML engineer | PRODUCTION |
| R-09 | Stale service scope | MEDIUM | HIGH | SI-01 version binding | Scope/core mismatch audit | Scope version bump + partial rerun | Operator | PRODUCTION |
| R-10 | Domain transfer failure | MEDIUM | HIGH | Corvonero pilot before full corpus | Pilot gate fail | Domain-specific retrain | ML engineer | PRODUCTION |
| R-11 | Russian morphology errors | MEDIUM | MEDIUM | Morphology-safe normalization tests | Normalization regression suite | Normalizer fix + re-normalize | Engineering | PILOT |
| R-12 | Product/service confusion | HIGH | HIGH | ABSTAIN on conflict; SI-09 adjudication | Mapping conflict rate | Human adjudication | Operator | PRODUCTION |
| R-13 | False confidence | MEDIUM | CRITICAL | Calibration requirement; CONSERVATIVE | ECE on blind set | Raise threshold; more ABSTAIN | QA | PRODUCTION |
| R-14 | Reviewer confirmation bias | MEDIUM | MEDIUM | Blind eval; random audits | Audit disagreement rate | Rotate reviewers | QA lead | PILOT |
| R-15 | Self-validation | MEDIUM | CRITICAL | Blind test isolation | Train/blind leakage check | Re-split benchmark | QA | PRODUCTION |
| R-16 | Campaign-layer contamination | HIGH | CRITICAL | SI-14 freeze; SI-15 read-only semantics | Export parity QA | Halt export; return to core | Operator | PRODUCTION |
| R-17 | Negative overblocking | MEDIUM | MEDIUM | Negatives after ownership only | Collision risk registry | Negative scope reduction | Operator | PILOT |
| R-18 | Post-launch feedback leakage | MEDIUM | CRITICAL | SI-17 proposals only | Core mutation audit | Versioned core review gate | Operator | PRODUCTION |

---

## Top blocking risks (Corvonero context)

1. **R-01** — Confirmed in clean-room v1; primary architecture driver.
2. **R-16** — Campaign production must not mutate semantics.
3. **R-18** — Post-launch terms must not silently alter approved core.

---

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `orca-semantic-intelligence-architecture-risks-v1.json` |
