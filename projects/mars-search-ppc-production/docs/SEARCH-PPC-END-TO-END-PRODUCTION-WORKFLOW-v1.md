# Search PPC end-to-end production workflow v1

**Status:** DOCUMENTED (human-operated)  
**Cross-ref:** `docs/release-gate/CAMPAIGN-RELEASE-STATE-MODEL-v1.md`, `semantic-lifecycle.mjs`

## Phases

1. **Business discovery** — intake, service scope, geo, commercial claims (SPPC-01)
2. **Research** — Wordstat, SERP, competitor signals
3. **Normalization** — dedupe, morphology, corpus hygiene
4. **Semantic classification** — KEEP / REJECT / HOLD / MOVE with rationale
5. **Operator semantic approval** — receipt required; never script-automated
6. **Authority freeze** — hashes locked
7. **Campaign architecture** — groups, routing, landing mapping
8. **Ad generation** — per-group copy, mode-aware propositions
9. **Negatives** — mode-level sets; TXT separate from embedded XLSX when policy blank
10. **Commander generation** — XLSX + manifests + checksums
11. **Artifact validation** — reopen XLSX, phrase-slot reconciliation, release gate
12. **Client approval materials** — ads workbook, strategy, appendix
13. **Landing production** — FINAL_PAGE_COPY + IMPLEMENTATION_PRODUCTION_BRIEF (separate)
14. **Client feedback wait** — CLIENT_FEEDBACK_PENDING
15. **Commander import** — operator only after client + technical gates
16. **Import reconciliation** — counts, bids, display paths
17. **Post-import** — manual TXT negatives, regions, analytics
18. **Launch approval** — operator only

## Distinctions (non-interchangeable)

| Gate | Meaning |
|------|---------|
| SCRIPT_PASS | Automation technical check |
| OPERATOR_SEMANTIC_APPROVAL | Human semantic sign-off |
| ARTIFACT_VALIDATED | XLSX matches frozen authority |
| CLIENT_APPROVED | Client signed off materials |
| IMPORT_RECONCILED | Post-import verification |
| LAUNCH_APPROVED | Direct launch authorized |

## Corvonero reference

Pilot closure: `pilots/corvonero/CORVONERO-POST-PROJECT-CLOSURE-CHECKLIST-v1.md`
