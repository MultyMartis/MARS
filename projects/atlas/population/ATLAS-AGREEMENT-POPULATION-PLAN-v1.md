# ATLAS Agreement Population Plan v1

**Status:** **documented** — Wave AGL-01 population evaluation (evidence-based; no runtime).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Wave:** AGL-01 — Agreement Layer Foundation  
**Parent:** [ATLAS-AGREEMENT-REALITY-MODEL-v1.md](../foundation/ATLAS-AGREEMENT-REALITY-MODEL-v1.md) · [ATLAS-POPULATION-STRATEGY-v1.md](../foundation/ATLAS-POPULATION-STRATEGY-v1.md)  
**Is not:** attestation act, register export, contract discovery, automated extraction.

---

## 1. Purpose

Evaluate **ORG-0004 Триумф**, **ORG-0005 ЗПМ**, **ORG-0006 SIBCAR**, and **ORG-0007 Макита** for Agreement Layer population readiness.

Determine:

- Which agreements can be **attested now**
- Which remain **SAFE UNKNOWN**
- Granularity rule for Wave AGL-01

**Evidence rule:** No guessing. Structural graph + operator attestation + project scope only.

---

## 2. Population scope

| In scope | Out of scope |
|----------|--------------|
| Four operator client orgs (W1 / W1-B / W1-C / W1-D) | ORG-0001..0003 internal vendor/agency agreements |
| Project-scoped commercial reality anchors | Contract text ingestion |
| Polygon vendor delivery (ORG-0001) | i-SEO vendor edges not yet attested |
| Documentation-only register rows | Runtime, API, registry file changes |

---

## 3. Granularity decision (AGL-01)

| Option | Decision |
|--------|----------|
| One umbrella agreement per CLIENT_OF edge | **Rejected** — loses project-level OPS binding |
| One agreement per attested Project delivery stream | **Approved** — default for AGL-01 |
| One agreement per inferred service line without Project | **Rejected** — EFV-03 inference |

**Rationale:** OPS WF-01 live binding pilot (2026-06-10) requires answering «which agreement covers **this project**» — project-scoped anchors satisfy without inventing legal document boundaries.

---

## 4. Client evaluation — ORG-0004 Триумф

| Field | Value |
|-------|-------|
| **org_id** | ORG-0004 |
| **Vendor (delivery)** | ORG-0001 Полигон |
| **Commercial edge** | REL-0016 CLIENT_OF — **active** (Wave 6A) |
| **Attested projects** | PRJ-0004..0008 |
| **Project relationships** | REL-0017..0026 COMMISSIONED_BY + EXECUTES — **active** (Wave 3B) |
| **Commercial evidence** | E1 EV-0005 (`triumph/…2024.xlsx`); E1 LE-0003 |

### 4.1 Per-project readiness

| project_id | canonical_name | lifecycle | agreement_type (inferred from scope) | Population verdict | Blocker |
|------------|----------------|-----------|--------------------------------------|--------------------|---------|
| PRJ-0004 | Редизайн gktriumph.ru | **deprecated** | DEVELOPMENT | **Attest EXPIRED** | Dates **SAFE UNKNOWN** |
| PRJ-0005 | Грузотакси | **active** | DEVELOPMENT | **Attest ACTIVE** | Dates **SAFE UNKNOWN** |
| PRJ-0006 | SEO gktriumph.ru | **active** | SEO_RETAINER | **Attest ACTIVE** | Dates **SAFE UNKNOWN** |
| PRJ-0007 | Блог gktriumph.ru | **active** | DEVELOPMENT | **Attest ACTIVE** | Dates **SAFE UNKNOWN** |
| PRJ-0008 | Манипулятор | **active** | DEVELOPMENT | **Attest ACTIVE** | Dates **SAFE UNKNOWN**; WF-01 pilot contour |

### 4.2 SAFE UNKNOWN (Triumph)

| Topic | Posture |
|-------|---------|
| Contract start / end dates | **SAFE UNKNOWN** — no E2 date extract attested |
| Single vs multiple legal contracts | **SAFE UNKNOWN** — project anchors used |
| Retainer billing cadence | **Out of scope** — not registered |
| Umbrella master agreement id | **SAFE UNKNOWN** |

**Triumph summary:** **5** agreements attestable (4 ACTIVE + 1 EXPIRED).

---

## 5. Client evaluation — ORG-0005 ЗПМ

| Field | Value |
|-------|-------|
| **org_id** | ORG-0005 |
| **Vendor (delivery)** | ORG-0001 Полигон |
| **Commercial edge** | REL-0040 CLIENT_OF — **active** (Wave 6B) |
| **Attested projects** | PRJ-0009, PRJ-0010 |
| **Project relationships** | REL-ZPM-PJ-01..04 — **active** (Wave 3B-ZPM) |
| **Commercial evidence** | E1 EV-W1B-CC-01; E0 EV-ZPM-OP-ACT-01 / EV-ZPM-OP-HIST-01 |

### 5.1 Per-project readiness

| project_id | canonical_name | lifecycle | agreement_type | Population verdict | Blocker |
|------------|----------------|-----------|----------------|--------------------|---------|
| PRJ-0009 | Каталог-платформа bzpm.ru | **active** | DEVELOPMENT | **Attest ACTIVE** | Dates **SAFE UNKNOWN** |
| PRJ-0010 | Сайт bzpm.ru (исходная версия) | **deprecated** | DEVELOPMENT | **Attest EXPIRED** | Dates **SAFE UNKNOWN** |

### 5.2 Held — not attested (ZPM)

| intake_label | Topic | Verdict | Reason |
|--------------|-------|---------|--------|
| ZPM-INTAKE-FUT-01 | SEO | **SAFE UNKNOWN** | No Project entity; no start evidence |
| ZPM-INTAKE-FUT-02 | Контекстная реклама | **SAFE UNKNOWN** | No Project entity |
| ZPM-INTAKE-FUT-03 | AI automation | **SAFE UNKNOWN** | No Project entity |
| ZPM-INTAKE-FUT-04 | OpenCartPilot maintenance | **SAFE UNKNOWN** | No Project entity |

### 5.3 SAFE UNKNOWN (ZPM)

| Topic | Posture |
|-------|---------|
| Historical contract dates (PRJ-0010) | **SAFE UNKNOWN** — SU-ZPM-PRJ-01 |
| Production deployment / acceptance | **SAFE UNKNOWN** — Wave 4 scope |

**ZPM summary:** **2** agreements attestable (1 ACTIVE + 1 EXPIRED).

---

## 6. Client evaluation — ORG-0006 SIBCAR

| Field | Value |
|-------|-------|
| **org_id** | ORG-0006 |
| **Vendor (delivery)** | ORG-0001 Полигон |
| **Commercial edge** | REL-0041 CLIENT_OF — **active** (Wave 6B) |
| **Attested projects** | PRJ-0011 |
| **Project relationships** | REL-SIBCAR-PJ-01..02 — **active** (Wave 3B-SIBCAR) |
| **Commercial evidence** | E1 EV-W1C-CC-01; E0 EV-W1C-02..03, EV-OCP-01..04 |

### 6.1 Per-project readiness

| project_id | canonical_name | lifecycle | agreement_type | Population verdict | Blocker |
|------------|----------------|-----------|----------------|--------------------|---------|
| PRJ-0011 | Автосалон СИБКАР — OpenCart dealership | **active** | DEVELOPMENT | **Attest ACTIVE** | Dates **SAFE UNKNOWN** |

### 6.2 Held — not attested (SIBCAR)

| intake_label | Topic | Verdict | Reason |
|--------------|-------|---------|--------|
| SIBCAR-INTAKE-FUT-01 | Yandex Direct standalone | **SAFE UNKNOWN** | No distinct project boundary |
| SIBCAR-INTAKE-FUT-02 | Custom module development | **SAFE UNKNOWN** | Not started |
| SIBCAR-INTAKE-FUT-03 | PROD migration / launch | **SAFE UNKNOWN** | Public URL unknown |

**SIBCAR summary:** **1** agreement attestable (ACTIVE).

---

## 7. Client evaluation — ORG-0007 Макита

