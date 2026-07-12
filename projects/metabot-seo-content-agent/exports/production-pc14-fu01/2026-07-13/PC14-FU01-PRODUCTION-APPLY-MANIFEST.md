# PC14-FU-01 Production Apply Manifest

**Date:** 2026-07-13
**Workflow:** SEO Content Agent Beta.v14 - Worker
**Workflow ID:** p4mqb4VuPcemIDlC
**Patch node:** Strict Cleanup (jsCode only)
**Version:** v14-strict-cleanup-pc14-r1 → v15-strict-cleanup-pc14-fu01-r1
**Harness:** PRODUCTION_PATCH_APPLIED_HARNESS_LOCAL
**Final decision:** PC14_FU01_PRODUCTION_APPLIED_HARNESS_VERIFIED
**Task status:** COMPLETE — PC14-FU-01 production patch applied and local harness verified

## Baseline

| Field | Before | After |
|-------|--------|-------|
| active | true | true |
| nodeCount | 91 | 91 |
| updatedAt | 2026-07-10T14:58:37.818Z | 2026-07-12T19:11:34.090Z |
| Strict Cleanup | v14-strict-cleanup-pc14-r1 | v15-strict-cleanup-pc14-fu01-r1 |

## Evidence files

- SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu01.before-apply.sanitized.json
- SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu01.after-apply.sanitized.json
- pc14-fu01-production-apply-baseline.json
- pc14-fu01-production-strict-cleanup-node-diff.json
- pc14-fu01-production-diff-scope-summary.json
- pc14-fu01-production-harness-results.json
- PC14-FU01-PRODUCTION-APPLY-MANIFEST.md
- run-production-pc14-fu01.mjs

## Raw (gitignored)

- local/pc14-fu01-production-apply-2026-07-13/before/worker.raw.json
- local/pc14-fu01-production-apply-2026-07-13/after/worker.raw.json
- local/pc14-fu01-production-apply-2026-07-13/apply-results.json

## Not performed

- Telegram smoke
- OpenRouter calls
- Google Sheets writes
- Intake/Admin mutation
- git stage / commit / push
