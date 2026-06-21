# ATLAS Wave 3 Project Attestation v1

**Status:** **documented** — Wave 3 Project attestation sequence, evidence gates, readiness verdict.  
**Attestation authority note (FINDING-INT-03):** Core Triumph Project lifecycle (PRJ-0004..0008) is **active** / **deprecated** in population registers and attested as relationship endpoints in [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md). No standalone `*-ACTIVE-ATTESTATION-v1.md` was filed for this tranche. **SAFE UNKNOWN:** whether discrete steward acts AT-W3-01..03 were executed as separate human steps before Wave 3B — not separately documented.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-PROJECT-POPULATION-v1.md) · [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md)  
**Is not:** attestation runtime, signature platform, relationship attestation, Wave 3B execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Population verdict: **READY FOR WAVE 3 PROJECT POPULATION**

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 3 Project, минимальные evidence gates, readiness по каждому проекту, missing evidence, candidate relationships для Wave 3B, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 3 attestation scope

| In scope | Out of scope |
|----------|--------------|
| Project entity → **proposed** / **active** / **deprecated** | COMMISSIONED_BY / EXECUTES edges |
| Evidence tier assignment per project | Website entity attestation (Wave 4) |
| Lifecycle structural state (no PM vocabulary) | BELONGS_TO edges (Wave 3B) |
| MARS program exclusion enforcement | Domain entities (Wave 5) |
| Wave 3B **queue preparation** | Person ↔ Project edges |
| Deprecated completed delivery (PRJ-0004) | Foundation amendments |

Wave 3B relationship **active** attestation executes in a **separate pass** after Project endpoints are **active** or **deprecated** (structural retire — still valid endpoint for historical edges).

---

## 3. Attestation readiness by project

| project_id | Project | Target state | Min tier | Readiness | Blocker |
|------------|---------|--------------|----------|-----------|---------|
| PRJ-0001 | MARS | **active** | E0 | **Ready** | — |
| PRJ-0004 | Редизайн gktriumph.ru | **deprecated** | E1 | **Ready** | — |
| PRJ-0005 | Грузотакси | **active** | E1 | **Ready** | — |
| PRJ-0006 | SEO gktriumph.ru | **active** | E1 | **Ready** | — |
| PRJ-0007 | Блог gktriumph.ru | **active** | E1 | **Ready** | — |
| PRJ-0008 | Манипулятор | **active** | E1 | **Ready** | — |

**Readiness legend:**

- **Ready** — steward may attest Project to target lifecycle state now.
- All six projects: **Ready** — no conditional blockers.

---

## 4. Attestation sequence

### 4.1 Tranche AT-W3-01 — Internal anchor

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify MARS ≠ MARS `project_id` registry row (E-17) | Steward | `registry/project-registry.md`, Population §5 |
| 2 | Propose PRJ-0001 canonical name **MARS** | Steward | Dataset + E0 |
| 3 | Assign E0; note internal initiative — no external commissioner | Steward | Operator-direct |
| 4 | Attest Project **active** | Steward (delegated) or Owner | Rationale: long-term strategic container |
| 5 | Queue 3B: EXECUTES candidate ORG-0002 — steward review | Steward | Dataset executor field |

### 4.2 Tranche AT-W3-02 — Triumph completed delivery

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify ORG-0004, ORG-0001 **active** (Wave 1) | Steward | Wave 1 exit |
| 2 | Propose PRJ-0004 | Steward | Dataset + WEB-0006 |
| 3 | Confirm completed delivery — **deprecated** not `done` | Steward | LT-P01 |
| 4 | Attest Project **deprecated** at E1 | Steward | Operator note + live site |

### 4.3 Tranche AT-W3-03 — Triumph active delivery (batch)

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Propose PRJ-0005..0008 | Steward | Dataset Projects + Websites |
| 2 | Verify commissioning ORG-0004, execution ORG-0001 context | Steward | Wave 1 + 2B |
| 3 | Assign E1 per project | Steward | WEB-0007..0009, gktriumph.ru |
| 4 | Attest **active** — PRJ-0005, 0006, 0007, 0008 | Steward | No PM status fields |
| 5 | Queue 3B: REL-0019..0026, REL-0027..0030 | Steward | Population §6 |

---

## 5. Lifecycle attestation rules (Wave 3)

| Rule ID | Rule | Enforcement |
|---------|------|-------------|
| **W3-LC-01** | Completed delivery → **deprecated** | PRJ-0004 |
| **W3-LC-02** | Ongoing work → **active** | PRJ-0005..0008 |
| **W3-LC-03** | Internal initiative → **active** | PRJ-0001 |
| **W3-LC-04** | Forbidden: `completed`, `closed`, `done`, task states | All |
| **W3-LC-05** | Deprecated project + active website allowed | PRJ-0004 + WEB-0006 |

---

## 6. Missing evidence register

