# PC14-FU03 Repair Loop Proposal — Manifest

**Date:** 2026-07-16  
**Proposal:** `PC14_FU03_REPAIR_LOOP_PROPOSAL`  
**Based on audit:** `PC14_FU03_GOVERNANCE_AUDIT_COMPLETE_REPAIR_LOOP_RECOMMENDED` (`230b490a`)  
**Related smoke:** Task `seo20260713221847nksocr` · Worker execution `3352`  
**Classification:** Proposal-only · no sandbox/production mutation · no stage/commit  

## Evidence files (this folder)

| File | Role |
|------|------|
| `pc14-fu03-repair-loop-proposed-architecture.json` | Layered governance architecture |
| `pc14-fu03-repair-loop-node-plan.json` | Sandbox node insert/modify plan |
| `pc14-fu03-repair-loop-surface-policy.json` | Marker SOT + Strategy/QA/Factcheck surface policy |
| `pc14-fu03-repair-loop-memory-get-contract.json` | Memory statuses + `/get` contract |
| `pc14-fu03-repair-loop-harness-plan.json` | FU03 harness labels and fixtures |
| `pc14-fu03-repair-loop-risk-matrix.json` | Risk matrix + mitigations |
| `PC14-FU03-REPAIR-LOOP-PROPOSAL-MANIFEST.md` | This manifest |

## Report

`projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu03-repair-loop-proposal.md`

## Recommended decision

| Field | Value |
|-------|-------|
| Decision | `PC14_FU03_REPAIR_LOOP_PROPOSAL_READY_FOR_SANDBOX_DESIGN` |
| Recommended next | `PC14_FU03_PROPOSAL_PERSIST` |
| Path | Option C — multi-surface scan + bounded LLM repair |

## Constraints honored

- No production / sandbox patch
- No n8n workflow create/update
- No Telegram / OpenRouter / Sheets / `/run`
- No stage / commit / push / pull
- Foreign WIP preserved
