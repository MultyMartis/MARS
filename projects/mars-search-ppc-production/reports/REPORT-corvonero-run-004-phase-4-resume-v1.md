# REPORT — CORVONERO RUN 004 PHASE 4 TRIGGER RECONCILIATION AND RESUME V1

**Run ID:** `corv-semantic-v2-20260626-004`  
**Branch:** `mars/canonical-post-recovery` @ `25f972f93b355d113222e08857837a1f51c14d5b`  
**Task authorization:** Operator Phase 4 trigger reconciliation + safe checkpoint resume  
**Final run state:** `PARTIAL — FAIL-CLOSED` (769 canonical records remain; provider `ENDPOINT_FAILED` on retry batches)

---

## 1. Safety and Authorization

Operator authorized:

- Forensic reconciliation of `CR2-PHR-00253` and `CR2-PHR-00584`
- Classifier and stop-gate repair (support layer only)
- Operator adjudication override for `CR2-PHR-00584`
- Preservation of valid first-720 results
- Safe resume from checkpoint `corv-semantic-v2-20260626-004`
- **Not authorized:** ORCA source changes, corpus changes, Phase 5, strategy, Wave 5

ORCA frozen authority verified on each executor invocation (hashes unchanged). No ORCA production files were modified in this task.

---

## 2. Git Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` |
| HEAD | `25f972f93b355d113222e08857837a1f51c14d5b` |
| Recovery ancestor `ebc65acd` | PASS |
| Unrelated WIP | Present (ORCA/ocpilot/fp-0002); not touched by this task |
| Commit/push | Not performed (per policy) |

---

## 3. Partial Checkpoint Integrity

Initial checkpoint (pre-task):

| Field | Value |
|-------|------|
| `canonical_total` | 2368 |
| `canary_attempt_2_reused` | 120 |
| `production_newly_processed` | 600 |
| `unique_assessed_total` | 720 |
| `missing` | 1648 |
| `complete` | false |
| Duplicate IDs | 0 |
| Orphan IDs | 0 |
| Batch receipts | 6 production + canary reuse audit |
| Schema validity (first 720) | 100% |
| Cumulative cost | ~1.2746 USD |
| Lock | RELEASED |

**Verdict:** `PHASE 4 CHECKPOINT INTEGRITY — PASS` (pre-reconciliation)

---

## 4. Trigger Record Review

### CR2-PHR-00253 — `сколько стоит работа программиста 1с`

| Dimension | Finding |
|-----------|---------|
| Classifier (v2.0.0) | `careers_training_education` + `career` tag (false positive via `работа программиста`) |
| Model path | Primary/reassessment ACCEPT → final ACCEPT |
| Stop-gate | Counted as career ACCEPT #1 |
| Policy expectation | `DIRECT_COMMERCIAL_1C_SERVICE` / ACCEPT |

### CR2-PHR-00584 — `программист 1с стажер аптека плюс самара`

| Dimension | Finding |
|-----------|---------|
| Classifier | `careers_training_education` + `career` (стажер, geography) |
| Model | Primary/reassessment REJECT; final model output ACCEPT |
| Stop-gate | Career ACCEPT #2 → fail-closed |
| Operator decision | Override to REJECT |

---

## 5. CR2-PHR-00253 Decision

```text
policy class: DIRECT_COMMERCIAL_1C_SERVICE
career tag: CLASSIFIER_FALSE_POSITIVE (removed)
final verdict: ACCEPT (unchanged)
operator decision: CONFIRMED
```

Reconciliation removed false `career` classification. Service-price construction (`сколько стоит работа`) no longer triggers employment gate.

---

## 6. CR2-PHR-00584 Decision

```text
policy class: CAREER_EMPLOYMENT
model_verdict: ACCEPT (preserved)
final_authoritative_verdict: REJECT
operator decision: MANUAL ADJUDICATION OVERRIDE
```

Immutable override record: `CORVONERO-RUN-004-PHASE-4-OPERATOR-OVERRIDES-v1.json`

---

## 7. Classifier Root Cause

