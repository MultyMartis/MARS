# ATLAS Wave 4 Website Population v1

**Status:** **documented** — Wave 4 canonical Website population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) · [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) · [ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md) · [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md)  
**Is not:** runtime, API, automation, database schema, relationship attestation, Domain population, Wave 4B execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization relationships: **COMPLETE**
- Wave 3 Projects: **COMPLETE**
- Wave 3B Project → Organization relationships: **COMPLETE**
- Population verdict: **READY FOR WAVE 4 WEBSITE POPULATION**

**Binding operator correction (Wave 4):**

- **Approved roster only:** WEB-0006..0009 (Triumph client properties).
- **Operator org websites** (WEB-0001..0005) — **out of scope** this pass; separate steward tranche when prioritized.
- **Website population now. Website relationships later** (Wave 4B).
- **Domain entities** (`DOM-*`) — Wave 5; no PRIMARY_DOMAIN / SECONDARY_DOMAIN in Wave 4.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Website** для Wave 4: состав, lifecycle, evidence, org/project context (display candidates only), aliases, candidate relationships для Wave 4B, границы foundation.

**Normative scope Wave 4:**

```text
Website entity intake + attestation plan
Wave 4B (отдельный пакет): Website ↔ Project BELONGS_TO, Organization ↔ Website OWNS/OPERATES — только после active Website endpoints
Wave 5: Domain entities + PRIMARY_DOMAIN family
Wave 6: remaining org↔org (REL-0016 CLIENT_OF) and cross-links
```

---

## 2. Population roster (canonical)

Источник: [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) (лист `Websites`, `Relationships`).  
Draft lifecycle в dataset — **не** canonical registry state до attestation.

### 2.1 Summary table

| website_id | canonical_name | website_kind | lifecycle_state | primary_org_candidate | primary_project_candidate | secondary_project_candidate | attestation readiness |
|------------|----------------|--------------|-----------------|----------------------|---------------------------|----------------------------|----------------------|
| WEB-0006 | gktriumph.ru | **corporate** | **active** | ORG-0004 Триумф | PRJ-0004 Редизайн gktriumph.ru | PRJ-0006 SEO gktriumph.ru | **ready** |
| WEB-0007 | blog.gktriumph.ru | **blog** | **active** | ORG-0004 Триумф | PRJ-0007 Блог gktriumph.ru | — | **ready** |
| WEB-0008 | gruzotaxi-triumph.ru | **landing** | **active** | ORG-0004 Триумф | PRJ-0005 Грузотакси | — | **ready** |
| WEB-0009 | manipulator-triumph.ru | **landing** | **active** | ORG-0004 Триумф | PRJ-0008 Манипулятор | — | **ready** |

