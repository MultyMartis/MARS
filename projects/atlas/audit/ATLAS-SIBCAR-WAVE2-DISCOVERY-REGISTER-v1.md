# ATLAS SIBCAR Wave 2 Person Discovery Register v1

**Status:** **documented** — point-in-time Person discovery register (audit only).  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07  
**Scope:** ORG-0006 **SIBCAR** — Person candidates, missing operational roles, operator questions, Wave 2C sequence  
**Parent:** [ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md) · [ATLAS-SIBCAR-WAVE2-DISCOVERY-SUMMARY-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-SUMMARY-v1.md)  
**Is not:** population register, attestation export, Person mint, runtime table.

---

## 1. Register purpose

Единый **discovery register** для подготовки Wave 2C-SIBCAR: известные Person-кандидаты, пробелы operational roles относительно ZPM, вопросы оператору, рекомендуемая последовательность. Lifecycle Person — **none minted**; все строки **candidate** или **missing**.

---

## 2. Anchor entity cross-reference

| Class | ID | Lifecycle | Person linkage |
|-------|-----|-----------|----------------|
| Organization | ORG-0006 SIBCAR | **active** — AT-W1C-01 | Person anchor; `primary_contact_person_id` **SAFE UNKNOWN** |
| Legal Entity | LE-0005 ООО «СибКар» | **active** — AT-W1C-01 | `document_signatory` = Карандашов М.П. |
| Project | PRJ-0011 | **active** — AT-W3-SIBCAR-01 | No Person↔Project edges |
| Relationship | REL-0041 | **active** — AT-W6B-02 | ORG-0006 → ORG-0001 CLIENT_OF — not Person role |

**Counts:** attested Person for SIBCAR **0** · attested Person→Org **0**

---

## 3. Known persons inventory

### 3.1 Attested roster

| person_id | canonical_name | primary_org | lifecycle | attestation | org_edge |
|-----------|----------------|-------------|-----------|-------------|----------|
| — | — | — | — | — | — |

**Total attested:** **0**

### 3.2 Candidate roster (discovery)

| candidate_id | proposed person_id | canonical_name | population_slice | role_signals | operational_contact | document_signatory | evidence_tier | evidence_ref | contacts | lifecycle | readiness |
|--------------|-------------------|----------------|------------------|--------------|---------------------|--------------------|--------------|--------------|----------|-----------|-----------|
| **CAND-SIBCAR-P01** | **PER-0016** *(proposed)* | Карандашов Максим Петрович | **client-side** | Руководитель *(CC)*; Главный бухгалтер *(CC)*; exact title **SAFE UNKNOWN** | **SAFE UNKNOWN** | **yes** — LE-0005 §22 | **E1** | EV-W1C-CC-01 §21–§24 | phone/TG/email **SAFE UNKNOWN** | **candidate** | **partial** — identity E1; contacts missing |
| **CAND-SIBCAR-P02** | **PER-0017** *(conditional)* | **SAFE UNKNOWN** | **client-side** | **SAFE UNKNOWN** | **yes** *(if exists)* | **no** | **E0** *(projected)* | EV-W2C-SIBCAR-OP-01 **TBD** | **SAFE UNKNOWN** | **not queued** | **blocked** — OQ-W2C-09 |

### 3.3 Org contact facts (non-Person rows)

| field | value | evidence_ref | maps_to_person |
|-------|-------|--------------|----------------|
| org_email | info_sibcar@mail.ru | EV-W1C-CC-01 §16 | **SAFE UNKNOWN** — OQ-W2C-08 |
| org_phone | **SAFE UNKNOWN** | — | ME-W1C-04 |
| edo_participant_id | **SAFE UNKNOWN** | — | ME-W1C-03 |

---

## 4. Missing operational roles inventory

### 4.1 Person → Organization relationships (missing)

| draft_rel_id | source_person | target_org | relationship_type | zpm_analog | evidence *(projected)* | lifecycle | blocking |
|--------------|---------------|------------|-------------------|------------|------------------------|-----------|----------|
| **REL-SIBCAR-01** | PER-0016 Карандашов | ORG-0006 | **GENERAL_DIRECTOR** | REL-ZPM-01 | E1 EV-W1C-CC-01 §22; LE-0005 signatory | **missing** | Person attestation |
| **REL-SIBCAR-02** | PER-0017 *(TBD)* | ORG-0006 | **REPRESENTATIVE** | REL-ZPM-02 | E0 EV-W2C-SIBCAR-OP-01 | **missing** | OQ-W2C-09; second Person |

### 4.2 Organization display pointer

| org_id | field | zpm_value | sibcar_value | status |
|--------|-------|-----------|--------------|--------|
| ORG-0006 | `primary_contact_person_id` | PER-0014 | **SAFE UNKNOWN** | **missing** |

### 4.3 Role signal gap matrix

| role_signal_slot | zpm_coverage | sibcar_coverage | gap |
|------------------|--------------|-----------------|-----|
| CC director / signatory Person | PER-0015 **active** | CAND-SIBCAR-P01 **candidate** | Mint pending |
| Primary operational contact | PER-0014 **active** | **SAFE UNKNOWN** | **High** |
| Work acceptance narrative | EV-W2-ZPM-OP-01 | **None** | **High** |
| Contact register (phone/TG/email) | Person register §4 | **None** | **High** |
| Alias register | PER-0014 aliases | **None** | Low — CC silent on variants |
| Diadoc signer | SAFE UNKNOWN | SAFE UNKNOWN | Parity — both open |

### 4.4 Excluded roles (do not mint — ZPM precedent)

| relationship_type | exclusion_basis |
|-------------------|-----------------|
| **OWNER** | Beneficial owner CC fact ≠ OWNER edge |
| **EMPLOYEE** | Use REPRESENTATIVE if operator confirms contact role |
| Person ↔ Person | Wrong family |
| Person ↔ Project / Website / Domain | Out of Wave 2C scope |

### 4.5 Missing documentation artifacts

| artifact_id | zpm_file_pattern | sibcar_status |
|-------------|------------------|---------------|
| DOC-W2C-01 | WAVE2*-PERSON-POPULATION | **Missing** |
| DOC-W2C-02 | WAVE2*-PERSON-REGISTER | **Missing** |
| DOC-W2C-03 | WAVE2*-PERSON-ATTESTATION | **Missing** |
| DOC-W2C-04 | WAVE2*-PERSON-ACTIVE-ATTESTATION | **Missing** |
| DOC-W2C-05 | WAVE2*-*-RELATIONSHIP-POPULATION | **Missing** |
| DOC-W2C-06 | WAVE2*-*-RELATIONSHIP-REGISTER | **Missing** |
| DOC-W2C-07 | WAVE2*-*-RELATIONSHIP-ATTESTATION | **Missing** |
| EV-W2C-SIBCAR-OP-01 | Operator mission inputs | **Missing** |

---

## 5. Operator questions register

| q_id | priority | question | blocks | default_if_unanswered |
|------|----------|----------|--------|----------------------|
| OQ-W2C-01 | **Blocking** | Карандашов = единственный операционный контакт Полигон ↔ SIBCAR? | Model selection | SAFE UNKNOWN |
| OQ-W2C-02 | **Blocking** | Точная должность Карандашова (CC §21)? | role_signals | «Руководитель» CC label only |
| OQ-W2C-03 | **Blocking** | Кто принимает работу / акты (имя + канал)? | operational_contact | SAFE UNKNOWN |
| OQ-W2C-04 | **Blocking** | Подтверждение PER-0016 для Карандашова? | ID assignment | Steward proposes PER-0016 |
| OQ-W2C-05 | High | Телефон контактного лица? | Contact register | SAFE UNKNOWN |
| OQ-W2C-06 | High | Telegram / мессенджер? | Contact register | SAFE UNKNOWN |
| OQ-W2C-07 | High | Email контактного лица? | Contact register | SAFE UNKNOWN |
| OQ-W2C-08 | High | info_sibcar@mail.ru — org или Person? | Email mapping | SAFE UNKNOWN |
| OQ-W2C-09 | Medium | Отдельное E0 контактное лицо (не на CC)? | Second Person | No second person |
| OQ-W2C-10 | Medium | ФИО / роль / контакты второго лица? | PER-0017 candidate | N/A |
| OQ-W2C-11 | Medium | Доверенное лицо (CC §25–§26)? | POA Person | None |
| OQ-W2C-12 | Low | Diadoc / EDO подписант? | EDO edge | SAFE UNKNOWN |
| OQ-W2C-13 | Low | Обновить CC до Wave 2C? | E1 enrichment | Optional E0 path |
| OQ-W2C-14 | Medium | Single-person model confirmed? | Parity decision | Pending OQ-W2C-01 |

---

## 6. Recommended Wave 2 population sequence

| step | phase | action | prerequisite | output artifact |
|------|-------|--------|--------------|-----------------|
| **1** | A | Operator discovery session — OQ-W2C-01..14 | This register | EV-W2C-SIBCAR-OP-01 |
| **2** | B | Evidence pre-check EV-W1C-CC-01 + OP-01 | Step 1 | Pre-check record in Population doc |
| **3** | B | Duplicate batch W2C-SIBCAR-D-* | PER-0001..0015 roster | Duplicate register section |
| **4** | B | Author Person Population + Register + Attestation plan | Steps 1–3 | DOC-W2C-01..03 |
| **5** | C | AT-W2C-SIBCAR-01 — PER-0016 Карандашов | Step 4; E1 ready | DOC-W2C-04 |
| **6** | C | AT-W2C-SIBCAR-02 — second Person *(conditional)* | OQ-W2C-09 yes | DOC-W2C-04 extension |
| **7** | D | Author Relationship Population / Register / Attestation | All Person endpoints **active** | DOC-W2C-05..07 |
| **8** | D | Attest REL-SIBCAR-01 GENERAL_DIRECTOR | Step 5 | Active relationship |
| **9** | D | Attest REL-SIBCAR-02 REPRESENTATIVE *(conditional)* | Step 6 | Active relationship |
| **10** | D | Set ORG-0006.primary_contact_person_id | Steps 8–9 | Org register sync |
| **11** | E | Slice consistency + backup refresh | Steps 5–10 | Future audit pack |

**Attestation order rule:** CC signatory Person **before** E0 operational Person; Person→Org edges **after** Person active acts.

---

## 7. ZPM parity checklist

| # | criterion | zpm | sibcar | pass |
|---|-----------|-----|--------|------|
| 1 | ORG endpoint **active** before Person | AT-W1B-01 | AT-W1C-01 | **Yes** |
| 2 | ≥1 E1 CC-backed Person **active** | PER-0015 | 0 — candidate | **No** |
| 3 | E0 operational Person *(if applicable)* | PER-0014 | Not documented | **No** |
| 4 | Person→Org GENERAL_DIRECTOR edge | REL-ZPM-01 | Missing | **No** |
| 5 | Person→Org REPRESENTATIVE edge | REL-ZPM-02 | Missing / may N/A | **No** |
| 6 | primary_contact_person_id on org | PER-0014 | SAFE UNKNOWN | **No** |
| 7 | Wave 2 Person doc pack (4 files) | Complete | 0 files | **No** |
| 8 | Wave 2B Relationship doc pack (3 files) | Complete | 0 files | **No** |
| 9 | Operator evidence EV-W2-*-OP-01 | Present | Missing | **No** |
| 10 | Duplicate review before attestation | W2-ZPM-D-* | Pending W2C | **Partial** |
| 11 | Person optional on structural stack | Required prereq cited | Optional — documented | **Delta** |
| 12 | Explicit relationship exclusions documented | Wave 2B §5 | Apply at 2C | **Pending** |

**Parity score:** **2 / 12** pass · **1** partial · **1** intentional delta

