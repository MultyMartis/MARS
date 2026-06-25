# ORCA Production Contract Integration Plan v1

**Date:** 2026-06-22  
**Contract:** `contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md`  
**Trigger:** Corvonero classifier/repair/validator authority defects v1–v6

---

## Root cause summary

| Failure | Where it became possible |
|---------|-------------------------|
| Service deletion | `run-full-production-v6.mjs` viability/HOLD logic without scope lock |
| Seed exclusion | Semantic classifier EXCLUDE without protected-seed registry |
| HOLD on narrow groups | Group viability min-count heuristics |
| Informational retention | Generic `inferLikelyIntent` + template evidence (v4) |
| Template substitution | `semantic-human-review-v4.mjs` identical reasons |
| False PASS | Pipeline validators check structure not operator scope |
| QA scope mutation | Repair packages applied without authority order |

Triumph avoided these via: **frozen scope → JSON SoT → human validation → mandatory cross-negatives → independent Commander review**. Corvonero lacked a **contract layer above** pipeline tools.

---

## Pipeline stage integration

| Stage | Current authority | Required authority | Contract input | Invariant checks | Prohibited mutations | Audit record |
|-------|-------------------|-------------------|----------------|------------------|---------------------|--------------|
| Operator scope intake | strategy markdown | **Operator scope registry** | `operator-service-scope-v1.json` | INV-SCOPE-01/02 | Auto-remove services | scope registry version |
| Campaign architecture | production JSON | **Operator architecture freeze** | campaign-architecture-v1 | INV-CAMP-01 | Undocumented split | architecture doc hash |
| Group design | ad-group-registry | **Operator group/intent map** | group registry | INV-GRP-01 | Merge without approval | group registry |
| Semantic classification | classifier scripts | **Advisory only** | semantic evidence | INV-SEM-01 | EXCLUDE protected seeds | per-phrase evidence |
| Group viability | pipeline heuristics | **Contract D + LAW-04** | scope + groups | INV-HOLD-01 | HOLD operator-required | viability log |
| Controlled tests | controlled-test-registry | **Operator test charter** | registry v2 | INV-CT-01 | Generic hypotheses | test registry |
| Negative build | collision scripts | **Post-ownership rules** | final keyword registry | INV-NEG-01 | Pre-ownership negatives | collision evidence |
| QA repair package | repair JSON | **Recommend only** | recovery package | INV-QA-01 | Scope/seed changes | repair diff |
| Pipeline validators | `*-validation-v7.json` | **Structural subset** | dataset | INV-QA-01 | Claim commercial PASS | validation JSON |
| Export XLSX | export-commander-xlsx | **Formatting only** | dataset | INV-AD-01 | Change scope | export consistency |
| Review workbook | generate-review-workbook | **Evidence display** | all registries | INV-QA-01 | Placeholder narratives | workbook inspector |
| **Contract validator** | **NEW — required gate** | **Commercial authority** | full config | all invariants | Any data mutation | `orca-production-contract-audit-v*.json` |

---

## Required wiring (planned — not full runtime rewrite)

1. **Pre-export gate:** run `validate-campaign-production-contract.mjs` — critical = block export.  
2. **Scope lock file:** update `operator-service-scope-v1.json` after recovery — no stale HOLD.  
3. **Protected seed registry:** derive from recovery package; classifier must read before EXCLUDE.  
4. **Classifier boundary:** write suggestions to advisory field; never mutate `operator-service-scope`.  
5. **Repair package boundary:** only apply items with `authority: operator_recovery`.  
6. **Validator hierarchy:** pipeline PASS must include `contract_audit: PASS` field (future).  
7. **Workbook:** add Contract Audit sheet from contract validator output.

---

## Small safe module delivered in this task

- `projects/orca/tools/validate-campaign-production-contract.mjs` (read-only)  
- **INV-SCOPE-02/03/04 authority drift checks** — blocks export when operator scope registry contradicts production (HOLD vs ACTIVE, missing groups, unauthorized export groups); does not auto-mutate authority or production files  
- Fixtures + regression tests in `projects/orca/tools/fixtures/campaign-contract/` (including authority-drift scenarios)  
- Corvonero v7 audit config and outputs

**Not delivered:** full pipeline refactor, Commander v8, automatic enforcement hooks.

---

## Authority defect closure criteria

| Defect | Closed when |
|--------|-------------|
| Scope loss | INV-SCOPE-01 passes on export candidate |
| Seed loss | INV-SEED-01 passes |
| False HOLD | INV-HOLD-01 passes |
| QA overreach | Repair cannot run without contract pre-check |
| False PASS | Contract gate required before dry-run authorization |
