# PC14-FU03 Operator Smoke Diagnostics — Manifest

**Date:** 2026-07-16  
**Label:** `PC14_FU03_OPERATOR_SMOKE_DIAGNOSTICS`  
**Decision:** `PC14_FU03_OPERATOR_SMOKE_DIAGNOSED_FIX_REQUIRED`  
**Recommended next:** `PC14_FU03_DIAGNOSTICS_PERSIST` → `PC14_FU03_HOTFIX01_SANDBOX_DESIGN`  
**Production apply:** `44c05c3b` / `PC14_FU03_PRODUCTION_APPLIED_HARNESS_VERIFIED`  
**Worker:** `p4mqb4VuPcemIDlC`  
**Smoke lock:** `chat:499423375:1784151029009`  

## Executions

| Role | ID | Status |
|------|----|--------|
| Intake `/run` | 3353 | success |
| Worker smoke | 3354 | error |
| Admin `/locks` | 3356 | success |
| Admin `/health` | 3358 | success |

## Root cause (one line)

`Restore Format Run Items` requires `$('Format Run Pipeline')`, which is skipped on FU03 reject branch → abort before Send Telegram / Close Lock / Memory after Status preface.

## Sanitized evidence (this folder)

- `pc14-fu03-operator-smoke-telegram-log.md`
- `pc14-fu03-operator-smoke-execution-index.json`
- `pc14-fu03-operator-smoke-worker-execution-summary.json`
- `pc14-fu03-operator-smoke-intake-execution-summary.json`
- `pc14-fu03-operator-smoke-admin-locks-summary.json`
- `pc14-fu03-operator-smoke-admin-health-summary.json`
- `pc14-fu03-operator-smoke-lock-row-summary.json`
- `pc14-fu03-operator-smoke-memory-row-summary.json`
- `pc14-fu03-operator-smoke-production-workflow-check.json`
- `pc14-fu03-operator-smoke-root-cause-analysis.json`
- `pc14-fu03-operator-smoke-recommended-next.json`
- `pc14-fu03-operator-smoke-node-output-trace.json`
- `pc14-fu03-operator-smoke-code-suspect-index.json`
- `pc14-fu03-operator-smoke-secret-scan.json`
- `run-pc14-fu03-operator-smoke-diagnostics.mjs`
- `enrich-pc14-fu03-diagnostics.mjs`

## Report

`projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu03-operator-smoke-diagnostics.md`

## Raw local (not for commit)

`local/pc14-fu03-operator-smoke-diagnostics-2026-07-16/`

## Persist posture

Diagnostics only — **do not stage/commit in this task**.
