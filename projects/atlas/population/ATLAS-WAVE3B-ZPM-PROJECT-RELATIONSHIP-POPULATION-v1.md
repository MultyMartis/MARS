# ATLAS Wave 3B ZPM Project Relationship Population v1

**Status:** **documented** — canonical Project ↔ Organization relationship population plan for Wave 3B ZPM tranche (ORG-0005).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ** · LE-0004  
**Parent:** [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 4 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- Wave 3 ZPM Project attestation: **COMPLETE** — AT-W3-ZPM-01..02
- Population verdict: **READY FOR WAVE 3B ZPM PROJECT RELATIONSHIP POPULATION**

---

## 1. Purpose

Зафиксировать **канонический план population** набора **Project ↔ Organization** relationships для Wave 3B tranche **ZPM** (ORG-0005): состав рёбер, типы, evidence basis, lifecycle intent, deferred items, границы foundation.

**Normative scope Wave 3B ZPM:**

```text
Project ↔ Organization relationships only (COMMISSIONED_BY + EXECUTES)
ZPM client delivery projects only (PRJ-0009, PRJ-0010)
No Person ↔ Project
No Website ↔ Project BELONGS_TO
No Organization ↔ Organization CLIENT_OF
No Website / Domain entities
No new entity types
No new relationship families
```

**Binding operator scope (this mission):**

- **REL-ZPM-PJ-01..04** — approved list only; no additional Project↔Org edges.
- **PRJ-0010 deprecated** — historical COMMISSIONED_BY / EXECUTES allowed per LT-P01 (Triumph PRJ-0004 analog).
- **REL-0016** CLIENT_OF ORG-0005 → ORG-0001 — **deferred** to Wave 6.
- Person ↔ Project — **не создавать**.

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **4** |
| Project endpoints (ZPM) | **2** (PRJ-0009 **active**, PRJ-0010 **deprecated**) |
| Organization endpoints (active) | **2** (ORG-0001, ORG-0005) |
| Relationship types used | **COMMISSIONED_BY**, **EXECUTES** |

### 2.1 Summary table

| relationship_id | source_id | target_id | relationship_type | project | attestation readiness |
|-----------------|-----------|-----------|-------------------|---------|-----------------------|
| REL-ZPM-PJ-01 | PRJ-0009 Каталог-платформа bzpm.ru | ORG-0005 ЗПМ | **COMMISSIONED_BY** | PRJ-0009 | **ready** |
| REL-ZPM-PJ-02 | ORG-0001 Полигон | PRJ-0009 Каталог-платформа bzpm.ru | **EXECUTES** | PRJ-0009 | **ready** |
| REL-ZPM-PJ-03 | PRJ-0010 Сайт bzpm.ru (исходная версия) | ORG-0005 ЗПМ | **COMMISSIONED_BY** | PRJ-0010 | **ready** |
| REL-ZPM-PJ-04 | ORG-0001 Полигон | PRJ-0010 Сайт bzpm.ru (исходная версия) | **EXECUTES** | PRJ-0010 | **ready** |

---

## 3. Per-relationship analysis

### 3.1 PRJ-0009 Каталог-платформа bzpm.ru — REL-ZPM-PJ-01, REL-ZPM-PJ-02

#### REL-ZPM-PJ-01 — COMMISSIONED_BY

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-PJ-01 |
| **source_id** | PRJ-0009 Каталог-платформа bzpm.ru |
| **target_id** | ORG-0005 ЗПМ |
| **relationship_type** | **COMMISSIONED_BY** |
| **attestation_basis** | E0 EV-ZPM-OP-ACT-01; ORG-0005 **active** (AT-W1B-01); PRJ-0009 **active** (AT-W3-ZPM-01); commissioning org display field from Wave 3 population |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Ongoing catalog-platform client delivery; `bzpm.ru` property deferred to Wave 4 WEB-* |

#### REL-ZPM-PJ-02 — EXECUTES

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-PJ-02 |
| **source_id** | ORG-0001 Полигон |
| **target_id** | PRJ-0009 Каталог-платформа bzpm.ru |
| **relationship_type** | **EXECUTES** |
| **attestation_basis** | E0 EV-ZPM-OP-ACT-01; ORG-0001 **active** (Wave 1); PRJ-0009 **active** (AT-W3-ZPM-01); operator: Polygon active WIP on catalog rebuild |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Polygon delivery org for ZPM catalog platform; PER-0014 primary operational contact (REL-ZPM-02) — no Person→Project edge |

### 3.2 PRJ-0010 Сайт bzpm.ru (исходная версия) — REL-ZPM-PJ-03, REL-ZPM-PJ-04

#### REL-ZPM-PJ-03 — COMMISSIONED_BY

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-PJ-03 |
| **source_id** | PRJ-0010 Сайт bzpm.ru (исходная версия) |
| **target_id** | ORG-0005 ЗПМ |
| **relationship_type** | **COMMISSIONED_BY** |
| **attestation_basis** | E0 EV-ZPM-OP-HIST-01; ORG-0005 **active** (AT-W1B-01); PRJ-0010 **deprecated** (AT-W3-ZPM-02); completed delivery ~5y ago; LT-P01 historical structural truth |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Deprecated project endpoint — edge attests historical commissioning; Triumph analog REL-0017 (PRJ-0004 → ORG-0004) |

#### REL-ZPM-PJ-04 — EXECUTES

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-PJ-04 |
| **source_id** | ORG-0001 Полигон |
| **target_id** | PRJ-0010 Сайт bzpm.ru (исходная версия) |
| **relationship_type** | **EXECUTES** |
| **attestation_basis** | E0 EV-ZPM-OP-HIST-01; ORG-0001 **active** (Wave 1); PRJ-0010 **deprecated** (AT-W3-ZPM-02); operator: Polygon historical delivery (WP + The7 + Custom) |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Completed delivery — EXECUTES edge remains structurally valid; Triumph analog REL-0018 (ORG-0001 → PRJ-0004) |

---

## 4. Commercial graph discipline — ZPM / Polygon

```text
PRJ-0009, PRJ-0010 ──COMMISSIONED_BY──► ORG-0005 ЗПМ
ORG-0001 Полигон ──EXECUTES──► PRJ-0009, PRJ-0010
```

**Paired edge rule:** Each ZPM project receives **one** COMMISSIONED_BY (client) and **one** EXECUTES (delivery org) — independent REL records per [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md).

**Not in this pass:** ORG-0005 ──CLIENT_OF──► ORG-0001 (REL-0016) — Wave 6 commercial org↔org family.

---

## 5. Validation review

### 5.1 Endpoint lifecycle verification

| Endpoint | Required state | Source act | Verified |
|----------|----------------|------------|----------|
| **ORG-0005** ЗПМ | **active** | AT-W1B-01 | **Pass** |
| **ORG-0001** Полигон | **active** | Wave 1 attestation | **Pass** |
| **PRJ-0009** | **active** | AT-W3-ZPM-01 | **Pass** |
| **PRJ-0010** | **deprecated** | AT-W3-ZPM-02 | **Pass** |

### 5.2 Historical project relationships (LT-P01)

| Check | Analysis | Verdict |
|-------|----------|---------|
| PRJ-0010 **deprecated** endpoint | COMMISSIONED_BY + EXECUTES attest structural truth — not lifecycle promotion | **Pass** — LT-P01 |
| Triumph precedent | PRJ-0004 **deprecated** + REL-0017/0018 **active** | **Pass** — pattern match |
| Relationship lifecycle vs Project lifecycle | Edges **active**; project **deprecated** — independent dimensions | **Pass** |

### 5.3 Duplicate edge review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **ZPM-3B-D-01** | REL-ZPM-PJ-01 vs REL-ZPM-PJ-03 — same target ORG-0005 | **Not duplicate** — distinct source projects | No |
| **ZPM-3B-D-02** | REL-ZPM-PJ-02 vs REL-ZPM-PJ-04 — same source ORG-0001 | **Not duplicate** — distinct target projects | No |
| **ZPM-3B-D-03** | vs Triumph REL-0017..0026 | **Distinct org** ORG-0005 vs ORG-0004 | No |
| **ZPM-3B-D-04** | vs Wave 2B REL-ZPM-01..02 | **Distinct family** Person→Org vs Project↔Org | No |
| **ZPM-3B-D-05** | Duplicate COMMISSIONED_BY PRJ-0009 → ORG-0005 | **None** — single edge | No |
| **ZPM-3B-D-06** | Duplicate EXECUTES ORG-0001 → PRJ-0009 | **None** — single edge | No |

**Duplicate review summary:** **Pass**

### 5.4 Triumph graph conflict check

| Check | Result |
|-------|--------|
| ORG-0004 Triumph projects unaffected | **Pass** — REL-0017..0026 separate namespace |
| ORG-0001 shared executor — cross-client | **Pass** — Polygon executes for both Triumph and ZPM; distinct project endpoints |
| PRJ namespace PRJ-0009/0010 vs PRJ-0004..0008 | **Pass** — no ID collision |
| `bzpm.ru` vs `gktriumph.ru` hostname families | **Pass** — distinct client contexts |

---

## 6. Explicit exclusions and deferred relationships

| Item | Treatment | Target |
|------|-----------|--------|
| WEB-* `bzpm.ru` | **Do not create** | Wave 4 |
| DOM-* `bzpm.ru` | **Do not create** | Wave 5 |
| WEB → Project **BELONGS_TO** | **Deferred** | Wave 4B |
| REL-0016 ORG-0005 CLIENT_OF ORG-0001 | **Deferred** | Wave 6 |
| ORG-0005 **OWNS** / **PRIMARY_DOMAIN** | **Do not create** | Out of scope |
| Person → Project edges (PER-0014, PER-0015) | **Do not create** | Operator scope |
| Person ↔ Person | **Forbidden** | — |
| Organization ↔ Organization (other) | **Out of scope** | Wave 6+ |
| Organization → Website / Domain | **Do not create** | Waves 4–5 |
| ZPM-INTAKE-FUT-01..04 Project rows | **Held** | Future intake |

---

## 7. Foundation consistency

| Foundation doc | Wave 3B ZPM alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Directed Project↔Org edges; paired COMMISSIONED_BY + EXECUTES — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §3 | COMMISSIONED_BY (Project→Org), EXECUTES (Org→Project) in baseline — **yes** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target state **active** after steward attestation — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints PRJ-0009/0010 / ORG-0001/0005 attested — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship lifecycle `active`; deprecated PRJ-0010 valid endpoint — **yes** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | PRJ-0010 deprecated — historical edges attestable — **yes** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward attestation path — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required for canonical promotion — **yes** |

**No new entity types.** **No new relationship families** (Organization ↔ Project only).

---

## 8. SAFE UNKNOWN inventory

| ID | Topic | Severity | Blocks 3B-ZPM |
|----|-------|----------|---------------|
| **SU-ZPM-PRJ-01** | Historical contract / act dates (PRJ-0010) | Low | **No** |
| **SU-ZPM-PRJ-02** | Formal acceptance document (E1 upgrade path) | Low | **No** |
| **SU-ZPM-PRJ-03** | Deployment replace vs coexistence (`bzpm.ru`) | Medium | **No** — Wave 4/4B |
| **SU-ZPM-PRJ-06** | PER-0014 / PER-0015 on Project | Low | **No** — out of scope |
| **SU-ZPM-PRJ-07** | CLIENT_OF ORG-0005 → ORG-0001 | Medium | **No** — Wave 6 |
| **SU-ZPM-PRJ-08** | Production domain registrant ORG-0005 | Low | **No** — Wave 5 |
| **SU-W3B-ZPM-01** | WEB-* single vs dual BELONGS_TO for same hostname | Medium | **No** — Wave 4B policy |
| **SU-W3B-ZPM-02** | E0-only evidence tier for all 4 edges | Low | **No** — operator path sufficient |

**Blocking gaps remaining:** **None**

---

## 9. Readiness verdict

```text
READY FOR WAVE 3B ZPM PROJECT RELATIONSHIP ATTESTATION
```

**Conditions:**

1. All four approved relationships pass endpoint, duplicate, and Triumph conflict checks.
2. Attestation executes as **separate act** — population plan ≠ canonical until AT-W3B-ZPM-01..02.
3. Website / Domain entities and BELONGS_TO remain **Wave 4+**.
4. CLIENT_OF and Person→Project remain **excluded**.

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Canonical relationship roster table |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) | Project endpoint prerequisite |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-POPULATION-v1.md) | Core Wave 3B Triumph precedent |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 3B ZPM Project Relationship Population v1 — documentation only.*
