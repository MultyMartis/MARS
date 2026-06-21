# ATLAS SIBCAR Evidence Verification v1

**Status:** **documented** — evidence-first verification package for Wave 1C SIBCAR intake.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md)  
**Is not:** attestation execution, registry mutation, runtime, API, database.

---

# REPORT — ATLAS SIBCAR Evidence Verification

**Verification date:** 2026-06-06  
**Evidence root:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\`  
**Compare targets:** ORG-0006 *(proposed)*, LE-0005 *(proposed)*; cross-check ORG-0005 / LE-0004 (BZPM)  
**Governance:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)

---

## 1. Evidence inventory

| # | File | Path | Format | Size | Last modified | Role |
|---|------|------|--------|------|---------------|------|
| 1 | `Реквизиты.docx` | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | DOCX | 74 779 bytes | 2026-04-04 22:11 | Counterparty Card — enterprise card («Карточка предприятия») with full legal requisites |

**Inventory notes:**

- **One file** in folder; no PDF, TXT, or secondary corroboration in the same folder.
- Document title (extracted): **«Карточка предприятия»**.
- **Evidence ref assigned:** `EV-W1C-CC-01`
- **Tier at human review:** **E1** — structured identifiers (INN, KPP, OGRN), legal name (RU/EN), addresses, bank, signatory, OKVED.

**Prior population state:** [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) **COR-W1B-05** reserved SIBCAR identity for **own** CC intake — this package fulfills that path.

---

## 2. Extracted organization facts

Source: **EV-W1C-CC-01** only. Fields absent in CC → **SAFE UNKNOWN** (no inference).

| Field | Value | CC section |
|-------|-------|------------|
| **Legal entity form** | Общество с ограниченной ответственностью (ООО) | §2–§4 |
| **Legal name (full, RU)** | Общество с ограниченной ответственностью «СибКар» | §4 |
| **Legal name (short, RU)** | ООО «СибКар» | §2, §6 |
| **Legal name (full, EN)** | Limited Liability Company «SibCar» | §8 |
| **Legal name (short, EN)** | LLC «SibCar» | §10 |
| **INN** | 5405512542 | §18 |
| **KPP** | 540501001 | §18 |
| **OGRN** | 1265400004220 | §20 |
| **Registration date** | **SAFE UNKNOWN** — not stated in CC | — |
| **Tax system** | УСН Доходы 6% | §39 |
| **OKVED (primary)** | 45.11 — Торговля легковыми автомобилями и грузовыми автомобилями малой грузоподъемности | §36–§37 |
| **Region** | Новосибирская область | §12 |
| **Legal address** | 630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11 | §12 |
| **Actual address** | 630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11 | §14 |
| **Postal address** | **SAFE UNKNOWN** — not separate in CC | — |
| **EDO operator / participant id** | **SAFE UNKNOWN** — not stated in CC | — |
| **Websites** | **SAFE UNKNOWN** — not stated in CC | — |
| **Domains (explicit)** | **SAFE UNKNOWN** — no corporate domain field; email uses `@mail.ru` | §16 |
| **Email** | info_sibcar@mail.ru | §16 |
| **Phone / fax** | **SAFE UNKNOWN** — not stated in CC | — |
| **Signatory (руководитель)** | Карандашов Максим Петрович | §21–§22 |
| **Signatory title (exact)** | **SAFE UNKNOWN** — CC lists «Руководитель (должность, ФИО)» but omits explicit должность string | §21 |
| **Chief accountant** | Карандашов Максим Петрович | §23–§24 |
| **Authorized representative (power of attorney)** | — *(none listed)* | §25–§26 |
| **Bank** | АО «ТБанк» | §28 |
| **Settlement account** | 40702810410002059263 | §34 |
| **BIC** | 044525974 | §30 |
| **Correspondent account** | 30101810145250000974 | §32 |

**Strings searched in CC (absent):** `BZPM`, `bzpm`, `ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ`, `2221237587`, `Triumph`, `Триумф`, `Полигон`, `MetaCode`, `МетаКод`, `i-SEO`, `Автосалон` *(as trade-name string)*.

---

## 3. Legal entity analysis

### 3.1 Proposed LE-0005

| Field | Value | Evidence |
|-------|-------|----------|
| **legal_entity_id** | LE-0005 *(proposed)* | Next slot after LE-0004 (BZPM) |
| **legal_entity_name** | Общество с ограниченной ответственностью «СибКар» | EV-W1C-CC-01 §4 |
| **entity_type** | ООО | EV-W1C-CC-01 §2–§4 |
| **inn** | 5405512542 | EV-W1C-CC-01 §18 |
| **kpp** | 540501001 | EV-W1C-CC-01 §18 |
| **ogrn_ogrnip** | 1265400004220 | EV-W1C-CC-01 §20 |
| **legal_address** | 630124, Новосибирская область, г Новосибирск, ул Доватора, д. 11 | EV-W1C-CC-01 §12 |
| **document_signatory** | Карандашов Максим Петрович | EV-W1C-CC-01 §22 |
| **lifecycle** | **proposed** | Population layer — attestation pending |

**Readiness:** Critical legal-entity fields present on E1 CC — **proposed** binding to ORG-0006 is **supported**; **active** LE attestation requires steward act per [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md).

---

## 4. Identity analysis

### 4.1 Canonical organization name

| Candidate | Evidence class | Verdict |
|-----------|----------------|---------|
| **SIBCAR** | Operator folder slug `sibcar\`; CC English «SibCar» | **Recommended canonical_name** for ORG-0006 — aligns with CC Latin stem |
| **СибКар** | CC short RU legal name ООО «СибКар» | **Supported alias** — same legal subject |
| **ООО «СибКар»** | CC legal short name | **Legal display form** — bind via LE-0005, not duplicate org |
| **Автосалон СИБКАР** | OCPilot [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) site title only | **Not attested alias** — string absent from CC; EFV-01 prohibits alias register entry without CC quote |

### 4.2 Questions (evidence-only)

| Question | Answer | Basis |
|----------|--------|-------|
| **Is SIBCAR identical to BZPM?** | **No** | EV-W1C-CC-01 INN 5405512542, OGRN 1265400004220, legal name «СибКар», Novosibirsk vs EV-W1B-CC-01 INN 2221237587, OGRN 1172225049787, «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ», Barnaul |
| **Is SIBCAR a separate organization from BZPM?** | **Yes** | Distinct legal identifiers — separate ORG-0006 / LE-0005 vs ORG-0005 / LE-0004 |
| **Evidence for alias equivalence SIBCAR ↔ BZPM?** | **None** | No shared INN/OGRN; no cross-mention in either CC |
| **Is SIBCAR identical to Triumph?** | **No** | ORG-0004 attested separately; no Triumph strings or shared identifiers in EV-W1C-CC-01 |
| **Is SIBCAR identical to Polygon / MetaCode / i-SEO?** | **No** | Operator orgs ORG-0001..0003; no shared identifiers in CC |

### 4.3 Relationship to prior Wave 1B inference

[ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) **COR-W1B-01..05** split BZPM and SIBCAR. **EV-W1C-CC-01 confirms** that correction: SIBCAR is an independent legal subject suitable for **ORG-0006**, not an alias on ORG-0005.

**Relationship ORG-0005 ↔ ORG-0006:** **SAFE UNKNOWN** — no commercial, ownership, or alias bridge cited in either CC ([COR-W1B-06](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md)).

---

## 5. Duplicate review

### 5.1 Compare EV-W1C-CC-01 to attested / proposed registry

| Attribute | ORG-0006 / LE-0005 (proposal) | EV-W1C-CC-01 | Match |
|-----------|-------------------------------|--------------|-------|
| **legal_name** | ООО «СибКар» / ООО «СибКар» full form | §2, §4 | **Match** |
| **INN** | 5405512542 | §18 | **Match** |
| **KPP** | 540501001 | §18 | **Match** |
| **OGRN** | 1265400004220 | §20 | **Match** |
| **Region** | Novosibirsk | §12 | **Match** |

### 5.2 Duplicate review matrix

| Review ID | Pair | Verdict | Reason |
|-----------|------|---------|--------|
| **W1C-D-01** | SIBCAR vs BZPM (ORG-0006 vs ORG-0005) | **Distinct — Pass** | INN 5405512542 ≠ 2221237587; legal names unrelated |
| **W1C-D-02** | SIBCAR vs Triumph (ORG-0006 vs ORG-0004) | **Distinct — Pass** | No identifier collision in CC |
| **W1C-D-03** | SIBCAR vs Polygon / MetaCode / i-SEO | **Distinct — Pass** | Operator orgs — no CC overlap |
| **W1C-D-04** | SIBCAR vs SITE-001 | **Class boundary — Pass** | SITE-001 = OCPilot site_id / future Website; ORG-0006 = legal counterparty |
| **W1C-D-05** | «Автосалон СИБКАР» site title vs CC legal name | **Open — low** | OKVED 45.11 supports auto-trade industry; site title not CC alias — disambiguation note at Website intake |
| **W1C-D-06** | D1 unresolved duplicate | **None** | No second CC with conflicting identifiers |

### 5.3 Cross-registry INN check

| Registry slice | INN 5405512542 | Result |
|----------------|----------------|--------|
| Wave 1 dataset ORG-0001..0004 | Not attested in repo markdown extracts | **No collision** *(documentation-level)* |
| ORG-0005 / LE-0004 (BZPM) | 2221237587 | **Distinct** |
| EV-W1C-CC-01 | 5405512542 | **Primary key for ORG-0006** |

---

## 6. Attestation readiness (verification slice)

| Gate | Status | Notes |
|------|--------|-------|
| CC present (EFV-04) | **Pass** | EV-W1C-CC-01 |
| Legal name + INN + OGRN on CC | **Pass** | §4, §18, §20 |
| Alias evidence discipline (EFV-01) | **Pass** | CC-backed aliases only |
| Duplicate review before merge claims | **Pass** | W1C-D-01..06 |
| Steward **active** attestation act | **Pending** | Human gate — [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md) |

---

## 7. Interpretation

Counterparty Card **EV-W1C-CC-01** establishes a **distinct legal organization** — ООО «СибКар» (INN 5405512542, OGRN 1265400004220) — for the `sibcar/` evidence folder.

- **SIBCAR ≠ BZPM** — proven by non-overlapping legal identifiers and legal names across CCs.
- **SIBCAR ≠ Triumph, Polygon, MetaCode, i-SEO** — no evidence of identity merge.
- **ORG-0006 / LE-0005** — appropriate proposed identifiers (next after ORG-0005 / LE-0004).

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) | Population plan + REPORT |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) | Register row |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-ATTESTATION-v1.md) | Attestation sequence |
| [ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md](ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md) | BZPM CC compare baseline |

---

*ATLAS SIBCAR Evidence Verification v1 — documentation only.*
