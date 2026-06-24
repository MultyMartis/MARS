# AG-WP-001 — FP-0002 Pilot Readiness Map v1

**Document type:** Pilot readiness mapping  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24  
**Project:** FP-0002 Shpigovsky

---

## 1. Current state map

| Requirement | State | Evidence |
|-------------|-------|----------|
| WordPress runtime | **READY** | MLI-WP-FP0002-LOCAL, `http://shpigovsky.test` |
| WordPress foundation | **READY** | FW-06A/06A.1 complete |
| Frontend implementation | **IN PROGRESS** | `workspaces/fp-0002-shpigovsky-v6/` (and v7 WIP) |
| Frontend Production Pass | **PENDING** | Not issued |
| Approved frontend intake | **PENDING** | FW-06B not executed |
| Agent architecture (AG-WP-001) | **COMPLETE** (after FW-07A) | This pack |
| Agent runtime | **NOT ACTIVE** | Documentation only |
| Pilot execution | **BLOCKED** | See §2 |

---

## 2. Pilot unlock checklist

| # | Unlock condition | Status |
|---|------------------|--------|
| 1 | Frontend completion to Production Pass criteria | **OPEN** |
| 2 | Operator visual approval | **OPEN** |
| 3 | Production Pass issued | **OPEN** |
| 4 | Approved Git commit frozen in handoff | **OPEN** |
| 5 | FW-06B intake authorized and executed | **NOT AUTHORIZED** |
| 6 | Architecture decision (mode, content model) approved | **OPEN** |
| 7 | AG-WP-001 pilot charter (operator) | **OPEN** |
| 8 | Operator WV6 (live visual parity) | **PENDING** |

---

## 3. What FW-07A does **not** unlock

- Theme integration into WordPress
- FW-06B execution
- WPilot install on FP-0002
- Autonomous agent runtime
- Production deployment

---

## 4. Expected first pilot scope (when unlocked)

1. FW-06B approved frontend intake
2. Architecture approval (likely CLASSIC or HYBRID)
3. Incremental theme block integration with visual QA
4. Content model finalization per FP-0002 discovery docs
5. Gate J handoff preparation — WPilot remains HOLD

---

## 5. Related FP-0002 documents

| Document | Role |
|----------|------|
| [FP-0002-FW-06B-APPROVED-FRONTEND-INTAKE-INPUT-v1.md](../projects/fp-0002/FP-0002-FW-06B-APPROVED-FRONTEND-INTAKE-INPUT-v1.md) | FW-06B charter input |
| [FP-0002-CONTENT-MODEL-DISCOVERY-v1.md](../projects/fp-0002/FP-0002-CONTENT-MODEL-DISCOVERY-v1.md) | Discovery — not final model |
| [FP-0002-WORDPRESS-FOUNDATION-REPORT-v1.md](../projects/fp-0002/FP-0002-WORDPRESS-FOUNDATION-REPORT-v1.md) | Foundation evidence |

---

## 6. Summary

```text
FP-0002 pilot:
BLOCKED UNTIL FRONTEND PRODUCTION PASS AND FW-06B

AG-WP-001 foundation:
READY TO SUPPORT PILOT (not execute it)
```

---

*Pilot readiness map v1 — honest blocked state.*
