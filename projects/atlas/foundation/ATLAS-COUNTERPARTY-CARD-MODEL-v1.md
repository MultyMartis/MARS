# ATLAS Counterparty Card Model v1

**Status:** **documented** — Phase 9 dedicated organization acquisition source (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-POPULATION-EXECUTION-PLAN-v1.md](ATLAS-POPULATION-EXECUTION-PLAN-v1.md) · [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md) · [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md)  
**Companion:** [ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) · [OPS-ATLAS-ALIGNMENT-v1.md](OPS-ATLAS-ALIGNMENT-v1.md)  
**Is not:** OCR specification, DMS design, card template library, automated extraction rules, storage schema.

**Phase 1–8 constraint:** Introduces Counterparty Card without modifying E0–E3 tier definitions. Card maps to existing tiers at human review.

---

## 1. Purpose

Define **Counterparty Card** as the **preferred source of organization reality** for ATLAS population — what it is, what may be extracted, what must never be inferred, and how it flows through evidence → proposal → review → attestation.

**Normative statement:**

> A **Counterparty Card** is a **business reality evidence artifact** describing a counterparty organization for structural identification — not a contract, invoice, or operational workflow object.

---

## 2. What a Counterparty Card is

### 2.1 Definition

A **Counterparty Card** (CC) is a **human-readable artifact** that consolidates **identifying and contact information** about a business counterparty, typically prepared for accounting, CRM, or partner onboarding — **outside** ATLAS contract and project-report domains.

| Property | Rule |
|----------|------|
| **Subject** | One primary organization per card (may list branches in notes) |
| **Intent** | Identify **who the business is** — not **what work was done** |
| **Provenance** | Issued by counterparty, operator, bank, EDO system, or steward compilation |
| **ATLAS role** | **Evidence** for Organization proposal — not canonical record itself |
| **Storage** | `evidence_ref` pointer — full card not required inside ATLAS |

### 2.2 What a Counterparty Card is not

| Artifact | Why excluded from CC model |
|----------|---------------------------|
| **Contract** | Legal agreement — OPS / legal domain; may corroborate only |
| **Act of acceptance** | Operational delivery proof |
| **Invoice** | Financial transaction artifact |
| **Technical specification** | Project/delivery document |
| **Project report** | Operational narrative |
| **CRM export row** | System import — separate intake path (E3 + review) |
| **SERP / MIG pack** | Market evidence — proposal support only (AT-E-03) |

**CC-B-01:** Labeling a contract PDF as "counterparty card" does **not** make it a CC — boundary review rejects misclassification.

### 2.3 Execution chain (reaffirmed)

```text
Counterparty Card → Evidence → Proposal → Review → Attestation → Organization Registry
```

---

## 3. Accepted formats

| Format | Acceptability | Notes |
|--------|---------------|-------|
| **PDF** | **Preferred** | Scanned or exported registrar/card PDF |
| **DOCX** | **Accepted** | Steward-compiled or partner-provided |
| **XLSX** | **Accepted** | Often CRM/accounting export — treat as CC only if card-shaped (one org profile), not bulk sheet |
| **Image** (PNG, JPG, HEIC) | **Accepted** | Photo of printed card; higher extraction error risk |
| **Plain text** | **Accepted** | Messenger or email paste — typically E1 |
| **Email body** | **Accepted** | When structured as org profile, not thread narrative |

**CC-FMT-01:** Format does **not** determine evidence tier — **content quality and provenance** do, at human review.

**CC-FMT-02:** Bulk spreadsheets with hundreds of rows are **import proposals** (E3 path) — not single CC intake. Split or reject at intake.

---

## 4. Evidence status

### 4.1 Tier mapping at review

Counterparty Cards map to existing tiers — **no new tier introduced**.

| Card profile | Typical tier | Active attest implication |
|--------------|--------------|---------------------------|
| Steward-compiled from operator knowledge | **E0** | Operator core org — steward attest sufficient |
| Informal text/messenger/email card | **E1** | External org — proposed → review → active |
| Formal registrar/bank/EDO card with identifiers | **E1–E2** | Strong existence proof; merge disputes may need E2 |
| Card + consumer system corroboration | **E1 + E3** | Import triage — human promote required |

**CC-EV-01:** Card presence does **not** auto-assign tier — steward assigns at review.

