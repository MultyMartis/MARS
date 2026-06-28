# REPORT — CORVONERO RUN 004 PHASE 5 PARTIAL SEMANTIC REVIEW V1

**Run ID:** `corv-semantic-v2-20260626-004`  
**Date:** 2026-06-28  
**Phase verdict:** PASS — OPERATOR REVIEW REQUIRED

---

## 1. Safety and Authorization

Phase 5 partial semantic review executed under operator authorization from Phase 4 partial freeze. No OpenRouter or external model API calls. No canonical corpus, ORCA, or Phase 4 source registry mutation. Strategy, Campaign Architecture, import, and launch **not authorized**.

Operator decisions recorded exactly:
- 1599 assessed records: **CURRENT-CYCLE SEMANTIC AUTHORITY**
- 769 unprocessed: **EXCLUDED FROM CURRENT-CYCLE ASSEMBLY — BACKLOG — DO NOT IMPUTE**
- Provider calls: **FROZEN**
- Phase 5: **AUTHORIZED WITHOUT MODEL CALLS**

---

## 2. Git Preflight

- Branch: `mars/canonical-post-recovery`
- Recovery ancestry: `ebc65acd4087fa9d180bb2a50921027fde51e3b7` — verified
- Partial-freeze artefacts: present
- Live Run 004 process: none detected
- Unrelated WIP: untouched

---

## 3. Partial Authority

Input authority limited to Phase 4 partial artefacts listed in task charter. Canonical corpus read for metadata only (frequency, IDs). 769 unprocessed IDs excluded from all assembly outputs.

---

## 4. Integrity Reconciliation

| Check | Result |
|-------|--------|
| Processed unique | 1599 |
| Unprocessed unique | 769 |
| ACCEPT + REJECT + ABSTAIN | 1599 |
| Overlap processed/unprocessed | 0 |
| Orphans | 0 |
| CR2-PHR-00584 override | preserved |

**Integrity verdict:** PASS — INTEGRITY RECONCILED

---

## 5. Unprocessed Boundary

```text
CURRENT-CYCLE ASSEMBLY SCOPE: 1599 assessed records only
OUT OF SCOPE: 769 unprocessed records
```

769 IDs preserved in Phase 4 unprocessed manifest only. Not included in service clusters, intent taxonomy counts for demand conclusions, or coverage percentages beyond the 67.5% assessed boundary.

---

## 6. Review Queue Triage

Source queue: 320 items (Phase 4 partial review queue).

| Triage class | Count |
|--------------|-------|
| CONFIRMED_ACCEPT | 39 |
| CONFIRMED_REJECT | 104 |
| RETAIN_ABSTAIN | 156 |
| OPERATOR_REVIEW_REQUIRED | 6 |
| DATA_OR_POLICY_ISSUE | 15 |

**CR2-PHR-00584:** CONFIRMED_REJECT — operator override preserved (model ACCEPT, authoritative REJECT).  
**CR2-PHR-00200:** OPERATOR_REVIEW_REQUIRED — informational phrasing; classifier policy disagreement.

---

## 7. ACCEPT Review

Phase 4 ACCEPT: 529 → Phase 5 reviewed ACCEPT: 531

- Accept-to-reject corrections: 1
- Accept-to-abstain corrections: 0
- Accept review-required: 347

Policy checks applied: career/employment, education, informational/self-service, foreign platforms, product-only, disagreement flags.

---

## 8. REJECT Review

Phase 4 REJECT: 762 → Phase 5 reviewed REJECT: 578

- Reject-to-accept corrections: 2
- Reject-to-abstain corrections: 184
- Reject review-required: 0

Commercial false-negative scan: price/cost of work, explicit service demand, marking, TS ПИОТ, integrations.

---

## 9. ABSTAIN Review

Phase 4 ABSTAIN: 308 → Phase 5 reviewed ABSTAIN: 490

- Promote to ACCEPT: 1
- Promote to REJECT: 1
- Retain ABSTAIN: 303
- Operator review required: 3

ABSTAIN retained as valid final state where genuine uncertainty remains.

---

## 10. Correction Ledger

Total Phase 5 corrections: **189** (all logged in `CORVONERO-RUN-004-PHASE-5-PARTIAL-CORRECTION-LEDGER-v1.json`). No silent changes.

---

## 11. Reviewed Verdict Distribution

| Verdict | Phase 4 | Phase 5 |
|---------|---------|---------|
| ACCEPT | 529 | 531 |
| REJECT | 762 | 578 |
| ABSTAIN | 308 | 490 |
| **Total** | **1599** | **1599** |

---

## 12. Service Taxonomy

- **1C programmer / specialist** (SF-1C-PROGRAMMER-SPECIALIST): 153 ACCEPT records
- **1C support and maintenance** (SF-SUPPORT-MAINTENANCE): 65 ACCEPT records
- **1C modification and development** (SF-MODIFICATION-DEVELOPMENT): 60 ACCEPT records
- **Reports and processing** (SF-REPORTS-PROCESSING): 29 ACCEPT records
- **Integrations** (SF-INTEGRATIONS): 41 ACCEPT records
- **Marking / Честный знак** (SF-MARKING-CHESTNY-ZNAK): 74 ACCEPT records
- **TS ПИОТ** (SF-TS-PIOT): 1 ACCEPT records
- **Subscription service** (SF-SUBSCRIPTION-SERVICE): 90 ACCEPT records
- **One-off work** (SF-ONE-OFF-WORK): 12 ACCEPT records
- **Other approved 1C services** (SF-OTHER-APPROVED-1C-SERVICE): 6 ACCEPT records

