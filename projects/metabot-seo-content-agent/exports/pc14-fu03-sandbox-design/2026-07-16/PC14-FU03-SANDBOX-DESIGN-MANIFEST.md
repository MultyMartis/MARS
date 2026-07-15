# PC14-FU03 Sandbox Design Manifest

**Date:** 2026-07-16  
**Design:** `PC14_FU03_SANDBOX_DESIGN`  
**Based on proposal:** `PC14_FU03_REPAIR_LOOP_PROPOSAL_READY_FOR_SANDBOX_DESIGN`  
**Proposal commit:** `56e82a05`  
**Related smoke Task ID:** `seo20260713221847nksocr`  
**Related Worker execution:** `3352`  

## Summary

Implementation-ready sandbox design for Option C: central strict marker SOT, final multi-surface scan gate, bounded LLM repair (max 1), re-scan, hard block if dirty, Strategy JSON hidden by default, QA/Factcheck summaries only if clean, memory/`/get` status contract.

## Sandbox target

| Field | Value |
|-------|-------|
| Clone from | Production Worker `p4mqb4VuPcemIDlC` (92 nodes, HOTFIX01 baseline) |
| Sandbox name | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03` |
| Active | `false` |
| Estimated nodes after | ~101 (9 new + 2–3 modified) |
| Insertion | After `Normalize Run Output`, before `Format Run Pipeline` |

## Format strategy decision

**Preferred: Choice 1 (minimal `Format Run Pipeline` edit)** — consume `public_payload` when present; remove raw Strategy JSON dump; preserve existing `Take First Item` / lock / Telegram multi-part wiring.  
**Rejected for v1: Choice 2** — separate `Format Final Public Payload` duplicates split logic and increases drift risk.

## New nodes (9)

1. Build Final Public Payload  
2. Final Surface Strict Scan  
3. IF Final Surface Clean  
4. Build Strict Surface Repair Payload  
5. Run Strict Surface Repair  
6. Extract Strict Surface Repair  
7. Final Surface Strict Re-Scan  
8. IF Repaired Surface Clean  
9. Format Strict Reject Message  

## Modified nodes (2 required + 1 optional)

- Format Run Pipeline (required)  
- Prepare Memory Row Run (required)  
- Route Command (optional NL strict detect)  

## Decision

| Field | Value |
|-------|-------|
| **Decision** | `PC14_FU03_SANDBOX_DESIGN_READY_FOR_IMPLEMENTATION` |
| **Recommended next** | `PC14_FU03_SANDBOX_DESIGN_PERSIST` |
| **Then** | `PC14_FU03_SANDBOX_IMPLEMENTATION` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` |

## Evidence files (this design task)

- `pc14-fu03-sandbox-design-node-plan.json`  
- `pc14-fu03-sandbox-design-graph-plan.json`  
- `pc14-fu03-sandbox-design-data-contracts.json`  
- `pc14-fu03-sandbox-design-harness-plan.json`  
- `pc14-fu03-sandbox-design-risk-rollback.json`  
- `pc14-fu03-sandbox-design-implementation-checklist.json`  
- `PC14-FU03-SANDBOX-DESIGN-MANIFEST.md`  

## Report

- `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu03-sandbox-design.md`

No stage. No commit.
