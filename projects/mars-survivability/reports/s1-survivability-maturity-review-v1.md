# S1 Survivability Maturity Review (v1)

**Status:** Qualitative maturity assessment — documentation only  
**Date:** 2026-05-24  
**Method:** Repo evidence + D-01/D-02 drill results + S1 audit  
**Ratings:** LOW · MEDIUM · HIGH · EXPERIMENTAL (higher = more mature for human-operated survivability)

---

## 1. Dimension scorecard

| Dimension | Score | Evidence summary |
|-----------|-------|------------------|
| **Filesystem survivability** | **MEDIUM** | Infra folders + quarantine protocol + destructive policy; **no** OS sandbox or enforced deny |
| **Rollback discipline** | **MEDIUM** | D-02 manual restore proven; rollback advisor + logs; **no** automation |
| **Human-operated recovery** | **HIGH** | D-02 quarantine-first + selective restore + hash verify; human authority protocol |
| **Drift detection** | **MEDIUM** | G4 tooling + chat drift protocol; registry linter RD-030; **no** scheduled scan |
| **Validator usefulness** | **HIGH** | D-01 DENY accuracy strong; most valuable pre-exec gate; CLI-only |
| **Operational resilience** | **MEDIUM** | Strong doc corpus + drills; operator load remains; no hooks |
| **AI execution safety** | **LOW** | AGENT + full shell still unblocked technically; guardrails doc-only |
| **Production readiness** | **EXPERIMENTAL** | Sandbox drills only; Triumph/production not exercised |
| **Website Factory safety** | **MEDIUM** | Factory enforcement contract + safe production rules; no CI pixel diff |
| **GitGuard maturity** | **MEDIUM** | Advisory framework complete G0–G4; **no** product pack; positioning stable |

---

## 2. Dimension detail

### Filesystem survivability — MEDIUM

- **Up:** `_snapshots`, `_quarantine`, protected zones, FORBIDDEN list  
- **Down:** Agent can still invoke destructive shell; `.cursorrules` not machine-enforced  

### Rollback discipline — MEDIUM

- **Up:** D-02 rollback map draft, logs/rollback-history/, rollback-advisor  
- **Down:** Partial snapshot mirrors; no one-click restore  

### Human-operated recovery — HIGH

- **Up:** D-02 restore-to-new-workspace, drift artifact exclusion, audit trail  
- **Down:** Drill ≠ real incident stress  

### Drift detection — MEDIUM

- **Up:** manifest-cross-validator, registry-drift-linter, chat-context-drift-protocol  
- **Down:** Label noise in sandbox; no continuous monitoring  

### Validator usefulness — HIGH

- **Up:** D-01 verdict "most valuable gate"; forbidden patterns reliable  
- **Down:** Sandbox false positives; not wired to shell  

### Operational resilience — MEDIUM

- **Up:** OPERATIONAL-INDEX, QUICKSTART, checklists, log format  
- **Down:** Many manual steps; documentation gravity  

### AI execution safety — LOW

- **Up:** Risk classes, halt protocol, prompt library  
- **Down:** Proven failure mode (context-drift incident); no enforcement hook  

### Production readiness — EXPERIMENTAL

- **Up:** Factory enforcement docs exist  
- **Down:** No production drill; hooks absent; scorecard pre-drill HIGH RISK domains largely unchanged for prod  

### Website Factory safety — MEDIUM

- **Up:** website-factory-enforcement-v1, safe-production-rules, clone-first patterns  
- **Down:** No automated parity gate in repo  

### GitGuard maturity — MEDIUM

- **Up:** Full advisory stack G0–G4; S1 positioning stable; terminology freeze  
- **Down:** No `projects/gitguard/`; future CLI/hooks SAFE UNKNOWN  

---

## 3. Comparison to pre-drill scorecard (2026-05-23)

| Domain | Scorecard v1 | S1 (post D-01/D-02) |
|--------|--------------|---------------------|
| Snapshot discipline | HIGH RISK posture | **MEDIUM** maturity in sandbox |
| Rollback readiness | HIGH RISK posture | **MEDIUM** maturity |
| Agent safety | HIGH RISK posture | **LOW** maturity (unchanged enforcement) |
| Overall | HIGH RISK for agent FS work | **MEDIUM** documented / **LOW** enforced |

Scorecard retained as **historical** baseline — not deleted.

---

## 4. Maturity summary

**Strongest:** human-operated recovery workflow, validator advisory value, GitGuard positioning clarity.  
**Weakest:** AI execution safety enforcement, production-scoped evidence, automated protection (intentionally absent).

---

## 5. SAFE UNKNOWN

- Operator acceptance of maturity ratings  
- Production tabletop drill outcomes (G5a charter)

---

*End of S1 Survivability Maturity Review v1.*
