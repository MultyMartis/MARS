# ATLAS Wave 1D Shpigovsky Organization Register v1

**Status:** **documented** — canonical Organization roster for Wave 1D Shpigovsky tranche.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Parent:** [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md) · [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md)  
**Is not:** LegalEntities attested export, runtime registry, database table, relationship register.

---

## 1. Purpose

Канонический **реестр Organization population** Wave 1D — tranche **Shpigovsky (ООО «Сознание»)**. Одна строка — одна attested Organization record at **E1/E2 operational-public** evidence tier.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Wave tier W1-D | **1** |
| Classification Polygon client | **1** |
| Target **active** | **1** |
| Legal entity | **0** — **SAFE UNKNOWN** |
| Attestation readiness | **ready** |

---

## 2. Population roster — full table

| org_id | canonical_name | wave_tier | classification | business_role | legal_entity_id | legal_entity_name | inn | kpp | ogrn_ogrnip | aliases | primary_website | primary_domain | evidence_tier | lifecycle_state | attestation_ref | notes |
|--------|----------------|-----------|----------------|---------------|-----------------|-------------------|-----|-----|-------------|---------|-----------------|----------------|---------------|-----------------|-----------------|-------|
| ORG-0008 | **ООО «Сознание»** | **W1-D** | **Polygon client** | **CLIENT** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | *(none attested)* | **SAFE UNKNOWN** *(candidate: shpigovsky.ru)* | **SAFE UNKNOWN** *(candidate: shpigovsky.ru)* | **E1/E2** *(operational-public)* | **active** | AT-W1D-SHPIG-01 | Brand: Шпиговский Дом; OOEP Category A; no CC; LE deferred |

---

## 3. Brand notes register *(not separate Organization)*

| org_id | brand_label | relationship_to_org | evidence_ref | separate_org? |
|--------|-------------|---------------------|--------------|---------------|
| ORG-0008 | **Шпиговский Дом** | Trade / public brand | EV-SHPIG-WEB-01 | **No** |
| ORG-0008 | Центр профилактики зависимостей Сергея Шпиговского | Positioning descriptor | EV-SHPIG-WEB-01 | **No** |

**Rule:** Brand labels recorded in **notes** only — **not** attested aliases; **not** separate `ORG-*`.

---

## 4. Legal entity index

**No Legal Entity rows minted in Wave 1D Shpigovsky.**

| legal_entity_id | status | notes |
|-----------------|--------|-------|
| LE-* | **Not created** | **SAFE UNKNOWN** until E1+ CC or E2 registry extract with identifiers |

**Deferred fields (explicit):**

| Field | Value |
|-------|-------|
| Legal entity | **SAFE UNKNOWN** |
| INN | **SAFE UNKNOWN** |
| KPP | **SAFE UNKNOWN** |
| OGRN | **SAFE UNKNOWN** |
| Legal signatory | **SAFE UNKNOWN** |
| EDO | **SAFE UNKNOWN** |
| Ownership structure | **SAFE UNKNOWN** |
| Contract data | **SAFE UNKNOWN** |
| Internal contacts | **SAFE UNKNOWN** |

**Note:** LE-0001..0005 attested in prior waves (Wave 1, 1B, 1C). **No LE-0006+** created for Shpigovsky.

---

## 5. Operational context register *(informational — not PER-* / REL-* mint)*

| org_id | context_field | value | person_id | evidence_ref | attestation_state |
|--------|---------------|-------|-----------|--------------|-------------------|
| ORG-0008 | acquisition | Ольга Дягилева | PER-0010 *(reference only)* | EV-SHPIG-OP-01 | informational |
| ORG-0008 | delivery_org | ORG-0001 Полигон | — | EV-SHPIG-OP-01 | informational |
| ORG-0008 | channel | Polygon client delivery | — | EV-SHPIG-OP-01 | informational |
| ORG-0008 | i-SEO project | **Excluded** | — | EV-SHPIG-OP-01 | informational |

---

## 6. Candidate asset register *(not WEB-* / DOM-* mint)*

### 6.1 Website candidates

| org_id | candidate_label | URL | hostname | web_id | evidence_ref | wave |
|--------|-----------------|-----|----------|--------|--------------|------|
| ORG-0008 | shpigovsky.ru (homepage) | https://shpigovsky.ru/ | shpigovsky.ru | **none** | EV-SHPIG-WEB-01 | Wave 4 |
| ORG-0008 | shpigovsky.ru (policy) | https://shpigovsky.ru/policy | shpigovsky.ru | **none** | EV-SHPIG-WEB-02 | Wave 4 |
| ORG-0008 | shpigovsky.ru (psy) | https://shpigovsky.ru/psy | shpigovsky.ru | **none** | EV-SHPIG-WEB-01 | Wave 4 |
| ORG-0008 | shpigovsky.ru (home) | https://shpigovsky.ru/home | shpigovsky.ru | **none** | EV-SHPIG-WEB-01 | Wave 4 |

### 6.2 Domain candidates

| org_id | candidate_label | fqdn | dom_id | derived_from | wave |
|--------|-----------------|------|--------|--------------|------|
| ORG-0008 | shpigovsky.ru | shpigovsky.ru | **none** | website candidate | Wave 5 |

### 6.3 Public contact signals *(website — not internal contacts)*

