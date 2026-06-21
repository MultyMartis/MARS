# ATLAS SIBCAR Wave 2 Person Discovery Audit v1

**Status:** **documented** — Person discovery preparation audit (audit only).  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07  
**Auditor posture:** Registry Steward review (documentation-level)  
**Scope:** SIBCAR slice — Person and operational-role gap analysis vs ZPM parity; anchor entities ORG-0006, LE-0005, PRJ-0011, REL-0041; SIBCAR Wave 1C through Wave 5 (+ Wave 6B commercial context)  
**Parent:** [ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md) · [ATLAS-SIBCAR-WAVE2-DISCOVERY-SUMMARY-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-SUMMARY-v1.md)  
**Is not:** population, attestation, entity creation, relationship creation, Foundation amendment, runtime export, git commit.

**Restrictions observed:** No entities created. No relationships created. No attestation acts. No Foundation modifications. No population state changes. No git commit. No push.

---

# REPORT — ATLAS SIBCAR Wave 2 Person Discovery Audit

## 0. Audit scope and method

### 0.1 Goal

Подготовить **discovery package** для Wave 2C-SIBCAR Person Population: зафиксировать известных кандидатов, пробелы operational roles относительно ZPM slice, вопросы оператору и рекомендуемую последовательность population **без** выполнения population.

### 0.2 In-scope anchor entities

| Class | ID | Lifecycle (attestation authority) | Person relevance |
|-------|-----|-----------------------------------|------------------|
| Organization | **ORG-0006** SIBCAR | **active** — AT-W1C-01 | Person anchor; `primary_contact_person_id` **SAFE UNKNOWN** |
| Legal Entity | **LE-0005** ООО «СибКар» | **active** — AT-W1C-01 | `document_signatory` = Карандашов М.П. (CC §22) |
| Project | **PRJ-0011** Автосалон СИБКАР — OpenCart dealership | **active** — AT-W3-SIBCAR-01 | Person↔Project **excluded** by scope |
| Relationship | **REL-0041** ORG-0006 → ORG-0001 **CLIENT_OF** | **active** — AT-W6B-02 | Commercial org↔org — **not** Person role |

### 0.3 SIBCAR wave artifacts reviewed

| Wave | Artifacts | Person posture in artifact |
|------|-----------|----------------------------|
| **1C** | Organization Population / Register / Attestation / Active Attestation; Evidence Verification | Candidate Persons §8; Wave 2C queue; PER-* **not minted** |
| **3** | Project Population / Register / Attestation / Active Attestation | No Person creation; SU-SIBCAR-PRJ-07 optional |
| **3B** | Project Relationship Population / Register / Attestation | No Person→Project; SU-SIBCAR-PRJ-07 optional |
| **4** | Website Population / Register / Attestation / Active Attestation | No Person↔Website |
| **4B** | Website Relationship Population / Register / Attestation | No Person edges |
| **5** | Domain Population / Register / Attestation | DOM-SIBCAR-01 **proposed**; no Person↔Domain |
| **6B** | Commercial Relationship *(REL-0041)* | Org↔org only |
| **Operational slice** | Operational Slice Audit / Register / Summary | Wave 2C Person **optional**, **PARTIAL** |
| **Crosswalk** | OCPilot SIBCAR Crosswalk Audit | No Person crosswalk |

**Not in scope for this audit:** Wave 5B SIBCAR Domain relationships (not authored); OCPilot Run 5 execution; EAR snapshot.

### 0.4 ZPM parity reference

ZPM slice (ORG-0005) — attested Person stack:

| Layer | ZPM (reference) | SIBCAR (current) |
|-------|-----------------|------------------|
| Person entities | PER-0014, PER-0015 **active** | **0** minted |
| Person→Org edges | REL-ZPM-01 GENERAL_DIRECTOR; REL-ZPM-02 REPRESENTATIVE | **0** |
| `primary_contact_person_id` | PER-0014 (Wave 2B) | **SAFE UNKNOWN** |
| E1 CC person | PER-0015 (signatory) | Candidate only — Карандашов |
| E0 operator person | PER-0014 (operational contact) | **Not documented** |
| Operator evidence | EV-W2-ZPM-OP-01 | **No EV-W2C-SIBCAR-OP-* artifact** |
| Wave 2 doc pack | 4 Person + 3 Relationship files | **0** Wave 2C-SIBCAR files |

### 0.5 Method

Cross-read SIBCAR Wave 1C–5 artifacts; extract CC person lines from [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](../population/ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md); compare operational-role coverage to [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](../population/ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) and [ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md](../population/ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md); inventory SAFE UNKNOWN fields; derive operator questions and recommended population sequence **for future authoring only**.

---

## 1. Current known persons inventory

### 1.1 Attested Person entities (minted graph)

| person_id | canonical_name | lifecycle | attestation | org_edge |
|-----------|----------------|-----------|-------------|----------|
| — | — | — | — | — |

**Count:** **0** attested Person records for ORG-0006.

**Verdict:** SIBCAR slice has **no** canonical Person entities. All person knowledge exists as **candidates** or **org-level fields** only.

### 1.2 CC-backed person candidate (E1)

Source: **EV-W1C-CC-01** — `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx`

| Field | Value | CC section | Population status |
|-------|-------|------------|-------------------|
| **Canonical name (proposed)** | Карандашов Максим Петрович | §21–§22, §23–§24 | **Wave 2 candidate** — PER-* **TBD** *(likely PER-0016)* |
| **Role signals (CC)** | Руководитель; Главный бухгалтер | §22, §24 | Not attested as relationship |
| **Signatory title (exact)** | **SAFE UNKNOWN** | §21 — template lists «Руководитель (должность, ФИО)» without explicit должность string | Operator question required |
| **document_signatory (LE-0005)** | Карандашов Максим Петрович | §22 | Bound at LE layer — AT-W1C-01 |
| **Authorized representative (POA)** | — *(none listed)* | §25–§26 | No second CC person |
| **operational_contact** | **SAFE UNKNOWN** | — | Not designated |
| **Population slice** | **client-side** *(proposed)* | ZPM analog | Pending Wave 2C |
| **Evidence tier (Person)** | **E1** *(CC identity)* | EV-W1C-CC-01 | Sufficient for identity anchor |
| **Contacts (person-level)** | **SAFE UNKNOWN** | Phone/fax absent on CC | ME-W1C-04 |
| **Duplicate review** | **Pending** | — | Batch W2C-SIBCAR-D-* not run |

**Cross-reference:** [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](../population/ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) §8 · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](../population/ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) §5 exclusions.

### 1.3 Org-level contact facts (not Person rows)

| Field | Value | evidence_ref | Person mapping |
|-------|-------|--------------|----------------|
| Org email | info_sibcar@mail.ru | EV-W1C-CC-01 §16 | **SAFE UNKNOWN** — consumer `@mail.ru`; not attested Person contact |
| Org phone / fax | **SAFE UNKNOWN** | — | ME-W1C-04 |
| EDO / Diadoc participant id | **SAFE UNKNOWN** | — | ME-W1C-03 |

### 1.4 E0 operator-direct person candidates

| Candidate | Role signals | Evidence | Status |
|-----------|--------------|----------|--------|
| **Primary operational contact** | **SAFE UNKNOWN** | — | No EV-W2C-SIBCAR-OP-01; OCPilot SITE-001 reports phone/messengers **unknown** |
| **Second named contact** | — | — | **None documented** |

**ZPM analog:** PER-0014 Дубинский — E0 operator-direct, not on CC, attested as primary operational contact.

**SIBCAR delta:** No operator mission pack equivalent to EV-W2-ZPM-OP-01 exists in repository.

### 1.5 OCPilot / execution-layer person signals

| Source | Person signal | Atlas disposition |
|--------|---------------|-------------------|
| [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](../../ocpilot/sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md) | Contacts partial — email only | Informational; not Person intake |
| [project-access-brief.md](../../ocpilot/sites/site-001/project-access-brief.md) | No named client contact roster | Not Person evidence |
| [ATLAS-OCPILOT-SIBCAR-CROSSWALK-AUDIT-v1.md](ATLAS-OCPILOT-SIBCAR-CROSSWALK-AUDIT-v1.md) | No Person crosswalk rows | Expected — Person layer absent |

### 1.6 Known persons inventory summary

| Category | Count | Notes |
|----------|-------|-------|
| Attested PER-* for SIBCAR | **0** | |
| E1 CC-backed candidates | **1** | Карандашов М.П. |
| E0 operator-direct candidates | **0** documented | Parity gap vs ZPM |
| POA / authorized representative on CC | **0** | §25–§26 empty |
| **Total discoverable today** | **1** (E1 thin) | ZPM had **2** at Wave 2 |

---

## 2. Missing operational roles inventory

Operational roles in Atlas wave discipline = **Person role signals** + **attested Person→Organization relationship types** + **ORG display pointer** (`primary_contact_person_id`). Not governance roles ([ATLAS-ROLE-MODEL-v1.md](../foundation/ATLAS-ROLE-MODEL-v1.md)).

### 2.1 Person→Organization relationships (missing)

| Proposed ID | Source person | Target org | relationship_type *(ZPM analog)* | Evidence basis *(projected)* | Status |
|-------------|---------------|------------|----------------------------------|------------------------------|--------|
| REL-SIBCAR-01 *(draft slot)* | PER-0016 *(TBD)* Карандашов | ORG-0006 | **GENERAL_DIRECTOR** | E1 EV-W1C-CC-01 §22; LE-0005 signatory | **Missing** — not authored |
| REL-SIBCAR-02 *(draft slot)* | *(TBD second person)* | ORG-0006 | **REPRESENTATIVE** | E0 operator — if second person attested | **Missing** — candidate may not exist |

**ZPM attested:** REL-ZPM-01, REL-ZPM-02 — both **active**.

**SIBCAR attested Person→Org edges:** **0**

### 2.2 Organization display pointer (missing)

| Field | ZPM value | SIBCAR value | Gap |
|-------|-----------|--------------|-----|
| ORG-0006.`primary_contact_person_id` | PER-0014 at Wave 2B | **SAFE UNKNOWN** | **Missing** — blocks contact graph parity |

Source: [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](../population/ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) §7; org register §2 omits populated field.

### 2.3 Role signal slots (missing documentation)

| Role signal | ZPM (PER-0015 / PER-0014) | SIBCAR | Gap severity |
|-------------|---------------------------|--------|--------------|
| CC director / signatory | Крюков — E1 | Карандашов — **candidate only** | **High** — identity known, not minted |
| Primary operational contact | Дубинский — E0 **yes** | **SAFE UNKNOWN** | **High** — parity gap |
| Work acceptance channel | Operator statements in EV-W2-ZPM-OP-01 | **SAFE UNKNOWN** | **High** |
| document_signatory (Person flag) | PER-0015 **yes** | Not on Person row — LE only | **Medium** — resolves at Wave 2C |
| Chief accountant (same subject) | PER-0015 (CC) | Карандашов (CC §24) — dual role | **Low** — note only |
| Diadoc / EDO signer | **SAFE UNKNOWN** (ZPM) | **SAFE UNKNOWN** | **Low** — consistent unknown |
| Beneficial owner → OWNER edge | **Excluded** (ZPM) | N/A — not on SIBCAR CC | — |

### 2.4 Explicitly excluded roles (carry forward at population)

Per ZPM Wave 2B exclusion pattern — apply at SIBCAR Wave 2C-SIBCAR relationship authoring:

| Edge | Reason | SIBCAR applicability |
|------|--------|----------------------|
| Person → ORG **OWNER** | Beneficial owner CC fact ≠ OWNER edge | CC has no beneficial-owner block — N/A |
| Person → ORG **EMPLOYEE** | Operator chooses REPRESENTATIVE family | Apply if operator confirms |
| Person ↔ Person | Wrong family | **Forbidden** |
| Person ↔ Project | Wrong wave / operator scope | **Excluded** — Waves 3–4B already attested without Person |
| Person ↔ Website / Domain | Wrong wave | **Excluded** |
| Diadoc signer relationship | **SAFE UNKNOWN** until evidence | ME-W1C-03 |

### 2.5 Wave 2C documentation pack (missing vs ZPM)

| Document | ZPM exists | SIBCAR |
|----------|------------|--------|
| Person Population | ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md | **Missing** |
| Person Register | ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md | **Missing** |
| Person Attestation plan | ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md | **Missing** |
| Person Active Attestation | ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md | **Missing** |
| Relationship Population | ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md | **Missing** |
| Relationship Register | ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md | **Missing** |
| Relationship Attestation | ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md | **Missing** |
| Operator evidence artifact | EV-W2-ZPM-OP-01 | **Missing** — EV-W2C-SIBCAR-OP-01 |

### 2.6 Downstream wave Person references (informational)

Waves 3–5 SIBCAR proceeded with Person **optional** and **independent**:

| Reference | Disposition |
|-----------|-------------|
| SU-SIBCAR-PRJ-07 | Person contacts on CC — Wave 2C optional — **No** |
| W3/W4 scope rules | No Person creation — **Pass** |
| Operational slice | Wave 2C **not on critical path** for structural stack |

**Parity note:** ZPM Waves 3–5 cite PER-0014/15 **active** as prerequisites. SIBCAR structural graph is attested **without** Person layer — intentional documented delta, not blocking retroactive Wave 2C.

### 2.7 REL-0041 commercial context (not a Person role)

REL-0041 ORG-0006 → ORG-0001 **CLIENT_OF** is attested at org↔org layer. It does **not** substitute for Person operational roles. Wave 6B register notes «project corroboration absent» at attestation time — PRJ-0011 now **active**, but commercial edge does not mint Person contacts.

---

## 3. Required operator questions

Questions required **before** Wave 2C Person Population authoring. Ordered by blocking impact.

### 3.1 Blocking (must resolve for minimal Wave 2C)

| Q ID | Question | Why required | Default if unanswered |
|------|----------|--------------|----------------------|
| **OQ-W2C-01** | Является ли **Карандашов Максим Петрович** единственным контактным лицом для операционной работы Полигон ↔ SIBCAR (аналог PER-0014 у ZPM)? | Determines single- vs two-person model | **SAFE UNKNOWN** — defer REPRESENTATIVE edge |
| **OQ-W2C-02** | Какова **точная должность** Карандашова на CC (CC §21 не содержит строку должности)? | role_signals + GENERAL_DIRECTOR qualifier | Record as «Руководитель» *(CC label only)* |
| **OQ-W2C-03** | Кто **принимает работу** / подписывает акты со стороны SIBCAR (имя + канал)? | operational_contact designation | **SAFE UNKNOWN** |
| **OQ-W2C-04** | Подтверждаете ли mint **PER-0016** *(next slot)* для Карандашова как E1 CC-backed Person? | ID assignment | Steward proposes PER-0016 — confirm no homonym conflict |

### 3.2 High priority (contact register)

| Q ID | Question | Why required |
|------|----------|--------------|
| **OQ-W2C-05** | Мобильный / рабочий телефон Карандашова или операционного контакта? | ME-W1C-04; OCPilot contact pack blocked |
| **OQ-W2C-06** | Telegram / мессенджер для операционного контакта? | ZPM contact register pattern |
| **OQ-W2C-07** | Email контактного лица (отдельно от org `info_sibcar@mail.ru`)? | Person contact row vs org email |
| **OQ-W2C-08** | Является ли `info_sibcar@mail.ru` общим ящиком или личным контактом конкретного Person? | Prevents incorrect Person↔email merge |

### 3.3 Medium priority (second person / E0 path)

| Q ID | Question | Why required |
|------|----------|--------------|
| **OQ-W2C-09** | Существует ли **отдельное** контактное лицо (не на CC), через которое ведётся ежедневная работа по PRJ-0011 / SITE-001? | ZPM two-person parity |
| **OQ-W2C-10** | Если да — ФИО, роль (зам./исп./тех. директор и т.д.), контакты? | E0 Person candidate pack |
| **OQ-W2C-11** | Есть ли доверенное лицо по доверенности (CC §25–§26 пуст)? | Additional Person candidate |

### 3.4 Low priority (EDO / documentation)

| Q ID | Question | Why required |
|------|----------|--------------|
| **OQ-W2C-12** | Кто подписант в ЭДО / Diadoc для ООО «СибКар»? | ME-W1C-03; no relationship edge until known |
| **OQ-W2C-13** | Нужно ли обновить CC (телефон, должность, EDO id) до Wave 2C? | E1 enrichment vs E0 operator path |
| **OQ-W2C-14** | Подтверждаете ли **single-person model** (Карандашов = signatory + primary contact)? | Closes parity decision vs ZPM two-person |

---

## 4. Recommended Wave 2 population sequence

**Discovery-only recommendation** — sequence for **future** steward execution after operator answers. **Not authorized** by this audit package.

### 4.1 Prerequisites (already met)

| Gate | Status | Authority |
|------|--------|-----------|
| ORG-0006 **active** | **Met** | AT-W1C-01 |
| LE-0005 **active** | **Met** | AT-W1C-01 |
| CC present EV-W1C-CC-01 | **Met** | Evidence Verification |
| Wave 1C duplicate review | **Met** | W1C-D-01..06 |
| Org endpoint for Person intake | **Met** | Org register §9 **Unblocked** |

### 4.2 Recommended sequence

```text
Phase A — Discovery (THIS PACKAGE)
    │
    ├─► Operator answers OQ-W2C-01..14
    ├─► Capture EV-W2C-SIBCAR-OP-01 (operator mission inputs)
    └─► Steward discovery sign-off
    │
    ▼
Phase B — Wave 2C Person Population (authoring — NOT THIS TASK)
    │
    ├─► Evidence pre-check: EV-W1C-CC-01 + EV-W2C-SIBCAR-OP-01
    ├─► Duplicate batch W2C-SIBCAR-D-01..N vs PER-0001..0015
    ├─► Author ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md
    ├─► Author ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md
    └─► Author ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md
    │
    ▼
Phase C — Person Active Attestation
    │
    ├─► AT-W2C-SIBCAR-01: PER-0016 Карандашов (E1 CC signatory) — FIRST
    └─► AT-W2C-SIBCAR-02: second E0 person — ONLY IF OQ-W2C-09 affirmed
    │
    ▼
Phase D — Wave 2C-SIBCAR Relationship Population (2B analog)
    │
    ├─► Author relationship population / register / attestation docs
    ├─► REL-SIBCAR-01: PER-0016 → ORG-0006 GENERAL_DIRECTOR (projected)
    ├─► REL-SIBCAR-02: E0 person → ORG-0006 REPRESENTATIVE — IF second person attested
    └─► Set ORG-0006.primary_contact_person_id at relationship attestation
    │
    ▼
Phase E — Documentation sync (post-population — future)
    │
    ├─► SIBCAR slice consistency audit (Person tranche)
    ├─► Backup / integrity snapshot refresh
    └─► Optional: org register sync (ZPM-C-01 pattern)
```

### 4.3 Attestation ordering rules (ZPM precedent)

1. CC signatory Person **before** E0 operational-contact Person (AT-W2-ZPM-01 before AT-W2-ZPM-02).
2. Person→Organization edges **only** in separate relationship pass **after** all in-scope Person endpoints **active**.
3. `primary_contact_person_id` set at relationship attestation — not at Person-only act.
4. No Person↔Project / Person↔Website retroactive edges without explicit new wave scope.

### 4.4 Model decision tree

| Operator answer OQ-W2C-01 / OQ-W2C-14 | Recommended mint |
|---------------------------------------|------------------|
| Single-person: Карандашов = signatory + primary contact | PER-0016 only; REL-SIBCAR-01 GENERAL_DIRECTOR; `primary_contact_person_id` = PER-0016 |
| Two-person: separate operational contact named | PER-0016 + PER-0017; REL-SIBCAR-01 + REL-SIBCAR-02; `primary_contact_person_id` = operational contact |
| Operational contact **SAFE UNKNOWN** after inquiry | PER-0016 only (minimal); `primary_contact_person_id` **SAFE UNKNOWN** or PER-0016 with steward note |

---

## 5. Parity check results

