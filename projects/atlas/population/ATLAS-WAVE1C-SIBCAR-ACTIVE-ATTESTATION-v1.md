# ATLAS Wave 1C SIBCAR Active Attestation v1

**Status:** **attested** — first official Organization active attestation for Wave 1C SIBCAR tranche.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) · [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md) · [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md)  
**Is not:** runtime, API, database export, Person population, Project / Website / Domain entities, Wave 2 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1 Attestation: **COMPLETE**
- Wave 1C SIBCAR Population (AT-W1C-00): **COMPLETE**
- Population verdict (prior): **PARTIALLY READY** — resolved by this act
- Counterparty Card SIBCAR: **present** at `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\`

---

# REPORT — ATLAS Wave 1C SIBCAR Active Attestation

**Attestation date:** 2026-06-06  
**Tranche:** **AT-W1C-01** — Active attest  
**Promotion:** ORG-0006, LE-0005 — **proposed** → **active**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** класса **Organization** и связанного **Legal Entity** для Wave 1C tranche **SIBCAR**: ORG-0006 и LE-0005 переведены из approved population draft (**proposed**) в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Organization ORG-0006 → **active** | Person entities |
| Legal entity LE-0005 → **active** | Person ↔ Organization edges (Wave 2C-SIBCAR) |
| CC-backed alias acceptance → **active** | Project / Website / Domain entities |
| Evidence tier **E1** assignment | CLIENT_OF ORG-0006 → ORG-0001 (Wave 6+) |
| Duplicate review sign-off | BZPM ↔ SIBCAR relationship edges |
| ME-W1C-01 resolution | Foundation amendments |
| Wave 2 SIBCAR **queue note only** | Runtime / API / database |

---

## 2. Pre-attestation verification

### 2.1 Legal entity consistency

Cross-check: population register ↔ EV-W1C-CC-01 ↔ attestation proposal.

| Field | LE-0005 (register) | EV-W1C-CC-01 | Match |
|-------|-------------------|--------------|-------|
| **legal_entity_name** | Общество с ограниченной ответственностью «СибКар» | §4 | **Match** |
| **entity_type** | ООО | §2–§4 | **Match** |
| **inn** | 5405512542 | §18 | **Match** |
| **kpp** | 540501001 | §18 | **Match** |
| **ogrn_ogrnip** | 1265400004220 | §20 | **Match** |
| **legal_address** | 630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11 | §12 | **Match** |
| **actual_address** | 630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11 | §14 | **Match** |
| **document_signatory** | Карандашов Максим Петрович | §22 | **Match** |
| **org_binding** | ORG-0006 | Population §4 | **Match** |

**Verdict:** **Pass** — legal entity layer consistent; no field conflicts; critical identifiers complete on E1 CC.

### 2.2 Identity consistency

| Check | Result | Basis |
|-------|--------|-------|
| **canonical_name** SIBCAR | **Pass** | EV-W1C-CC-01 §8, §10 — Latin stem «SibCar»; operator folder `sibcar\` |
| **legal display** ООО «СибКар» via LE-0005 | **Pass** | CC §2, §6 — not duplicate org |
| **Alias register** (4 rows) | **Pass** | All CC-backed per EFV-01 |
| **«Автосалон СИБКАР»** excluded | **Pass** | Site title absent from CC — not attested alias |
| **SIBCAR ≠ BZPM** | **Pass** | COR-W1B-05 fulfilled; distinct INN/OGRN |
| **SIBCAR ≠ Triumph / operator orgs** | **Pass** | W1C-D-02, W1C-D-03 |
| **ORG-0006 ↔ LE-0005 binding** | **Pass** | Single legal subject, single org anchor |

**Verdict:** **Pass** — identity layer consistent; canonical name and aliases align with evidence.

### 2.3 Duplicate review status

| review_id | Pair | Verdict | Blocking |
|-----------|------|---------|----------|
| **W1C-D-01** | SIBCAR vs BZPM (ORG-0006 vs ORG-0005) | **Distinct — Pass** | No |
| **W1C-D-02** | SIBCAR vs Triumph (ORG-0006 vs ORG-0004) | **Distinct — Pass** | No |
| **W1C-D-03** | SIBCAR vs operator orgs | **Distinct — Pass** | No |
| **W1C-D-04** | SIBCAR vs SITE-001 | **Class boundary — Pass** | No |
| **W1C-D-05** | «Автосалон СИБКАР» site title vs CC legal name | **Open — low** | No |
| **W1C-D-06** | D1 unresolved duplicate | **None** | No |

**INN 5405512542 cross-registry:** no collision with Wave 1 dataset ORG-0001..0004 or ORG-0005 BZPM (INN 2221237587).

**Verdict:** **Pass** — duplicate review complete; no blocking duplicates; W1C-D-05 deferred to future Website intake (non-blocking for Organization **active**).

### 2.4 Evidence sufficiency

| Gate ID | Rule | Status |
|---------|------|--------|
| **W1C-EG-01** | W1-C minimum E1 at **active** | **Pass** — EV-W1C-CC-01 |
| **W1C-EG-02** | CC preferred path when obtainable | **Pass** — CC placed |
| **W1C-EG-03** | No contract/invoice primary (OAR-BAN-01) | **Pass** |
| **W1C-EG-04** | No hostname-only org (OAR-BAN-03) | **Pass** |
| **W1C-EG-05** | Duplicate batch before **active** | **Pass** — W1C-D-01..06 |
| **W1C-EG-06** | Human attest mandatory (OAR-HUM-01) | **Pass** — this act |
| **W1C-EG-07** | LE critical fields reviewed before org **active** | **Pass** |

**Primary evidence:** EV-W1C-CC-01 — `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` — E1 «Карточка предприятия» (74 779 bytes, 2026-04-04).

**Verdict:** **Pass** — E1 CC satisfies W1-C Organization attestation minimum; no evidence fabrication; ME-W1C-01 resolved by steward act.

---

## 3. Attestation tranche executed

### 3.1 AT-W1C-01 — Active attest

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Confirm CC path and extraction accuracy | Steward | EV-W1C-CC-01 | **Done** |
| 2 | Duplicate review sign-off on INN/OGRN | Steward | W1C-D-01..06 | **Done** |
| 3 | Attest LE-0005 **active** | Steward | LegalEntities discipline | **Done** |
| 4 | Attest Organization ORG-0006 **active** | Steward (delegated) | W1-EXEC-04 analog | **Done** |
| 5 | Promote CC-backed aliases **active** | Steward | Register §4 | **Done** |

**Not executed in this tranche (by scope):**

| Step | Action | Reason |
|------|--------|--------|
| Queue Wave 2 Person candidates | Deferred | Wave 2 starts later — no Person entities created |

---

## 4. Attested entity records

### 4.1 LE-0005 — ООО «СибКар»

| Field | Value |
|-------|-------|
| **legal_entity_id** | LE-0005 |
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
| **org_binding** | ORG-0006 |
| **attestation_basis** | E1 EV-W1C-CC-01; duplicate review W1C-D-01..06 **Pass**; legal entity consistency check §2.1 |
| **evidence_tier** | **E1** |
| **lifecycle_state (prior)** | **proposed** |
| **lifecycle_state (attested)** | **active** |
| **notes** | LE-0004 remains BZPM binding; not in Wave 1 dataset xlsx |

### 4.2 ORG-0006 — SIBCAR

| Field | Value |
|-------|-------|
| **org_id** | ORG-0006 |
| **canonical_name** | SIBCAR |
| **wave_tier** | W1-C |
| **business_role** | **CLIENT** |
| **legal_entity_id** | LE-0005 |
| **legal_entity_name** | ООО «СибКар» |
| **inn** | 5405512542 |
| **ogrn_ogrnip** | 1265400004220 |
| **primary_website** | **SAFE UNKNOWN** *(prod)* |
| **primary_domain** | **SAFE UNKNOWN** *(prod)* |
| **primary_contact_person_id** | **SAFE UNKNOWN** — Wave 2C-SIBCAR |
| **attestation_basis** | E1 EV-W1C-CC-01; identity consistency §2.2; COR-W1B-05 split honored |
| **evidence_tier** | **E1** |
| **lifecycle_state (prior)** | **proposed** |
| **lifecycle_state (attested)** | **active** |
| **notes** | Third W1-B-class client; distinct from ORG-0005 BZPM; OCPilot SITE-001 is engagement context only — not org identity proof |

### 4.3 Attested aliases (proposed → active)

| org_id | alias | alias_type | evidence_ref | attestation_state (prior) | attestation_state (attested) |
|--------|-------|------------|--------------|---------------------------|------------------------------|
| ORG-0006 | SIBCAR | Latin trade / operator slug | EV-W1C-CC-01 §8, §10 | **proposed** | **active** |
| ORG-0006 | СибКар | RU short legal / trade | EV-W1C-CC-01 §2, §6 | **proposed** | **active** |
| ORG-0006 | SibCar | EN short legal | EV-W1C-CC-01 §8, §10 | **proposed** | **active** |
| ORG-0006 | ООО «СибКар» | RU legal short name | EV-W1C-CC-01 §2 | **proposed** | **active** |

---

## 5. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| Person entities (PER-*) | **Not created** — Wave 2C-SIBCAR deferred |
| Карандашов Максим Петрович → PER-* | **Queue note only** — CC §22 signatory; Person wave later |
| Person ↔ Organization edges | **Deferred** — Wave 2C-SIBCAR |
| Project entities (PRJ-*) | **Not created** — Wave 3+ |
| Website entities (WEB-*) | **Not created** — Wave 4 |
| Domain entities (DOM-*) | **Not created** — Wave 5 |
| REL-* CLIENT_OF ORG-0006 → ORG-0001 | **Deferred** — Wave 6+ |
| REL-* ORG-0005 ↔ ORG-0006 | **SAFE UNKNOWN** — no CC bridge |
| ORG-0005 BZPM attestation | **Separate tranche** — remains **proposed** |

---

## 6. Residual gaps (non-blocking)

| ID | Topic | Severity | Mitigation |
|----|-------|----------|------------|
| **ME-W1C-02** | Production public URL | Low | Wave 4 Website population |
| **ME-W1C-03** | EDO / Diadoc participant id | Low | CC update |
| **ME-W1C-04** | Phone on CC | Low | CC update or Wave 2 |
| **ME-W1C-05** | Corporate domain / website on CC | Low | Wave 4 / 5 |
| **W1C-D-05** | Site title «Автосалон СИБКАР» vs CC name | Low | Website intake disambiguation |

**Blocking gaps remaining:** **None**

---

## 7. Foundation consistency check

| Check | Result |
|-------|--------|
| No new entity types | **Pass** |
| No Foundation modification | **Pass** |
| No Wave 1 record modification | **Pass** |
| W1-C acquisition rules followed | **Pass** |
| SAFE UNKNOWN — no invented identifiers | **Pass** |
| EFV-01 alias discipline | **Pass** |
| SIBCAR ≠ BZPM split honored (COR-W1B-05) | **Pass** |
| ATLAS-ATTESTATION-MODEL contract followed | **Pass** |
| Documentation only | **Pass** |

---

## 8. Attestation verdict

```text
ACTIVE ORGANIZATION
```

**Conditions met:**

1. ORG-0006 **active** — canonical Organization attested under E1 CC discipline.
2. LE-0005 **active** — legal entity attested and bound to ORG-0006.
3. CC-backed aliases (4 rows) promoted to **active**.
4. Legal entity consistency, identity consistency, duplicate review, and evidence sufficiency — **all Pass**.
5. ME-W1C-01 (steward active attestation act) — **resolved**.

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **PARTIALLY READY** | [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md) §10 | **Superseded** for Organization lifecycle — ORG-0006 now **active** |

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **PARTIALLY READY** | AT-W1C-01 complete; no blockers remain |
| **NOT READY** | All verification gates pass |
| **NO EVIDENCE FOUND** | EV-W1C-CC-01 present and sufficient |

**Downstream note:** Wave 2C-SIBCAR Person Population may proceed in a **separate future pass** — not executed in this package.

---

## 9. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ▼
Wave 1B BZPM (ORG-0005 proposed) ──► Identity correction (SIBCAR split)
        │
        ▼
Wave 1C SIBCAR Population (AT-W1C-00) ──► proposed ORG-0006
        │
        ▼
Wave 1C SIBCAR Active Attestation (THIS PACKAGE — AT-W1C-01) ──► ORG-0006 active
        │
        ▼
Wave 2C-SIBCAR Person Population (FUTURE — separate pass)
```

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) | Population register (prior **proposed** state) |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md) | Attestation sequence plan |
| [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | Evidence verification |
| [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) | Prior split — COR-W1B-05 |

---

*ATLAS Wave 1C SIBCAR Active Attestation v1 — documentation only.*
