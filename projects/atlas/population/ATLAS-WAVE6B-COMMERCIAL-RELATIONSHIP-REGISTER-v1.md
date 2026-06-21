# ATLAS Wave 6B Commercial Relationship Register v1

**Status:** **attested** — canonical Organization ↔ Organization commercial relationship roster after Wave 6B attestation (ZPM + SIBCAR expansion).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md)  
**Is not:** runtime export, database table, Person registry, Project registry, full org↔org historical catalog.

---

## 1. Purpose

Канонический **реестр аттестированных Organization ↔ Organization commercial relationships** после Wave 6B attestation act. Включает REL-0016 (Wave 6A) и новые рёбра REL-0040, REL-0041. Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Organization → Organization) | **3** |
| Added in Wave 6B | **2** (REL-0040, REL-0041) |
| Lifecycle **active** | **3** |
| Lifecycle deferred / proposed | **0** |
| Relationship types | **CLIENT_OF** only |
| Organization endpoints in commercial graph | **4** (ORG-0001, ORG-0004, ORG-0005, ORG-0006) |
| Polygon inbound CLIENT_OF (as vendor) | **3** |

---

## 2. Attested roster — full table

| relationship_id | source_organization | target_organization | relationship_type | attestation_basis | evidence_tier | lifecycle_state | wave | notes |
|-----------------|---------------------|---------------------|-------------------|-------------------|---------------|-----------------|------|-------|
| REL-0016 | ORG-0004 ООО «Триумф» | ORG-0001 Веб-студия «Полигон» | **CLIENT_OF** | E1 dataset REL-0016 + Wave 3B + EV-0005 / EV-0003 + operator commercial reality | E1 | **active** | 6A | Triumph = client; first org↔org commercial edge |
| REL-0040 | ORG-0005 ЗПМ | ORG-0001 Веб-студия «Полигон» | **CLIENT_OF** | E1 EV-W1B-CC-01 + Wave 3B-ZPM + Wave 4B + operator commercial reality | E1 | **active** | 6B | ЗПМ = client; full stack corroboration |
| REL-0041 | ORG-0006 SIBCAR | ORG-0001 Веб-студия «Полигон» | **CLIENT_OF** | E1 EV-W1C-CC-01 + W1-C CLIENT role + Polygon channel + operator commercial reality | E1 | **active** | 6B | SIBCAR = client; project corroboration absent |

---

## 3. Attested roster — by organization

### 3.1 ORG-0001 Веб-студия «Полигон» (vendor object)

| relationship_id | source_organization | relationship_type | evidence_tier | lifecycle_state | role |
|-----------------|---------------------|-------------------|---------------|-----------------|------|
| REL-0016 | ORG-0004 Триумф | **CLIENT_OF** (inbound) | E1 | **active** | Vendor / service provider |
| REL-0040 | ORG-0005 ЗПМ | **CLIENT_OF** (inbound) | E1 | **active** | Vendor / service provider |
| REL-0041 | ORG-0006 SIBCAR | **CLIENT_OF** (inbound) | E1 | **active** | Vendor / service provider |

### 3.2 ORG-0004 ООО «Триумф» (client subject)

| relationship_id | target_organization | relationship_type | evidence_tier | lifecycle_state | role |
|-----------------|---------------------|-------------------|---------------|-----------------|------|
| REL-0016 | ORG-0001 Полигон | **CLIENT_OF** (outbound) | E1 | **active** | Client |

### 3.3 ORG-0005 ЗПМ (client subject)

| relationship_id | target_organization | relationship_type | evidence_tier | lifecycle_state | role |
|-----------------|---------------------|-------------------|---------------|-----------------|------|
| REL-0040 | ORG-0001 Полигон | **CLIENT_OF** (outbound) | E1 | **active** | Client |

### 3.4 ORG-0006 SIBCAR (client subject)

| relationship_id | target_organization | relationship_type | evidence_tier | lifecycle_state | role |
|-----------------|---------------------|-------------------|---------------|-----------------|------|
| REL-0041 | ORG-0001 Полигон | **CLIENT_OF** (outbound) | E1 | **active** | Client |

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **CLIENT_OF** | 3 | REL-0016, REL-0040, REL-0041 |

---

## 5. Direction consistency matrix

