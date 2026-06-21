# ATLAS Wave 1C SIBCAR Organization Register v1

**Status:** **documented** — canonical Organization roster for Wave 1C SIBCAR tranche (**active**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06 · **sync:** 2026-06-07 (audit findings remediation — FINDING-INT-01)  
**Parent:** [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) · [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md)  
**Is not:** LegalEntities runtime export, runtime registry, database table.

---

## 1. Purpose

Канонический **реестр Organization population** Wave 1C — tranche **SIBCAR**. Одна строка — одна approved Organization record для attestation.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Wave tier W1-C | **1** |
| Lifecycle **active** | **1** (ORG-0006) |
| Legal entity **active** | **1** (LE-0005) |
| Attestation | **Complete** — AT-W1C-01 |

---

## 2. Population roster — full table

| org_id | canonical_name | wave_tier | business_role | legal_entity_id | legal_entity_name | inn | ogrn_ogrnip | aliases | primary_website | primary_domain | evidence_tier | lifecycle_state | attestation_readiness | notes |
|--------|----------------|-----------|---------------|-----------------|-------------------|-----|-------------|---------|-----------------|----------------|---------------|-----------------|----------------------|-------|
| ORG-0006 | SIBCAR | **W1-C** | **CLIENT** | **LE-0005** | ООО «СибКар» | 5405512542 | 1265400004220 | SIBCAR; СибКар; SibCar; ООО «СибКар» | **SAFE UNKNOWN** *(prod)* | **SAFE UNKNOWN** *(prod)* | **E1** *(CC)* | **active** | **complete** | AT-W1C-01; third W1-B-class client; distinct from ORG-0005 ЗПМ |

---

## 3. Legal entity index

| legal_entity_id | legal_entity_name | entity_type | inn | kpp | ogrn_ogrnip | lifecycle | org_binding | attestation_readiness |
|-----------------|-------------------|-------------|-----|-----|-------------|-----------|-------------|----------------------|
| LE-0005 | Общество с ограниченной ответственностью «СибКар» | ООО | 5405512542 | 540501001 | 1265400004220 | **active** | ORG-0006 | **complete** — AT-W1C-01 |

**Note:** LE-0001..0003 attested in Wave 1 dataset. LE-0004 reserved for BZPM. LE-0005 reserved for SIBCAR — not in [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx).

---

## 4. Alias register (CC-backed — attested)

| org_id | alias | alias_type | evidence_ref | attestation_state |
|--------|-------|------------|--------------|-------------------|
| ORG-0006 | SIBCAR | Latin trade / operator slug | EV-W1C-CC-01 §8, §10 | **active** |
| ORG-0006 | СибКар | RU short legal / trade | EV-W1C-CC-01 §2, §6 | **active** |
| ORG-0006 | SibCar | EN short legal | EV-W1C-CC-01 §8, §10 | **active** |
| ORG-0006 | ООО «СибКар» | RU legal short name | EV-W1C-CC-01 §2 | **active** |

**Excluded (EFV-01):** «Автосалон СИБКАР» — site title in OCPilot only; **not** on CC — see cross-reference §5.

---

## 5. Cross-reference index (informational — not Wave 1C edges)

| Related artifact | Entity class | Relationship to ORG-0006 | Wave |
|------------------|--------------|----------------------------|------|
| SITE-001 | OCPilot site_id | Managed OpenCart engagement context — **not** org identity proof | OCPilot / future Project |
| `sibcar.new-site.space` | Website hostname candidate | Future WEB-* (TEST) | Wave 4 |
| ORG-0005 BZPM | Organization | **Distinct** legal subject — COR-W1B-05 fulfilled | Wave 1B |
| ORG-0004 Триумф | Organization | Separate W1-B client — no merge | Wave 1 |
| ORG-0001 Полигон | Organization | Future **CLIENT_OF** vendor (ORG-0006 → ORG-0001) | Wave 6+ |

---

## 6. Evidence index (population references)

| Ref | Artifact | Role |
|-----|----------|------|
| EV-W1C-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | **Primary** — E1 CC «Карточка предприятия» |
| EV-W1C-02 | [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) | Website candidate context only — **not** org alias proof |
| EV-W1C-03 | [project-access-brief.md](../../../projects/ocpilot/sites/site-001/project-access-brief.md) | TEST URL context |
| EV-W1B-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx` | BZPM compare — proves distinct subject |

---

## 7. Duplicate review register

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| W1C-D-01 | SIBCAR vs BZPM | **Distinct** | No |
| W1C-D-02 | SIBCAR vs ORG-0004 Triumph | **Distinct** | No |
| W1C-D-03 | SIBCAR vs operator orgs | **Distinct** | No |
| W1C-D-04 | SITE-001 class boundary | **Pass** | No |
| W1C-D-05 | Site title «Автосалон СИБКАР» vs CC name | **Open — low** | No (proposed) |
| W1C-D-06 | D1 unresolved | **None** | No |

---

## 8. Gap register

| gap_id | topic | severity | mitigation |
|--------|-------|----------|------------|
| ME-W1C-01 | Steward **active** attestation not executed | **Resolved** | AT-W1C-01 — [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) |
| ME-W1C-02 | Production public URL unknown | Low | Wave 4 Website population |
| ME-W1C-03 | EDO / Diadoc participant id | Low | CC expansion or operator note |
| ME-W1C-04 | Phone / fax not on CC | Low | CC update or Wave 2 contact corroboration |
| ME-W1C-05 | Corporate website / domain not on CC | Low | Wave 4 / 5 with registrar E1 |

---

## 9. Readiness summary

| org_id | population | duplicate review | attestation (active) | wave 2 person deps |
|--------|------------|------------------|----------------------|---------------------|
| ORG-0006 | **Complete** | **Pass** | **Complete** — AT-W1C-01 | **Unblocked** *(org endpoint active)* |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) | Population plan + REPORT |
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | Active attestation act (AT-W1C-01) |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md) | Attestation sequence plan *(superseded for lifecycle)* |
| [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | Evidence verification |
| [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | Wave 1 orgs ORG-0001..0004 — baseline |

---

*ATLAS Wave 1C SIBCAR Organization Register v1 — documentation only.*
