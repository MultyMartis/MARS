# ATLAS Wave 3B Project Relationship Attestation v1

**Status:** **attested** — first official Project ↔ Organization relationship attestation set for ATLAS.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, Wave 4 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Wave 3 Project Population: **COMPLETE**
- Population verdict: **READY FOR WAVE 3B PROJECT RELATIONSHIP POPULATION**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** первого набора **Project ↔ Organization** relationships для Wave 3B: **10** записей переведены в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Project ↔ Organization → **active** | Person ↔ Project |
| COMMISSIONED_BY + EXECUTES only | Organization ↔ Organization |
| Triumph client delivery (PRJ-0004..0008) | PRJ-0001 MARS edges |
| Evidence tier per relationship | Website ↔ Project BELONGS_TO |
| Deprecated PRJ-0004 historical edges | Person ↔ Person |
| Wave 4 readiness statement | Runtime / API / database |

**Binding operator corrections (enforced):**

- **PRJ-0001 MARS** — no COMMISSIONED_BY / EXECUTES edges in this package.
- **REL-0016** CLIENT_OF — **не аттестирован**; Wave 6.
- **REL-0027..0030** BELONGS_TO — **не аттестированы**; Wave 4 coordination.
- Person → Project — **не создавать**.

---

## 2. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W3B-01** | REL-0017, REL-0018 | E1 dataset + WEB-0006; PRJ-0004 **deprecated**; ORG-0001, ORG-0004 **active** | **active** |
| **AT-W3B-02** | REL-0019, REL-0020 | E1 dataset + WEB-0008; PRJ-0005 **active** | **active** |
| **AT-W3B-03** | REL-0021, REL-0022 | E1 dataset + WEB-0006; PRJ-0006 **active** | **active** |
| **AT-W3B-04** | REL-0023, REL-0024 | E1 dataset + WEB-0007; PRJ-0007 **active** | **active** |
| **AT-W3B-05** | REL-0025, REL-0026 | E1 dataset + WEB-0009; PRJ-0008 **active** | **active** |

---

## 3. Per-relationship attestation records

### 3.1 PRJ-0004 — REL-0017, REL-0018

| Field | REL-0017 | REL-0018 |
|-------|----------|----------|
| **relationship_id** | REL-0017 | REL-0018 |
| **source_id** | PRJ-0004 Редизайн gktriumph.ru | ORG-0001 Веб-студия «Полигон» |
| **target_id** | ORG-0004 ООО «Триумф» | PRJ-0004 Редизайн gktriumph.ru |
| **relationship_type** | **COMMISSIONED_BY** | **EXECUTES** |
| **attestation_basis** | PRJ-0004 **deprecated** (Wave 3); ORG-0004 **active**; E1 dataset + WEB-0006; EV-0005 Triumph CC | ORG-0001 **active**; PRJ-0004 **deprecated**; E1 dataset executor field; REL-0001 delivery steward context |
| **evidence_tier** | **E1** | **E1** |
| **lifecycle_state** | **active** | **active** |
| **notes** | Historical commissioning — structural truth preserved | Historical execution — completed delivery |

### 3.2 PRJ-0005 — REL-0019, REL-0020

| Field | REL-0019 | REL-0020 |
|-------|----------|----------|
| **relationship_id** | REL-0019 | REL-0020 |
| **source_id** | PRJ-0005 Грузотакси | ORG-0001 Полигон |
| **target_id** | ORG-0004 Триумф | PRJ-0005 Грузотакси |
| **relationship_type** | **COMMISSIONED_BY** | **EXECUTES** |
| **attestation_basis** | PRJ-0005 **active**; ORG-0004 **active**; E1 dataset + WEB-0008; EV-0005 | ORG-0001 **active**; PRJ-0005 **active**; E1 dataset executor field |
| **evidence_tier** | **E1** | **E1** |
| **lifecycle_state** | **active** | **active** |
| **notes** | Ongoing client initiative | MIG pilot references container — not duplicate Project |

### 3.3 PRJ-0006 — REL-0021, REL-0022

| Field | REL-0021 | REL-0022 |
|-------|----------|----------|
| **relationship_id** | REL-0021 | REL-0022 |
| **source_id** | PRJ-0006 SEO gktriumph.ru | ORG-0001 Полигон |
| **target_id** | ORG-0004 Триумф | PRJ-0006 SEO gktriumph.ru |
| **relationship_type** | **COMMISSIONED_BY** | **EXECUTES** |
| **attestation_basis** | PRJ-0006 **active**; ORG-0004 **active**; E1 dataset; WEB-0006 main site | ORG-0001 **active**; PRJ-0006 **active**; E1 dataset executor field |
| **evidence_tier** | **E1** | **E1** |
| **lifecycle_state** | **active** | **active** |
| **notes** | SEO on main property — no separate Website entity | i-SEO operational participation — no Person→Project edge |

### 3.4 PRJ-0007 — REL-0023, REL-0024

| Field | REL-0023 | REL-0024 |
|-------|----------|----------|
| **relationship_id** | REL-0023 | REL-0024 |
| **source_id** | PRJ-0007 Блог gktriumph.ru | ORG-0001 Полигон |
| **target_id** | ORG-0004 Триумф | PRJ-0007 Блог gktriumph.ru |
| **relationship_type** | **COMMISSIONED_BY** | **EXECUTES** |
| **attestation_basis** | PRJ-0007 **active**; ORG-0004 **active**; E1 dataset + WEB-0007 | ORG-0001 **active**; PRJ-0007 **active**; E1 dataset executor field |
| **evidence_tier** | **E1** | **E1** |
| **lifecycle_state** | **active** | **active** |
| **notes** | Blog subsite initiative | WEB-0007 BELONGS_TO deferred Wave 4 |

### 3.5 PRJ-0008 — REL-0025, REL-0026

| Field | REL-0025 | REL-0026 |
|-------|----------|----------|
| **relationship_id** | REL-0025 | REL-0026 |
| **source_id** | PRJ-0008 Манипулятор | ORG-0001 Полигон |
| **target_id** | ORG-0004 Триумф | PRJ-0008 Манипулятор |
| **relationship_type** | **COMMISSIONED_BY** | **EXECUTES** |
| **attestation_basis** | PRJ-0008 **active**; ORG-0004 **active**; E1 dataset + WEB-0009; EV-0005 | ORG-0001 **active**; PRJ-0008 **active**; E1 dataset executor field |
| **evidence_tier** | **E1** | **E1** |
| **lifecycle_state** | **active** | **active** |
| **notes** | Website Factory / ORCA case | MARS delivery pack ≠ duplicate ATLAS Project |

---

## 4. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| PRJ-0001 MARS COMMISSIONED_BY | **Excluded** — SAFE UNKNOWN internal sponsor |
| ORG-0002 MetaCode EXECUTES PRJ-0001 | **Excluded** — internal governance decision required |
| REL-0016 ORG-0004 CLIENT_OF ORG-0001 | **Deferred** — Wave 6 |
| REL-0027..0030 Website → Project BELONGS_TO | **Deferred** — Wave 4 |
| WEB-0006 → PRJ-0006 SEO BELONGS_TO | **Deferred** — Wave 4 review |
| Person → Project edges | **Excluded** — future expansion |
| Person ↔ Person | **Rejected** |
| Organization ↔ Organization (other) | **Out of scope** |

---

## 5. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | 10 directed Project↔Org edges; paired COMMISSIONED_BY + EXECUTES — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §3 | COMMISSIONED_BY, EXECUTES in baseline — **Pass** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | All edges **active** post attestation — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints PRJ-* / ORG-* attested — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship state `active`; deprecated PRJ-0004 valid endpoint — **Pass** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | PRJ-0004 deprecated — historical edges valid — **Pass** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward path; dataset draft not substituted — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per relationship batch — **Pass** |

**Foundation modified:** **No**  
**Wave 1 / Wave 2 / Wave 2B / Wave 3 modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (Organization ↔ Project only)

---

## 6. Remaining SAFE UNKNOWN items

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W3B-01** | PRJ-0001 MARS COMMISSIONED_BY sponsor org | Medium for internal graph | Blocks MARS org edges only |
| **SU-W3B-02** | ORG-0002 MetaCode EXECUTES PRJ-0001 | Medium for internal graph | Blocks MARS org edges only |
| **SU-W3B-03** | REL-0016 CLIENT_OF ORG-0004 → ORG-0001 | Medium for commercial graph | Wave 6 |
| **SU-W3B-04** | WEB-0006 → PRJ-0006 SEO BELONGS_TO | Low | Wave 4 review candidate |
| **SU-W3B-05** | Person → Project participation edges | Low | Future expansion — not blocking Wave 4 |
| **SU-W3B-06** | i-SEO subcontractor role on PRJ-0006 | Low | Operational detail — EXECUTES remains ORG-0001 |

---

## 7. Wave 4 readiness assessment

### 7.1 Criteria

| Criterion | Status |
|-----------|--------|
| Wave 1 Organizations active (ORG-0001, ORG-0004) | **Pass** |
| Wave 3 Projects attested (PRJ-0004..0008) | **Pass** |
| Wave 3B COMMISSIONED_BY + EXECUTES for Triumph pilot | **Pass** — 10/10 attested |
| Project endpoints available for BELONGS_TO targets | **Pass** — PRJ-0004..0008 |
| MARS project edges correctly excluded | **Pass** |
| No Person→Project attested | **Pass** |
| Website entities not yet attested | **Expected** — Wave 4 scope |

### 7.2 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Structural graph insufficient for Website population |
| **PARTIALLY READY** | Wave 4 may start for subset only |
| **READY FOR WAVE 4 WEBSITE POPULATION** | Project + Project↔Org anchor complete for Triumph pilot |

### 7.3 Verdict

```text
READY FOR WAVE 4 WEBSITE POPULATION
```

**Conditions:**

1. Wave 4 executes as **separate population pass** — Website entities and Website-family relationships not bundled into 3B.
2. BELONGS_TO edges (REL-0027..0030) attested in Wave 4 or coordinated 3B Phase B per W3-R-03.
3. PRJ-0001 MARS org edges remain **SAFE UNKNOWN** until internal governance decision.
4. REL-0016 CLIENT_OF remains **Wave 6**.
5. Draft dataset relationship flags **do not substitute** for steward attestation acts.

---

## 8. Attestation verdict

```text
WAVE 3B PROJECT RELATIONSHIP ATTESTATION — COMPLETE
10 / 10 Project ↔ Organization relationships attested active
0 relationships deferred from approved 3B list
Wave 4 Website population — READY TO START
```

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Attested relationship roster |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md) | Project attestation prerequisite |
| [ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md) | Prior wave prerequisite |
| [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | Draft REL-* source ids |