**CC-EV-02:** Fabricated or edited card without disclosure = governance violation (AT-E-05).

### 4.2 Evidence package contents (conceptual)

| Element | Required |
|---------|----------|
| `evidence_ref` to card artifact | Yes |
| Card format note | Yes |
| Intake date | Yes |
| Provenance (who provided) | Yes |
| Extraction log (what fields were read) | Recommended |
| Known gaps / illegible sections | Yes if any |

---

## 5. Extractable information

### 5.1 Field classes

| Field | May extract to proposal? | Active attest note |
|-------|--------------------------|-------------------|
| **Legal name** (полное наименование) | Yes | Core identity — duplicate review mandatory |
| **Short / trade name** | Yes → alias candidate | Alias model — not second org |
| **INN** | Yes | High-trust identifier when visually verified |
| **KPP** | Yes | Branch disambiguation — review if multi-KPP |
| **OGRN / ОГРНИП** | Yes | Strong existence signal |
| **Legal address** | Yes | Review branch vs legal seat |
| **Postal address** | Yes | Optional metadata |
| **Director / CEO name** | Yes → **proposed Person** link | Requires human review — CC-PER-01 |
| **Contact persons** (name + role) | Yes → **proposed Person** | No auto-active from card |
| **Phone / email** | Yes → contact metadata | Not Person alone — homonym risk |
| **EDO operator** (Контур, СБIS, etc.) | Yes | Business reality identifier — see §6 |
| **EDO participant id** | Yes | Pair with EDO operator |
| **Bank name / BIK** | Yes → optional metadata | OPS requisites alignment — not standalone entity |
| **Settlement account** | Yes → optional metadata | Sensitive — attest caution; OPS primary use |
| **OKVED / activity text** | Yes → descriptive metadata | Not taxonomy expansion |
| **Website URL on card** | Yes → **proposed Website** (Wave 4) | Not Wave 1 org shortcut |

### 5.2 EDO as business reality

**Decision A3 (normative):**

> **EDO operator and participant identifier** on a Counterparty Card are **business reality** — they identify **how the organization participates in electronic document exchange** as a structural fact, analogous to INN for registry identification.

| Aspect | Ruling |
|--------|--------|
| Stored as | Optional attested metadata on Organization (future field expansion) or proposal note until expansion |
| Not stored as | OPS workflow state, invitation status, document queue |
| Evidence | CC line or registrar extract — E1+ |
| Review | Confirm EDO id matches INN/OGRN subject — mismatch → disputed |

**CC-EDO-01:** EDO metadata does **not** imply CLIENT_OF, VENDOR_OF, or contract existence.

---

## 6. Review expectations

### 6.1 Intake review checklist

| Check | Action if fail |
|-------|----------------|
| Is artifact actually a CC (not contract/invoice)? | Reject or reclassify |
| Single org subject? | Split multi-org cards |
| Readable critical fields? | Defer — note illegibility |
| Duplicate signals (INN, name)? | Duplicate review D1 |
| Homonym risk? | Disambiguation note required |

### 6.2 Evidence review

| Check | Action |
|-------|--------|
| Tier appropriate for target class and wave | Adjust or defer |
| Extracted fields match visual card | Fix proposal — never silent drift |
| Conflicts with existing active org | Disputed or merge path |
| Missing INN/OGRN for external org | Remain **proposed** — CC-INC-01 |

### 6.3 Fields requiring human review (Decision A6)

**Always human-reviewed before active attest:**

- Director name → Person identity and REPRESENTATIVE/OWNER edge
- All contact persons and role labels
- Trade name vs legal name (alias vs duplicate org)
- EDO operator + id pair
- Address(es) — legal vs actual vs branch
- Any inferred commercial relationship (client, vendor, partner)
- Bank details (accuracy + scope — OPS overlap)
- Multi-card field conflicts

**May proceed to active org attest without separate Person attest:**

- Legal name, INN, KPP, OGRN (when verified on card)
- EDO identifiers (when consistent with other fields)
- Legal address (when unambiguous)

---

## 7. Attestation implications

| Outcome | Meaning |
|---------|---------|
| **Org → active** | Steward/owner attests Organization exists; card supports tier |
| **Fields → active metadata** | Only fields explicitly reviewed and attested |
| **Person → proposed** | Director/contacts extracted but **not** active until Person wave |
| **Relationship → proposed** | No CLIENT_OF from card alone |
| **SAFE UNKNOWN** | Missing fields declared — not invented |
| **Reject** | Misclassified artifact, fabricated card, wrong entity class |

