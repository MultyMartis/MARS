# PC14-FU03 HOTFIX01 Production Proposal — Manifest

**Date:** 2026-07-16  
**Proposal:** `PC14_FU03_HOTFIX01_PRODUCTION_PROPOSAL`  
**Based on sandbox implementation:** `PC14_FU03_HOTFIX01_SANDBOX_APPLIED_HARNESS_VERIFIED`  
**Sandbox implementation commit:** `3a41bbc8`  
**Design commit:** `7443c4e9`  
**Diagnostics commit:** `cab4597a`  
**Production apply commit:** `44c05c3b`  
**Production Worker:** `p4mqb4VuPcemIDlC`  
**Sandbox source:** `tVGWi7Ud3zz2eGKo`  
**Decision:** `PC14_FU03_HOTFIX01_READY_FOR_PRODUCTION_APPROVAL`  
**Recommended next:** `PC14_FU03_HOTFIX01_PRODUCTION_PROPOSAL_PERSIST`  
**Secret scan:** `PASS_WITH_REVIEW_LABELS`  

## Explicit non-apply

- Production was **not** mutated in this task.
- Sandbox was **not** mutated in this task.
- No Telegram / OpenRouter / Sheets calls.
- No `/run` / `/health` / `/locks`.
- No stage / commit / push / pull.

## Proposed patch

- Nodes: Restore Format Run Items, Restore Format Run Items After Lock
- Type: jsCode replace only
- Node delta: 0
- Connections: unchanged
- Preserve production active=true and side-effect enabled states
- Keep `Run Strict Surface Repair` enabled in production

## Preflight (automated)

- allAutomatedGatesPass: true
- blockers: (none)

## Evidence files

- SEO-Content-Agent-Beta-v14-Worker.production-preproposal-hotfix01.sanitized.json
- SEO-Content-Agent-Beta-v14-Worker.sandbox-hotfix01-source.sanitized.json
- pc14-fu03-hotfix01-production-proposal-delta.json
- pc14-fu03-hotfix01-production-proposal-target-node-diff.json
- pc14-fu03-hotfix01-production-proposal-preflight-gates.json
- pc14-fu03-hotfix01-production-proposal-apply-plan.json
- pc14-fu03-hotfix01-production-proposal-rollback-plan.json
- pc14-fu03-hotfix01-production-proposal-harness-plan.json
- pc14-fu03-hotfix01-production-proposal-smoke-charter.md
- pc14-fu03-hotfix01-production-proposal-risk-matrix.json
- pc14-fu03-hotfix01-production-proposal-secret-scan.json
- (optional) code-node-index / side-effect-baseline / structural-validation

## Raw local

- `local/pc14-fu03-hotfix01-production-proposal-2026-07-16/`
