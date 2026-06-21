# ATLAS Wave 4B Website Relationship Register v1

**Status:** **attested** — canonical Website relationship roster after Wave 4B attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, Domain registry, OPERATES registry.

---

## 1. Purpose

Канонический **реестр аттестированных Website-family relationships** после Wave 4B attestation act. Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Website family) | **9** |
| BELONGS_TO (Website → Project) | **5** |
| OWNS (Organization → Website) | **4** |
| Lifecycle **active** | **9** |
| Lifecycle deferred / proposed | **0** |
| Multi-project websites | **1** (WEB-0006) |
| Relationship families | BELONGS_TO, OWNS only |

---

## 2. Attested roster — full table

| relationship_id | source_id | target_id | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|-----------|-----------|-------------------|-------------------|---------------|-----------------|-------|
| REL-0027 | WEB-0006 gktriumph.ru | PRJ-0004 Редизайн gktriumph.ru | **BELONGS_TO** | E1 dataset + live URL; WEB-0006 active; PRJ-0004 deprecated; REL-0017 | E1 | **active** | Redesign deliverable grouping |
| REL-0028 | WEB-0006 gktriumph.ru | PRJ-0006 SEO gktriumph.ru | **BELONGS_TO** | E1 dataset + operator approval; WEB-0006 active; PRJ-0006 active; REL-0021 | E1 | **active** | Multi-project case — SEO on main site |
| REL-0029 | WEB-0007 blog.gktriumph.ru | PRJ-0007 Блог gktriumph.ru | **BELONGS_TO** | E1 dataset; WEB-0007 active; PRJ-0007 active; REL-0023 | E1 | **active** | Blog subsite initiative |
| REL-0030 | WEB-0008 gruzotaxi-triumph.ru | PRJ-0005 Грузотакси | **BELONGS_TO** | E1 dataset + live URL; WEB-0008 active; PRJ-0005 active; REL-0019 | E1 | **active** | Landing property |
| REL-0031 | WEB-0009 manipulator-triumph.ru | PRJ-0008 Манипулятор | **BELONGS_TO** | E1 dataset + live URL; WEB-0009 active; PRJ-0008 active; REL-0025 | E1 | **active** | Website Factory case |
| REL-0032 | ORG-0004 ООО «Триумф» | WEB-0006 gktriumph.ru | **OWNS** | E1 dataset + EV-0005; ORG-0004 active; WEB-0006 active | E1 | **active** | Structural client ownership |
| REL-0033 | ORG-0004 Триумф | WEB-0007 blog.gktriumph.ru | **OWNS** | E1 dataset; ORG-0004 active; WEB-0007 active | E1 | **active** | Blog subsite ownership |
| REL-0034 | ORG-0004 Триумф | WEB-0008 gruzotaxi-triumph.ru | **OWNS** | E1 dataset + EV-0005; ORG-0004 active; WEB-0008 active | E1 | **active** | Landing ownership |
| REL-0035 | ORG-0004 Триумф | WEB-0009 manipulator-triumph.ru | **OWNS** | E1 dataset + EV-0005; ORG-0004 active; WEB-0009 active | E1 | **active** | Landing ownership |

---

## 3. Attested roster — by website

### 3.1 WEB-0006 gktriumph.ru (corporate — multi-project)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-0027 | WEB-0006 → PRJ-0004 | **BELONGS_TO** | E1 | **active** |
| REL-0028 | WEB-0006 → PRJ-0006 | **BELONGS_TO** | E1 | **active** |
| REL-0032 | ORG-0004 → WEB-0006 | **OWNS** | E1 | **active** |

### 3.2 WEB-0007 blog.gktriumph.ru (blog)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-0029 | WEB-0007 → PRJ-0007 | **BELONGS_TO** | E1 | **active** |
| REL-0033 | ORG-0004 → WEB-0007 | **OWNS** | E1 | **active** |

### 3.3 WEB-0008 gruzotaxi-triumph.ru (landing)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-0030 | WEB-0008 → PRJ-0005 | **BELONGS_TO** | E1 | **active** |
| REL-0034 | ORG-0004 → WEB-0008 | **OWNS** | E1 | **active** |

### 3.4 WEB-0009 manipulator-triumph.ru (landing)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-0031 | WEB-0009 → PRJ-0008 | **BELONGS_TO** | E1 | **active** |
| REL-0035 | ORG-0004 → WEB-0009 | **OWNS** | E1 | **active** |

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **BELONGS_TO** | 5 | REL-0027, REL-0028, REL-0029, REL-0030, REL-0031 |
| **OWNS** | 4 | REL-0032, REL-0033, REL-0034, REL-0035 |

---

## 5. Attested roster — by project (BELONGS_TO inbound)

| project_id | project lifecycle | inbound BELONGS_TO | relationship_ids |
|------------|-------------------|--------------------|------------------|
| PRJ-0004 Редизайн | **deprecated** | WEB-0006 | REL-0027 |
| PRJ-0005 Грузотакси | **active** | WEB-0008 | REL-0030 |
| PRJ-0006 SEO | **active** | WEB-0006 | REL-0028 |
| PRJ-0007 Блог | **active** | WEB-0007 | REL-0029 |
| PRJ-0008 Манипулятор | **active** | WEB-0009 | REL-0031 |

---

## 6. Attested roster — by organization (OWNS outbound)

### 6.1 ORG-0004 Триумф — website ownership (4)

| relationship_id | target_website | relationship_type | evidence_tier | lifecycle_state |
|-----------------|----------------|-------------------|---------------|-----------------|
| REL-0032 | WEB-0006 gktriumph.ru | **OWNS** | E1 | **active** |
| REL-0033 | WEB-0007 blog.gktriumph.ru | **OWNS** | E1 | **active** |
| REL-0034 | WEB-0008 gruzotaxi-triumph.ru | **OWNS** | E1 | **active** |
| REL-0035 | WEB-0009 manipulator-triumph.ru | **OWNS** | E1 | **active** |

---

## 7. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| ORG-0001 OPERATES WEB-0006..0009 | Operations responsibility — separate governance | SAFE UNKNOWN |
| REL-0016 ORG-0004 CLIENT_OF ORG-0001 | Org ↔ Org out of 4B scope | **Wave 6** |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN | Domain family not populated | **Wave 5 + 6C** |
| Website → Domain | No Domain entities | **Wave 5** |
| Domain → Website | No Domain entities | **Wave 5** |
| Person → Website | Not in approved 4B list | Future expansion |
| WEB-0001..0005 operator sites | Separate tranche | Future wave |

---

## 8. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| Dataset Websites sheet | [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | REL-0027, 0029..0031; OWNS context |
| Dataset Projects sheet | Same | REL-0028 (PRJ-0006); BELONGS_TO targets |
| Dataset Relationships sheet | Draft REL-0027..0030 (renumbered at 4B) | ID continuity |
| EV-0005 | `triumph/…2024.xlsx` | REL-0032, 0034, 0035; Triumph client context |
| WEB-0006 | `https://gktriumph.ru` | REL-0027, 0028, 0032 |
| WEB-0007 | `https://blog.gktriumph.ru` | REL-0029, 0033 |
| WEB-0008 | `https://gruzotaxi-triumph.ru` | REL-0030, 0034 |
| WEB-0009 | `https://manipulator-triumph.ru` | REL-0031, 0035 |
| Wave 4 Website attestation | WEB-0006..0009 **active** | All edges |
| Wave 3B register | REL-0017..0026 COMMISSIONED_BY / EXECUTES | Cross-check |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 9. Endpoint cross-reference

| Website | BELONGS_TO (outbound) | OWNS (inbound) | Website lifecycle |
|---------|----------------------|----------------|-------------------|
| WEB-0006 | PRJ-0004, PRJ-0006 | ORG-0004 | **active** |
| WEB-0007 | PRJ-0007 | ORG-0004 | **active** |
| WEB-0008 | PRJ-0005 | ORG-0004 | **active** |
| WEB-0009 | PRJ-0008 | ORG-0004 | **active** |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | Website endpoints |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Prior relationship wave |
