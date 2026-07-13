# PC14-FU02 Production Proposal Manifest

**Date:** 2026-07-13
**Proposal:** PC14_FU02_PRODUCTION_PROPOSAL
**Decision:** PC14_FU02_READY_FOR_PRODUCTION_APPROVAL
**Status:** proposed only — **not applied**
**Production Worker:** SEO Content Agent Beta.v14 - Worker (`p4mqb4VuPcemIDlC`)
**Production active (baseline):** true
**Production node count (baseline):** 91
**Production updatedAt (baseline):** 2026-07-12T19:11:34.090Z
**Method:** GET_ONLY fresh baseline
**Sandbox source:** WCBIB9L2I8VbGtRs (commit ee0c4653)
**Strategy:** A
**Proposed node:** TZ Strict Cleanup
**Proposed version:** v1-tz-strict-cleanup-pc14-fu02-r1
**Proposed graph:** Run Extract Outline → TZ Strict Cleanup → Switch Run After Outline
**Proposed retargets:** Restore Outline Data, Extract SEO Strategy
**Recommended next step:** PC14_FU02_PRODUCTION_APPLY

## Explicit non-apply

- Production was **not** mutated in this task.
- Sandbox was **not** mutated in this task.
- No Telegram / OpenRouter / Sheets calls.

## Evidence files (sanitized / repo)

- SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu02.preproposal.sanitized.json
- pc14-fu02-production-preproposal-baseline.json
- pc14-fu02-production-proposed-node-diff.json
- pc14-fu02-production-proposed-scope-summary.json
- PC14-FU02-PRODUCTION-PROPOSAL-MANIFEST.md

## Raw (local only — not staged)

- local/pc14-fu02-production-proposal-2026-07-13/worker.raw.json
- local/pc14-fu02-production-proposal-2026-07-13/run-pc14-fu02-production-preproposal.mjs

## Baseline checks (summary)

```json
{
  "decision": "PC14_FU02_READY_FOR_PRODUCTION_APPROVAL",
  "blockers": [],
  "active": true,
  "nodeCount": 91,
  "hasTzStrictCleanup": false,
  "expectedPreGraph": true,
  "strictCleanupVersion": "v15-strict-cleanup-pc14-fu01-r1",
  "closeLockOk": true,
  "nonTargetDriftCount": 0,
  "sandboxGraphOk": true
}
```
