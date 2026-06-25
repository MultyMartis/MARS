# REPORT — MARS SEARCH PPC PRODUCTION — WAVE 3.1 LIVE PROVIDER COMPLETION V1

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**HEAD (post Wave 3.1 checkpoint):** `7f7cb21`  
**Wave 3 core checkpoint:** `2820b9f` (confirmed in history)  
**Wave 2.2 checkpoint:** `021062b` (confirmed in history)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| `2820b9f` in git history | **CONFIRMED** — ancestor of HEAD |
| Wave 3.1 implementation uncommitted at task start | **YES** — now **CHECKPOINTED** at `7f7cb21` |
| Wave 4 started | **NO** |
| Corvonero frozen | **YES** — E2E blocking 9/9 PASS |
| Unrelated WIP staged in Wave 3.1 commit | **NO** — selective 34-file commit |

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
| Cursor task linter (example contract) | VALID |

**Preflight verdict:** PASS — no Wave 3.1 regression before checkpoint.

---

## 2. Operator Decisions W3.1C-D1–D7

Recorded (completion-pass set, uncommitted with this report):

- `projects/mars-search-ppc-production/decisions/WAVE-3.1C-COMPLETION-PASS-DECISIONS-v1.md`
- `projects/mars-search-ppc-production/decisions/WAVE-3.1C-COMPLETION-PASS-DECISIONS-v1.json`

| ID | Status |
|----|--------|
| W3.1C-D1 | APPROVED — READY FOR CHECKPOINT |
| W3.1C-D2 | LIVE PROVIDER VALIDATION REQUIRED |
| W3.1C-D3 | Environment-only credentials; `OPENAI_API_KEY` / `OPENROUTER_API_KEY` permitted; never committed |
| W3.1C-D4 | Six-stage gated execution required |
| W3.1C-D5 | Per-stage hard cost cap required |
| W3.1C-D6 | Single final blind holdout; no tuning on holdout |
| W3.1C-D7 | Corvonero FROZEN |

---

## 3. Wave 3.1 Framework Approval and Checkpoint

**Status:** `APPROVED — CHECKPOINTED`

- **Commit:** `7f7cb21` — `feat(orca): implement live semantic validation framework wave 3.1`
- **Pushed:** `origin/mars/post-cycle8-live-tests`
- **Included (34 files):** provider-neutral adapter, OpenAI-compatible adapter, schemas, prompt/context contract, blind assessment, independent reassessment, model adjudicator, cost/rate/cache/checkpoint controls, privacy/logging boundary, evaluation corpus (665 records: 202 calibration + 133 holdout + indexes), gold/silver authority policy, D3 metrics, calibration framework, holdout framework, human-review generator, mock/full-corpus readiness fixtures, bypass tests, Corvonero read-only readiness audit, W3.1 + W3.1C decisions, implementation report, roadmap update, pre-live security precheck, reports `.gitignore`
- **Excluded:** live provider responses, API keys, raw secret logs, completion-pass results, dynamic `blind-eval-*` / `holdout-eval-*` folders, benchmark charters, Corvonero production output, Wave 4, unrelated WIP, `.recovery-temp/`

---

## 4. Provider Environment Check

| Variable | Status |
|----------|--------|
| `OPENAI_API_KEY` | NOT SET |
| `OPENROUTER_API_KEY` | NOT SET |
| `ANTHROPIC_API_KEY` | NOT SET |
| `OLLAMA_HOST` | NOT SET |
| `ORCA_LIVE_PROVIDER` | NOT SET |
| `ORCA_LIVE_MODEL` | NOT SET |
| `ORCA_EVAL_MAX_COST` | NOT SET |

**Provider selection priority applied:**

1. `ORCA_LIVE_PROVIDER` — not set  
2. OpenAI-compatible configured provider — **NOT AVAILABLE**  
3. Other implemented provider — **none configured**  
4. Result — **BLOCKED**

```text
WAVE 3.1 COMPLETION PASS — BLOCKED
REASON: LIVE MODEL PROVIDER REQUIRED
```

### Local setup instruction (Windows PowerShell)

Set credentials and cost authorization **only in your local environment** — never in Git or reports:

```powershell
# Option A — OpenAI direct
$env:OPENAI_API_KEY = "<operator-supplied-key>"
$env:ORCA_SEMANTIC_MODEL = "gpt-4o-mini"
$env:ORCA_SEMANTIC_PROVIDER = "openai"

# Option B — OpenRouter gateway
$env:OPENROUTER_API_KEY = "<operator-supplied-key>"
$env:ORCA_SEMANTIC_MODEL = "<approved-model-slug-from-openrouter>"
$env:ORCA_SEMANTIC_PROVIDER = "openrouter"

# Cost and live execution gates (required before stages C+)
$env:ORCA_EVAL_LIVE = "1"
$env:ORCA_EVAL_MAX_COST = "10"
$env:ORCA_EVAL_MAX_RECORDS = "665"
$env:ORCA_EVAL_BATCH_SIZE = "25"
$env:ORCA_EVAL_CONCURRENCY = "3"
```

Re-run completion pass after credentials are set. **Do not commit keys.**

---

## 5. Model Selection

**Status:** `BLOCKED — LIVE SEMANTIC MODEL IDENTIFIER REQUIRED`

No provider credentials present; model inventory not queried against live API. Default adapter fallback when configured: `gpt-4o-mini` via `ORCA_SEMANTIC_MODEL`.

| Field | Value |
|-------|-------|
| Provider | NOT SELECTED |
| Model identifier | NOT SELECTED |
| Endpoint class | OpenAI-compatible (`/chat/completions`) when configured |
| Structured output | JSON object (`response_format: json_object`) |
| Context limit | SAFE UNKNOWN until provider+model confirmed |
| Temperature | 0.1 (adapter default) |
| Pricing source | NOT VERIFIED |
| Cost-estimation confidence | LOW — no live pricing probe executed |

---

## 6. Secret and Logging Precheck

**Report:** `projects/orca/semantic-intelligence/live-model/reports/pre-live-security-precheck-v1.json` (checkpointed)

| Check | Status |
|-------|--------|
| Secrets absent from git diff | PASS |
| Secrets absent from generated configs | PASS |
| Logging redaction documented | PASS |
| Raw HTTP headers not persisted | PASS |
| Provider errors sanitized | PASS |
| Blind input separation enforced | PASS |
| Live output directory gitignored | PASS |

**Verdict:** PRE-LIVE SECURITY PRECHECK — PASS (live execution still blocked on missing provider).

---

## 7. Connectivity Smoke (Stage A)

**Status:** NOT EXECUTED — blocked on missing provider.

Expected gate when provider available: one minimal non-client request verifying auth, endpoint, timeout, sanitized errors.

---

## 8. Structured Output Smoke (Stage B)

**Status:** NOT EXECUTED — blocked on Stage A.

Planned: 6–10 controlled records covering provider search, career, education, DIY, product-only, ambiguous problem query. Gate: `STRUCTURED OUTPUT SMOKE — PASS`.

---

## 9. Stratified Live Pilot (Stage C)

**Status:** NOT EXECUTED — blocked on Stages A–B.

Planned: 60–100 stratified records, blind A + reassessment B + hard rules + adjudication + preliminary metrics + error-family report.

---

## 10. Cost Gate

**Status:** `BLOCKED — LIVE EVALUATION COST CAP REQUIRED`

| Control | Status |
|---------|--------|
| `ORCA_EVAL_MAX_COST` | NOT SET |
| `ORCA_EVAL_MAX_RECORDS` | NOT SET |
| `ORCA_EVAL_BATCH_SIZE` | NOT SET (default 25 in code) |
| `ORCA_EVAL_CONCURRENCY` | NOT SET (default 3 in code) |

### Projected costs (estimation only — not live-validated)

Based on `cost-rate-controls.mjs` defaults (800 tokens/phrase × 2 passes, $0.15/M blended):

| Stage | Records | Est. tokens | Est. cost USD | Confidence |
|-------|---------|-------------|---------------|------------|
| Structured smoke | 8 | 12,800 | ~$0.002 | LOW |
| Stratified pilot | 80 | 128,000 | ~$0.019 | LOW |
| Calibration corpus | 202 | 323,200 | ~$0.048 | LOW |
| Holdout (single) | 133 | 212,800 | ~$0.032 | LOW |
| Full non-client corpus | 665 | 1,064,000 | ~$0.160 | LOW |
| Corvonero (2370 phrases, read-only est.) | 2370 | 3,792,000 | ~$0.569 | LOW |

Operator must set `ORCA_EVAL_MAX_COST` per stage before live execution.

---

## 11. Calibration Iterations (Stage D)

**Status:** NOT EXECUTED — blocked.

Prior local **mock** calibration artifacts exist under `live-model/reports/blind-eval-*` — **not live evidence**, not committed.

---

## 12. Calibration D3 Metrics

**Status:** NOT EXECUTED on live provider.

Mock holdout D3 (local, uncommitted, `MOCK_PIPELINE`) showed gates PASS — **explicitly not counted as semantic validation evidence**.

---

## 13. Holdout Integrity

| Check | Status |
|-------|--------|
| Holdout checksum fixed in fixture | PASS — `evaluation-holdout-v1.json` (133 records) |
| Holdout excluded from calibration fixture | PASS — separate file |
| Expected labels excluded from assessor input | PASS — blind separation enforced |
| Evaluation config frozen pre-live | PASS — prompt v1 checkpointed |
| Holdout live run executed | **NOT EXECUTED** — provider blocked |

---

## 14. Final Blind Holdout (Stage E)

**Status:** NOT EXECUTED — blocked on provider and cost authorization.

Holdout must run exactly once when provider is available. Resume of incomplete IDs only if technical failure mid-run.

---

## 15. Live Quality Decision

```text
WAVE 3.1 — BLOCKED
WAVE 3.1 COMPLETION PASS — BLOCKED
REASON: LIVE MODEL PROVIDER OR COST AUTHORIZATION REQUIRED
```

Mock D3 PASS is **not** used as live validation. Wave 3 overall remains **NOT OPERATIONAL**.

---

## 16. Human Review Package

**Status:** NOT GENERATED for live evaluation (no live run).

Conflict-focused package generator exists in `run-blind-evaluation.mjs`. Prior mock packages in local `blind-eval-*` folders are uncommitted and not operator-deliverable as live evidence.

---

## 17. P0-I Comparison

**Status:** NOT EXECUTED on live provider.

Mock local comparison artifacts exist (uncommitted). P0-I deterministic remains reference lane only — not live validation authority.

---

## 18. Non-Client Readiness Run (Stage F)

**Status:** NOT EXECUTED on live provider.

Mock readiness probe (100 phrases, local uncommitted): reconciliation PASS, mode `mock_pipeline`. **Not full-corpus live proof.**

When holdout quality decision is not BLOCKED and cost cap set, run:

```powershell
$env:ORCA_EVAL_LIVE = "1"
node projects/orca/semantic-intelligence/live-model/tests/run-full-corpus-readiness.mjs
```

---

## 19. Corvonero Cost and Readiness Estimate (Read-Only)

**Corvonero status:** FROZEN — no classification attempted.

Based on **2370 reconciled phrases** (read-only audit reference):

| Metric | Estimate range |
|--------|----------------|
| Primary model calls | 2,370 |
| Reassessment calls | 2,370 (same-model independent context path) |
| Adjudication calls | 2,370 (local — no API) |
| Total API calls | ~4,740 |
| Est. tokens | 3.0M – 4.5M |
| Est. cost USD | $0.45 – $1.50 (model-dependent; LOW confidence) |
| Est. runtime | 45 – 90 min at concurrency 3 |
| Batch size | 25 (default) |
| Cache potential | High on re-runs (assessment cache key by phrase+scope+model) |
| Expected review volume | 2 – 8% of phrases (based on mock pipeline ratios) |

**Verdict:** NOT READY — remain FROZEN until Wave 3.1 live D3 operator approval + explicit run authorization.

---

## 20. Live-Path Bypass Re-Audit

**Wave 3.1 bypass audit:** 20/20 PASS (post-checkpoint, adapter path including mock/live resolution)

Critical cases verified:

| # | Case | Result |
|---|------|--------|
| 1 | Expected-label leakage | PASS |
| 2 | Prior-result leakage | PASS |
| 3 | Malformed structured output | PASS |
| 4 | Provider unavailable fallback | PASS |
| 5 | Deterministic preview promoted to production | PASS |
| 6 | Cost cap exceeded | PASS |
| 7 | Partial run marked complete | PASS |
| 8 | Duplicate resume records | PASS |
| 9 | Assessment B sees A | PASS |
| 10 | Holdout reused | PASS |
| 11 | Diagnostic authority contamination | PASS |
| 12 | Full corpus routed to operator | PASS |
| 13 | Outside-scope service hallucination | PASS |
| 14 | D3 PASS claimed on mock | PASS |
| 15 | D3 PASS on insufficient gold support | PASS |

No critical executable bypass open on tested path.

---

## 21. Wave 3 Final Maturity

```text
Wave 3 Core — APPROVED — CHECKPOINTED (2820b9f)
Wave 3.1 Implementation — APPROVED — CHECKPOINTED (7f7cb21)
Wave 3.1 Live Quality — BLOCKED — LIVE MODEL PROVIDER REQUIRED
Wave 3 Overall — NOT OPERATIONAL
Wave 4 — BLOCKED
Corvonero — FROZEN
```

Wave 3 operational self-approval **not** issued.

---

## 22. Wave 4 Readiness

```text
Wave 4 — BLOCKED UNTIL WAVE 3.1 QUALITY REVIEW AND OPERATOR APPROVAL
```

