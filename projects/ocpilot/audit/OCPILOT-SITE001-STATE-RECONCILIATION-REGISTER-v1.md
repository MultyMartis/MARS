# OCPilot SITE-001 State Reconciliation Register v1

**Status:** **documented** — operational state reconciliation register (audit only).  
**Program:** OCPilot  
**Audit date:** 2026-06-07  
**Parent finding:** FINDING-XW-SIBCAR-02  
**Parent:** [OCPILOT-SITE001-STATE-RECONCILIATION-AUDIT-v1.md](OCPILOT-SITE001-STATE-RECONCILIATION-AUDIT-v1.md) · [OCPILOT-SITE001-STATE-RECONCILIATION-SUMMARY-v1.md](OCPILOT-SITE001-STATE-RECONCILIATION-SUMMARY-v1.md)  
**Is not:** site registry replacement, runtime state table, git commit.

---

## 1. Register purpose

Единый **state reconciliation register** для OCPilot **SITE-001**: декомпозиция статуса по слоям, матрица расхождений между документами, классификация Run 5, prerequisites и sync actions.

**Authority hierarchy:**

1. [OCPILOT-STATE.md](../OCPILOT-STATE.md) — execution authority  
2. [project-site-registry.md](../project-site-registry.md) — registry lifecycle  
3. [intake-readiness-review.md](../intake-readiness-review.md) + [AUDIT-CHARTER.md](../sites/site-001/AUDIT-CHARTER.md) — charter gate  
4. Site container docs — local facts; gate rows subject to drift  

---

## 2. Canonical state register

| state_id | dimension | canonical_value | primary_authority | last_signal_date |
|----------|-----------|-----------------|-------------------|------------------|
| **ST-SR-A** | Registry lifecycle | **READY FOR AUDIT** | project-site-registry.md | 2026-06-01 |
| **ST-SR-B** | Intake closure | **COMPLETE** (Run 4.99) | INTAKE-COMPLETE.md; intake-readiness-review | 2026-06-01 |
| **ST-SR-C** | Run 5 charter | **AUTHORIZED** (read-only) | AUDIT-CHARTER.md; intake-readiness-review § YES | 2026-06-01 |
| **ST-SR-D** | Run 5 execution | **PAUSED** | OCPILOT-STATE.md | 2026-06-07 |
| **ST-SR-E** | Phase 1 writes | **NOT AUTHORIZED** | SITE-001-CHANGE-AUTHORIZATION-DECISION-v1 | 2026-06-07 |
| **ST-SR-F** | EAR acquisition | **NOT EXECUTED** | PILOT-001 STATUS.md | 2026-06-01 |

---

## 3. Conflicting source register (FINDING-XW-SIBCAR-02)

| source_doc | declared_signal | dimension | reconciled | drift_flag |
|------------|-----------------|-----------|------------|------------|
| [site-passport.md](../sites/site-001/site-passport.md) | **READY FOR RUN 5** | C | **Correct** (charter) | **SR-D-01** — missing pause |
| [site-passport.md](../sites/site-001/site-passport.md) | Blocked by: **None** | D | **Incorrect** | **SR-D-02** |
| [AUDIT-CHARTER.md](../sites/site-001/AUDIT-CHARTER.md) | **READY FOR RUN 5** | C | **Correct** | — |
| [project-access-brief.md](../sites/site-001/project-access-brief.md) | Run 5 allowed **NO** | C | **Stale** | **SR-D-03** |
| [project-access-brief.md](../sites/site-001/project-access-brief.md) | Run 5 not authorized (Current State) | C | **Stale** | **SR-D-04** |
| [README.md](../sites/site-001/README.md) | Run 5 gate **NO** | C | **Stale** | **SR-D-05** |
| [README.md](../sites/site-001/README.md) | EAR snapshot path not executed | D | **Correct** | — |
| [OCPILOT-STATE.md](../OCPILOT-STATE.md) | Run 5 **paused** | D | **Correct — canonical** | — |
| [OCPILOT-STATE.md](../OCPILOT-STATE.md) | Registry **READY FOR AUDIT** | A | **Correct — canonical** | — |
| [project-site-registry.md](../project-site-registry.md) | **READY FOR AUDIT** | A | **Correct** | — |
| [intake-readiness-review.md](../intake-readiness-review.md) | Run 5 allowed **YES** | C | **Correct** | — |

