# ATLAS Wave 4B SIBCAR Website Relationship Register v1

**Status:** **attested** — canonical Website-family relationship roster after Wave 4B SIBCAR attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR** · LE-0005  
**Parent:** [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, Domain registry, OPERATES registry.

---

## 1. Purpose

Канонический **реестр аттестированных Website-family relationships** после Wave 4B SIBCAR attestation act. Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Website family, SIBCAR) | **2** |
| BELONGS_TO (Website → Project) | **1** |
| OWNS (Organization → Website) | **1** |
| Lifecycle **active** | **2** |
| Lifecycle deferred / proposed | **0** |
| Multi-project websites | **0** — single Project on TEST hostname |
| Relationship families | BELONGS_TO, OWNS only |

---

## 2. Attested roster — full table

| relationship_id | source_id | target_id | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|-----------|-----------|-------------------|-------------------|---------------|-----------------|-------|
| REL-SIBCAR-WB-01 | WEB-SIBCAR-01 sibcar.new-site.space | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **BELONGS_TO** | E0 EV-W1C-02..03, EV-OCP-01..04; WEB-SIBCAR-01 active; PRJ-0011 active; REL-SIBCAR-PJ-01..02 | E0 | **active** | Sole TEST property grouped under PRJ-0011; EFV-03 |
| REL-SIBCAR-WB-02 | ORG-0006 SIBCAR | WEB-SIBCAR-01 sibcar.new-site.space | **OWNS** | E0 EV-W1C-02..03; ORG-0006 active; WEB-SIBCAR-01 active; EV-W1C-CC-01 org anchor | E0 | **active** | Structural client ownership — TEST deployment; not production registrant proof |

---

## 3. Attested roster — by website

### 3.1 WEB-SIBCAR-01 sibcar.new-site.space (TEST — single project)

| relationship_id | direction | relationship_type | evidence_tier | lifecycle_state |
|-----------------|-----------|-------------------|---------------|-----------------|
| REL-SIBCAR-WB-01 | WEB-SIBCAR-01 → PRJ-0011 | **BELONGS_TO** | E0 | **active** |
| REL-SIBCAR-WB-02 | ORG-0006 → WEB-SIBCAR-01 | **OWNS** | E0 | **active** |

**Website posture (unchanged):** `website_kind` **test_deployment** · environment **TEST** · canonical_name `sibcar.new-site.space`.

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **BELONGS_TO** | 1 | REL-SIBCAR-WB-01 |
| **OWNS** | 1 | REL-SIBCAR-WB-02 |

---

## 5. Attested roster — by project (BELONGS_TO inbound)

| project_id | project lifecycle | inbound BELONGS_TO | relationship_ids |
|------------|-------------------|--------------------|------------------|
| PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **active** | WEB-SIBCAR-01 | REL-SIBCAR-WB-01 |

---

## 6. Attested roster — by organization (OWNS outbound)

### 6.1 ORG-0006 SIBCAR — website ownership (1)

| relationship_id | target_website | relationship_type | evidence_tier | lifecycle_state |
|-----------------|----------------|-------------------|---------------|-----------------|
| REL-SIBCAR-WB-02 | WEB-SIBCAR-01 sibcar.new-site.space | **OWNS** | E0 | **active** |

---

## 7. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| ORG-0001 OPERATES WEB-SIBCAR-01 | Operations responsibility — separate governance | SAFE UNKNOWN |
| REL-0041 ORG-0006 CLIENT_OF ORG-0001 | Org ↔ Org — already attested | **Wave 6B** — not re-minted |
| DOM-* `sibcar.new-site.space` | Domain entity not populated | **Wave 5 SIBCAR** |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN | Domain family not populated | **Wave 5B SIBCAR** |
| Website → Domain | No Domain entities | **Wave 5** |
| Domain → Website | No Domain entities | **Wave 5** |
| Person → Website | Not in approved 4B-SIBCAR list | Future expansion |
| Person → Project | Not in approved 4B-SIBCAR list | Operator scope |
| Organization → Domain | No Domain entities | **Wave 5** |
| SIBCAR-INTAKE-WEB-02 production Website | Public URL **SAFE UNKNOWN** | **Blocked** — ME-W1C-02 |
| SIBCAR-INTAKE-FUT-03 PROD migration | No distinct boundary evidence | **Hold** |

---

## 8. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| EV-W1C-02 | OCPilot site-passport — SITE-001; TEST URL `sibcar.new-site.space` | REL-SIBCAR-WB-01, REL-SIBCAR-WB-02 |
| EV-W1C-03 | OCPilot project-access-brief — Business Goal; Planned Work | REL-SIBCAR-WB-01 |
| EV-OCP-01..04 | Intake complete; SITE-001 registry; pilot narrative | REL-SIBCAR-WB-01, REL-SIBCAR-WB-02 |
| EV-W1C-CC-01 | `sibcar/Реквизиты.docx` | REL-SIBCAR-WB-02 org anchor; indirect corroboration |
| AT-W4-SIBCAR-01 | [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) | WEB-SIBCAR-01 **active** — all edges |
| AT-W3-SIBCAR-01 | [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) | PRJ-0011 **active** — REL-SIBCAR-WB-01 |
| AT-W1C-01 | [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | ORG-0006 **active** — REL-SIBCAR-WB-02 |
| AT-W3B-SIBCAR-01 | [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | COMMISSIONED_BY / EXECUTES context — REL-SIBCAR-PJ-01..02 |
| AT-W6B-02 | [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | REL-0041 **active** — informational; not re-minted |

**Primary evidence paths:**

```text
E0 OCPilot — EV-W1C-02 (SITE-001; TEST URL https://sibcar.new-site.space/)
E0 OCPilot — EV-W1C-03 (PRJ-0011 Business Goal + Planned Work)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx (org anchor only)
```

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 9. Endpoint cross-reference

| Website | BELONGS_TO (outbound) | OWNS (inbound) | Website lifecycle | website_kind |
|---------|----------------------|----------------|-------------------|--------------|
| WEB-SIBCAR-01 sibcar.new-site.space | PRJ-0011 | ORG-0006 | **active** | **test_deployment** |

**Structural graph (attested):**

```text
ORG-0006 SIBCAR
    └── OWNS (REL-SIBCAR-WB-02)
        ▼
WEB-SIBCAR-01 sibcar.new-site.space
    └── BELONGS_TO (REL-SIBCAR-WB-01)
        ▼
PRJ-0011 Автосалон СИБКАР — OpenCart dealership
```

**Cross-tranche note:** Triumph websites WEB-0006..0009 and ZPM WEB-ZPM-01 retain separate Website-family edges — no conflict with SIBCAR graph.

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md) | Website endpoints |
| [ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Prior relationship wave |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | ZPM tranche structural precedent |

---

*ATLAS Wave 4B SIBCAR Website Relationship Register v1 — attested canonical roster.*
