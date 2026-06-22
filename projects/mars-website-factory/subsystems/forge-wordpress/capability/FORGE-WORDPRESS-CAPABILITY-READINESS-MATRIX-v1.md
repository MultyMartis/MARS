# Forge WordPress Capability Readiness Matrix v1

**Version:** v1.1  
**Stage:** FW-05 complete  
**Date:** 2026-06-22

---

## Matrix

| Component | Status | Notes |
|-----------|--------|-------|
| Primary specialist | **READY** | Invoked on FWS-0001 |
| Execution contract | **PROVEN** | Preflight + scope on synthetic case |
| Context model | **READY** | Tier loading used |
| Filesystem scope | **PROVEN** | FWS-0001 isolated; FP-0002 untouched |
| Task template | **READY** | FW-05 task followed |
| Skill pack | **PROVEN WITH LIMITATIONS** | FW-SK-01–14 exercised; runtime steps partial |
| Validator pack | **PROVEN** | FW-V-01–07 reports with honest gaps |
| Prompt pack | **READY** | — |
| Reporting standard | **PROVEN** | FW-05 report chain |
| Git workflow | **PROVEN** | FW-04 selective checkpoint |
| Local environment | **PARTIAL** | Laragon enabled MLI-01; WordPress profile validation pending MLI-03 |
| Required tools | **PARTIAL** | Node/Gulp/Playwright yes; PHP/PHPCS no |
| WordPress runtime | **PARTIAL** | Code complete; live population not executed |
| ACF workflow | **PARTIAL** | Free + Settings API deviation |
| Validation runners | **PARTIAL** | Static + Playwright reference |
| Visual regression | **PARTIAL** | Reference captures; no WP diff |
| Packaging | **PROVEN** | FWS-0001-RC1 |
| Handoff | **PROVEN** | Simulation only |
| Synthetic test | **COMPLETE** | FWS-0001 |
| Agent promotion | **ELIGIBLE (doc pack)** | Registry still requires charter |
| Client pilot eligibility | **READY FOR FW-06 INTAKE** | Operator env + charter still required |

---

## Lifecycle

```text
FOUNDATION / PRE-OPERATIONAL
Synthetic capability: PROVEN WITH LIMITATIONS
```

Do **not** use `OPERATIONAL` until client pilot evidence (FW-06+).

---

## FW-05 outcome block

```text
FW-05 — COMPLETE
Synthetic capability — PROVEN WITH LIMITATIONS
Prompt-driven operational_doc_pack candidate — ELIGIBLE
Agent registration — NOT PERFORMED
FW-06 — NEXT
```

---

*Readiness matrix v1.1 — post FW-05.*
