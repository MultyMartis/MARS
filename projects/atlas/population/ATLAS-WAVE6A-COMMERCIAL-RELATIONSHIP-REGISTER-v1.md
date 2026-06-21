# ATLAS Wave 6A Commercial Relationship Register v1

**Status:** **attested** — canonical Organization ↔ Organization commercial relationship roster after Wave 6A attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, Person registry, Project registry, full org↔org historical catalog.

---

## 1. Purpose

Канонический **реестр аттестированных Organization ↔ Organization commercial relationships** после Wave 6A attestation act. Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Organization → Organization) | **1** |
| Lifecycle **active** | **1** |
| Lifecycle deferred / proposed | **0** |
| Relationship types | **CLIENT_OF** only |
| Organization endpoints in commercial graph | **2** (ORG-0001, ORG-0004) |

---

## 2. Attested roster — full table

| relationship_id | source_organization | target_organization | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|---------------------|---------------------|-------------------|-------------------|---------------|-----------------|-------|
| REL-0016 | ORG-0004 ООО «Триумф» | ORG-0001 Веб-студия «Полигон» | **CLIENT_OF** | E1 dataset REL-0016 + Wave 3B project corroboration + EV-0005 / EV-0003 + operator commercial reality | E1 | **active** | Triumph = client; Polygon = vendor; first org↔org commercial edge |

---

## 3. Attested roster — by organization

### 3.1 ORG-0001 Веб-студия «Полигон» (vendor object)

| relationship_id | source_organization | relationship_type | evidence_tier | lifecycle_state | role |
|-----------------|---------------------|-------------------|---------------|-----------------|------|
| REL-0016 | ORG-0004 Триумф | **CLIENT_OF** (inbound) | E1 | **active** | Vendor / service provider |

### 3.2 ORG-0004 ООО «Триумф» (client subject)

| relationship_id | target_organization | relationship_type | evidence_tier | lifecycle_state | role |
|-----------------|---------------------|-------------------|---------------|-----------------|------|
| REL-0016 | ORG-0001 Полигон | **CLIENT_OF** (outbound) | E1 | **active** | Client |

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **CLIENT_OF** | 1 | REL-0016 |

---

## 5. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| ORG-0001 → **VENDOR_OF** → ORG-0004 | Inverse mirror not in approved 6A list | **Not created** — CLIENT_OF sufficient |
| **PARTNER_OF** (any approved org pair) | No attested peer partnership | Future review |
| **SUPPLIER_OF** (any pair) | Out of Wave 6A scope | Future review |
| ORG-0002 MetaCode commercial edges | No operator-approved candidate | Future 6A extension |
| ORG-0003 i-SEO commercial edges | No operator-approved candidate | Future 6A extension |
| W1-C latent client orgs → ORG-0001 | Organization not populated | Future Organization + 6A |
| Moscow SERM / Metallka → any vendor | Organization not populated | Future waves |
| **FORMER_CLIENT_OF** REL-0016 | Relationship ongoing | N/A |

---

## 6. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| Dataset draft | `ATLAS-WAVE1-DATASET-v0.4.xlsx` Relationships REL-0016 | REL-0016 type, direction, endpoints |
| EV-0005 | `triumph/…2024.xlsx` | REL-0016 client endpoint (ORG-0004) |
| EV-0003 | `polygon/ИП Русецкий А. А.pdf` (LE-0001) | REL-0016 vendor endpoint (ORG-0001) |
| Wave 3B register | REL-0017..0026 | REL-0016 commercial direction corroboration |
| Operator intake | Wave 6A approved reality | REL-0016 E0 overlay |
| LE-0001 | ИП Русецкий А. А. (Polygon legal entity context) | ORG-0001 endpoint |
| LE-0003 | ООО «Триумф» (Triumph legal entity context) | ORG-0004 endpoint |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 7. Endpoint cross-reference

| Organization | Commercial edges (outbound CLIENT_OF) | Commercial edges (inbound — as vendor) | Non-commercial context (reference only) |
|--------------|--------------------------------------|----------------------------------------|----------------------------------------|
| ORG-0001 Полигон | *(none attested)* | REL-0016 ← ORG-0004 | REL-0001 OWNER; REL-0018..0026 EXECUTES |
| ORG-0004 Триумф | REL-0016 → ORG-0001 | *(none attested)* | REL-0013..0015 Person edges; REL-0017..0025 COMMISSIONED_BY; REL-0032..0035 OWNS |

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Project-level commercial corroboration |
| [ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md) | Person → Organization anchor graph |
