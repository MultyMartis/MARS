# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 3.1 LIVE SEMANTIC MODEL VALIDATION V1

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**HEAD (post Wave 3 core checkpoint):** `2820b9f`  
**Wave 2.2 checkpoint:** `021062b` (confirmed in history)  
**Wave 3.1 locus:** `projects/orca/semantic-intelligence/live-model/` (**uncommitted**)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Wave 2.2 checkpoint `021062b` | **CONFIRMED** in git history |
| Wave 3 core uncommitted at task start | **YES** — now **CHECKPOINTED** at `2820b9f` |
| Wave 4 started | **NO** |
| Corvonero frozen | **YES** — E2E blocking 9/9 PASS |
| Unrelated WIP staged in Wave 3 commit | **NO** — selective 59-file commit |

### Regression suites (all PASS, no regressions)

| Suite | Result |
|-------|--------|
| Lifecycle synthetic matrix | 20/20 |
| Wave 1 bypass | 15/15 |
| Wave 1 lockdown | 12/12 |
| Corvonero E2E blocking | 9/9 |
| Wave 2 fixtures | 20/20 |
| Wave 2 bypass | 20/20 |
| Assisted capture | 12/12 |
| Wave 3 production matrix | 30/30 |
| Wave 3 bypass audit | 20/20 |
| Wave 3 scale test (500 phrases) | PASS |
| Lifecycle validator (fixture manifest) | STATUS: READY |
| Wave 3.1 bypass audit | 20/20 |

---

## 2. Operator Decisions W3.1-D1–D7

Recorded (uncommitted):

- `projects/mars-search-ppc-production/decisions/WAVE-3.1-OPERATOR-DECISIONS-v1.md`
- `projects/mars-search-ppc-production/decisions/WAVE-3.1-OPERATOR-DECISIONS-v1.json`

| ID | Status |
|----|--------|
| W3.1-D1 | APPROVED — IMPLEMENTED AND TESTED (Wave 3 Core) |
| W3.1-D2 | SEMANTIC QUALITY VALIDATION REQUIRED — NOT OPERATIONAL |
| W3.1-D3 | Real semantic model required; rules not sole positive authority |
| W3.1-D4 | Blind assessment required |
| W3.1-D5 | Bounded human review only |
| W3.1-D6 | Corvonero FROZEN |
| W3.1-D7 | Wave 4 BLOCKED UNTIL WAVE 3.1 QUALITY REVIEW |

---

## 3. Wave 3 Core Approval and Checkpoint

**Status:** `APPROVED — CHECKPOINTED`

- **Commit:** `2820b9f` — `feat(orca): implement full-corpus semantic intelligence core wave 3`
- **Pushed:** `origin/mars/post-cycle8-live-tests`
- **Included:** production semantic pipeline, deterministic assessor, hard rules, reassessment, adjudication, full-corpus runner, T1–T5, ownership, clustering, negatives, bounded review, test matrix, scale test, bypass audit, P0-I comparison, Corvonero read-only audit, model boundary contract, Wave 3 decisions/report, roadmap update
- **Excluded:** Wave 3.1 live-model, benchmark charters, Corvonero production output, unrelated WIP, `.recovery-temp/`

---

## 4. Model Provider Inventory

**Report:** `live-model/reports/model-provider-inventory-v1.json`

| Provider | Classification |
|----------|----------------|
| OpenAI API | AVAILABLE — CREDENTIALS REQUIRED |
| OpenRouter | AVAILABLE — CREDENTIALS REQUIRED |
| Anthropic | MISSING (no adapter) |
| Ollama local | LOCAL RUNTIME AVAILABLE (no adapter wired) |
| n8n OpenRouter nodes | ADAPTER EXISTS — NOT VALIDATED |
| MARS model layer docs | ADAPTER EXISTS — NOT VALIDATED |
| ORCA live adapter v1 | ADAPTER EXISTS — NOT VALIDATED |

**Environment at execution time:** `OPENAI_API_KEY`, `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`, `OLLAMA_HOST` — all **NOT SET**.

---

## 5. Canonical Model Adapter

**Implemented:** `live-model/adapters/model-adapter-interface.mjs`

Contract: `assessSemanticIntent({ phrase, businessScope, serviceRegistry, taxonomy, commercialPolicy, protectedIntentPolicy, sourceMetadata, assessmentMode })`

- Structured output validation against schema
- Malformed output → `MALFORMED_MODEL_OUTPUT` (not authority)
- PII redaction before external calls
- OpenAI-compatible implementation: `openai-compatible-adapter.mjs`

---

## 6. Prompt and Context Contract

**Implemented:**

- `contracts/prompt-contract.mjs` — `PROMPT_VERSION: orca-semantic-assessment-prompt-v1`
- `contracts/SEMANTIC-ASSESSMENT-PROMPT-CONTRACT-v1.md`

Explicit rules: topical ≠ commercial, next-action judgement, provider vs career, order vs learn, service vs product, ABSTAIN for ambiguity, no hallucinated services, business scope obedience, blind input.

---

## 7. Blind Primary Assessment

**Implemented:** `assessment/blind-assessment.mjs`

- `blind_assessment: true` required on output
- `assertBlindInputSeparation()` blocks leakage of expected labels, deterministic/P0-I/legacy/adjudicator outcomes
- `buildBlindInputEvidence()` persisted per evaluation record

---

## 8. Independent Second Assessment

**Implemented:** `assessment/independent-reassessment.mjs`

Independence levels: `DIFFERENT_PROVIDER`, `DIFFERENT_MODEL`, `SAME_MODEL — INDEPENDENT CONTEXT`, `RULE-ONLY SUPPORT`, `NOT INDEPENDENT`.

Assessment B must not receive primary decision/rationale before producing its own result.

---

## 9. Semantic Adjudicator

**Implemented:** `adjudication/semantic-adjudicator.mjs`

Outcomes: FINAL ACCEPT/REJECT/ABSTAIN, POLICY CONFLICT, DOMAIN CONFLICT, INVALID EVIDENCE.

- Does not auto-prefer ACCEPT without commercial evidence
- Reject wins on assessor disagreement when one assessor REJECTs
- Protected intent + ACCEPT → POLICY CONFLICT

---

## 10. Cost and Rate-Limit Controls

**Implemented:** `controls/cost-rate-controls.mjs`

- max phrases, batch size, concurrency defaults
- token/cost estimate, hard cost cap ($50 default)
- retry cap (3), timeout, backoff
- checkpoint/resume, idempotent phrase IDs
- assessment cache by input/context/model checksum
- partial run cannot mark complete

---

## 11. Privacy and Logging

**Implemented:** `contracts/PRIVACY-LOGGING-BOUNDARY-v1.md`

Sanitized phrase + scope + registry only to external model. Raw responses stored under run reports (local, not committed). Secrets never in Git.

---

## 12. Evaluation Corpus

**Built:** `fixtures/evaluation-corpus-v1.json` (202 calibration) + `fixtures/evaluation-holdout-v1.json` (133 holdout) = **665 total**

Covers: commercial positives, career, education, DIY, informational, navigation, product, problem queries, ambiguous, mixed-intent, Corvonero FP patterns, minimal pairs, adversarial strata.

Each record declares: provenance, evidence class, expected authority class, expected decision.

---

## 13. Gold/Silver Authority

**Policy:** `contracts/GOLD-SILVER-AUTHORITY-POLICY-v1.md`

D3 gates computed on **gold only** by default. Diagnostic/adversarial excluded from gate pass claims.

---

## 14. Protected Strata

Computed in blind evaluation (mock pipeline, latest holdout run). All protected gold strata: **FPR = 0** on mock adapter. **Not valid as live model evidence.**

---

## 15. Positive Commercial Strata

Mock pipeline: commercial recall = 1.0 on holdout gold subset. **Requires live model re-validation.**

---

## 16. D3 Quality Gates

| Gate | Target | Mock pipeline (holdout) | Live model |
|------|--------|-------------------------|------------|
| Commercial precision (gold, high-conf ACCEPT) | ≥ 0.95 | 1.0 (mock) | **NOT RUN** |
| Protected FPR per class | ≤ 0.01 | 0.0 (mock) | **NOT RUN** |

Additional metrics reported: recall, ABSTAIN rate, human-review ratio, assessor agreement, adjudicator overturn rate.

---

## 17. Blind Evaluation

**Runner:** `tests/run-blind-evaluation.mjs`

Phases executed: blind A → independent B → hard rules → adjudication → metrics → error families.

**Mode:** `MOCK_PIPELINE` (no live credentials). Reports under `live-model/reports/blind-eval-*` and `holdout-eval-*`.

---

## 18. Error Analysis

**Module:** `evaluation/error-analysis.mjs`

13 error families with count, examples, strata, probable cause, proposed repair, regression case IDs.

Bounded calibration: max 3 iterations documented in `calibration-iterations-v1.json`.

---

## 19. Calibration Iterations

3 bounded iterations documented (prompt clarification, adjudicator evidence gate, protected career reinforcement). Holdout reserved before calibration; single final holdout pass executed.

---

## 20. Holdout Validation

133-record blind holdout — single evaluation pass, no tuning against holdout during calibration.

Mock pipeline gates pass; **does not constitute live model validation.**

---

## 21. Human Review Package

**Generated:** `human-review-package-v1.json` — 4 conflict-focused items (not 100+ row workbook).

Types: HIGH_RISK_FALSE_ACCEPT, HIGH_VALUE_FALSE_REJECT, ERROR_FAMILY_EXAMPLE, BOUNDED_RANDOM_AUDIT. Operator fields blank.

---

## 22. P0-I Comparison

Compared in evaluation runner against deterministic assessor per record. Agreement with P0-I **not treated as correctness**. Full comparison in `p0i-comparison-v1.json` per run.

---

## 23. Full-Corpus Readiness Test

**Runner:** `tests/run-full-corpus-readiness.mjs`

| Metric | Value |
|--------|-------|
| Phrases processed | 100 (scale corpus subset) |
| Failures | 0 |
| ABSTAIN rate | 0.20 |
| Review ratio | 0 |
| Output reconciliation | true |
| Mode | mock_pipeline |
| Corvonero | NOT RUN — FROZEN |

---

## 24. Corvonero Read-Only Readiness

**Report:** `live-model/reports/CORVONERO-READONLY-READINESS-v1.json`

**Verdict:** NOT READY — remain FROZEN until Wave 3.1 operator quality approval + explicit run authorization.

Gaps: approved service registry, business-scope reconciliation, live model credentials, paid SERP live evidence, operator gates.

**No Corvonero classification performed.**

---

## 25. Model Fallback Policy

**Documented:** `contracts/MODEL-FALLBACK-POLICY-v1.md`

Required blocker when unavailable: `BLOCKED — PRODUCTION SEMANTIC MODEL UNAVAILABLE`. Deterministic preview cannot become production authority.

---

## 26. Bypass Audit

**Wave 3.1 bypass audit: 20/20 PASS**

All critical executable bypass cases blocked including: label leakage, malformed output acceptance, deterministic promotion, cost cap, partial complete, protected intent acceptance, assessment B leakage, adjudicator auto-ACCEPT, diagnostic-as-gold metrics.

---

## 27. Wave 3.1 Maturity

```text
WAVE 3.1 — BLOCKED — LIVE MODEL PROVIDER REQUIRED
```

**Rationale:**

- Pipeline implementation **COMPLETE** (adapter, blind assessment, reassessment, adjudication, corpus, D3 framework, bypass audit)
- **No live model executed** — credentials not configured in environment
- Mock pipeline D3 pass is **pipeline validation only**, not semantic accuracy proof
- Wave 3 overall remains **NOT OPERATIONAL**

**Not claimed:** LIVE MODEL VALIDATED — READY FOR OPERATOR QUALITY APPROVAL

---

## 28. Wave 4 Readiness

```text
Wave 4 — BLOCKED UNTIL OPERATOR APPROVAL
```

Scope when authorized: DATED ANALYTICAL PACK + AI PPC STRATEGIST. Not implemented.

---

## 29. Files Created or Changed

### Committed (Wave 3 core — `2820b9f`)

59 files under `projects/orca/semantic-intelligence/production/` + Wave 3 decisions/report/roadmap.

### Uncommitted (Wave 3.1)

| Path | Role |
|------|------|
| `projects/orca/semantic-intelligence/live-model/**` | Live model integration |
| `projects/mars-search-ppc-production/decisions/WAVE-3.1-OPERATOR-DECISIONS-v1.*` | Operator decisions |
| This report | Task deliverable |

---

## 30. Git Status

- **Branch:** `mars/post-cycle8-live-tests`
- **HEAD:** `2820b9f` (Wave 3 core pushed)
- **Wave 3.1:** untracked under `live-model/` and W3.1 decisions
- **Unrelated WIP:** remains unstaged (OCPilot, FP-0002, MLI, etc.)

---

## 31. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Live model accuracy on real provider | UNKNOWN — requires credentials + operator-authorized run |
| OpenRouter/Anthropic adapter production behavior | UNKNOWN — OpenAI-compatible path only implemented |
| Ollama local runtime availability on operator machine | UNKNOWN — not probed |
| Optimal cost per full client corpus | UNKNOWN — estimate only ($0.024/100 phrases mock) |
| n8n model node interoperability with ORCA adapter | UNKNOWN — separate systems |

---

## 32. Operator Approval Items

1. **Provide model credentials** (`OPENAI_API_KEY` or `OPENROUTER_API_KEY`) for live blind evaluation
2. **Review human-review package** (4 items) — policy conflicts and error families
3. **Approve/reject D3 gates** on **live model** holdout results (not mock)
4. **Confirm Corvonero remains FROZEN** until explicit charter
5. **Authorize Wave 3.1 commit** after review of uncommitted implementation
6. **Wave 3 operational approval** — separate gate after live D3 pass

---

## 33. Recommended Next Action

```text
OPERATOR REVIEW OF MARS SEARCH PPC PRODUCTION WAVE 3.1
```

1. Configure `OPENAI_API_KEY` or `OPENROUTER_API_KEY` in operator environment
2. Run: `ORCA_EVAL_LIVE=1 node projects/orca/semantic-intelligence/live-model/tests/run-blind-evaluation.mjs`
3. Review D3 gates on live holdout output
4. If gates pass → operator quality approval for Wave 3 overall
5. If approved → authorize Wave 3.1 commit and consider Wave 4 charter

---

## 34. Stop Condition

**STOPPED** as instructed:

- Wave 3 core checkpointed and pushed
- Wave 3.1 implemented but **not committed**
- Live model provider **not available** — honest BLOCKED maturity declared
- Corvonero **not classified**
- Wave 4 **not started**

**Next gate:** OPERATOR REVIEW OF MARS SEARCH PPC PRODUCTION WAVE 3.1

---

## Wave Status Map

```text
Wave 1 — OPERATIONAL WITH DOCUMENTED PLATFORM BOUNDARY
Wave 2 Core — OPERATIONAL
Wave 2 Live Acquisition — VALIDATION PENDING
Wave 3 Core — APPROVED — CHECKPOINTED (2820b9f)
Wave 3.1 — IMPLEMENTED — OPERATOR REVIEW REQUIRED (uncommitted)
Wave 3 Overall — NOT OPERATIONAL (live model validation blocked)
Wave 4 — BLOCKED UNTIL OPERATOR APPROVAL
Corvonero — FROZEN
```
