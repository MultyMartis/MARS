# ATLAS ↔ OCPilot SIBCAR Crosswalk Register v1

**Status:** **documented** — cross-system crosswalk audit register (audit only).  
**Program:** ATLAS — Business Reality Registry · OCPilot  
**Audit date:** 2026-06-07  
**Parent:** [ATLAS-OCPILOT-SIBCAR-CROSSWALK-AUDIT-v1.md](ATLAS-OCPILOT-SIBCAR-CROSSWALK-AUDIT-v1.md) · [ATLAS-OCPILOT-SIBCAR-CROSSWALK-SUMMARY-v1.md](ATLAS-OCPILOT-SIBCAR-CROSSWALK-SUMMARY-v1.md)  
**Is not:** population register, attestation export, OCPilot site registry replacement, runtime table.

---

## 1. Register purpose

Единый **crosswalk register** сопоставления Atlas SIBCAR entities с OCPilot **SITE-001**. Одна строка — одна пара entity ↔ object с результатом проверки, evidence refs и audit flags.

**Authority hierarchy applied:**

1. Atlas **attestation acts** — canonical business identity and lifecycle.
2. OCPilot **site-passport** + **project-site-registry** — operational deployment facts.
3. Crosswalk fields in Atlas registers — documentation linkage only (not graph edges).

---

## 2. Primary crosswalk matrix

| atlas_id | atlas_class | atlas_lifecycle | ocpilot_id | ocpilot_class | crosswalk_kind | match | evidence_refs | audit_flag |
|----------|-------------|-----------------|------------|---------------|----------------|-------|---------------|------------|
| **ORG-0006** | Organization | **active** | SITE-001 | site_id *(client context)* | documentation | **Pass** | AT-W1C-01; EV-W1C-02; Register §5 | — |
| **LE-0005** | Legal Entity | **active** | *(none)* | — | absent — expected | **Pass** | AT-W1C-01; EV-W1C-CC-01 | — |
| **PRJ-0011** | Project | **active** | SITE-001 | engagement container | documentation | **Pass** | AT-W3-SIBCAR-01; EV-W1C-03; EV-OCP-01..04 | FINDING-XW-SIBCAR-01 |
| **WEB-SIBCAR-01** | Website | **active** | SITE-001 | deployment | documentation | **Pass** | AT-W4-SIBCAR-01; EV-W1C-02 | — |
| **DOM-SIBCAR-01** | Domain | **proposed** | SITE-001 | hostname *(implicit)* | documentation | **Partial** | Register W5; EV-W1C-02 | FINDING-XW-SIBCAR-04 |

---

## 3. Field-level crosswalk — Organization (ORG-0006)

| Field | Atlas value | OCPilot value | Match | Notes |
|-------|-------------|---------------|-------|-------|
| org_id | ORG-0006 | *(not recorded)* | n/a | Expected — OCPilot has no org_id namespace |
| canonical_name | SIBCAR | *(implicit via engagement)* | **Partial** | Trade title used in OCPilot |
| legal display | ООО «СибКар» | *(absent in intake)* | n/a | LE-0005 only |
| business_role | **CLIENT** | Client engagement implied | **Pass** | |
| aliases (attested) | SIBCAR · СибКар · SibCar · ООО «СибКар» | «Автосалон СИБКАР» site title | **Partial** | W1C-D-05 — not org alias |
| primary_website | **SAFE UNKNOWN** *(prod)* | Public URL **SAFE UNKNOWN** | **Pass** | |
| inn / ogrn | 5405512542 / 1265400004220 | *(absent)* | n/a | LE layer only |

---

## 4. Field-level crosswalk — Legal Entity (LE-0005)

| Field | Atlas value | OCPilot core intake | OCPilot execution reports | Duplicate risk |
|-------|-------------|---------------------|---------------------------|----------------|
| legal_entity_id | LE-0005 | — | Referenced in change-auth review | **None** |
| legal_entity_name | ООО «СибКар» | — | Cited via Atlas CC path | **None** |
| inn | 5405512542 | — | — | **None** |
| kpp | 540501001 | — | — | **None** |
| ogrn | 1265400004220 | — | — | **None** |
| org_binding | ORG-0006 | — | — | **None** |

---

## 5. Field-level crosswalk — Project (PRJ-0011)

| Field | Atlas value | OCPilot value | Match |
|-------|-------------|---------------|-------|
| project_id | PRJ-0011 | *(not recorded)* | n/a |
| canonical_name | Автосалон СИБКАР — OpenCart dealership | Project name: Автосалон СИБКАР | **Pass** |
| population_slice | client_delivery | Business Goal + Planned Work | **Pass** |
| commissioning_org | ORG-0006 *(display)* | Implicit client | **Pass** |
| execution_org | ORG-0001 Полигон *(display)* | OCPilot operator context | **Pass** |
| ocpilot_crosswalk | SITE-001 | Site ID SITE-001 | **Pass** |
| technology | ocStore 3.0.3.8 (rs.2) TEST | ocStore 3.0.3.8 (rs.2) TEST | **Pass** |
| related property | `sibcar.new-site.space` | Test URL same hostname | **Pass** |

**Engagement determination:** **Same project** — not different, not partial overlap.

---

## 6. Field-level crosswalk — Website (WEB-SIBCAR-01)

| Field | Atlas value | OCPilot value | Match |
|-------|-------------|---------------|-------|
| website_id | WEB-SIBCAR-01 | *(not recorded)* | n/a |
| canonical_name | sibcar.new-site.space | Test URL hostname | **Pass** |
| url | `https://sibcar.new-site.space/` | `https://sibcar.new-site.space/` | **Pass** |
| environment | **TEST** | **TEST** | **Pass** |
| website_kind | test_deployment | TEST deployment | **Pass** |
| platform | ocStore 3.0.3.8 (rs.2) | ocStore 3.0.3.8 (rs.2) | **Pass** |
| baseline | *(Atlas consumer context)* | ocstore-3038-rs2 approved | **Pass** |
| ocpilot_crosswalk | SITE-001 | Site ID SITE-001 | **Pass** |
| hosting | *(not Atlas field)* | **SAFE UNKNOWN** | **Pass** — both unknown |

---

## 7. Field-level crosswalk — Domain (DOM-SIBCAR-01)

| Field | Atlas value | OCPilot value | Match |
|-------|-------------|---------------|-------|
| domain_id | DOM-SIBCAR-01 | *(not recorded)* | n/a |
| canonical_name | sibcar.new-site.space | Test URL hostname | **Pass** |
| hostname_class | hosting_subdomain | *(implicit TEST subdomain)* | **Pass** |
| environment | **TEST** | **TEST** | **Pass** |
| lifecycle | **proposed** | n/a | **Partial** |
| registrar | **SAFE UNKNOWN** | Hosting **SAFE UNKNOWN** | **Pass** |
| primary_website_candidate | WEB-SIBCAR-01 | SITE-001 deployment | **Pass** |

---

## 8. Relationship crosswalk (Atlas only — not mirrored in OCPilot)

| relationship_id | type | endpoints | attested | ocpilot_mirror | conflict |
|-----------------|------|-----------|----------|----------------|----------|
| REL-SIBCAR-PJ-01 | COMMISSIONED_BY | PRJ-0011 → ORG-0006 | **active** | — | **None** |
| REL-SIBCAR-PJ-02 | EXECUTES | ORG-0001 → PRJ-0011 | **active** | — | **None** |
| REL-SIBCAR-WB-01 | BELONGS_TO | WEB-SIBCAR-01 → PRJ-0011 | **active** | — | **None** |
| REL-SIBCAR-WB-02 | OWNS | ORG-0006 → WEB-SIBCAR-01 | **active** | — | **None** |
| REL-0041 | CLIENT_OF | ORG-0006 → ORG-0001 | **active** | — | **None** |