| Check | ZPM reference | SIBCAR | Result |
|-------|---------------|--------|--------|
| **P-01** | Person entity count ≥ 1 CC-backed | 0 minted; 1 candidate | **Fail** — expected pre-Wave 2C |
| **P-02** | Person→Org edge count ≥ 1 | 0 | **Fail** |
| **P-03** | primary_contact_person_id populated | SAFE UNKNOWN | **Fail** |
| **P-04** | Wave 2 doc pack complete | 0 files | **Fail** |
| **P-05** | Operator evidence artifact | EV-W2-ZPM-OP-01 | **Fail** — missing |
| **P-06** | ORG endpoint active before Person | AT-W1C-01 | **Pass** |
| **P-07** | CC person line on file | EV-W1C-CC-01 §22 | **Pass** |
| **P-08** | Structural stack without Person allowed | Documented optional | **Pass** — intentional delta |
| **P-09** | Duplicate review before Person mint | Pending W2C batch | **Partial** |
| **P-10** | REL-0041 does not imply Person | Org↔org only | **Pass** |

**Overall parity vs ZPM Person layer:** **Not met** — discovery preparation identifies gaps; structural SIBCAR stack (PRJ-0011, WEB-SIBCAR-01, REL-0041) **does not** depend on Person completion.

---

## 6. Findings register

| ID | Severity | Topic | Remediation |
|----|----------|-------|-------------|
| **SIBCAR-W2D-01** | **High** | Zero attested Person entities for ORG-0006 | Execute Wave 2C after operator Q&A |
| **SIBCAR-W2D-02** | **High** | No Person→Organization operational edges | Wave 2C-SIBCAR relationship pass |
| **SIBCAR-W2D-03** | **High** | `primary_contact_person_id` unset on ORG-0006 | Set at relationship attestation |
| **SIBCAR-W2D-04** | **High** | No EV-W2C-SIBCAR-OP-01 operator mission pack | Operator session — OQ-W2C-01..14 |
| **SIBCAR-W2D-05** | **Medium** | Single CC person vs ZPM two-person model undecided | OQ-W2C-01, OQ-W2C-14 |
| **SIBCAR-W2D-06** | **Medium** | Signatory exact title SAFE UNKNOWN on CC | OQ-W2C-02 |
| **SIBCAR-W2D-07** | **Medium** | Person-level contacts absent (phone, TG, email) | OQ-W2C-05..08; ME-W1C-04 |
| **SIBCAR-W2D-08** | **Low** | Wave 2C doc pack not authored (7 files) | Phase B authoring |
| **SIBCAR-W2D-09** | **Low** | Duplicate review W2C-SIBCAR-D-* pending | Pre-attestation batch |
| **SIBCAR-W2D-10** | **Info** | Waves 3–5 marked Person optional — doc drift vs ZPM prerequisite language | Accept or sync downstream docs post-Wave 2C |
| **SIBCAR-W2D-11** | **Info** | ATLAS-COVERAGE-AUDIT-v1 § SIBCAR stale on Person count | Refresh on Person attestation |
| **SIBCAR-W2D-12** | **Info** | DOM-SIBCAR-01 still **proposed** — orthogonal to Person wave | Wave 5 attestation separate |

---

## 7. Audit verdict

```text
READY FOR OPERATOR DISCOVERY SESSION
```

SIBCAR Person discovery inventory is **complete at documentation level**. One E1 CC-backed candidate (Карандашов М.П.) is queued; operational-role parity with ZPM **requires** operator inputs and future Wave 2C authoring. **No population authorized** by this package.

**Next steward action:** Collect operator answers (§3); record **EV-W2C-SIBCAR-OP-01**; proceed to Phase B authoring when model decision (single- vs two-person) is confirmed.

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md) | Point-in-time discovery register |
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-SUMMARY-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-SUMMARY-v1.md) | Executive summary |
| [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](../population/ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) | Parity reference |
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md](../population/ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md) | Operational roles reference |
| [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](../population/ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | CC person lines |
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](../population/ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | Org anchor + Wave 2C queue |

---

*ATLAS SIBCAR Wave 2 Person Discovery Audit v1 — audit only; no population.*
