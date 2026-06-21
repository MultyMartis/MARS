# ATLAS Foundation Risk Register v1

**Status:** Post-Phase-7 audit risk register (documentation only).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent audit:** [ATLAS-FOUNDATION-AUDIT-v1.md](ATLAS-FOUNDATION-AUDIT-v1.md)  
**Severity scale:** P0 (blocker) · P1 (high) · P2 (medium) · P3 (low)

---

## 1. Register summary

| Severity | Count | Action posture |
|----------|-------|----------------|
| **P0** | 0 | — |
| **P1** | 2 | Correct before population execution |
| **P2** | 6 | Correct before or during Stage A population |
| **P3** | 4 | Track; amend docs/index when convenient |

---

## 2. Risk entries

### R-ATLAS-P1-001 — OPS consumer ontology drift vs ATLAS MVP

| Field | Value |
|-------|-------|
| **Severity** | **P1** |
| **Category** | Boundary integrity · ecosystem |
| **Description** | [OPS-ATLAS-RELATIONSHIP-v1.md](../../ops/foundation/OPS-ATLAS-RELATIONSHIP-v1.md) lists ATLAS consumer classes **Clients, Contacts, Services, Agreements, Requisites** (C-01–C-08). ATLAS MVP taxonomy defines only **Organization, Person, Project, Website, Domain, Relationship**. No ATLAS foundation document defines Clients/Contacts/Services/Agreements/Requisites as entity classes. |
| **Impact** | OPS operators or integrators may create **parallel canonical concepts** or assume ATLAS will store requisites/agreements as core entities — boundary violation (E-11–E-13, E-26). |
| **Likelihood** | Medium — OPS foundation is active in repo |
| **Mitigation** | Map OPS logical classes to ATLAS MVP + relationships; amend OPS doc with explicit “logical view, not entity types”; attested attributes via expansion only |
| **Owner** | ATLAS program owner + OPS foundation maintainer |
| **Status** | Open |

---

### R-ATLAS-P1-002 — Population execution without Operational Model

| Field | Value |
|-------|-------|
| **Severity** | **P1** |
| **Category** | Governance · population |
| **Description** | Phase 7 defers steward roster, intake SLA, queue discipline, and STOP-03 capacity handling to **ATLAS Operational Model** ([ATLAS-POPULATION-STRATEGY-v1.md](../foundation/ATLAS-POPULATION-STRATEGY-v1.md) POP-O-02). Executing waves without this package risks **ad hoc ownership** and inconsistent attest quality. |
| **Impact** | Identity chaos (PR-01), mass **proposed** backlog (PR-07), uneven attest standards across waves |
| **Likelihood** | High if population starts under consumer pressure |
| **Mitigation** | Complete **ATLAS Operational Model** before Population Execution Planning; honor POP halt triggers |
| **Owner** | ATLAS program owner |
| **Status** | Open (expected deferral) |

---

### R-ATLAS-P2-001 — Stale Phase 1–2 “future relationship” narrative

