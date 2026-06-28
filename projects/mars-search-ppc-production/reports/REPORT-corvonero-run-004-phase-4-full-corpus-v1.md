# REPORT — CORVONERO RUN 004 PHASE 4 FULL CORPUS V1

## 1. Safety and Authorization

Operator authorized **Phase 4 controlled full-corpus semantic execution** for Run `corv-semantic-v2-20260626-004` after Phase 3 Canary Attempt 2 PASS. SPPC-05 and ORCA frozen authority preserved. Strategy, Wave 5, Campaign Architecture, Commander, import, and launch remain **BLOCKED**.

**Outcome:** **PARTIAL — FAIL-CLOSED** at 720/2368 assessed records. Not full corpus completion.

## 2. Git Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` |
| HEAD | `f9494570` (descends from recovery authority `ebc65acd`) |
| Recovery ancestry | PASS |
| Phase 3 Attempt 2 PASS authority | Present |
| ORCA on-disk hashes | PASS (match approved freeze) |
| Unrelated WIP | Not altered |

Note: ORCA files show working-tree modifications in `git status`, but SHA-256 verification against approved freeze **passed** at execution time.

## 3. Run 004 Authority

| Field | Value |
|-------|-------|
| Run ID | `corv-semantic-v2-20260626-004` |
| Pre-execution lifecycle | `PHASE_3_COMPLETE` |
| Phase 4 authorization | Operator-approved in task charter |
| Runs 002/003 | Immutable, non-resumable |
| Attempt 1 canary | Immutable failed evidence — not production authority |

## 4. ORCA Authority

Frozen components verified (no drift):

| Component | Version | Hash prefix |
|-----------|---------|-------------|
| semantic-adjudicator.mjs | v1.5 | `9618364947BA812C` |
| platform-compatibility.mjs | v1.1 | `49B8C4D604EE732F` |
| hard-rules.mjs | v1.2 | `E6CD74CCCA6ED453` |
| prompt-contract.mjs | v1.4 | `481075E55A827404` |
| service-intent-evidence.mjs | v1.1 | `5BFFF7AE2ED3B854` |

ORCA production source **not modified** during Phase 4.

## 5. Input Authority

| Input | Value |
|-------|-------|
| Project | PRJ-0013 |
| MIG session | session-mig-20260622-corv01 |
| Canonical corpus | 2368 records |
| Corpus SHA-256 prefix | `eaa09b8450f82738` |
| Stable IDs | CR2-PHR-* |
| Canonical input | Not rewritten |

## 6. Cost Projection

Pre-execution projection (2248 remaining after 120 canary reuse):

| Item | USD |
|------|-----|
| Cumulative before Phase 4 | 0.8568 |
| Projected Phase 4 (2248 × ~2503/575 tokens) | ~1.62 |
| Projected total | ~2.48 |
| Hard cap | 3.00 |
| Pre-flight projection | **PASS** |

Actual at stop: **1.2746 USD** (soft warning 2.00 not reached).

## 7. Canary Attempt 2 Reuse Audit

Audit file: `CORVONERO-RUN-004-PHASE-4-CANARY-REUSE-AUDIT-v1.json`

| Metric | Value |
|--------|------:|
| Attempt 2 records | 120 |
| Reusable (PRODUCTION_ELIGIBLE) | **120** |
| Reprocess required | 0 |
| Receipt trace | Batch results + canary result v2 (117 lacked per-ID raw files; batch receipt trace accepted) |

Initial audit bug (raw-file-only check) was corrected before production run; all 120 registered as reusable.

## 8. Residual Review Queue

Review queue: `CORVONERO-RUN-004-PHASE-4-REVIEW-QUEUE-v1.json` — **72 items**

Mandatory items preserved:

- **CR2-PHR-00200** — classifier/policy vs model disagreement (canary residual)
- **CR2-PHR-00253**, **CR2-PHR-00584** — career-tagged ACCEPT (fail-closed triggers)
- PSR-AMB-01 / generic ERP / DIY ambiguity / primary-reassessment disagreement subsets