**CC-ATT-01:** Attesting Organization **does not** attest all lines on card — only reviewed claims.

**CC-ATT-02:** Card expiry (outdated director) → lifecycle supersession later — not retroactive silent edit.

---

## 8. What must never be inferred automatically

| Prohibited inference | Correct handling |
|---------------------|------------------|
| Organization from website URL on card | Proposed Website in Wave 4 — separate review |
| Person from email/phone alone | Proposed or UNKNOWN — homonym review |
| CLIENT_OF / VENDOR_OF from card context | Relationship proposal in Wave 6 — separate evidence |
| Contract existence from EDO presence | EDO ≠ agreement |
| Second Organization from trade name | Alias review first (D1) |
| Missing INN/OGRN from similar org | SAFE UNKNOWN — never copy |
| Active attest from OCR confidence | Human review mandatory (ER-01) |
| OPS "Client" entity from card | Organization + future CLIENT_OF only |
| Bank details correctness from old card | Defer or UNKNOWN — verify if critical |

**CC-INF-01:** Agents and imports may **suggest** extractions — steward **confirms** before proposal update.

**CC-INF-02:** Zero-field inference: if a field is absent on card, registry field remains **empty/UNKNOWN** — not defaulted.

---

## 9. Incomplete cards

**Decision A7 (normative):**

| Condition | Registry posture |
|-----------|------------------|
| Legal name present, INN missing (external org) | **proposed** — defer active until INN or E2 alternate |
| Legal name + INN present, OGRN missing | **proposed** or **active** with UNKNOWN OGRN note (steward choice + risk note) |
| Illegible scan | **proposed** — request reissue; document gap |
| Only trade name, no legal name | **proposed** — defer active; alias hunt |
| Operator core org, steward knows entity, card partial | E0 steward attest may suffice for **active** with gap register |

**CC-INC-01:** Incomplete card **never** blocks **proposed** intake — blocks **active** only when minimum evidence unmet ([ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.1).

**CC-INC-02:** Gap register entry required for every deferred field at active boundary.

---

## 10. Multiple cards for one organization

**Decision A8 (normative):**

| Scenario | Handling |
|----------|----------|
| Same INN, updated director | Supersession note; update **proposed** Person; org may stay active |
| Same INN, conflicting legal name | **Disputed** — investigate merge/alias |
| Different INN, same trade name | **Duplicate review D1** — likely separate orgs or error |
| Old + new card in evidence bundle | Valid — list refs chronologically |
| Card from counterparty + steward compilation | Both in bundle — tier = highest justified, not sum |

**CC-MULT-01:** Multiple cards strengthen evidence bundle — they do **not** multiply Organization entities.

**CC-MULT-02:** Conflicting **critical** fields (INN, OGRN, legal name) block new active dependencies until **disputed** resolved.

---

## 11. Contacts on cards (Decision A2)

| Extraction | Allowed state | Rule |
|------------|---------------|------|
| Named contact + role | **proposed** Person + **proposed** REPRESENTATIVE/EMPLOYEE | CC-PER-01 |
| Phone/email only | Contact metadata on org proposal — not Person | No PER mint |
| Director named | **proposed** Person — priority in Wave 2 | Role type reviewed at 2B |
| Multiple contacts | Separate proposed Person each — homonym check | |

**CC-PER-01:** Contact extraction creates **candidates** — never **active** Person without Wave 2 attest path.

---

## 12. Organization from card alone (Decision A1)

| Target state | Card alone sufficient? | Additional requirement |
|--------------|------------------------|------------------------|
| **proposed** Organization | **Yes** | Valid CC intake package |
| **active** operator core (W1-A) | **Yes with E0** | Steward human confirmation |
| **active** external org (W1-B) | **Conditional** | E1+ card + duplicate review; critical fields present |
| **active** legal merge | **No** | E2 + identity governance |

**CC-ORG-01:** Card alone **never** triggers automated active promotion.

---

## 13. Non-deliverables

No card templates, OCR models, vault paths, or canonical Organization records.

---

*ATLAS Counterparty Card Model v1 — Phase 9 Foundation. Documentation only.*
