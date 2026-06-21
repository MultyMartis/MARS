# ATLAS Wave 1B BZPM Evidence Verification v1

**Status:** **documented** — evidence-first verification and correction package.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** attestation execution, registry mutation, runtime, API, database.

---

# REPORT — ATLAS BZPM Evidence Verification

**Verification date:** 2026-06-06  
**Evidence root:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\`  
**Compare targets:** ORG-0005, LE-0004  
**Governance:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) (new)

---

## 1. Evidence inventory

| # | File | Path | Format | Size | Last modified | Role |
|---|------|------|--------|------|---------------|------|
| 1 | `Реквизиты.docx` | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx` | DOCX | 15 762 bytes | 2025-12-02 13:30 | Counterparty Card — auction participant questionnaire with full legal requisites |

**Inventory notes:**

- **One file** in folder; no PDF, TXT, or secondary corroboration in the same folder.
- Document title (extracted): **«Анкета Участника аукциона»** / **«Сведения об Участнике»**.
- **Evidence ref assigned:** `EV-W1B-CC-01`
- **Tier at human review:** **E1** — structured identifiers (INN, KPP, OGRN), legal name, addresses, bank, signatory.

**Prior population state:** Wave 1B packages recorded **ME-W1B-01** (CC missing). That marker is **obsolete** — CC exists; verification proceeded per operator report.

---

## 2. Extracted organization facts

Source: **EV-W1B-CC-01** only. Fields absent in CC → **SAFE UNKNOWN** (no inference).

| Field | Value | CC section |
|-------|-------|------------|
| **Legal entity form** | Общество с ограниченной ответственностью (ООО) | §1 |
| **Legal name (full)** | Общество с ограниченной ответственностью «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | §1 |
| **Legal name (short)** | Общество с ограниченной ответственностью «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | §2 |
| **INN** | 2221237587 | §3, §23 |
| **KPP** | 222101001 | §3, §23 |
| **OGRN** | 1172225049787 | §3, §23 |
| **Registration date** | 22.12.2017 | §4 |
| **Tax system** | Общая, НДС 20% | §5 |
| **OKPO** | 14705112 | §6 |
| **OKTMO** | 01701000 | §12 |
| **Region** | Алтайский край | §7 |
| **Legal address** | 656011, Россия, г. Барнаул, пр-т Калинина, 15в, оф. 110 | §8 |
| **Registration address** | 656011, Россия, г. Барнаул, пр-т Калинина, 15в, оф. 110 | §9 |
| **Postal address** | 656011, Россия, г. Барнаул, пр-т Калинина, 15в, оф. 110 | §10 |
| **Actual address** | 656011, Россия, г. Барнаул, пр-т Калинина, 15в, оф. 110 | §11 |
| **Production site address** | 656011, Россия, г. Барнаул, пр-т Калинина, 15в | §13 |
| **Warehouse address** | 656011, Барнаул, пр-т Калинина, 15в; также г. Москва, ул. Басовская 14с2 | §14 |
| **EDO operator / participant id** | **SAFE UNKNOWN** — not stated in CC | — |
| **Websites** | **Bzpm.ru** | §17 |
| **Domains (explicit)** | **bzpm.ru** (from website field; registrant not in CC) | §17 |
| **Email** | zakaz@bzmp.ru | §17, §18 |
| **Phone / fax** | +7 (3852) 72-18-90 | §17 |
| **Signatory (director)** | Директор Крюков Александр Сергеевич | §19, §24 |
| **Beneficial owner** | Крюков Александр Сергеевич, ИНН 222304520613 (100%) | §20 |
| **Chief accountant / responsible** | Крюков Александр Сергеевич | §21–§22 |
| **Bank** | ПАО Сбербанк, Алтайское отделение № 8644, г. Барнаул | §23 |
| **Settlement account** | 40702810802000017761 | §23 |
| **BIC** | 040173604 | §23 |
| **Correspondent account** | 30101810200000000604 | §23 |

**Strings searched in CC (absent):** `SIBCAR`, `СИБКАР`, `Автосалон`, `sibcar`, `автосалон`, `OpenCart`, `ocStore`.

**CC email note:** CC lists `zakaz@bzmp.ru` (typo **bzmp** vs **bzpm** in domain) — recorded as-is; no correction applied.

