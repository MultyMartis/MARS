# ATLAS Wave 3 Project Population v1

**Status:** **documented** — Wave 3 canonical Project population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) · [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) · [ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md)  
**Is not:** runtime, API, automation, database schema, relationship attestation, Wave 3B execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization relationships: **COMPLETE**
- Population verdict: **READY FOR WAVE 3 PROJECT POPULATION**

**Binding operator correction (Wave 3):**

- **HomeGateway, WPilot, OCPilot, MIG, ORCA, ATLAS, NOVA, OPS** — MARS systems/programs/registry infrastructure (`registry/project-registry.md`); **не** ATLAS Project records.
- **Allowed internal ATLAS Project:** **MARS** (`PRJ-0001`) — overall strategic ecosystem initiative container.
- **Project population now. Project relationships later** (Wave 3B).

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Project** для Wave 3: состав, классификация, lifecycle, evidence, org context, candidate relationships для Wave 3B, границы foundation.

**Normative scope Wave 3:**

```text
Project entity intake + attestation plan
Wave 3B (отдельный пакет): Project ↔ Organization, Website ↔ Project — только после active Project endpoints
```

---

## 2. Population roster (canonical)

Источник: [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) (лист `Projects`, `Websites`, `Relationships`).  
Draft lifecycle в dataset — **не** canonical registry state до attestation.

### 2.1 Summary table

| project_id | canonical_name | population_slice | lifecycle_state | commissioning_org | execution_org | attestation readiness |
|------------|----------------|------------------|-----------------|-------------------|---------------|----------------------|
| PRJ-0001 | MARS | **internal** | **active** | **SAFE UNKNOWN** *(internal)* | ORG-0002 MetaCode *(display)* | **ready** |
| PRJ-0004 | Редизайн gktriumph.ru | **client_delivery** | **deprecated** | ORG-0004 Триумф | ORG-0001 Полигон | **ready** |
| PRJ-0005 | Грузотакси | **client_delivery** | **active** | ORG-0004 Триумф | ORG-0001 Полигон | **ready** |
| PRJ-0006 | SEO gktriumph.ru | **client_delivery** | **active** | ORG-0004 Триумф | ORG-0001 Полигон | **ready** |
| PRJ-0007 | Блог gktriumph.ru | **client_delivery** | **active** | ORG-0004 Триумф | ORG-0001 Полигон | **ready** |
| PRJ-0008 | Манипулятор | **client_delivery** | **active** | ORG-0004 Триумф | ORG-0001 Полигон | **ready** |

**Population slice** — intake classification (не новый тип entity).  
**Commissioning / execution org** — display context from dataset; structural edges **deferred** to Wave 3B.

---

## 3. Per-project analysis

### 3.1 Internal — PRJ-0001 MARS

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0001 |
| **canonical_name** | MARS |
| **lifecycle_state** | **active** — internal long-term strategic initiative |
| **owning / commissioning organization** | **SAFE UNKNOWN** — no external client; internal ecosystem container |
| **execution organization** | ORG-0002 Агентство «МетаКод» *(dataset executor; cross-org delivery via Polygon/MetaCode — edges in 3B)* |
| **related people (informational)** | PER-0001 Русецкий А. А. — program owner / steward context |
| **evidence basis** | **E0** operator-direct; repo structural evidence (`README.md`, `governance/`, `registry/project-registry.md` boundary E-17); dataset Projects sheet |
| **scope notes** | Overall MARS strategic ecosystem — **not** a MARS `project_id` registry row. Distinct from program packs (`atlas`, `mig`, `orca`, …). |
| **attestation readiness** | **Ready** |

### 3.2 Triumph — PRJ-0004 Редизайн gktriumph.ru

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0004 |
| **canonical_name** | Редизайн gktriumph.ru |
| **lifecycle_state** | **deprecated** — completed delivery; structural retire per LT-P01 ([ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) §5.3) |
| **owning / commissioning organization** | ORG-0004 ООО «Триумф» |
| **execution organization** | ORG-0001 Веб-студия «Полигон» |
| **related people (informational)** | PER-0004 Макарова (client contact); PER-0006 Вагин (signatory); PER-0005 Подзолков (IT); PER-0001 (delivery steward) |
| **evidence basis** | **E1** dataset + live property WEB-0006 `gktriumph.ru` (WP + The7 + WPBakery + Custom); operator note: завершённый редизайн |
| **scope notes** | Deliverable site remains **active** (WEB-0006); project container **deprecated** — initiative complete, site persists under org. |
| **attestation readiness** | **Ready** |