| Field | Value |
|-------|-------|
| **Severity** | **P2** |
| **Category** | Consistency · semantic drift |
| **Description** | [ATLAS-REALITY-MODEL-v1.md](../foundation/ATLAS-REALITY-MODEL-v1.md) §5.2 and [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §6 state relationship type taxonomy is “future / not implemented.” Phase 2 delivered full taxonomy. |
| **Impact** | Stewards or consumers skip Phase 2/5; misconfigure intake as “links without types”; under-attest OWNER/CLIENT_OF |
| **Likelihood** | Medium for new readers |
| **Mitigation** | Foundation index + addendum footnotes; mandatory read order including Phase 2 taxonomy |
| **Owner** | ATLAS program owner |
| **Status** | Open |

---

### R-ATLAS-P2-002 — Import / consumer pressure for placeholder canonical

| Field | Value |
|-------|-------|
| **Severity** | **P2** |
| **Category** | Population · trust |
| **Description** | Documented risk PR-02, PR-08: pressure to mint `org-unknown-*` or parallel ids for exports ([ATLAS-REALITY-MODEL-v1.md](../foundation/ATLAS-REALITY-MODEL-v1.md) CR-10). |
| **Impact** | Permanent polluted graph; merge debt; consumer C3 reliance on false structure |
| **Likelihood** | High at first Factory/ORCA handoff |
| **Mitigation** | POP-P-03/04; steward STOP rules; certification gate C2+ |
| **Owner** | Registry steward |
| **Status** | Open (operational control) |

---

### R-ATLAS-P2-003 — Shadow canonical registries in consumers

| Field | Value |
|-------|-------|
| **Severity** | **P2** |
| **Category** | Consumer adoption |
| **Description** | CA-P04 / CERT downgrade triggers: parallel org/person/site lists marketed as canonical ([ATLAS-CONSUMER-CERTIFICATION-v1.md](../foundation/ATLAS-CONSUMER-CERTIFICATION-v1.md)). HomeGateway noted as broad-read shadow risk. |
| **Impact** | Semantic forks; reconciliation cost exceeds merge |
| **Likelihood** | Medium pre-implementation |
| **Mitigation** | C1 adoption statements; governance S4 incidents; population roadmap gates |
| **Owner** | Consumer program leads |
| **Status** | Open |

---

### R-ATLAS-P2-004 — MIG market evidence conflated with business existence

| Field | Value |
|-------|-------|
| **Severity** | **P2** |
| **Category** | Boundary · attestation |
| **Description** | AT-E-03: SERP packs support **proposal** only. MIG pilots generate rich market artifacts in repo (`incoming/mig/...`). |
| **Impact** | Auto-promotion of competitors/sites as canonical orgs |
| **Likelihood** | Medium during population Wave 4–6 |
| **Mitigation** | MAP-B08; population PR-06; steward boundary checklist |
| **Owner** | MIG + ATLAS steward |
| **Status** | Open |

---

### R-ATLAS-P2-005 — Relationship-before-endpoint active edges

| Field | Value |
|-------|-------|
| **Severity** | **P2** |
| **Category** | Population · relationships |
| **Description** | POP-P-03, EIR-R02, PR-03: active OWNER/CLIENT_OF without canonical endpoints. |
| **Impact** | Relationship chaos; disputed slots; irreversible consumer dependencies |
| **Likelihood** | Medium if Wave 6 accelerated |
| **Mitigation** | Wave order; POP-W-04 owner exception only; remain **proposed** |
| **Owner** | Registry steward |
| **Status** | Open (controlled by strategy) |

---

### R-ATLAS-P2-006 — Steward capacity exceeded (STOP-03)

| Field | Value |
|-------|-------|
| **Severity** | **P2** |
| **Category** | Operational |
| **Description** | [ATLAS-POPULATION-GOVERNANCE-v1.md](../foundation/ATLAS-POPULATION-GOVERNANCE-v1.md) STOP-03 references SLA breach — details deferred to Operational Model. |
| **Impact** | Proposed backlog; delayed dispute resolution; agent mass proposals (PR-07) |
| **Likelihood** | Medium at Stage A |
| **Mitigation** | Operational Model SLA; halt population; defer agent proposals |
| **Owner** | Program owner |
| **Status** | Open |

---

### R-ATLAS-P2-007 — CRM/ERP field bleed at intake

| Field | Value |
|-------|-------|
| **Severity** | **P2** |
| **Category** | Boundary |
| **Description** | PR-05; boundaries E-14, E-26. Import paths may carry pipeline/deal fields. |
| **Impact** | Canonical CRM semantics in ATLAS; boundary defect |
| **Likelihood** | Medium on first CRM import triage |
| **Mitigation** | Intake template; boundaries checklist §8; steward reject |
| **Owner** | Registry steward |
| **Status** | Open |

---

### R-ATLAS-P3-001 — No foundation navigation index

| Field | Value |
|-------|-------|
| **Severity** | **P3** |
| **Category** | Governance · documentation |
| **Description** | 31 documents without authoritative index / read order. |
| **Impact** | Slower audits; inconsistent steward training |
| **Likelihood** | High |
| **Mitigation** | `ATLAS-FOUNDATION-INDEX-v1.md` |
| **Owner** | ATLAS program owner |
| **Status** | Open |

---

### R-ATLAS-P3-002 — Registration log phase metadata lag

| Field | Value |
|-------|-------|
| **Severity** | **P3** |
| **Category** | Metadata |
| **Description** | [logs/atlas/atlas-registration-v1.md](../../logs/atlas/atlas-registration-v1.md) states Phase 1 complete only. |
| **Impact** | Ecosystem topology readers underestimate foundation maturity |
| **Likelihood** | Low |
| **Mitigation** | Update registration log phase label (docs only) |
| **Owner** | Program owner |
| **Status** | Open |

---

### R-ATLAS-P3-003 — Lifecycle code synonyms (`merged_into`, `split_from`)

| Field | Value |
|-------|-------|
| **Severity** | **P3** |
| **Category** | Consistency |
| **Description** | Phase 3 vs Phase 5 naming ([ATLAS-LIFECYCLE-CROSSWALK-v1.md](../foundation/ATLAS-LIFECYCLE-CROSSWALK-v1.md) §6.1–6.2). |
| **Impact** | Implementation enum duplication if migration aliases omitted |
| **Likelihood** | Low if crosswalk followed |
| **Mitigation** | Single enum module; alias map in implementation charter |
| **Owner** | Implementation lead (future) |
| **Status** | Open |

---

### R-ATLAS-P3-004 — Cosmetic “Future phase” tables in Phase 2 Relationship Model

| Field | Value |
|-------|-------|
| **Severity** | **P3** |
| **Category** | Documentation |
| **Description** | [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) §1 still lists Identity/Registry as “Future.” |
| **Impact** | Reader confusion only |
| **Likelihood** | Low |
| **Mitigation** | Footnote to Phase 3–4 |
| **Owner** | ATLAS program owner |
| **Status** | Open |

---

## 3. Risk–verdict linkage

| Verdict | Supporting risks |
|---------|------------------|
| **PARTIAL PASS** | P1-001, P1-002 prevent “clean PASS before execution”; no P0 |

---

## 4. Review cadence (recommended)

| Trigger | Action |
|---------|--------|
| Operational Model published | Re-score P1-002; close or downgrade |
| OPS mapping amended | Close P1-001 |
| Stage A population start | Review all P2 population risks |
| Semantic Contract amendment | Re-open consumer P2/P3 risks |

---

*ATLAS Foundation Risk Register v1 — documentation only.*