---

## 4. Vocabulary crosswalk register

| phrase | registry meaning | charter meaning | execution meaning | canonical use |
|--------|------------------|-----------------|-------------------|---------------|
| **READY FOR AUDIT** | Intake complete; Run 5 may be chartered | — | Not executing | **ST-SR-A** |
| **READY FOR RUN 5** | — | Read-only audit scope authorized | Does **not** mean actively running | **ST-SR-C** only |
| **Run 5 NO** | — | Denies charter | — | **Stale** in brief/README |
| **Run 5 paused** | Does not downgrade registry | Charter remains valid | Initialization done; Phases 2–8 stopped | **ST-SR-D** |
| **NOT AUTHORIZED** | — | — | Phase 1 writes blocked | **ST-SR-E** |

---

## 5. Run 5 classification register

| class_id | layer | value | evidence_refs | operator_action |
|----------|-------|-------|---------------|-----------------|
| **R5-CLASS-01** | Charter / intake gate | **READY** | intake-readiness-review; AUDIT-CHARTER; INTAKE-COMPLETE | None — already closed Run 4.99 |
| **R5-CLASS-02** | Execution posture | **PAUSED** | OCPILOT-STATE; freeze summary; RUN-5-FIRST-FINDINGS | Wait for EAR snapshot path |
| **R5-CLASS-03** | Prerequisite debt | **BLOCKED** *(execution only)* | AUDIT-BLOCKERS-v1; PILOT-001 STATUS | Charter EAR; produce Snapshot Package |
| **R5-CLASS-04** | **Primary operational label** | **PAUSED** | Synthesis R5-CLASS-01 + 02 + 03 | Do not start Phases 2–8 |

---

## 6. Prerequisites register

### 6.1 Execution resume (blocking Phases 2–8)

| pre_id | prerequisite | type | owner | status | ref |
|--------|--------------|------|-------|--------|-----|
| **PRE-SR-01** | Snapshot Package contract operational for SITE-001 | Architecture | EAR / Operator | Not implemented | B-ARCH-01 |
| **PRE-SR-02** | First SITE-001 snapshot in external bulk | Operational | Operator | **Missing** | B-EV-02; RUN-5-FIRST-FINDINGS |
| **PRE-SR-03** | PILOT-001 approval → implementation | Process | Operator | **NOT STARTED** | PILOT-001 STATUS |
| **PRE-SR-04** | Mode 0 vs Mode 2 acquisition decision | Decision | Operator | **SAFE UNKNOWN** | AUDIT-BLOCKERS § SAFE UNKNOWN |
| **PRE-SR-05** | Version proof on live/site snapshot | Evidence | Operator / EAR | **Missing** | B-EV-01 |
| **PRE-SR-06** | File manifest vs baseline | Evidence | Operator / EAR | **Missing** | B-EV-02 |
| **PRE-SR-07** | Theme / extension / SEO / DB facts | Evidence | OCPilot post-snapshot | **Missing** | B-EV-04 |
| **PRE-SR-08** | ocStore comparison-notes methodology | Process | OCPilot human | **Empty** | B-EV-05 |

### 6.2 Documentation sync (non-blocking for charter)

| pre_id | prerequisite | type | owner | status | sync_ref |
|--------|--------------|------|-------|--------|----------|
| **PRE-SR-09** | Access-brief Run 5 gate alignment | Doc sync | Operator / editor | **Pending** | SYNC-SR-01 |
| **PRE-SR-10** | README Run 5 gate alignment | Doc sync | Operator / editor | **Pending** | SYNC-SR-02 |
| **PRE-SR-11** | Passport pause / blocker note | Doc sync | Operator / editor | **Pending** | SYNC-SR-03 |

### 6.3 Explicit non-prerequisites

| item | reason | authority |
|------|--------|-----------|
| Credential location SAFE UNKNOWN | Accepted Run 4.99 | intake-readiness-review §4b |
| Stale brief **NO** row | Doc drift only | AUDIT-BLOCKERS § Non-blockers |
| Phase 1 authorization | Separate track | CHANGE-AUTHORIZATION-DECISION |
| Atlas DOM-SIBCAR-01 attestation | Atlas-internal | Crosswalk audit §7 |

---

## 7. Drift register