### 3.3 Triumph — PRJ-0005 Грузотакси

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0005 |
| **canonical_name** | Грузотакси |
| **lifecycle_state** | **active** — ongoing landing + Yandex Direct advertising |
| **owning / commissioning organization** | ORG-0004 Триумф |
| **execution organization** | ORG-0001 Полигон |
| **related people (informational)** | PER-0004, PER-0005, PER-0006 (client); PER-0001 (delivery); MIG pilot context — **tooling on project**, not separate ATLAS Project |
| **evidence basis** | **E1** WEB-0008 `gruzotaxi-triumph.ru`; dataset; MIG pilot prep `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` (proposal support only — AT-E-03) |
| **scope notes** | Landing + реклама; distinct from ORG-0004 and from MIG program pack. MIG sessions reference this project container — not duplicate Project entity. |
| **attestation readiness** | **Ready** |

### 3.4 Triumph — PRJ-0006 SEO gktriumph.ru

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0006 |
| **canonical_name** | SEO gktriumph.ru |
| **lifecycle_state** | **active** — ongoing SEO promotion |
| **owning / commissioning organization** | ORG-0004 Триумф |
| **execution organization** | ORG-0001 Полигон |
| **related people (informational)** | PER-0008 Денис Леонов *(i-SEO; dataset notes SEO execution)*; PER-0004, PER-0006 (client); PER-0001 (steward) |
| **evidence basis** | **E1** primary site WEB-0006 `gktriumph.ru`; dataset Projects/Websites; operator context |
| **scope notes** | SEO initiative on main Triumph site — **not** a separate Website entity. No task/sprint status in ATLAS. |
| **attestation readiness** | **Ready** |

### 3.5 Triumph — PRJ-0007 Блог gktriumph.ru

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0007 |
| **canonical_name** | Блог gktriumph.ru |
| **lifecycle_state** | **active** — live blog property under ongoing initiative |
| **owning / commissioning organization** | ORG-0004 Триумф |
| **execution organization** | ORG-0001 Полигон |
| **related people (informational)** | PER-0008 Денис Леонов *(dataset: assembled on WP)*; client contacts PER-0004, PER-0005, PER-0006 |
| **evidence basis** | **E1** WEB-0007 `blog.gktriumph.ru` (WordPress); dataset |
| **scope notes** | Blog subsite grouped under this project; WEB-0007 link deferred to Wave 3B BELONGS_TO. |
| **attestation readiness** | **Ready** |

### 3.6 Triumph — PRJ-0008 Манипулятор

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0008 |
| **canonical_name** | Манипулятор |
| **lifecycle_state** | **active** — landing + advertising; first Website Factory / ORCA operational case |
| **owning / commissioning organization** | ORG-0004 Триумф |
| **execution organization** | ORG-0001 Полигон |
| **related people (informational)** | PER-0004, PER-0005, PER-0006 (client); PER-0001 (delivery steward) |
| **evidence basis** | **E1** WEB-0009 `manipulator-triumph.ru`; dataset; `projects/triumph-manipulator-landing/` (MARS program pack — **not** duplicate ATLAS Project) |
| **scope notes** | MARS `triumph-manipulator-landing` program pack documents delivery — ATLAS Project is structural container PRJ-0008 only. |
| **attestation readiness** | **Ready** |

---

## 4. Lifecycle decisions

| Rule | Application in Wave 3 |
|------|-------------------------|
| Completed delivery → **deprecated**, not `done` / `closed` | **PRJ-0004** — redesign complete |
| Active ongoing work → **active** | **PRJ-0005..0008** |
| Internal long-term initiative → **active** | **PRJ-0001** MARS |
| No operational task statuses (To Do, In Progress, Completed ticket) | All projects — structural lifecycle only ([ATLAS-LIFECYCLE-MODEL-v1.md](../foundation/ATLAS-LIFECYCLE-MODEL-v1.md) LC-BAN-01) |
| Deprecated project + active website | **PRJ-0004** deprecated; **WEB-0006** remains active — valid pattern |

---

## 5. Explicit exclusions

### 5.1 MARS program registry — not ATLAS Projects

| MARS `project_id` | Treatment | Rationale |
|-------------------|-----------|-----------|
| `atlas` | **Excluded** | Registry infrastructure — E-17 |
| `mig` | **Excluded** | MARS program pack — consumer may reference PRJ-0005 |
| `orca` | **Excluded** | MARS program pack |
| `wpilot` | **Excluded** | MARS program pack |
| `ocpilot` | **Excluded** | MARS program pack |
| `nova` | **Excluded** | MARS program pack |
| `ops` | **Excluded** | MARS program pack |
| `homegateway-v4-ai` | **Excluded** | MARS program pack |
| `mars-website-factory` | **Excluded** | Methodology program — not client initiative container |
| `metabot-seo-content-agent` | **Excluded** | External workflow documentation pack |
| `triumph-manipulator-landing` | **Excluded** | Delivery documentation for **PRJ-0008** — not second Project |
| `ear-runtime`, `mars-survivability`, … | **Excluded** | Engineering/operational MARS packs |

