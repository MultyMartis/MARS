# ATLAS Wave 1D Makita Organization Population v1

**Status:** **documented** — Wave 1D canonical Organization population for Makita Snab (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) · [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Companion:** [ATLAS-WAVE1D-MAKITA-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-REGISTER-v1.md) · [ATLAS-WAVE1D-MAKITA-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-ATTESTATION-v1.md)  
**Supersedes (population posture):** [ATLAS-MAKITA-INTAKE-SUMMARY-v1.md](ATLAS-MAKITA-INTAKE-SUMMARY-v1.md) · [ATLAS-MAKITA-INTAKE-REGISTER-v1.md](ATLAS-MAKITA-INTAKE-REGISTER-v1.md) — «INTAKE ONLY / AWAITING CC» hold lifted for Organization layer.  
**Is not:** runtime, API, automation, database schema, Legal Entity population, relationship creation.

**Wave 1 prerequisite:** Organizations ORG-0001..0006 — **unchanged** (operator-confirmed).

**Wave 1D intent:**

Perform **Operational Organization Evidence Path (OOEP)** intake for **Макита Снаб** as a **Category B** i-SEO client Organization — Organization **active** at **E0**; Legal Entity **deferred**.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Organization** для Wave 1D tranche **Makita Snab**: identity, operational evidence, duplicate review, attestation, и explicit deferrals (Legal Entity, Person, Website, Domain, Project, Relationship).

**Normative scope Wave 1D:**

```text
Organization entity population + attestation (single org: Макита Снаб)
Legal Entity population — DEFERRED (SAFE UNKNOWN)
Wave 2 (future): Person ↔ Organization — only after explicit Person wave decision
Wave 3+ (future): Project — only after commercial evidence
Wave 4 / 5 (future): Website / Domain — candidate assets listed; no mint
Wave 6+ (future): CLIENT_OF edges — only after commercial review
```

**Binding evidence context:**

- **EV-MAKITA-OP-01** — steward intake inputs (2026-06-07) — **E0**.
- **EV-MAKITA-OP-02** — steward statement — both websites exist — **E0**.
- **EV-MAKITA-OP-03** — intake enrichment consolidation — **E0** ([ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md](ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md)).
- **ORG-0007** — canonical Organization id (next after ORG-0006 SIBCAR).
- **No CC** — `makita-snab\` folder absent — Category B path per [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md).

---

## 2. Population roster (canonical)

Источник: operational evidence EV-MAKITA-OP-01..03; duplicate review vs attested Wave 1 orgs ORG-0001..0006.  
**Не** в [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) — Wave 1D post-dataset expansion tranche.

### 2.1 Summary table

| org_id | canonical_name | wave_tier | classification | legal_entity_id | lifecycle (target) | evidence_tier | attestation readiness |
|--------|----------------|-----------|----------------|-----------------|-------------------|---------------|----------------------|
| ORG-0007 | Макита Снаб | **W1-D** | **i-SEO client** | **SAFE UNKNOWN** | **active** | **E0** *(operational)* | **ready** |

**Wave tier:** W1-D — Category B i-SEO client; Operational Organization Evidence Path.

---

## 3. Organization identity analysis

### 3.1 ORG-0007 — Макита Снаб

| Field | Value |
|-------|-------|
| **org_id** | ORG-0007 |
| **canonical_name** | **Макита Снаб** |
| **lifecycle_state** | **active** |
| **wave_tier** | W1-D |
| **classification** | **i-SEO client** |
| **business_role** | **CLIENT** — operational counterparty (SEO + Direct scope) |
| **legal_entity_id** | **SAFE UNKNOWN** — LE-* not created |
| **primary_contact_person_id** | **SAFE UNKNOWN** — PER-* not minted; contact **Артём** recorded as operational signal only |
| **primary_website (display candidate)** | **SAFE UNKNOWN** — two candidates; no primary designation |
| **primary_domain (display candidate)** | **SAFE UNKNOWN** |
| **edo_enabled** | **SAFE UNKNOWN** |
| **notes** | Category B; no contract / accounting / document access in steward scope |

### 3.2 Required SAFE UNKNOWN fields (Legal Entity layer)

| Field | Value |
|-------|-------|
| Legal entity | **SAFE UNKNOWN** |
| INN | **SAFE UNKNOWN** |
| KPP | **SAFE UNKNOWN** |
| OGRN | **SAFE UNKNOWN** |
| Legal signatory | **SAFE UNKNOWN** |
| EDO | **SAFE UNKNOWN** |

### 3.3 Operational contact signals *(not PER-* mint)*

| Signal | Value | Evidence |
|--------|-------|----------|
| Primary contact *(given name)* | **Артём** | EV-MAKITA-OP-01 |
| Phone | **+7 926 022-30-91** | EV-MAKITA-OP-01 |
| Direct communication | Steward ↔ **Артём** | EV-MAKITA-OP-01; EV-MAKITA-OP-03 |

### 3.4 Identity disambiguation (evidence-only)

| Signal | Resolution | Evidence |
|--------|------------|----------|
| **Макита Снаб** vs **ORG-0001..0006** | **Distinct** | No identifier collision; new display name |
| **Макита Снаб** vs global «Makita» tool brand | **Open — low** | Trade-name homonym; legal identity **SAFE UNKNOWN** |
| **makita-snab.ru** / **makita-land.ru** vs org identity | **Candidates only** | EFV-03; no WEB-* / DOM-* mint |
| ORCA Makita pilot | **Excluded** | EFV-02 — pilot ≠ Organization |

**Alias policy (EFV-01):** No attested aliases without CC. **Макита Снаб** is **canonical_name** from operational evidence — not a legal alias cluster.

---

## 4. Legal entity analysis — DEFERRED

| Check | Result |
|-------|--------|
| CC present | **No** — Category B; LE population **deferred** per OOER-02 |
| LE-* creation | **Prohibited** — STOP-OOER-02 |
| Legal entity **active** path | **Blocked** until E1+ CC or E2 registry extract |
| Organization **active** at E0 | **Authorized** — layer separation per OOEP |

**Gap register (Legal Entity — non-blocking for Organization active):**

| Gap ID | Topic | Severity |
|--------|-------|----------|
| **ME-W1D-01** | Legal entity form (ООО / ИП / etc.) | **Deferred** |
| **ME-W1D-02** | INN / KPP / OGRN | **Deferred** |
| **ME-W1D-03** | Legal vs trade name mapping | **Deferred** |
| **ME-W1D-04** | CC folder absent | **Expected** — Category B |

---

## 5. Evidence basis

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| **EV-MAKITA-OP-01** | Steward intake inputs (2026-06-07) | **E0** | Display name, contact, phone, URLs, scope |
| **EV-MAKITA-OP-02** | Steward statement — both websites exist | **E0** | Website candidate corroboration |
| **EV-MAKITA-OP-03** | Intake enrichment — service context, boundaries | **E0** | i-SEO SEO scope; steward Direct scope |
| OOEP | [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) | governance | Category B authorization |

**Operational signals satisfied (≥2 required):**

1. Direct communication — steward ↔ **Артём** *(EV-MAKITA-OP-01)*  
2. Active work — SEO by i-SEO; Yandex Direct by steward *(EV-MAKITA-OP-01, EV-MAKITA-OP-03)*  
3. Known websites — makita-snab.ru; makita-land.ru *(EV-MAKITA-OP-01, EV-MAKITA-OP-02)*  
4. Known contact — **Артём** + phone *(EV-MAKITA-OP-01)*  
5. Confirmed business relationship — client of i-SEO *(EV-MAKITA-OP-01, EV-MAKITA-OP-03)*  

---

## 6. Service context *(informational — no REL-* mint)*

| Service | Provider / actor | Scope | Atlas edge |
|---------|----------------|-------|------------|
| **SEO** | i-SEO (ORG-0003 — attested vendor context only) | Both websites | **None** — deferred Wave 6+ |
| **Yandex Direct** | Steward (Polygon operational scope) | Paid search only | **None** — deferred Wave 6+ |

**Operational boundaries (steward scope):**

| In scope | Out of scope |
|----------|--------------|
| Yandex Direct | SEO delivery (i-SEO) |
| Direct communication with **Артём** | Contracts |
| | Accounting |
| | Document flow |

---

## 7. Duplicate review

| Review ID | Pair | Verdict | Basis |
|-----------|------|---------|-------|
| **W1D-D-01** | Makita vs ORG-0001 Полигон | **Distinct — Pass** | No shared identifiers |
| **W1D-D-02** | Makita vs ORG-0002 MetaCode | **Distinct — Pass** | No overlap |
| **W1D-D-03** | Makita vs ORG-0003 i-SEO | **Distinct — Pass** | Vendor ≠ client |
| **W1D-D-04** | Makita vs ORG-0004 Триумф | **Distinct — Pass** | No overlap |
| **W1D-D-05** | Makita vs ORG-0005 ЗПМ | **Distinct — Pass** | No overlap |
| **W1D-D-06** | Makita vs ORG-0006 SIBCAR | **Distinct — Pass** | No overlap |
| **W1D-D-07** | Makita vs ORCA pilot | **Class boundary — Pass** | EFV-02 |
| **W1D-D-08** | «Makita» tool brand homonym | **Open — low** | Legal identity **SAFE UNKNOWN** — expected for Category B |

**Explicit validations (mission-required):**

| Claim | Verdict | Evidence |
|-------|---------|----------|
| ORG-0001..0006 unchanged | **Confirmed** | No merge; no modification in this package |
| ZPM (ORG-0005) intact | **Confirmed** | W1D-D-05 |
| SIBCAR (ORG-0006) intact | **Confirmed** | W1D-D-06 |
| No merge operations | **Confirmed** | Duplicate review |
| No LE creation | **Confirmed** | §4 |
| No relationships | **Confirmed** | §6 |
| No projects | **Confirmed** | §9 |

---

## 8. Steward checklist (population)

| ID | Check | Result |
|----|-------|--------|
| W1D-S-01 | Category B classification (i-SEO client) | **Pass** |
| W1D-S-02 | OOEP operational signals ≥2 | **Pass** |
| W1D-S-03 | EFV rules applied — no project merge | **Pass** |
| W1D-S-04 | Legal entity fields **SAFE UNKNOWN** | **Pass** |
| W1D-S-05 | Duplicate batch W1D-D-01..08 | **Pass** |
| W1D-S-06 | ORG-0007 identifier slot | **Pass** — next after ORG-0006 |
| W1D-S-07 | No LE-* / PER-* / WEB-* / DOM-* / PRJ-* / REL-* mint | **Pass** |
| W1D-S-08 | No Foundation modification | **Pass** |
| W1D-S-09 | Prior intake-only hold superseded for Organization layer | **Pass** |

---

## 9. Candidate assets only — no mint

### 9.1 Website candidates

| Candidate | URL | web_id | Status |
|-----------|-----|--------|--------|
| makita-snab.ru | https://makita-snab.ru/ | **none** | Wave 4 candidate — EV-MAKITA-OP-01, EV-MAKITA-OP-02 |
| makita-land.ru | https://makita-land.ru/ | **none** | Wave 4 candidate — EV-MAKITA-OP-01, EV-MAKITA-OP-02 |

**Do not mint WEB entities.**

### 9.2 Domain candidates

| Candidate | FQDN | dom_id | Status |
|-----------|------|--------|--------|
| makita-snab.ru | makita-snab.ru | **none** | Wave 5 candidate |
| makita-land.ru | makita-land.ru | **none** | Wave 5 candidate |

**Do not mint DOM entities.**

### 9.3 Deferred entity classes

| Class | Status |
|-------|--------|
| LE-* | **Not created** — SAFE UNKNOWN until E1+ |
| PER-* | **Not created** — contact **Артём** is operational signal only |
| PRJ-* | **Not created** — future Wave 3 |
| REL-* | **Not created** — future Wave 6+ |

---

## 10. Attestation readiness

| Dimension | Assessment |
|-----------|------------|
| Operational evidence | **Complete** — EV-MAKITA-OP-01..03 |
| OOEP gates | **Pass** |
| Duplicate review | **Pass** |
| Organization **active** | **Ready** — see attestation package |
| Legal Entity | **Deferred** — SAFE UNKNOWN |
| Wave 2 Person | **Not in scope** |
| Wave 3 Project | **Deferred** |
| Wave 4 / 5 Website / Domain | **Deferred** — candidates only |

See [ATLAS-WAVE1D-MAKITA-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-ATTESTATION-v1.md).

---

## 11. Package lineage

```text
Wave 1 (ORG-0001..0004) ──COMPLETE──► Wave 1 Attestation ──COMPLETE
        │
        ▼
Wave 1B ЗПМ (ORG-0005 active) ──► Wave 1C SIBCAR (ORG-0006 active)
        │
        ▼
Makita Intake (INTAKE ONLY) ──► superseded for Organization layer
        │
        ▼
Wave 1D Makita Organization Population (THIS PACKAGE) ──► ORG-0007 active
        │
        ▼
Future: CC arrival ──► Legal Entity wave (LE-* TBD)
Future: Wave 2 Person / Wave 3 Project / Wave 4–6 assets & edges
```

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1D-MAKITA-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-REGISTER-v1.md) | Canonical register row |
| [ATLAS-WAVE1D-MAKITA-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-ATTESTATION-v1.md) | Attestation sequence and verdict |
| [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) | Category B policy |
| [ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md](ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md) | Prior operational evidence consolidation |

---

*ATLAS Wave 1D Makita Organization Population v1 — documentation only.*