OCPilot does not model Atlas relationship graph — **expected**. No inversion: SITE-001 does not claim COMMISSIONED_BY or OWNS edges.

---

## 9. Duplicate risk register

| review_id | signal | atlas_outcome | ocpilot_outcome | crosswalk_verdict | blocking |
|-----------|--------|---------------|-----------------|-------------------|----------|
| XW-DUP-01 | ORG-0006 vs SITE-001 as second org | Class boundary | site_id only | **Pass** | No |
| XW-DUP-02 | PRJ-0011 vs SITE-001 as Project | REJ-SIBCAR-PRJ-02 | site workspace | **Pass** | No |
| XW-DUP-03 | WEB-SIBCAR-01 vs SITE-001 as Website | SIBCAR-WEB-D-01 | deployment container | **Pass** | No |
| XW-DUP-04 | Second SIBCAR hostname in OCPilot | — | Single TEST URL | **Pass** | No |
| XW-DUP-05 | LE-0005 vs OCPilot legal block | Single LE | Atlas CC cite only | **Pass** | No |
| XW-DUP-06 | SIBCAR vs BZPM | Distinct INN/OGRN | N/A — single site | **Pass** | No |
| XW-DUP-07 | Run 5 audit as Project | REJ-SIBCAR-PRJ-01 | Program context | **Pass** | No |

---

## 10. Drift register

| drift_id | topic | atlas_state | ocpilot_state | severity | sync_ref |
|----------|-------|-------------|---------------|----------|----------|
| XW-SIBCAR-D-01 | Atlas ID back-links | Present in registers | Absent in passport/registry | Low | SYNC-XW-02 |
| XW-SIBCAR-D-02 | project-site-registry crosswalk | EV-OCP-03 cited by Atlas | No Atlas IDs in row | Low | SYNC-XW-03 |
| XW-SIBCAR-D-03 | Run 5 authorization narrative | N/A (Atlas excludes Run 5 as Project) | passport READY / brief NO / STATE paused | Medium | SYNC-XW-01 |
| XW-SIBCAR-D-04 | Site title vs legal name | W1C-D-05 documented | «Автосалон СИБКАР» | Low | SYNC-XW-04 |
| XW-SIBCAR-D-05 | Domain lifecycle | DOM-SIBCAR-01 **proposed** | No Domain class | Low | SYNC-XW-05 |
| XW-SIBCAR-D-06 | Production URL | ME-W1C-02 SAFE UNKNOWN | Public URL SAFE UNKNOWN | Medium | SYNC-XW-06 |
| XW-SIBCAR-D-07 | Access brief Run 5 gates | N/A | Stale checkboxes § Run 5 Readiness | Medium | SYNC-XW-01 |
| XW-SIBCAR-D-08 | EAR snapshot | SU-SIBCAR-PRJ-08 | Run 5 paused | Medium | Cross-program |

---

## 11. Finding register

| finding_id | severity | category | summary | blocking | remediation_type |
|------------|----------|----------|---------|----------|------------------|
| **FINDING-XW-SIBCAR-01** | Low | Crosswalk linkage | Missing OCPilot → Atlas ID back-references | No | Doc sync |
| **FINDING-XW-SIBCAR-02** | Medium | OCPilot doc drift | Run 5 status inconsistent across SITE-001 files | No | Doc reconcile |
| **FINDING-XW-SIBCAR-03** | Low | Naming | W1C-D-05 trade title vs legal alias | No | Policy note |
| **FINDING-XW-SIBCAR-04** | Low | Atlas lifecycle | DOM-SIBCAR-01 proposed — W5 pending | No | Future attestation |
| **FINDING-XW-SIBCAR-05** | Medium | SAFE UNKNOWN | Production URL unknown both sides | No | Hold until evidence |
| **FINDING-XW-SIBCAR-06** | Info | Cross-program | EAR Run 5 paused — not identity issue | No | Operational |

