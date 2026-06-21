# ATLAS Agreement Active Attestation v1

**Status:** **attested** — Wave AGL-01 ACTIVE Agreement subset verification act.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Wave:** AGL-01 — Agreement Layer Foundation  
**Attestor role:** Registry Steward (delegated)  
**Parent:** [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) · [ATLAS-AGREEMENT-REGISTER-v1.md](ATLAS-AGREEMENT-REGISTER-v1.md)  
**Is not:** runtime export, legal validity confirmation, renewal schedule.

---

## 1. Purpose

Determine which Agreement records in Wave AGL-01 register are **ACTIVE** — currently effective commercial work anchors — versus **EXPIRED** or **not attested**.

**Normative question answered:**

> Which agreements are ACTIVE right now for operational consumption?

No assumptions beyond documented evidence.

---

## 2. Active attestation act

По [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) §2.2:

**ACTIVE** = attested Agreement row where linked Project lifecycle is **active** and delivery graph (COMMISSIONED_BY + EXECUTES) is attested **active**.

**Result:** **6** agreements attested **ACTIVE** · **2** attested **EXPIRED** · **0** PLANNED · **ORG-0007** — **not attested** (full SAFE UNKNOWN).

---

## 3. ACTIVE roster — full table

| agreement_id | client_org | vendor_org | agreement_type | related_projects | project_lifecycle | evidence_level | active_basis |
|--------------|------------|------------|----------------|------------------|-------------------|----------------|--------------|
| AGR-0002 | ORG-0004 Триумф | ORG-0001 Полигон | DEVELOPMENT | PRJ-0005 | **active** | E1 | REL-0019/0020; ongoing delivery |
| AGR-0003 | ORG-0004 Триумф | ORG-0001 Полигон | SEO_RETAINER | PRJ-0006 | **active** | E1 | REL-0021/0022; SEO scope |
| AGR-0004 | ORG-0004 Триумф | ORG-0001 Полигон | DEVELOPMENT | PRJ-0007 | **active** | E1 | REL-0023/0024 |
| AGR-0005 | ORG-0004 Триумф | ORG-0001 Полигон | DEVELOPMENT | PRJ-0008 | **active** | E1 | REL-0025/0026; WF-01 contour |
| AGR-0006 | ORG-0005 ЗПМ | ORG-0001 Полигон | DEVELOPMENT | PRJ-0009 | **active** | E0 | REL-ZPM-PJ-01/02; WIP catalog |
| AGR-0008 | ORG-0006 SIBCAR | ORG-0001 Полигон | DEVELOPMENT | PRJ-0011 | **active** | E0 | REL-SIBCAR-PJ-01/02; OCPilot WIP |

---

## 4. ACTIVE roster — by client

### 4.1 ORG-0004 Триумф — 4 ACTIVE

| agreement_id | related_projects | agreement_type |
|--------------|------------------|----------------|
| AGR-0002 | PRJ-0005 Грузотакси | DEVELOPMENT |
| AGR-0003 | PRJ-0006 SEO gktriumph.ru | SEO_RETAINER |
| AGR-0004 | PRJ-0007 Блог gktriumph.ru | DEVELOPMENT |
| AGR-0005 | PRJ-0008 Манипулятор | DEVELOPMENT |

### 4.2 ORG-0005 ЗПМ — 1 ACTIVE

| agreement_id | related_projects | agreement_type |
|--------------|------------------|----------------|
| AGR-0006 | PRJ-0009 Каталог-платформа bzpm.ru | DEVELOPMENT |

### 4.3 ORG-0006 SIBCAR — 1 ACTIVE

| agreement_id | related_projects | agreement_type |
|--------------|------------------|----------------|
| AGR-0008 | PRJ-0011 OpenCart dealership | DEVELOPMENT |

---

## 5. NOT ACTIVE — attested EXPIRED

