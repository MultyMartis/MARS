# ATLAS Wave 2B Relationship Attestation v1

**Status:** **attested** — first official Person → Organization relationship attestation set for ATLAS.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE2B-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE2-ATTESTATION-v1.md](ATLAS-WAVE2-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, Wave 3 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Attestation: **COMPLETE**
- Wave 2 Attestation: **COMPLETE**
- Population verdict: **READY FOR WAVE 2B RELATIONSHIP POPULATION**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** первого набора **Person → Organization** relationships для Wave 2B: **12** записей переведены в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Person → Organization → **active** | Person ↔ Person |
| Evidence tier per relationship | Organization entity attestation (Wave 1 — prior) |
| Type assignment per approved 2B list | Organization ↔ Organization |
| Partner / MANAGER exclusions | Project / Website / Domain edges |
| Wave 3 readiness statement | Runtime / API / database |

**Binding operator corrections (enforced):**

- MetaCode OWNER — **only** PER-0001 → ORG-0002.
- PER-0002 Сергей и PER-0003 Роман — **no** Person → Organization edges.
- REL-0004 / REL-0005 Person ↔ Person — **не аттестированы**.
- REL-0003 MANAGER (PER-0001 → ORG-0003) — **не в approved list**; не аттестирован.

---

## 2. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W2B-01** | REL-0001, REL-0002 | E0 PER-0001 + E1 CC EV-0003; ORG-0001, ORG-0002 active | **active** |
| **AT-W2B-02** | REL-0006 | E1 EV-0004; PER-0011 OWNER distinct from deferred MANAGER | **active** |
| **AT-W2B-03** | REL-0007..REL-0012 | E1 EV-0004 + PersonContacts; ME-W2-06 → EMPLOYEE | **active** |
| **AT-W2B-04** | REL-0013..REL-0015 | E1 EV-0005 + CC-PER-01; type overrides per approved list | **active** |

---

## 3. Per-relationship attestation records

### 3.1 Polygon — REL-0001

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0001 |
| **source_person** | PER-0001 Русецкий Андрей Анатольевич |
| **target_organization** | ORG-0001 Веб-студия «Полигон» |
| **relationship_type** | **OWNER** |
| **attestation_basis** | PER-0001 **active** (Wave 2); ORG-0001 **active** (Wave 1); E0 operator-direct ownership; E1 corroboration `polygon/ИП Русецкий А. А.pdf` (EV-0003, LE-0001) |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |

### 3.2 MetaCode — REL-0002

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0002 |
| **source_person** | PER-0001 Русецкий Андрей Анатольевич |
| **target_organization** | ORG-0002 Агентство «МетаКод» |
| **relationship_type** | **OWNER** |
| **attestation_basis** | PER-0001 **active**; ORG-0002 **active**; E0 operator correction MetaCode only Andrey; E1 `metacode/ИП Русецкий А. А.pdf` (EV-0003); exclusion verified: no PER-0002 / PER-0003 edge |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |

### 3.3 i-SEO — REL-0006 (owner)

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0006 |
| **source_person** | PER-0011 Шваков Никита Алексеевич |
| **target_organization** | ORG-0003 i-SEO Studio |
| **relationship_type** | **OWNER** |
| **attestation_basis** | PER-0011 **active**; ORG-0003 **active**; E1 `i-seo/requisites.txt` (EV-0004); CC signatory = Шваков (LE-0002) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |

### 3.4 i-SEO — team REL-0007..REL-0012

| relationship_id | source_person | target_organization | relationship_type | attestation_basis | evidence_tier | lifecycle_state |
|-----------------|---------------|---------------------|-------------------|-------------------|---------------|-----------------|
| REL-0007 | PER-0007 Беслангурова Тамила | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + contacts; primary operational contact; 2B type override (draft REPRESENTATIVE → EMPLOYEE) | E1 | **active** |
| REL-0008 | PER-0008 Денис Леонов | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + PersonContacts (EV-0004) | E1 | **active** |
| REL-0009 | PER-0010 Дягилева Ольга | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + contacts; alias Оля attested Wave 2 | E1 | **active** |
| REL-0010 | PER-0012 Илья Гуренков | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + PersonContacts | E1 | **active** |
| REL-0011 | PER-0013 Иван Корольков | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + contacts; alias Ваня attested Wave 2 | E1 | **active** |
| REL-0012 | PER-0009 Антон Кораблёв | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + contacts; ME-W2-06 resolved: EMPLOYEE (not CONTRACTOR) | E1 | **active** |

### 3.5 Triumph — REL-0013..REL-0015

| relationship_id | source_person | target_organization | relationship_type | attestation_basis | evidence_tier | lifecycle_state |
|-----------------|---------------|---------------------|-------------------|-------------------|---------------|-----------------|
| REL-0013 | PER-0004 Макарова Алеся Леонидовна | ORG-0004 Триумф | **REPRESENTATIVE** | E1 CC EV-0005; CC-PER-01; primary operational contact ORG-0004 | E1 | **active** |
| REL-0014 | PER-0005 Подзолков Максим | ORG-0004 Триумф | **EMPLOYEE** | E1 CC + operator context; IT director; 2B type override (draft REPRESENTATIVE → EMPLOYEE) | E1 | **active** |
| REL-0015 | PER-0006 Вагин Иван Владимирович | ORG-0004 Триумф | **GENERAL_DIRECTOR** | E1 CC signatory match LE-0003 ООО «Триумф» (EV-0005); генеральный директор | E1 | **active** |

**REL-0015 taxonomy alignment (W2B-TAX-01):** Operator label **GENERAL_DIRECTOR**; canonical taxonomy family **REPRESENTATIVE** (Person → Organization) with `role_qualifier: general_director` per [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §1 and RR-02.

---

## 4. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| PER-0002 → any Organization | **Excluded** — SAFE UNKNOWN org endpoint |
| PER-0003 → any Organization | **Excluded** — SAFE UNKNOWN org endpoint |
| REL-0003 PER-0001 MANAGER ORG-0003 | **Deferred** — not in approved 2B list |
| REL-0004 PER-0002 PARTNER PER-0001 | **Rejected** |
| REL-0005 PER-0003 PARTNER PER-0001 | **Rejected** |
| Sergey / Roman → ORG-0002 MetaCode | **Forbidden** |
| REL-0016 ORG-0004 CLIENT_OF ORG-0001 | **Deferred** — Wave 6 |
| REL-0017+ Project / Website / Domain | **Deferred** — Wave 3+ |

---

## 5. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | 12 directed Person→Org edges; multi-hat via independent REL-* — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) | OWNER, EMPLOYEE, REPRESENTATIVE in baseline — **Pass**; GENERAL_DIRECTOR via W2B-TAX-01 — **Pass with note** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | All edges **active** post attestation — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | All endpoints PER-* / ORG-* attested active — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship state `active` — **Pass** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward path; dataset draft not substituted — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per relationship batch — **Pass** |

**Foundation modified:** **No**  
**Wave 1 / Wave 2 modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (Person → Organization only)

---

## 6. Remaining SAFE UNKNOWN items

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W2B-01** | PER-0002 primary organization (Moscow SERM) | High for partner 2B | Blocks partner org edges only |
| **SU-W2B-02** | PER-0003 primary organization (Metallka) | High for partner 2B | Blocks partner org edges only |
| **SU-W2B-03** | REL-0003 MANAGER PER-0001 → ORG-0003 | Low | Optional future 2B extension |
| **SU-W2B-04** | Patronymic UNKNOWN (several i-SEO / Triumph persons) | Low | Not blocking relationships |
| **SU-W2B-05** | GENERAL_DIRECTOR taxonomy explicit type | Low | W2B-TAX-01 role qualifier sufficient for Wave 3 |
| **SU-W2B-06** | CLIENT_OF ORG-0004 → ORG-0001 (REL-0016) | Medium for commercial graph | Wave 6 |

---

## 7. Wave 3 readiness assessment

### 7.1 Criteria

| Criterion | Status |
|-----------|--------|
| Wave 1 Organizations active (ORG-0001..0004) | **Pass** (operator: Wave 1 complete) |
| Wave 2 Persons active (13/13) | **Pass** |
| Wave 2B Person→Org edges for anchor orgs | **Pass** — 12/12 attested |
| Partner persons isolated (no false org edges) | **Pass** |
| No Person↔Person attested | **Pass** |
| Sponsor / client org endpoints for Triumph pilot | **Pass** — ORG-0004 + REL-0013..0015 |
| Project edges deferred correctly | **Pass** — REL-0017+ not in 2B |

### 7.2 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Structural graph insufficient for Project population |
| **PARTIALLY READY** | Wave 3 may start for subset only |
| **READY FOR WAVE 3 PROJECT POPULATION** | Org + Person + Person→Org anchor complete |

### 7.3 Verdict

```text
READY FOR WAVE 3 PROJECT POPULATION
```

**Conditions:**

1. Wave 3 executes as **separate population pass** — Project entities and Project-family relationships not bundled into 2B.
2. PER-0002 and PER-0003 remain without org edges until dedicated Organization population.
3. REL-0016 CLIENT_OF and COMMISSIONED_BY edges remain **Wave 6 / Wave 3B** per execution plan.
4. W2B-TAX-01 (GENERAL_DIRECTOR) does not block Project intake.

---

## 8. Attestation verdict

```text
WAVE 2B RELATIONSHIP ATTESTATION — COMPLETE
12 / 12 Person → Organization relationships attested active
0 relationships deferred from approved 2B list
Wave 3 Project population — READY TO START
```

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md) | Attested relationship roster |
| [ATLAS-WAVE2B-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE2-ATTESTATION-v1.md](ATLAS-WAVE2-ATTESTATION-v1.md) | Person attestation prerequisite |
| [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | Draft REL-* source ids |
