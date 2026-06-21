# FP-0002 — Onboarding Readiness

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-11  
**Scope:** Playbook 01–05 readiness vs foundation initialization facts  

---

## Summary

Foundation initialization creates the **operational workspace** and **intake infrastructure**. It does **not** complete any Factory Playbook. FP-0002 remains **Pre-Onboarding** until Playbook 01 Manifest Enrollment is executed by a Factory operator.

**Reference playbooks:** `workspaces/website-factory-reference-v1/FACTORY-*-WORKFLOW-v1.md`  
**Pilot substrate pattern:** `workspaces/website-factory-operations/projects/FP-0001-triumph-manipulator-landing/`

---

## Playbook 01 — Manifest Enrollment

**Document:** [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](../../website-factory-reference-v1/FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md)

| Step / criterion | Status | Foundation fact |
|------------------|--------|-----------------|
| Production intent signal (E1) | **Partial** | ATLAS PRJ-0012 **active**; EV-SHPIG-OP-01 documents delivery intent |
| ATLAS-first check (ENROLL-ATLAS-01) | **Done (refs)** | ORG-0008, PRJ-0012, WEB-SHPIG-01, DOM-SHPIG-01 attested — ids known |
| Factory-scoped recognition (decision class B) | **Not done** | No operator recognition declaration recorded |
| Charter & scope tier (MRDY-02) | **Partial** | Boundaries in passport; full manifest charter categories not populated |
| Lifecycle endpoint (MRDY-03) | **Not done** | Delivery phase **SAFE UNKNOWN** |
| Reference topology (MRDY-05) | **Partial** | Workspace index exists; POC-03…POC-09 topology **not created** |
| Manifest entry anchor (MRDY-06) | **Partial** | README as informal anchor; doctrinal MOC-01 **not created** |
| MRDY-01…07 operator attestation | **Not done** | No enrollment decision (E7) |
| Outcome: **manifest-enrolled** | **Not done** | Workflow **not complete** |
| RT-G04 substrate POC-01…POC-02 | **Not done** | FP-0001 pattern not replicated for FP-0002 |

**Foundation contributes:** workspace, passport, ATLAS id bindings documented, intake ready.  
**Remaining:** full Playbook 01 operator session → manifest-enrolled + MOC-* physical artifacts.

---

## Playbook 02 — Registry Enrollment

**Document:** [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](../../website-factory-reference-v1/FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md)

| Step / criterion | Status | Note |
|------------------|--------|------|
| Prerequisite: manifest-enrolled | **Not met** | Playbook 01 incomplete |
| Registry-ready (RRDY-01…06) | **Not done** | |
| Operator catalog enrollment decision | **Not done** | |
| ROC-* registry facet entries | **Not done** | FP-0002 absent from ROC-01 catalog |
| Outcome: catalog-discoverable | **Not done** | |

**Foundation contributes:** nothing toward registry — correctly deferred.  
**Remaining:** complete Playbook 01 first; then optional Playbook 02.

---

## Playbook 03 — Tracking Surface Session

**Document:** [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](../../website-factory-reference-v1/FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md)

| Step / criterion | Status | Note |
|------------------|--------|------|
| Per-project entry (manifest anchor) | **Not met** | MOC-01 not created |
| SOC-01…SOC-08 surface views | **Not done** | |
| First operational session | **Not done** | |
| Session outcome recorded | **Not done** | |

**Foundation contributes:** PROJECT-STATUS as informal orientation only — **not** Surface.  
**Remaining:** substrate + first Surface session after Playbook 01.

---

## Playbook 04 — Project Declaration

**Document:** [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](../../website-factory-reference-v1/FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md)

| Step / criterion | Status | Note |
|------------------|--------|------|
| POC-03 state index | **Not done** | |
| POC-04 gate index | **Not done** | |
| POC-05 handoff index | **Not done** | |
| POC-06 declaration records | **Not done** | DECISIONS.md is ADR shell only — not POC-06 |
| State / gate / handoff declarations | **Not done** | |

**Foundation contributes:** DECISIONS.md template — not declarations.  
**Remaining:** full onboarding + production progress before meaningful declarations.

---

## Playbook 05 — Project Closure

**Document:** [FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md](../../website-factory-reference-v1/FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md)

| Step / criterion | Status | Note |
|------------------|--------|------|
| Active Factory track | **Not started** | |
| Closure readiness assessment | **Not done** | |
| POC-08 closure record | **Not done** | |
| Terminal outcome | **Not done** | |

**Foundation contributes:** nothing — correctly N/A at foundation.  
**Remaining:** entire production lifecycle.

---

## Cross-playbook prerequisites map

```text
  FOUNDATION (this charter) ──▶ partial Playbook 01 inputs only
         │
         ▼
  Playbook 01 Manifest Enrollment ──▶ manifest-enrolled + MOC-*
         │
         ├──▶ Playbook 02 Registry (optional)
         │
         ▼
  Playbook 03 Surface sessions (repeat)
         │
         ├──▶ Playbook 04 Declarations (repeat)
         │
         ▼
  Playbook 05 Closure (terminal)
```

---

## Additional onboarding items (outside playbooks)

| Item | Status |
|------|--------|
| Design intake (01_DESIGN/) | **Awaiting Intake** |
| Factory operator formal assignment | **Not recorded** |
| Zone README portfolio row (ROC-01) | **Not updated** — FP-0002 not in catalog |
| Physical project home under `projects/` | **Not created** — workspace at `FP-0002-SHPIGOVSKY/` per foundation charter |

---

## Readiness verdict

| Verdict | Meaning |
|---------|---------|
| **Foundation ready** | Workspace, docs, intake, learning containers — **yes** |
| **Factory onboarding ready** | Playbook 01 session can start — **yes** (ATLAS ids + intent exist) |
| **Manifest-enrolled** | **No** |
| **Production ready** | **No** — design materials required first |

---

*Human-operated readiness assessment. Not automated gate.*
