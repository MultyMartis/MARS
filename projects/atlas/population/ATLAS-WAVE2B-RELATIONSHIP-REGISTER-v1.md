# ATLAS Wave 2B Relationship Register v1

**Status:** **attested** — canonical Person → Organization relationship roster after Wave 2B attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE2B-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, Person registry, org↔org registry.

---

## 1. Purpose

Канонический **реестр аттестированных Person → Organization relationships** после Wave 2B attestation act. Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Person → Organization) | **12** |
| Lifecycle **active** | **12** |
| Lifecycle deferred / proposed | **0** |
| Person endpoints without org edge (by design) | **2** (PER-0002, PER-0003) |
| Relationship families | Person → Organization only |

---

## 2. Attested roster — full table

| relationship_id | source_person | target_organization | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|---------------|---------------------|-------------------|-------------------|---------------|-----------------|-------|
| REL-0001 | PER-0001 Русецкий Андрей Анатольевич | ORG-0001 Веб-студия «Полигон» | **OWNER** | E0 operator + E1 CC EV-0003 (LE-0001) | E0 | **active** | Polygon anchor |
| REL-0002 | PER-0001 Русецкий Андрей Анатольевич | ORG-0002 Агентство «МетаКод» | **OWNER** | E0 operator + E1 CC EV-0003; MetaCode only Andrey | E0 | **active** | Partner isolation enforced |
| REL-0006 | PER-0011 Шваков Никита Алексеевич | ORG-0003 i-SEO Studio | **OWNER** | E1 `i-seo/requisites.txt` EV-0004; CC signatory | E1 | **active** | i-SEO owner |
| REL-0007 | PER-0007 Беслангурова Тамила | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + contacts; primary operational contact | E1 | **active** | Type: EMPLOYEE (2B override) |
| REL-0008 | PER-0008 Денис Леонов | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + PersonContacts EV-0004 | E1 | **active** | SEO specialist |
| REL-0009 | PER-0010 Дягилева Ольга | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + contacts; alias Оля | E1 | **active** | SEO specialist |
| REL-0010 | PER-0012 Илья Гуренков | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + PersonContacts | E1 | **active** | SEO specialist |
| REL-0011 | PER-0013 Иван Корольков | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + contacts; alias Ваня | E1 | **active** | SEO specialist |
| REL-0012 | PER-0009 Антон Кораблёв | ORG-0003 i-SEO Studio | **EMPLOYEE** | E1 CC + contacts; ME-W2-06 → EMPLOYEE | E1 | **active** | Developer |
| REL-0013 | PER-0004 Макарова Алеся Леонидовна | ORG-0004 Триумф | **REPRESENTATIVE** | E1 CC EV-0005 + CC-PER-01; primary contact | E1 | **active** | Client-side curator |
| REL-0014 | PER-0005 Подзолков Максим | ORG-0004 Триумф | **EMPLOYEE** | E1 CC + operator context; IT director | E1 | **active** | Type: EMPLOYEE (2B override) |
| REL-0015 | PER-0006 Вагин Иван Владимирович | ORG-0004 Триумф | **GENERAL_DIRECTOR** | E1 CC signatory LE-0003 EV-0005 | E1 | **active** | W2B-TAX-01: REPRESENTATIVE + role_qualifier |

---

## 3. Attested roster — by organization

### 3.1 ORG-0001 Полигон (1)

| relationship_id | source_person | relationship_type | evidence_tier | lifecycle_state |
|-----------------|---------------|-------------------|---------------|-----------------|
| REL-0001 | PER-0001 Русецкий Андрей Анатольевич | **OWNER** | E0 | **active** |

### 3.2 ORG-0002 MetaCode (1)

| relationship_id | source_person | relationship_type | evidence_tier | lifecycle_state |
|-----------------|---------------|-------------------|---------------|-----------------|
| REL-0002 | PER-0001 Русецкий Андрей Анатольевич | **OWNER** | E0 | **active** |

### 3.3 ORG-0003 i-SEO Studio (7)