## 9. Phase Transition

Lifecycle transitions executed:

```text
PHASE_3_COMPLETE
→ PHASE_4_FULL_CORPUS_AUTHORIZED
→ PHASE_4_FULL_CORPUS_EXECUTING
→ BLOCKED_AT_PHASE_4 (fail-closed)
```

Authorization receipt: `STORAGE/.../receipts/phase-4-full-corpus-authorization-v1.json`

## 10. Production Lock

| Field | Value |
|-------|-------|
| Lock file | `run-phase4.lock.json` (STORAGE) |
| Phase | PHASE_4_FULL_CORPUS |
| Status | **RELEASED** |
| Release outcome | `PARTIAL — FAIL-CLOSED — career_education_acceptance_family` |
| Owner | Single PID, atomic acquire/release |

## 11. Production Checkpoint

Checkpoint: `STORAGE/.../checkpoints/checkpoint-phase4-v1.json`

| Counter | Value |
|---------|------:|
| canonical_total | 2368 |
| canary_attempt_2_reused | 120 |
| production_newly_processed | 600 |
| unique_assessed_total | 720 |
| missing | 1648 |
| complete | false |

## 12. Execution Plan

| Parameter | Value |
|-----------|-------|
| Remaining after reuse | 2248 |
| Batch size | 100 |
| Planned batches | ~23 |
| Completed before stop | **6** |
| Pipeline | Wave 3.1F (primary → reassessment → evidence → platform → hard rules → adjudication) |

## 13. Batch Execution

| Batch | Status |
|-------|--------|
| phase4-batch-001 … 006 | Complete |
| phase4-batch-007+ | Not started (stopped after batch 6 record processing triggered fail-closed) |

600 new production records + 120 canary reuse = 720 total assessed.

## 14. Mid-Run Gate C1

Gate receipt: `gate-c1-receipt-v1.json` at **503 unique assessed**

| Metric | Value |
|--------|------:|
| ACCEPT | 144 |
| REJECT | 347 |
| ABSTAIN | 12 |
| Schema valid rate | 100% |
| Gate stop | **No** (issues array empty at C1) |

Fail-closed fired later at 720 assessed via cumulative `checkStopConditions`.

## 15. Mid-Run Gate C2

**Not reached** (stop at 720 < 1200 threshold).

## 16. Mid-Run Gate C3

**Not reached** (stop at 720 < 2000 threshold).

## 17. Verdict Distribution

Partial corpus (720 records):

| Verdict | Count | % |
|---------|------:|--:|
| ACCEPT | 249 | 34.6% |
| REJECT | 433 | 60.1% |
| ABSTAIN | 38 | 5.3% |

## 18. Structured Output

| Metric | Value |
|--------|------:|
| Schema valid (assessed set) | 100% |
| Malformed first attempt | 0 |
| Quarantined | 0 |
| Structured-output failure spike | **No** |

## 19. Retry and Malformed Output

Malformed retry policy active; **zero** malformed/quarantine events in partial run.

## 20. Direct Commercial Demand

`direct_commercial_1c_service` (51 in partial set): **48 ACCEPT**, 2 REJECT, 1 ABSTAIN. No systematic rejection signal.

## 21. Career and Education

`careers_training_education` (168 in partial set): **166 REJECT**, **2 ACCEPT**.

Fail-closed triggers:

