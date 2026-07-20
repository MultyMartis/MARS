# PC14-FU03 HOTFIX02 Send Branch Production Proposal — Manifest

**Date:** 2026-07-20  
**Proposal:** `PC14_FU03_HOTFIX02_PRODUCTION_PROPOSAL`  
**Based on sandbox implementation:** `PC14_FU03_HOTFIX02_SANDBOX_APPLIED_HARNESS_VERIFIED`  
**Production HOTFIX01 apply commit:** `67ecdc7c`  
**Production Worker:** `p4mqb4VuPcemIDlC`  
**Sandbox source:** `TMhJbxtk6uUPDpEb`  
**Decision:** `PC14_FU03_HOTFIX02_READY_FOR_PRODUCTION_APPROVAL`  
**Recommended next:** `PC14_FU03_HOTFIX02_PRODUCTION_PROPOSAL_PERSIST`  
**Secret scan:** `PASS_WITH_REVIEW_LABELS`  

## Explicit non-apply

- Production was **not** mutated in this task.
- Sandbox was **not** mutated in this task.
- No Telegram / OpenRouter / Sheets calls.
- No `/run` / `/health` / `/locks`.
- No stage / commit / push / pull.

## Proposed patch

- Nodes: Format Strict Reject Message, Parse Mode
- Type: jsCode replace on 2 nodes + 1 connection fan-out reorder
- Node delta: 0
- Connection key: Format Strict Reject Message
- Fan-out: Take First Item, Prepare Memory Row Run → Prepare Memory Row Run, Take First Item
- Preserve production active=true and side-effect enabled states
- Keep `Run Strict Surface Repair` enabled in production
- Preserve HOTFIX01 restores / PC-07 / TZ HOTFIX01
- Do not change `Send Telegram Run` expression

## Preflight (automated)

- allAutomatedGatesPass: true
- blockers: (none)

## Evidence files

- SEO-Content-Agent-Beta-v14-Worker.production-preproposal-hotfix02.sanitized.json
- SEO-Content-Agent-Beta-v14-Worker.sandbox-hotfix02-source.sanitized.json
- SEO-Content-Agent-Beta-v14-Worker.production-hotfix02.transformed-preview.sanitized.json
- pc14-fu03-hotfix02-send-branch-production-proposal-delta.json
- pc14-fu03-hotfix02-send-branch-production-proposal-target-node-diff.json
- pc14-fu03-hotfix02-send-branch-production-proposal-connection-diff.json
- pc14-fu03-hotfix02-send-branch-production-proposal-preflight-gates.json
- pc14-fu03-hotfix02-send-branch-production-proposal-apply-plan.json
- pc14-fu03-hotfix02-send-branch-production-proposal-rollback-plan.json
- pc14-fu03-hotfix02-send-branch-production-proposal-harness-plan.json
- pc14-fu03-hotfix02-send-branch-production-proposal-smoke-charter.md
- pc14-fu03-hotfix02-send-branch-production-proposal-risk-matrix.json
- pc14-fu03-hotfix02-send-branch-production-proposal-secret-scan.json
- (optional) code-node-index / side-effect-baseline / structural-validation / transform-preview-meta

## Raw local

- `local/pc14-fu03-hotfix02-send-branch-production-proposal-2026-07-20/`