| Field | Value |
|-------|-------|
| **org_id** | ORG-0007 Макита Снаб |
| **Vendor (operational context)** | ORG-0003 i-SEO *(not attested commercial edge)* |
| **Commercial edge** | **None attested** — ORG-0007 → ORG-0003 CLIENT_OF **deferred** (Wave 6B §6) |
| **Attested projects** | **None** |
| **Steward boundary** | Yandex Direct only; **explicitly excludes** contracts / accounting / document flow (EV-MAKITA-OP-01) |
| **Legal entity** | **SAFE UNKNOWN** — no CC |
| **Counterparty card** | **Absent** — blocks E1+ |

### 7.1 Readiness matrix

| Candidate scope | vendor_org | Verdict | Reason |
|-----------------|------------|---------|--------|
| SEO on makita-snab.ru + makita-land.ru | ORG-0003 i-SEO | **Do not register** | No attested Project; no CLIENT_OF; steward excludes contract scope |
| PPC / Yandex Direct | ORG-0003 or steward | **Do not register** | Operational signal only — not agreement anchor |
| Any Makita ↔ Polygon arrangement | ORG-0001 | **Do not register** | No delivery graph |

**Makita summary:** **0** agreements attestable — **full SAFE UNKNOWN** for Agreement Layer until commercial graph + project population complete.

---

## 8. Population readiness summary

| client_org | Attestable now | ACTIVE | EXPIRED | SAFE UNKNOWN (no row) |
|------------|----------------|--------|---------|------------------------|
| ORG-0004 Триумф | **5** | 4 | 1 | Dates; legal contract count |
| ORG-0005 ЗПМ | **2** | 1 | 1 | 4 future service intakes |
| ORG-0006 SIBCAR | **1** | 1 | 0 | 3 future intakes |
| ORG-0007 Макита | **0** | 0 | 0 | **All agreement fields** |
| **Total** | **8** | **6** | **2** | Makita + 7 future intakes |

---

## 9. Evidence index (population references)

| Ref | Artifact | Clients / projects |
|-----|----------|-------------------|
| REL-0016 | Wave 6A commercial register | ORG-0004 vendor context |
| REL-0040, REL-0041 | Wave 6B commercial register | ORG-0005, ORG-0006 |
| REL-0017..0026 | Wave 3B project relationships | Triumph PRJ-0004..0008 |
| REL-ZPM-PJ-01..04 | Wave 3B-ZPM | PRJ-0009, PRJ-0010 |
| REL-SIBCAR-PJ-01..02 | Wave 3B-SIBCAR | PRJ-0011 |
| EV-0005 | `triumph/…2024.xlsx` | ORG-0004 E1 overlay |
| EV-W1B-CC-01 | ZPM counterparty card | ORG-0005 |
| EV-W1C-CC-01 | SIBCAR counterparty card | ORG-0006 |
| EV-ZPM-OP-ACT-01 / HIST-01 | Operator statements | PRJ-0009, PRJ-0010 |
| EV-MAKITA-OP-01..03 | Makita intake | Exclusion boundary only |
| OPS-WF01-LIVE-BINDING-PILOT | WF-01 pilot 2026-06-10 | PRJ-0008 gap driver |

---

## 10. Deferred register

| Item | Reason | Target |
|------|--------|--------|
| ORG-0007 any agreement | No project + no commercial edge + CC absent | Future Makita commercial + project waves |
| ZPM FUT-01..04 | No Project entities | Future intake |
| SIBCAR FUT-01..03 | No Project entities | Future intake |
| Umbrella Triumph master agreement | Legal boundary unknown | Operator attestation + E1+ if needed |
| Agreement dates (all attested rows) | No E2 date extract | Future evidence pass |
| ORG-0007 → ORG-0003 SEO_RETAINER | Vendor edge not attested | Wave 6C / Makita commercial pass |

---

## 11. Related documents

| Document | Role |
|----------|------|
| [ATLAS-AGREEMENT-REGISTER-v1.md](ATLAS-AGREEMENT-REGISTER-v1.md) | Attested roster execution |
| [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) | Methodology |
| [ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md](ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md) | ACTIVE subset act |

---

*ATLAS Agreement Population Plan v1 — Wave AGL-01. Evidence-based evaluation only.*