- `CR2-PHR-00253` — «сколько стоит работа программиста 1с»
- `CR2-PHR-00584` — «программист 1с стажер аптека плюс самара`

Threshold: ≥2 career/education ACCEPT → **stop** (per harness policy copied from canary gates).

## 22. Informational and Self-Service

23 records — **23/23 REJECT**. No informational acceptance family signal.

## 23. Problems and DIY Intent

15 problem/troubleshooting — 1 REJECT, 14 ABSTAIN. Conservative pattern preserved.

## 24. Platform Compatibility

No foreign/incompatible platform ACCEPT detected in partial set.

## 25. Product and License

No `product_license_version` family hits in partial 720 set at classifier layer.

## 26. Product-Plus-Service Ambiguity

PSR-AMB-01 family: **0** records in partial assessed set. Monitored; no false-accept family signal.

## 27. Integrations

13 records — 6 ACCEPT, 3 REJECT, 4 ABSTAIN.

## 28. Marking and Честный знак

10 records — 3 ACCEPT, 5 REJECT, 2 ABSTAIN.

## 29. TS ПИОТ

5 records — 1 ACCEPT, 2 REJECT, 2 ABSTAIN.

## 30. Geography

8 records — 8 ACCEPT (geo-modified commercial queries in partial slice).

## 31. Error-Family Analysis

| Family | Count |
|--------|------:|
| MALFORMED_MODEL_OUTPUT | 0 |
| QUARANTINED | 0 |
| Fail-closed stop | 1 (`career_education_acceptance_family`) |

Report: `STORAGE/.../reports/error-family-report-v1.json`

## 32. Cost and Runtime

| Item | Value |
|------|-------|
| Phase 4 execution runtime | ~91 min (09:43–11:15 UTC) |
| Cumulative before Phase 4 | 0.8568 USD |
| Phase 4 spend | 0.4178 USD |
| **Total cumulative** | **1.2746 USD** |
| Hard cap headroom | 1.7254 USD |

## 33. Final Reconciliation

**FAILED — partial run**

| Check | Expected | Actual |
|-------|----------|--------|
| Canonical total | 2368 | 2368 |
| Unique assessed | 2368 | **720** |
| Missing | 0 | **1648** |
| Duplicates | 0 | 0 |
| Quarantined unresolved | 0 | 0 |
| Full production complete | true | **false** |

```text
BLOCKED — FINAL SEMANTIC RECONCILIATION FAILED (partial)
```

## 34. Full Semantic Registries

Partial registries written to STORAGE:

- `full-semantic-registry-v1.json` (720 records)
- `accept-registry-v1.json` (249)
- `reject-registry-v1.json` (433)
- `abstain-registry-v1.json` (38)

Git summary: `CORVONERO-RUN-004-PHASE-4-FULL-CORPUS-RESULT-v1.{json,md}`

## 35. Review Queue

72 items — includes CR2-PHR-00200, stop-trigger career ACCEPTs, disagreement subset.

## 36. Phase 4 Verdict

```text
PHASE 4: PARTIAL — FAIL-CLOSED
Run 004: BLOCKED_AT_PHASE_4
Stop: career_education_acceptance_family
```

Not `PASS — OPERATOR REVIEW REQUIRED` for full corpus.

## 37. Project Lifecycle

```text
Project: FROZEN (partial Phase 4 — not FROZEN_PENDING_SEMANTIC_REVIEW)
Strategy: not started
Wave 5: BLOCKED
```

Full success lifecycle state **not** reached.

## 38. Runtime Cleanup

- Production lock **released** with partial failure receipt
- Checkpoint preserved (resumable)
- Registry preserved (720 records)
- Completed batches preserved (001–006)
- No auto-restart

## 39. Outputs Created

**Git (pilots/corvonero/):**

- `CORVONERO-RUN-004-PHASE-4-CANARY-REUSE-AUDIT-v1.json`
- `CORVONERO-RUN-004-PHASE-4-FULL-CORPUS-RESULT-v1.{json,md}`
- `CORVONERO-RUN-004-PHASE-4-REVIEW-QUEUE-v1.json`
- `CORVONERO-RUN-004-PHASE-4-REVIEW-PACKAGE-v1.{json,md}`
- `CORVONERO-RUN-004-PHASE-5-NEXT-TASK-v1.md`
- `tools/execute-run-004-phase4-full-corpus-v1.mjs`
- `tools/finalize-run-004-phase4-full-corpus-v1.mjs`
- `runs/corv-semantic-v2-20260626-004/sanitized-phase4-authorization-receipt-v1.json`
- `runs/corv-semantic-v2-20260626-004/lifecycle-decision-v1.json` (updated)

**Git (reports/):**

- `REPORT-corvonero-run-004-phase-4-full-corpus-v1.md` (this file)

**STORAGE:** checkpoints, batches 001–006, raw-responses/phase4, receipts, partial registries.

## 40. Git and STORAGE Placement

| Layer | Location |
|-------|----------|
| Sanitized Git artefacts | `projects/mars-search-ppc-production/pilots/corvonero/` |
| Report | `projects/mars-search-ppc-production/reports/` |
| Mutable runtime | `C:\MARS Phenix\AI MARS STORAGE\mig\corvonero\semantic-runs\corv-semantic-v2-20260626-004\` |

Lock/checkpoint/raw responses **not** in Git (per policy).

## 41. Tests

| Test | Result |
|------|--------|
| ORCA hash preflight | PASS |
| Corpus count/hash | PASS |
| Canary reuse audit (corrected) | 120/120 PASS |
| Cost pre-projection | PASS |
| Phase 4 harness fail-closed | **TRIGGERED** (career ACCEPT ≥2) |
| Full reconciliation | **FAIL** (partial) |

## 42. Files Changed

Created/modified by this task (Corvonero Phase 4 scope):

- `pilots/corvonero/tools/execute-run-004-phase4-full-corpus-v1.mjs` (new)
- `pilots/corvonero/tools/finalize-run-004-phase4-full-corpus-v1.mjs` (new)
- All Phase 4 Git artefacts listed in §39
- STORAGE runtime artefacts (batches, checkpoint, registry, receipts)

ORCA source, canonical corpus, MIG source, Runs 002/003 — **untouched**.

## 43. Git Status

Branch `mars/canonical-post-recovery`. New untracked Corvonero pilot/report files under `projects/mars-search-ppc-production/`. Unrelated WIP (FP-0002, ORCA working tree) unchanged by this task. **No commit** (per task policy).

## 44. SAFE UNKNOWN

- Whether the two career ACCEPT triggers represent systematic policy failure vs edge-case review items at full-corpus scale — **operator judgment required**
- Exact OpenRouter billed amount vs calculated token cost — verify against provider dashboard
- Optimal fail-closed threshold at full-corpus scale (absolute count vs rate) — not specified beyond canary-parity harness

## 45. Operator Decisions Required

1. **Review fail-closed triggers** CR2-PHR-00253 and CR2-PHR-00584 — confirm REJECT override or accept as review-queue-only.
2. **Authorize resume** from checkpoint (`1648` remaining) with one of:
   - Operator-signed threshold adjustment (rate-based stop for career/education at full corpus), or
   - Manual verdict correction for trigger IDs then resume unchanged harness.
3. **Disposition CR2-PHR-00200** and PSR-AMB-01 monitored items in review queue.
4. **Do not** authorize strategy/Wave 5 until full 2368 reconciliation PASS.

## 46. Exact Phase 5 Task

Phase 5 **blocked** until full Phase 4 PASS. If operator authorizes resume and full corpus completes:

```text
OPERATOR REVIEW OF CORVONERO RUN 004 PHASE 4 RESULT
→ Phase 5 semantic review/assembly (separate authorization)
→ CORVONERO-RUN-004-PHASE-5-NEXT-TASK-v1.md
```

Strategy and Campaign Architecture remain **NOT AUTHORIZED**.

## 47. Stop Condition

**Stop condition met:** Phase 4 fail-closed partial result.

```text
Next gate: OPERATOR REVIEW OF CORVONERO RUN 004 PHASE 4 PARTIAL RESULT
Do not proceed to Phase 5, strategy, Wave 5, Commander, import, or launch.
```

**Recovery command (after operator authorization only):**

```bash
node projects/mars-search-ppc-production/pilots/corvonero/tools/execute-run-004-phase4-full-corpus-v1.mjs
```

Harness resumes from `checkpoint-phase4-v1.json` / `phase4-semantic-registry-v1.json` when lock is free.
