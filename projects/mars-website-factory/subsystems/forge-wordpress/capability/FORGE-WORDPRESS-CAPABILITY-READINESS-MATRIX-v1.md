# Forge WordPress Capability Readiness Matrix v1

**Version:** v1.2  
**Date:** 2026-06-23

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
| Local environment | **PROVEN WITH LIMITATIONS** | MLI-03 WordPress synthetic runtime MLI-WP-SYN-001 on Laragon |
| Required tools | **PROVEN WITH LIMITATIONS** | PHP/PHPCS/WP-CLI on MLI; live WP baseline validated |
| WordPress runtime | **PROVEN WITH LIMITATIONS** | Live synthetic runtime installed; Forge theme/plugin pending FW-05R |
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

## MLI alignment (MLI-03)

```text
MLI shared toolchain: READY
WordPress runtime profile: PROVEN WITH LIMITATIONS (MLI-WP-SYN-001)
FW-05R live synthetic validation: AUTHORIZED
```

---

## FW-05 outcome block

```text
FW-05 — COMPLETE
MLI-03 — COMPLETE
FW-05R — AUTHORIZED (next)
FW-06 — AFTER FW-05R
```

---

*Readiness matrix v1.2 — post MLI-03.*
