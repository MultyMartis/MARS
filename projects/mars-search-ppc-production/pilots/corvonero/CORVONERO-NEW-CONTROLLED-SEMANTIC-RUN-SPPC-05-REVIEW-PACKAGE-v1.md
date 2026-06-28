# CORVONERO NEW CONTROLLED SEMANTIC RUN — SPPC-05 REVIEW PACKAGE v1

**Run ID:** `corv-semantic-v2-20260626-002`  
**Provider / model:** openrouter / openai/gpt-5-mini  
**Wave:** 3.1F · Prompt v1.3 · Adjudicator v1.3  
**Verdict:** **FAILED** — `BLOCKED_AT_SPPC_05`

---

## 1. Executive summary for operator

SPPC-05 closed-dataset validation did **not** pass canonical thresholds. Two critical failure families were observed:

| Family | Result | Threshold |
|--------|--------|-----------|
| Product confirmation adversarial FPR | **0.0125** (1/80 protected negatives) | ≤ 0.01 |
| Problem query policy | **9/10** | 10/10 required by test exit code |

Geo commercial v2, closed supplementary regression, Wave 3.1F bypass, and under-admission unit tests **passed**.

**Fail-closed actions taken:** lock released with failure receipt; checkpoint preserved; no canary; no 2368 corpus processing; no Wave 5.

---

## 2. False accept detail (critical)

| record_id | query | expected | final | class |
|-----------|-------|----------|-------|-------|
| CFM-PROD-UPD-02 | обновление sap business one до новой версии | REJECT | ACCEPT | protected product / update |

This single false accept drives FPR above the canonical 0.01 gate from `run-confirmation-validation.mjs`.

---

## 3. Problem query failure

| record_id | query | expected | final | class |
|-----------|-------|----------|-------|-------|
| PQR-ABSTAIN-03 | как исправить ошибку 0x80004005 1с | ABSTAIN | REJECT | diy_ambiguous_error |

Bare-error ABSTAIN policy may be over-aggressive on DIY-framed error queries.

---

## 4. Passed suite summary

| Suite | Result | Evidence run_id |
|-------|--------|-----------------|
| Wave 3.1F bypass audit | 12/12 PASS | static |
| Under-admission regression | 16/16 PASS | static |
| Closed-dataset regression | PASS (product FPR 0) | closed-regression-1782418950653 |
| Geo confirmation v2 | gate_pass true | confirmation-geo-pass-1782429005975 |
| Product confirmation | **gate_pass false** | confirmation-product-pass-1782425250184 |
| Problem query policy | **9/10 FAIL** | problem-policy-regression-1782429006146 |

---

## 5. Cost and runtime

| Metric | Value |
|--------|-------|
| Cumulative SPPC-05 cost | ~$0.80 USD |
| Hard cap | $3.00 USD |
| Soft warning | $2.00 USD (not exceeded) |
| Full corpus calls | 0 |

---

## 6. Operator decisions required

1. Review false accept on SAP Business One update query — product vs service boundary.  
2. Review PQR-ABSTAIN-03 ABSTAIN vs REJECT policy for DIY-framed error codes.  
3. Decide whether to authorize ORCA brain repair task (separate charter) before any new SPPC-05 attempt.  
4. **Do not** authorize Phase 3 canary until Gate B pass after repair.

Machine-readable: `CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-SPPC-05-REVIEW-PACKAGE-v1.json`
