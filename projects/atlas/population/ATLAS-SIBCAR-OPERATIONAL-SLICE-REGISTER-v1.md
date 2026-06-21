# ATLAS SIBCAR Operational Slice Register v1

**Status:** **documented** — operational expansion register (pre-population).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Subject contour:** ORG-0006 **SIBCAR** · LE-0005 · REL-0041  
**Parent:** [ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md) · [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md)  
**Is not:** canonical Project / Website / Domain registry, attested export, entity or relationship minting.

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Attested anchor entities | **2** (ORG-0006, LE-0005) |
| Attested commercial edges | **1** (REL-0041) |
| Project candidates (accept) | **1** |
| Website candidates (TEST accept) | **1** |
| Website candidates (production) | **0** *(BLOCKED)* |
| Domain candidates (TEST partial) | **1** |
| Domain candidates (production) | **0** *(BLOCKED)* |
| Draft structural relationships | **6** |
| Cross-program linkages | **5** (OCPilot ×2, EAR ×3) |
| `PRJ-*` / `WEB-*` / `DOM-*` / `REL-*` assigned | **0** *(audit only)* |

---

## 2. Attested anchor register (baseline — not expansion queue)

| entity_class | id | canonical_name | lifecycle | attestation | evidence_tier |
|--------------|-----|----------------|-----------|-------------|---------------|
| Organization | ORG-0006 | SIBCAR | **active** | AT-W1C-01 | E1 |
| Legal Entity | LE-0005 | ООО «СибКар» | **active** | AT-W1C-01 | E1 |
| Relationship | REL-0041 | ORG-0006 → ORG-0001 **CLIENT_OF** | **active** | AT-W6B-02 | E1 |

---

## 3. Evidence inventory register

| ref_id | artifact | tier | location / link | expansion role |
|--------|----------|------|-----------------|------------------|
| EV-W1C-CC-01 | Карточка предприятия | **E1** | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | Org / LE anchor |
| EV-W1C-02 | OCPilot site-passport | E0 | [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) | Website candidate |
| EV-W1C-03 | OCPilot project-access-brief | E0 | [project-access-brief.md](../../../projects/ocpilot/sites/site-001/project-access-brief.md) | Project + Website context |
| EV-OCP-01 | INTAKE-COMPLETE | E0 | [materials/INTAKE-COMPLETE.md](../../../projects/ocpilot/sites/site-001/materials/INTAKE-COMPLETE.md) | Engagement corroboration |
| EV-OCP-02 | AUDIT-CHARTER | E0 | [AUDIT-CHARTER.md](../../../projects/ocpilot/sites/site-001/AUDIT-CHARTER.md) | Run 5 scope |
| EV-OCP-03 | project-site-registry row | E0 | [project-site-registry.md](../../../projects/ocpilot/project-site-registry.md) | SITE-001 registration |
| EV-EAR-01 | EAR-SITE-001-ACQUISITION-OPTIONS | design | [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](../../../shared/external-access-runtime/EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) | Channel analysis |
| EV-EAR-02 | EAR-SITE-001-WORKFLOW-EXAMPLE | design | [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](../../../shared/external-access-runtime/EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) | Run 5 target level |
| EV-EAR-03 | site-001-pre-runtime-bridge | freeze | [freeze/site-001-pre-runtime-bridge/](../../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/) | Acquisition blocker state |
| AT-W6B-02 | REL-0041 attestation | attestation | [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | Commercial anchor |

---

## 4. Candidate Project register

| intake_label | proposed_canonical_name | commissioning_org | execution_org | related_property | target_lifecycle | evidence_tier | evidence_ref | intake_verdict | wave_3_roster | readiness |
|--------------|-------------------------|-------------------|---------------|------------------|------------------|---------------|--------------|----------------|---------------|-----------|
| **SIBCAR-INTAKE-CAND-A01** | Автосалон СИБКАР — OpenCart dealership | ORG-0006 | ORG-0001 *(display)* | `sibcar.new-site.space` | **active** | **E0** | EV-W1C-02..03; REL-0041 | **Accept** | **Yes — P0** | **PARTIAL** |

### 4.1 Future candidates (hold)

| intake_label | description | evidence_ref | verdict | roster |
|--------------|-------------|--------------|---------|--------|
| SIBCAR-INTAKE-FUT-01 | Standalone Yandex Direct campaign | EV-W1C-03 checkbox only | **Future — hold** | No |
| SIBCAR-INTAKE-FUT-02 | Custom module development | EV-W1C-03 — not started | **Future — hold** | No |
| SIBCAR-INTAKE-FUT-03 | Production launch / PROD migration | **SAFE UNKNOWN** | **Future — hold** | No |

### 4.2 Rejected candidates

| rejected_label | description | rejection_class | basis |
|----------------|-------------|-----------------|-------|
| REJ-SIBCAR-PRJ-01 | OCPilot Run 5 audit program | MARS program | E-17; REJ-ZPM-PRJ-02 analog |
| REJ-SIBCAR-PRJ-02 | SITE-001 as Project entity | Class boundary | site_id ≠ Project |
| REJ-SIBCAR-PRJ-03 | ORG-0005 / BZPM engagement | Identity pollution | COR-W1B-03 |
| REJ-SIBCAR-PRJ-04 | Per-checkbox split (SEO, theme, …) | Inference | EFV-03 — single engagement narrative |

---

## 5. Candidate Website register

| intake_label | proposed_canonical_name | website_kind | url | environment | primary_org | primary_project | evidence_tier | evidence_ref | wave_4_roster | readiness |
|--------------|-------------------------|--------------|-----|-------------|-------------|-----------------|---------------|--------------|---------------|-----------|
| **SIBCAR-INTAKE-WEB-01** | sibcar.new-site.space | test_deployment | `https://sibcar.new-site.space/` | **TEST** | ORG-0006 | SIBCAR-INTAKE-CAND-A01 | **E0** | EV-W1C-02, EV-W1C-03 | **Yes — P0** | **PARTIAL** |
| SIBCAR-INTAKE-WEB-02 | *(production)* | corporate | **SAFE UNKNOWN** | PROD | ORG-0006 | — | — | — | **No — deferred** | **BLOCKED** |

**Display alias (not org alias):** «Автосалон СИБКАР» — OCPilot site title; resolve at Website intake (W1C-D-05).

---

## 6. Candidate Domain register

| intake_label | fqdn | domain_class | related_website | registrant_evidence | evidence_tier | evidence_ref | wave_5_roster | readiness |
|--------------|------|--------------|-------------------|---------------------|---------------|--------------|---------------|-----------|
| **SIBCAR-INTAKE-DOM-01** | `sibcar.new-site.space` | hosting_subdomain | SIBCAR-INTAKE-WEB-01 | **SAFE UNKNOWN** | **E0** | EV-W1C-02 | **Yes — P0** | **PARTIAL** |
| SIBCAR-INTAKE-DOM-02 | **SAFE UNKNOWN** | corporate_apex | SIBCAR-INTAKE-WEB-02 | **None** | — | — | **No** | **BLOCKED** |

**Excluded:** `mail.ru` — consumer email domain (CC §16).

---

## 7. Candidate relationship register

*Draft slots — ids assigned only at population tranches.*

### 7.1 Wave 3B — Project ↔ Organization

| draft_slot | source | target | type | wave | evidence_ref | readiness |
|------------|--------|--------|------|------|--------------|-----------|
| REL-SIBCAR-PJ-01 | PRJ-* *(A01)* | ORG-0006 | **COMMISSIONED_BY** | 3B | EV-W1C-03; AT-W1C-01 | **PARTIAL** |
| REL-SIBCAR-PJ-02 | ORG-0001 | PRJ-* *(A01)* | **EXECUTES** | 3B | REL-0041; EV-W1C-03 | **PARTIAL** |

### 7.2 Wave 4B — Website family

| draft_slot | source | target | type | wave | evidence_ref | readiness |
|------------|--------|--------|------|------|--------------|-----------|
| REL-SIBCAR-WB-01 | WEB-* *(TEST)* | PRJ-* *(A01)* | **BELONGS_TO** | 4B | EV-W1C-02 | **PARTIAL** |
| REL-SIBCAR-WB-02 | ORG-0006 | WEB-* *(TEST)* | **OWNS** | 4B | EV-W1C-03 TEST env | **PARTIAL** |

### 7.3 Wave 5B — Domain family

| draft_slot | source | target | type | wave | evidence_ref | readiness |
|------------|--------|--------|------|------|--------------|-----------|
| REL-SIBCAR-DM-01 | DOM-* *(TEST)* | WEB-* *(TEST)* | **PRIMARY_DOMAIN** | 5B | Hostname match | **PARTIAL** |
| REL-SIBCAR-DM-02 | ORG-0006 | DOM-* *(TEST)* | **OWNS** | 5B | Registrar E1 | **BLOCKED** / defer |

### 7.4 Attested — not in queue

| relationship_id | source | target | type | lifecycle |
|-----------------|--------|--------|------|-----------|
| REL-0041 | ORG-0006 | ORG-0001 | **CLIENT_OF** | **active** |

---

## 8. OCPilot linkage register

| link_id | ocpilot_ref | atlas_target | link_type | evidence_ref | readiness |
|---------|-------------|--------------|-----------|--------------|-----------|
| LK-OCP-01 | SITE-001 | SIBCAR-INTAKE-CAND-A01 | documentation crosswalk | EV-OCP-03; EV-W1C-03 | **PARTIAL** |
| LK-OCP-02 | SITE-001 | ORG-0006 | informational contour | W1C-D-04 | **READY** *(doc)* |
| LK-OCP-03 | Run 5 audit scope | WEB-* TEST | consumer enrichment | EV-OCP-02 | **BLOCKED** — Run 5 not executing |

**OCPilot storage path:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\`

---

## 9. EAR linkage register

| link_id | ear_ref | atlas_target | link_type | evidence_ref | readiness |
|---------|---------|--------------|-----------|--------------|-----------|
| LK-EAR-01 | Published snapshot | OCPilot Run 5 | consumer feed | EV-EAR-02 | **BLOCKED** |
| LK-EAR-02 | Evidence Package / Request | SITE-001 | acquisition intake | EV-EAR-01 | **PARTIAL** |
| LK-EAR-03 | Snapshot metadata | WEB-* evidence tier | optional enrichment | — | **SAFE UNKNOWN** |

**Run 5 minimum (documented):** Snapshot Level **1+** with `file-manifest` — [EV-EAR-02].

---

## 10. Evidence readiness register

| expansion_target | classification | primary_evidence | blocker |
|------------------|----------------|------------------|---------|
| Wave 3 Project | **PARTIAL** | EV-W1C-03; REL-0041 | SU-W6B-04 |
| Wave 3B Project ↔ Org | **PARTIAL** | ZPM analog; REL-0041 | Wave 3 mint |
| Wave 4 Website (TEST) | **PARTIAL** | EV-W1C-02, EV-W1C-03 | TEST-only scope |
| Wave 4 Website (PROD) | **BLOCKED** | — | ME-W1C-02 |
| Wave 4B Website rels | **PARTIAL** | ZPM REL-ZPM-WB-* analog | Waves 3 + 4 |
| Wave 5 Domain (TEST) | **PARTIAL** | Hostname from Wave 4 | Registrar SAFE UNKNOWN |
| Wave 5 Domain (PROD) | **BLOCKED** | — | No FQDN |
| Wave 5B Domain rels | **PARTIAL** | ZPM 5B precedent | Domain OWNS defer |
| OCPilot linkage | **PARTIAL** | SITE-001 package complete | Run 5 blocked |
| EAR linkage | **BLOCKED** | Design docs only | No published snapshot |
| Wave 2C Person *(optional)* | **PARTIAL** | EV-W1C-CC-01 §22 | Not on critical path |

---

## 11. Gap register

| gap_id | topic | severity | mitigation | wave |
|--------|-------|----------|------------|------|
| SU-W6B-04 | Project COMMISSIONED_BY corroboration | Medium | Operator boundary statement at Wave 3 | 3 |
| ME-W1C-02 | Production public URL | Low | Operator intake when known | 4 |
| ME-W1C-05 | Corporate domain / registrar | Low | Registrar E1 or defer OWNS | 5 / 5B |
| W1C-D-05 | Site title vs CC name | Low | Website register note | 4 |
| EV-EAR-GAP-01 | No EAR snapshot | Medium | Mode 0/1 acquisition per EV-EAR-01 | EAR pilot |
| EV-OCP-GAP-01 | Run 5 file-manifest | Medium | Beget backup export or SFTP | EAR → OCPilot |

---

## 12. Duplicate review register

| review_id | pair | verdict | blocking |
|-----------|------|---------|----------|
| SIBCAR-OS-D-01 | ORG-0006 vs ORG-0005 / SITE-001 on BZPM | **Distinct** | No |
| SIBCAR-OS-D-02 | SITE-001 vs ORG-0006 | **Class boundary** | No |
| SIBCAR-OS-D-03 | «Автосалон СИБКАР» vs «СибКар» | **Open — low** | No |
| SIBCAR-OS-D-04 | REL-0041 vs project edges | **Complementary** | No |
| SIBCAR-OS-D-05 | Multi-project on TEST hostname | **Single project** | No |

---

## 13. Recommended execution sequence register

| seq | wave | tranche | primary deliverable | readiness | depends_on |
|-----|------|---------|---------------------|-----------|------------|
| **1** | Wave 3 | SIBCAR Project population | 1 × PRJ-* (A01) | **PARTIAL** | ORG-0006 active ✓ |
| **2** | Wave 3B | SIBCAR Project ↔ Org | COMMISSIONED_BY + EXECUTES | **PARTIAL** | Seq 1 |
| **3** | Wave 4 | SIBCAR Website population | 1 × WEB-* TEST | **PARTIAL** | Seq 1 |
| **4** | Wave 4B | SIBCAR Website rels | BELONGS_TO + OWNS | **PARTIAL** | Seq 2, 3 |
| **5** | Wave 5 | SIBCAR Domain population | 1 × DOM-* TEST | **PARTIAL** | Seq 3 |
| **6** | Wave 5B | SIBCAR Domain rels | PRIMARY_DOMAIN; OWNS defer | **PARTIAL** | Seq 4, 5 |
| — | EAR | SITE-001 acquisition | Published snapshot | **BLOCKED** | Operator path |
| — | OCPilot | Run 5 resume | Audit artifacts | **BLOCKED** | EAR LK-EAR-01 |
| *(done)* | Wave 6B | CLIENT_OF | REL-0041 | **READY** ✓ | — |

**Estimated id slots at population (not assigned):** PRJ-0011 · WEB-0010 · DOM-0005 *(sequential estimate — steward confirms)*.

---

## 14. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md) | Full audit narrative |
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-SUMMARY-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-SUMMARY-v1.md) | Executive summary |
| [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | REL-0041 attested row |

---

*ATLAS SIBCAR Operational Slice Register v1 — documentation only.*
