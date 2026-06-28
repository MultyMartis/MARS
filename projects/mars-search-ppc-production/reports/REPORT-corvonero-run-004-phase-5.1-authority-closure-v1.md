# REPORT — CORVONERO RUN 004 PHASE 5.1 SEMANTIC AUTHORITY CLOSURE V1

**Run ID:** `corv-semantic-v2-20260626-004`  
**Date:** 2026-06-28

---

## 1. Safety and Scope

Phase 5.1 partial semantic authority closure using existing Phase 4/5 artefacts only. No provider calls. No canonical/Phase 4/Phase 5 source mutation. 769 unprocessed IDs excluded. Campaign Architecture **NOT AUTHORIZED**.

---

## 2. Git Preflight

- Branch: `mars/canonical-post-recovery`
- Recovery ancestry: verified
- Integrity: 531+578+490=1599; union=2368; disjoint manifests ✓

---

## 3. Input Authority

Run `corv-semantic-v2-20260626-004`. Phase 5 partial assembly as input. Unprocessed backlog preserved.

---

## 4. CR2-PHR-00200 Resolution

Correction record added. **REJECT**, **OPERATOR_CONFIRMED**. Model/classifier fields preserved.

---

## 5. Review-Flag Root Cause

| Root cause | Records |
|------------|---------|
| stale_review_flag_after_authoritative_verdict | 338 |
| informational_diy_ambiguity | 1 |
| education_platform_ambiguity | 1 |
| operator_decision_applied | 1 |
| product_plus_service_ambiguity | 1 |
| primary_reassessment_disagreement_only | 6 |
| ambiguous_diy_problem_demand | 3 |

---

## 6. Review Queue Reconciliation

| Disposition | Count |
|-------------|-------|
| RESOLVED_FROM_PHASE51_POLICY | 291 |
| OPERATOR_DECISION_REQUIRED | 12 |
| OPERATOR_DECISION_APPLIED | 1 |
| OPERATOR_OVERRIDE_PRESERVED | 1 |
| MALFORMED_RETRY_VERIFIED | 13 |
| RESOLVED_FROM_EXISTING_EVIDENCE | 2 |

Phase 5 operator-review-required registry records: **350** → Phase 5.1 remaining flags: **47**

---

## 7. ACCEPT Authority

Phase 5.1 ACCEPT: **926** (Phase 5: 531). Commercial demand, price/cost, marking service, integration service, and cleared stale disagreement flags.

---

## 8. REJECT Authority

Phase 5.1 REJECT: **358** (Phase 5: 578). Career, education, informational/DIY, product-only, marking DIY, TS ПИОТ certification.

---

## 9. ABSTAIN Authority

Phase 5.1 ABSTAIN: **315** (Phase 5: 490). Genuine ambiguity retained — sync troubleshooting, short queries, combined compliance scopes. Not forced to ACCEPT/REJECT.

---

## 10. Data and Policy Issues

15 records reviewed:

| Disposition | Count |
|-------------|-------|
| MALFORMED_RETRY_VERIFIED | 13 |
| RESOLVED_FROM_EXISTING_EVIDENCE | 2 |

Malformed retry flags cleared where valid Phase 4/5 responses exist.

---

## 11. Troubleshooting Coverage

| Verdict | Count |
|---------|-------|
| ACCEPT | 1 |
| REJECT | 1 |
| ABSTAIN | 14 |
| **Total** | **16** |

Phase 5 zero ACCEPT was partially caused by taxonomy mapping — sync-error phrases classified as integration troubleshooting, not SF-TROUBLESHOOTING-NOT-WORKING; classic program-not-working phrases remain ambiguous DIY vs service

---

## 12. TS ПИОТ Coverage

| Verdict | Count |
|---------|-------|
| ACCEPT | 1 |
| REJECT | 2 |
| ABSTAIN | 4 |
| **Total** | **7** |

Only explicit setup/service-demand phrases (e.g. настройка тс пиот) map to SF-TS-PIOT ACCEPT; combined marking+TS ПИОТ and DIY install queries remain ABSTAIN/REJECT

---

## 13. Integrations and Marking

Promoted from ABSTAIN to ACCEPT (stale-flag cleanup): **143**  
Total integration/marking assessed: **482**  
Remain ABSTAIN: **195**

---

## 14. Geography

| Bucket | Count |
|--------|-------|
| Novosibirsk/NSO (PRIMARY) | 4 |
| Krasnodar | 2 |
| Ekaterinburg | 8 |
| Krasnoyarsk | 5 |
| Other Russian cities | 57 |
| Russia-wide/remote | 3 |
| Irrelevant/unknown | 8 |

Geography alone does not change verdict.

---

## 15. Correction Ledger

Phase 5 corrections preserved: **189**  
Phase 5.1 additional corrections: **428**  
Total ledger v2: **617**

---

## 16. Final Verdict Distribution

| Stage | ACCEPT | REJECT | ABSTAIN |
|-------|--------|--------|---------|
| Phase 4 | 529 | 762 | 308 |
| Phase 5 | 531 | 578 | 490 |
| Phase 5.1 | 926 | 358 | 315 |

---

## 17. Genuine Operator Decision Packet

**47** records requiring actual business judgment. See `CORVONERO-RUN-004-PHASE-5.1-OPERATOR-DECISION-PACKET-v1.md`.

---

## 18. Partial Coverage Limitation

```text
ASSESSED: 1599 / 2368
UNPROCESSED: 769 / 2368
```

769 backlog IDs not imputed.

---

## 19. Phase 5.1 Verdict

```text
PHASE 5.1:
PASS — OPERATOR DECISION PACKET REQUIRED

Project:
READY_FOR_FINAL_PARTIAL_SEMANTIC_SIGN-OFF
```

---

## 20. Project Lifecycle

Ready for final partial semantic sign-off after operator packet review. Campaign Architecture remains **NOT AUTHORIZED**.

---

## 21. Outputs Created

All under `projects/mars-search-ppc-production/pilots/corvonero/` plus report in `reports/`.

---

## 22. Files Changed

New Phase 5.1 v2 artefacts only. Phase 4/5 sources unchanged.

---

## 23. Git Status

No commit. No push.

---

## 24. SAFE UNKNOWN

- 769 unprocessed phrases: verdict unknown until authorized resume
- Market demand volume: not inferred from counts

---

## 25. Operator Decisions Required

Review **47** genuine operator packet records. Approve Phase 5.1 partial semantic authority for interim planning.

---

## 26. Exact Next Task

See `CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v2.md`

---

## 27. Stop Condition

Phase 5.1 semantic authority closure **complete**. Stopped before Campaign Architecture, ad groups, ads, negatives, Commander, import, launch, Wave 5.