| relationship_id | source_person | relationship_type | evidence_tier | lifecycle_state |
|-----------------|---------------|-------------------|---------------|-----------------|
| REL-0006 | PER-0011 Шваков Никита Алексеевич | **OWNER** | E1 | **active** |
| REL-0007 | PER-0007 Беслангурова Тамила | **EMPLOYEE** | E1 | **active** |
| REL-0008 | PER-0008 Денис Леонов | **EMPLOYEE** | E1 | **active** |
| REL-0009 | PER-0010 Дягилева Ольга | **EMPLOYEE** | E1 | **active** |
| REL-0010 | PER-0012 Илья Гуренков | **EMPLOYEE** | E1 | **active** |
| REL-0011 | PER-0013 Иван Корольков | **EMPLOYEE** | E1 | **active** |
| REL-0012 | PER-0009 Антон Кораблёв | **EMPLOYEE** | E1 | **active** |

### 3.4 ORG-0004 Триумф (3)

| relationship_id | source_person | relationship_type | evidence_tier | lifecycle_state |
|-----------------|---------------|-------------------|---------------|-----------------|
| REL-0013 | PER-0004 Макарова Алеся Леонидовна | **REPRESENTATIVE** | E1 | **active** |
| REL-0014 | PER-0005 Подзолков Максим | **EMPLOYEE** | E1 | **active** |
| REL-0015 | PER-0006 Вагин Иван Владимирович | **GENERAL_DIRECTOR** | E1 | **active** |

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **OWNER** | 3 | REL-0001, REL-0002, REL-0006 |
| **EMPLOYEE** | 7 | REL-0007, REL-0008, REL-0009, REL-0010, REL-0011, REL-0012, REL-0014 |
| **REPRESENTATIVE** | 1 | REL-0013 |
| **GENERAL_DIRECTOR** | 1 | REL-0015 *(taxonomy: REPRESENTATIVE + role_qualifier)* |

---

## 5. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| PER-0002 → any Organization | Moscow SERM Organization not populated; partner isolation | Future Organization wave |
| PER-0003 → any Organization | Metallka Organization not populated; partner isolation | Future Organization wave |
| REL-0003 PER-0001 MANAGER ORG-0003 | Not in operator-approved Wave 2B list | Future 2B extension or separate review |
| REL-0004 PER-0002 PARTNER PER-0001 | Person ↔ Person forbidden | **Rejected** |
| REL-0005 PER-0003 PARTNER PER-0001 | Person ↔ Person forbidden | **Rejected** |
| Sergey / Roman → ORG-0002 MetaCode | Operator correction | **Forbidden** |
| REL-0016 ORG-0004 CLIENT_OF ORG-0001 | Org ↔ Org out of 2B scope | **Wave 6** |
| REL-0017+ Project / Website / Domain edges | Wrong family / wave | **Wave 3+** |

---

## 6. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| E0 operator-direct | Steward / Owner attestation context | REL-0001, REL-0002 |
| EV-0003 | `polygon/`, `metacode/` CC (LE-0001) | REL-0001, REL-0002 |
| EV-0004 | `i-seo/requisites.txt` | REL-0006..REL-0012 |
| EV-0005 | `triumph/…2024.xlsx` | REL-0013, REL-0014, REL-0015 |
| PersonContacts sheet | Dataset contacts | REL-0007..REL-0012 corroboration |
| CC-PER-01 | Triumph name-to-CC-row mapping | REL-0013..REL-0015 |
| LE-0003 | ООО «Триумф» signatory | REL-0015 |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 7. Endpoint cross-reference

| Person | Attested org edges | Primary org (display) |
|--------|-------------------|----------------------|
| PER-0001 | REL-0001, REL-0002 | ORG-0001 |
| PER-0002 | *(none)* | **SAFE UNKNOWN** |
| PER-0003 | *(none)* | **SAFE UNKNOWN** |
| PER-0004 | REL-0013 | ORG-0004 |
| PER-0005 | REL-0014 | ORG-0004 |
| PER-0006 | REL-0015 | ORG-0004 |
| PER-0007 | REL-0007 | ORG-0003 |
| PER-0008 | REL-0008 | ORG-0003 |
| PER-0009 | REL-0012 | ORG-0003 |
| PER-0010 | REL-0009 | ORG-0003 |
| PER-0011 | REL-0006 | ORG-0003 |
| PER-0012 | REL-0010 | ORG-0003 |
| PER-0013 | REL-0011 | ORG-0003 |

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE2B-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md](ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md) | Person endpoints |