**website_kind** — intake classification (не новый тип entity; metadata facet per [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4).  
**primary_org / primary_project** — display context from operator-approved knowledge; structural edges **deferred** to Wave 4B.

---

## 3. Per-website analysis

### 3.1 WEB-0006 — gktriumph.ru (main corporate site)

| Field | Value |
|-------|-------|
| **website_id** | WEB-0006 |
| **canonical_name** | gktriumph.ru |
| **lifecycle_state** | **active** — primary brand web property ORG-0004 |
| **primary_org_candidate** | ORG-0004 ООО «Триумф» |
| **primary_project_candidate** | PRJ-0004 Редизайн gktriumph.ru *(dataset deliverable link; project **deprecated**, site **active** — valid W3-LC-05 pattern)* |
| **secondary_project_candidate** | PRJ-0006 SEO gktriumph.ru *(ongoing SEO on same property — no separate Website entity)* |
| **aliases** | «Основной сайт Триумфа»; «Сайт Триумфа» |
| **evidence_tier** | **E1** |
| **evidence_sources** | Dataset Websites sheet; live `https://gktriumph.ru`; platform WP + The7 + WPBakery + Custom; EV-0005 Triumph CC; REL-0017/0021 commissioning context (Wave 3B) |
| **open questions** | Dual BELONGS_TO (PRJ-0004 vs PRJ-0006) at Wave 4B — dataset links PRJ-0004 only; PRJ-0006 SEO edge not in dataset draft |
| **readiness assessment** | **Ready** — org and project endpoints attested; E1 client property |

### 3.2 WEB-0007 — blog.gktriumph.ru

| Field | Value |
|-------|-------|
| **website_id** | WEB-0007 |
| **canonical_name** | blog.gktriumph.ru |
| **lifecycle_state** | **active** — live blog subsite under Triumph brand |
| **primary_org_candidate** | ORG-0004 Триумф |
| **primary_project_candidate** | PRJ-0007 Блог gktriumph.ru |
| **secondary_project_candidate** | — |
| **aliases** | «Блог gktriumph.ru»; «Блог основного сайта» |
| **evidence_tier** | **E1** |
| **evidence_sources** | Dataset Websites sheet; live `https://blog.gktriumph.ru`; platform WordPress; operator note: assembled by PER-0008 on WP; REL-0023 commissioning (Wave 3B) |
| **open questions** | Subsite vs separate property — attested as **separate Website** (distinct hostname identity per EIR-W01) |
| **readiness assessment** | **Ready** |

### 3.3 WEB-0008 — gruzotaxi-triumph.ru

| Field | Value |
|-------|-------|
| **website_id** | WEB-0008 |
| **canonical_name** | gruzotaxi-triumph.ru |
| **lifecycle_state** | **active** — landing + Yandex Direct advertising |
| **primary_org_candidate** | ORG-0004 Триумф |
| **primary_project_candidate** | PRJ-0005 Грузотакси |
| **secondary_project_candidate** | — |
| **aliases** | «Лендинг Грузотакси»; «Gruzotaxi Triumph landing» |
| **evidence_tier** | **E1** |
| **evidence_sources** | Dataset Websites sheet; live `https://gruzotaxi-triumph.ru`; platform WP + The7 + WPBakery + Custom; EV-0005 Triumph CC; REL-0019 commissioning; MIG pilot prep `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` (proposal support only — AT-E-03) |
| **open questions** | MIG pilot sessions reference PRJ-0005 — not a second Website |
| **readiness assessment** | **Ready** |

### 3.4 WEB-0009 — manipulator-triumph.ru

| Field | Value |
|-------|-------|
| **website_id** | WEB-0009 |
| **canonical_name** | manipulator-triumph.ru |
| **lifecycle_state** | **active** — landing + advertising; Website Factory / ORCA operational case |
| **primary_org_candidate** | ORG-0004 Триумф |
| **primary_project_candidate** | PRJ-0008 Манипулятор |
| **secondary_project_candidate** | — |
| **aliases** | «Лендинг Манипулятор»; «Manipulator Triumph landing» |
| **evidence_tier** | **E1** |
| **evidence_sources** | Dataset Websites sheet; live `https://manipulator-triumph.ru`; platform Website Factory / static or custom; EV-0005 Triumph CC; REL-0025 commissioning; `projects/triumph-manipulator-landing/` (MARS program pack — **not** duplicate ATLAS Website) |
| **open questions** | Route-level URLs (`*.html` paths) — page-level; out of ATLAS Website scope |
| **readiness assessment** | **Ready** |

---

## 4. Lifecycle decisions

| Rule | Application in Wave 4 |
|------|------------------------|
| Live client property in production → **active** | **WEB-0006..0009** — operator-approved |
| Staging URL ≠ production Website | No staging entities in roster |
| Deprecated project + active website | **PRJ-0004** deprecated; **WEB-0006** **active** — W3-LC-05 / W4-LC-01 |
| No operational deploy flags (CMS version, PageSpeed) | Structural lifecycle only ([ATLAS-LIFECYCLE-MODEL-v1.md](../foundation/ATLAS-LIFECYCLE-MODEL-v1.md) LC-BAN-01) |
| Website without attested org at **active** | **Not applicable** — ORG-0004 **active** (Wave 1); org link deferred as **edge**, not UNKNOWN slot |

---

## 5. Explicit exclusions

### 5.1 Out of approved Wave 4 roster

| website_id | Treatment | Reason |
|------------|-----------|--------|
| WEB-0001 polygon-ws.ru | **Deferred** | Operator org site — not in approved Triumph roster |
| WEB-0002 polygon-ws.com | **Deferred** | Operator org site |
| WEB-0003 metacode-agency.com | **Deferred** | Operator org site |
| WEB-0004 metacode-agency.ru | **Deferred** | Operator org site |
| WEB-0005 i-seo.su | **Deferred** | Operator org site |
| DOM-* hostnames | **Wave 5** | Domain ≠ Website |
| MARS workspace paths | **Excluded** | Deploy artifact — not ATLAS Website entity |

### 5.2 Relationship and edge exclusions (Wave 4B+)

| Item | Treatment | Target wave |
|------|-----------|-------------|
| BELONGS_TO Website → Project | **Deferred** | **Wave 4B** |
| OWNS / OPERATES Organization → Website | **Deferred** | **Wave 4B** |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN Domain → Website | **Deferred** | **Wave 5 / 6C** |
| REL-0016 CLIENT_OF ORG-0004 → ORG-0001 | **Deferred** | **Wave 6** |
| Person ↔ Website edges | **Deferred** | Future expansion |

### 5.3 Other rejected candidates

| Candidate | Treatment | Reason |
|-----------|-----------|--------|
| PRJ-0006 as separate Website | **Rejected** | SEO scope on WEB-0006 — Wave 3 §3.4 |
| MIG SERP-only URL without live property | **Rejected** | Insufficient for active ([ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.4) |
| `www.gktriumph.ru` as separate Website | **Rejected** | Hostname policy → Wave 5 Domain + PRIMARY_DOMAIN |
| MARS `triumph-manipulator-landing` program id | **Excluded** | Program pack ≠ WEB-0009 |

---

## 6. Candidate relationships for Wave 4B

**Not attested in Wave 4.** Prepared for separate Wave 4B population pass.

### 6.1 Website → Project BELONGS_TO

| Draft rel_id | source_website | target_project | Notes |
|--------------|----------------|----------------|-------|
| REL-0027 | WEB-0006 gktriumph.ru | PRJ-0004 Редизайн | Dataset draft; deliverable grouping |
| REL-0028 | WEB-0007 blog.gktriumph.ru | PRJ-0007 Блог | Dataset draft |
| REL-0029 | WEB-0008 gruzotaxi-triumph.ru | PRJ-0005 Грузотакси | Dataset draft |
| REL-0030 | WEB-0009 manipulator-triumph.ru | PRJ-0008 Манипулятор | Dataset draft |
| *(TBD)* | WEB-0006 gktriumph.ru | PRJ-0006 SEO | **Not in dataset draft** — steward review (SU-W3B-04) |

**Cardinality note:** One website may BELONGS_TO multiple projects if attested (SEO + redesign on same property).

### 6.2 Organization → Website OWNS / OPERATES

| Draft rel_id | source_organization | target_website | Type | Notes |
|--------------|---------------------|----------------|------|-------|
| *(TBD)* | ORG-0004 Триумф | WEB-0006 | **OWNS** | Client org owns corporate property |
| *(TBD)* | ORG-0004 Триумф | WEB-0007 | **OWNS** | Blog subsite |
| *(TBD)* | ORG-0004 Триумф | WEB-0008 | **OWNS** | Landing property |
| *(TBD)* | ORG-0004 Триумф | WEB-0009 | **OWNS** | Landing property |
| *(TBD)* | ORG-0001 Полигон | WEB-0006..0009 | **OPERATES** | Execution context — steward choice vs OWNS-only model |

**Wave 4B ordering note:** BELONGS_TO may proceed after Website attestation; OWNS requires ORG-0004 **active** (met) + Website **active** endpoints.

### 6.3 Domain → Website (Wave 5 prerequisite)

| Hostname | target_website | Type | Wave |
|----------|----------------|------|------|
| gktriumph.ru | WEB-0006 | PRIMARY_DOMAIN | **Wave 5 + 6C** |
| blog.gktriumph.ru | WEB-0007 | PRIMARY_DOMAIN | **Wave 5 + 6C** |
| gruzotaxi-triumph.ru | WEB-0008 | PRIMARY_DOMAIN | **Wave 5 + 6C** |
| manipulator-triumph.ru | WEB-0009 | PRIMARY_DOMAIN | **Wave 5 + 6C** |

---

## 7. Dataset reconciliation notes

| Item | Treatment in Wave 4 |
|------|---------------------|
| Dataset lifecycle on Websites sheet | **Draft only** — re-attest under Wave 4 governance |
| Dataset `project_id` on Websites sheet | Display context — BELONGS_TO attestation in Wave 4B |
| WEB-0006 linked only to PRJ-0004 in dataset | PRJ-0006 SEO edge — Wave 4B review |
| Platform strings (WP, Factory) | Consumer metadata — not lifecycle substitute |
| MIG session artifacts | Proposal support only — not Website mint evidence alone |

---

## 8. Foundation consistency

| Foundation doc | Wave 4 alignment |
|----------------|------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4 Website | Web property identity — not deploy/CMS — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-W01..W04 | One property per id; staging excluded — **yes** |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.4 | Brand titles as aliases; hostname on DOM — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | **active** for all four — **yes** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.4 | E1 client property — **yes** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) | Wave 4 after Project; org context available — **yes** |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | No edges without endpoints — **yes** (edges deferred) |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required — **yes** |

**No new entity types.** **No foundation modifications.**

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | Canonical website roster table |
| [ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md) | Attestation sequence and verdict |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | COMMISSIONED_BY context |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |
