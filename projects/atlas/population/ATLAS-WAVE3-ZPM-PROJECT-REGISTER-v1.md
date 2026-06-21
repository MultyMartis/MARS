# ATLAS Wave 3 ZPM Project Register v1

**Status:** **documented** — canonical Project roster for Wave 3 ZPM tranche (**active** / **deprecated**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07 · **sync:** 2026-06-07 (ZPM documentation sync)  
**Organization anchor:** ORG-0005 **ЗПМ** · LE-0004  
**Parent:** [ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md) · [ATLAS-ZPM-PROJECT-INTAKE-REGISTER-v1.md](ATLAS-ZPM-PROJECT-INTAKE-REGISTER-v1.md)  
**Is not:** relationship registry, runtime export, database table, attested canonical export until attestation act completes.

---

## 1. Purpose

Канонический **реестр Project population** Wave 3 tranche **ZPM** (ORG-0005). Одна строка — одна approved Project record для attestation.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **2** |
| Lifecycle **active** | **1** (PRJ-0009) |
| Lifecycle **deprecated** | **1** (PRJ-0010) |
| Population slice **client_delivery** | **2** |
| Evidence **E0** | **2** |
| Future candidates held | **4** |
| Attestation | **Complete** — AT-W3-ZPM-01, AT-W3-ZPM-02 |

---

## 2. Population roster — full table

| project_id | intake_label | canonical_name | population_slice | roster_priority | commissioning_org | execution_org | related_property | evidence_tier | evidence_ref | lifecycle_state | attestation | notes |
|------------|--------------|----------------|------------------|-----------------|-------------------|---------------|------------------|---------------|--------------|-----------------|-------------|-------|
| PRJ-0009 | ZPM-INTAKE-CAND-A01 | Каталог-платформа bzpm.ru | **client_delivery** | **P0** | ORG-0005 ЗПМ | ORG-0001 Полигон | `bzpm.ru` *(WEB-ZPM-01)* | **E0** | EV-ZPM-OP-ACT-01 | **active** | AT-W3-ZPM-01 | Catalog platform; almost complete; Polygon WIP |
| PRJ-0010 | ZPM-INTAKE-CAND-H01 | Сайт bzpm.ru (исходная версия) | **client_delivery** | **P1** | ORG-0005 ЗПМ | ORG-0001 Полигон | `bzpm.ru` *(historical)* | **E0** | EV-ZPM-OP-HIST-01 | **deprecated** | AT-W3-ZPM-02 | ~5y ago; WP + The7 + Custom; completed |

---

## 3. Population roster — by lifecycle target

### 3.1 Active (1)

| project_id | canonical_name | evidence_tier | evidence_ref | attestation |
|------------|----------------|---------------|--------------|-------------|
| PRJ-0009 | Каталог-платформа bzpm.ru | **E0** | EV-ZPM-OP-ACT-01 | AT-W3-ZPM-01 |

### 3.2 Deprecated (1)

| project_id | canonical_name | evidence_tier | evidence_ref | attestation |
|------------|----------------|---------------|--------------|-------------|
| PRJ-0010 | Сайт bzpm.ru (исходная версия) | **E0** | EV-ZPM-OP-HIST-01 | AT-W3-ZPM-02 |

---

## 4. Related people index (informational — not Wave 3 edges)

| project_id | related_people | role context |
|------------|----------------|--------------|
| PRJ-0009 | PER-0014, PER-0015 | Client operational contacts for Polygon vendor work on ЗПМ account |
| PRJ-0010 | PER-0014, PER-0015 | Same org context — historical delivery |

Person ↔ Project relationships — **not in Wave 3 ZPM scope**; future expansion review only.

---

## 5. Excluded register (not in population set)

| Item | Reason | Belongs to |
|------|--------|------------|
| ZPM-INTAKE-FUT-01 SEO | No start evidence | Future intake |
| ZPM-INTAKE-FUT-02 Контекстная реклама | No start evidence | Future intake |
| ZPM-INTAKE-FUT-03 AI automation | No start evidence | Future intake |
| ZPM-INTAKE-FUT-04 OpenCartPilot maintenance | No start evidence | Future intake |
| BZPM / SITE-001 OpenCart | Identity pollution COR-W1B-03 | **Rejected** |
| OCPilot read-only audit | MARS program context | **Rejected** |
| MARS `ocpilot`, `ear-runtime`, … | E-17 excluded | `registry/project-registry.md` |
| Single merged bzpm.ru Project | EFV-03 inference | **Rejected** |
| `bzpm.ru` hostname alone | Website class | Wave 4 |
| ORG-0005 ЗПМ | Organization entity | Wave 1B |
| WEB-* / DOM-* for bzpm.ru | Out of operator scope | Waves 4–5 |

---

## 6. Evidence index

| Ref | Artifact | Projects supported |
|-----|----------|-------------------|
| EV-ZPM-OP-ACT-01 | Operator statement — current catalog rebuild | PRJ-0009 |
| EV-ZPM-OP-HIST-01 | Operator statement — historical `bzpm.ru` delivery | PRJ-0010 |
| EV-ZPM-OP-FUT-01 | Operator statement — future possibilities | Exclusion basis FUT-01..04 |
| EV-W1B-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx` | Org anchor; §17 indirect hostname corroboration |
| AT-W1B-01 | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | ORG-0005 **active** prerequisite |
| AT-W2B-ZPM-01 | [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) | Person + vendor context prerequisite |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 7. Duplicate review register

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| ZPM-PRJ-D-01 | PRJ-0009 vs PRJ-0010 same hostname | **Not duplicate** — sequential deliveries | No |
| ZPM-PRJ-D-02 | PRJ-0009 vs FUT-01 SEO | **Distinct** — future held | No |
| ZPM-PRJ-D-03 | vs PRJ-0004..0008 Triumph | **Distinct org** | No |
| ZPM-PRJ-D-04 | vs future WEB-* | **Class boundary** | No |
| ZPM-PRJ-D-05 | vs SITE-001 | **Reject SITE-001** | No |
| ZPM-PRJ-D-06 | Name disambiguation | **Resolved** — version suffix | No |
| ZPM-PRJ-D-07 | Catalog vs site stem | **Pass** | No |

**Duplicate review summary:** **Pass**

---

## 8. SAFE UNKNOWN index

| id | topic | blocks_attestation |
|----|-------|------------------|
| SU-ZPM-PRJ-01 | Historical contract dates | **No** |
| SU-ZPM-PRJ-02 | Formal acceptance docs (E1 path) | **No** |
| SU-ZPM-PRJ-03 | Deployment replace vs coexistence | **Resolved** — single Website model (WEB-ZPM-01) |
| SU-ZPM-PRJ-04 | Final canonical name strings | **No** |
| SU-ZPM-PRJ-05 | OCPilot scope if FUT-04 approved | **No** |
| SU-ZPM-PRJ-06 | Person ↔ Project edges | **No** — out of scope |
| SU-ZPM-PRJ-07 | CLIENT_OF commercial edge | **No** — Wave 6 |
| SU-ZPM-PRJ-08 | Domain registrant | **No** — Wave 5 |

---

## 9. Deferred register (Wave 6+ and future intake)

| Item | Reason | Target wave |
|------|--------|-------------|
| REL-0016 CLIENT_OF ORG-0005 → ORG-0001 | Org↔org family | **Wave 6** |
| ZPM-INTAKE-FUT-01..04 | No start evidence | **Hold** |

**Completed (attested — see relationship registers):**

| Item | Attestation | Register |
|------|-------------|----------|
| REL-ZPM-PJ-01..04 | Wave 3B ZPM | [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) |
| WEB-ZPM-01 | AT-W4-ZPM-01 | [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) |
| DOM-ZPM-01 | AT-W5-ZPM-01 | [ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md) |
| REL-ZPM-WB-01, 03, 04 | Wave 4B ZPM | [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md) |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md) | Per-project analysis and exclusions |
| [ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md) | Attestation gates and verdict |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Core Wave 3 roster PRJ-0001..0008 |
| [ATLAS-ZPM-PROJECT-INTAKE-SUMMARY-v1.md](ATLAS-ZPM-PROJECT-INTAKE-SUMMARY-v1.md) | Intake executive summary |

---

*ATLAS Wave 3 ZPM Project Register v1 — PRJ-0009 **active**, PRJ-0010 **deprecated**; synced 2026-06-07 per attestation acts AT-W3-ZPM-01..02.*