| client_org | vendor_org | relationship_id | direction vs REL-0016 | status |
|------------|------------|-----------------|-------------------------|--------|
| ORG-0004 Триумф | ORG-0001 Полигон | REL-0016 | **Reference** | **active** |
| ORG-0005 ЗПМ | ORG-0001 Полигон | REL-0040 | **Identical** | **active** |
| ORG-0006 SIBCAR | ORG-0001 Полигон | REL-0041 | **Identical** | **active** |

```text
CLIENT ──CLIENT_OF──► VENDOR

ORG-0004 ──CLIENT_OF──► ORG-0001
ORG-0005 ──CLIENT_OF──► ORG-0001
ORG-0006 ──CLIENT_OF──► ORG-0001
```

---

## 6. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| ORG-0001 → **VENDOR_OF** → clients | Inverse mirror not in approved list | **Not created** |
| **PARTNER_OF** / **SUPPLIER_OF** (any approved org pair) | No attested peer partnership | Future review |
| ORG-0007 Makita → ORG-0003 i-SEO **CLIENT_OF** | E0 channel — separate intake | Future commercial pass |
| ORG-0002 / ORG-0003 commercial org↔org edges | No operator-approved candidate | Future extension |
| Moscow SERM / Metallka → any vendor | Organization not populated | Future waves |
| **FORMER_CLIENT_OF** (any attested edge) | Relationships ongoing | N/A |
| Invented contract / invoice evidence | Evidence First — forbidden | N/A |

---

## 7. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| Dataset draft | `ATLAS-WAVE1-DATASET-v0.4.xlsx` Relationships REL-0016 | REL-0016 type, direction, endpoints |
| EV-0005 | `triumph/…2024.xlsx` | REL-0016 client endpoint (ORG-0004) |
| EV-0003 | `polygon/ИП Русецкий А. А.pdf` (LE-0001) | Vendor endpoint (ORG-0001) — all three edges |
| EV-W1B-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx` | REL-0040 client endpoint (ORG-0005) |
| EV-W1C-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | REL-0041 client endpoint (ORG-0006) |
| Wave 3B register | REL-0017..0026 | REL-0016 commercial direction corroboration |
| Wave 3B-ZPM register | REL-ZPM-PJ-01..04 | REL-0040 commercial direction corroboration |
| Wave 4B-ZPM register | REL-ZPM-WB-04 | REL-0040 client property context |
| EV-ZPM-OP-ACT-01 / EV-ZPM-OP-HIST-01 | Operator statements | REL-0040 delivery context |
| Operator intake | Wave 6A + Wave 6B approved reality | E0 overlay — all CLIENT_OF edges |
| LE-0001 | ИП Русецкий А. А. | ORG-0001 vendor context |
| LE-0003 | ООО «Триумф» | ORG-0004 client context |
| LE-0004 | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | ORG-0005 client context |
| LE-0005 | ООО «СибКар» | ORG-0006 client context |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 8. Endpoint cross-reference

| Organization | Commercial edges (outbound CLIENT_OF) | Commercial edges (inbound — as vendor) | Non-commercial context (reference only) |
|--------------|--------------------------------------|----------------------------------------|----------------------------------------|
| ORG-0001 Полигон | *(none attested)* | REL-0016 ← ORG-0004; REL-0040 ← ORG-0005; REL-0041 ← ORG-0006 | REL-0001 OWNER; REL-0018..0026 EXECUTES; REL-ZPM-PJ-02, 04 EXECUTES |
| ORG-0004 Триумф | REL-0016 → ORG-0001 | *(none attested)* | REL-0013..0015 Person; REL-0017..0025 COMMISSIONED_BY; REL-0032..0035 OWNS |
| ORG-0005 ЗПМ | REL-0040 → ORG-0001 | *(none attested)* | REL-ZPM-01, 02 Person; REL-ZPM-PJ-01, 03 COMMISSIONED_BY; REL-ZPM-WB-04 OWNS |
| ORG-0006 SIBCAR | REL-0041 → ORG-0001 | *(none attested)* | *(no attested Project / Website / Domain edges)* |

---

## 9. Commercial graph summary (post Wave 6B)

| Metric | Before 6B | After 6B |
|--------|-----------|----------|
| CLIENT_OF edges to ORG-0001 | 1 | **3** |
| Active Polygon clients (commercial graph) | ORG-0004 | ORG-0004, ORG-0005, ORG-0006 |
| Commercial coverage (attested client orgs) | 1/3 W1-B/C clients | **3/3** |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | Prior register baseline |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | ZPM project corroboration |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) | SIBCAR org anchor |
