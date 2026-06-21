# ATLAS Wave 4B Website Relationship Population v1

**Status:** **documented** — first canonical Website relationship population plan.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) · [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 5 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Wave 3 Projects: **COMPLETE**
- Wave 3B Project → Organization: **COMPLETE**
- Wave 4 Website Population: **COMPLETE**
- Population verdict: **READY FOR WAVE 4B WEBSITE RELATIONSHIP POPULATION**

---

## 1. Purpose

Зафиксировать **канонический план population** первого набора **Website-family** relationships для Wave 4B: состав рёбер, типы, evidence basis, lifecycle intent, deferred items, границы foundation.

**Normative scope Wave 4B:**

```text
Website → Project BELONGS_TO (REL-0027..0031)
Organization → Website OWNS (REL-0032..0035)
Triumph client properties only (WEB-0006..0009)
No OPERATES in this pass
No Domain entities
No Website ↔ Domain edges
No Person ↔ Website
No Organization ↔ Organization CLIENT_OF
No new entity types
No new relationship families
No Foundation modifications
```

**Binding operator modeling decision:**

- **OWNS** (Organization → Website) — structural business ownership of web property identity.
- **BELONGS_TO** (Website → Project) — initiative grouping; one website may belong to multiple projects when attested.
- **OPERATES** — **deferred**; operations/support/maintenance responsibility may change over time and requires separate governance.

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **9** |
| Website endpoints | **4** (WEB-0006..0009) |
| Project endpoints (BELONGS_TO targets) | **5** (PRJ-0004..0008) |
| Organization endpoints (OWNS source) | **1** (ORG-0004 Триумф) |
| Relationship types used | **BELONGS_TO**, **OWNS** |
| Multi-project websites | **1** (WEB-0006 → PRJ-0004 + PRJ-0006) |

### 2.1 Summary table

| relationship_id | source_id | target_id | relationship_type | attestation readiness |
|-----------------|-----------|-----------|-------------------|-----------------------|
| REL-0027 | WEB-0006 gktriumph.ru | PRJ-0004 Редизайн gktriumph.ru | **BELONGS_TO** | **ready** |
| REL-0028 | WEB-0006 gktriumph.ru | PRJ-0006 SEO gktriumph.ru | **BELONGS_TO** | **ready** |
| REL-0029 | WEB-0007 blog.gktriumph.ru | PRJ-0007 Блог gktriumph.ru | **BELONGS_TO** | **ready** |
| REL-0030 | WEB-0008 gruzotaxi-triumph.ru | PRJ-0005 Грузотакси | **BELONGS_TO** | **ready** |
| REL-0031 | WEB-0009 manipulator-triumph.ru | PRJ-0008 Манипулятор | **BELONGS_TO** | **ready** |
| REL-0032 | ORG-0004 ООО «Триумф» | WEB-0006 gktriumph.ru | **OWNS** | **ready** |
| REL-0033 | ORG-0004 Триумф | WEB-0007 blog.gktriumph.ru | **OWNS** | **ready** |
| REL-0034 | ORG-0004 Триумф | WEB-0008 gruzotaxi-triumph.ru | **OWNS** | **ready** |
| REL-0035 | ORG-0004 Триумф | WEB-0009 manipulator-triumph.ru | **OWNS** | **ready** |

### 2.2 ID continuity note (dataset draft reconciliation)

Wave 1 dataset draft assigned REL-0027..0030 to four BELONGS_TO edges (WEB-0006..0009 → one project each). Wave 4B **operator-approved roster** inserts **REL-0028** for WEB-0006 → PRJ-0006 and **renumbers** subsequent BELONGS_TO ids:

| Draft rel_id (Wave 4 §6.1) | Wave 4B canonical rel_id | Change |
|----------------------------|--------------------------|--------|
| REL-0027 WEB-0006 → PRJ-0004 | REL-0027 | unchanged |
| *(TBD)* WEB-0006 → PRJ-0006 | **REL-0028** | **new — operator approved** |
| REL-0028 WEB-0007 → PRJ-0007 | **REL-0029** | renumbered |
| REL-0029 WEB-0008 → PRJ-0005 | **REL-0030** | renumbered |
| REL-0030 WEB-0009 → PRJ-0008 | **REL-0031** | renumbered |
| *(TBD)* ORG-0004 OWNS WEB-* | **REL-0032..0035** | minted at 4B |

---

## 3. Per-relationship analysis

### 3.1 WEB-0006 gktriumph.ru — REL-0027, REL-0028, REL-0032

#### REL-0027 — BELONGS_TO (redesign deliverable)

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0027 |
| **source_id** | WEB-0006 gktriumph.ru |
| **target_id** | PRJ-0004 Редизайн gktriumph.ru |
| **relationship_type** | **BELONGS_TO** |
| **attestation_basis** | E1 dataset Websites sheet + Projects sheet; WEB-0006 **active** (Wave 4); PRJ-0004 **deprecated** (Wave 3 — completed delivery); REL-0017 COMMISSIONED_BY context; live URL `https://gktriumph.ru`; EV-0005 Triumph CC |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Deliverable grouping — deprecated project container + active website is valid pattern (W4-LC-02); edge attests structural grouping, not project lifecycle |

#### REL-0028 — BELONGS_TO (SEO initiative)

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0028 |
| **source_id** | WEB-0006 gktriumph.ru |
| **target_id** | PRJ-0006 SEO gktriumph.ru |
| **relationship_type** | **BELONGS_TO** |
| **attestation_basis** | E1 dataset Projects sheet; WEB-0006 **active**; PRJ-0006 **active**; REL-0021 COMMISSIONED_BY context; operator-approved multi-project case; SEO scope on main property — no separate Website entity |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | **Approved multi-project website case** — not in dataset draft rel_id; resolves SU-W3B-04; coexists with REL-0027 |

#### REL-0032 — OWNS

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0032 |
| **source_id** | ORG-0004 ООО «Триумф» |
| **target_id** | WEB-0006 gktriumph.ru |
| **relationship_type** | **OWNS** |
| **attestation_basis** | E1 dataset org context; ORG-0004 **active** (Wave 1); WEB-0006 **active**; EV-0005 Triumph CC; client org owns corporate web property identity |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Structural business ownership — distinct from Polygon EXECUTES on projects; OPERATES for ORG-0001 **not created** |

### 3.2 WEB-0007 blog.gktriumph.ru — REL-0029, REL-0033

#### REL-0029 — BELONGS_TO

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0029 |
| **source_id** | WEB-0007 blog.gktriumph.ru |
| **target_id** | PRJ-0007 Блог gktriumph.ru |
| **relationship_type** | **BELONGS_TO** |
| **attestation_basis** | E1 dataset Websites sheet (draft REL-0028 → renumbered REL-0029); WEB-0007 **active**; PRJ-0007 **active**; REL-0023 COMMISSIONED_BY; live URL `https://blog.gktriumph.ru`; distinct property from WEB-0006 (EIR-W01) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Blog subsite initiative grouping |

#### REL-0033 — OWNS

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0033 |
| **source_id** | ORG-0004 Триумф |
| **target_id** | WEB-0007 blog.gktriumph.ru |
| **relationship_type** | **OWNS** |
| **attestation_basis** | E1 dataset; ORG-0004 **active**; WEB-0007 **active**; client org owns blog subsite property |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Subsite under Triumph brand — ownership at org level, not hostname-level Domain edge |

### 3.3 WEB-0008 gruzotaxi-triumph.ru — REL-0030, REL-0034

#### REL-0030 — BELONGS_TO

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0030 |
| **source_id** | WEB-0008 gruzotaxi-triumph.ru |
| **target_id** | PRJ-0005 Грузотакси |
| **relationship_type** | **BELONGS_TO** |
| **attestation_basis** | E1 dataset (draft REL-0029 → REL-0030); WEB-0008 **active**; PRJ-0005 **active**; REL-0019 COMMISSIONED_BY; live URL `https://gruzotaxi-triumph.ru`; MIG pilot prep (support only) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Yandex Direct landing property grouped under Грузотакси project |

#### REL-0034 — OWNS

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0034 |
| **source_id** | ORG-0004 Триумф |
| **target_id** | WEB-0008 gruzotaxi-triumph.ru |
| **relationship_type** | **OWNS** |
| **attestation_basis** | E1 dataset; ORG-0004 **active**; WEB-0008 **active**; EV-0005 Triumph CC |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Client-owned landing property |

### 3.4 WEB-0009 manipulator-triumph.ru — REL-0031, REL-0035

#### REL-0031 — BELONGS_TO

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0031 |
| **source_id** | WEB-0009 manipulator-triumph.ru |
| **target_id** | PRJ-0008 Манипулятор |
| **relationship_type** | **BELONGS_TO** |
| **attestation_basis** | E1 dataset (draft REL-0030 → REL-0031); WEB-0009 **active**; PRJ-0008 **active**; REL-0025 COMMISSIONED_BY; live URL `https://manipulator-triumph.ru`; Website Factory / ORCA case |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | MARS `triumph-manipulator-landing` program pack ≠ duplicate ATLAS Project |

#### REL-0035 — OWNS

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0035 |
| **source_id** | ORG-0004 Триумф |
| **target_id** | WEB-0009 manipulator-triumph.ru |
| **relationship_type** | **OWNS** |
| **attestation_basis** | E1 dataset; ORG-0004 **active**; WEB-0009 **active**; EV-0005 Triumph CC |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Client-owned manipulator landing property |

---

## 4. Multi-project website analysis — WEB-0006

```text
WEB-0006 gktriumph.ru
    ├── BELONGS_TO ──► PRJ-0004 Редизайн (deprecated project — deliverable container)
    └── BELONGS_TO ──► PRJ-0006 SEO (active project — ongoing initiative)

ORG-0004 Триумф ── OWNS ──► WEB-0006
```

| Question | Resolution |
|----------|------------|
| May one website BELONGS_TO multiple projects? | **Yes** — foundation cardinality allows when attested ([ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §6; Wave 4 §6.1) |
| Should WEB-0006 normalize to one project? | **No** — operator-approved; redesign deliverable and SEO initiative are distinct structural groupings on same property |
| Conflict with deprecated PRJ-0004? | **No** — W4-LC-02 / LT-P01: deprecated project + active website + active BELONGS_TO edge is valid |
| OWNS vs BELONGS_TO overlap? | **No conflict** — OWNS is org-level property identity; BELONGS_TO is project initiative grouping ([ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §5–6) |

---

## 5. Structural graph — Triumph pilot (post 4B)

```text
ORG-0004 Триумф ──OWNS──► WEB-0006..0009

WEB-0006 ──BELONGS_TO──► PRJ-0004 (deprecated)
WEB-0006 ──BELONGS_TO──► PRJ-0006 (active)
WEB-0007 ──BELONGS_TO──► PRJ-0007
WEB-0008 ──BELONGS_TO──► PRJ-0005
WEB-0009 ──BELONGS_TO──► PRJ-0008

(Prior Wave 3B — unchanged)
PRJ-0004..0008 ──COMMISSIONED_BY──► ORG-0004
ORG-0001 Полигон ──EXECUTES──► PRJ-0004..0008
```

**Not in this pass:** ORG-0001 ──OPERATES──► WEB-0006..0009 — deferred to future governance review.

---

## 6. Explicit exclusions and deferred relationships

| Item | Treatment | Target |
|------|-----------|--------|
| ORG-0001 OPERATES WEB-0006..0009 | **Do not create** | SAFE UNKNOWN — separate governance |
| REL-0016 ORG-0004 CLIENT_OF ORG-0001 | **Deferred** | Wave 6 |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN | **Do not create** | Wave 5 + 6C |
| Website → Domain | **Do not create** | Wave 5 |
| Domain → Website | **Do not create** | Wave 5 |
| Domain entities | **Do not mint** | Wave 5 |
| Person → Website | **Do not create** | Future expansion |
| Person → Project | **Do not create** | Future expansion |
| WEB-0001..0005 operator org sites | **Out of scope** | Separate future tranche |
| PRJ-0001 MARS edges | **Out of scope** | Internal governance |

---

## 7. Candidate relationships for Wave 5

| Candidate | Type | Endpoints | Prerequisite |
|-----------|------|-----------|--------------|
| DOM-* gktriumph.ru | Domain entity | — | Wave 5 Domain population |
| DOM-* blog.gktriumph.ru | Domain entity | — | Wave 5 |
| DOM-* gruzotaxi-triumph.ru | Domain entity | — | Wave 5 |
| DOM-* manipulator-triumph.ru | Domain entity | — | Wave 5 |
| DOM → WEB-0006 | **PRIMARY_DOMAIN** | gktriumph.ru | Domain attestation + Wave 6C |
| DOM → WEB-0007 | **PRIMARY_DOMAIN** | blog.gktriumph.ru | Wave 5 + 6C |
| DOM → WEB-0008 | **PRIMARY_DOMAIN** | gruzotaxi-triumph.ru | Wave 5 + 6C |
| DOM → WEB-0009 | **PRIMARY_DOMAIN** | manipulator-triumph.ru | Wave 5 + 6C |
| ORG-0004 → DOM-* | **OWNS** (domain) | registrar / CC evidence | Wave 5 |
| `www.gktriumph.ru` | SECONDARY_DOMAIN or redirect | WEB-0006 | Wave 5 hostname policy |

---

## 8. Foundation consistency

| Foundation doc | Wave 4B alignment |
|----------------|-------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Directed Website→Project and Org→Website edges — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §5–6 | OWNS (Org→Website), BELONGS_TO (Website→Project) in baseline — **yes** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target state **active** after steward attestation — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints WEB-* / PRJ-* / ORG-* attested — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship lifecycle `active`; deprecated PRJ-0004 valid BELONGS_TO target — **yes** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | PRJ-0004 deprecated — historical/grouping edges attestable — **yes** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4 | E1 for BELONGS_TO structural + OWNS (site) — **yes** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward attestation path; dataset draft ≠ canonical — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required for canonical promotion — **yes** |

**Cross-wave validation:**

| Prior wave doc | Endpoint check |
|----------------|----------------|
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | WEB-0006..0009 **active** — **Pass** |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | PRJ-0004..0008 endpoints — **Pass** |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | COMMISSIONED_BY pairs consistent — **Pass** |
| Wave 1 Organization register | ORG-0004 **active** — **Pass** |

**No new entity types.** **No new relationship families.** **No Foundation modifications.**

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Canonical relationship roster table |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | Website endpoints |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | COMMISSIONED_BY context |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |
