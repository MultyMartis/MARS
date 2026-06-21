# ATLAS Wave 3B Project Relationship Population v1

**Status:** **documented** — first canonical Project ↔ Organization relationship population plan.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) · [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 4 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Wave 3 Project Population: **COMPLETE**
- Population verdict: **READY FOR WAVE 3B PROJECT RELATIONSHIP POPULATION**

---

## 1. Purpose

Зафиксировать **канонический план population** первого набора **Project ↔ Organization** relationships для Wave 3B: состав рёбер, типы, evidence basis, lifecycle intent, deferred items, границы foundation.

**Normative scope Wave 3B:**

```text
Project ↔ Organization relationships only (COMMISSIONED_BY + EXECUTES)
Triumph client delivery projects only (PRJ-0004..0008)
No Person ↔ Project
No Website ↔ Project BELONGS_TO (unless explicitly proposed — not in this pass)
No Organization ↔ Organization CLIENT_OF
No PRJ-0001 MARS edges
No new entity types
No new relationship families
```

**Binding operator corrections (carried from Wave 3):**

- **PRJ-0001 MARS** — internal strategic ecosystem project; COMMISSIONED_BY / EXECUTES remain **SAFE UNKNOWN** until separate internal governance decision.
- **REL-0016** ORG-0004 CLIENT_OF ORG-0001 — **deferred** to Wave 6.
- **REL-0027..0030** Website → Project BELONGS_TO — **deferred** to Wave 4 coordination.

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **10** |
| Project endpoints (Triumph) | **5** (PRJ-0004..0008) |
| Organization endpoints (active) | **2** (ORG-0001, ORG-0004) |
| Relationship types used | **COMMISSIONED_BY**, **EXECUTES** |
| Projects excluded by design | **1** (PRJ-0001 MARS) |

### 2.1 Summary table

| relationship_id | source_id | target_id | relationship_type | project | attestation readiness |
|-----------------|-----------|-----------|-------------------|---------|-----------------------|
| REL-0017 | PRJ-0004 Редизайн gktriumph.ru | ORG-0004 Триумф | **COMMISSIONED_BY** | PRJ-0004 | **ready** |
| REL-0018 | ORG-0001 Веб-студия «Полигон» | PRJ-0004 Редизайн gktriumph.ru | **EXECUTES** | PRJ-0004 | **ready** |
| REL-0019 | PRJ-0005 Грузотакси | ORG-0004 Триумф | **COMMISSIONED_BY** | PRJ-0005 | **ready** |
| REL-0020 | ORG-0001 Полигон | PRJ-0005 Грузотакси | **EXECUTES** | PRJ-0005 | **ready** |
| REL-0021 | PRJ-0006 SEO gktriumph.ru | ORG-0004 Триумф | **COMMISSIONED_BY** | PRJ-0006 | **ready** |
| REL-0022 | ORG-0001 Полигон | PRJ-0006 SEO gktriumph.ru | **EXECUTES** | PRJ-0006 | **ready** |
| REL-0023 | PRJ-0007 Блог gktriumph.ru | ORG-0004 Триумф | **COMMISSIONED_BY** | PRJ-0007 | **ready** |
| REL-0024 | ORG-0001 Полигон | PRJ-0007 Блог gktriumph.ru | **EXECUTES** | PRJ-0007 | **ready** |
| REL-0025 | PRJ-0008 Манипулятор | ORG-0004 Триумф | **COMMISSIONED_BY** | PRJ-0008 | **ready** |
| REL-0026 | ORG-0001 Полигон | PRJ-0008 Манипулятор | **EXECUTES** | PRJ-0008 | **ready** |

---

## 3. Per-relationship analysis

### 3.1 PRJ-0004 Редизайн gktriumph.ru — REL-0017, REL-0018

#### REL-0017 — COMMISSIONED_BY

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0017 |
| **source_id** | PRJ-0004 Редизайн gktriumph.ru |
| **target_id** | ORG-0004 ООО «Триумф» |
| **relationship_type** | **COMMISSIONED_BY** |
| **attestation_basis** | E1 dataset Projects sheet; ORG-0004 **active** (Wave 1); PRJ-0004 **deprecated** (Wave 3 — completed delivery); EV-0005 `triumph/…2024.xlsx`; live property WEB-0006 `gktriumph.ru` |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Deprecated project endpoint — edge attests historical structural truth; commissioning org unchanged |

#### REL-0018 — EXECUTES

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0018 |
| **source_id** | ORG-0001 Веб-студия «Полигон» |
| **target_id** | PRJ-0004 Редизайн gktriumph.ru |
| **relationship_type** | **EXECUTES** |
| **attestation_basis** | E1 dataset executor field; ORG-0001 **active** (Wave 1); PRJ-0004 **deprecated**; delivery steward context PER-0001 → ORG-0001 OWNER (REL-0001) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Completed delivery — EXECUTES edge remains structurally valid for historical graph |

### 3.2 PRJ-0005 Грузотакси — REL-0019, REL-0020

#### REL-0019 — COMMISSIONED_BY

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0019 |
| **source_id** | PRJ-0005 Грузотакси |
| **target_id** | ORG-0004 Триумф |
| **relationship_type** | **COMMISSIONED_BY** |
| **attestation_basis** | E1 dataset; ORG-0004 **active**; PRJ-0005 **active** (Wave 3); WEB-0008 `gruzotaxi-triumph.ru`; EV-0005 Triumph CC |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Ongoing landing + Yandex Direct; MIG pilot references this container — not duplicate Project |

#### REL-0020 — EXECUTES

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0020 |
| **source_id** | ORG-0001 Полигон |
| **target_id** | PRJ-0005 Грузотакси |
| **relationship_type** | **EXECUTES** |
| **attestation_basis** | E1 dataset executor field; ORG-0001 **active**; PRJ-0005 **active**; MIG pilot prep `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` (proposal support only) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Polygon delivery org for Triumph client initiative |

### 3.3 PRJ-0006 SEO gktriumph.ru — REL-0021, REL-0022

#### REL-0021 — COMMISSIONED_BY

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0021 |
| **source_id** | PRJ-0006 SEO gktriumph.ru |
| **target_id** | ORG-0004 Триумф |
| **relationship_type** | **COMMISSIONED_BY** |
| **attestation_basis** | E1 dataset; ORG-0004 **active**; PRJ-0006 **active**; primary site WEB-0006 `gktriumph.ru` (SEO on main property — no separate Website entity for SEO scope) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | SEO initiative on main Triumph site; i-SEO team (PER-0008) participates operationally — no Person→Project edge in 3B |

#### REL-0022 — EXECUTES

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0022 |
| **source_id** | ORG-0001 Полигон |
| **target_id** | PRJ-0006 SEO gktriumph.ru |
| **relationship_type** | **EXECUTES** |
| **attestation_basis** | E1 dataset executor field; ORG-0001 **active**; PRJ-0006 **active**; operator context: Polygon as delivery org for Triumph SEO contract |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Dataset notes SEO execution via i-SEO persons — structural EXECUTES remains ORG-0001 per Wave 3 population |

### 3.4 PRJ-0007 Блог gktriumph.ru — REL-0023, REL-0024

#### REL-0023 — COMMISSIONED_BY

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0023 |
| **source_id** | PRJ-0007 Блог gktriumph.ru |
| **target_id** | ORG-0004 Триумф |
| **relationship_type** | **COMMISSIONED_BY** |
| **attestation_basis** | E1 dataset; ORG-0004 **active**; PRJ-0007 **active**; WEB-0007 `blog.gktriumph.ru` |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Blog subsite initiative; WEB-0007 BELONGS_TO deferred to Wave 4 |

#### REL-0024 — EXECUTES

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0024 |
| **source_id** | ORG-0001 Полигон |
| **target_id** | PRJ-0007 Блог gktriumph.ru |
| **relationship_type** | **EXECUTES** |
| **attestation_basis** | E1 dataset executor field; ORG-0001 **active**; PRJ-0007 **active**; dataset notes blog assembled on WP |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Polygon delivery for Triumph blog property |

### 3.5 PRJ-0008 Манипулятор — REL-0025, REL-0026

#### REL-0025 — COMMISSIONED_BY

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0025 |
| **source_id** | PRJ-0008 Манипулятор |
| **target_id** | ORG-0004 Триумф |
| **relationship_type** | **COMMISSIONED_BY** |
| **attestation_basis** | E1 dataset; ORG-0004 **active**; PRJ-0008 **active**; WEB-0009 `manipulator-triumph.ru`; EV-0005 Triumph CC |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Website Factory / ORCA operational case; MARS `triumph-manipulator-landing` pack ≠ duplicate ATLAS Project |

#### REL-0026 — EXECUTES

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0026 |
| **source_id** | ORG-0001 Полигон |
| **target_id** | PRJ-0008 Манипулятор |
| **relationship_type** | **EXECUTES** |
| **attestation_basis** | E1 dataset executor field; ORG-0001 **active**; PRJ-0008 **active**; `projects/triumph-manipulator-landing/` (MARS delivery pack — support only) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Polygon delivery for Triumph manipulator landing |

---

## 4. Commercial graph discipline — Triumph / Polygon

```text
PRJ-0004..0008 ──COMMISSIONED_BY──► ORG-0004 Триумф
ORG-0001 Полигон ──EXECUTES──► PRJ-0004..0008
```

**Paired edge rule:** Each Triumph project receives **one** COMMISSIONED_BY (client) and **one** EXECUTES (delivery org) — independent REL records per [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md).

**Not in this pass:** ORG-0004 ──CLIENT_OF──► ORG-0001 (REL-0016) — Wave 6 commercial org↔org family.

---

## 5. Explicit exclusions and deferred relationships

| Item | Treatment | Target |
|------|-----------|--------|
| PRJ-0001 MARS → COMMISSIONED_BY | **Do not create** | Internal governance decision |
| ORG-0002 MetaCode → PRJ-0001 EXECUTES | **Do not create** | SAFE UNKNOWN — dataset executor field not attested at 3B |
| REL-0016 ORG-0004 CLIENT_OF ORG-0001 | **Deferred** | Wave 6 |
| REL-0027 WEB-0006 → PRJ-0004 BELONGS_TO | **Deferred** | Wave 4 Website population |
| REL-0028 WEB-0007 → PRJ-0007 BELONGS_TO | **Deferred** | Wave 4 |
| REL-0029 WEB-0008 → PRJ-0005 BELONGS_TO | **Deferred** | Wave 4 |
| REL-0030 WEB-0009 → PRJ-0008 BELONGS_TO | **Deferred** | Wave 4 |
| WEB-0006 → PRJ-0006 SEO BELONGS_TO | **Deferred** | Not in dataset draft — Wave 4 review |
| Person → Project edges | **Do not create** | Future expansion review |
| Person ↔ Person | **Forbidden** | — |
| Organization ↔ Organization (other) | **Out of scope** | Wave 6+ |

---

## 6. Foundation consistency

| Foundation doc | Wave 3B alignment |
|----------------|-------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Directed Project↔Org edges; paired COMMISSIONED_BY + EXECUTES — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §3 | COMMISSIONED_BY (Project→Org), EXECUTES (Org→Project) in baseline — **yes** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target state **active** after steward attestation — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints PRJ-* / ORG-* attested — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship lifecycle `active`; deprecated PRJ-0004 still valid endpoint — **yes** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | PRJ-0004 deprecated — historical edges attestable — **yes** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward attestation path; dataset draft ≠ canonical — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required for canonical promotion — **yes** |

**No new entity types.** **No new relationship families** (Organization ↔ Project only).

---

## 7. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Canonical relationship roster table |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md) | Organization endpoints |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |
