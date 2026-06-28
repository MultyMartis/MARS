# REPORT — CORVONERO RUN 004 PHASE 3 CONTROLLED CANARY V1

## 1. Safety and Authorization

Operator authorized **Phase 3 controlled canary only** (120 phrases). Gate B **APPROVED**. Full corpus **NOT AUTHORIZED**. Wave 5 **BLOCKED**. PSR-AMB-01 **KNOWN NON-BLOCKING — MONITORED**.

## 2. Git Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/canonical-post-recovery` |
| HEAD | `774d53bb4c81c2cde9ad45d98a854ee2f6ca976e` |
| Recovery ancestor `ebc65acd…` | PASS |
| Run 004 SPPC-05 PASS authority | Present |
| Phase 3 prior execution | None (first run) |
| Unrelated WIP | Untouched |

## 3. Run 004 Authority

- **Run ID:** `corv-semantic-v2-20260626-004`
- **Prior lifecycle:** `PHASE_0_1_2_COMPLETE`
- **Post-canary lifecycle:** `BLOCKED_AT_PHASE_3_CANARY`
- **Gate B:** PASS — OPERATOR REVIEW REQUIRED
- **Corpus processed (production):** 0 / 2368

## 4. ORCA Authority

All five frozen components verified by SHA-256 — **no drift**:

| Component | Version | Hash prefix |
|-----------|---------|-------------|
| semantic-adjudicator.mjs | v1.5 | 9618364947BA812C |
| platform-compatibility.mjs | v1.1 | 49B8C4D604EE732F |
| hard-rules.mjs | v1.2 | E6CD74CCCA6ED453 |
| prompt-contract.mjs | v1.4 | 481075E55A827404 |
| service-intent-evidence.mjs | v1.1 | 5BFFF7AE2ED3B854 |

Approved fixtures unchanged: PQR-ABSTAIN-03 → ABSTAIN; PC-ABSTAIN-01 → ABSTAIN; CFM-PROD-UPD-02 → REJECT.

## 5. Input Authority

- **Project:** PRJ-0013
- **MIG session:** session-mig-20260622-corv01
- **Corpus:** 2368 records, SHA-256 prefix `eaa09b8450f82738`, IDs `CR2-PHR-*`
- **Parent normalized:** 2399 → 31 dedup clusters → 2368 canonical

## 6. Cost Projection

| Item | USD |
|------|-----|
| SPPC-05 recorded | 0.6853 |
| Projected canary (pre-run) | ~0.10–0.15 |
| Max exposure (pre-run) | ~0.83 |
| Hard cap | 3.00 |
| Soft warning | 2.00 |
| **Actual canary cost** | **0.0851** |
| **Cumulative** | **0.7703** |

Expected calls: ~240 (primary + reassessment × 120). Actual tokens: 299,068 in / 66,999 out.

## 7. Phase Transition

`PHASE_0_1_2_COMPLETE` → `PHASE_3_CANARY_AUTHORIZED` → execution → `BLOCKED_AT_PHASE_3_CANARY` (automated fail rule).

Authorization receipt: STORAGE `receipts/phase-3-authorization-receipt-v1.json`.

## 8. Canary Selection Method

- **Seed:** `corv-run004-canary-v1-20260628`
- **Algorithm:** edge-case representatives first → family minimums (with tag fallback) → deterministic SHA-256 rank fill to exactly 120
- **Reproducible:** yes — stable IDs + seed + documented priority

## 9. Canary Composition

All 11 family minimums met (120 total):

| Family | Selected |
|--------|--------:|
| direct_commercial_1c_service | 20 |
| problem_troubleshooting | 15 |
| integrations | 10 |
| marking_chestny_znak | 8 |
| ts_piot | 5 |
| product_license_version | 12 |
| informational_self_service | 12 |
| careers_training_education | 8 |
| generic_erp_platform_ambiguity | 8 |
| geography_modified | 10 |
| ambiguous_mixed_intent | 12 |

## 10. Selection Manifest

Git: `CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v1.json`  
STORAGE: `manifests/canary-selection-v1.json`

