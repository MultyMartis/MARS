# ATLAS Wave 3 Project Register v1

**Status:** **documented** — canonical Project roster after Wave 3 population (pending steward attestation act).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-PROJECT-POPULATION-v1.md) · [ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md)  
**Is not:** relationship registry, runtime export, database table, attested canonical export until attestation act completes.

---

## 1. Purpose

Канонический **реестр Project population** Wave 3. Одна строка — одна approved Project record для attestation.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **6** |
| Target **active** | **5** (PRJ-0001, 0005..0008) |
| Target **deprecated** | **1** (PRJ-0004) |
| Excluded MARS programs | **12+** (see Population §5) |
| Attestation readiness **ready** | **6** |

---

## 2. Population roster — full table

| project_id | canonical_name | population_slice | commissioning_org | execution_org | evidence_tier | lifecycle_state | attestation_readiness | notes |
|------------|----------------|------------------|---------------------|---------------|---------------|-----------------|----------------------|-------|
| PRJ-0001 | MARS | internal | **SAFE UNKNOWN** | ORG-0002 MetaCode | E0 | **active** | **ready** | Strategic ecosystem; not MARS `project_id` row |
| PRJ-0004 | Редизайн gktriumph.ru | client_delivery | ORG-0004 Триумф | ORG-0001 Полигон | E1 | **deprecated** | **ready** | Completed redesign; WEB-0006 persists |
| PRJ-0005 | Грузотакси | client_delivery | ORG-0004 Триумф | ORG-0001 Полигон | E1 | **active** | **ready** | WEB-0008; MIG pilot references this container |
| PRJ-0006 | SEO gktriumph.ru | client_delivery | ORG-0004 Триумф | ORG-0001 Полигон | E1 | **active** | **ready** | SEO on WEB-0006 — no separate site entity |
| PRJ-0007 | Блог gktriumph.ru | client_delivery | ORG-0004 Триумф | ORG-0001 Полигон | E1 | **active** | **ready** | WEB-0007 blog subsite |
| PRJ-0008 | Манипулятор | client_delivery | ORG-0004 Триумф | ORG-0001 Полигон | E1 | **active** | **ready** | WEB-0009; Website Factory / ORCA case |

---

## 3. Population roster — by slice

### 3.1 Internal (1)

| project_id | canonical_name | lifecycle_state | evidence_tier | attestation_readiness |
|------------|----------------|-----------------|---------------|----------------------|
| PRJ-0001 | MARS | **active** | E0 | **ready** |

### 3.2 Triumph client delivery (5)

| project_id | canonical_name | lifecycle_state | evidence_tier | attestation_readiness |
|------------|----------------|-----------------|---------------|----------------------|
| PRJ-0004 | Редизайн gktriumph.ru | **deprecated** | E1 | **ready** |
| PRJ-0005 | Грузотакси | **active** | E1 | **ready** |
| PRJ-0006 | SEO gktriumph.ru | **active** | E1 | **ready** |
| PRJ-0007 | Блог gktriumph.ru | **active** | E1 | **ready** |
| PRJ-0008 | Манипулятор | **active** | E1 | **ready** |

---

## 4. Related people index (informational — not Wave 3 edges)

| project_id | related_people | role context |
|------------|----------------|--------------|
| PRJ-0001 | PER-0001 | Program owner / steward |
| PRJ-0004 | PER-0004, PER-0005, PER-0006, PER-0001 | Client contacts + delivery steward |
| PRJ-0005 | PER-0004, PER-0005, PER-0006, PER-0001 | Client + delivery |
| PRJ-0006 | PER-0008, PER-0004, PER-0006, PER-0001 | SEO execution (Denis) + client + steward |
| PRJ-0007 | PER-0008, PER-0004, PER-0005, PER-0006 | Blog build (Denis) + client |
| PRJ-0008 | PER-0004, PER-0005, PER-0006, PER-0001 | Client + delivery |

Person ↔ Project relationships — **not in Wave 3 scope**; future expansion review only.

---

## 5. Excluded register (not in population set)

| Item | Reason | Belongs to |
|------|--------|------------|
| `atlas`, `mig`, `orca`, `wpilot`, `ocpilot`, `nova`, `ops`, `homegateway-v4-ai` | MARS program registry — E-17 | `registry/project-registry.md` |
| `mars-website-factory`, `triumph-manipulator-landing`, `metabot-seo-content-agent` | Program/documentation packs | MARS `projects/` |
| MIG Pilot «Триумф / Грузотакси / Краснодар» | Session cluster on PRJ-0005 | MIG consumer context |
| ORG-0004 Триумф | Organization entity | Wave 1 |
| WEB-0006..0009 | Website entities | Wave 4 |
| PRJ-0002, PRJ-0003 | Not in dataset / no evidence | — |

---

## 6. Evidence index (population references)

| Ref | Artifact | Projects supported |
|-----|----------|-------------------|
| E0 operator-direct | Steward / Owner attestation context | PRJ-0001 |
| Dataset Projects sheet | [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | PRJ-0001..0008 |
| Dataset Websites sheet | WEB-0006..0009 URL/platform | PRJ-0004..0008 |
| EV-0001, EV-0002 | Yandex Maps / Avito — ORG-0004 | Triumph org context (commissioning) |
| EV-0005 | `triumph/…2024.xlsx` | Client-side context |
| WEB-0006 | `https://gktriumph.ru` | PRJ-0004, PRJ-0006 |
| WEB-0007 | `https://blog.gktriumph.ru` | PRJ-0007 |
| WEB-0008 | `https://gruzotaxi-triumph.ru` | PRJ-0005 |
| WEB-0009 | `https://manipulator-triumph.ru` | PRJ-0008 |
| Repo README / governance | MARS ecosystem documentation | PRJ-0001 |
| `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` | MIG pilot prep | PRJ-0005 (support only) |
| `projects/triumph-manipulator-landing/` | Delivery pack | PRJ-0008 (support only) |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 7. Deferred register (Wave 3B+)

| Item | Reason | Target wave |
|------|--------|-------------|
| REL-0017..0026 COMMISSIONED_BY / EXECUTES | Project endpoints must be **active** first | **Wave 3B** |
| REL-0027..0030 BELONGS_TO | Website endpoints — Wave 4 coordination | **Wave 3B** (with Wave 4 policy) |
| PRJ-0006 → WEB-0006 BELONGS_TO | Not in dataset draft | **Wave 3B review** |
| PRJ-0001 EXECUTES edge | ORG-0002 vs ORG-0001 steward choice | **Wave 3B** |
| REL-0016 CLIENT_OF | Org↔org family | **Wave 6** |
| Person ↔ Project edges | Not in taxonomy baseline Wave 3 | **Future expansion** |

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-PROJECT-POPULATION-v1.md) | Per-project analysis and exclusions |
| [ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md) | Attestation gates and verdict |
| [ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md) | Organization endpoints |
| [ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md](ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md) | Person endpoints |
