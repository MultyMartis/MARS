# Wave 3.1 Completion Pass Operator Decisions v1

**Date:** 2026-06-23  
**Decision set:** `wave-3.1c-completion-pass-decisions-v1`  
**Task:** MARS SEARCH PPC PRODUCTION — WAVE 3.1 LIVE PROVIDER COMPLETION PASS

| ID | Subject | Status |
|----|---------|--------|
| W3.1C-D1 | Wave 3.1 implementation | APPROVED — READY FOR CHECKPOINT |
| W3.1C-D2 | Semantic quality | LIVE PROVIDER VALIDATION REQUIRED |
| W3.1C-D3 | Provider credentials | Environment-only boundary; `OPENAI_API_KEY` and `OPENROUTER_API_KEY` permitted; never committed |
| W3.1C-D4 | Staged execution | Six-stage gate: connectivity → structured output → pilot → calibration → holdout → full-corpus readiness |
| W3.1C-D5 | Cost control | Per-stage hard cost cap required; block if cap unset or forecast exceeds cap |
| W3.1C-D6 | Holdout | Single final blind holdout; no tuning on holdout records |
| W3.1C-D7 | Corvonero | FROZEN — no corpus sent to model; no production classification |

## Wave status snapshot

```text
Wave 3.1 Implementation — APPROVED — READY FOR CHECKPOINT
Wave 3.1 Live Quality — VALIDATION IN PROGRESS
Wave 3 Overall — NOT OPERATIONAL
Wave 4 — BLOCKED
Corvonero — FROZEN
```