Families with zero ACCEPT evidence are documented with ambiguity notes in taxonomy file.

---

## 13. Intent Taxonomy

- AMBIGUOUS: 490
- INFORMATIONAL: 397
- CAREER_OR_EDUCATION: 180
- SPECIALIST_SEARCH: 155
- SUPPORT_AND_MAINTENANCE: 140
- DIRECT_SERVICE_ORDER: 107
- MODIFICATION: 62
- INTEGRATION: 53
- PRICE_AND_COST: 7
- IMPLEMENTATION: 7
- PRODUCT_OR_LICENSE: 1

---

## 14. Geography

Geography-modified phrases in assessed corpus: 87

- Primary (Novosibirsk region): 4
- Expansion cities: 15
- Remote/Russia-wide: 3
- Irrelevant geography: 8

Geography alone not treated as commercial intent.

---

## 15. Exclusion Taxonomy

- Career and jobs: 124 (overblock risk: medium)
- Education and courses: 56 (overblock risk: medium)
- Salary: 2 (overblock risk: high)
- Free downloads: 4 (overblock risk: medium)
- Self-service manuals: 17 (overblock risk: high)
- Informational research: 387 (overblock risk: high)
- Irrelevant geography: 6 (overblock risk: medium)

Taxonomy for future negative-keyword work — **not** a final Direct import list.

---

## 16. Direct Commercial Demand

ACCEPT records with direct commercial or specialist-search intent: **269**

Representative families: 1C programmer/specialist, support, modification, one-off work.

---

## 17. Problems and DIY Intent

Problem-resolution / troubleshooting records: **0** (includes ACCEPT, ABSTAIN, REJECT triage)

DIY/self-service excluded via EX-SELF-SERVICE-MANUALS and informational markers.

---

## 18. Product and License

Product/license-only records: **1**

Not equated with service intent. Product-plus-service bundles flagged for operator review.

---

## 19. Integrations

Integration-related records: **53**

---

## 20. Marking and Честный знак

Marking-related records: **418**

---

## 21. TS ПИОТ

TS ПИОТ records: **7**

---

## 22. Career and Education

Career/education excluded records: **180**

Career gate from Phase 4 preserved. CR2-PHR-00584 operator override intact.

---

## 23. Informational Demand

Informational demand records: **398**

---

## 24. Partial Coverage

```text
PARTIAL DATASET: 1599 / 2368 assessed
UNPROCESSED: 769 / 2368
COVERAGE: 67.5% of canonical records assessed
```

Phrase count does not imply market demand volume unless frequency data explicitly supports that conclusion.

---

## 25. Remaining Operator Review

Items requiring operator disposition: **350** registry records + mandatory queue items.

Review queue OPERATOR_REVIEW_REQUIRED / DATA_OR_POLICY_ISSUE items included in Phase 5 review queue output.

---

## 26. Phase 5 Verdict

```text
PHASE 5 PARTIAL: PASS — OPERATOR REVIEW REQUIRED
```

---

## 27. Project Lifecycle

```text
Project: READY_FOR_PARTIAL_CAMPAIGN-PLANNING AUTHORIZATION
```

PASS does **not** authorize Campaign Architecture automatically.

---

## 28. Outputs Created

All files under `projects/mars-search-ppc-production/pilots/corvonero/`:

- CORVONERO-RUN-004-PHASE-5-PARTIAL-INTEGRITY-v1.json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEWED-REGISTRY-v1.json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-ACCEPT/REJECT/ABSTAIN-v1.json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEW-QUEUE-v1.json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-CORRECTION-LEDGER-v1.json
- CORVONERO-RUN-004-PHASE-5-SERVICE/INTENT/GEOGRAPHY/EXCLUSION-TAXONOMY-v1.json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-COVERAGE-v1.md/json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-RESULT-v1.md/json
- CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v1.md

Report: `projects/mars-search-ppc-production/reports/REPORT-corvonero-run-004-phase-5-partial-semantic-review-v1.md`

---

## 29. Files Changed

New Phase 5 artefacts only. Phase 4 source registries unchanged.

---

## 30. Git Status

No commit. No push.

---

## 31. SAFE UNKNOWN

- Remaining 769 unprocessed phrases: semantic verdict unknown until separate authorized resume
- Market demand volume from phrase counts: not inferred
- Final minus-word lists: not produced (exclusion taxonomy is preparatory only)

---

## 32. Operator Decisions Required

1. Approve or adjust Phase 5 partial semantic assembly
2. Disposition CR2-PHR-00200 (informational vs commercial)
3. Review 350 operator-review-required registry items
4. Decide: accept 67.5% partial coverage for interim planning **or** schedule authorized resume for 769 backlog

---

## 33. Exact Phase 6 Task

See `CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v1.md`

Next gate: **OPERATOR REVIEW OF CORVONERO PARTIAL SEMANTIC ASSEMBLY**

---

## 34. Stop Condition

Phase 5 partial semantic review and assembly **complete**. Stopped before Campaign Architecture, ad groups, ads, negatives deployment, Commander, import, launch, Wave 5.
