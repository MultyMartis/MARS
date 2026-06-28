# ORCA Wave 3.1F — Targeted SPPC-05 Repair Decisions v1

**Repair ID:** `ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-v1`  
**Authority:** Semantic Intelligence Wave 3.1F  
**Date:** 2026-06-26

## Verdict

`ORCA_WAVE_3_1F_TARGETED_REPAIR — PASS`  
`READY_FOR_NEW_SPPC_05_ATTEMPT`

Does **not** authorize Corvonero run `corv-semantic-v2-20260626-003`.

## Defect A — CFM-PROD-UPD-02

**Root cause:** Product version maintenance («обновление … до новой версии») was not classified as protected product intent. Wave 3.1F commercial/scope separation and missing `product_version_update` signal allowed model ACCEPT. Hard-rules lacked version-update pattern present only in adjudicator disambiguation regex.

**Repair:** Semantic class `product_version_update` + hard-rule block + adjudicator guard + prompt rule 23. Platform compatibility layer added for foreign ERP vs project-approved platforms (1C-only eval scope).

## Defect B — PQR-ABSTAIN-03

**Root cause:** `EXPLICIT_ERROR_RESOLUTION` matched «исправить» inside «как исправить», suppressing bare-error abstain and treating query as commercial task. Model REJECT (DIY). Adjudicator `SINGLE_ASSESSOR` path overwrote hard-rule ABSTAIN.

**Repair:** Split DIY-framed errors (`ambiguous_diy_problem`) from direct commercial error resolution. Hard-rule ABSTAIN on model REJECT. Adjudicator respects `hard_rule_override` on single-assessor path. Prompt rule 24.

## Version bumps

| Component | Before | After |
|-----------|--------|-------|
| Prompt contract | v1.3 | v1.4 |
| Adjudicator | v1.3 | v1.4 |
| Hard rules | implicit | v1.1 |
| Service intent evidence | v1.0 | v1.1 |
| Platform compatibility | — | v1.0 (new) |

## Regression gates (post-repair)

| Suite | Result |
|-------|--------|
| SPPC-05 defect repro | 2/2 PASS |
| Problem query policy | 10/10 PASS |
| Platform compatibility matrix | 7/7 PASS |
| Under-admission | 21/21 PASS |
| Wave 3.1F bypass audit | 15/15 PASS |
| Product confirmation FPR | 0.0 (gate ≤ 0.01) |
| Geo commercial recall | 0.96 (gate ≥ 0.90) |
| Model variance (repair fixtures, n=3) | stable |

## Immutable failed run

`corv-semantic-v2-20260626-002` remains `BLOCKED_AT_SPPC_05`, non-resumable, evidence frozen — see `CORVONERO-RUN-002-SPPC-05-FAILURE-ACCEPTANCE-v1.md`.