| ID | Project | Gap | Severity | Mitigation |
|----|---------|-----|----------|------------|
| **ME-W3-01** | PRJ-0001 | No COMMISSIONED_BY sponsor org | Low | **SAFE UNKNOWN** — internal; no edge required |
| **ME-W3-02** | PRJ-0001 | EXECUTES org ORG-0001 vs ORG-0002 | Low | Steward resolves at Wave 3B |
| **ME-W3-03** | PRJ-0006 | No WEB→PRJ BELONGS_TO in dataset | Low | Candidate edge at 3B — SEO on main site |
| **ME-W3-04** | PRJ-0005 | MIG pilot not executed | Low | E1 site evidence sufficient; MIG = support only |
| **ME-W3-05** | All Triumph | Contract/invoice primary path | — | OAR-BAN-01 — structural E1 sufficient |

**No blocking gaps.**

---

## 7. Readiness checklist crosswalk

| Check ID | Wave 3 Project package assessment |
|----------|-----------------------------------|
| W3-S-01 | Org anchor stable (ORG-0001..0004 active) | **Pass** |
| W3-S-02 | Project vs Organization boundary | **Pass** |
| W3-S-03 | MARS `project_id` disambiguation | **Pass** — Population §5 |
| W3-E-01 | E0–E1 structural attest path | **Pass** |
| W3-E-02 | Triumph pilot separate from org CC | **Pass** — PRJ-0005 ≠ ORG-0004 |
| W3-E-03 | MIG artifacts = proposal support only | **Pass** |
| W3-E-04 | Sponsor org reference available | **Pass** — ORG-0004 for Triumph; PRJ-0001 SAFE UNKNOWN |
| W3-D-01 | Project name collision with org names | **Pass** |
| W3-D-02 | Pilot vs production naming separated | **Pass** |
| W3-D-03 | MIG pack ≠ auto Project | **Pass** |
| W3-I-01 | PRJ-* mint rules reviewed | **Pass** |
| W3-I-02 | Not Jira/PM semantics | **Pass** |
| W3-R-01 | COMMISSIONED_BY / BELONGS_TO deferred | **Pass** — Wave 3B queue |
| W3-R-02 | Sponsor org identified per project | **Pass** |
| W3-R-03 | Website links deferred | **Pass** |

---

## 8. Wave 3B readiness assessment

### 8.1 Candidate relationship inventory

| Family | Count | Draft rel_ids | Endpoint prerequisite |
|--------|-------|---------------|----------------------|
| Project → Org **COMMISSIONED_BY** | 5 | REL-0017, 0019, 0021, 0023, 0025 | Project + ORG-0004 **active/deprecated** |
| Org → Project **EXECUTES** | 5–6 | REL-0018, 0020, 0022, 0024, 0026 + PRJ-0001 TBD | Project + ORG-0001 **active** |
| Website → Project **BELONGS_TO** | 4 (+1 candidate) | REL-0027..0030; PRJ-0006 TBD | Website Wave 4 or proposed policy |

### 8.2 Wave 3B prerequisites

| Prerequisite | Status |
|--------------|--------|
| ORG-0001, ORG-0004 active (Wave 1) | **Met** |
| Person endpoints for context (Wave 2) | **Met** |
| Project population defined (Wave 3) | **Met** (this package) |
| Project attestation act executed | **Pending steward** — gates pass |
| Website endpoints for BELONGS_TO | **Partial** — Wave 4; COMMISSIONED_BY/EXECUTES may proceed first |

---

## 9. Final verdict

### 9.1 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Wave 3 Project intake cannot start |
| **PARTIALLY READY** | Subset only; documented blockers |
| **READY FOR WAVE 3 PROJECT ATTESTATION** | Full Project intake plan executable |
| **READY FOR WAVE 3B PROJECT RELATIONSHIP POPULATION** | Project population complete; 3B relationship pass may proceed |

### 9.2 Assessment

| Criterion | Status |
|-----------|--------|
| All 6 required projects classified | **Pass** |
| MARS programs excluded (E-17) | **Pass** |
| Lifecycle states per LT-P01 | **Pass** |
| Org endpoints available (ORG-0001, 0002, 0004) | **Pass** |
| Evidence paths documented (E0/E1) | **Pass** |
| Foundation consistency — no new entity types | **Pass** |
| Known gaps enumerated (ME-W3-01..05) | **Pass** — none blocking |
| Wave 3B candidates prepared | **Pass** — REL-0017..0030 |

### 9.3 Verdict

```text
READY FOR WAVE 3B PROJECT RELATIONSHIP POPULATION
```

**Conditions:**

1. Steward executes attestation tranches AT-W3-01..03 to promote six projects from population draft to canonical **active** / **deprecated** before Wave 3B **active** relationship promotion.
2. Wave 3B **Phase A** (COMMISSIONED_BY + EXECUTES) may start immediately after Project attestation act.
3. Wave 3B **Phase B** (BELONGS_TO) coordinates with Wave 4 Website population — or **proposed** website edges per steward policy (W3-R-03).
4. MARS program registry rows remain **outside** ATLAS Project namespace — no retroactive mint.
5. Draft dataset lifecycle flags **do not substitute** for steward attestation acts.

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-PROJECT-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Project roster |
| [ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md) | Prior wave prerequisite |
| [ATLAS-POPULATION-READINESS-CHECKLIST-v1.md](../foundation/ATLAS-POPULATION-READINESS-CHECKLIST-v1.md) | W3 check IDs |
