# PC14-FU02 HOTFIX01 Sandbox Patch Manifest

**Date:** 2026-07-14
**Hotfix:** PC14_FU02_HOTFIX01_STRUCTUREDCLONE_VM_SAFE
**Sandbox workflow:** SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu02-hotfix01
**Sandbox ID:** 6xpeMYaPxK7uGkIM
**Webhook path (inactive):** seo-content-agent-worker-sandbox-pc14-fu02-hotfix01
**Active:** false
**Broken version:** v1-tz-strict-cleanup-pc14-fu02-r1
**Hotfix version:** v1.1-tz-strict-cleanup-pc14-fu02-hotfix01
**Node patched:** TZ Strict Cleanup
**Change:** replace `structuredClone` with VM-safe `clonePlain`
**Harness:** SANDBOX_HOTFIX01_HARNESS_LOCAL_WITH_RESTRICTED_VM
**Harness allPass:** true
**VM allPass:** true
**Diff scopeOk:** true
**Production Worker unchanged:** true
**Final decision:** PC14_FU02_HOTFIX01_SANDBOX_APPLIED_HARNESS_VERIFIED
**Recommended next step:** PC14_FU02_HOTFIX01_PRODUCTION_PROPOSAL

## Graph (preserved)

```
Run Outline → Run Extract Outline → TZ Strict Cleanup → Switch Run After Outline
```

## Retargets (preserved)

- Restore Outline Data → `$('TZ Strict Cleanup')`
- Extract SEO Strategy → `$node['TZ Strict Cleanup'].json`

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

- SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14-fu02-hotfix01.before-patch.sanitized.json
- SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14-fu02-hotfix01.after-patch.sanitized.json
- pc14-fu02-hotfix01-tz-strict-cleanup-node-diff.json
- pc14-fu02-hotfix01-diff-scope-summary.json
- pc14-fu02-hotfix01-harness-results.json
- PC14-FU02-HOTFIX01-SANDBOX-PATCH-MANIFEST.md

## Helper scripts (untracked / evidence-local)

- run-sandbox-pc14-fu02-hotfix01.mjs
- pc14-fu02-hotfix01-harness.mjs
- pc14-fu02-hotfix01-patch.mjs

## Raw (gitignored)

- local/sandbox-pc14-fu02-hotfix01-2026-07-14/before/
- local/sandbox-pc14-fu02-hotfix01-2026-07-14/after/

## Prior FU-02 sandbox

- SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu02 / WCBIB9L2I8VbGtRs — inspect-only; not overwritten
