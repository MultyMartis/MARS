# PC14-FU02 HOTFIX01 Production Apply Manifest

**Date:** 2026-07-14
**Hotfix:** PC14_FU02_HOTFIX01_STRUCTUREDCLONE_VM_SAFE
**Apply:** PC14_FU02_HOTFIX01_PRODUCTION_APPLY
**Decision:** PC14_FU02_HOTFIX01_PRODUCTION_APPLIED_HARNESS_VERIFIED
**Recommended next:** PC14_FU02_HOTFIX01_PRODUCTION_APPLY_EVIDENCE_PERSIST
**Status:** COMPLETE — PC14-FU02 HOTFIX01 production apply completed and harness verified
**Production Worker:** SEO Content Agent Beta.v14 - Worker (`p4mqb4VuPcemIDlC`)
**Production active:** true
**Production node count:** 92
**updatedAt before:** 2026-07-13T16:40:11.596Z
**updatedAt after:** 2026-07-13T21:49:02.829Z
**TZ version before:** v1-tz-strict-cleanup-pc14-fu02-r1
**TZ version after:** v1.1-tz-strict-cleanup-pc14-fu02-hotfix01
**Change:** 2× `structuredClone` → VM-safe `clonePlain` in `TZ Strict Cleanup` only
**Sandbox donor:** SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu02-hotfix01 (`6xpeMYaPxK7uGkIM`) — not mutated
**Harness:** TZ01–TZ07 · NR01–NR09 · SG01–SG05 · VM01–VM06 PASS
**Secret scan:** PASS_WITH_REVIEW_LABELS

## Baseline → After

| Field | Before | After |
|-------|--------|-------|
| active | true | true |
| nodeCount | 92 | 92 |
| updatedAt | 2026-07-13T16:40:11.596Z | 2026-07-13T21:49:02.829Z |
| TZ Strict Cleanup | v1-tz-strict-cleanup-pc14-fu02-r1 (structuredClone×2) | v1.1-tz-strict-cleanup-pc14-fu02-hotfix01 (clonePlain) |
| Graph | Extract → TZ → Switch | preserved |
| Strict Cleanup v15 | unchanged | unchanged |
| PC-07 Close Lock | intact | intact |

## Evidence files (sanitized / repo)

- SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu02-hotfix01.before-apply.sanitized.json
- SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu02-hotfix01.after-apply.sanitized.json
- pc14-fu02-hotfix01-production-apply-node-diff.json
- pc14-fu02-hotfix01-production-apply-diff-scope-summary.json
- pc14-fu02-hotfix01-production-apply-harness-results.json
- PC14-FU02-HOTFIX01-PRODUCTION-APPLY-MANIFEST.md
- run-pc14-fu02-hotfix01-production-apply.mjs (helper — untracked; do not stage in this task)

## Raw (local only — not staged)

- local/pc14-fu02-hotfix01-production-apply-2026-07-14/rollback/worker-before-hotfix01.raw.json
- local/pc14-fu02-hotfix01-production-apply-2026-07-14/after/worker-after-hotfix01.raw.json
- local/pc14-fu02-hotfix01-production-apply-2026-07-14/apply-results.json

## Not performed

- Telegram smoke
- OpenRouter calls
- Google Sheets writes
- Intake/Admin mutation
- Sandbox mutation
- git stage / commit / push / pull
