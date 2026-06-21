# ATLAS Wave 3 Shpigovsky Project Register v1

**Status:** **documented** — canonical Project roster for Wave 3 Shpigovsky tranche (**active**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Organization anchor:** ORG-0008 **ООО «Сознание»**  
**Parent:** [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-POPULATION-v1.md) · [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ATTESTATION-v1.md) · [ATLAS-SHPIGOVSKY-INTAKE-REGISTER-v1.md](ATLAS-SHPIGOVSKY-INTAKE-REGISTER-v1.md)  
**Is not:** relationship registry, runtime export, database table, attested canonical export until attestation act completes.

---

## 1. Purpose

Канонический **реестр Project population** Wave 3 tranche **Shpigovsky** (ORG-0008). Одна строка — одна approved Project record для attestation.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Lifecycle **active** *(target)* | **1** (PRJ-0012) |
| Lifecycle **deprecated** | **0** |
| Population slice **client_delivery** | **1** |
| Evidence **E0/E1** | **1** |
| Future candidates held | **4+** |
| Attestation | **Complete** — AT-W3-SHPIG-01 |

---

## 2. Population roster — full table

| project_id | intake_label | canonical_name | population_slice | roster_priority | commissioning_org | execution_org | related_property | evidence_tier | evidence_ref | lifecycle_state *(target)* | attestation | notes |
|------------|--------------|----------------|------------------|-----------------|-------------------|---------------|------------------|---------------|--------------|------------------------------|-------------|-------|
| PRJ-0012 | SHPIGOVSKY-INTAKE-CAND-PRJ-A01 | Сайт shpigovsky.ru | **client_delivery** | **P0** | ORG-0008 ООО «Сознание» | ORG-0001 Полигон | `shpigovsky.ru` → WEB-SHPIG-01 | **E0/E1** | EV-SHPIG-OP-01; AT-W1D-SHPIG-01 | **active** | AT-W3-SHPIG-01 | Polygon delivery; Website Factory; WordPress; not i-SEO channel |

---

## 3. Population roster — by lifecycle target

### 3.1 Active (1)

| project_id | canonical_name | evidence_tier | evidence_ref | attestation |
|------------|----------------|---------------|--------------|-------------|
| PRJ-0012 | Сайт shpigovsky.ru | **E0/E1** | EV-SHPIG-OP-01; AT-W1D-SHPIG-01 | AT-W3-SHPIG-01 |

### 3.2 Deprecated (0)

*No historical delivery phase evidenced — single delivery initiative only.*

---

## 4. Related people index (informational — not Wave 3 edges)

| project_id | related_people | role context |
|------------|----------------|--------------|
| PRJ-0012 | PER-0010 | Acquisition; client comms; coordination; SEO supervision; primary acceptance |

Person ↔ Project relationships — **not in Wave 3 Shpigovsky scope**; future expansion review only.

---

## 5. Excluded register (not in population set)

| Item | Reason | Belongs to |
|------|--------|------------|
| SHPIGOVSKY-INTAKE-FUT-01 WP automation agents | No start evidence | Future intake |
| SHPIGOVSKY-INTAKE-FUT-02 Extended SEO program | No start evidence | Future intake |
| Future Direct contract | No start evidence | Future intake |
| Future AI automation work | No start evidence | Future intake |
| SEO supervision as separate Project | Supervision on delivery ≠ separate initiative | **Rejected** — REJ-SHPIG-PRJ-01 |
| Website Factory as separate Project | Workflow context | **Rejected** — REJ-SHPIG-PRJ-02 |
| WordPress / Frontend / ACF / Custom split | EFV-03 inference | **Rejected** — REJ-SHPIG-PRJ-03 |
| `shpigovsky.ru` hostname alone | Website class | Wave 4 |
| ORG-0008 ООО «Сознание» | Organization entity | Wave 1D |
| WEB-* / DOM-* for shpigovsky.ru | Out of operator scope | Waves 4–5 |
| PER-* Person rows | Out of operator scope | Wave 2 optional |
| LE-* Legal Entity | CC absent — deferred | Future CC wave |
| i-SEO project channel | Operator exclusion | **Rejected** — REJ-SHPIG-PRJ-06 |
| Historical site version twin | No second phase evidenced | **Rejected** — REJ-SHPIG-PRJ-07 |

---

## 6. Evidence index

| Ref | Artifact | Projects supported |
|-----|----------|-------------------|
| EV-SHPIG-OP-01 | Operator intake statements (2026-06-10) | PRJ-0012 — delivery channel, roles, stack, i-SEO exclusion |
| EV-SHPIG-WEB-01 | Live capture `https://shpigovsky.ru/` | Public property corroboration — Website class at Wave 4 |
| EV-SHPIG-WEB-02 | Live capture `https://shpigovsky.ru/policy` | Org corroboration — not project boundary proof |
| AT-W1D-SHPIG-01 | [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md) | ORG-0008 **active** prerequisite — E1 org anchor |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md). CC folder `shpigovsky\` — **absent** (expected for Category A operational-public path).

---

## 7. Duplicate review register

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| SHPIG-PRJ-D-01 | PRJ-0012 vs ORG-0008 | **Class boundary** | No |
| SHPIG-PRJ-D-02 | PRJ-0012 vs future WEB-* | **Class boundary** | No |
| SHPIG-PRJ-D-03 | vs PRJ-0009..0011 | **Distinct org** | No |
| SHPIG-PRJ-D-04 | vs FUT-01 WP automation | **Distinct** — future held | No |
| SHPIG-PRJ-D-05 | vs FUT-02 SEO program | **Distinct** — future held | No |
| SHPIG-PRJ-D-06 | Single vs multi-project stack slices | **Not duplicate** — EFV-03 | No |
| SHPIG-PRJ-D-07 | vs ORG-0001..0007 | **Distinct** — no merge | No |
| SHPIG-PRJ-D-08 | vs Makita / ZPM / SIBCAR | **Distinct** — integrity pass | No |
| SHPIG-PRJ-D-09 | Historical deprecated twin | **N/A** — no historical Project | No |

**Duplicate review summary:** **Pass**

---

## 8. SAFE UNKNOWN index

| id | topic | blocks_attestation |
|----|-------|-------------------|
| SU-SHPIG-PRJ-01 | Contract dates | **No** |
| SU-SHPIG-PRJ-02 | Acceptance dates | **No** |
| SU-SHPIG-PRJ-03 | Legal signatory | **No** |
| SU-SHPIG-PRJ-04 | Internal client contacts | **No** |
| SU-SHPIG-PRJ-05 | Future SEO contract | **No** |
| SU-SHPIG-PRJ-06 | Future Direct contract | **No** |
| SU-SHPIG-PRJ-07 | Future AI automation work | **No** |
| SU-SHPIG-PRJ-08 | Delivery phase precision | **No** |
| SU-SHPIG-PRJ-09 | ACF / custom programming scope | **No** |
| SU-SHPIG-PRJ-10 | Person ↔ Project edges | **No** — out of scope |
| SU-SHPIG-PRJ-11 | CLIENT_OF commercial edge | **No** — Wave 6 |
| SU-SHPIG-PRJ-12 | Domain registrant | **No** — Wave 5 |

---

## 9. Deferred register (Wave 3B+ and future intake)

| Item | Reason | Target wave |
|------|--------|-------------|
| REL-SHPIG-PJ-01 PRJ-0012 → ORG-0008 **COMMISSIONED_BY** | Attested | **Wave 3B-SHPIG** — **active** AT-W3B-SHPIG-01 |
| REL-SHPIG-PJ-02 ORG-0001 → PRJ-0012 **EXECUTES** | Attested | **Wave 3B-SHPIG** — **active** AT-W3B-SHPIG-01 |
| SHPIGOVSKY-INTAKE-FUT-01..02 | No start evidence | **Hold** |
| Future SEO / Direct / AI automation contracts | No start evidence | **Hold** |
| CLIENT_OF ORG-0008 → ORG-0001 | Commercial review | **Wave 6** |
| WEB-SHPIG-01 / DOM-SHPIG-01 | Attested | **Waves 4–5** — **active** |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-POPULATION-v1.md) | Per-project analysis and exclusions |
| [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ATTESTATION-v1.md) | Attestation gates and verdict |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Core Wave 3 roster PRJ-0001..0008 |
| [ATLAS-SHPIGOVSKY-INTAKE-SUMMARY-v1.md](ATLAS-SHPIGOVSKY-INTAKE-SUMMARY-v1.md) | Intake executive summary |

---

*ATLAS Wave 3 Shpigovsky Project Register v1 — PRJ-0012 **active** — AT-W3-SHPIG-01 complete.*
