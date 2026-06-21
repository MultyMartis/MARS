# ATLAS Wave 3B Project Relationship Register v1

**Status:** **attested** — canonical Project ↔ Organization relationship roster after Wave 3B attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, Website registry, org↔org registry.

---

## 1. Purpose

Канонический **реестр аттестированных Project ↔ Organization relationships** после Wave 3B attestation act. Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Project ↔ Organization) | **10** |
| Lifecycle **active** | **10** |
| Lifecycle deferred / proposed | **0** |
| Projects without org edges (by design) | **1** (PRJ-0001 MARS) |
| Relationship families | COMMISSIONED_BY, EXECUTES only |

---

## 2. Attested roster — full table

| relationship_id | source_id | target_id | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|-----------|-----------|-------------------|-------------------|---------------|-----------------|-------|
| REL-0017 | PRJ-0004 Редизайн gktriumph.ru | ORG-0004 Триумф | **COMMISSIONED_BY** | E1 dataset + WEB-0006; ORG-0004 active; PRJ-0004 deprecated | E1 | **active** | Historical commissioning — completed delivery |
| REL-0018 | ORG-0001 Веб-студия «Полигон» | PRJ-0004 Редизайн gktriumph.ru | **EXECUTES** | E1 dataset executor; ORG-0001 active; PRJ-0004 deprecated | E1 | **active** | Historical execution — completed delivery |
| REL-0019 | PRJ-0005 Грузотакси | ORG-0004 Триумф | **COMMISSIONED_BY** | E1 dataset + WEB-0008; ORG-0004 active; PRJ-0005 active | E1 | **active** | Ongoing client initiative |
| REL-0020 | ORG-0001 Полигон | PRJ-0005 Грузотакси | **EXECUTES** | E1 dataset executor; ORG-0001 active; PRJ-0005 active | E1 | **active** | Polygon delivery |
| REL-0021 | PRJ-0006 SEO gktriumph.ru | ORG-0004 Триумф | **COMMISSIONED_BY** | E1 dataset + WEB-0006; ORG-0004 active; PRJ-0006 active | E1 | **active** | SEO on main site |
| REL-0022 | ORG-0001 Полигон | PRJ-0006 SEO gktriumph.ru | **EXECUTES** | E1 dataset executor; ORG-0001 active; PRJ-0006 active | E1 | **active** | Polygon delivery org |
| REL-0023 | PRJ-0007 Блог gktriumph.ru | ORG-0004 Триумф | **COMMISSIONED_BY** | E1 dataset + WEB-0007; ORG-0004 active; PRJ-0007 active | E1 | **active** | Blog initiative |
| REL-0024 | ORG-0001 Полигон | PRJ-0007 Блог gktriumph.ru | **EXECUTES** | E1 dataset executor; ORG-0001 active; PRJ-0007 active | E1 | **active** | Polygon delivery |
| REL-0025 | PRJ-0008 Манипулятор | ORG-0004 Триумф | **COMMISSIONED_BY** | E1 dataset + WEB-0009; ORG-0004 active; PRJ-0008 active | E1 | **active** | Website Factory case |
| REL-0026 | ORG-0001 Полигон | PRJ-0008 Манипулятор | **EXECUTES** | E1 dataset executor; ORG-0001 active; PRJ-0008 active | E1 | **active** | Polygon delivery |

---

## 3. Attested roster — by project

### 3.1 PRJ-0004 Редизайн gktriumph.ru (deprecated)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-0017 | PRJ-0004 → ORG-0004 | **COMMISSIONED_BY** | E1 | **active** |
| REL-0018 | ORG-0001 → PRJ-0004 | **EXECUTES** | E1 | **active** |

### 3.2 PRJ-0005 Грузотакси (active)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-0019 | PRJ-0005 → ORG-0004 | **COMMISSIONED_BY** | E1 | **active** |
| REL-0020 | ORG-0001 → PRJ-0005 | **EXECUTES** | E1 | **active** |

### 3.3 PRJ-0006 SEO gktriumph.ru (active)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-0021 | PRJ-0006 → ORG-0004 | **COMMISSIONED_BY** | E1 | **active** |
| REL-0022 | ORG-0001 → PRJ-0006 | **EXECUTES** | E1 | **active** |

### 3.4 PRJ-0007 Блог gktriumph.ru (active)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-0023 | PRJ-0007 → ORG-0004 | **COMMISSIONED_BY** | E1 | **active** |
| REL-0024 | ORG-0001 → PRJ-0007 | **EXECUTES** | E1 | **active** |

### 3.5 PRJ-0008 Манипулятор (active)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-0025 | PRJ-0008 → ORG-0004 | **COMMISSIONED_BY** | E1 | **active** |
| REL-0026 | ORG-0001 → PRJ-0008 | **EXECUTES** | E1 | **active** |

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **COMMISSIONED_BY** | 5 | REL-0017, REL-0019, REL-0021, REL-0023, REL-0025 |
| **EXECUTES** | 5 | REL-0018, REL-0020, REL-0022, REL-0024, REL-0026 |

---

## 5. Attested roster — by organization

### 5.1 ORG-0004 Триумф — commissioning (5)

| relationship_id | source_project | relationship_type | evidence_tier | lifecycle_state |
|-----------------|----------------|-------------------|---------------|-----------------|
| REL-0017 | PRJ-0004 | **COMMISSIONED_BY** | E1 | **active** |
| REL-0019 | PRJ-0005 | **COMMISSIONED_BY** | E1 | **active** |
| REL-0021 | PRJ-0006 | **COMMISSIONED_BY** | E1 | **active** |
| REL-0023 | PRJ-0007 | **COMMISSIONED_BY** | E1 | **active** |
| REL-0025 | PRJ-0008 | **COMMISSIONED_BY** | E1 | **active** |

### 5.2 ORG-0001 Полигон — execution (5)

| relationship_id | target_project | relationship_type | evidence_tier | lifecycle_state |
|-----------------|----------------|-------------------|---------------|-----------------|
| REL-0018 | PRJ-0004 | **EXECUTES** | E1 | **active** |
| REL-0020 | PRJ-0005 | **EXECUTES** | E1 | **active** |
| REL-0022 | PRJ-0006 | **EXECUTES** | E1 | **active** |
| REL-0024 | PRJ-0007 | **EXECUTES** | E1 | **active** |
| REL-0026 | PRJ-0008 | **EXECUTES** | E1 | **active** |

---

## 6. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| PRJ-0001 MARS COMMISSIONED_BY | Internal strategic project — no external client | Internal governance decision |
| ORG-0002 MetaCode EXECUTES PRJ-0001 | Dataset executor — not operator-approved at 3B | Internal governance decision |
| REL-0016 ORG-0004 CLIENT_OF ORG-0001 | Org ↔ Org out of 3B scope | **Wave 6** |
| REL-0027 WEB-0006 → PRJ-0004 BELONGS_TO | Website ↔ Project family | **Wave 4** |
| REL-0028 WEB-0007 → PRJ-0007 BELONGS_TO | Website endpoints not attested | **Wave 4** |
| REL-0029 WEB-0008 → PRJ-0005 BELONGS_TO | Website endpoints not attested | **Wave 4** |
| REL-0030 WEB-0009 → PRJ-0008 BELONGS_TO | Website endpoints not attested | **Wave 4** |
| WEB-0006 → PRJ-0006 SEO BELONGS_TO | Not in dataset draft | **Wave 4 review** |
| Person → Project edges | Not in approved 3B list | Future expansion |

---

## 7. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| Dataset Projects sheet | [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | REL-0017..REL-0026 |
| Dataset Relationships sheet | Draft rel_ids REL-0017..0026 | ID continuity |
| EV-0005 | `triumph/…2024.xlsx` | REL-0017, 0019, 0021, 0023, 0025 (commissioning context) |
| EV-0003 | `polygon/` CC (LE-0001) | REL-0018, 0020, 0022, 0024, 0026 (executor org) |
| WEB-0006 | `https://gktriumph.ru` | REL-0017, REL-0021 |
| WEB-0007 | `https://blog.gktriumph.ru` | REL-0023 |
| WEB-0008 | `https://gruzotaxi-triumph.ru` | REL-0019 |
| WEB-0009 | `https://manipulator-triumph.ru` | REL-0025 |
| Wave 1 attestation | ORG-0001, ORG-0004 **active** | All edges |
| Wave 3 attestation | PRJ-0004..0008 endpoints | All edges |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 8. Endpoint cross-reference

| Project | COMMISSIONED_BY | EXECUTES | Project lifecycle |
|---------|-----------------|----------|-------------------|
| PRJ-0001 MARS | *(none)* | *(none)* | **active** — org edges **SAFE UNKNOWN** |
| PRJ-0004 | REL-0017 → ORG-0004 | REL-0018 ← ORG-0001 | **deprecated** |
| PRJ-0005 | REL-0019 → ORG-0004 | REL-0020 ← ORG-0001 | **active** |
| PRJ-0006 | REL-0021 → ORG-0004 | REL-0022 ← ORG-0001 | **active** |
| PRJ-0007 | REL-0023 → ORG-0004 | REL-0024 ← ORG-0001 | **active** |
| PRJ-0008 | REL-0025 → ORG-0004 | REL-0026 ← ORG-0001 | **active** |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md) | Person → Organization edges |
