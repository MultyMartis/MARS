# ATLAS Wave 3B SIBCAR Project Relationship Register v1

**Status:** **attested** — canonical Project ↔ Organization relationship roster after Wave 3B SIBCAR attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR** · LE-0005  
**Parent:** [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, Website registry, org↔org registry.

---

## 1. Purpose

Канонический **реестр аттестированных Project ↔ Organization relationships** после Wave 3B SIBCAR attestation act. Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Project ↔ Organization, SIBCAR) | **2** |
| Lifecycle **active** | **2** |
| Lifecycle deferred / proposed | **0** |
| Relationship families | COMMISSIONED_BY, EXECUTES only |
| Project endpoints covered | **1** (PRJ-0011 **active**) |

---

## 2. Attested roster — full table

| relationship_id | source_id | target_id | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|-----------|-----------|-------------------|-------------------|---------------|-----------------|-------|
| REL-SIBCAR-PJ-01 | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | ORG-0006 SIBCAR | **COMMISSIONED_BY** | E0 EV-W1C-02..03, EV-OCP-01..04; ORG-0006 active; PRJ-0011 active | E0 | **active** | Ongoing OpenCart dealership commissioning |
| REL-SIBCAR-PJ-02 | ORG-0001 Полигон | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **EXECUTES** | E0 EV-W1C-03; ORG-0001 active; PRJ-0011 active; REL-0041 vendor context | E0 | **active** | Polygon active WIP delivery |

---

## 3. Attested roster — by project

### 3.1 PRJ-0011 Автосалон СИБКАР — OpenCart dealership (active)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-SIBCAR-PJ-01 | PRJ-0011 → ORG-0006 | **COMMISSIONED_BY** | E0 | **active** |
| REL-SIBCAR-PJ-02 | ORG-0001 → PRJ-0011 | **EXECUTES** | E0 | **active** |

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **COMMISSIONED_BY** | 1 | REL-SIBCAR-PJ-01 |
| **EXECUTES** | 1 | REL-SIBCAR-PJ-02 |

---

## 5. Attested roster — by organization

### 5.1 ORG-0006 SIBCAR — commissioning (1)

| relationship_id | source_project | relationship_type | evidence_tier | lifecycle_state |
|-----------------|----------------|-------------------|---------------|-----------------|
| REL-SIBCAR-PJ-01 | PRJ-0011 | **COMMISSIONED_BY** | E0 | **active** |

### 5.2 ORG-0001 Полигон — execution (1)

| relationship_id | target_project | relationship_type | evidence_tier | lifecycle_state |
|-----------------|----------------|-------------------|---------------|-----------------|
| REL-SIBCAR-PJ-02 | PRJ-0011 | **EXECUTES** | E0 | **active** |

---

## 6. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| WEB-* `sibcar.new-site.space` | Website entity | **Wave 4** |
| DOM-* TEST hostname | Domain entity | **Wave 5** |
| WEB → Project **BELONGS_TO** (REL-SIBCAR-WB-01) | Website ↔ Project family | **Wave 4B** |
| REL-0041 ORG-0006 CLIENT_OF ORG-0001 | **Already attested** — Wave 6B | **Complete** |
| Person → Project edges | Not in approved 3B-SIBCAR list | Future expansion |
| SIBCAR-INTAKE-FUT-01..03 | No distinct boundary evidence | Future intake |

---

## 7. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| EV-W1C-02 | OCPilot site-passport — SITE-001; TEST URL | REL-SIBCAR-PJ-01, REL-SIBCAR-PJ-02 |
| EV-W1C-03 | OCPilot project-access-brief — Business Goal + Planned Work | REL-SIBCAR-PJ-01, REL-SIBCAR-PJ-02 |
| EV-OCP-01..04 | OCPilot intake / registry / pilot narrative | REL-SIBCAR-PJ-01, REL-SIBCAR-PJ-02 |
| EV-W1C-CC-01 | `sibcar\Реквизиты.docx` | Org anchor indirect corroboration |
| AT-W1C-01 | [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | ORG-0006 **active** — REL-SIBCAR-PJ-01 |
| AT-W3-SIBCAR-01 | [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) | PRJ-0011 **active** — both edges |
| AT-W6B-02 | [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | REL-0041 vendor context — REL-SIBCAR-PJ-02 |
| Wave 1 attestation | ORG-0001 **active** | REL-SIBCAR-PJ-02 |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 8. Endpoint cross-reference

| Project | COMMISSIONED_BY | EXECUTES | Project lifecycle |
|---------|-----------------|----------|-------------------|
| PRJ-0011 | REL-SIBCAR-PJ-01 → ORG-0006 | REL-SIBCAR-PJ-02 ← ORG-0001 | **active** |

**Cross-tranche note:** Triumph projects (REL-0017..0026), ZPM projects (REL-ZPM-PJ-01..04), and commercial REL-0041 retain separate namespaces — no conflict with SIBCAR project graph.

**Commercial complement:**

| relationship_id | family | status |
|-----------------|--------|--------|
| REL-0041 | ORG-0006 → ORG-0001 **CLIENT_OF** | **active** (Wave 6B) |
| REL-SIBCAR-PJ-01 | PRJ-0011 → ORG-0006 **COMMISSIONED_BY** | **active** (this register) |
| REL-SIBCAR-PJ-02 | ORG-0001 → PRJ-0011 **EXECUTES** | **active** (this register) |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | ZPM tranche precedent |
| [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | REL-0041 commercial context |

---

*ATLAS Wave 3B SIBCAR Project Relationship Register v1 — attested canonical roster.*
