# CORVONERO NEW CONTROLLED SEMANTIC RUN — OPERATOR CHARTER v1

**Status:** `APPROVED FOR PHASE 0/1/2`  
**Date:** 2026-06-26  
**Gate A:** `APPROVED` (2026-06-26)  
**Project:** PRJ-0013 — Корво Неро

---

## 1. Project identity

Client: **Корво Неро** · Project: **PRJ-0013** · Workspace: `corvonero-direct-v2-clean-room`  
Sites: `lk.corvonero.ru`, `corvonero.ru` (secondary/Tilda)  
ATLAS: ORG-0009, LE-0006, PRJ-0013, WEB-CORV-01, DOM-CORV-01, REL-0042

## 2. Purpose

Authorize a **completely new** controlled ORCA semantic run on the preserved **2368-phrase canonical corpus**, using **Wave 3.1F** admission brain. This is **not** a resume of clean-room v1 or old Corvonero production lines.

## 3. Operator authority required

- Charter approval (Gate A)
- Production model/provider confirmation
- Cost cap confirmation
- SPPC-05 pass/fail acceptance
- Canary and mid-run/final review decisions

## 4. Reusable inputs

Raw Wordstat (18 XLSX), normalized 2399, canonical 2368, MIG handoff, Research Pack, demand surface, keyword registry, SERP evidence, business intake, service scope, Wave 3.1F brain, deep research v1.

## 5. Prohibited old state

Old run ID/lock/checkpoint/cache; v1 diagnostic semantic decisions; forensic cache as authority; Wave 5; strategy/campaign work.

## 6. Exact canonical corpus

**2368 records** — `projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json`  
SHA-256 prefix: `eaa09b8450f82738` · IDs: `CR2-PHR-*`

## 7. ORCA Wave 3.1F authority

semantic-adjudicator.mjs, prompt-contract v1.3, hard-rules.mjs, regression suites including wave31f bypass audit. **Do not downgrade to 3.1E.**

## 8. Model/runtime policy

| Parameter | Authority |
|-----------|-----------|
| Provider | **openrouter** (operator approved 2026-06-26) |
| Model | **openai/gpt-5-mini** (operator approved; **not** `gpt-4o-mini`) |
| Temperature | 0.1 (from adapter) |
| Structured output | JSON required |
| Retry | 3 max |
| Timeout | 30000 ms default |
| Batch size | 25 default; 10 used in confirmation runs |
| Hard cost cap | **$3.00 USD** (SPPC-05 / Phase 0–2) |
| Soft cost warning | **$2.00 USD** |
| Full-corpus cost cap | **OPERATOR_DECISION_REQUIRED** before Phase 5 |
| Secrets | `.secrets/orca-live-model.env` — never Git |
| Old run resume | **PROHIBITED** |
| Old forensic cache reuse | **PROHIBITED** |
| Missing TS PIOT SERP | **NON-BLOCKING** for Phase 0/1/2 |
| Wave 5 | **BLOCKED** |

## 9. SPPC-05 gate

Closed-dataset validation before canary. **Adversarial false-accept rate ≤ 0.01** (canonical from `run-confirmation-validation.mjs`). Fail-closed — stop before full corpus on failure.

## 10. Canary

120 phrases, deterministic seed, balanced class coverage (commercial, problem, product/service, license, career, info, integration, marking, TS PIOT, geo, 1C ambiguity). Operator review sample: 30. **Not started in preflight.**

## 11. Batch plan

Bounded batches of 25 (default); concurrency 3; cumulative cost tracking; stop at cost-cap risk.

## 12. Checkpoint/lock model

STORAGE root: `C:\MARS Phenix\AI MARS STORAGE\orca\corvonero\semantic-runs\<run_id>\`  
Atomic lock, heartbeat, processed-ID registry, batch receipts, resume **only within same new run**.

## 13. Human review gates

Gates A–F — see `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-GATE-MATRIX-v1.md`

## 14. Output schemas

Run manifest, lock record, checkpoints, batch receipts, ACCEPT/REJECT/ABSTAIN registries, SPPC-05 report, canary report, cost report, reconciliation receipt, semantic registry, operator review package, handoff manifest. Raw provider responses → STORAGE only.

## 15. Git/STORAGE boundaries

Git: manifests, schemas, sanitized registries, reports, decisions.  
STORAGE: raw XLSX (existing), raw model responses, mutable cache, checkpoints, locks.

## 16. Cost and rate limits

Defaults from `cost-rate-controls.mjs`; operator must confirm cap for 2368-phrase run.

## 17. Stop conditions

Fail-closed on hash mismatch, count mismatch, ID integrity failure, ORCA authority mismatch, SPPC-05 failure, canary failure, cost-cap risk, lock conflict, operator rejection.

## 18. Failure handling

Write failure receipt; release or retain lock per policy; **new run ID** required after admission failure or corruption.

## 19. Resume policy

Resume **only** within the same approved new run ID after operator pause approval — never resume old v1 run.

## 20. Privacy and secrets

No secrets in Git; sanitize provider errors in receipts; raw responses in STORAGE with retention policy **OPERATOR_DECISION_REQUIRED**.

## 21. Search PPC handoff boundary

No SPPC-12+ strategy work until Gates E+F and separate lifecycle unfreeze.

## 22. Wave 5 prohibition

**Wave 5 BLOCKED** — do not start campaign production architecture.

## 23. Approval fields

| Field | Value |
|-------|-------|
| operator_name | Operator (charter authorization task) |
| approved_at | 2026-06-26 |
| decision | APPROVE_CHARTER — Phase 0/1/2 only |
| gate_a | APPROVED |
| phases_authorized | Phase 0, Phase 1, Phase 2 |
| phases_not_authorized | Phase 3+ (canary, production batches, Wave 5) |

## 24. Charter status

**APPROVED FOR PHASE 0/1/2** — Gate A closed; Gate B requires SPPC-05 operator review on pass

Machine-readable: `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-OPERATOR-CHARTER-v1.json`
