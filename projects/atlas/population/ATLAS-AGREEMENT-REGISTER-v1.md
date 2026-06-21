# ATLAS Agreement Register v1

**Status:** **attested** — canonical Agreement roster after Wave AGL-01 attestation act.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Wave:** AGL-01 — Agreement Layer Foundation  
**Parent:** [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) · [ATLAS-AGREEMENT-POPULATION-PLAN-v1.md](ATLAS-AGREEMENT-POPULATION-PLAN-v1.md) · [ATLAS-AGREEMENT-REALITY-MODEL-v1.md](../foundation/ATLAS-AGREEMENT-REALITY-MODEL-v1.md)  
**Is not:** runtime export, database table, contract archive, legal repository.

---

## 1. Purpose

Канонический **реестр аттестированных Agreement records** после Wave AGL-01. Одна строка — одна attested business-reality anchor. **No contract text stored.**

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested agreements | **8** |
| Status **ACTIVE** | **6** |
| Status **EXPIRED** | **2** |
| Status PLANNED | **0** |
| Client orgs covered | **3** (ORG-0004, ORG-0005, ORG-0006) |
| Vendor org (all rows) | ORG-0001 Полигон |
| Projects with agreement binding | **8** (PRJ-0004..0011 subset) |
| ORG-0007 Makita | **0** rows — SAFE UNKNOWN |

---

## 2. Attested roster — full table

| agreement_id | status | client_org | vendor_org | agreement_type | start_date | end_date | scope_summary | related_projects | evidence_level | attestation_ref | notes |
|--------------|--------|------------|------------|----------------|------------|----------|---------------|------------------|----------------|-----------------|-------|
| AGR-0001 | **EXPIRED** | ORG-0004 Триумф | ORG-0001 Полигон | DEVELOPMENT | **SAFE UNKNOWN** | **SAFE UNKNOWN** | Редизайн основного сайта gktriumph.ru — завершённая delivery phase | PRJ-0004 | E1 | AT-AGL-01 | Historical; PRJ-0004 deprecated |
| AGR-0002 | **ACTIVE** | ORG-0004 Триумф | ORG-0001 Полигон | DEVELOPMENT | **SAFE UNKNOWN** | **SAFE UNKNOWN** | Разработка и сопровождение сайта грузотакси (gruzotaxi-triumph.ru) | PRJ-0005 | E1 | AT-AGL-02 | Ongoing delivery |
| AGR-0003 | **ACTIVE** | ORG-0004 Триумф | ORG-0001 Полигон | SEO_RETAINER | **SAFE UNKNOWN** | **SAFE UNKNOWN** | SEO-продвижение основного сайта gktriumph.ru | PRJ-0006 | E1 | AT-AGL-03 | Scope from attested project identity |
| AGR-0004 | **ACTIVE** | ORG-0004 Триумф | ORG-0001 Полигон | DEVELOPMENT | **SAFE UNKNOWN** | **SAFE UNKNOWN** | Разработка блога blog.gktriumph.ru | PRJ-0007 | E1 | AT-AGL-04 | Ongoing delivery |
| AGR-0005 | **ACTIVE** | ORG-0004 Триумф | ORG-0001 Полигон | DEVELOPMENT | **SAFE UNKNOWN** | **SAFE UNKNOWN** | Landing / сайт manipulator-triumph.ru (Website Factory case) | PRJ-0008 | E1 | AT-AGL-05 | WF-01 live binding contour |
| AGR-0006 | **ACTIVE** | ORG-0005 ЗПМ | ORG-0001 Полигон | DEVELOPMENT | **SAFE UNKNOWN** | **SAFE UNKNOWN** | Каталог-платформа bzpm.ru — активная rebuild / WIP delivery | PRJ-0009 | E0 | AT-AGL-06 | Operator + project graph |
| AGR-0007 | **EXPIRED** | ORG-0005 ЗПМ | ORG-0001 Полигон | DEVELOPMENT | **SAFE UNKNOWN** | **SAFE UNKNOWN** | Исходная версия сайта bzpm.ru (WP + The7 + Custom) — завершена ~5 лет назад | PRJ-0010 | E0 | AT-AGL-07 | Historical; PRJ-0010 deprecated |
| AGR-0008 | **ACTIVE** | ORG-0006 SIBCAR | ORG-0001 Полигон | DEVELOPMENT | **SAFE UNKNOWN** | **SAFE UNKNOWN** | OpenCart dealership — автосалон WIP (TEST env; OCPilot SITE-001 context) | PRJ-0011 | E0 | AT-AGL-08 | Operator + OCPilot corroboration |

---

## 3. Attested roster — by client organization

### 3.1 ORG-0004 Триумф

| agreement_id | status | agreement_type | related_projects | evidence_level |
|--------------|--------|----------------|------------------|----------------|
| AGR-0001 | **EXPIRED** | DEVELOPMENT | PRJ-0004 | E1 |
| AGR-0002 | **ACTIVE** | DEVELOPMENT | PRJ-0005 | E1 |
| AGR-0003 | **ACTIVE** | SEO_RETAINER | PRJ-0006 | E1 |
| AGR-0004 | **ACTIVE** | DEVELOPMENT | PRJ-0007 | E1 |
| AGR-0005 | **ACTIVE** | DEVELOPMENT | PRJ-0008 | E1 |

### 3.2 ORG-0005 ЗПМ

| agreement_id | status | agreement_type | related_projects | evidence_level |
|--------------|--------|----------------|------------------|----------------|
| AGR-0006 | **ACTIVE** | DEVELOPMENT | PRJ-0009 | E0 |
| AGR-0007 | **EXPIRED** | DEVELOPMENT | PRJ-0010 | E0 |

### 3.3 ORG-0006 SIBCAR

| agreement_id | status | agreement_type | related_projects | evidence_level |
|--------------|--------|----------------|------------------|----------------|
| AGR-0008 | **ACTIVE** | DEVELOPMENT | PRJ-0011 | E0 |

### 3.4 ORG-0007 Макита — not in register

| Posture | Reason |
|---------|--------|
| **SAFE UNKNOWN** | No attested Project; no CLIENT_OF edge; CC absent; steward excludes contract scope |

---

## 4. Attested roster — by status

| status | Count | agreement_ids |
|--------|-------|---------------|
| **ACTIVE** | 6 | AGR-0002, AGR-0003, AGR-0004, AGR-0005, AGR-0006, AGR-0008 |
| **EXPIRED** | 2 | AGR-0001, AGR-0007 |

---

## 5. Attested roster — by agreement type

| agreement_type | Count | agreement_ids |
|----------------|-------|---------------|
| DEVELOPMENT | 7 | AGR-0001, 0002, 0004, 0005, 0006, 0007, 0008 |
| SEO_RETAINER | 1 | AGR-0003 |
| PPC_RETAINER | 0 | — |
| SUPPORT | 0 | — |
| MIXED | 0 | — |
| OTHER | 0 | — |

---

## 6. Project coverage matrix

| project_id | agreement_id | status | client_org | vendor_org | coverage |
|------------|--------------|--------|------------|------------|----------|
| PRJ-0004 | AGR-0001 | EXPIRED | ORG-0004 | ORG-0001 | **Bound** |
| PRJ-0005 | AGR-0002 | ACTIVE | ORG-0004 | ORG-0001 | **Bound** |
| PRJ-0006 | AGR-0003 | ACTIVE | ORG-0004 | ORG-0001 | **Bound** |
| PRJ-0007 | AGR-0004 | ACTIVE | ORG-0004 | ORG-0001 | **Bound** |
| PRJ-0008 | AGR-0005 | ACTIVE | ORG-0004 | ORG-0001 | **Bound** |
| PRJ-0009 | AGR-0006 | ACTIVE | ORG-0005 | ORG-0001 | **Bound** |
| PRJ-0010 | AGR-0007 | EXPIRED | ORG-0005 | ORG-0001 | **Bound** |
| PRJ-0011 | AGR-0008 | ACTIVE | ORG-0006 | ORG-0001 | **Bound** |
| PRJ-0001 MARS | — | — | — | — | **N/A** — internal |
| *(Makita future)* | — | — | ORG-0007 | — | **SAFE UNKNOWN** |

---

## 7. Structural corroboration index

| agreement_id | CLIENT_OF | COMMISSIONED_BY | EXECUTES |
|--------------|-----------|-----------------|----------|
| AGR-0001..0005 | REL-0016 | REL-0017, 0019, 0021, 0023, 0025 | REL-0018, 0020, 0022, 0024, 0026 |
| AGR-0006, AGR-0007 | REL-0040 | REL-ZPM-PJ-01, REL-ZPM-PJ-03 | REL-ZPM-PJ-02, REL-ZPM-PJ-04 |
| AGR-0008 | REL-0041 | REL-SIBCAR-PJ-01 | REL-SIBCAR-PJ-02 |

---

## 8. Deferred register (not in attested set)

| Item | Reason |
|------|--------|
| ORG-0007 Makita agreements | Evidence insufficient — see Population Plan §7 |
| ZPM FUT-01..04 service agreements | No Project entity |
| SIBCAR FUT-01..03 | No Project entity |
| Triumph umbrella master agreement | Legal boundary unknown — per-project anchors used |
| Agreement date fields (all rows) | No E2 date extract attested |
| PPC_RETAINER (Makita Yandex Direct) | Steward scope — not agreement anchor |
| ORG-0007 → ORG-0003 SEO agreement | Commercial edge not attested |

---

## 9. Evidence index

| Ref | Artifact | Agreements supported |
|-----|----------|---------------------|
| AT-AGL-01..08 | [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) | All register rows |
| REL-0016 | Wave 6A commercial register | AGR-0001..0005 client-vendor context |
| REL-0040 | Wave 6B | AGR-0006, AGR-0007 |
| REL-0041 | Wave 6B | AGR-0008 |
| Wave 3B register | REL-0017..0026 | AGR-0001..0005 |
| Wave 3B-ZPM | REL-ZPM-PJ-01..04 | AGR-0006, AGR-0007 |
| Wave 3B-SIBCAR | REL-SIBCAR-PJ-01..02 | AGR-0008 |
| EV-0005 | Triumph commercial spreadsheet | AGR-0001..0005 E1 overlay |
| EV-W1B-CC-01 | ZPM CC | AGR-0006, AGR-0007 vendor/client context |
| EV-W1C-CC-01 | SIBCAR CC | AGR-0008 |
| EV-ZPM-OP-ACT-01 / HIST-01 | Operator statements | AGR-0006, AGR-0007 |
| EV-OCP-01..04 | OCPilot SITE-001 | AGR-0008 corroboration |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) | Formal attestation methodology and act |
| [ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md](ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md) | ACTIVE subset verification |
| [ATLAS-AGREEMENT-POPULATION-PLAN-v1.md](ATLAS-AGREEMENT-POPULATION-PLAN-v1.md) | Readiness evaluation |
| [REPORT-atlas-agreement-layer-foundation-v1.md](../reports/REPORT-atlas-agreement-layer-foundation-v1.md) | Wave pass record |

---

*ATLAS Agreement Register v1 — Wave AGL-01. Attested business reality anchors only.*