---

## 3. Identity analysis

### 3.1 Questions (evidence-only)

| Question | Answer | Basis |
|----------|--------|-------|
| **Is BZPM identical to SIBCAR?** | **No** — not supported by CC | EV-W1B-CC-01: legal subject is OOO «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ»; website **Bzpm.ru**; **no** SIBCAR/автосалон strings |
| **Is BZPM a separate organization?** | **Yes** — CC defines a distinct legal person (INN 2221237587) suitable for ORG-0005 / LE-0004 binding | EV-W1B-CC-01 §3 |
| **Evidence for alias equivalence BZPM ↔ SIBCAR?** | **None** in CC | Absence of SIBCAR-family strings; no second INN; no trade-name bridge |

### 3.2 BZPM operator codename vs CC subject

| Name | Evidence class | Verdict |
|------|----------------|---------|
| **BZPM** (operator / folder slug) | Corroborated **indirectly** by CC website **Bzpm.ru** | **Plausible link** to same legal subject — **not** to SIBCAR |
| **ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ»** | CC legal name | **Primary legal identity** for LE-0004 |
| **SIBCAR / Автосалон СИБКАР / СИБКАР** | OCPilot [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) — **Website/project context only** | **Must not** merge into ORG-0005 without separate CC ([COR-W1B-03](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md)) |

### 3.3 Prior inference rejected

Wave 1B population inferred from EAR docs + SITE-001 that BZPM and SIBCAR are **one Organization**. That inference used **project naming**, not CC. CC review **refutes** the alias-cluster claim.

---

## 4. Duplicate review

### 4.1 Compare extracted CC to ORG-0005 / LE-0004 proposals

| Attribute | ORG-0005 / LE-0004 (prior proposal) | EV-W1B-CC-01 | Match |
|-----------|--------------------------------------|--------------|-------|
| **org_id** | ORG-0005 | — | N/A |
| **canonical_name** | BZPM | Bzpm.ru (website) | Partial — codename vs domain stem |
| **legal_entity_id** | LE-0004 | — | Binding target |
| **legal_name** | SAFE UNKNOWN | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | **Mismatch with empty proposal; CC fills LE-0004** |
| **INN** | SAFE UNKNOWN | 2221237587 | **CC provides value** |
| **KPP** | SAFE UNKNOWN | 222101001 | **CC provides value** |
| **OGRN** | SAFE UNKNOWN | 1172225049787 | **CC provides value** |
| **Proposed aliases** | SIBCAR, Автосалон СИБКАР, СИБКАР | **Absent in CC** | **Conflict — aliases unsupported** |
| **Industry / activity (narrative)** | Dealership / OpenCart (from project docs) | Food machinery plant (legal name) | **Narrative conflict** — CC controls legal identity |

### 4.2 Duplicate review matrix (reopened)

| Review ID | Pair | Prior verdict | **Corrected verdict** | Reason |
|-----------|------|---------------|----------------------|--------|
| **W1B-D-01** | BZPM / SIBCAR / СИБКАР | Pass (alias cluster) | **Fail — reopened** | CC lacks SIBCAR; different legal narrative |
| **W1B-D-02** | BZPM vs Triumph | Pass | **Pass** | Unchanged — distinct clients |
| **W1B-D-03** | SIBCAR vs Triumph aliases | Pass | **Pass** | Unchanged |
| **W1B-D-04** | SITE-001 vs ORG-0005 | Pass (class boundary) | **Pass** | Unchanged |
| **W1B-D-05** | Dealership homonym | Open — low | **Open** | CC suggests non-dealership legal subject — homonym risk **increased** for SIBCAR name |

### 4.3 Cross-registry INN check

Wave 1 dataset organizations (ORG-0001..0004): **no** row with INN 2221237587 in repo-attested Wave 1 xlsx path. **No duplicate INN** in attested Wave 1 org set (documentation-level check; full xlsx not re-parsed in this pass).

---

## 5. Correction actions