| agreement_id | client_org | related_projects | status | reason |
|--------------|------------|------------------|--------|--------|
| AGR-0001 | ORG-0004 | PRJ-0004 Редизайн | **EXPIRED** | PRJ-0004 **deprecated** — completed delivery |
| AGR-0007 | ORG-0005 | PRJ-0010 Исходный bzpm.ru | **EXPIRED** | PRJ-0010 **deprecated** — historical delivery |

**Rule applied:** EXPIRED status from project lifecycle — **not** from missing end_date.

---

## 6. NOT ATTESTED — SAFE UNKNOWN

| client_org | candidate scope | posture | blocker |
|------------|-----------------|---------|---------|
| ORG-0007 Макита | SEO on makita-snab.ru + makita-land.ru | **Not attested** | No Project; no CLIENT_OF to ORG-0003; CC absent |
| ORG-0007 Макита | Yandex Direct | **Not attested** | Steward scope — not agreement layer |
| ORG-0005 ЗПМ | SEO (FUT-01) | **Not attested** | No Project |
| ORG-0005 ЗПМ | Контекстная реклама (FUT-02) | **Not attested** | No Project |
| ORG-0005 ЗПМ | AI automation (FUT-03) | **Not attested** | No Project |
| ORG-0005 ЗПМ | OpenCartPilot maintenance (FUT-04) | **Not attested** | No Project |
| ORG-0006 SIBCAR | Yandex Direct standalone (FUT-01) | **Not attested** | No Project |
| ORG-0006 SIBCAR | Custom modules (FUT-02) | **Not attested** | No Project |
| ORG-0006 SIBCAR | PROD migration (FUT-03) | **Not attested** | No Project |

**No PLANNED rows** in AGL-01 — future intakes held in population plan only.

---

## 7. OPS consumption matrix

| OPS question | AGL-01 answer | Coverage |
|--------------|---------------|----------|
| Which agreement covers ORG-0004? | AGR-0002..0005 (ACTIVE) | **Partial** — 4 active streams; dates UNKNOWN |
| Which agreement covers PRJ-0008? | **AGR-0005** | **Pass** |
| Agreement status for PRJ-0006? | **ACTIVE** (AGR-0003) | **Pass** |
| Agreement period? | **SAFE UNKNOWN** (all rows) | **Gap** — expected |
| Agreement scope? | scope_summary on each row | **Pass** |
| Which agreement covers ORG-0007? | **None attested** | **SAFE UNKNOWN** |
| WF-02 document closing anchor? | ACTIVE rows available for 3/4 clients | **Partial** |

---

## 8. Verification checklist

| Check | Result |
|-------|--------|
| Every ACTIVE row has active Project | **Pass** (6/6) |
| Every ACTIVE row has COMMISSIONED_BY + EXECUTES | **Pass** (6/6) |
| EXPIRED rows have deprecated Project | **Pass** (2/2) |
| No ACTIVE row without project graph | **Pass** |
| Makita — no assumed ACTIVE | **Pass** |
| Dates not invented | **Pass** |

---

## 9. Summary counts

| Metric | Count |
|--------|-------|
| Register total | **8** |
| **ACTIVE** (this act) | **6** |
| **EXPIRED** | **2** |
| **PLANNED** | **0** |
| **Not attested** (Makita + futures) | **9** candidate scopes — SAFE UNKNOWN |
| Active client orgs with ≥1 ACTIVE agreement | **3/4** evaluated |
| Active projects with agreement binding | **6/6** active client-delivery projects |

---

## 10. Related documents

| Document | Role |
|----------|------|
| [ATLAS-AGREEMENT-REGISTER-v1.md](ATLAS-AGREEMENT-REGISTER-v1.md) | Full roster |
| [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) | Parent attestation act |
| [REPORT-atlas-agreement-layer-foundation-v1.md](../reports/REPORT-atlas-agreement-layer-foundation-v1.md) | Wave summary |

---

*ATLAS Agreement Active Attestation v1 — Wave AGL-01. ACTIVE subset verification.*
