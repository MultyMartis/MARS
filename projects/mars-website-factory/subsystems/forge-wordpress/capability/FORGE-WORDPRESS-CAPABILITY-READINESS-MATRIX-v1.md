# Forge WordPress Capability Readiness Matrix v1

**Version:** v1.3  
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
| WordPress runtime | **PROVEN WITH LIMITATIONS** | Live MLI-WP-SYN-001; Forge theme/plugin active (FW-05R) |
| ACF workflow | **PROVEN WITH LIMITATIONS** | ACF Free 6.8.4 live; Settings API deviation |
| Validation runners | **PROVEN WITH LIMITATIONS** | Live PHP/PHPCS/routes + Playwright captures |
| Visual regression | **PROVEN WITH LIMITATIONS** | 12 pairs; PASS WITH DEVIATIONS; WV6 pending |
| Packaging | **PROVEN** | FWS-0001-RC2 complete |
| Handoff | **PROVEN WITH LIMITATIONS** | Simulation v2 complete |
| Synthetic source persistence | **PROVEN** | Narrow Git whitelist (FW-05R checkpoint) |
| Synthetic test | **COMPLETE** | FWS-0001 static + live |
| Agent promotion | **ELIGIBLE (doc pack)** | Registry still requires charter |
| Client pilot eligibility | **WAITING** | FP-0002 frontend not complete |

---

## Lifecycle

```text
FOUNDATION / PRE-OPERATIONAL
Synthetic capability: PROVEN WITH LIMITATIONS
```

Do **not** use `OPERATIONAL` until client pilot evidence (FW-06+).

---

## MLI alignment (MLI-03 / FW-05R)

```text
MLI shared toolchain: READY
WordPress runtime profile: PROVEN WITH LIMITATIONS (MLI-WP-SYN-001)
FW-05R live synthetic validation: COMPLETE
```

---

## FW-05 / FW-05R outcome block

```text
FW-05 — COMPLETE
FW-05R — COMPLETE (PROVEN WITH LIMITATIONS)
FW-06 — WAITING FOR FP-0002 FRONTEND
Operator WV6 — PENDING
Direct local domain — PENDING HOSTS ELEVATION
Synthetic source — TRACKED
```

---

*Readiness matrix v1.3 — post FW-05R.*
