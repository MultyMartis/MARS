# Website Factory — Runtime Roadmap v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/runtime-architecture/`  
**Статус:** evolution roadmap — **documentation only**  
**Связь:** [RUNTIME-GAPS-v1.md](RUNTIME-GAPS-v1.md), [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)

---

## 1. Current delivery (v1)

| Artefact | Status |
|----------|--------|
| Runtime Architecture System v1 | **ACCEPTED** (2026-06-04) |
| Project Lifecycle v1 | **ACCEPTED** |
| Project State Model v1 | **ACCEPTED** |
| State Transition Rules v1 | **ACCEPTED** |
| Runtime Gates v1 | **ACCEPTED** |
| Runtime Handoffs v1 | **ACCEPTED** |
| Runtime Failure Library v1 | **ACCEPTED** |
| Runtime Gaps v1 | **ACCEPTED** |

**Maturity:** documentation + human-operated movement discipline. **No runtime product.**

---

## 2. Operator acceptance

| Step | Status |
|------|--------|
| Runtime Architecture v1 delivery | **COMPLETE** (documentation) |
| Operator acceptance | **PENDING** — per priorities register |
| Integration with ARCHITECTURE-FOUNDATION-v1 | **RECOMMENDED** — hygiene pass after acceptance |

---

## 3. Post-v1 phases (not queued)

| Phase | Scope | Prerequisite |
|-------|-------|--------------|
| **R2** | Project manifest standard (RT-G10) | Runtime v1 ACCEPTED |
| **R3** | Human-operated state log template | R2 or parallel charter |
| **R4** | Factory Engine Architecture | Separate workstream — **NOT QUEUED** |
| **R5** | MIG interoperability semantics | MIG charter + RT-G08 |
| **R6** | Semi-automated gate helpers (read-only advisors) | S5 tooling boundaries |
| **R7** | Workflow engine evaluation | Explicit drift review — high risk |

---

## 4. Relationship to Production QA

Production QA v1 defines **readiness before Frontend**.

Runtime v1 defines **when** project may occupy `PRODUCTION_QA_READY`, `FRONTEND_READY`, `COMPLETE`.

**No duplication:** Production QA gates remain in [production-qa/](../production-qa/); Runtime references them via `RG-PRODUCTION_QA_PASS`.

---

## 5. Success criteria (v1)

- [x] Full state model (14 states)
- [x] Transition discipline documented
- [x] Gates + handoffs + failures
- [x] No agents / engine / code claims
- [ ] Operator acceptance — **pending**
- [ ] ARCHITECTURE-FOUNDATION pointer update — **optional hygiene**

---

*Runtime Roadmap v1 — 2026-06-01.*