**Namespace rule:** MARS `project_id` (`registry/project-registry.md`) ≠ ATLAS `PRJ-*` ([ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) §4).

### 5.2 Other rejected candidates

| Candidate | Treatment | Reason |
|-----------|-----------|--------|
| MIG Pilot «Триумф / Грузотакси / Краснодар» as Project | **Rejected** | Research session cluster on **PRJ-0005** — W3-D-03 |
| Triumph Organization (ORG-0004) as Project | **Rejected** | Org ≠ initiative ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3) |
| PRJ-0002, PRJ-0003 | **Not in dataset** | No evidence — not minted |
| Website entities as Projects | **Rejected** | WEB-* is Wave 4 |

---

## 6. Candidate relationships for Wave 3B

**Not attested in Wave 3.** Prepared for separate Wave 3B population pass.

### 6.1 Project → Organization COMMISSIONED_BY

| Draft rel_id | source_project | target_organization | Notes |
|--------------|----------------|---------------------|-------|
| REL-0017 | PRJ-0004 | ORG-0004 Триумф | Deprecated project — edge may attest **active** with historical structural truth |
| REL-0019 | PRJ-0005 | ORG-0004 | |
| REL-0021 | PRJ-0006 | ORG-0004 | |
| REL-0023 | PRJ-0007 | ORG-0004 | |
| REL-0025 | PRJ-0008 | ORG-0004 | |
| *(TBD)* | PRJ-0001 MARS | — | **No COMMISSIONED_BY** — internal; sponsor **SAFE UNKNOWN** unless owner adds edge |

### 6.2 Organization → Project EXECUTES

| Draft rel_id | source_organization | target_project | Notes |
|--------------|---------------------|----------------|-------|
| REL-0018 | ORG-0001 Полигон | PRJ-0004 | |
| REL-0020 | ORG-0001 Полигон | PRJ-0005 | |
| REL-0022 | ORG-0001 Полигон | PRJ-0006 | |
| REL-0024 | ORG-0001 Полигон | PRJ-0007 | |
| REL-0026 | ORG-0001 Полигон | PRJ-0008 | |
| *(TBD)* | ORG-0002 MetaCode | PRJ-0001 | Dataset executor — steward review at 3B |

### 6.3 Website → Project BELONGS_TO

| Draft rel_id | source_website | target_project | Wave 4 prerequisite |
|--------------|----------------|----------------|---------------------|
| REL-0027 | WEB-0006 gktriumph.ru | PRJ-0004 | WEB-0006 **active** at Wave 4 |
| REL-0029 | WEB-0008 gruzotaxi-triumph.ru | PRJ-0005 | |
| REL-0028 | WEB-0007 blog.gktriumph.ru | PRJ-0007 | |
| REL-0030 | WEB-0009 manipulator-triumph.ru | PRJ-0008 | |
| — | WEB-0006 (main site) | PRJ-0006 SEO | **Not in dataset** — candidate for 3B review (SEO on main site) |

**Wave 3B ordering note:** COMMISSIONED_BY + EXECUTES may proceed after Project attestation; BELONGS_TO edges require **active** Website endpoints (Wave 4) or **proposed** website with explicit steward policy per W3-R-03.

---

## 7. Dataset reconciliation notes

| Item | Treatment in Wave 3 |
|------|---------------------|
| Dataset lifecycle on Projects sheet | **Draft only** — re-attest under Wave 3 governance |
| Identifier model exemplar «грузотакси pilot → PRJ-0001» | **Superseded** — PRJ-0001 = MARS; gruzotaxi = **PRJ-0005** |
| REL-0016 CLIENT_OF ORG-0004 → ORG-0001 | **Still Wave 6** — not Wave 3B |
| MIG session artifacts | Proposal support only — not Project mint evidence |

---

## 8. Foundation consistency

| Foundation doc | Wave 3 alignment |
|----------------|------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3 Project | Initiative container — not PM/tasks — **yes** |
| [ATLAS-BOUNDARIES-v1.md](../foundation/ATLAS-BOUNDARIES-v1.md) E-17 | MARS program ids excluded — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | `active`, `deprecated` only — no `completed`/`closed` — **yes** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | PRJ-0004 deprecated not “done” — **yes** |
| [ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) | PRJ-* namespace separate from MARS project_id — **yes** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) | Wave 3 before Wave 4 websites — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required — **yes** |

**No new entity types.** **No foundation modifications.**

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Canonical project roster table |
| [ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md) | Attestation sequence and verdict |
| [ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md) | Org/Person endpoints |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |
