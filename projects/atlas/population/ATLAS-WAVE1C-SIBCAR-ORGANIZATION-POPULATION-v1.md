# ATLAS Wave 1C SIBCAR Organization Population v1

**Status:** **documented** — Wave 1C canonical Organization population plan for SIBCAR (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) · [ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](../foundation/ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) · [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Companion:** [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) · [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md) · [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md)  
**Is not:** runtime, API, automation, database schema, attested registry export.

**Wave 1 prerequisite:** Organizations Wave 1 (ORG-0001..0004) — status **COMPLETE** (operator, 2026-06-06).

**Wave 1C intent:**

Perform **evidence-first intake** for **SIBCAR** as a **distinct** W1-B-class client Organization — fulfilling [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) **COR-W1B-05** after Counterparty Card placement in `sibcar\` external storage.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Organization** для Wave 1C tranche **SIBCAR**: identity, legal entity linkage, CC-backed aliases, website/domain candidates, evidence, duplicate review, attestation readiness, и downstream candidates (Person, Project, Website, Domain).

**Normative scope Wave 1C:**

```text
Organization entity intake + attestation plan (single org: SIBCAR)
Wave 2C-SIBCAR (future): Person ↔ Organization — только после active ORG-0006
Wave 3+ (future): Project / Website / Domain — только после org anchor
Wave 6+ (future): CLIENT_OF ORG-0006 → ORG-0001 — только после org active + commercial review
```

**Binding evidence context:**

- **EV-W1C-CC-01** — `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` — **E1** «Карточка предприятия».
- **ORG-0006** — proposed canonical Organization id (next after ORG-0005 BZPM).
- **LE-0005** — proposed Legal Entity id (next after LE-0004 BZPM).
- **No project-context inference** — OCPilot SITE-001 cited only for Website **candidates** (EFV-02).

---

## 2. Population roster (canonical)

Источник: **EV-W1C-CC-01** (primary); duplicate review vs attested Wave 1 orgs and ORG-0005 BZPM.  
**Не** в [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) — Wave 1C — post-dataset expansion tranche.

### 2.1 Summary table

| org_id | canonical_name | wave_tier | business_role | legal_entity_id | lifecycle (target) | evidence_tier (population) | attestation readiness |
|--------|----------------|-----------|---------------|-----------------|-------------------|---------------------------|----------------------|
| ORG-0006 | SIBCAR | **W1-C** | **CLIENT** | **LE-0005** *(proposed)* | **proposed** | **E1** *(CC)* | **partially ready** |

**Wave tier:** W1-C — mirrors W1-B client discipline; third-party organization with E1 CC ([ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) §2.1 analog).

---

## 3. Organization identity analysis

### 3.1 ORG-0006 — SIBCAR

| Field | Value |
|-------|-------|
| **org_id** | ORG-0006 |
| **canonical_name** | SIBCAR |
| **lifecycle_state (population)** | **proposed** |
| **wave_tier** | W1-C |
| **business_role** | **CLIENT** — commercial counterparty (auto trade per CC OKVED) |
| **legal_entity_id** | **LE-0005** *(proposed — see §4)* |
| **primary_contact_person_id** | **SAFE UNKNOWN** — Person not yet populated |
| **primary_website (display candidate)** | **SAFE UNKNOWN** (production) |
| **primary_domain (display candidate)** | **SAFE UNKNOWN** (production) |
| **edo_enabled** | **SAFE UNKNOWN** |
| **notes** | Distinct from ORG-0005 BZPM per CC identifiers; CC present |

### 3.2 Identity disambiguation (evidence-only)

| Signal | Resolution | Evidence |
|--------|------------|----------|
| **SIBCAR** vs **BZPM (ORG-0005)** | **Distinct organizations** | INN 5405512542 ≠ 2221237587; legal names unrelated; separate CC folders |
| **SIBCAR** vs **Triumph (ORG-0004)** | **Distinct clients** | No shared identifiers in EV-W1C-CC-01 |
| **SIBCAR** vs **Polygon / MetaCode / i-SEO** | **Distinct** | Operator orgs ORG-0001..0003 — no CC overlap |
| **SIBCAR** vs **SITE-001** | **Different entity classes** | SITE-001 = OCPilot site_id / future Website; ORG-0006 = CC-backed legal counterparty |
| **«Автосалон СИБКАР»** site title | **Not org alias** | Absent from CC — EFV-01; OKVED 45.11 supports industry context only |

### 3.3 Proposed aliases (CC-backed)

Per [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) — aliases attach to **ORG-0006** only when cited on EV-W1C-CC-01:

| Alias | evidence_ref |
|-------|--------------|
| SIBCAR | EV-W1C-CC-01 §8, §10 |
| СибКар | EV-W1C-CC-01 §2, §6 |
| SibCar | EV-W1C-CC-01 §8, §10 |
| ООО «СибКар» | EV-W1C-CC-01 §2 |

---

## 4. Legal entity analysis

### 4.1 Proposed LE-0005

| Field | Value |
|-------|-------|
| **legal_entity_id** | LE-0005 *(proposed — not attested)* |
| **legal_entity_name** | Общество с ограниченной ответственностью «СибКар» |
| **entity_type** | ООО |
| **inn** | 5405512542 |
| **kpp** | 540501001 |
| **ogrn_ogrnip** | 1265400004220 |
| **legal_address** | 630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11 |
| **actual_address** | 630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11 |
| **document_signatory** | Карандашов Максим Петрович |
| **tax_system** | УСН Доходы 6% |
| **okved_primary** | 45.11 — торговля легковыми и малыми грузовыми автомобилями |
| **lifecycle** | **proposed** |
| **notes** | Populated from EV-W1C-CC-01; LE-0004 remains BZPM binding |

### 4.2 Legal entity readiness

| Check | Result |
|-------|--------|
| CC provides legal name + INN/OGRN | **Pass** — EV-W1C-CC-01 |
| Registry extract alternate (E2) | **Not required** — CC sufficient for proposed |
| Operator E0-only path for W1-C | **Prohibited** — W1-C requires E1+ |
| LE-0005 may attest **active** without org CC | **No** — org and LE attest together at AT-W1C-01 |

**Gap register:**

| Gap ID | Topic | Severity |
|--------|-------|----------|
| **ME-W1C-01** | Steward **active** attestation not executed | **Blocking** for **active** / Wave 2 |
| **ME-W1C-02** | Production public URL unknown | Low |
| **ME-W1C-03** | EDO participant id unknown | Low |
| **ME-W1C-04** | Phone not on CC | Low |
| **ME-W1C-05** | Corporate website / domain not on CC | Low |

---

## 5. Evidence basis

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| **EV-W1C-CC-01** | `sibcar\Реквизиты.docx` | **E1** | Primary — legal identity, requisites, signatory |
| EV-W1C-02 | [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) | E1 operational | Website candidate context — **not** org identity |
| EV-W1C-03 | [project-access-brief.md](../../../projects/ocpilot/sites/site-001/project-access-brief.md) | E1 operational | TEST URL — Website candidate |
| EV-W1B-CC-01 | `bzpm\Реквизиты.docx` | E1 | Compare — proves BZPM distinct subject |

---

## 6. Duplicate review

| Review ID | Pair | Verdict | Basis |
|-----------|------|---------|-------|
| **W1C-D-01** | SIBCAR vs BZPM | **Distinct — Pass** | INN/OGRN/legal name mismatch across CCs |
| **W1C-D-02** | SIBCAR vs Triumph | **Distinct — Pass** | No identifier collision |
| **W1C-D-03** | SIBCAR vs Polygon / MetaCode / i-SEO | **Distinct — Pass** | Operator org separation |
| **W1C-D-04** | SIBCAR vs SITE-001 | **Class boundary — Pass** | Website ≠ Organization |
| **W1C-D-05** | Site title vs CC legal name | **Open — low** | Industry OKVED aligns; title not CC alias |
| **W1C-D-06** | D1 duplicate | **None** | Single CC; unique INN |

**Explicit validations (mission-required):**

| Claim | Verdict | Evidence |
|-------|---------|----------|
| SIBCAR ≠ BZPM | **Confirmed** | EV-W1C-CC-01 vs EV-W1B-CC-01 — different INN, OGRN, legal names, regions |
| SIBCAR ≠ Triumph | **Confirmed** | No Triumph identifiers in EV-W1C-CC-01 |
| SIBCAR ≠ Polygon | **Confirmed** | ORG-0001 separate; no shared CC identifiers |
| SIBCAR ≠ MetaCode | **Confirmed** | ORG-0002 separate; no shared CC identifiers |
| SIBCAR ≠ i-SEO | **Confirmed** | ORG-0003 separate; no shared CC identifiers |

---

## 7. Steward checklist (population)

| ID | Check | Result |
|----|-------|--------|
| W1C-S-01 | CC folder inspected | **Pass** |
| W1C-S-02 | Evidence inventory recorded | **Pass** |
| W1C-S-03 | EFV rules applied — no project merge | **Pass** |
| W1C-S-04 | Legal entity critical fields from CC | **Pass** |
| W1C-S-05 | Duplicate batch W1C-D-01..06 | **Pass** |
| W1C-S-06 | ORG-0006 / LE-0005 identifier slots | **Pass** — next after ORG-0005 / LE-0004 |
| W1C-S-07 | SAFE UNKNOWN for absent CC fields | **Pass** |
| W1C-S-08 | No Foundation modification | **Pass** |

---

## 8. Candidate Persons

| Candidate | Role (from CC) | evidence_ref | Status |
|-----------|----------------|--------------|--------|
| Карандашов Максим Петрович | Руководитель; also Главный бухгалтер | EV-W1C-CC-01 §22, §24 | **Wave 2 candidate** — PER-* TBD |
| Primary operational contact | **SAFE UNKNOWN** | — | Pending CC expansion |
| Phone contacts | **SAFE UNKNOWN** | — | Not on CC |

**Wave 2C-SIBCAR Person Population** — **blocked** until ORG-0006 **active**.

---

## 9. Candidate Projects

| Candidate | Client org | Executor (informational) | Status |
|-----------|------------|--------------------------|--------|
| PRJ-* TBD | ORG-0006 SIBCAR | ORG-0001 Полигон *(future)* | **Future Wave 3** — requires commercial evidence; OCPilot SITE-001 context **not** sufficient alone |
| OCPilot Run 5+ audit container | ORG-0006 | — | **Future Wave 3** — project context only |

---

## 10. Candidate Websites

| Candidate | URL | Status |
|-----------|-----|--------|
| Production site | **SAFE UNKNOWN** | Wave 4 — not on CC |
| TEST OpenCart site | `https://sibcar.new-site.space/` | Wave 4 candidate — EV-W1C-03; TEST environment; **not** org identity proof |

---

## 11. Candidate Domains

| Candidate | FQDN | Status |
|-----------|------|--------|
| Production apex | **SAFE UNKNOWN** | Wave 5 — registrar E1 required |
| TEST subdomain | `sibcar.new-site.space` | Wave 5 candidate — not registrant proof |
| Email domain | `mail.ru` | Consumer mail — **not** corporate domain candidate |

---

## 12. Attestation readiness

| Dimension | Assessment |
|-----------|------------|
| CC present | **Yes** — EV-W1C-CC-01 |
| Legal entity fields | **Complete** for proposed tier |
| Duplicate review | **Pass** |
| **proposed** population | **Complete** |
| **active** attestation | **Pending** steward AT-W1C-01 |
| Wave 2 Person | **Blocked** |

See [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md).

---

## 13. Package lineage

```text
Wave 1 (ORG-0001..0004) ──COMPLETE──► Wave 1 Attestation ──COMPLETE
        │
        ▼
Wave 1B BZPM (ORG-0005) ──► Identity correction (SIBCAR split)
        │
        ▼
Wave 1C SIBCAR Organization Population (THIS PACKAGE) ──► proposed ORG-0006
        │
        ▼
Wave 1C SIBCAR Organization Attestation (NEXT) ──► AT-W1C-01 pending
        │
        ▼
Wave 2 SIBCAR Person Population (FUTURE) ──► after ORG-0006 active
```

---

## 14. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) | Canonical register row |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md) | Attestation sequence and verdict |
| [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | Evidence verification report |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External CC path |
| [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) | Prior split — COR-W1B-05 fulfilled |

---

# REPORT — ATLAS Wave 1C SIBCAR Organization Population

**Date:** 2026-06-06  
**Scope:** Documentation-only evidence-first Organization intake for SIBCAR using existing model.

---

## 1. Evidence inventory

| # | File | Path | Format | Size | Role |
|---|------|------|--------|------|------|
| 1 | `Реквизиты.docx` | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | DOCX | 74 779 bytes | E1 CC «Карточка предприятия» |

**Evidence ref:** `EV-W1C-CC-01`  
**Folder contents:** one file; no secondary corroboration in-folder.

---

## 2. Extracted organization facts

| Field | Value | Source |
|-------|-------|--------|
| Legal entity form | ООО | EV-W1C-CC-01 §2–§4 |
| Legal name (full) | Общество с ограниченной ответственностью «СибКар» | §4 |
| Legal name (short) | ООО «СибКар» | §2 |
| INN | 5405512542 | §18 |
| KPP | 540501001 | §18 |
| OGRN | 1265400004220 | §20 |
| Legal / actual address | 630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11 | §12, §14 |
| EDO | **SAFE UNKNOWN** | — |
| Websites | **SAFE UNKNOWN** | — |
| Domains | **SAFE UNKNOWN** (corporate) | — |
| Email | info_sibcar@mail.ru | §16 |
| Signatory | Карандашов Максим Петрович (руководитель) | §22 |
| Chief accountant | Карандашов Максим Петрович | §24 |
| OKVED | 45.11 — auto trade | §36–§37 |
| Tax system | УСН Доходы 6% | §39 |

---

## 3. Legal entity analysis

| Item | Finding |
|------|---------|
| Proposed **LE-0005** | Bound to ORG-0006 from EV-W1C-CC-01 |
| Entity type | **ООО** |
| Legal name | Общество с ограниченной ответственностью «СибКар» |
| INN / KPP / OGRN | 5405512542 / 540501001 / 1265400004220 |
| Signatory | Карандашов Максим Петрович |
| Lifecycle | **proposed** — attestation pending |

**Conclusion:** Legal entity layer **supported at proposed tier** from E1 CC. **Active** LE requires steward attestation (AT-W1C-01).

---

## 4. Identity analysis

| Item | Finding |
|------|---------|
| **Canonical organization name** | **SIBCAR** (ORG-0006) — CC Latin stem + operator folder |
| **Aliases (CC-backed)** | СибКар; SibCar; ООО «СибКар» |
| **Rejected alias** | «Автосалон СИБКАР» — site title only; absent from CC (EFV-01) |
| **Relationship to BZPM** | **Distinct** — fulfills COR-W1B-05 separate intake |
| **Relationship ORG-0005 ↔ ORG-0006** | **SAFE UNKNOWN** — no CC bridge |

---

## 5. Duplicate review

| Result | Detail |
|--------|--------|
| **Pass** | SIBCAR distinct from BZPM — INN 5405512542 ≠ 2221237587 |
| **Pass** | Distinct from ORG-0004 Triumph |
| **Pass** | Distinct from ORG-0001 Polygon, ORG-0002 MetaCode, ORG-0003 i-SEO |
| **Pass** | SITE-001 remains site id — not second Organization |
| **Open (low)** | Site title «Автосалон СИБКАР» vs CC «СибКар» — resolve at Website intake |

No D1 blocker for **proposed** population.

---

## 6. Candidate Persons

| Candidate | Status |
|-----------|--------|
| Карандашов Максим Петрович | **Wave 2 candidate** — руководитель + главный бухгалтер on CC |
| Primary contact (operational) | **SAFE UNKNOWN** — no phone on CC |
| PER-* assignment | **TBD** at Wave 2C-SIBCAR |

Wave 2 SIBCAR Person Population — **not ready** (org not **active**).

---

## 7. Candidate Projects

| Candidate | Status |
|-----------|--------|
| SITE-001 / OpenCart support engagement | **Future Wave 3** — ORG-0006 → COMMISSIONED_BY candidate; commercial evidence required |
| OCPilot audit runs | **Future Wave 3** — project container only |

---

## 8. Candidate Websites

| Candidate | URL | Status |
|-----------|-----|--------|
| Production site | **SAFE UNKNOWN** | Wave 4 |
| TEST dealership site | `https://sibcar.new-site.space/` | Wave 4 candidate — OCPilot TEST only |

---

## 9. Candidate Domains

| Candidate | FQDN | Status |
|-----------|------|--------|
| Production domain | **SAFE UNKNOWN** | Wave 5 |
| TEST subdomain | `sibcar.new-site.space` | Wave 5 candidate — not registrant proof |

---

## 10. Attestation readiness

| Dimension | Assessment |
|-----------|------------|
| Organization model fit | **Validated** — SIBCAR populates as W1-C **proposed** ORG-0006 |
| CC intake | **Complete** — EV-W1C-CC-01 |
| Legal entity from CC | **Complete** for proposed tier |
| Duplicate review | **Clear** |
| Attestation (**active**) | **Pending** — steward AT-W1C-01 |
| Wave 2 SIBCAR Person Population | **Blocked** — org not **active** |

### Verdict

```text
PARTIALLY READY
```

**Meaning:**

1. Wave 1C **population** objective met — SIBCAR fits existing Organization model as **proposed** ORG-0006 with CC-backed LE-0005.
2. **SIBCAR ≠ BZPM** and **SIBCAR ≠ Triumph / Polygon / MetaCode / i-SEO** — confirmed by CC identifiers; no merge assumptions.
3. **Active** attestation and Wave 2 SIBCAR Person Population remain **blocked** until steward executes AT-W1C-01 (ME-W1C-01).

**Not selected:**

| Verdict | Why not |
|---------|---------|
| **NO EVIDENCE FOUND** | CC present with full legal requisites |
| **READY FOR WAVE 2 SIBCAR PERSON POPULATION** | ORG-0006 not **active** |

---

**Changed files:** `projects/atlas/population/ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md`, `ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md`, `ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md`, `ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md`  
**Git:** no commit, no push  
**UNKNOWN:** production URL; corporate domain; EDO participant id; phone; exact signatory должность string; commercial relationship ORG-0005 ↔ ORG-0006  
**SECURITY RISK:** None — no credentials recorded; bank account numbers cited from CC as structural facts only (standard CC intake)

---

*ATLAS Wave 1C SIBCAR Organization Population v1 — documentation only.*
