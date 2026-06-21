# ATLAS Wave 3B SIBCAR Project Relationship Population v1

**Status:** **documented** — canonical Project ↔ Organization relationship population plan for Wave 3B SIBCAR tranche (ORG-0006).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR** · LE-0005  
**Parent:** [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 4 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1C SIBCAR Organization ORG-0006: **active** — AT-W1C-01
- Wave 6B Commercial REL-0041 ORG-0006 → ORG-0001 **CLIENT_OF**: **active** — AT-W6B-02
- Wave 3 SIBCAR Project attestation: **COMPLETE** — AT-W3-SIBCAR-01
- Population verdict: **READY FOR WAVE 3B SIBCAR PROJECT RELATIONSHIP POPULATION**

---

## 1. Purpose

Зафиксировать **канонический план population** набора **Project ↔ Organization** relationships для Wave 3B tranche **SIBCAR** (ORG-0006): состав рёбер, типы, evidence basis, lifecycle intent, deferred items, границы foundation.

**Normative scope Wave 3B SIBCAR:**

```text
Project ↔ Organization relationships only (COMMISSIONED_BY + EXECUTES)
SIBCAR client delivery project only (PRJ-0011)
No Person ↔ Project
No Website ↔ Project BELONGS_TO
No Organization ↔ Organization CLIENT_OF (already attested Wave 6B)
No Website / Domain entities
No new entity types
No new relationship families
```

**Binding operator scope (this mission):**

- **REL-SIBCAR-PJ-01..02** — approved list only; no additional Project↔Org edges.
- **REL-0041** CLIENT_OF ORG-0006 → ORG-0001 — **already attested** (Wave 6B); **не пересоздавать**.
- Person ↔ Project — **не создавать**.
- No deprecated historical project — unlike ZPM dual-phase PRJ-0009 + PRJ-0010.

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **2** |
| Project endpoints (SIBCAR) | **1** (PRJ-0011 **active**) |
| Organization endpoints (active) | **2** (ORG-0001, ORG-0006) |
| Relationship types used | **COMMISSIONED_BY**, **EXECUTES** |

### 2.1 Summary table

| relationship_id | source_id | target_id | relationship_type | project | attestation readiness |
|-----------------|-----------|-----------|-------------------|---------|-----------------------|
| REL-SIBCAR-PJ-01 | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | ORG-0006 SIBCAR | **COMMISSIONED_BY** | PRJ-0011 | **ready** |
| REL-SIBCAR-PJ-02 | ORG-0001 Полигон | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **EXECUTES** | PRJ-0011 | **ready** |

---

## 3. Per-relationship analysis

### 3.1 PRJ-0011 — REL-SIBCAR-PJ-01, REL-SIBCAR-PJ-02

#### REL-SIBCAR-PJ-01 — COMMISSIONED_BY

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SIBCAR-PJ-01 |
| **source_id** | PRJ-0011 Автосалон СИБКАР — OpenCart dealership |
| **target_id** | ORG-0006 SIBCAR |
| **relationship_type** | **COMMISSIONED_BY** |
| **attestation_basis** | E0 EV-W1C-02, EV-W1C-03, EV-OCP-01..04; ORG-0006 **active** (AT-W1C-01); PRJ-0011 **active** (AT-W3-SIBCAR-01); commissioning org display field from Wave 3 population |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Ongoing OpenCart dealership client delivery; `sibcar.new-site.space` property deferred to Wave 4 WEB-* |

#### REL-SIBCAR-PJ-02 — EXECUTES

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SIBCAR-PJ-02 |
| **source_id** | ORG-0001 Полигон |
| **target_id** | PRJ-0011 Автосалон СИБКАР — OpenCart dealership |
| **relationship_type** | **EXECUTES** |
| **attestation_basis** | E0 EV-W1C-03; ORG-0001 **active** (Wave 1); PRJ-0011 **active** (AT-W3-SIBCAR-01); REL-0041 + AT-W6B-02 vendor context *(informational)*; operator: Polygon active WIP on OpenCart dealership |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Polygon delivery org for SIBCAR engagement; ZPM analog REL-ZPM-PJ-02; no Person→Project edge |

---

## 4. Commercial graph discipline — SIBCAR / Polygon

```text
PRJ-0011 ──COMMISSIONED_BY──► ORG-0006 SIBCAR
ORG-0001 Полигон ──EXECUTES──► PRJ-0011
ORG-0006 SIBCAR ──CLIENT_OF──► ORG-0001 Полигон   (REL-0041 — Wave 6B; not re-minted)
```

**Paired edge rule:** PRJ-0011 receives **one** COMMISSIONED_BY (client) and **one** EXECUTES (delivery org) — independent REL records per [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md).

**Complementary, not duplicate:** REL-0041 **CLIENT_OF** (org↔org commercial) and REL-SIBCAR-PJ-01/02 (project structural) serve distinct relationship families — SIBCAR-PRJ-D-08 precedent.

**Not in this pass:** REL-0041 re-attestation — already **active** at Wave 6B.

---

## 5. Validation review

### 5.1 Endpoint lifecycle verification

| Endpoint | Required state | Source act | Verified |
|----------|----------------|------------|----------|
| **ORG-0006** SIBCAR | **active** | AT-W1C-01 | **Pass** |
| **ORG-0001** Полигон | **active** | Wave 1 attestation | **Pass** |
| **PRJ-0011** | **active** | AT-W3-SIBCAR-01 | **Pass** |

### 5.2 Paired delivery consistency

| Check | Analysis | Verdict |
|-------|----------|---------|
| COMMISSIONED_BY client = ORG-0006 | Matches PRJ-0011 display commissioning org | **Pass** |
| EXECUTES delivery org = ORG-0001 | Matches PRJ-0011 display execution org + REL-0041 vendor | **Pass** |
| Single project — one pair only | No second SIBCAR project phase evidenced | **Pass** |
| REL-0041 direction ORG-0006 → ORG-0001 | Consistent with Polygon as vendor for SIBCAR client | **Pass** |

### 5.3 Duplicate edge review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **SIBCAR-3B-D-01** | REL-SIBCAR-PJ-01 vs REL-0041 | **Not duplicate** — Project→Org vs Org→Org families | No |
| **SIBCAR-3B-D-02** | REL-SIBCAR-PJ-02 vs REL-0041 | **Not duplicate** — Org→Project vs Org→Org | No |
| **SIBCAR-3B-D-03** | vs ZPM REL-ZPM-PJ-01..04 | **Distinct org** ORG-0006 vs ORG-0005; distinct project PRJ-0011 | No |
| **SIBCAR-3B-D-04** | vs Triumph REL-0017..0026 | **Distinct org** ORG-0006 vs ORG-0004 | No |
| **SIBCAR-3B-D-05** | Duplicate COMMISSIONED_BY PRJ-0011 → ORG-0006 | **None** — single edge | No |
| **SIBCAR-3B-D-06** | Duplicate EXECUTES ORG-0001 → PRJ-0011 | **None** — single edge | No |

**Duplicate review summary:** **Pass**

### 5.4 Cross-tranche conflict check

| Check | Result |
|-------|--------|
| ORG-0004 Triumph projects unaffected | **Pass** — REL-0017..0026 separate namespace |
| ORG-0005 ZPM projects unaffected | **Pass** — REL-ZPM-PJ-01..04 separate namespace |
| ORG-0001 shared executor — cross-client | **Pass** — Polygon executes for Triumph, ZPM, and SIBCAR; distinct project endpoints |
| PRJ-0011 vs PRJ-0001..0010 | **Pass** — no ID collision |
| `sibcar.new-site.space` vs `bzpm.ru` / `gktriumph.ru` | **Pass** — distinct client contexts |

---

## 6. Explicit exclusions and deferred relationships

| Item | Treatment | Target |
|------|-----------|--------|
| WEB-* `sibcar.new-site.space` | **Do not create** | Wave 4 |
| DOM-* TEST hostname | **Do not create** | Wave 5 |
| WEB → Project **BELONGS_TO** (REL-SIBCAR-WB-01) | **Deferred** | Wave 4B |
| REL-0041 ORG-0006 CLIENT_OF ORG-0001 | **Already attested** | Wave 6B — complete |
| ORG-0006 **OWNS** / **PRIMARY_DOMAIN** | **Do not create** | Out of scope |
| Person → Project edges | **Do not create** | Operator scope |
| Person ↔ Person | **Forbidden** | — |
| Organization ↔ Organization (new) | **Out of scope** | Wave 6+ |
| Organization → Website / Domain | **Do not create** | Waves 4–5 |
| SIBCAR-INTAKE-FUT-01..03 Project rows | **Held** | Future intake |

---

## 7. Foundation consistency

| Foundation doc | Wave 3B SIBCAR alignment |
|----------------|--------------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Directed Project↔Org edges; paired COMMISSIONED_BY + EXECUTES — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §3 | COMMISSIONED_BY (Project→Org), EXECUTES (Org→Project) in baseline — **yes** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target state **active** after steward attestation — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints PRJ-0011 / ORG-0001/0006 attested — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship lifecycle `active` — **yes** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward attestation path — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required for canonical promotion — **yes** |

**No new entity types.** **No new relationship families** (Organization ↔ Project only). **No Foundation changes.**

---

## 8. SAFE UNKNOWN inventory

| ID | Topic | Severity | Blocks 3B-SIBCAR |
|----|-------|----------|------------------|
| **SU-SIBCAR-PRJ-01** | Production public URL | Medium | **No** — Wave 4 |
| **SU-SIBCAR-PRJ-02** | Contract / SOW artifact | Low | **No** |
| **SU-SIBCAR-PRJ-03** | Formal acceptance document | Low | **No** |
| **SU-SIBCAR-PRJ-06** | PROD migration / launch phase | Medium | **No** — future intake |
| **SU-SIBCAR-PRJ-07** | Person contacts on CC (Карандашов) | Low | **No** — Wave 2C optional |
| **SU-W3B-SIBCAR-01** | WEB-* BELONGS_TO policy for TEST hostname | Medium | **No** — Wave 4B |
| **SU-W3B-SIBCAR-02** | E0-only evidence tier for both edges | Low | **No** — operator path sufficient |
| **W1C-D-05** *(carry-forward)* | «Автосалон СИБКАР» vs «СибКар» CC alias | Low | **No** — Website intake note |

**Closed by Wave 3 attestation:**

| ID | Topic | Disposition |
|----|-------|-------------|
| **SU-W6B-04** | Project-level COMMISSIONED_BY / EXECUTES corroboration | **Closed** — PRJ-0011 endpoint attested; this pass supplies structural edges |

**Blocking gaps remaining:** **None**

---

## 9. Readiness verdict

```text
READY FOR WAVE 3B SIBCAR PROJECT RELATIONSHIP ATTESTATION
```

**Conditions:**

1. Both approved relationships pass endpoint, duplicate, and cross-tranche conflict checks.
2. Attestation executes as **separate act** — population plan ≠ canonical until AT-W3B-SIBCAR-01.
3. Website / Domain entities and BELONGS_TO remain **Wave 4+**.
4. REL-0041 CLIENT_OF remains **already attested** — not re-minted.
5. Person→Project remains **excluded**.

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Canonical relationship roster table |
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) | Project endpoint prerequisite |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md) | ZPM tranche precedent |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 3B SIBCAR Project Relationship Population v1 — documentation only.*
