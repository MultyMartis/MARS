# ATLAS Wave 3 SIBCAR Project Register v1

**Status:** **documented** — canonical Project roster for Wave 3 SIBCAR tranche (**proposed**; attestation pending).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR** · LE-0005  
**Parent:** [ATLAS-WAVE3-SIBCAR-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-POPULATION-v1.md) · [ATLAS-WAVE3-SIBCAR-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ATTESTATION-v1.md) · [ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md)  
**Is not:** relationship registry, runtime export, database table, attested canonical export until attestation act completes.

---

## 1. Purpose

Канонический **реестр Project population** Wave 3 tranche **SIBCAR** (ORG-0006). Одна строка — одна approved Project record для attestation.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Lifecycle **active** *(target)* | **1** (PRJ-0011) |
| Lifecycle **deprecated** | **0** |
| Population slice **client_delivery** | **1** |
| Evidence **E0** | **1** |
| Future candidates held | **3** |
| Attestation | **Pending** — AT-W3-SIBCAR-01 |

---

## 2. Project roster — full table

| project_id | intake_label | canonical_name | population_slice | roster_priority | commissioning_org | execution_org | related_property | ocpilot_crosswalk | evidence_tier | evidence_ref | lifecycle_state *(target)* | attestation | notes |
|------------|--------------|----------------|------------------|-----------------|-------------------|---------------|------------------|-------------------|---------------|--------------|------------------------------|-------------|-------|
| PRJ-0011 | SIBCAR-INTAKE-CAND-A01 | Автосалон СИБКАР — OpenCart dealership | **client_delivery** | **P0** | ORG-0006 SIBCAR | ORG-0001 Полигон | `sibcar.new-site.space` *(WEB candidate)* | SITE-001 | **E0** | EV-W1C-02..03; EV-OCP-01..04 | **active** | AT-W3-SIBCAR-01 *(pending)* | OpenCart dealership WIP; TEST env; OCPilot first combat pilot context |

---

## 3. Project roster — by lifecycle target

### 3.1 Active (1)

| project_id | canonical_name | evidence_tier | evidence_ref | attestation |
|------------|----------------|---------------|--------------|-------------|
| PRJ-0011 | Автосалон СИБКАР — OpenCart dealership | **E0** | EV-W1C-02..03; EV-OCP-01..04 | AT-W3-SIBCAR-01 *(pending)* |

### 3.2 Deprecated (0)

*No historical delivery phase evidenced — contrast ZPM PRJ-0009 + PRJ-0010 dual-phase model.*

---

## 4. OCPilot crosswalk index (informational — not Wave 3 edges)

| ocpilot_id | entity_class | atlas_crosswalk | relationship to PRJ-0011 | wave |
|------------|--------------|-----------------|--------------------------|------|
| SITE-001 | OCPilot site_id | PRJ-0011 | Documentation linkage — engagement container | Wave 3 |
| `sibcar.new-site.space` | Website hostname candidate | Future WEB-* | Property candidate — not Project substitute | Wave 4 |

---

## 5. Excluded register (not in population set)

| Item | Reason | Belongs to |
|------|--------|------------|
| SIBCAR-INTAKE-FUT-01 Yandex Direct standalone | No distinct project boundary | Future intake |
| SIBCAR-INTAKE-FUT-02 Custom module development | Not started | Future intake |
| SIBCAR-INTAKE-FUT-03 PROD migration / launch | Public URL SAFE UNKNOWN | Future intake |
| OCPilot Run 5 read-only audit | MARS program context | **Rejected** — REJ-SIBCAR-PRJ-01 |
| SITE-001 as Project entity | Class boundary | **Rejected** — REJ-SIBCAR-PRJ-02 |
| ORG-0005 / BZPM engagement | Identity pollution | **Rejected** — COR-W1B-03 |
| Per-checkbox split (SEO, theme, …) | EFV-03 inference | **Rejected** |
| `sibcar.new-site.space` hostname alone | Website class | Wave 4 |
| ORG-0006 SIBCAR | Organization entity | Wave 1C |
| WEB-* / DOM-* | Out of operator scope | Waves 4–5 |
| PER-* Person rows | Out of operator scope | Wave 2C optional |

---

## 6. Evidence index

| Ref | Artifact | Projects supported |
|-----|----------|-------------------|
| EV-W1C-02 | OCPilot site-passport | PRJ-0011 — engagement context |
| EV-W1C-03 | OCPilot project-access-brief | PRJ-0011 — Business Goal + Planned Work |
| EV-OCP-01 | INTAKE-COMPLETE | PRJ-0011 — corroboration |
| EV-OCP-02 | AUDIT-CHARTER | Exclusion basis for Run 5 program row |
| EV-OCP-03 | project-site-registry | SITE-001 crosswalk |
| EV-OCP-04 | project-access-brief § Business Goal | PRJ-0011 — pilot narrative |
| EV-W1C-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | Org anchor only — ORG-0006 |
| AT-W1C-01 | [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | ORG-0006 **active** prerequisite |
| AT-W6B-02 | [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | REL-0041 vendor context |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 7. Duplicate review register

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| SIBCAR-PRJ-D-01 | PRJ-0011 vs SITE-001 | **Class boundary** — crosswalk only | No |
| SIBCAR-PRJ-D-02 | PRJ-0011 vs ORG-0006 | **Class boundary** | No |
| SIBCAR-PRJ-D-03 | vs ORG-0005 BZPM | **Distinct** — COR-W1B-03 | No |
| SIBCAR-PRJ-D-04 | vs PRJ-0009 ZPM | **Distinct org** | No |
| SIBCAR-PRJ-D-05 | Single vs multi-project checkboxes | **Not duplicate** — EFV-03 | No |
| SIBCAR-PRJ-D-06 | «Автосалон СИБКАР» vs «СибКар» | **Open — low** — W1C-D-05 | No |
| SIBCAR-PRJ-D-07 | Run 5 audit vs PRJ-0011 | **Distinct** — program excluded | No |
| SIBCAR-PRJ-D-08 | REL-0041 vs COMMISSIONED_BY | **Complementary** | No |

**Duplicate review summary:** **Pass**

---

## 8. SAFE UNKNOWN index

| id | topic | blocks_attestation |
|----|-------|-------------------|
| SU-SIBCAR-PRJ-01 | Production public URL | **No** |
| SU-SIBCAR-PRJ-02 | Contract / SOW artifact | **No** |
| SU-SIBCAR-PRJ-03 | Formal acceptance docs | **No** |
| SU-SIBCAR-PRJ-04 | Final canonical name strings | **No** |
| SU-SIBCAR-PRJ-05 | Custom module scope (FUT-02) | **No** |
| SU-SIBCAR-PRJ-06 | PROD migration (FUT-03) | **No** |
| SU-SIBCAR-PRJ-07 | Person contacts (Wave 2C) | **No** — out of scope |
| SU-W6B-04 | Project-level org edge corroboration | **No** — closes at Wave 3B |
| SU-SIBCAR-PRJ-08 | EAR published snapshot | **No** — cross-program |
| SU-SIBCAR-PRJ-09 | Credential channel confirmation | **No** |

---

## 9. Deferred register (Wave 3B+ and future intake)

| Item | Reason | Target wave |
|------|--------|-------------|
| REL-SIBCAR-PJ-01 COMMISSIONED_BY PRJ-0011 → ORG-0006 | Org edges deferred | **Wave 3B-SIBCAR** |
| REL-SIBCAR-PJ-02 EXECUTES ORG-0001 → PRJ-0011 | Org edges deferred | **Wave 3B-SIBCAR** |
| REL-SIBCAR-WB-01 BELONGS_TO WEB → PRJ-0011 | Website prerequisite | **Wave 4B** |
| SIBCAR-INTAKE-FUT-01..03 | No distinct boundary evidence | **Hold** |
| WEB-* TEST `sibcar.new-site.space` | Website class | **Wave 4** |
| DOM-* TEST hostname | Domain class | **Wave 5** |
| REL-0041 CLIENT_OF ORG-0006 → ORG-0001 | **Already attested** | Wave 6B — complete |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-SIBCAR-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-POPULATION-v1.md) | Per-project analysis and exclusions |
| [ATLAS-WAVE3-SIBCAR-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ATTESTATION-v1.md) | Attestation gates and verdict |
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md) | Source expansion audit |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Core Wave 3 roster PRJ-0001..0008 |
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | ZPM tranche PRJ-0009..0010 |

---

*ATLAS Wave 3 SIBCAR Project Register v1 — PRJ-0011 **proposed** pending attestation act AT-W3-SIBCAR-01.*
