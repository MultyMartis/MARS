# ATLAS Wave 3B Shpigovsky Project Relationship Population v1

**Status:** **documented** — canonical Project ↔ Organization relationship population plan for Wave 3B Shpigovsky tranche (ORG-0008).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Organization anchor:** ORG-0008 **ООО «Сознание»**  
**Parent:** [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md) · [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 4 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1D Shpigovsky Organization ORG-0008: **active** — AT-W1D-SHPIG-01
- Wave 3 Shpigovsky Project attestation: **COMPLETE** — AT-W3-SHPIG-01
- Population verdict: **READY FOR WAVE 3B SHPIGOVSKY PROJECT RELATIONSHIP POPULATION**

**Binding operator scope (this tranche):**

- **REL-SHPIG-PJ-01..02** — approved list only; no additional Project↔Org edges.
- Person ↔ Project — **не создавать**.
- Website / Domain — **не создавать**.

---

## 1. Purpose

Зафиксировать **канонический план population** набора **Project ↔ Organization** relationships для Wave 3B tranche **Shpigovsky** (ORG-0008): состав рёбер, типы, evidence basis, lifecycle intent, deferred items.

**Normative scope Wave 3B Shpigovsky:**

```text
Project ↔ Organization relationships only (COMMISSIONED_BY + EXECUTES)
Shpigovsky client delivery project only (PRJ-0012)
No Person ↔ Project
No Website ↔ Project BELONGS_TO
No Organization ↔ Organization CLIENT_OF
No Website / Domain entities
```

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **2** |
| Project endpoints | **1** (PRJ-0012 **active**) |
| Organization endpoints (active) | **2** (ORG-0001, ORG-0008) |
| Relationship types used | **COMMISSIONED_BY**, **EXECUTES** |

### 2.1 Summary table

| relationship_id | source_id | target_id | relationship_type | project | attestation readiness |
|-----------------|-----------|-----------|-------------------|---------|-----------------------|
| REL-SHPIG-PJ-01 | PRJ-0012 Сайт shpigovsky.ru | ORG-0008 ООО «Сознание» | **COMMISSIONED_BY** | PRJ-0012 | **ready** |
| REL-SHPIG-PJ-02 | ORG-0001 Полигон | PRJ-0012 Сайт shpigovsky.ru | **EXECUTES** | PRJ-0012 | **ready** |

---

## 3. Per-relationship analysis

### 3.1 REL-SHPIG-PJ-01 — COMMISSIONED_BY

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SHPIG-PJ-01 |
| **source_id** | PRJ-0012 Сайт shpigovsky.ru |
| **target_id** | ORG-0008 ООО «Сознание» |
| **relationship_type** | **COMMISSIONED_BY** |
| **attestation_basis** | E0 EV-SHPIG-OP-01; ORG-0008 **active** (AT-W1D-SHPIG-01); PRJ-0012 **active** (AT-W3-SHPIG-01) |
| **evidence_tier** | **E0/E1** |
| **lifecycle_state (target)** | **active** |

### 3.2 REL-SHPIG-PJ-02 — EXECUTES

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SHPIG-PJ-02 |
| **source_id** | ORG-0001 Полигон |
| **target_id** | PRJ-0012 Сайт shpigovsky.ru |
| **relationship_type** | **EXECUTES** |
| **attestation_basis** | ORG-0001 **active** (Wave 1); PRJ-0012 **active**; E0 EV-SHPIG-OP-01 — Polygon delivery channel |
| **evidence_tier** | **E0** |
| **lifecycle_state (target)** | **active** |

---

## 4. Paired delivery verification

```text
PRJ-0012 ──COMMISSIONED_BY──► ORG-0008 ООО «Сознание»   (REL-SHPIG-PJ-01)
ORG-0001 Полигон ──EXECUTES──► PRJ-0012                 (REL-SHPIG-PJ-02)
```

---

## 5. Explicit exclusions

| Item | Treatment |
|------|-----------|
| CLIENT_OF ORG-0008 → ORG-0001 | **Deferred** — Wave 6 |
| WEB-* / DOM-* | **Excluded** — Waves 4–5 |
| Person → Project | **Excluded** |
| Foundation documents | **Not modified** |

---

## 6. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-POPULATION-v1.md) | Structural analog |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md) | ZPM tranche precedent |

---

*ATLAS Wave 3B Shpigovsky Project Relationship Population v1 — documentation only.*