| Action | Artifact | Status |
|--------|----------|--------|
| Identity correction record | [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) | **Created** |
| Governance safeguard | [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) | **Created** |
| Revoke SIBCAR alias cluster on ORG-0005 | COR-W1B-01 | **Documented** — steward register update pending |
| Downgrade W1B-D-01 | COR-W1B-02 | **Documented** |
| Bind LE-0004 from CC | COR-W1B-04 | **Documented** — attestation still required for **active** |
| Prior population packages | ATLAS-WAVE1B-BZPM-ORGANIZATION-* v1 | **Not edited** — correction by supersession pointer (no Foundation change) |

---

## 6. New governance rule

**Document:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)

| Rule ID | Requirement |
|---------|-------------|
| **EFV-01** | No alias creation without evidence |
| **EFV-02** | No organization merge from project context |
| **EFV-03** | No organization equivalence from website/project naming |
| **EFV-04** | Counterparty Card overrides assumptions |
| **EFV-05** | Evidence review mandatory before duplicate conclusions |
| **EFV-06** | Identity decisions require cited evidence source |

**Stop conditions:** STOP-EFV-01..04 in rule document.

---

## 7. Impact assessment on ORG-0005 / LE-0004

### ORG-0005

| Aspect | Impact |
|--------|--------|
| **lifecycle_state** | Remains **proposed** — CC present but identity correction must precede **active** attestation |
| **canonical_name BZPM** | **Review recommended** — CC supports **Bzpm.ru** / food-machinery legal subject, not dealership narrative |
| **Aliases SIBCAR / Автосалон СИБКАР / СИБКАР** | **Revoke** (COR-W1B-01) — unsupported by CC |
| **W1-B CLIENT role** | **Unchanged** at class level — still external client candidate |
| **ME-W1B-01** | **Cleared** (CC found) — replaced by correction gate |
| **ME-W1B-02** | **Partially cleared** — INN/KPP/OGRN now known from CC; **active** LE still needs attestation |
| **Downstream Waves 2B / 3 / 4 / 6+** | **Still blocked** on ORG-0005 **active** + corrected identity register |

### LE-0004

| Field | Prior | After CC review |
|-------|-------|-----------------|
| **legal_name** | SAFE UNKNOWN | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» *(proposed from CC)* |
| **INN** | SAFE UNKNOWN | 2221237587 |
| **KPP** | 222101001 | 222101001 |
| **OGRN** | SAFE UNKNOWN | 1172225049787 |
| **lifecycle_state** | proposed | **proposed** — attestation not executed in this pass |
| **org binding** | ORG-0005 | ORG-0005 — **unchanged id link** |

### SIBCAR (not ORG-0005)

| Aspect | Status |
|--------|--------|
| Legal identity | **SAFE UNKNOWN** — no CC in `sibcar/` or equivalent folder |
| Relation to ORG-0005 | **SAFE UNKNOWN** — **no merge** |
| SITE-001 | Remains **Website/project** context until separate org intake |

---

## 8. Final verdict

### **EVIDENCE FOUND — BZPM SEPARATE ORGANIZATION**

**Interpretation:** Counterparty Card **EV-W1B-CC-01** establishes a **distinct legal organization** (ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ», INN 2221237587) for the `bzpm/` evidence folder. **BZPM is not identical to SIBCAR.** **No evidence** supports alias equivalence between BZPM (CC-backed legal subject) and SIBCAR / Автосалон СИБКАР (project/site naming only).

**Not selected:**

| Verdict | Why excluded |
|---------|--------------|
| NO EVIDENCE FOUND | CC exists and was reviewed |
| EVIDENCE FOUND — ALIAS CONFIRMED | CC contains no SIBCAR-family identifiers; alias cluster refuted |

---

## UNKNOWN / risks

| Signal | Detail |
|--------|--------|
| **UNKNOWN** | Whether operator engagement on SITE-001 (OpenCart) is commercially tied to OOO ЗПМ or to a **different** undisclosed legal entity — **no CC for SIBCAR** |
| **UNKNOWN** | Production registrant for `sibcar.*` domains |
| **UNKNOWN** | EDO participation for OOO ЗПМ |
| **SECURITY RISK** | None identified in repo from this pass — CC stored outside git as intended |

---

## Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) | Binding corrections |
| [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) | Future safeguard |
| [ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md) | Prior package (partially superseded) |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | Storage pointer |

---

*ATLAS Wave 1B BZPM Evidence Verification v1 — documentation only.*
