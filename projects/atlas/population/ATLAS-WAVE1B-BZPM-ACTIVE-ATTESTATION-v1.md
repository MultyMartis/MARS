# ATLAS Wave 1B BZPM Active Attestation v1



**Status:** **attested** — first official Organization active attestation for Wave 1B BZPM tranche.  

**Program:** ATLAS — Business Reality Registry  

**Date:** 2026-06-06  

**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  

**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md](ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md) · [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md)  

**Is not:** runtime, API, database export, Person population, Project / Website / Domain entities, Relationship edges, Foundation amendment.



**Prerequisites (operator-confirmed):**



- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**

- Wave 1 Attestation: **COMPLETE**

- Wave 1B BZPM Population (AT-W1B-00): **COMPLETE**

- Wave 1B BZPM Evidence Verification: **COMPLETE**

- Wave 1B BZPM Identity Correction (COR-W1B-01..06): **COMPLETE**

- Counterparty Card BZPM: **present** at `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\`



---



# REPORT — ATLAS Wave 1B BZPM Active Attestation



**Attestation date:** 2026-06-06  

**Tranche:** **AT-W1B-01** — Active attest  

**Promotion:** ORG-0005, LE-0004 — **proposed** → **active**



---



## 1. Pre-check — evidence inventory (mandatory)



**Governance:** [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01..03 · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-04.



**Folder verified:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\` — **exists** (filesystem listing 2026-06-06).



| # | Filename | Format | Size | Role |

|---|----------|--------|------|------|

| 1 | `Реквизиты.docx` | DOCX | 15 762 bytes (15.4 KB) | **Primary Counterparty Card** — «Анкета Участника аукциона / Сведения об Участнике»; structured legal requisites (INN, KPP, OGRN, legal name, addresses, bank, signatory, website) |



**Inventory verdict:**



| Check | Result |

|-------|--------|

| Folder exists | **Pass** |

| Inventory table produced | **Pass** |

| ≥1 non-placeholder evidence file | **Pass** — one DOCX CC |

| Primary Counterparty Card cited | **Pass** — `Реквизиты.docx` → **EV-W1B-CC-01** |



**Primary evidence path:**



```text

C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx

```



**Prior marker obsolete:** ME-W1B-01 («CC absent») — **cleared** per filesystem proof and [ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md](ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md).



---



## 2. Legal entity review — LE-0004



**Source:** EV-W1B-CC-01 only. Cross-check against operator expected facts and attestation proposal.



| Field | Expected (operator) | EV-W1B-CC-01 | Match |

|-------|---------------------|--------------|-------|

| **Legal name (full)** | Общество с ограниченной ответственностью «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | §1 — identical string | **Match** |

| **Legal name (short)** | *(same as full in CC)* | §2 — identical string | **Match** |

| **Entity type** | ООО | §1–§2 | **Match** |

| **INN** | 2221237587 | §3, §23 | **Match** |

| **KPP** | 222101001 | §3, §23 | **Match** |

| **OGRN** | 1172225049787 | §3, §23 | **Match** |

| **Director / signatory** | Крюков Александр Сергеевич | §19, §21–§24 — «Директор Крюков Александр Сергеевич» | **Match** |

| **Website** | bzpm.ru | §17 — **Bzpm.ru** | **Match** *(case variant only)* |

| **Registration date** | — | 22.12.2017 | CC-only — no conflict |

| **Legal address** | — | 656011, г. Барнаул, пр-т Калинина, 15в, оф. 110 | CC-only |

| **org_binding** | ORG-0005 | Population §4 | **Match** |



**Discrepancies:** **None** — all operator-expected critical identifiers match CC extraction. No silent overwrite applied.



**CC ancillary notes (non-blocking, recorded as-is):**



| Note | Detail |

|------|--------|

| Email typo | CC lists `zakaz@bzmp.ru` — domain stem **bzmp** vs website **bzpm**; recorded verbatim; no correction applied |

| Industry narrative | CC legal name indicates food machinery (ЗПМ); prior dealership narrative from project context **does not** override CC legal identity |



**Verdict:** **Pass** — legal entity layer consistent; critical identifiers complete on E1 CC.



---



## 3. Identity review



**Governance:** EFV-01..06 · COR-W1B-01..06.



| Check | Result | Basis |

|-------|--------|-------|

| **BZPM standalone organization** | **Pass** | EV-W1B-CC-01 defines distinct legal person INN 2221237587 |

| **canonical_name BZPM** | **Pass** | Operator slug corroborated by CC website **Bzpm.ru** §17; not dealership narrative |

| **LE-0004 legal display** ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | **Pass** | CC §1–§2 — bound to ORG-0005, not a second org |

| **BZPM ≠ SIBCAR** | **Pass** | COR-W1B-01, COR-W1B-05; ORG-0006 INN 5405512542; zero SIBCAR strings in CC |

| **BZPM ≠ Triumph (ORG-0004)** | **Pass** | W1B-D-02 — distinct clients |

| **BZPM ≠ Polygon (ORG-0001)** | **Pass** | W1B-D-03 |

| **BZPM ≠ MetaCode (ORG-0002)** | **Pass** | W1B-D-03 |

| **BZPM ≠ i-SEO (ORG-0003)** | **Pass** | W1B-D-03 |

| **SIBCAR alias cluster revoked** | **Pass** | COR-W1B-01 — Автосалон СИБКАР, SIBCAR, СИБКАР **not** attested |

| **ORG-0005 ↔ LE-0004 binding** | **Pass** | Single legal subject, single org anchor |

| **SITE-001 class boundary** | **Pass** | W1B-D-04 — Website/project context ≠ Organization identity |



**Verdict:** **Pass** — BZPM is a **standalone organization**; identity correction honored; no merge with SIBCAR or operator orgs.



---



## 4. Duplicate review



**Reopened per** [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) COR-W1B-02 after CC intake.



| review_id | Pair | Verdict | Blocking |

|-----------|------|---------|----------|

| **W1B-D-01** | BZPM vs SIBCAR / alias cluster | **Distinct — Fail (reopened → Pass distinct)** | No — subjects are **not** merged; COR-W1B-01 enforced |

| **W1B-D-02** | BZPM vs Triumph (ORG-0005 vs ORG-0004) | **Distinct — Pass** | No |

| **W1B-D-03** | BZPM vs operator orgs (ORG-0001..0003) | **Distinct — Pass** | No |

| **W1B-D-04** | ORG-0005 vs SITE-001 | **Class boundary — Pass** | No |

| **W1B-D-05** | Dealership homonym / site title | **Open — low** | No |

| **W1B-D-06** | D1 unresolved duplicate | **None** | No |

| **W1C-D-01** *(cross-tranche)* | SIBCAR (ORG-0006) vs BZPM (ORG-0005) | **Distinct — Pass** | No |



**INN 2221237587 cross-registry:** no collision with Wave 1 dataset ORG-0001..0004 (documentation-level check) or ORG-0006 SIBCAR (INN 5405512542).



**Verdict:** **Pass** — duplicate review complete on CC-backed identifiers; no blocking duplicates; W1B-D-05 deferred (non-blocking for Organization **active**).



---



## 5. Evidence sufficiency and attestation gates



| Gate ID | Rule | Status |

|---------|------|--------|

| **W1B-EG-01** | W1-B minimum E1 at **active** | **Pass** — EV-W1B-CC-01 |

| **W1B-EG-02** | CC preferred path when obtainable | **Pass** — CC placed and inventoried |

| **W1B-EG-03** | No contract/invoice primary (OAR-BAN-01) | **Pass** |

| **W1B-EG-04** | No hostname-only org (OAR-BAN-03) | **Pass** — CC primary, not SITE-001 hostname |

| **W1B-EG-05** | Duplicate batch before **active** | **Pass** — W1B-D-01..06 + W1C-D-01 |

| **W1B-EG-06** | Human attest mandatory (OAR-HUM-01) | **Pass** — this act |

| **W1B-EG-07** | LE critical fields reviewed before org **active** | **Pass** — §2 legal entity review |

| **STOP-EFV-04** | Active while CC contradicts proposal | **Pass** — COR-W1B-01 applied; contradictions resolved |

| **STOP-CPV-01..03** | Inventory before attest | **Pass** — §1 |



**ME-* resolution:**



| ID | Prior | After this act |

|----|-------|----------------|

| **ME-W1B-01** | CC absent — **blocking** | **Resolved** — EV-W1B-CC-01 |

| **ME-W1B-02** | Legal entity unknown — **blocking** | **Resolved** — LE-0004 fields from CC |



**Verdict:** **Pass** — E1 CC satisfies W1-B Organization attestation minimum.



---



## 6. Attestation tranche executed



### 6.1 AT-W1B-01 — Active attest



| Step | Action | Attestor | Evidence ref | Status |

|------|--------|----------|--------------|--------|

| 1 | Verify CC folder + inventory | Steward | CPV-01; §1 | **Done** |

| 2 | Extract and reconcile LE-0004 fields | Steward | EV-W1B-CC-01 | **Done** |

| 3 | Apply identity correction (COR-W1B-01) | Steward | Identity correction v1 | **Done** |

| 4 | Duplicate review sign-off on INN/OGRN | Steward | W1B-D-01..06 | **Done** |

| 5 | Attest LE-0004 **active** | Steward | LegalEntities discipline | **Done** |

| 6 | Attest Organization ORG-0005 **active** | Steward (delegated) | W1-EXEC-04 analog | **Done** |

| 7 | Promote CC-backed alias **active**; revoke unsupported aliases | Steward | EFV-01; COR-W1B-01 | **Done** |



**Not executed in this tranche (by scope restriction):**



| Step | Action | Reason |

|------|--------|--------|

| Create Person entities | **Excluded** | Operator scope — Wave 2B-BZPM deferred |

| Create Project / Website / Domain | **Excluded** | Operator scope |

| Create Relationship edges | **Excluded** | Wave 6+ deferred |

| Queue Wave 2 Person candidates | **Deferred** | Separate future pass |



---



## 7. Attested entity records



### 7.1 LE-0004 — ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ»



| Field | Value |

|-------|-------|

| **legal_entity_id** | LE-0004 |

| **legal_entity_name** | Общество с ограниченной ответственностью «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» |

| **entity_type** | ООО |

| **inn** | 2221237587 |

| **kpp** | 222101001 |

| **ogrn_ogrnip** | 1172225049787 |

| **registration_date** | 22.12.2017 |

| **legal_address** | 656011, Россия, г. Барнаул, пр-т Калинина, 15в, оф. 110 |

| **actual_address** | 656011, Россия, г. Барнаул, пр-т Калинина, 15в, оф. 110 |

| **document_signatory** | Крюков Александр Сергеевич |

| **beneficial_owner** | Крюков Александр Сергеевич, ИНН 222304520613 (100%) |

| **tax_system** | Общая, НДС 20% |

| **org_binding** | ORG-0005 |

| **attestation_basis** | E1 EV-W1B-CC-01; duplicate review W1B-D-01..06 **Pass**; legal entity review §2 |

| **evidence_tier** | **E1** |

| **lifecycle_state (prior)** | **proposed** |

| **lifecycle_state (attested)** | **active** |

| **notes** | Not in Wave 1 dataset xlsx; LE-0005 reserved for SIBCAR |



### 7.2 ORG-0005 — BZPM



| Field | Value |

|-------|-------|

| **org_id** | ORG-0005 |

| **canonical_name** | BZPM |

| **wave_tier** | W1-B |

| **business_role** | **CLIENT** |

| **legal_entity_id** | LE-0004 |

| **legal_entity_name** | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» |

| **inn** | 2221237587 |

| **kpp** | 222101001 |

| **ogrn_ogrnip** | 1172225049787 |

| **primary_website** | **Bzpm.ru** *(CC §17 — corporate site field; prod registrant not attested)* |

| **primary_domain** | **SAFE UNKNOWN** *(prod registrant)* |

| **primary_contact_person_id** | **SAFE UNKNOWN** — Wave 2B-BZPM |

| **attestation_basis** | E1 EV-W1B-CC-01; identity review §3; COR-W1B-01..06 |

| **evidence_tier** | **E1** |

| **lifecycle_state (prior)** | **proposed** |

| **lifecycle_state (attested)** | **active** |

| **notes** | Second W1-B client; distinct from ORG-0006 SIBCAR; SITE-001 is engagement context only |



### 7.3 Alias disposition (proposed → active / revoked)



| org_id | alias | alias_type | evidence_ref | prior state | attested state |

|--------|-------|------------|--------------|-------------|----------------|

| ORG-0005 | BZPM | operator slug / domain stem | EV-W1B-CC-01 §17 (Bzpm.ru) | **proposed** | **active** |

| ORG-0005 | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | RU legal short display | EV-W1B-CC-01 §1–§2 | — | **active** |

| ORG-0005 | ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ | RU trade fragment (quoted name) | EV-W1B-CC-01 §1 | — | **active** |

| ORG-0005 | Автосалон СИБКАР | RU site brand | EV-W1B-01 *(project only)* | **proposed** | **revoked** — COR-W1B-01 |

| ORG-0005 | SIBCAR | Latin trade | EV-W1B-02 *(project only)* | **proposed** | **revoked** — COR-W1B-01 |

| ORG-0005 | СИБКАР | Cyrillic abbreviation | EV-W1B-01 *(project only)* | **proposed** | **revoked** — COR-W1B-01 |



---



## 8. Explicit exclusions (not attested in this package)



| Item | Treatment |

|------|-----------|

| Person entities (PER-*) | **Not created** — Wave 2B-BZPM deferred |

| Крюков Александр Сергеевич → PER-* | **Queue note only** — CC §19–§22; Person wave later |

| Person ↔ Organization edges | **Deferred** — Wave 2B-BZPM |

| Project entities (PRJ-*) | **Not created** — Wave 3+ |

| Website entities (WEB-*) | **Not created** — Wave 4 |

| Domain entities (DOM-*) | **Not created** — Wave 5 |

| REL-* CLIENT_OF ORG-0005 → ORG-0001 | **Deferred** — Wave 6+ |

| REL-* ORG-0005 ↔ ORG-0006 | **SAFE UNKNOWN** — COR-W1B-06 |

| Foundation documents | **Not modified** |



---



## 9. Residual gaps (non-blocking)



| ID | Topic | Severity | Mitigation |

|----|-------|----------|------------|

| **ME-W1B-03** | Production public URL / registrant proof | Low | Wave 4 / 5 |

| **ME-W1B-04** | BZPM acronym expansion (ЗПМ) | Low | Steward note — CC legal name clarifies |

| **ME-W1B-05** | EDO / Diadoc participant id | Low | CC update |

| **W1B-D-05** | Dealership homonym vs CC industry | Low | Website intake if needed |

| **UNKNOWN** | Commercial tie SITE-001 ↔ OOO ЗПМ vs undisclosed SIBCAR entity | Medium | Separate SIBCAR CC path (ORG-0006 active) |



**Blocking gaps remaining:** **None**



---



## 10. Foundation consistency check



| Check | Result |

|-------|--------|

| No new entity types | **Pass** |

| No Foundation modification | **Pass** |

| No Wave 1 record modification | **Pass** |

| W1-B acquisition rules followed | **Pass** |

| SAFE UNKNOWN — no invented identifiers | **Pass** |

| EFV-01 alias discipline | **Pass** |

| CPV-01 inventory discipline | **Pass** |

| BZPM ≠ SIBCAR split honored | **Pass** |

| ATLAS-ATTESTATION-MODEL contract followed | **Pass** |

| Documentation only | **Pass** |



---



## 11. Attestation verdict



```text

ACTIVE ORGANIZATION

```



**Conditions met:**



1. ORG-0005 **active** — canonical Organization attested under E1 CC discipline.

2. LE-0004 **active** — legal entity attested and bound to ORG-0005.

3. CC-backed aliases (3 rows) promoted to **active**; unsupported SIBCAR cluster **revoked** per COR-W1B-01.

4. Pre-check inventory, legal entity review, identity review, duplicate review, and evidence gates — **all Pass**.

5. ME-W1B-01, ME-W1B-02 — **resolved**.



**Supersedes prior verdict:**



| Prior verdict | Source | Disposition |

|---------------|--------|-------------|

| **PARTIALLY READY** | [ATLAS-WAVE1B-BZPM-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-ATTESTATION-v1.md) §10 | **Superseded** — ORG-0005 now **active** |



**Not selected:**



| Verdict | Reason |

|---------|--------|

| **PARTIALLY READY** | AT-W1B-01 complete |

| **NOT READY** | All gates pass |

| **NO EVIDENCE FOUND** | EV-W1B-CC-01 present |

| **EVIDENCE FOUND — ALIAS CONFIRMED (BZPM=SIBCAR)** | Refuted by CC and COR-W1B-01 |



**Downstream note:** Wave 2B-BZPM Person Population may proceed in a **separate future pass** — not executed in this package.



---



## 12. Package lineage



```text

Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)

        │

        ▼

Wave 1B BZPM Population (AT-W1B-00) ──► proposed ORG-0005

        │

        ▼

Evidence Verification + Identity Correction ──► COR-W1B-01..06

        │

        ▼

Wave 1C SIBCAR Active Attestation ──► ORG-0006 active (distinct)

        │

        ▼

Wave 1B BZPM Active Attestation (THIS PACKAGE — AT-W1B-01) ──► ORG-0005 active

        │

        ▼

Wave 2B-BZPM Person Population (FUTURE — separate pass)

```



---



## 13. Related documents



| Doc | Role |

|-----|------|

| [ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md](ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md) | Evidence extraction |

| [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) | COR-W1B-01..06 |

| [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) | Prior **proposed** register |

| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | Parallel client attest |

| [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) | Inventory discipline |



---



*ATLAS Wave 1B BZPM Active Attestation v1 — documentation only.*

