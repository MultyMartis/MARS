# VPS Procurement Gate v1

**Programme:** MARS Server Ops & VPS Forge  
**Stage:** 9 — PROCUREMENT DECISION  
**Status:** **BASELINE v1** — human-operated gate  
**Not:** payment automation, provider API, or implied purchase authorization for agents

---

## 1. Purpose

Define the **minimum checklist** that must pass before any VPS purchase under Server Ops discipline.

```text
Only after ALL required gates PASS → PROCUREMENT ALLOWED
```

Agents do **not** purchase. Operator purchases after gate PASS and explicit approval.

---

## 2. Required gates

| # | Gate | PASS criteria | Status |
|---|------|---------------|--------|
| 1 | **REQUIREMENTS COMPLETE** | Stage 0–1 intake/normalization done; open blockers resolved or accepted as residuals | ☐ |
| 2 | **COMPLIANCE PASS** | Provider accepts customer from actual operator jurisdiction; no falsification proposed | ☐ |
| 3 | **USE-CASE POLICY PASS** | VPN/proxy/workload allowed for chosen location per reviewed provider material | ☐ |
| 4 | **PAYMENT PASS** | Workable legitimate payment path for operator | ☐ |
| 5 | **FAILURE-DOMAIN PASS** | Acceptable independence from existing nodes (provider / region / ASN / DNS as required) | ☐ |
| 6 | **DEEP SITE REVIEW COMPLETE** | Stage 6 done for chosen candidate; contradictions/residuals recorded | ☐ |
| 7 | **NETWORK PREFLIGHT PASS** | Stage 8 PASS where latency/throughput-sensitive (or explicitly waived with reason) | ☐ |
| 8 | **OPERATOR APPROVAL** | Named human approval to purchase exact candidate | ☐ |

If any required gate fails → **PROCUREMENT NOT ALLOWED**.

---

## 3. Verdict vocabulary

| Verdict | Meaning |
|---------|---------|
| **PROCUREMENT ALLOWED** | All required gates PASS |
| **PROCUREMENT ALLOWED WITH RESIDUALS** | PASS with listed residuals that do not block purchase |
| **HOLD** | Incomplete evidence or operator decision pending |
| **PROCUREMENT NOT ALLOWED** | Hard exclusion or failed gate |

---

## 4. Post-gate purchase constraints

Even when **PROCUREMENT ALLOWED**:

| Constraint | Rule |
|------------|------|
| Disk / storage | Confirm from **actual checkout** — do not invent |
| Marketplace preinstalls | Prefer clean OS + controlled MARS install unless chartered otherwise |
| Term | Prefer short initial term when testing new provider |
| DNS | No DNS mutation unless separately chartered |
| Build | Stop after provision → return sanitized facts → separate implementation charter |
| Post-provision network | Stage 10 required before heavy production build |

---

## 5. Related documents

- [VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](VPS-PROVIDER-SELECTION-RUNBOOK-v1.md)  
- [VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md)  
- [CHANGE-RISK-MODEL-v1.md](CHANGE-RISK-MODEL-v1.md)  
- Server B decision: [assets/SERVER-B-PLANNING/SERVER-B-PROVIDER-DECISION-v2.md](assets/SERVER-B-PLANNING/SERVER-B-PROVIDER-DECISION-v2.md)  

---

*Procurement Gate v1 · human approval required · no agent purchase.*
