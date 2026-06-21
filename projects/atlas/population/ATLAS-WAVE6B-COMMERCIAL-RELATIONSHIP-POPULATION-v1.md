# ATLAS Wave 6B Commercial Relationship Population v1

**Status:** **documented** — Wave 6B canonical Organization ↔ Organization commercial relationship population plan (ZPM + SIBCAR).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md)  
**Is not:** runtime, API, database schema, relationship attestation act, Foundation amendment, new entity creation.

**Prerequisites (operator-confirmed):**

- Wave 6A Commercial Relationships: **COMPLETE** (REL-0016 attested)
- Wave 1B ZPM Organization: **COMPLETE** — ORG-0005 **active** (AT-W1B-01)
- Wave 1C SIBCAR Organization: **COMPLETE** — ORG-0006 **active** (AT-W1C-01)
- Wave 3B ZPM Project Relationships: **COMPLETE** — REL-ZPM-PJ-01..04
- Wave 4B ZPM Website Relationships: **COMPLETE** — REL-ZPM-WB-01, 03, 04
- Wave 5 ZPM Domain: **COMPLETE** — DOM-ZPM-01 **active**
- Population verdict: **READY FOR WAVE 6B COMMERCIAL RELATIONSHIP POPULATION**

---

## 1. Purpose

Зафиксировать **канонический план population** Wave 6B: расширение commercial graph двумя **CLIENT_OF** рёбрами для уже аттестированных client organizations **ЗПМ** (ORG-0005) и **SIBCAR** (ORG-0006) к vendor **Полигон** (ORG-0001), по тому же шаблону, что **REL-0016** (Triumph).

**Normative scope Wave 6B:**

```text
Organization ↔ Organization commercial relationships only
Type: CLIENT_OF only (approved operator list)
Endpoints: ORG-0005 ЗПМ, ORG-0006 SIBCAR → ORG-0001 Полигон
Authority precedent: REL-0016 (ORG-0004 → ORG-0001)
No VENDOR_OF, PARTNER_OF, SUPPLIER_OF
No new Organizations, Legal Entities, Persons, Projects, Websites, Domains
No new entity types
No new relationship families
```

**Binding operator business reality:**

- ЗПМ (**ORG-0005**) **purchases services from** Polygon (**ORG-0001**).
- SIBCAR (**ORG-0006**) **purchases services from** Polygon (**ORG-0001**).
- Canonical edges:
  - **ORG-0005 ──CLIENT_OF──► ORG-0001** (REL-0040)
  - **ORG-0006 ──CLIENT_OF──► ORG-0001** (REL-0041)
- Direction identical to **REL-0016**: client = subject; vendor = object.

**Identifier note (correction):** ранние ZPM deferral-документы ссылались на «REL-0016» для ORG-0005 CLIENT_OF как **placeholder слота** — **REL-0016** канонически занят Triumph (Wave 6A). Wave 6B назначает **REL-0040** и **REL-0041** как следующие sequential org↔org commercial ids после REL-0039.

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **2** |
| Organization endpoints (active) | **3** (ORG-0001, ORG-0005, ORG-0006) |
| Relationship family used | Organization → Organization only |
| Relationship types used | **CLIENT_OF** only |
| Commercial graph after Wave 6B | **3** CLIENT_OF edges (incl. REL-0016) |

### 2.1 Summary table

| relationship_id | source_organization | target_organization | relationship_type | commercial role | attestation readiness |
|-----------------|---------------------|---------------------|-------------------|-----------------|-----------------------|
| REL-0040 | ORG-0005 ООО «ЗПМ» | ORG-0001 Веб-студия «Полигон» | **CLIENT_OF** | ЗПМ = client; Polygon = vendor | **ready** |
| REL-0041 | ORG-0006 ООО «СибКар» | ORG-0001 Веб-студия «Полигон» | **CLIENT_OF** | SIBCAR = client; Polygon = vendor | **ready** |

---

## 3. Per-relationship analysis

### 3.1 REL-0040 — ORG-0005 → ORG-0001 CLIENT_OF

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0040 |
| **source_organization** | ORG-0005 ЗПМ |
| **target_organization** | ORG-0001 Веб-студия «Полигон» |
| **relationship_type** | **CLIENT_OF** |
| **attestation_basis** | E1 EV-W1B-CC-01; ORG-0005 **active** (AT-W1B-01); ORG-0005 **business_role CLIENT**; E1 Wave 3B-ZPM project corroboration (PRJ-0009 **COMMISSIONED_BY** ORG-0005, **EXECUTES** ORG-0001; PRJ-0010 historical pair); E0 EV-ZPM-OP-ACT-01 / EV-ZPM-OP-HIST-01; Wave 4B REL-ZPM-WB-04 ORG-0005 **OWNS** WEB-ZPM-01; operator-confirmed: ЗПМ purchases services from Polygon |
| **evidence_tier** | **E1** (primary CC + structural corroboration); E0 operator statements |
| **lifecycle_state** | **active** (target upon attestation) |
| **slot** | CLIENT_OF, ORG-0005 → ORG-0001 |
| **notes** | Full ZPM stack attested; strongest Wave 6B candidate (C-01 / P0) |

### 3.2 REL-0041 — ORG-0006 → ORG-0001 CLIENT_OF

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0041 |
| **source_organization** | ORG-0006 SIBCAR |
| **target_organization** | ORG-0001 Веб-студия «Полигон» |
| **relationship_type** | **CLIENT_OF** |
| **attestation_basis** | E1 EV-W1C-CC-01; ORG-0006 **active** (AT-W1C-01); ORG-0006 **business_role CLIENT** (W1-C); Polygon channel Category A (`sibcar\` CC path per [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md)); operator-confirmed: SIBCAR purchases services from Polygon; OCPilot SITE-001 engagement context *(informational — not sole proof)* |
| **evidence_tier** | **E1** (CC path); project-level corroboration **absent** |
| **lifecycle_state** | **active** (target upon attestation) |
| **slot** | CLIENT_OF, ORG-0006 → ORG-0001 |
| **notes** | Weaker structural corroboration than REL-0040 / REL-0016 — no attested Project COMMISSIONED_BY/EXECUTES pair; E1 CC + CLIENT role sufficient per §4.6 |

---

## 4. Required analysis

### 4.1 Commercial reality validation

| Check | REL-0040 (ZPM) | REL-0041 (SIBCAR) | Basis |
|-------|----------------|-------------------|-------|
| Org is **client** of operator delivery stack | **Pass** | **Pass** | W1-B / W1-C **CLIENT** role; AT-W1B-01 / AT-W1C-01 |
| Polygon is **delivery / vendor org** | **Pass** | **Pass** | REL-ZPM-PJ-02, 04 **EXECUTES**; REL-0018..0026 Triumph precedent |
| Active or historical commercial delivery | **Pass** | **Partial** | ZPM: PRJ-0009 **active**; SIBCAR: no attested Project — OCPilot context only |
| OPS «Client» maps to Organization + CLIENT_OF | **Pass** | **Pass** | [OPS-ATLAS-ALIGNMENT-v1.md](../foundation/OPS-ATLAS-ALIGNMENT-v1.md) §4.2 |
| CC alone auto-creates CLIENT_OF | **Rejected path** | **Rejected path** | [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) CC-EDO-01 — multi-source E1 |
| Contract / invoice as primary evidence | **Not used** | **Not used** | OAR-BAN-01 — structural E1 sufficient |

**Verdict:** Commercial reality **validated** for both edges at org↔org structural level.

### 4.2 Evidence review

| Ref | Artifact | REL-0040 | REL-0041 |
|-----|----------|----------|----------|
| EV-W1B-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx` | **Primary E1** — client endpoint | — |
| EV-W1C-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | — | **Primary E1** — client endpoint |
| EV-0003 | `polygon/ИП Русецкий А. А.pdf` (LE-0001) | Vendor endpoint | Vendor endpoint |
| Wave 3B-ZPM register | REL-ZPM-PJ-01..04 | **Corroboration** | — |
| Wave 4B-ZPM register | REL-ZPM-WB-04 ORG-0005 **OWNS** | **Corroboration** | — |
| EV-ZPM-OP-ACT-01 / EV-ZPM-OP-HIST-01 | Operator statements | **Corroboration** | — |
| EV-W1C-02 / EV-W1C-03 | OCPilot SITE-001 docs | — | **Informational only** |
| REL-0016 | ORG-0004 → ORG-0001 **active** | Direction template | Direction template |
| Operator intake | Wave 6B approved business reality | E0 overlay | E0 overlay |
| **Excluded** | Contracts, acts, invoices | Not invented | Not invented |

**Minimum tier:** E1 for CLIENT_OF per [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) — **met** for both.

### 4.3 Lifecycle validation

| Rule | Check | Result |
|------|-------|--------|
| LC-P02 | Both endpoints **active** before **active** edge | **Pass** — ORG-0001, ORG-0005, ORG-0006 attested |
| Target state | **active** post steward attestation | **ready** |
| FORMER_CLIENT_OF | Not applicable — relationships ongoing | — |
| disputed | No conflicting canonical slot | **Pass** |
| effective_from / effective_to | Not attested at Wave 6B | **SAFE UNKNOWN** — see §6 |

### 4.4 Duplicate review

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| W6B-D-01 | REL-0040 vs REL-0016 (same vendor, different client) | **Distinct slots** — ORG-0005 ≠ ORG-0004 | No |
| W6B-D-02 | REL-0041 vs REL-0016 / REL-0040 | **Distinct slots** — ORG-0006 ≠ ORG-0004 / ORG-0005 | No |
| W6B-D-03 | ORG-0005 vs ORG-0006 homonym / merge | **Distinct** — W1B-D-01 / W1C-D-01 prior pass | No |
| W6B-D-04 | Dual CLIENT_OF same pair | **None** — single canonical direction each | No |
| W6B-D-05 | Prior «REL-0016» ZPM placeholder | **Resolved** — REL-0040 assigned; no id collision | No |

**Verdict:** No duplicate or conflicting commercial slots detected.

### 4.5 Relationship direction validation

```text
Business fact:  Client org purchases services from Polygon
Taxonomy rule:  Subject (client) ──CLIENT_OF──► Object (vendor)

REL-0016:  ORG-0004 Триумф  ──CLIENT_OF──► ORG-0001 Полигон   ✓  [Wave 6A — attested]
REL-0040:  ORG-0005 ЗПМ     ──CLIENT_OF──► ORG-0001 Полигон   ✓  [Wave 6B — proposed]
REL-0041:  ORG-0006 SIBCAR  ──CLIENT_OF──► ORG-0001 Полигон   ✓  [Wave 6B — proposed]
```

| Direction candidate | Verdict | Reason |
|---------------------|---------|--------|
| ORG-0005 → CLIENT_OF → ORG-0001 | **Approved** | Subject = client; object = vendor |
| ORG-0006 → CLIENT_OF → ORG-0001 | **Approved** | Subject = client; object = vendor |
| ORG-0001 → CLIENT_OF → ORG-0005 / ORG-0006 | **Rejected** | Would assert Polygon is client — contradicts business reality |
| ORG-0001 → VENDOR_OF → clients | **Not created** | Out of Wave 6B scope |
| Dual CLIENT_OF (both directions) | **Rejected** | Taxonomy symmetry — not attested |

**Cross-check vs REL-0016:** ORG-0004, ORG-0005, ORG-0006 use **identical CLIENT_OF direction** — **Pass**.

**SC-R02 alignment:** CLIENT_OF = subject org is **client** of object org — **Pass**.

### 4.6 Foundation consistency

| Foundation doc | Wave 6B alignment |
|----------------|-------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Directed Org→Org edges; RP-04 single canonical CLIENT_OF slot per pair — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §2 | CLIENT_OF in Organization ↔ Organization family — **yes** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target **active** after attestation — **yes** |
| [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](../foundation/ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §6.1 | Direction verified before affirm — **yes** |
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) | Organization endpoints only — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required — **yes** |
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | Wave 6B readiness gate satisfied — **yes** |

**No Foundation changes.** **No new entity types.** **No new relationship families.**

---

## 5. Commercial graph discipline — expanded view

```text
ORG-0004 Триумф  ──CLIENT_OF──► ORG-0001 Полигон     [Wave 6A — REL-0016 attested]
ORG-0005 ЗПМ     ──CLIENT_OF──► ORG-0001 Полигон     [Wave 6B — REL-0040]
ORG-0006 SIBCAR  ──CLIENT_OF──► ORG-0001 Полигон     [Wave 6B — REL-0041]

── ZPM project corroboration (independent families) ──
PRJ-0009 ──COMMISSIONED_BY──► ORG-0005    ORG-0001 ──EXECUTES──► PRJ-0009
PRJ-0010 ──COMMISSIONED_BY──► ORG-0005    ORG-0001 ──EXECUTES──► PRJ-0010
ORG-0005 ──OWNS──► WEB-ZPM-01

── Triumph project corroboration (reference) ──
PRJ-0004..0008 ──COMMISSIONED_BY──► ORG-0004    ORG-0001 ──EXECUTES──► PRJ-0004..0008
```

**Layering rule:** CLIENT_OF is **org-level commercial structure**. Project COMMISSIONED_BY / EXECUTES, Website OWNS, Domain PRIMARY_DOMAIN remain **independent** attested families.

---

## 6. Explicit exclusions and deferred commercial relationships

| Item | Treatment | Target |
|------|-----------|--------|
| ORG-0001 → **VENDOR_OF** → clients | **Do not create** | Out of Wave 6B scope |
| **PARTNER_OF** / **SUPPLIER_OF** (any pair) | **Do not create** | No attested peer partnership |
| ORG-0007 Makita → ORG-0003 i-SEO CLIENT_OF | **Deferred** | E0 channel — separate intake (C-03) |
| Moscow SERM / Metallka commercial edges | **Deferred** | Organization not populated |
| W1-C other latent historical clients | **Deferred** | Future Organization + commercial pass |
| Person / Project / Website / Domain new edges | **Out of scope** | No new entities |
| Contract value, SOW, invoice metadata on edge | **Forbidden** | RP-03 / RR-09 |
| Invented contracts / invoices / acts | **Forbidden** | Evidence First discipline |

---

## 7. SAFE UNKNOWN inventory

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W6B-01** | REL-0040 / REL-0041 `effective_from` / `effective_to` | Low | Optional future enrichment |
| **SU-W6B-02** | Service line granularity on CLIENT_OF edges | Low | Not encoded per RP-03 |
| **SU-W6B-03** | Whether formal E2 contract extract exists externally (ZPM / SIBCAR) | Low | Not required for structural E1 |
| **SU-W6B-04** | SIBCAR project-level COMMISSIONED_BY / EXECUTES corroboration | Medium | Does **not** block REL-0041 — CC + CLIENT role sufficient |
| **SU-W6B-05** | OCPilot SITE-001 binding to ORG-0006 vs ORG-0005 disambiguation | Low | Resolved at org layer — distinct INN |
| **SU-W6B-06** | Prior ZPM docs «REL-0016» placeholder label | Low | **Resolved** — REL-0040 canonical id |

---

## 8. Readiness assessment

| Criterion | Status |
|-----------|--------|
| Wave 6A commercial anchor (REL-0016) attested | **Pass** |
| ORG-0005, ORG-0006 endpoints **active** | **Pass** |
| Evidence E1 minimum for CLIENT_OF | **Pass** |
| Direction consistent with REL-0016 | **Pass** |
| Duplicate review complete | **Pass** |
| No Foundation changes required | **Pass** |

```text
READY FOR WAVE 6B COMMERCIAL RELATIONSHIP ATTESTATION
```

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | Canonical commercial relationship roster |
| [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | Prior commercial graph (REL-0016) |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | ZPM project corroboration |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |
