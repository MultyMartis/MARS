# PC14-FU03 Production Proposal Manifest

**Date:** 2026-07-16
**Proposal:** PC14_FU03_PRODUCTION_PROPOSAL
**Based on sandbox implementation:** PC14_FU03_SANDBOX_IMPLEMENTATION_APPLIED_HARNESS_VERIFIED
**Sandbox implementation commit:** `a64da270`
**Decision:** PC14_FU03_READY_FOR_PRODUCTION_APPROVAL
**Recommended next:** PC14_FU03_PRODUCTION_PROPOSAL_PERSIST
**Status:** proposed only — **not applied**
**Secret scan:** PASS_WITH_REVIEW_LABELS

## Targets

| Role | Id | Name | Active | Nodes |
|------|-----|------|--------|-------|
| Production | `p4mqb4VuPcemIDlC` | SEO Content Agent Beta.v14 - Worker | true | 92 |
| Sandbox source | `tVGWi7Ud3zz2eGKo` | SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03 | false | 101 |

## Production baseline (fresh GET)

- updatedAt: `2026-07-13T21:49:02.829Z`
- TZ: `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01`
- structuredClone: 0
- FU03 nodes in production: none
- Close Lock OK: true

## Proposed patch (apply later)

- Add 9 FU03 nodes (Enable `Run Strict Surface Repair` in production)
- Modify `Format Run Pipeline` + `Prepare Memory Row Run`
- Rewire Normalize → FU03 gate → Format / Repair / Reject
- Preserve production active=true, credentials, side-effect enabled states, PC-07 lock mapping
- Do **not** copy sandbox disabled side-effects / active=false / id/name/webhook

## Explicit non-apply

- Production was **not** mutated
- Sandbox was **not** mutated
- No Telegram / OpenRouter / Sheets / `/run` / `/health` / `/locks`
- No stage / commit / push / pull

## Evidence files

- SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu03.before-proposal.sanitized.json
- SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14-fu03.proposal-source.sanitized.json
- pc14-fu03-production-proposal-diff-summary.json
- pc14-fu03-production-proposal-node-plan.json
- pc14-fu03-production-proposal-connection-plan.json
- pc14-fu03-production-proposal-side-effect-preservation.json
- pc14-fu03-production-proposal-risk-rollback.json
- pc14-fu03-production-proposal-smoke-charter.md
- pc14-fu03-production-proposal-code-node-index.json
- pc14-fu03-production-proposal-secret-scan.json
- PC14-FU03-PRODUCTION-PROPOSAL-MANIFEST.md

## Raw local (not for commit)

- local/pc14-fu03-production-proposal-2026-07-16/worker-before-proposal.raw.json
- local/pc14-fu03-production-proposal-2026-07-16/sandbox-pc14-fu03.source.raw.json

## Decision summary

```json
{
  "decision": "PC14_FU03_READY_FOR_PRODUCTION_APPROVAL",
  "recommendedNext": "PC14_FU03_PRODUCTION_PROPOSAL_PERSIST",
  "blockers": [],
  "production": {
    "active": true,
    "nodeCount": 92,
    "updatedAt": "2026-07-13T21:49:02.829Z",
    "tzVersion": "v1.1-tz-strict-cleanup-pc14-fu02-hotfix01",
    "structuredCloneCount": 0,
    "fu03Absent": true,
    "closeLockOk": true
  },
  "sandbox": {
    "liveGetOk": true,
    "active": false,
    "nodeCount": 101,
    "fu03AllPresent": true,
    "graphOk": true,
    "runRepairDisabled": true,
    "harnessAllPass": true
  },
  "secretScanStatus": "PASS_WITH_REVIEW_LABELS"
}
```
