# REPORT — CORVONERO PHASE 6 PARTIAL CAMPAIGN-PLANNING ARCHITECTURE V1

## 1. Safety and Authorization

- Phase 6 authorized by operator partial semantic sign-off (Run corv-semantic-v2-20260626-004)
- No OpenRouter or provider calls
- No semantic verdict changes
- No ORCA / canonical corpus mutation

## 2. Git Preflight

- Branch: `mars/canonical-post-recovery`
- HEAD descends from pre-Phase-6 checkpoint (`88facdb7`)
- Unrelated WIP untouched

## 3. Semantic Authority

| Registry | Count | Expected |
|----------|-------|----------|
| ACCEPT | 935 | 935 |
| REJECT | 368 | 368 |
| ABSTAIN | 296 | 296 |
| Assessed | 1599 | 1599 |

Integrity: PASS

## 4. Partial-Coverage Boundary

- **PARTIAL SEMANTIC AUTHORITY:** 1599 / 2368 assessed
- **UNPROCESSED BACKLOG:** 769 / 2368 excluded
- **COVERAGE:** 67.5%

## 5. Campaign-Eligible Input

935 ACCEPT records → CAMPAIGN_ELIGIBLE_ACCEPT manifest  
368 REJECT → EXCLUSION_EVIDENCE_REJECT only  
296 ABSTAIN → HOLDOUT_ABSTAIN  
769 → UNPROCESSED_BACKLOG excluded

## 6. Campaign-Family Proposal

- CF-PROGRAMMER-SPECIALIST: 383 phrases
- CF-SUPPORT-AND-SUBSCRIPTION: 152 phrases
- CF-MODIFICATION-DEVELOPMENT: 64 phrases
- CF-REPORTS-PROCESSING: 37 phrases
- CF-INTEGRATIONS: 48 phrases
- CF-MARKING-CHESTNY-ZNAK: 218 phrases
- CF-TS-PIOT: 4 phrases
- CF-TROUBLESHOOTING: 2 phrases
- CF-PRICE-AND-COST: 17 phrases
- CF-ONE-OFF-WORK: 5 phrases
- CF-IMPLEMENTATION: 5 phrases

## 7. Intent Architecture

Eight intent classes separated in ad-group draft: SPECIALIST_SEARCH, DIRECT_SERVICE_ORDER, PRICE_AND_COST, SUPPORT_AND_MAINTENANCE, PROBLEM_RESOLUTION, MODIFICATION, INTEGRATION, IMPLEMENTATION.

## 8. Ad-Group Architecture Draft

30 draft groups — split by campaign family × primary intent × geography bucket.

## 9. Phrase Allocation Reconciliation

```
935 ACCEPT = 935 allocated + 0 planning holdout
```

- Duplicates: 0
- Missing ACCEPT: 0
- REJECT in allocation: 0
- ABSTAIN in allocation: 0
- Unprocessed in allocation: 0
- **Reconciliation:** PASS

## 10. Geography Options

See `CORVONERO-PHASE-6-GEOGRAPHY-OPTIONS-v1.md` — options GEO-A (recommended default), GEO-B, GEO-C.

## 11. Landing-Page Mapping

All matches **SAFE UNKNOWN** — operator confirmation required. Sites: lk.corvonero.ru, corvonero.ru.

## 12. Exclusion Boundaries

12 exclusion families from Phase 5.2 taxonomy — design-only boundaries, not deployable minus lists.

## 13. ABSTAIN Holdout

296 records classified into 6 holdout categories — not allocated to standard groups.

## 14. Commercial Prioritization

Tier distribution in `CORVONERO-PHASE-6-COMMERCIAL-PRIORITIES-v1.json`.

## 15. Risk Register

11 risks documented — R-04 (LP mismatch) blocking for ad phase.

## 16. Operator Decision Packet

9 decisions — OD-01, OD-06, OD-09 blocking.

## 17. Phase 6 Verdict

**PASS — OPERATOR ARCHITECTURE REVIEW REQUIRED**

Project: READY_FOR_PARTIAL_CAMPAIGN-ARCHITECTURE SIGN-OFF

## 18. Project Lifecycle

READY_FOR_PARTIAL_CAMPAIGN-ARCHITECTURE SIGN-OFF (pending operator review)

## 19. Outputs Created

- pilots/corvonero/CORVONERO-PHASE-6-PARTIAL-CAMPAIGN-PLANNING-RESULT-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-CAMPAIGN-FAMILIES-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-AD-GROUP-ARCHITECTURE-DRAFT-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-PHRASE-ALLOCATION-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-GEOGRAPHY-OPTIONS-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-LANDING-PAGE-MAP-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-EXCLUSION-BOUNDARIES-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-ABSTAIN-HOLDOUT-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-COMMERCIAL-PRIORITIES-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-RISK-REGISTER-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-OPERATOR-DECISION-PACKET-v1.json
- pilots/corvonero/CORVONERO-PHASE-6-PARTIAL-CAMPAIGN-PLANNING-RESULT-v1.md
- pilots/corvonero/CORVONERO-PHASE-6-GEOGRAPHY-OPTIONS-v1.md
- pilots/corvonero/CORVONERO-PHASE-6-OPERATOR-DECISION-PACKET-v1.md
- pilots/corvonero/CORVONERO-PHASE-7-NEXT-TASK-PARTIAL-v1.md
- reports/REPORT-corvonero-phase-6-partial-campaign-planning-v1.md

## 20. Files Changed

New Phase 6 artefacts under `projects/mars-search-ppc-production/pilots/corvonero/` and report under `reports/`.  
Tool script: `tools/execute-phase-6-partial-campaign-planning-v1.mjs` (generator — not a runtime product).

## 21. Git Status

No commit. No push. Unrelated WIP unchanged.

## 22. SAFE UNKNOWN

- NDS / VAT status for ad messaging
- Landing-page URL-level suitability on lk.corvonero.ru / corvonero.ru
- Conversion rates and budget forecasts
- Content of 769 unprocessed backlog IDs

## 23. Operator Decisions Required

- OD-01: Launch geography
- OD-02: Campaign separation vs consolidation
- OD-03: Product-plus-service demand
- OD-04: Troubleshooting separate campaign
- OD-05: TS ПИОТ separate campaign or group
- OD-06: Landing-page assignments
- OD-07: ABSTAIN experimental holdouts
- OD-08: P1/P2/P3 launch tiers
- OD-09: Acceptability of 67.5% coverage planning

## 24. Exact Next Task

**OPERATOR REVIEW OF CORVONERO PARTIAL CAMPAIGN-PLANNING ARCHITECTURE**

## 25. Stop Condition

Phase 6 complete. Do not start ad copy, import, Commander, launch, or Wave 5.
