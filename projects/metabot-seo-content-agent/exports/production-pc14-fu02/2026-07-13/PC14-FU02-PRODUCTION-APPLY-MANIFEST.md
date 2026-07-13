# PC14-FU02 Production Apply Manifest

**Date:** 2026-07-13
**Workflow:** SEO Content Agent Beta.v14 - Worker
**Workflow ID:** p4mqb4VuPcemIDlC
**Strategy:** A
**Node added:** TZ Strict Cleanup
**Sanitizer version:** v1-tz-strict-cleanup-pc14-fu02-r1
**Retargets:** Restore Outline Data, Extract SEO Strategy
**Harness:** PRODUCTION_PATCH_APPLIED_HARNESS_LOCAL
**Final decision:** PC14_FU02_PRODUCTION_APPLIED_HARNESS_VERIFIED
**Task status:** COMPLETE — PC14-FU02 production patch applied and local harness verified
**Recommended next step:** PC14_FU02_PRODUCTION_APPLY_EVIDENCE_PERSIST

## Baseline → After

| Field | Before | After |
|-------|--------|-------|
| active | true | true |
| nodeCount | 91 | 92 |
| updatedAt | 2026-07-12T19:11:34.090Z | 2026-07-13T16:40:11.596Z |
| TZ Strict Cleanup | absent | present (v1-tz-strict-cleanup-pc14-fu02-r1) |
| Graph | Run Extract Outline → Switch Run After Outline | Run Extract Outline → TZ Strict Cleanup → Switch Run After Outline |
| Strict Cleanup | v15-strict-cleanup-pc14-fu01-r1 | unchanged |
| PC-07 Close Lock | intact | intact |

## Evidence files (sanitized / repo)

- SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu02.before-apply.sanitized.json
- SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu02.after-apply.sanitized.json
- pc14-fu02-production-apply-node-diff.json
- pc14-fu02-production-apply-diff-scope-summary.json
- pc14-fu02-production-apply-harness-results.json
- PC14-FU02-PRODUCTION-APPLY-MANIFEST.md
- run-production-pc14-fu02.mjs (helper — untracked; do not stage in this task)

## Raw (local only — not staged)

- local/pc14-fu02-production-apply-2026-07-13/before/worker.raw.json
- local/pc14-fu02-production-apply-2026-07-13/after/worker.raw.json
- local/pc14-fu02-production-apply-2026-07-13/apply-results.json
- local/pc14-fu02-production-apply-2026-07-13/run-production-pc14-fu02.mjs

## Not performed

- Telegram smoke
- OpenRouter calls
- Google Sheets writes
- Intake/Admin mutation
- Sandbox mutation
- git stage / commit / push / pull