---

## 8. Evidence index (Person discovery)

| ref | artifact | person_role |
|-----|----------|-------------|
| EV-W1C-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | CAND-SIBCAR-P01 identity; LE-0005 signatory |
| EV-W1C-02 | [site-passport.md](../../ocpilot/sites/site-001/site-passport.md) | Not Person evidence |
| EV-W1C-03 | [project-access-brief.md](../../ocpilot/sites/site-001/project-access-brief.md) | Project context only |
| EV-W2C-SIBCAR-OP-01 | **TBD** — operator mission inputs | Operational contact; contacts; work acceptance |
| AT-W1C-01 | [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](../population/ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | Org endpoint gate |

---

## 9. SAFE UNKNOWN inventory (Person slice)

| field | entity | status | resolution_path |
|-------|--------|--------|-----------------|
| primary_contact_person_id | ORG-0006 | Open | Wave 2C-SIBCAR relationship attestation |
| Signatory exact title | CAND-SIBCAR-P01 | Open | OQ-W2C-02 or CC update |
| operational_contact designation | CAND-SIBCAR-P01 | Open | OQ-W2C-01, OQ-W2C-03 |
| Person phone / TG / email | CAND-SIBCAR-P01 | Open | OQ-W2C-05..07 |
| Second E0 person identity | CAND-SIBCAR-P02 | Open | OQ-W2C-09..10 |
| Diadoc signer | ORG-0006 / Person | Open | OQ-W2C-12 |
| PER-* canonical assignment | CAND-SIBCAR-P01 | Open | OQ-W2C-04 — propose PER-0016 |

---

## 10. Findings register

| id | severity | topic |
|----|----------|-------|
| SIBCAR-W2D-01 | High | Zero attested Person entities |
| SIBCAR-W2D-02 | High | Zero Person→Org operational edges |
| SIBCAR-W2D-03 | High | primary_contact_person_id unset |
| SIBCAR-W2D-04 | High | No operator mission pack |
| SIBCAR-W2D-05 | Medium | Single- vs two-person model undecided |
| SIBCAR-W2D-06 | Medium | Signatory title SAFE UNKNOWN |
| SIBCAR-W2D-07 | Medium | Person contacts absent |
| SIBCAR-W2D-08 | Low | Wave 2C doc pack not authored |
| SIBCAR-W2D-09 | Low | W2C duplicate batch pending |
| SIBCAR-W2D-10 | Info | Downstream waves treat Person as optional |
| SIBCAR-W2D-11 | Info | Coverage audit stale on Person |
| SIBCAR-W2D-12 | Info | DOM-SIBCAR-01 proposed — orthogonal |

---

## 11. SIBCAR Person graph (current vs projected)

**Current:**

```text
ORG-0006 SIBCAR ──CLIENT_OF──► ORG-0001 Полигон     (REL-0041 — active)
       │
       ├──► LE-0005 (signatory name on LE only — not PER-*)
       ├──► PRJ-0011 (active — no Person edges)
       └──► WEB-SIBCAR-01 / DOM-SIBCAR-01 (no Person edges)

Person layer: EMPTY
```

**Projected (minimal single-person model):**

```text
ORG-0006 ◄──REL-SIBCAR-01── PER-0016 Карандашов (GENERAL_DIRECTOR)
       │
       primary_contact_person_id = PER-0016  *(if single-person confirmed)*
```

**Projected (ZPM two-person parity):**

```text
ORG-0006 ◄──REL-SIBCAR-01── PER-0016 Карандашов (GENERAL_DIRECTOR)
       ◄──REL-SIBCAR-02── PER-0017 *(TBD)* (REPRESENTATIVE; primary_contact)
```

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md) | Full audit narrative |
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-SUMMARY-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-SUMMARY-v1.md) | Executive summary |
| [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](../population/ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | CC extraction |
| [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](../population/ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) | Parity template |

---

*ATLAS SIBCAR Wave 2 Person Discovery Register v1 — discovery only; no population.*
