# PC14-FU02 Sandbox Patch Manifest

**Date:** 2026-07-13
**Sandbox workflow:** SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu02
**Sandbox ID:** WCBIB9L2I8VbGtRs
**Webhook path (inactive):** seo-content-agent-worker-sandbox-pc14-fu02
**Active:** false
**Strategy:** A
**Node added:** TZ Strict Cleanup
**Sanitizer version:** v1-tz-strict-cleanup-pc14-fu02-r1
**Retargets:** Restore Outline Data, Extract SEO Strategy
**Harness:** SANDBOX_PATCH_APPLIED_HARNESS_LOCAL
**Final decision:** PC14_FU02_SANDBOX_PATCH_APPLIED_HARNESS_VERIFIED
**Recommended next step:** PC14_FU02_PRODUCTION_PROPOSAL
**Production Worker unchanged:** true

## Graph

```
Run Outline → Run Extract Outline → TZ Strict Cleanup → Switch Run After Outline
```

## Side-effect nodes disabled (sandbox)

- Append Memory Local
- Append Memory Run
- Append Memory Single
- Close Lock Before Sending
- Close Single Lock Before Sending
- Finish Lock
- OpenRouter Single Mode
- Run Auto Polish Text
- Run Factcheck
- Run Outline
- Run SEO QA
- Run SEO Strategy
- Run Single Text Repair
- Run Text
- Run Text Repair
- Send Telegram Local
- Send Telegram Memory Get
- Send Telegram Run
- Send Telegram Single
- Status Complete
- Status Factcheck
- Status Final
- Status Outline
- Status SEO QA
- Status Single
- Status Single Complete
- Status Strategy
- Status Text

## Evidence files

- SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14-fu02.before-patch.sanitized.json
- SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14-fu02.after-patch.sanitized.json
- pc14-fu02-tz-strict-cleanup-node-diff.json
- pc14-fu02-diff-scope-summary.json
- pc14-fu02-harness-results.json
- PC14-FU02-SANDBOX-PATCH-MANIFEST.md

## Helper scripts (untracked / evidence-local)

- run-sandbox-pc14-fu02.mjs
- pc14-fu02-harness.mjs
- pc14-fu02-patch.mjs

## Raw (gitignored)

- local/sandbox-pc14-fu02-2026-07-13/before/
- local/sandbox-pc14-fu02-2026-07-13/after/