| drift_id | topic | stale_source | canonical_source | severity | finding |
|----------|-------|--------------|------------------|----------|---------|
| **SR-D-01** | Passport omits execution pause | site-passport | OCPILOT-STATE | Medium | FINDING-XW-SIBCAR-02 |
| **SR-D-02** | Passport "Blocked by: None" | site-passport | AUDIT-BLOCKERS | Medium | FINDING-XW-SIBCAR-02 |
| **SR-D-03** | Access brief Run 5 **NO** | project-access-brief | intake-readiness-review | Medium | FINDING-XW-SIBCAR-02 |
| **SR-D-04** | Access brief "not authorized" | project-access-brief | AUDIT-CHARTER | Medium | FINDING-XW-SIBCAR-02 |
| **SR-D-05** | README Run 5 gate **NO** | README | intake-readiness-review | Medium | FINDING-XW-SIBCAR-02 |
| **SR-D-06** | READY FOR RUN 5 vs READY FOR AUDIT label mix | site-passport | project-site-registry | Low | Vocabulary — not factual conflict |

---

## 8. Synchronization action register

| sync_id | priority | action | target_doc | mutates_in_audit_pass | status |
|---------|----------|--------|------------|----------------------|--------|
| **SYNC-SR-01** | P1 | Run 5 **YES** + execution paused note | project-access-brief.md | **No** | Recommended |
| **SYNC-SR-02** | P1 | Gate narrative: charter YES, execution PAUSED | README.md | **No** | Recommended |
| **SYNC-SR-03** | P1 | Blocked by: EAR / Snapshot Package | site-passport.md | **No** | Recommended |
| **SYNC-SR-04** | P2 | OCPILOT-STATE cross-ref as execution authority | passport, README | **No** | Recommended |
| **SYNC-SR-05** | P2 | Keep AUDIT-CHARTER unchanged | AUDIT-CHARTER.md | **No** | No action needed |
| **SYNC-SR-06** | Hold | Human charter Run 5 Phases 2–8 post-snapshot | Operator | N/A | Out of scope |

---

## 9. Authority evidence index

| ref | artifact | reconciliation use |
|-----|----------|-------------------|
| **EV-SR-01** | [OCPILOT-STATE.md](../OCPILOT-STATE.md) | Execution authority — ST-SR-D, ST-SR-E |
| **EV-SR-02** | [project-site-registry.md](../project-site-registry.md) | Registry — ST-SR-A |
| **EV-SR-03** | [intake-readiness-review.md](../intake-readiness-review.md) | Charter gate — ST-SR-C |
| **EV-SR-04** | [AUDIT-CHARTER.md](../sites/site-001/AUDIT-CHARTER.md) | Read-only authorization |
| **EV-SR-05** | [INTAKE-COMPLETE.md](../sites/site-001/materials/INTAKE-COMPLETE.md) | Intake closure — ST-SR-B |
| **EV-SR-06** | [OCPILOT-STATE-SUMMARY-v1.md](../freeze/site-001-pre-runtime-bridge/OCPILOT-STATE-SUMMARY-v1.md) | Frozen pause baseline |
| **EV-SR-07** | [AUDIT-BLOCKERS-v1.md](../freeze/site-001-pre-runtime-bridge/AUDIT-BLOCKERS-v1.md) | Blockers vs non-blockers |
| **EV-SR-08** | [RUN-5-FIRST-FINDINGS.md](../sites/site-001/reports/RUN-5-FIRST-FINDINGS.md) | Initialization evidence |
| **EV-SR-09** | [PILOT-001 STATUS.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/STATUS.md) | EAR cross-program |
| **EV-SR-10** | [ATLAS-OCPILOT-SIBCAR-CROSSWALK-AUDIT-v1.md](../../atlas/audit/ATLAS-OCPILOT-SIBCAR-CROSSWALK-AUDIT-v1.md) | Parent finding FINDING-XW-SIBCAR-02 |

---

## 10. Register counts

| Metric | Count |
|--------|-------|
| Canonical state dimensions | **6** |
| Conflicting sources reviewed | **11 signals** across **6 docs** |
| Drift items | **6** |
| Execution prerequisites (blocking) | **8** |
| Doc sync prerequisites (non-blocking) | **3** |
| Sync actions recommended | **6** *(1 = no change needed)* |
| Blocking findings | **0** |

---

*OCPilot SITE-001 State Reconciliation Register v1 — documentation only.*