1. **`работа` ambiguity:** Regex `работа\s+программист` matched genitive `работа программиста` in price queries.
2. **`зарплата` ambiguity:** Bare `зарплат` marker matched payroll-module service queries (`сопровождение 1с зарплата`).
3. **Stop gate:** Raw `career` tag + ACCEPT count ≥ 2 without evidence classification.

---

## 8. Classifier Repair

**File:** `canary-family-classifier-v2.mjs` → `v2.0.1`

- Added `COMMERCIAL_PRICE_WORK`, `PAYROLL_MODULE_SERVICE`, `CAREER_SALARY_MARKER`
- Employment `работа` requires instrumental case (`программистом`) or explicit career markers
- Payroll/service `зарплата` contexts excluded from career
- Evidence precedence: explicit career markers / price constructions > bare tokens

---

## 9. Stop-Gate Repair

**New module:** `career-stop-gate-v1.mjs`

Classifications: `RAW_CLASSIFIER_FLAG`, `CONFIRMED_POLICY_ERROR`, `OPERATOR_REVIEW_REQUIRED`, `CLASSIFIER_FALSE_POSITIVE`, `OPERATOR_OVERRIDE`

Gate fields: `career_accept_raw_count`, `career_accept_confirmed_error_count`, `career_accept_classifier_false_positive_count`, `career_accept_review_pending_count`, `career_accept_override_count`, `career_accept_rate`

Stop fires on ≥2 unresolved confirmed policy errors or systematic confirmed pattern — **not** on classifier false positives or payroll-module phrases.

---

## 10. Focused Regression

```text
run-career-classifier-focused-regression.mjs — PASS (7/7)
run-canary-classifier-v2-regression.mjs — PASS (19/19)
```

---

## 11. Operator Override

`CORVONERO-RUN-004-PHASE-4-OPERATOR-OVERRIDES-v1.json` — status `OPERATOR_ADJUDICATION_OVERRIDE` for `CR2-PHR-00584`. Raw provider output preserved in storage; override applied in reconciled registry/review layers only.

---

## 12. First-720 Metrics Reconciliation

```text
PHASE_4_TRIGGER_RECONCILIATION — PASS

raw career ACCEPT triggers (historical): 2
classifier false positives: 1 (CR2-PHR-00253)
confirmed career false accepts before override: 1 (CR2-PHR-00584)
operator overrides: 1
remaining unresolved career false accepts: 0
```

Receipt: `CORVONERO-RUN-004-PHASE-4-TRIGGER-RECONCILIATION-v1.json`

Additional review item (not a trigger): `CR2-PHR-00559` (assessment consensus REJECT vs final ACCEPT).

---

## 13. Resume Cost Projection

| Metric | Value |
|--------|------|
| Cumulative at reconciliation | 1.2746 USD |
| Hard cap | 3.00 USD |
| Actual cost per new record (Phase 4) | ~0.000696 USD |
| Projected total (2368) | ~2.42 USD |
| **Projection verdict** | PASS (under cap) |

---

## 14. Resume Lock

Resume lock acquisitions recorded with `resume_from_unique_assessed` / `remaining_at_resume`. All locks released after each partial/fail-closed segment. No conflicting live lock at report time.

---

## 15. Resume Checkpoint

| Resume point | Unique assessed | Batches | Notes |
|--------------|----------------:|--------:|-------|
| Post-reconciliation | 720 | 6 | Trigger reconciliation PASS |
| After batch 007 | 820 | 7 | Career gate repair validated |
| After batch 023 | 1601 | 23 | Gate C2 passed |
| Final | 1599 | 31 | 769 missing; ENDPOINT_FAILED on batches 024–031 |

Cost-tracker resume bug (token recalculation dropping baseline) **repaired** in executor (`phase4_baseline_usd` + incremental tracking).

---

## 16. Remaining Batch Execution

Resume processed batches 007–023 successfully (~881 new valid records). Batches 024–031 attempted remaining 769 IDs; **all records returned `ENDPOINT_FAILED`** (0 schema-valid). No silent provider/model drift; failures are adapter-level endpoint errors.

---

## 17. Gate C2

**Gate C2 @ 1200 unique assessed — PASS**