Edge cases included: product_plus_service_bundle, problem_without_commercial_marker, psr_amb_01_family.  
**Not in corpus:** foreign_incompatible_platform, generic_erp_ambiguity exact fixture, self_service_update_instructions, direct_1c_version_update_service, ambiguous_diy_troubleshooting (closest representatives used where available).

## 11. Lock Authority

Phase `PHASE_3_CANARY` lock acquired atomically, owner PID written, released with receipt.  
STORAGE: `locks/run.lock.json` (status RELEASED), `receipts/phase3-lock-release-receipt-v1.json`.

## 12. Checkpoint Authority

Pre-execution: `project_processed: 0`, `canary_selected: 120`, `canary_processed: 0`.  
Post-execution: `canary_processed: 120`, `full_production_processed: 0`.  
STORAGE: `checkpoints/checkpoint-phase3-canary-failed-v1.json`.

## 13. Batch Execution

6 batches × 20 phrases. All batches completed. Immutable input ID lists + start/completion receipts under STORAGE `batches/canary-batch-01…06/`.

## 14. Assessment Pipeline

Wave 3.1F per phrase: blind primary → independent reassessment → service-intent evidence → platform compatibility → hard rules → adjudication → mandatory invariants.

## 15. Verdict Distribution

| Verdict | Count | % |
|---------|------:|--:|
| ACCEPT | 32 | 26.7 |
| REJECT | 59 | 49.2 |
| ABSTAIN | 29 | 24.2 |

## 16. Structured Output

Schema validity: **100%** (120/120). Model errors during pipeline: 2 (non-blocking; all records schema-valid).

## 17. Expected-Policy Evaluation

| Metric | Count |
|--------|------:|
| Pre-authorized items | 46 |
| False accepts | **0** |
| False rejects | **12** |
| Wrong abstains | **2** |

**Critical finding:** All 12 false-rejects are phrases bucketed as `direct_commercial_1c_service` with pre-authorized ACCEPT, but phrases are career/education/informational (e.g. «собеседование 1с программиста», «как стать программистом 1с»). ORCA **correctly REJECTed** them. Failure is **expectation-policy / selection-classifier mislabel**, not demonstrated ORCA over-rejection of true commercial demand.

## 18. Platform Compatibility

EXPLICIT_COMPATIBLE dominant on 1C service phrases. No foreign-platform corpus fixtures available. Generic ERP bucket uses ERP-tagged representatives (8 phrases).

## 19. Problem and DIY Queries

15 problem/troubleshooting phrases; conservative ABSTAIN/REJECT mix. Ambiguous DIY edge not represented by exact corpus fixture.

## 20. Product and License Queries

12 product_license_version phrases (tag-fallback selection). Pre-authorized REJECT policy applied where product-only evidence detected.

## 21. Product-Plus-Service Ambiguity

3 PSR-AMB-01 family phrases monitored. Verdicts: 1 ACCEPT, remainder REJECT/ABSTAIN. **Does not expand false-accept family** (threshold >60% not met).

## 22. Integrations

10 phrases; mixed ACCEPT/REJECT/ABSTAIN — review-required for borderline integration+DIY overlap.

## 23. Marking and Честный знак

8 phrases; predominantly REJECT/ABSTAIN on product-adjacent marking queries — aligned with product/service separation policy.

## 24. TS ПИОТ

5 phrases selected; commercial-service ACCEPT on direct TS PIOT service demand; ABSTAIN on informational variants.

## 25. Careers and Training

8 phrases in dedicated bucket; **100% REJECT** — matches exclusion policy.

## 26. Geography

10 geography-modified phrases; strong-commercial geo ACCEPT cases preserved; geography-alone insufficient cases ABSTAIN/REJECT.

## 27. Error-Family Analysis

Full JSON in `CORVONERO-RUN-004-PHASE-3-CANARY-REVIEW-PACKAGE-v1.json` → `error_families`. No broad false-accept family. Automated stop triggered on false-reject count driven by classifier mis-bucketing.

## 28. PSR-AMB-01 Family Status

| Metric | Value |
|--------|-------|
| Monitored phrases | 3 |
| ACCEPT | 1 |
| Expands false-accept family | **NO** |
| Operator status | REVIEW REQUIRED (non-blocking) |

