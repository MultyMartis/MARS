# ATLAS Wave 4 Website Register v1

**Status:** **documented** — canonical Website roster after Wave 4 population (pending steward attestation act).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE4-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md)  
**Is not:** relationship registry, Domain registry, runtime export, database table, attested canonical export until attestation act completes.

---

## 1. Purpose

Канонический **реестр Website population** Wave 4. Одна строка — одна approved Website record для attestation.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **4** |
| Target **active** | **4** (WEB-0006..0009) |
| Target **deprecated** | **0** |
| Deferred operator sites | **5** (WEB-0001..0005) |
| Attestation readiness **ready** | **4** |

---

## 2. Population roster — full table

| website_id | canonical_name | website_kind | url | primary_org_candidate | primary_project_candidate | secondary_project_candidate | evidence_tier | lifecycle_state | attestation_readiness | notes |
|------------|----------------|--------------|-----|----------------------|---------------------------|----------------------------|---------------|-----------------|----------------------|-------|
| WEB-0006 | gktriumph.ru | corporate | `https://gktriumph.ru` | ORG-0004 Триумф | PRJ-0004 Редизайн gktriumph.ru | PRJ-0006 SEO gktriumph.ru | E1 | **active** | **ready** | Main site; PRJ-0004 deprecated |
| WEB-0007 | blog.gktriumph.ru | blog | `https://blog.gktriumph.ru` | ORG-0004 Триумф | PRJ-0007 Блог gktriumph.ru | — | E1 | **active** | **ready** | WordPress subsite |
| WEB-0008 | gruzotaxi-triumph.ru | landing | `https://gruzotaxi-triumph.ru` | ORG-0004 Триумф | PRJ-0005 Грузотакси | — | E1 | **active** | **ready** | Yandex Direct landing |
| WEB-0009 | manipulator-triumph.ru | landing | `https://manipulator-triumph.ru` | ORG-0004 Триумф | PRJ-0008 Манипулятор | — | E1 | **active** | **ready** | Website Factory / ORCA case |

---

## 3. Population roster — by website_kind

### 3.1 Corporate (1)

| website_id | canonical_name | lifecycle_state | evidence_tier | attestation_readiness |
|------------|----------------|-----------------|---------------|----------------------|
| WEB-0006 | gktriumph.ru | **active** | E1 | **ready** |

### 3.2 Blog (1)

| website_id | canonical_name | lifecycle_state | evidence_tier | attestation_readiness |
|------------|----------------|-----------------|---------------|----------------------|
| WEB-0007 | blog.gktriumph.ru | **active** | E1 | **ready** |

### 3.3 Landing (2)

| website_id | canonical_name | lifecycle_state | evidence_tier | attestation_readiness |
|------------|----------------|-----------------|---------------|----------------------|
| WEB-0008 | gruzotaxi-triumph.ru | **active** | E1 | **ready** |
| WEB-0009 | manipulator-triumph.ru | **active** | E1 | **ready** |

---

## 4. Aliases index (informational — not Wave 4 edges)

| website_id | aliases | alias_type |
|------------|---------|------------|
| WEB-0006 | Основной сайт Триумфа; Сайт Триумфа | display / brand |
| WEB-0007 | Блог gktriumph.ru; Блог основного сайта | display |
| WEB-0008 | Лендинг Грузотакси; Gruzotaxi Triumph landing | display |
| WEB-0009 | Лендинг Манипулятор; Manipulator Triumph landing | display |

Hostname strings (`gktriumph.ru`, etc.) attach to **Domain** entities in Wave 5 — not substitutes for Website aliases ([ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.4).

---

## 5. Platform metadata (consumer context — non-lifecycle)

| website_id | platform (dataset) | consumer_program_refs |
|------------|-------------------|----------------------|
| WEB-0006 | WP + The7 + WPBakery + Custom | WPilot context |
| WEB-0007 | WordPress | WPilot context |
| WEB-0008 | WP + The7 + WPBakery + Custom | MIG pilot on PRJ-0005 |
| WEB-0009 | Website Factory / static or custom | ORCA, Website Factory |

Platform metadata does **not** substitute for lifecycle attestation.

---

## 6. Excluded register (not in population set)

| Item | Reason | Belongs to |
|------|--------|------------|
| WEB-0001..0005 | Operator org sites — not in approved Wave 4 roster | Future Wave 4 tranche |
| DOM-* for Triumph hostnames | Domain entity class | **Wave 5** |
| REL-0027..0030 BELONGS_TO | Relationship family | **Wave 4B** |
| OWNS / OPERATES org↔website | Relationship family | **Wave 4B** |
| PRIMARY_DOMAIN edges | Domain ↔ Website | **Wave 5 / 6C** |
| REL-0016 CLIENT_OF | Org ↔ Org | **Wave 6** |
| MARS workspace deploy paths | Deploy artifact | MARS `workspaces/` |

---

## 7. Evidence index (population references)

| Ref | Artifact | Websites supported |
|-----|----------|-------------------|
| Dataset Websites sheet | [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | WEB-0006..0009 |
| Live URL probe | `https://gktriumph.ru` | WEB-0006 |
| Live URL probe | `https://blog.gktriumph.ru` | WEB-0007 |
| Live URL probe | `https://gruzotaxi-triumph.ru` | WEB-0008 |
| Live URL probe | `https://manipulator-triumph.ru` | WEB-0009 |
| EV-0005 | `triumph/…2024.xlsx` | Triumph org + site context |
| EV-0001, EV-0002 | Yandex Maps / Avito — ORG-0004 | Org anchor for properties |
| Wave 3B REL-0017..0025 | COMMISSIONED_BY edges | Project commissioning context |
| MIG pilot prep | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` | WEB-0008 (support only) |
| MARS delivery pack | `projects/triumph-manipulator-landing/` | WEB-0009 (support only) |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 8. Deferred register (Wave 4B+)

| Item | Reason | Target wave |
|------|--------|-------------|
| REL-0027 WEB-0006 → PRJ-0004 BELONGS_TO | Website endpoints pending attestation act | **Wave 4B** |
| REL-0028 WEB-0007 → PRJ-0007 BELONGS_TO | Website endpoints pending attestation act | **Wave 4B** |
| REL-0029 WEB-0008 → PRJ-0005 BELONGS_TO | Website endpoints pending attestation act | **Wave 4B** |
| REL-0030 WEB-0009 → PRJ-0008 BELONGS_TO | Website endpoints pending attestation act | **Wave 4B** |
| WEB-0006 → PRJ-0006 SEO BELONGS_TO | Not in dataset draft | **Wave 4B review** |
| ORG-0004 OWNS WEB-0006..0009 | Org ↔ Website family | **Wave 4B** |
| ORG-0001 OPERATES WEB-0006..0009 | Execution operator context | **Wave 4B** (steward choice) |
| DOM-* + PRIMARY_DOMAIN | Hostname identity | **Wave 5 / 6C** |
| WEB-0001..0005 operator sites | Out of approved roster | **Future tranche** |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-WEBSITE-POPULATION-v1.md) | Per-website analysis and exclusions |
| [ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md) | Attestation gates and verdict |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Project ↔ Org attested edges |