Receipt: `gate-c2-receipt-v1.json`  
Career metrics at gate: no stop-required issues under repaired evidence gate.

---

## 18. Gate C3

**Gate C3 @ 2000 — NOT REACHED** (execution halted at 1599 assessed before threshold).

---

## 19. Career Review

Monitored patterns active during resume. Immediate review list maintained in storage (`career-immediate-review-v1.json`). Items include `CR2-PHR-00559` and career-tagged ACCEPTs flagged `OPERATOR_REVIEW_REQUIRED` without auto-override.

---

## 20. Other Error Families

| Family | Status |
|--------|--------|
| Informational systematic ACCEPT | Not triggered |
| Incompatible platform ACCEPT | Not triggered |
| Generic ERP systematic | Not triggered |
| Schema failure spike | Not triggered (isolated malformed/quarantine) |
| `ENDPOINT_FAILED` (batches 024–031) | **ACTIVE — blocks completion** |
| Cost cap | Not exceeded (1.9159 USD) |

---

## 21. Verdict Distribution (1599 assessed, authoritative)

| Verdict | Count (approx.) |
|---------|----------------:|
| ACCEPT | ~380 |
| REJECT | ~1180 |
| ABSTAIN | ~39 |

(Exact counts in `CORVONERO-RUN-004-PHASE-4-FULL-CORPUS-RESULT-v2.json`)

---

## 22. Structured Output

- Malformed retry policy unchanged; 2 transient quarantines cleared for retry (`CR2-PHR-00799`, `CR2-PHR-00935`, `CR2-PHR-01119`)
- Batches 024–031: 100% `ENDPOINT_FAILED`, 0 schema-valid

---

## 23. Retry and Malformed Output

| Metric | Value |
|--------|------|
| Retries (cumulative) | 27+ |
| Malformed first-attempt | low single digits |
| Quarantine (final) | 0 in registry |
| Failed-not-in-registry | ~769 (endpoint failures) |

---

## 24. Cost and Runtime

| Metric | Value |
|--------|------|
| Cumulative cost | **1.9159 USD** |
| Hard cap | 3.00 USD |
| Phase 4 wall time (resume sessions) | ~3.5 h aggregate |
| Cost basis | Incremental token tracking post-fix |

---

## 25. Final Reconciliation

```text
canonical_total: 2368
unique_assessed: 1599
missing: 769
duplicates: 0
orphans: 0
quarantined_unresolved: 0
complete: false
```

**Identity equation (partial):**

```text
2368 ≠ 120 + 1479 + 769 (769 not successfully assessed)
```

**Verdict:** `FINAL RECONCILIATION — FAIL` (incomplete corpus)

---

## 26. Operator Overrides

| ID | Model | Authoritative | Status |
|----|-------|---------------|--------|
| CR2-PHR-00584 | ACCEPT | REJECT | OPERATOR_ADJUDICATION_OVERRIDE |

---

## 27. Full Semantic Registries

- Checkpoint registry: `STORAGE/.../checkpoints/phase4-semantic-registry-v1.json` (1599 records)
- Pilot v2 summary: `CORVONERO-RUN-004-PHASE-4-FULL-CORPUS-RESULT-v2.json`
- Accept/reject/abstain registries in STORAGE `reports/` (partial, pre-finalize)

---

## 28. Review Queue

`CORVONERO-RUN-004-PHASE-4-REVIEW-QUEUE-v2.json` — **320 items**  
Mandatory: `CR2-PHR-00200`, `CR2-PHR-00584`

---

## 29. Phase 4 Verdict

```text
PHASE 4:
PARTIAL — FAIL-CLOSED

Run 004:
BLOCKED_AT_PHASE_4

Reason:
ENDPOINT_FAILED on remaining 769 canonical IDs (batches 024–031)

Trigger reconciliation:
PASS

Full corpus:
1599 / 2368
```

---

## 30. Project Lifecycle

```text
Project: BLOCKED_AT_PHASE_4 (not FROZEN_PENDING_SEMANTIC_REVIEW — corpus incomplete)
Strategy: NOT STARTED
Wave 5: BLOCKED
```

---

## 31. Runtime Cleanup

- Phase 4 lock: RELEASED
- No active executor process at report time
- Checkpoint preserved with `stop_reason: INCOMPLETE — 1599/2368 assessed`

---

## 32. Outputs Created

| Output |
|--------|
| `CORVONERO-RUN-004-PHASE-4-TRIGGER-RECONCILIATION-v1.md/.json` |
| `CORVONERO-RUN-004-PHASE-4-OPERATOR-OVERRIDES-v1.json` |
| `CORVONERO-RUN-004-PHASE-4-FULL-CORPUS-RESULT-v2.md/.json` |
| `CORVONERO-RUN-004-PHASE-4-REVIEW-QUEUE-v2.json` |
| `CORVONERO-RUN-004-PHASE-4-REVIEW-PACKAGE-v2.md/.json` |
| `CORVONERO-RUN-004-PHASE-5-NEXT-TASK-v2.md` |
| `REPORT-corvonero-run-004-phase-4-resume-v1.md` (this file) |

Original partial report `REPORT-corvonero-run-004-phase-4-full-corpus-v1.md` preserved.

---

## 33. Files Changed

**Support layer (this task):**

- `pilots/corvonero/tools/canary-family-classifier-v2.mjs`
- `pilots/corvonero/tools/career-stop-gate-v1.mjs` (new)
- `pilots/corvonero/tools/run-career-classifier-focused-regression.mjs` (new)
- `pilots/corvonero/tools/reconcile-run-004-phase4-triggers-v1.mjs` (new)
- `pilots/corvonero/tools/execute-run-004-phase4-full-corpus-v1.mjs`
- `pilots/corvonero/tools/finalize-run-004-phase4-full-corpus-v2.mjs` (new)
- `pilots/corvonero/tools/repair-run-004-phase4-checkpoint-cost-v1.mjs` (new)
- Pilot v1/v2 artifacts under `pilots/corvonero/`
- STORAGE checkpoints, batches 007–031, receipts

**Not modified:** ORCA production source, canonical corpus, `projects/projects/`

---

## 34. Git Status

Branch `mars/canonical-post-recovery`; no commit. Corvonero pilot tree largely untracked under `projects/mars-search-ppc-production/pilots/`. Unrelated ORCA WIP modifications pre-exist in working tree.

---

## 35. SAFE UNKNOWN

- Exact OpenRouter billed USD vs calculated token cost — verify against provider dashboard
- Root cause of `ENDPOINT_FAILED` burst (rate limit vs key quota vs transient outage) — requires provider-side logs
- Whether failed 769 IDs would succeed on immediate re-run without operator intervention

---

## 36. Operator Decisions Required

1. **Diagnose `ENDPOINT_FAILED`** for batches 024–031 before next resume.
2. **Authorize re-resume** of remaining 769 IDs (cost headroom ~1.08 USD under 3.00 cap).
3. **Review** `CORVONERO-RUN-004-PHASE-4-REVIEW-QUEUE-v2` (320 items) including `CR2-PHR-00559`.
4. **Do not** authorize Phase 5 until `2368/2368` reconciliation PASS.

---

## 37. Exact Phase 5 Task

```text
BLOCKED until Phase 4 completes 2368/2368

Next gate after completion:
OPERATOR REVIEW OF CORVONERO RUN 004 COMPLETED PHASE 4

See: CORVONERO-RUN-004-PHASE-5-NEXT-TASK-v2.md
```

---

## 38. Stop Condition

**Stop condition met:** Phase 4 partial fail-closed; trigger reconciliation and classifier repair complete; resume advanced corpus to 1599/2368; remaining 769 blocked by `ENDPOINT_FAILED`.

```text
Do not proceed to Phase 5, strategy, Wave 5, Commander, import, or launch.

Next operator gate:
RESUME AUTHORIZATION — CORVONERO RUN 004 PHASE 4 REMAINING 769 IDS
```

**Recovery command (after operator authorization + endpoint fix):**

```bash
node projects/mars-search-ppc-production/pilots/corvonero/tools/execute-run-004-phase4-full-corpus-v1.mjs
```
