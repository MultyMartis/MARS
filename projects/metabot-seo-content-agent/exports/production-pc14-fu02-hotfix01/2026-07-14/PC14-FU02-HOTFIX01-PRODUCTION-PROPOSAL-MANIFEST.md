# PC14-FU02 HOTFIX01 Production Proposal Manifest

**Date:** 2026-07-14
**Hotfix:** PC14_FU02_HOTFIX01_STRUCTUREDCLONE_VM_SAFE
**Proposal:** PC14_FU02_HOTFIX01_PRODUCTION_PROPOSAL
**Decision:** PC14_FU02_HOTFIX01_READY_FOR_PRODUCTION_APPROVAL
**Recommended next:** PC14_FU02_HOTFIX01_PRODUCTION_APPLY
**Status:** proposed only — **not applied**
**Production Worker:** SEO Content Agent Beta.v14 - Worker (`p4mqb4VuPcemIDlC`)
**Production active (baseline):** true
**Production node count (baseline):** 92
**Production updatedAt (baseline):** 2026-07-13T16:40:11.596Z
**Broken TZ version:** v1-tz-strict-cleanup-pc14-fu02-r1
**Proposed TZ version:** v1.1-tz-strict-cleanup-pc14-fu02-hotfix01
**Method:** GET_ONLY fresh baseline + sandbox source verification
**Sandbox source:** 6xpeMYaPxK7uGkIM (commit e9d12305)
**Change:** 2× `structuredClone` → VM-safe `clonePlain` in `TZ Strict Cleanup` only
**Secret scan:** PASS_WITH_REVIEW_LABELS

## Explicit non-apply

- Production was **not** mutated in this task.
- Sandbox was **not** mutated in this task.
- No Telegram / OpenRouter / Sheets calls.
- No `/run` retry.

## Evidence files (sanitized / repo)

- SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu02-hotfix01.before-proposal.sanitized.json
- SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14-fu02-hotfix01.source.sanitized.json
- pc14-fu02-hotfix01-production-proposal-diff-preview.json
- pc14-fu02-hotfix01-production-proposal-scope-summary.json
- PC14-FU02-HOTFIX01-PRODUCTION-PROPOSAL-MANIFEST.md

## Raw (local only — not staged)

- local/pc14-fu02-hotfix01-production-proposal-2026-07-14/worker-before-proposal.raw.json
- local/pc14-fu02-hotfix01-production-proposal-2026-07-14/sandbox-hotfix01.source.raw.json (if GET succeeded)

## Baseline checks (summary)

```json
{
  "decision": "PC14_FU02_HOTFIX01_READY_FOR_PRODUCTION_APPROVAL",
  "recommendedNext": "PC14_FU02_HOTFIX01_PRODUCTION_APPLY",
  "blockers": [],
  "production": {
    "active": true,
    "nodeCount": 92,
    "updatedAt": "2026-07-13T16:40:11.596Z",
    "tzVersion": "v1-tz-strict-cleanup-pc14-fu02-r1",
    "structuredCloneCount": 2,
    "graphOk": true,
    "closeLockOk": true,
    "nonTargetDriftCount": 0
  },
  "sandbox": {
    "active": false,
    "tzVersion": "v1.1-tz-strict-cleanup-pc14-fu02-hotfix01",
    "structuredCloneCount": 0,
    "clonePlainPresent": true,
    "harnessAllPass": true,
    "vmAllPass": true,
    "scopeOk": true
  },
  "secretScanStatus": "PASS_WITH_REVIEW_LABELS"
}
```
