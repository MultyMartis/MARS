# REPORT — CORVONERO NEW CONTROLLED SEMANTIC RUN PHASE 0/1/2 V1

**Date:** 2026-06-26  
**Run ID:** `corv-semantic-v2-20260626-002`  
**Branch:** `mars/canonical-post-recovery` @ `ebc65acd4087fa9d180bb2a50921027fde51e3b7`

---

## 1. Safety and Authorization

Operator charter `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-OPERATOR-CHARTER-v1` approved for **Phase 0/1/2 only**. Gate A: **APPROVED**. Phases 3+ (canary, production batches, Wave 5) **not authorized**. Task scope limited to authority freeze, new run registration, and closed-dataset SPPC-05.

---

## 2. Git Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` ✓ |
| HEAD | `ebc65acd4087fa9d180bb2a50921027fde51e3b7` ✓ |
| Recovery anchor | `fe9d9c8e52edd2632de15dcc5ee5d353d8660362` ✓ |
| Preflight/charter docs | Present under `pilots/corvonero/` ✓ |
| Unrelated WIP | Untouched (not staged) ✓ |
| Prior new-run dir | None before execution; `001` and `002` created this task |

---

## 3. Charter Approval

Charter status updated: **APPROVED FOR PHASE 0/1/2**. Operator decisions recorded: provider `openrouter`, model `openai/gpt-5-mini`, hard cap `$3.00`, soft warning `$2.00`, old-run resume prohibited, forensic cache prohibited, TS PIOT SERP non-blocking, Wave 5 blocked.

---

## 4. New Run Identity

| Field | Value |
|-------|-------|
| Run ID | `corv-semantic-v2-20260626-002` |
| Project | PRJ-0013 |
| MIG session | session-mig-20260622-corv01 |
| Corpus | corvonero-canonical-phrase-registry-v1 |
| Count | 2368 |
| SHA-256 | eaa09b8450f8273890676c1ac2746172fac3cd884a4ee9697a8076593355b4fc |
| ORCA wave | 3.1F |
| Provider / model | openrouter / openai/gpt-5-mini |

Abandoned attempt: `corv-semantic-v2-20260626-001` (orchestrator isolation false-positive; not authoritative).

---

## 5. STORAGE Root

```text
C:\MARS Phenix\AI MARS STORAGE\mig\corvonero\semantic-runs\corv-semantic-v2-20260626-002\
```

Subdirs created: manifests, runtime, checkpoints, locks, batches, cache, raw-responses, receipts, reports, quarantine. Inside canonical STORAGE; not old forensic location; no old files copied.

---

## 6. Immutable Input Registration

Run-local input reference manifest written with source path, corpus ID, count 2368, full SHA-256, read-only authority, lineage 2399→31 clusters→2368. Corpus **not** rewritten.

---

## 7. Dataset Verification

| Check | Result |
|-------|--------|
| Row count | 2368 ✓ |
| Duplicate IDs | 0 ✓ |
| Missing IDs | 0 ✓ |
| Hash prefix | eaa09b8450f82738 ✓ |
| Lineage evidence | Present ✓ |

---

## 8. Old Run Isolation

Verdict: **OLD_RUN_ISOLATION — PASS**. No old run ID, checkpoint, lock, cache, or forensic artefact paths in new runtime dirs. Old run `corvonero-direct-v2-clean-room-v1-diagnostic` remains non-resumable.

---

## 9. ORCA Wave 3.1F Authority

| File | SHA-256 prefix |
|------|----------------|
| semantic-adjudicator.mjs | 4e197d816cfd1389 |
| prompt-contract.mjs | 0fbe20bfef33d2e6 |
| hard-rules.mjs | aed6d1078aa87833 |

Prompt v1.3 · Adjudicator v1.3 verified.

---

## 10. Model and Provider

| Field | Value |
|-------|-------|
| Provider | openrouter |
| Model | openai/gpt-5-mini |
| Secret source | `.secrets/orca-live-model.env` |
| Secret status | SET (values not logged) |
| Fallback gpt-4o-mini | NOT used |

---

## 11. Cost Projection

Pre-execution estimate: ~472 live records, ~944 model calls, ~$0.23 USD. SPPC-05 allocation bounded at $1.00 within $3.00 hard cap. Actual cumulative ~$0.80 USD — **in bounds**.

---

## 12. Lock Authority

Atomic lock acquired at `locks/run.lock.json`; released with failure receipt after SPPC-05 fail-closed. Stale lock from incomplete orchestrator run released on finalize.

---

## 13. Checkpoint Authority

Initial checkpoint: processed 0 / total 2368, phase SPPC-05_VALIDATION. Final checkpoint: `BLOCKED_AT_SPPC_05`, cumulative cost recorded. Atomic write via temp+rename.

---

## 14. Closed Dataset Inventory

| Dataset | Count | Authority |
|---------|-------|-----------|
| protected_product_confirmation | 106 | confirmation/strata |
| geo_commercial_confirmation_v2 | 120 | confirmation/strata |
| protected_product supplementary | 70 | supplementary/strata |
| protected_informational | 66 | supplementary/strata |
| problem query policy | 10 | inline fixtures |
| under-admission unit | 16 | regression JSON |
| Wave 3.1F bypass | 12 | static audit |

Old Corvonero cache **not** used as fixture truth.

---

## 15. SPPC-05 Criteria

Canonical threshold: adversarial FPR ≤ 0.01 (`run-confirmation-validation.mjs`). Geo recall ≥ 0.90, adversarial geo FPR ≤ 0.01. Problem query 10/10. Closed regression product FPR ≤ 0.01.

---

## 16. SPPC-05 Execution

Executed via canonical Wave 3.1F test runners with explicit openrouter / openai/gpt-5-mini. No 2368 corpus. No canary. No production batches.

---

## 17. Quality Metrics

| Suite | Pass | Key metric |
|-------|------|------------|
| Wave 3.1F bypass | ✓ | 12/12 |
| Under-admission | ✓ | 16/16 |
| Closed regression | ✓ | product FPR 0 |
| Geo confirmation v2 | ✓ | adv FPR 0, recall 1.0 |
| Product confirmation | ✗ | FPR 0.0125 |
| Problem query | ✗ | 9/10 |

---

## 18. Error Families

- **Product false accept:** SAP Business One update classified ACCEPT (service vs product boundary).
- **Problem query:** DIY-framed error code REJECT instead of ABSTAIN.

No structured-output parse failures observed in summarized runs.

---

## 19. Bypass Audit

Wave 3.1F bypass audit: **12/12 PASS** — no phrase-specific exceptions, holdout checksum unchanged, commercial intent separated from scope fit.

---

## 20. Cost and Runtime

| Metric | Value |
|--------|-------|
| Closed regression | $0.28 · ~105 min |
| Product confirmation | $0.22 · ~62 min |
| Geo confirmation v2 | $0.24 · ~61 min |
| Problem query | ~$0.05 · ~2.5 min |
| **Total** | **~$0.80 USD** |

Under hard cap $3.00; below soft warning $2.00 for individual suites; cumulative under soft warning.

---

## 21. Gate B Verdict

```text
SPPC-05: FAILED
Project: BLOCKED_AT_SPPC_05
```

Critical criteria not met (product FPR, problem query).

---

## 22. Project Lifecycle State

```text
BLOCKED_AT_SPPC_05
```

Not `FROZEN_PENDING_CANARY_AUTHORIZATION`. Full corpus not started.

---

## 23. Runtime Cleanup

Lock **RELEASED** with failure receipt. Checkpoint and SPPC-05 evidence preserved in STORAGE. No active owner PID.

---

## 24. Outputs Created

**Git (pilots/corvonero/):**

- Updated charter MD/JSON
- CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-0-1-2-RESULT-v1.md/json
- CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-SPPC-05-REVIEW-PACKAGE-v1.md/json
- CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-3-NEXT-TASK-v1.md
- Updated INPUT-MANIFEST status

**Git (runs/corv-semantic-v2-20260626-002/):**

- run-manifest-v1.json
- immutable-input-reference-v1.json
- sanitized-execution-receipt-v1.json
- reports/sppc-05-sanitized-report-v1.json
- lifecycle-decision-v1.json

**STORAGE:** manifests, checkpoints, receipts, SPPC-05 report (raw ORCA reports remain under live-model/reports/).

---

## 25. Git and STORAGE Placement

Git: sanitized authority + reports only. STORAGE: mutable lock (released), checkpoints, cost projection, execution receipts. Secrets never in Git.

---

## 26. Tests

| Test | Result |
|------|--------|
| Input hash | PASS |
| Record count 2368 | PASS |
| ID uniqueness | PASS |
| Lineage | PASS |
| Old-run isolation | PASS |
| Forensic cache exclusion | PASS |
| Lock atomicity | PASS (002) |
| Checkpoint atomicity | PASS |
| Product/service regression (closed) | PASS |
| Problem-query regression | **FAIL 9/10** |
| Under-admission | PASS |
| Wave 3.1F bypass | PASS |
| Confirmation product FPR | **FAIL** |
| Confirmation geo v2 | PASS |
| Cost cap | PASS |
| No full corpus | PASS |
| No Wave 5 | PASS |

---

## 27. Files Changed

- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-OPERATOR-CHARTER-v1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-OPERATOR-CHARTER-v1.json`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-INPUT-MANIFEST-v1.json`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-0-1-2-RESULT-v1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-0-1-2-RESULT-v1.json`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-SPPC-05-REVIEW-PACKAGE-v1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-SPPC-05-REVIEW-PACKAGE-v1.json`
- `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-3-NEXT-TASK-v1.md`
- `projects/mars-search-ppc-production/pilots/corvonero/tools/execute-phase-0-1-2-v1.mjs` (new)
- `projects/mars-search-ppc-production/pilots/corvonero/tools/finalize-phase-0-1-2-v1.mjs` (new)
- `projects/mars-search-ppc-production/pilots/corvonero/runs/corv-semantic-v2-20260626-002/*` (new)
- `projects/mars-search-ppc-production/reports/REPORT-corvonero-new-controlled-semantic-run-phase-0-1-2-v1.md` (this file)

---

## 28. Git Status

Changes **uncommitted** per git policy. Unrelated WIP not staged.

---

## 29. SAFE UNKNOWN

- Exact OpenRouter billing line-item for this run (estimated from token pricing in test scripts).
- Whether SAP Business One update false accept reproduces on re-run (single-record variance unknown).
- Retention policy for raw provider responses in STORAGE (operator decision still pending per charter §20).

---

## 30. Operator Decisions Required

1. Review SPPC-05 failure evidence (product FPR, problem query).
2. Authorize ORCA repair task or accept fail-closed stop.
3. Decide if new run ID required after brain repair.
4. **Do not** authorize Phase 3 canary until Gate B pass.

---

## 31. Exact Phase 3 Task

See `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-3-NEXT-TASK-v1.md` — **currently BLOCKED** pending SPPC-05 pass.

---

## 32. Stop Condition

**STOPPED — FAIL**

```text
SPPC-05: FAILED
Project: BLOCKED_AT_SPPC_05
```

Next gate: **OPERATOR REVIEW OF CORVONERO NEW CONTROLLED RUN SPPC-05 RESULT**

Did not continue to: Phase 3 canary, full corpus, semantic assembly, strategy, Campaign Architecture, Commander, import, launch, Wave 5.