---

## 12. Synchronization recommendation register

| sync_id | priority | action | target doc(s) | mutates_graph |
|---------|----------|--------|---------------|---------------|
| **SYNC-XW-01** | P1 | Reconcile Run 5 gate narrative | site-passport, project-access-brief, README, OCPILOT-STATE | **No** |
| **SYNC-XW-02** | P2 | Add Atlas crosswalk block | site-passport.md | **No** |
| **SYNC-XW-03** | P2 | Add Atlas IDs to registry Notes | project-site-registry.md | **No** |
| **SYNC-XW-04** | P3 | Document W1C-D-05 display policy | site-passport.md Notes | **No** |
| **SYNC-XW-05** | P3 | Post-W5 register header sync | ATLAS-WAVE5-SIBCAR-DOMAIN-REGISTER-v1.md | **No** |
| **SYNC-XW-06** | Hold | Production URL crosswalk | Both — when URL evidenced | **No** |

---

## 13. Evidence index (crosswalk)

| Ref | Artifact | Crosswalk use |
|-----|----------|---------------|
| **EV-W1C-02** | [site-passport.md](../../ocpilot/sites/site-001/site-passport.md) | ORG/WEB/DOM hostname; SITE-001 identity |
| **EV-W1C-03** | [project-access-brief.md](../../ocpilot/sites/site-001/project-access-brief.md) | PRJ-0011 Business Goal scope |
| **EV-OCP-01** | [INTAKE-COMPLETE.md](../../ocpilot/sites/site-001/materials/INTAKE-COMPLETE.md) | Engagement corroboration |
| **EV-OCP-02** | [AUDIT-CHARTER.md](../../ocpilot/sites/site-001/AUDIT-CHARTER.md) | Run 5 program boundary |
| **EV-OCP-03** | [project-site-registry.md](../../ocpilot/project-site-registry.md) | SITE-001 registry row |
| **EV-OCP-04** | project-access-brief § Business Goal | Pilot narrative |
| **EV-W1C-CC-01** | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | LE-0005 identifiers |
| **AT-W1C-01** | Wave 1C active attestation | ORG-0006, LE-0005 |
| **AT-W3-SIBCAR-01** | Wave 3 Project attestation | PRJ-0011 |
| **AT-W4-SIBCAR-01** | Wave 4 Website attestation | WEB-SIBCAR-01 |

---

## 14. OCPilot SITE-001 document inventory (audit scope)

| Document | Version / date signal | Crosswalk relevance |
|----------|----------------------|---------------------|
| site-passport.md | READY FOR RUN 5 | Primary deployment identity |
| project-access-brief.md | INTAKE COMPLETE; Run 5 NO | Project scope + drift source |
| AUDIT-CHARTER.md | READY FOR RUN 5 | Operational authorization |
| project-site-registry.md | 2026-06-01 intake | Canonical OCPilot site row |
| README.md | Run 5 gate NO | Drift source |
| OCPILOT-STATE.md | 2026-06-07 | Program authority — Run 5 paused |
| INTAKE-COMPLETE.md | Baseline approved | Intake closure |
| SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md | 2026-06-07 | Atlas LE-0005 consumption |
| SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md | NOT AUTHORIZED | Execution gate — separate from crosswalk |

---

## 15. Register counts

| Metric | Count |
|--------|-------|
| Primary crosswalk pairs | **5** |
| Pass | **4** |
| Partial | **1** (DOM-SIBCAR-01 lifecycle) |
| Fail | **0** |
| Duplicate risks reviewed | **7** — all **Pass** |
| Drift items | **8** |
| Findings | **6** — **0 blocking** |
| Sync recommendations | **6** |

---

*ATLAS ↔ OCPilot SIBCAR Crosswalk Register v1 — documentation only.*