## 29. Cost and Runtime

- Runtime: ~15 min (890 s)
- Canary: $0.0851
- Cumulative: $0.7703
- Retries: 0
- Confirmation disagreement rate: 10%

## 30. Canary Verdict

```text
CANARY: FAILED
Run 004: BLOCKED_AT_PHASE_3_CANARY
```

Automated fail rules: `broad_false_reject_family` (12 ≥ 5 threshold), `direct_commercial_systematically_rejected` (12/20 REJECT in mislabeled bucket). **Substantive ORCA regression not established** — false rejects trace to selection/expectation misclassification.

## 31. Project Lifecycle

```text
Project: FROZEN (full corpus NOT authorized)
Run: BLOCKED_AT_PHASE_3_CANARY
canary_processed: 120
full_production_processed: 0
```

## 32. Runtime Cleanup

Lock released. No orphaned ACTIVE lock. Raw responses preserved in STORAGE `raw-responses/` (outside Git).

## 33. Outputs Created

| Output | Location |
|--------|----------|
| Selection manifest | `pilots/corvonero/CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v1.json` |
| Result MD/JSON | `CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v1.*` |
| Review package | `CORVONERO-RUN-004-PHASE-3-CANARY-REVIEW-PACKAGE-v1.*` |
| Phase 4 next task | `CORVONERO-RUN-004-PHASE-4-NEXT-TASK-v1.md` |
| This report | `reports/REPORT-corvonero-run-004-phase-3-canary-v1.md` |
| Run receipts | `runs/corv-semantic-v2-20260626-004/sanitized-canary-receipt-v1.json` |

## 34. Git and STORAGE Placement

- **Git:** sanitized manifests, results, review packages, reports
- **STORAGE:** locks, checkpoints, batches, raw-responses, authorization receipts
- **No commit. No push.**

## 35. Tests

Execution script + classifier validated pre-run. Post-run: 120/120 processed, 100% schema valid, ORCA hash verification PASS.

## 36. Files Changed

**Created (this task):**

- `pilots/corvonero/tools/canary-family-classifier.mjs`
- `pilots/corvonero/tools/execute-run-004-phase3-canary-v1.mjs`
- `pilots/corvonero/tools/finalize-run-004-phase3-canary-v1.mjs`
- All Phase 3 output artefacts listed in §33
- STORAGE batch/checkpoint/raw-response artefacts

**Not modified:** ORCA source, `projects/projects/`, historical runs 002/003, raw Wordstat/MIG corpus.

## 37. Git Status

Branch `mars/canonical-post-recovery`. New untracked files under `pilots/corvonero/` and `reports/`. Pre-existing unrelated WIP unchanged.

## 38. SAFE UNKNOWN

- No **foreign/incompatible platform** phrase exists in the 2368-record canonical corpus — policy edge not live-tested.
- Automated FAIL may **overstate ORCA risk** due to selection-classifier assigning career/education phrases to `direct_commercial_1c_service` with ACCEPT expectation.

## 39. Operator Decisions Required

1. Review canary evidence package and 12 false-reject IDs (likely classifier issue).
2. Decide: **(A)** accept ORCA stability and authorize Phase 4 with improved canary selection v2, **(B)** request canary re-run with fixed classifier (new operator authorization — do not overwrite this run), **(C)** block full corpus pending further review.
3. PSR-AMB-01: review 1 ACCEPT instance in monitored family.
4. **Do not** authorize full corpus without explicit Phase 4 charter.

## 40. Exact Phase 4 Task

See `pilots/corvonero/CORVONERO-RUN-004-PHASE-4-NEXT-TASK-v1.md` — **NOT AUTHORIZED** until operator sign-off on Phase 3 review.

## 41. Stop Condition

**STOPPED** after 120-phrase canary and review package. Did **not** continue to: remaining corpus, production batches, semantic assembly, strategy, Campaign Architecture, Commander, import, launch, Wave 5.

**Next gate:**

```text
OPERATOR REVIEW OF CORVONERO RUN 004 PHASE 3 CANARY
```
