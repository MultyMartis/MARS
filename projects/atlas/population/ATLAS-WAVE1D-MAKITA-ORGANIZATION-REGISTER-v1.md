# ATLAS Wave 1D Makita Organization Register v1

**Status:** **documented** — canonical Organization roster for Wave 1D Makita tranche.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-WAVE1D-MAKITA-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1D-MAKITA-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-ATTESTATION-v1.md) · [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md)  
**Is not:** LegalEntities attested export, runtime registry, database table, relationship register.

---

## 1. Purpose

Канонический **реестр Organization population** Wave 1D — tranche **Makita Snab (Макита Снаб)**. Одна строка — одна attested Organization record at **E0** operational evidence tier.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Wave tier W1-D | **1** |
| Classification i-SEO client | **1** |
| Target **active** | **1** |
| Legal entity | **0** — **SAFE UNKNOWN** |
| Attestation readiness | **ready** |

---

## 2. Population roster — full table

| org_id | canonical_name | wave_tier | classification | business_role | legal_entity_id | legal_entity_name | inn | kpp | ogrn_ogrnip | aliases | primary_website | primary_domain | evidence_tier | lifecycle_state | attestation_ref | notes |
|--------|----------------|-----------|----------------|---------------|-----------------|-------------------|-----|-----|-------------|---------|-----------------|----------------|---------------|-----------------|-----------------|-------|
| ORG-0007 | **Макита Снаб** | **W1-D** | **i-SEO client** | **CLIENT** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | *(none attested)* | **SAFE UNKNOWN** *(candidates: makita-snab.ru; makita-land.ru)* | **SAFE UNKNOWN** | **E0** *(operational)* | **active** | AT-W1D-01 | Category B; OOEP; no CC; LE deferred |

---

## 3. Legal entity index

**No Legal Entity rows minted in Wave 1D.**

| legal_entity_id | status | notes |
|-----------------|--------|-------|
| LE-* | **Not created** | **SAFE UNKNOWN** until E1+ CC or E2 registry extract appears |

**Deferred fields (explicit):**

| Field | Value |
|-------|-------|
| Legal entity | **SAFE UNKNOWN** |
| INN | **SAFE UNKNOWN** |
| KPP | **SAFE UNKNOWN** |
| OGRN | **SAFE UNKNOWN** |
| Legal signatory | **SAFE UNKNOWN** |
| EDO | **SAFE UNKNOWN** |

**Note:** LE-0001..0005 attested in prior waves (Wave 1, 1B, 1C). **No LE-0006** created for Makita.

---

## 4. Operational contact register *(informational — not PER-* mint)*

| org_id | contact_label | phone | person_id | evidence_ref | attestation_state |
|--------|---------------|-------|-----------|--------------|-------------------|
| ORG-0007 | **Артём** *(given name)* | +7 926 022-30-91 | **none** | EV-MAKITA-OP-01 | operational signal only |

**Full legal name of contact:** **SAFE UNKNOWN**

---

## 5. Candidate asset register *(not WEB-* / DOM-* mint)*

### 5.1 Website candidates

| org_id | candidate_label | URL | hostname | web_id | evidence_ref | wave |
|--------|-----------------|-----|----------|--------|--------------|------|
| ORG-0007 | makita-snab.ru | https://makita-snab.ru/ | makita-snab.ru | **none** | EV-MAKITA-OP-01; EV-MAKITA-OP-02 | Wave 4 |
| ORG-0007 | makita-land.ru | https://makita-land.ru/ | makita-land.ru | **none** | EV-MAKITA-OP-01; EV-MAKITA-OP-02 | Wave 4 |

### 5.2 Domain candidates

| org_id | candidate_label | fqdn | dom_id | derived_from | wave |
|--------|-----------------|------|--------|--------------|------|
| ORG-0007 | makita-snab.ru | makita-snab.ru | **none** | website candidate | Wave 5 |
| ORG-0007 | makita-land.ru | makita-land.ru | **none** | website candidate | Wave 5 |

---

## 6. Cross-reference index (informational — not Wave 1D edges)

| Related artifact | Entity class | Relationship to ORG-0007 | Wave |
|------------------|--------------|----------------------------|------|
| ORG-0003 i-SEO | Organization | Vendor context — SEO provider; **no REL-* minted** | informational |
| ORG-0001 Полигон | Organization | Steward operational scope (Direct) — **no REL-* minted** | informational |
| ORG-0005 ЗПМ | Organization | **Distinct** — unchanged | — |
| ORG-0006 SIBCAR | Organization | **Distinct** — unchanged | — |
| ORCA Makita pilot | Pilot charter | **Not** Organization evidence — EFV-02 | excluded |

---

## 7. Evidence index (population references)

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| EV-MAKITA-OP-01 | Steward intake inputs (2026-06-07) | **E0** | Primary operational evidence |
| EV-MAKITA-OP-02 | Steward statement — both websites exist | **E0** | Website candidate corroboration |
| EV-MAKITA-OP-03 | Intake enrichment consolidation | **E0** | Service context, boundaries |
| OOEP | [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) | governance | Category B path |

**Counterparty Card path:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\makita-snab\` — **absent** — **not blocking** Organization **active** (Category B).

---

## 8. Duplicate review register

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| W1D-D-01 | Makita vs ORG-0001 | **Distinct** | No |
| W1D-D-02 | Makita vs ORG-0002 | **Distinct** | No |
| W1D-D-03 | Makita vs ORG-0003 i-SEO | **Distinct** | No |
| W1D-D-04 | Makita vs ORG-0004 | **Distinct** | No |
| W1D-D-05 | Makita vs ORG-0005 ЗПМ | **Distinct** | No |
| W1D-D-06 | Makita vs ORG-0006 SIBCAR | **Distinct** | No |
| W1D-D-07 | ORCA pilot class boundary | **Pass** | No |
| W1D-D-08 | «Makita» tool brand homonym | **Open — low** | No |

---

## 9. Integrity validation — prior orgs unchanged

| Check | Result |
|-------|--------|
| ORG-0001..0006 register rows | **Unchanged** — no edits in this package |
| ZPM (ORG-0005) | **Intact** |
| SIBCAR (ORG-0006) | **Intact** |
| Merge operations | **None** |
| LE-* creation | **None** |
| REL-* creation | **None** |
| PRJ-* creation | **None** |

---

## 10. Gap register

| gap_id | topic | severity | mitigation |
|--------|-------|----------|------------|
| ME-W1D-01 | Legal entity form | **Deferred** | Future CC or E2 extract |
| ME-W1D-02 | INN / KPP / OGRN | **Deferred** | Future CC |
| ME-W1D-03 | Legal vs trade name | **Deferred** | Future CC |
| ME-W1D-04 | CC folder absent | **Expected** | Category B — not blocking org |
| ME-W1D-05 | Primary website designation | Low | Wave 4 Website population |
| ME-W1D-06 | Commercial edges (CLIENT_OF) | Medium | Wave 6+ |

---

## 11. Readiness summary

| org_id | population | duplicate review | attestation | legal entity |
|--------|------------|------------------|-------------|--------------|
| ORG-0007 | **Complete** | **Pass** | **active** — AT-W1D-01 | **Deferred — SAFE UNKNOWN** |

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1D-MAKITA-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-POPULATION-v1.md) | Population plan |
| [ATLAS-WAVE1D-MAKITA-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-ATTESTATION-v1.md) | Attestation act |
| [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | Wave 1 orgs ORG-0001..0004 — baseline |
| [ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md](ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md) | Prior E0 evidence source |

---

*ATLAS Wave 1D Makita Organization Register v1 — documentation only.*
