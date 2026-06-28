# CORVONERO NEW CONTROLLED SEMANTIC RUN — PHASE 0/1/2 RESULT v1

**Run ID:** `corv-semantic-v2-20260626-002`  
**Date:** 2026-06-26  
**Gate A:** APPROVED  
**Gate B:** FAILED  
**Project lifecycle:** `BLOCKED_AT_SPPC_05`

---

## Summary

Phase 0 (authority freeze), Phase 1 (immutable input registration), and Phase 2 (closed-dataset SPPC-05 validation) were executed on a new isolated STORAGE root. The canonical 2368-phrase corpus was verified and registered read-only. Old-run isolation passed. SPPC-05 **failed** on product confirmation adversarial FPR (0.0125 > 0.01) and problem-query policy (9/10). Full corpus, canary, and Wave 5 were **not** started.

**Note:** Run `corv-semantic-v2-20260626-001` was an abandoned orchestrator attempt (isolation false-positive on policy text); authoritative run is **002**.

---

## Operator decisions recorded

| Decision | Value |
|----------|-------|
| Production provider | openrouter |
| Production model | openai/gpt-5-mini |
| Hard cost cap | $3.00 USD |
| Soft cost warning | $2.00 USD |
| Old run resume | PROHIBITED |
| Old forensic cache reuse | PROHIBITED |
| Missing TS PIOT SERP | NON-BLOCKING |
| Wave 5 | BLOCKED |

---

## Gate verdicts

| Gate | Verdict |
|------|---------|
| A — Charter | APPROVED FOR PHASE 0/1/2 |
| B — SPPC-05 | **FAILED** |
| C — Canary | NOT AUTHORIZED |
| Full corpus | NOT STARTED |

---

## Critical SPPC-05 failures

1. **Product confirmation** — adversarial FPR **0.0125** (threshold ≤ 0.01). False accept: `CFM-PROD-UPD-02` — «обновление sap business one до новой версии».
2. **Problem query policy** — **9/10**. Failure: `PQR-ABSTAIN-03` — «как исправить ошибку 0x80004005 1с» — expected ABSTAIN, received REJECT.

---

## Passed dimensions

- Wave 3.1F bypass audit: 12/12  
- Under-admission unit regression: 16/16  
- Closed-dataset regression: product FPR 0, boxed delivery fixed  
- Geo commercial confirmation v2: gate_pass true, adversarial FPR 0, commercial recall 1.0  
- Old-run isolation: PASS  
- Corpus integrity: 2368 records, hash verified  
- Cost: ~$0.80 USD (under hard cap)

---

## Next gate

**OPERATOR REVIEW OF CORVONERO NEW CONTROLLED RUN SPPC-05 RESULT**

Do not authorize Phase 3 canary until operator reviews failure evidence and decides repair path (separate ORCA task required).

Machine-readable: `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-0-1-2-RESULT-v1.json`
