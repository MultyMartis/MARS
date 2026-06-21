# ATLAS Wave 4B ZPM Website Relationship Population v1

**Status:** **documented** — canonical Website-family relationship population plan for Wave 4B ZPM tranche (ORG-0005).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ** · LE-0004  
**Parent:** [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 5 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- Wave 3 ZPM Projects PRJ-0009, PRJ-0010: **attested** — AT-W3-ZPM-01..02
- Wave 3B ZPM Project ↔ Organization: **COMPLETE** — AT-W3B-ZPM-01..02
- ZPM Website Model Correction: **EXECUTED** — COR-ZPM-WEB-01..12
- Wave 4 ZPM Website attestation: **COMPLETE** — AT-W4-ZPM-01 (WEB-ZPM-01 **active**)
- Population verdict: **READY FOR WAVE 4B ZPM WEBSITE RELATIONSHIP POPULATION**

---

# REPORT — ATLAS Wave 4B ZPM Website Relationship Population

**Population date:** 2026-06-07  
**Tranche:** **POP-W4B-ZPM-01**

---

## 1. Purpose

Зафиксировать **канонический план population** набора **Website-family** relationships для Wave 4B tranche **ZPM** (ORG-0005): состав рёбер, типы, evidence basis, lifecycle intent, deferred items, границы foundation.

**Normative scope Wave 4B ZPM:**

```text
Website → Project BELONGS_TO (REL-ZPM-WB-01, REL-ZPM-WB-03)
Organization → Website OWNS (REL-ZPM-WB-04)
ZPM client property WEB-ZPM-01 only (single Website model)
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

- **OWNS** (Organization → Website) — structural business ownership of web property identity (ORG-0005 → WEB-ZPM-01).
- **BELONGS_TO** (Website → Project) — initiative grouping; one website may belong to **multiple** projects when attested — Triumph precedent REL-0027/0028 on WEB-0006.
- **OPERATES** — **не создавать**; deferred to separate governance review.
- **REL-ZPM-WB-02** — **cancelled** per COR-ZPM-WEB-06 (WEB-ZPM-02 retired).

---

## 2. Approved state (operator-confirmed)

| Entity class | id | canonical_name | lifecycle_state |
|--------------|-----|----------------|-----------------|
| Organization | **ORG-0005** | ЗПМ | **active** |
| Website | **WEB-ZPM-01** | bzpm.ru | **active** |
| Project | **PRJ-0009** | Каталог-платформа bzpm.ru | **active** |
| Project | **PRJ-0010** | Сайт bzpm.ru (исходная версия) | **deprecated** |

---

## 3. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **3** |
| Website endpoints | **1** (WEB-ZPM-01) |
| Project endpoints (BELONGS_TO targets) | **2** (PRJ-0009 **active**, PRJ-0010 **deprecated**) |
| Organization endpoints (OWNS source) | **1** (ORG-0005 ЗПМ) |
| Relationship types used | **BELONGS_TO**, **OWNS** |
| Multi-project websites | **1** (WEB-ZPM-01 → PRJ-0009 + PRJ-0010) |
| Cancelled (not in scope) | **1** (REL-ZPM-WB-02 — COR-ZPM-WEB-06) |

### 3.1 Summary table

| relationship_id | source_id | target_id | relationship_type | attestation readiness |
|-----------------|-----------|-----------|-------------------|-----------------------|
| REL-ZPM-WB-01 | WEB-ZPM-01 bzpm.ru | PRJ-0009 Каталог-платформа bzpm.ru | **BELONGS_TO** | **ready** |
| REL-ZPM-WB-03 | WEB-ZPM-01 bzpm.ru | PRJ-0010 Сайт bzpm.ru (исходная версия) | **BELONGS_TO** | **ready** |
| REL-ZPM-WB-04 | ORG-0005 ЗПМ | WEB-ZPM-01 bzpm.ru | **OWNS** | **ready** |

---

## 4. Per-relationship analysis

### 4.1 WEB-ZPM-01 bzpm.ru — REL-ZPM-WB-01, REL-ZPM-WB-03, REL-ZPM-WB-04

#### REL-ZPM-WB-01 — BELONGS_TO (active catalog platform)

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-WB-01 |
| **source_id** | WEB-ZPM-01 bzpm.ru |
| **target_id** | PRJ-0009 Каталог-платформа bzpm.ru |
| **relationship_type** | **BELONGS_TO** |
| **attestation_basis** | E0 EV-ZPM-OP-ACT-01; WEB-ZPM-01 **active** (AT-W4-ZPM-01); PRJ-0009 **active** (AT-W3-ZPM-01); REL-ZPM-PJ-01 COMMISSIONED_BY context; single-property model COR-ZPM-WEB-03 |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Ongoing catalog-platform initiative grouping on sole `bzpm.ru` Website; Triumph analog REL-0028 (WEB-0006 → PRJ-0006 active) |

#### REL-ZPM-WB-03 — BELONGS_TO (historical site delivery)

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-WB-03 |
| **source_id** | WEB-ZPM-01 bzpm.ru |
| **target_id** | PRJ-0010 Сайт bzpm.ru (исходная версия) |
| **relationship_type** | **BELONGS_TO** |
| **attestation_basis** | E0 EV-ZPM-OP-HIST-01; WEB-ZPM-01 **active** (AT-W4-ZPM-01); PRJ-0010 **deprecated** (AT-W3-ZPM-02); REL-ZPM-PJ-03 COMMISSIONED_BY context; LT-P01 historical structural truth; COR-ZPM-WEB-07 |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | **Multi-project website case** — deprecated project container + active website is valid pattern (W4-LC-02 / LT-P01); Triumph analog REL-0027 (WEB-0006 → PRJ-0004 deprecated); replaces cancelled REL-ZPM-WB-02 |

#### REL-ZPM-WB-04 — OWNS

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-WB-04 |
| **source_id** | ORG-0005 ЗПМ |
| **target_id** | WEB-ZPM-01 bzpm.ru |
| **relationship_type** | **OWNS** |
| **attestation_basis** | E0 EV-ZPM-OP-ACT-01; ORG-0005 **active** (AT-W1B-01); WEB-ZPM-01 **active** (AT-W4-ZPM-01); EV-W1B-CC-01 org anchor; client org owns corporate web property identity; COR-ZPM-WEB-09 |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Structural business ownership — distinct from Polygon EXECUTES on projects; OPERATES for ORG-0001 **not created** |

---

## 5. Multi-project website analysis — WEB-ZPM-01

```text
WEB-ZPM-01 bzpm.ru
    ├── BELONGS_TO ──► PRJ-0009 Каталог-платформа (active project — ongoing initiative)
    └── BELONGS_TO ──► PRJ-0010 Сайт исходная версия (deprecated project — historical deliverable)

ORG-0005 ЗПМ ── OWNS ──► WEB-ZPM-01
```

| Question | Resolution |
|----------|------------|
| May one website BELONGS_TO multiple projects? | **Yes** — foundation cardinality allows when attested; Triumph REL-0027 + REL-0028 precedent |
| Should WEB-ZPM-01 normalize to one project? | **No** — operator-approved; catalog rebuild and historical site are distinct structural groupings on same property (EFV-03 at Project layer) |
| Conflict with deprecated PRJ-0010? | **No** — W4-LC-02 / LT-P01: deprecated project + active website + active BELONGS_TO edge is valid |
| OWNS vs BELONGS_TO overlap? | **No conflict** — OWNS is org-level property identity; BELONGS_TO is project initiative grouping |
| Single Website model honored? | **Yes** — WEB-ZPM-02 retired; COR-ZPM-WEB-01; EIR-W01 |

**Triumph analog (attested reference):**

```text
WEB-0006 gktriumph.ru ──BELONGS_TO──► PRJ-0004 (deprecated)
WEB-0006 gktriumph.ru ──BELONGS_TO──► PRJ-0006 (active)
ORG-0004 Триумф ──OWNS──► WEB-0006
```

---

## 6. Structural graph — ZPM (post 4B-ZPM)

```text
ORG-0005 ЗПМ ──OWNS──► WEB-ZPM-01 bzpm.ru

WEB-ZPM-01 ──BELONGS_TO──► PRJ-0009 (active)
WEB-ZPM-01 ──BELONGS_TO──► PRJ-0010 (deprecated)

(Prior Wave 3B ZPM — unchanged)
PRJ-0009/0010 ──COMMISSIONED_BY──► ORG-0005
ORG-0001 Полигон ──EXECUTES──► PRJ-0009/0010

(Prior Wave 2B ZPM — unchanged)
PER-0014, PER-0015 ──WORKS_FOR──► ORG-0005
```

**Not in this pass:** ORG-0001 ──OPERATES──► WEB-ZPM-01 — deferred; REL-0016 CLIENT_OF — Wave 6.

---

## 7. Validation review

### 7.1 Endpoint lifecycle verification

| Endpoint | Required state | Source act | Verified |
|----------|----------------|------------|----------|
| **ORG-0005** ЗПМ | **active** | AT-W1B-01 | **Pass** |
| **WEB-ZPM-01** bzpm.ru | **active** | AT-W4-ZPM-01 | **Pass** |
| **PRJ-0009** | **active** | AT-W3-ZPM-01 | **Pass** |
| **PRJ-0010** | **deprecated** | AT-W3-ZPM-02 | **Pass** |

### 7.2 Single Website model verification

| Check | Source | Verified |
|-------|--------|----------|
| WEB-ZPM-02 **retired** — not minted | COR-ZPM-WEB-01 | **Pass** |
| REL-ZPM-WB-02 **cancelled** | COR-ZPM-WEB-06 | **Pass** |
| One hostname → one Website | COR-ZPM-WEB-03; Decision §4 | **Pass** |
| EFV-03 at Project layer only | COR-ZPM-WEB-12 | **Pass** |

### 7.3 Triumph precedent alignment

| Check | Triumph reference | ZPM mapping | Verified |
|-------|-------------------|-------------|----------|
| Multi-project BELONGS_TO | REL-0027 + REL-0028 on WEB-0006 | REL-ZPM-WB-01 + REL-ZPM-WB-03 on WEB-ZPM-01 | **Pass** |
| Deprecated project as BELONGS_TO target | PRJ-0004 **deprecated** + REL-0027 **active** | PRJ-0010 **deprecated** + REL-ZPM-WB-03 **active** | **Pass** |
| OWNS separation | REL-0032 ORG-0004 → WEB-0006 | REL-ZPM-WB-04 ORG-0005 → WEB-ZPM-01 | **Pass** |
| No OPERATES in 4B pass | Triumph 4B exclusion | ZPM 4B exclusion | **Pass** |

### 7.4 Duplicate edge review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **ZPM-4B-D-01** | REL-ZPM-WB-01 vs REL-ZPM-WB-03 — same source WEB-ZPM-01 | **Not duplicate** — distinct target projects | No |
| **ZPM-4B-D-02** | vs cancelled REL-ZPM-WB-02 | **Resolved** — source Website retired | No |
| **ZPM-4B-D-03** | vs Triumph REL-0027..0035 | **Distinct org** ORG-0005 vs ORG-0004 | No |
| **ZPM-4B-D-04** | Duplicate BELONGS_TO WEB-ZPM-01 → PRJ-0009 | **None** — single edge | No |
| **ZPM-4B-D-05** | OWNS vs BELONGS_TO type collision | **None** — distinct relationship families | No |
| **ZPM-4B-D-06** | vs Wave 3B REL-ZPM-PJ-01..04 | **Distinct family** Project↔Org vs Website↔Project | No |

**Duplicate review summary:** **Pass**

### 7.5 Exclusion verification

| Check | Result |
|-------|--------|
| No DOM-* entities | **Pass** |
| No PRIMARY_DOMAIN / SECONDARY_DOMAIN | **Pass** |
| No CLIENT_OF | **Pass** |
| No OPERATES | **Pass** |
| No Person → Website | **Pass** |
| No Person → Project | **Pass** |
| No Organization → Domain | **Pass** |

---

## 8. Explicit exclusions and deferred relationships

| Item | Treatment | Target |
|------|-----------|--------|
| REL-ZPM-WB-02 WEB-ZPM-02 → PRJ-0010 **BELONGS_TO** | **Cancelled** — COR-ZPM-WEB-06 | — |
| ORG-0001 OPERATES WEB-ZPM-01 | **Do not create** | SAFE UNKNOWN — separate governance |
| REL-0016 ORG-0005 CLIENT_OF ORG-0001 | **Deferred** | Wave 6 |
| DOM-* `bzpm.ru` | **Do not create** | Wave 5 ZPM |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN | **Do not create** | Wave 5B ZPM |
| Website → Domain | **Do not create** | Wave 5 |
| Person → Website (PER-0014, PER-0015) | **Do not create** | Operator scope |
| Person → Project | **Do not create** | Operator scope |
| Organization → Domain | **Do not create** | Wave 5 |
| WEB-ZPM-02 | **Retired** — not minted | COR-ZPM-WEB-01 |
| ZPM-INTAKE-FUT-01..04 | **Held** | Future intake |

---

## 9. Candidate relationships for Wave 5 ZPM

| Candidate | Type | Endpoints | Prerequisite |
|-----------|------|-----------|--------------|
| DOM-* `bzpm.ru` | Domain entity | — | Wave 5 ZPM Domain population |
| DOM-* → WEB-ZPM-01 | **PRIMARY_DOMAIN** | `bzpm.ru` | Domain attestation + Wave 5B ZPM |
| ORG-0005 → DOM-* | **OWNS** (domain) | registrar / CC evidence | Wave 5; SU-ZPM-PRJ-08 |
| `www.bzpm.ru` | SECONDARY_DOMAIN or redirect | WEB-ZPM-01 | Wave 5 hostname policy — **SAFE UNKNOWN** |

---

## 10. Foundation consistency

| Foundation doc | Wave 4B ZPM alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Directed Website→Project and Org→Website edges — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §5–6 | OWNS (Org→Website), BELONGS_TO (Website→Project) in baseline — **yes** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target state **active** after steward attestation — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints WEB-ZPM-01 / PRJ-0009/0010 / ORG-0005 attested — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship `active`; deprecated PRJ-0010 valid BELONGS_TO target — **yes** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | PRJ-0010 deprecated — historical/grouping edges attestable — **yes** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4 | E0 structural path for client property — **yes** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward attestation path — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required for canonical promotion — **yes** |

**Cross-wave validation:**

| Prior wave doc | Endpoint check |
|----------------|----------------|
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | WEB-ZPM-01 **active** — **Pass** |
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | PRJ-0009/0010 endpoints — **Pass** |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | COMMISSIONED_BY pairs consistent — **Pass** |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Triumph precedent REL-0027/0028 — **Pass** |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | 4B queue corrected — **Pass** |

**No new entity types.** **No new relationship families.** **No Foundation modifications.**

---

## 11. SAFE UNKNOWN inventory

| ID | Topic | Severity | Blocks 4B-ZPM |
|----|-------|----------|---------------|
| **SU-ZPM-PRJ-01** | Historical contract / act dates (PRJ-0010) | Low | **No** |
| **SU-ZPM-PRJ-02** | Formal acceptance document (E1 upgrade path) | Low | **No** |
| **SU-ZPM-PRJ-07** | CLIENT_OF ORG-0005 → ORG-0001 | Medium | **No** — Wave 6 |
| **SU-ZPM-PRJ-08** | Production domain registrant ORG-0005 | Low | **No** — Wave 5 |
| **SU-W4-ZPM-01** | Live URL probe for `bzpm.ru` | Low | **No** — E0 sufficient |
| **SU-W4B-ZPM-01** | ORG-0001 OPERATES WEB-ZPM-01 | Low | **No** — separate governance |
| **SU-W4B-ZPM-02** | `www.bzpm.ru` redirect / secondary hostname | Low | **No** — Wave 5 policy |
| **SU-W3B-ZPM-01** | Dual BELONGS_TO for same hostname | Medium | **Resolved** — REL-ZPM-WB-01 + REL-ZPM-WB-03 |
| **SU-ZPM-PRJ-03** | Deployment replace vs coexistence | Medium | **Resolved** — single Website model |

**Blocking gaps remaining:** **None**

---

## 12. Readiness verdict

```text
READY FOR WAVE 4B ZPM WEBSITE RELATIONSHIP ATTESTATION
```

**Conditions:**

1. All three approved relationships pass endpoint, single-Website, Triumph precedent, and duplicate checks.
2. Attestation executes as **separate act** — population plan ≠ canonical until AT-W4B-ZPM-01..02.
3. REL-ZPM-WB-02 remains **cancelled** — not in attestation scope.
4. Domain entities and PRIMARY_DOMAIN remain **Wave 5 / 5B ZPM**.
5. OPERATES, CLIENT_OF, and Person↔Website remain **excluded**.

---

## 13. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Canonical relationship roster table |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) | Website endpoint prerequisite |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-POPULATION-v1.md) | Core Wave 4B Triumph precedent |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | Correction execution basis |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 4B ZPM Website Relationship Population v1 — documentation only.*