| org_id | contact_type | value | evidence_ref | internal? |
|--------|--------------|-------|--------------|-----------|
| ORG-0008 | email (public) | Info@shpigovsky.ru | EV-SHPIG-WEB-01 | **No** — public only |
| ORG-0008 | phone (public) | +7 (925) 183-64-64 | EV-SHPIG-WEB-01 | **No** — public only |
| ORG-0008 | phone (public) | +7 (995) 023-92-26 | EV-SHPIG-WEB-01 | **No** — public only |
| ORG-0008 | location (public) | МО, район ЖД станции Катуар | EV-SHPIG-WEB-01 | **No** — public only |

**Internal contacts:** **SAFE UNKNOWN**

---

## 7. Cross-reference index (informational — not Wave 1D edges)

| Related artifact | Entity class | Relationship to ORG-0008 | Wave |
|------------------|--------------|----------------------------|------|
| ORG-0001 Полигон | Organization | Delivery org reference — **no REL-* minted** | informational |
| PER-0010 Ольга Дягилева | Person | Acquisition/coordination reference — **no new edges** | informational |
| ORG-0005 ЗПМ | Organization | **Distinct** — unchanged | — |
| ORG-0006 SIBCAR | Organization | **Distinct** — unchanged | — |
| ORG-0007 Макита Снаб | Organization | **Distinct** — unchanged | — |
| SHPIGOVSKY-INTAKE-CAND-PRJ-A01 | Project candidate | **Not minted** — Wave 3 | deferred |

---

## 8. Evidence index (population references)

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| EV-SHPIG-OP-01 | Operator intake statements (2026-06-10) | **E0** | Polygon channel, roles, stack, i-SEO exclusion |
| EV-SHPIG-WEB-01 | Live capture homepage | **E2** | Brand, services, contacts, footer legal-name signal |
| EV-SHPIG-WEB-02 | Live capture `/policy` | **E2** | Privacy policy operator **ООО "Сознание"** |
| OOEP | [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) | governance | Category A operational-public path |

**Counterparty Card path:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\shpigovsky\` — **absent** — **not blocking** Organization **active** (Category A operational-public path; LE deferred).

---

## 9. Duplicate review register

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| W1D-SHPIG-D-01 | Shpigovsky vs ORG-0001 | **Distinct** | No |
| W1D-SHPIG-D-02 | Shpigovsky vs ORG-0002 | **Distinct** | No |
| W1D-SHPIG-D-03 | Shpigovsky vs ORG-0003 i-SEO | **Distinct** | No |
| W1D-SHPIG-D-04 | Shpigovsky vs ORG-0004 | **Distinct** | No |
| W1D-SHPIG-D-05 | Shpigovsky vs ORG-0005 ЗПМ | **Distinct** | No |
| W1D-SHPIG-D-06 | Shpigovsky vs ORG-0006 SIBCAR | **Distinct** | No |
| W1D-SHPIG-D-07 | Shpigovsky vs ORG-0007 Makita | **Distinct** | No |
| W1D-SHPIG-D-08 | shpigovsky.ru vs existing WEB-* | **No collision** | No |
| W1D-SHPIG-D-09 | INN/OGRN legal-identity close | **Open — expected** | No — LE deferred |

---

## 10. Integrity validation — prior orgs unchanged

| Check | Result |
|-------|--------|
| ORG-0001..0007 register rows | **Unchanged** — no edits in this package |
| Makita (ORG-0007) | **Intact** |
| ZPM (ORG-0005) | **Intact** |
| SIBCAR (ORG-0006) | **Intact** |
| Merge operations | **None** |
| LE-* creation | **None** |
| REL-* creation | **None** |
| PRJ-* creation | **None** |
| WEB-* / DOM-* creation | **None** |
| PER-* creation | **None** |
| Graph redesign | **None** |
| Foundation changes | **None** |

---

## 11. Gap register

| gap_id | topic | severity | mitigation |
|--------|-------|----------|------------|
| ME-W1D-SHPIG-01 | Legal entity form | **Deferred** | Future CC or E2 registry extract |
| ME-W1D-SHPIG-02 | INN / KPP / OGRN | **Deferred** | Future CC |
| ME-W1D-SHPIG-03 | Legal vs trade name (Сознание ↔ Шпиговский Дом) | **Deferred** | Future CC |
| ME-W1D-SHPIG-04 | CC folder absent | **Expected** | Category A operational-public path |
| ME-W1D-SHPIG-05 | Contract data | **Deferred** | Future commercial wave |
| ME-W1D-SHPIG-06 | Ownership structure | **Deferred** | Future CC |
| ME-W1D-SHPIG-07 | Internal contacts | **Deferred** | Future CC / steward confirmation |
| ME-W1D-SHPIG-08 | Primary website designation | Low | Wave 4 Website population |
| ME-W1D-SHPIG-09 | Commercial edges (CLIENT_OF) | Medium | Wave 6+ |
| ME-W1D-SHPIG-10 | Delivery phase (WIP vs complete) | Low | Wave 3 Project population |

---

## 12. Readiness summary

| org_id | population | duplicate review | attestation | legal entity |
|--------|------------|------------------|-------------|--------------|
| ORG-0008 | **Complete** | **Pass** | **active** — AT-W1D-SHPIG-01 | **Deferred — SAFE UNKNOWN** |

---

## 13. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-POPULATION-v1.md) | Population plan |
| [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md) | Attestation act |
| [ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md](ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md) | Prior intake evidence |
| [ATLAS-SHPIGOVSKY-INTAKE-REGISTER-v1.md](ATLAS-SHPIGOVSKY-INTAKE-REGISTER-v1.md) | Prior intake register |

---

*ATLAS Wave 1D Shpigovsky Organization Register v1 — documentation only.*
