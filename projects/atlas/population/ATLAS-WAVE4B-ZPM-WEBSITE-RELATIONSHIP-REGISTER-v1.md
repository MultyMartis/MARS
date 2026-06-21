# ATLAS Wave 4B ZPM Website Relationship Register v1

**Status:** **attested** — canonical Website-family relationship roster after Wave 4B ZPM attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ** · LE-0004  
**Parent:** [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, Domain registry, OPERATES registry.

---

## 1. Purpose

Канонический **реестр аттестированных Website-family relationships** после Wave 4B ZPM attestation act. Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Website family, ZPM) | **3** |
| BELONGS_TO (Website → Project) | **2** |
| OWNS (Organization → Website) | **1** |
| Lifecycle **active** | **3** |
| Lifecycle deferred / proposed | **0** |
| Multi-project websites | **1** (WEB-ZPM-01) |
| Relationship families | BELONGS_TO, OWNS only |
| Cancelled (not in register) | **1** (REL-ZPM-WB-02) |

---

## 2. Attested roster — full table

| relationship_id | source_id | target_id | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|-----------|-----------|-------------------|-------------------|---------------|-----------------|-------|
| REL-ZPM-WB-01 | WEB-ZPM-01 bzpm.ru | PRJ-0009 Каталог-платформа bzpm.ru | **BELONGS_TO** | E0 EV-ZPM-OP-ACT-01; WEB-ZPM-01 active; PRJ-0009 active; REL-ZPM-PJ-01 | E0 | **active** | Ongoing catalog-platform initiative grouping |
| REL-ZPM-WB-03 | WEB-ZPM-01 bzpm.ru | PRJ-0010 Сайт bzpm.ru (исходная версия) | **BELONGS_TO** | E0 EV-ZPM-OP-HIST-01; WEB-ZPM-01 active; PRJ-0010 deprecated; LT-P01; COR-ZPM-WEB-07 | E0 | **active** | Multi-project case — historical deliverable on same property |
| REL-ZPM-WB-04 | ORG-0005 ЗПМ | WEB-ZPM-01 bzpm.ru | **OWNS** | E0 EV-ZPM-OP-ACT-01; ORG-0005 active; WEB-ZPM-01 active; EV-W1B-CC-01; COR-ZPM-WEB-09 | E0 | **active** | Structural client ownership — sole ZPM web property |

---

## 3. Attested roster — by website

### 3.1 WEB-ZPM-01 bzpm.ru (corporate — multi-project)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-ZPM-WB-01 | WEB-ZPM-01 → PRJ-0009 | **BELONGS_TO** | E0 | **active** |
| REL-ZPM-WB-03 | WEB-ZPM-01 → PRJ-0010 | **BELONGS_TO** | E0 | **active** |
| REL-ZPM-WB-04 | ORG-0005 → WEB-ZPM-01 | **OWNS** | E0 | **active** |

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **BELONGS_TO** | 2 | REL-ZPM-WB-01, REL-ZPM-WB-03 |
| **OWNS** | 1 | REL-ZPM-WB-04 |

---

## 5. Attested roster — by project (BELONGS_TO inbound)

| project_id | project lifecycle | inbound BELONGS_TO | relationship_ids |
|------------|-------------------|--------------------|------------------|
| PRJ-0009 Каталог-платформа bzpm.ru | **active** | WEB-ZPM-01 | REL-ZPM-WB-01 |
| PRJ-0010 Сайт bzpm.ru (исходная версия) | **deprecated** | WEB-ZPM-01 | REL-ZPM-WB-03 |

---

## 6. Attested roster — by organization (OWNS outbound)

### 6.1 ORG-0005 ЗПМ — website ownership (1)

| relationship_id | target_website | relationship_type | evidence_tier | lifecycle_state |
|-----------------|----------------|-------------------|---------------|-----------------|
| REL-ZPM-WB-04 | WEB-ZPM-01 bzpm.ru | **OWNS** | E0 | **active** |

---

## 7. Cancelled register (not in attested set)

| relationship_id | Prior draft | Reason |
|-----------------|-------------|--------|
| REL-ZPM-WB-02 | WEB-ZPM-02 → PRJ-0010 **BELONGS_TO** | **Cancelled** — COR-ZPM-WEB-06; source Website WEB-ZPM-02 retired (COR-ZPM-WEB-01) |

---

## 8. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| ORG-0001 OPERATES WEB-ZPM-01 | Operations responsibility — separate governance | SAFE UNKNOWN |
| REL-0016 ORG-0005 CLIENT_OF ORG-0001 | Org ↔ Org out of 4B scope | **Wave 6** |
| DOM-* `bzpm.ru` | Domain entity not populated | **Wave 5 ZPM** |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN | Domain family not populated | **Wave 5B ZPM** |
| Website → Domain | No Domain entities | **Wave 5** |
| Domain → Website | No Domain entities | **Wave 5** |
| Person → Website (PER-0014, PER-0015) | Not in approved 4B-ZPM list | Future expansion |
| Person → Project | Not in approved 4B-ZPM list | Operator scope |
| Organization → Domain | No Domain entities | **Wave 5** |
| WEB-ZPM-02 | Retired — not minted | COR-ZPM-WEB-01 |
| ZPM-INTAKE-FUT-01..04 | No start evidence | Future intake |

---

## 9. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| EV-ZPM-OP-ACT-01 | Operator statement — current catalog rebuild | REL-ZPM-WB-01, REL-ZPM-WB-04 |
| EV-ZPM-OP-HIST-01 | Operator statement — historical `bzpm.ru` delivery | REL-ZPM-WB-03 |
| EV-W1B-CC-01 | `bzpm/Реквизиты.docx` §17 | REL-ZPM-WB-04 org anchor; indirect hostname corroboration |
| AT-W4-ZPM-01 | [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) | WEB-ZPM-01 **active** — all edges |
| AT-W3-ZPM-01 | [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) | PRJ-0009 **active** — REL-ZPM-WB-01 |
| AT-W3-ZPM-02 | Same | PRJ-0010 **deprecated** — REL-ZPM-WB-03 |
| AT-W1B-01 | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | ORG-0005 **active** — REL-ZPM-WB-04 |
| AT-W3B-ZPM-01..02 | [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | COMMISSIONED_BY context — REL-ZPM-PJ-01, REL-ZPM-PJ-03 |
| COR-ZPM-WEB-01..12 | [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | Single Website model; REL-ZPM-WB-03 queue; REL-ZPM-WB-02 cancel |
| Triumph precedent | REL-0027, REL-0028, REL-0032 | Multi-project BELONGS_TO + OWNS pattern |

**Primary evidence paths:**

```text
E0 operator — EV-ZPM-OP-ACT-01 (REL-ZPM-WB-01, REL-ZPM-WB-04)
E0 operator — EV-ZPM-OP-HIST-01 (REL-ZPM-WB-03)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx
```

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 10. Endpoint cross-reference

| Website | BELONGS_TO (outbound) | OWNS (inbound) | Website lifecycle |
|---------|----------------------|----------------|-------------------|
| WEB-ZPM-01 bzpm.ru | PRJ-0009, PRJ-0010 | ORG-0005 | **active** |

**Cross-tranche note:** Triumph websites WEB-0006..0009 retain separate Website-family edges (REL-0027..0035) via ORG-0004 — no conflict with ZPM graph.

**Triumph analog:**

| Triumph | ZPM |
|---------|-----|
| WEB-0006 → PRJ-0004 (deprecated) | WEB-ZPM-01 → PRJ-0010 (deprecated) |
| WEB-0006 → PRJ-0006 (active) | WEB-ZPM-01 → PRJ-0009 (active) |
| ORG-0004 → WEB-0006 **OWNS** | ORG-0005 → WEB-ZPM-01 **OWNS** |

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | Website endpoints |
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Prior relationship wave |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Core Wave 4B Triumph roster |

---

*ATLAS Wave 4B ZPM Website Relationship Register v1 — attested canonical roster.*