No Wave 4 artifacts started.

---

## 23. Corvonero Boundary

```text
Corvonero — FROZEN
Production semantic run — NOT AUTHORIZED
Semantic Core — NOT CREATED
```

2370-phrase corpus not sent to any model in this task.

---

## 24. Files Created or Changed

### Checkpointed (`7f7cb21`)

| Path | Action |
|------|--------|
| `projects/orca/semantic-intelligence/live-model/**` | Added framework (34 files subset) |
| `projects/mars-search-ppc-production/decisions/WAVE-3.1-OPERATOR-DECISIONS-v1.*` | Added |
| `projects/mars-search-ppc-production/decisions/WAVE-3.1C-COMPLETION-PASS-DECISIONS-v1.*` | Added |
| `projects/mars-search-ppc-production/reports/REPORT-mars-search-ppc-wave3-1-live-semantic-model-validation-v1.md` | Added |
| `projects/mars-search-ppc-production/roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md` | Updated |

### Uncommitted (completion pass — operator review)

| Path | Action |
|------|--------|
| `projects/mars-search-ppc-production/reports/REPORT-mars-search-ppc-wave3-1-live-provider-completion-v1.md` | Created (this report) |
| `projects/orca/semantic-intelligence/live-model/reports/blind-eval-*` | Local mock runs (gitignored) |
| `projects/orca/semantic-intelligence/live-model/reports/holdout-eval-*` | Local mock runs (gitignored) |

---

## 25. Git Status

- **Branch:** `mars/post-cycle8-live-tests`
- **HEAD:** `7f7cb21` (pushed)
- **Wave 3.1 checkpoint:** committed and pushed
- **Completion pass report:** uncommitted (by design)
- **Unrelated WIP:** remains unstaged (localhost, ocpilot, fp-0002, `.recovery-temp/`, etc.)

---

## 26. SAFE UNKNOWN

| Item | Unknown | Would verify |
|------|---------|--------------|
| Live model semantic accuracy | Unknown — no provider | Stages A–E with real credentials |
| OpenRouter model slug for production | Unknown | Operator-approved model list + connectivity smoke |
| gpt-4o-mini structured output reliability on RU queries | Unknown | Stage B smoke |
| Actual token pricing | Unknown | Provider billing API or published rates post-smoke |
| Protected_product / protected_informational gold support | INSUFFICIENT GOLD SUPPORT in holdout fixture (0 records each) | Expand gold corpus before claiming stratum PASS |
| Corvonero exact runtime on operator hardware | Unknown | Authorized scale run |

---

## 27. Operator Approval Items

1. **Supply provider credentials** via environment (`OPENAI_API_KEY` or `OPENROUTER_API_KEY`)
2. **Approve model identifier** (`ORCA_SEMANTIC_MODEL` or `ORCA_LIVE_MODEL`)
3. **Set per-stage cost caps** (`ORCA_EVAL_MAX_COST`)
4. **Authorize live completion pass re-run** (Stages A–F)
5. **Review live D3 holdout results** when available
6. **Approve or reject Wave 3 semantic quality** (does not auto-unblock Wave 4)
7. **Review this completion-pass report** before any commit of live outputs

---

## 28. Recommended Next Action

1. Configure provider environment locally (see §4)
2. Set cost cap: `$env:ORCA_EVAL_MAX_COST = "10"` (adjust per operator budget)
3. Re-run completion pass task or execute staged runners manually:
   - Connectivity: minimal adapter probe
   - `$env:ORCA_EVAL_LIVE = "1"; node projects/orca/semantic-intelligence/live-model/tests/run-blind-evaluation.mjs`
4. Submit holdout D3 results for operator quality review
5. Do **not** unfreeze Corvonero or start Wave 4 until explicit approval

---

## 29. Stop Condition

**Stop reached:**

- Wave 3.1 framework checkpoint committed and pushed (`7f7cb21`)
- Provider environment checked — **NOT SET**
- Live Stages A–E **not executed** (blocked — no mock substitute)
- Pre-live security precheck **PASS**
- Bypass re-audit **20/20 PASS**
- Corvonero read-only cost estimate recorded
- Completion-pass package **uncommitted** for operator review

**Not performed (by design):**

- Live semantic evaluation
- Holdout D3 live decision
- Corvonero classification
- Semantic Core creation
- Wave 4 work
- Mock-as-live evidence claims

**Next gate:**

```text
OPERATOR REVIEW OF MARS SEARCH PPC PRODUCTION WAVE 3.1 LIVE PROVIDER COMPLETION
```

Then: configure credentials + cost cap → re-run live stages → operator quality approval.
