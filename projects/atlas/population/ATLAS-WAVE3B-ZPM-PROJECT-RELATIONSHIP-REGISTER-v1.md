# ATLAS Wave 3B ZPM Project Relationship Register v1

**Status:** **attested** — canonical Project ↔ Organization relationship roster after Wave 3B ZPM attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ** · LE-0004  
**Parent:** [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, Website registry, org↔org registry.

---

## 1. Purpose

Канонический **реестр аттестированных Project ↔ Organization relationships** после Wave 3B ZPM attestation act. Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Project ↔ Organization, ZPM) | **4** |
| Lifecycle **active** | **4** |
| Lifecycle deferred / proposed | **0** |
| Relationship families | COMMISSIONED_BY, EXECUTES only |
| Project endpoints covered | **2** (PRJ-0009 **active**, PRJ-0010 **deprecated**) |

---

## 2. Attested roster — full table

| relationship_id | source_id | target_id | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|-----------|-----------|-------------------|-------------------|---------------|-----------------|-------|
| REL-ZPM-PJ-01 | PRJ-0009 Каталог-платформа bzpm.ru | ORG-0005 ЗПМ | **COMMISSIONED_BY** | E0 EV-ZPM-OP-ACT-01; ORG-0005 active; PRJ-0009 active | E0 | **active** | Ongoing catalog-platform commissioning |
| REL-ZPM-PJ-02 | ORG-0001 Полигон | PRJ-0009 Каталог-платформа bzpm.ru | **EXECUTES** | E0 EV-ZPM-OP-ACT-01; ORG-0001 active; PRJ-0009 active | E0 | **active** | Polygon active WIP delivery |
| REL-ZPM-PJ-03 | PRJ-0010 Сайт bzpm.ru (исходная версия) | ORG-0005 ЗПМ | **COMMISSIONED_BY** | E0 EV-ZPM-OP-HIST-01; ORG-0005 active; PRJ-0010 deprecated | E0 | **active** | Historical commissioning — completed delivery |
| REL-ZPM-PJ-04 | ORG-0001 Полигон | PRJ-0010 Сайт bzpm.ru (исходная версия) | **EXECUTES** | E0 EV-ZPM-OP-HIST-01; ORG-0001 active; PRJ-0010 deprecated | E0 | **active** | Historical execution — completed delivery |

---

## 3. Attested roster — by project

### 3.1 PRJ-0009 Каталог-платформа bzpm.ru (active)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-ZPM-PJ-01 | PRJ-0009 → ORG-0005 | **COMMISSIONED_BY** | E0 | **active** |
| REL-ZPM-PJ-02 | ORG-0001 → PRJ-0009 | **EXECUTES** | E0 | **active** |

### 3.2 PRJ-0010 Сайт bzpm.ru (исходная версия) (deprecated)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-ZPM-PJ-03 | PRJ-0010 → ORG-0005 | **COMMISSIONED_BY** | E0 | **active** |
| REL-ZPM-PJ-04 | ORG-0001 → PRJ-0010 | **EXECUTES** | E0 | **active** |

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **COMMISSIONED_BY** | 2 | REL-ZPM-PJ-01, REL-ZPM-PJ-03 |
| **EXECUTES** | 2 | REL-ZPM-PJ-02, REL-ZPM-PJ-04 |

---

## 5. Attested roster — by organization

### 5.1 ORG-0005 ЗПМ — commissioning (2)

| relationship_id | source_project | relationship_type | evidence_tier | lifecycle_state |
|-----------------|----------------|-------------------|---------------|-----------------|
| REL-ZPM-PJ-01 | PRJ-0009 | **COMMISSIONED_BY** | E0 | **active** |
| REL-ZPM-PJ-03 | PRJ-0010 | **COMMISSIONED_BY** | E0 | **active** |

### 5.2 ORG-0001 Полигон — execution (2)

| relationship_id | target_project | relationship_type | evidence_tier | lifecycle_state |
|-----------------|----------------|-------------------|---------------|-----------------|
| REL-ZPM-PJ-02 | PRJ-0009 | **EXECUTES** | E0 | **active** |
| REL-ZPM-PJ-04 | PRJ-0010 | **EXECUTES** | E0 | **active** |

---

## 6. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| WEB-* `bzpm.ru` | Website entity | **Wave 4** |
| DOM-* `bzpm.ru` | Domain entity | **Wave 5** |
| WEB → Project **BELONGS_TO** | Website ↔ Project family | **Wave 4B** |
| REL-0016 ORG-0005 CLIENT_OF ORG-0001 | Org ↔ Org out of 3B scope | **Wave 6** |
| Person → Project edges | Not in approved 3B-ZPM list | Future expansion |
| ZPM-INTAKE-FUT-01..04 | No start evidence | Future intake |

---

## 7. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| EV-ZPM-OP-ACT-01 | Operator statement — current catalog rebuild | REL-ZPM-PJ-01, REL-ZPM-PJ-02 |
| EV-ZPM-OP-HIST-01 | Operator statement — historical `bzpm.ru` delivery | REL-ZPM-PJ-03, REL-ZPM-PJ-04 |
| EV-W1B-CC-01 | `bzpm/Реквизиты.docx` | Org anchor indirect corroboration |
| AT-W1B-01 | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | ORG-0005 **active** — all COMMISSIONED_BY |
| AT-W3-ZPM-01 | [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) | PRJ-0009 **active** — REL-ZPM-PJ-01, 02 |
| AT-W3-ZPM-02 | Same | PRJ-0010 **deprecated** — REL-ZPM-PJ-03, 04 |
| Wave 1 attestation | ORG-0001 **active** | REL-ZPM-PJ-02, REL-ZPM-PJ-04 |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 8. Endpoint cross-reference

| Project | COMMISSIONED_BY | EXECUTES | Project lifecycle |
|---------|-----------------|----------|-------------------|
| PRJ-0009 | REL-ZPM-PJ-01 → ORG-0005 | REL-ZPM-PJ-02 ← ORG-0001 | **active** |
| PRJ-0010 | REL-ZPM-PJ-03 → ORG-0005 | REL-ZPM-PJ-04 ← ORG-0001 | **deprecated** |

**Cross-tranche note:** Triumph projects PRJ-0004..0008 retain separate COMMISSIONED_BY / EXECUTES edges (REL-0017..0026) via ORG-0004 — no conflict with ZPM graph.

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Core Wave 3B Triumph roster |
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md) | Person → Organization edges |

---

*ATLAS Wave 3B ZPM Project Relationship Register v1 — attested canonical roster.*
