# PC14-FU03 HOTFIX01 Sandbox Design — Manifest

**Date:** 2026-07-16  
**Label:** `PC14_FU03_HOTFIX01_SANDBOX_DESIGN`  
**Based on diagnostics:** `PC14_FU03_OPERATOR_SMOKE_DIAGNOSED_FIX_REQUIRED`  
**Diagnostics commit:** `cab4597a`  
**Production apply commit:** `44c05c3b`  
**Production Worker:** `p4mqb4VuPcemIDlC`  
**Smoke lock key:** `chat:499423375:1784151029009`  
**Decision:** `PC14_FU03_HOTFIX01_SANDBOX_DESIGN_READY_FOR_IMPLEMENTATION`  
**Recommended next:** `PC14_FU03_HOTFIX01_DESIGN_PERSIST` → then `PC14_FU03_HOTFIX01_SANDBOX_IMPLEMENTATION`  
**Secret scan:** `PASS_WITH_REVIEW_LABELS`

## Selected design

Option **A** — reject-safe dual-source restore on:
- `Restore Format Run Items`
- `Restore Format Run Items After Lock`

Fallback order: `Format Run Pipeline` → `Format Strict Reject Message` → explicit throw.

Optional hardening: reorder `Format Strict Reject Message` fan-out to put `Prepare Memory Row Run` first.

Node delta: **0**.

## Evidence files (this folder)

- PC14-FU03-HOTFIX01-SANDBOX-DESIGN-MANIFEST.md
- pc14-fu03-hotfix01-root-cause-summary.json
- pc14-fu03-hotfix01-design-options.json
- pc14-fu03-hotfix01-selected-design.json
- pc14-fu03-hotfix01-node-plan.json
- pc14-fu03-hotfix01-graph-plan.json
- pc14-fu03-hotfix01-harness-plan.json
- pc14-fu03-hotfix01-risk-matrix.json
- pc14-fu03-hotfix01-lock-cleanup-policy.json
- pc14-fu03-hotfix01-rollback-plan.json
- pc14-fu03-hotfix01-code-sketches.json
- pc14-fu03-hotfix01-restore-node-analysis.json
- pc14-fu03-hotfix01-secret-scan.json

## Report

`projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu03-hotfix01-sandbox-design.md`

## Raw local (not for commit)

`local/pc14-fu03-hotfix01-sandbox-design-2026-07-16/`

## Persist posture

Design only — **do not stage/commit in this task**.
