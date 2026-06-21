# ATLAS Evidence Requirements v1

**Status:** **documented** — Phase 7 population evidence expectations (governance).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-POPULATION-STRATEGY-v1.md](ATLAS-POPULATION-STRATEGY-v1.md)  
**Is not:** runtime validation, evidence vault implementation, OCR pipeline, automated tier classifier.

**Phase 1–6 constraint:** Uses existing **E0–E3** attestation model without modification. No contradictions found.

---

## 1. Purpose

Define **minimum evidence expectations** for population of each MVP entity class and for relationship promotion — **governance expectations only**.

Humans assign tiers at review; systems **must not** auto-promote on tier match alone.

---

## 2. Evidence tier reference (unchanged)

From [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §3.2:

| Tier | Description |
|------|-------------|
| **E0** | Internal attestation — trusted operator context |
| **E1** | Informal document — email, chat export, letter scan ref |
| **E2** | Formal document — contract extract, registrar, corporate registry |
| **E3** | System corroboration — consumer FK, API snapshot ref |

**Rules carried forward:** AT-E-01 through AT-E-05; fabricated tier = governance violation.

---

## 3. Population evidence philosophy

| Principle | Application |
|-----------|-------------|
| **Tier matches claim risk** | OWNER / legal merge > casual website existence |
| **Pointer not payload** | `evidence_ref` + note — not full contracts in ATLAS |
| **Import is E3 at best** | Still requires human promote |
| **MIG is not structural proof** | SERP packs support **proposal** only (AT-E-03) |
| **Absence blocks active** | Remain **proposed** or **SAFE UNKNOWN** (AT-E-04) |

---

## 4. Minimum evidence by entity class

### 4.1 Organization

| Population scenario | Minimum tier at **active** attest | Notes |
|---------------------|-----------------------------------|-------|
| Operator-known core org | **E0** | Steward attestation note sufficient |
| Client / third-party org | **E1** | Commercial subject with delivery history |
| Legal same-subject merge | **E2** | Survivor merge per IGV |
| Import-only CRM company | **E1 or E3 + review** | No E0 |
| Existence inferred from website URL | **Insufficient** | No auto-org |

**Required evidence elements (conceptual):**

- Attested **display name** and disambiguation note if homonym risk
- **Why** this is an Organization entity vs CRM Account (boundary check)
- `evidence_ref` when tier ≥ E1

### 4.2 Person

| Population scenario | Minimum tier at **active** attest | Notes |
|---------------------|-----------------------------------|-------|
| Operator-known individual | **E0** | Direct steward/owner attest |
| Contractor / external person | **E1** | Structural role, not payroll |
| Import CRM contact only | **E1 or E3 + review** | No E0 |
| Person inferred from email alone | **Insufficient** | Homonym risk → proposed or UNKNOWN |

**Required elements:**

- Legal or preferred name attested
- Explicit **not** a service account / bot boundary

### 4.3 Project

| Population scenario | Minimum tier at **active** attest | Notes |
|---------------------|-----------------------------------|-------|
| Active pilot / pack (operator) | **E0–E1** | Structural container, not Jira |
| Historical closed initiative | **E1** | May enter **proposed** until confirmed |
| Name collision with MARS `project_id` | **E1 note** | Disambiguation in attest rationale |
| Import-only project code | **E3 + review** | |

**Required elements:**

- **Initiative identity** — what is being clustered
- Sponsor org **reference** (active, proposed, or SAFE UNKNOWN for sponsor slot)

### 4.4 Website

| Population scenario | Minimum tier at **active** attest | Notes |
|---------------------|-----------------------------------|-------|
| Internal operator site | **E0–E1** | Per AT §4.3 |
| Client property in production | **E1** | Factory/ORCA handoff |
| Staging-only URL | **proposed** preferred | May defer active |
| Existence from SERP only | **Insufficient for active** | MIG proposal only |
| Website without known org | **E1 for site existence**; org slot **UNKNOWN** | No BELONGS_TO active |

**Required elements:**

- Canonical **web property identity** (brand/product level, not single A/B URL)
- Consumer cross-ref optional (E3) — not sufficient alone

### 4.5 Domain

| Population scenario | Minimum tier at **active** attest | Notes |
|---------------------|-----------------------------------|-------|
| Operator primary domain | **E1** | Registrar/DNS intent |
| Parked domain (no site) | **E1** | May be **proposed** until launch |
| Import registrar API only | **E3 + review** | |
| Domain guessed from email | **Insufficient** | |

**Required elements:**

- Hostname string attested
- Intended **PRIMARY_DOMAIN** or alias role deferred to Wave 6C relationship

### 4.6 Relationship

Minimum tiers align with [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §3.1 and [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §4.3:

| Type category | Minimum tier at **active** attest |
|---------------|-----------------------------------|
| OWNER, OWNS (domain/site) | **E1** (E2 if dispute risk) |
| CLIENT_OF, VENDOR_OF | **E1** |
| REPRESENTATIVE | **E1** |
| EMPLOYEE, CONTRACTOR | **E1** |
| PRIMARY_DOMAIN, BELONGS_TO (structural) | **E1** |
| Operator direct structural fact | **E0** allowed **only** with steward/owner note |
| Import-only relationship | **E1 or E3 + human review** |

**Endpoint evidence rule (EV-R-01):** Evidence for the **edge** does not substitute for missing **endpoint** attestation. Endpoints must be **active** or explicitly **proposed** as a documented pair pending joint promotion.

---

## 5. First-wave (Wave 1–2) evidence profile

| Wave | Default tier band | Exception |
|------|-------------------|-----------|
| Wave 1 operator orgs | E0–E1 | Client orgs → E1+ |
| Wave 2 operator persons | E0–E1 | External → E1+ |
| Wave 2B participation edges | E1 for OWNER/CLIENT_OF; E0 only operator-direct | |

**EV-FW-01:** First wave **never** uses “import bulk E3 → active” without spot attest records.

---

## 6. SAFE UNKNOWN handling

### 6.1 When to declare SAFE UNKNOWN (population)

| Situation | Population action |
|-----------|-------------------|
| Org for website unknown | Website may be **proposed**; org slot **SAFE UNKNOWN**; no active OWNS/BELONGS_TO |
| Person homonym unresolved | No active Person; separate **proposed** or UNKNOWN |
| Relationship type unclear | No active edge; **proposed** without type lock or UNKNOWN |
| Consumer key unmapped | UNKNOWN until steward maps — no invented id |
| Business Scope label only | **Not** evidence for entity existence |

Rules: AT-UK-01 through AT-UK-05.

### 6.2 UNKNOWN is not a workaround for laziness

**EV-UK-01:** UNKNOWN requires **steward/owner declaration** with gap description — not default empty field.

**EV-UK-02:** UNKNOWN may queue work; **must not** drive automation that mints ids (AT-UK-04).

---

## 7. Incomplete evidence handling

| State | Evidence condition | Allowed registry posture |
|-------|-------------------|---------------------------|
| **Incomplete** | Below minimum tier for target class | **proposed** only |
| **Partial** | Tier met for existence, not for link | Entity **active**; relationship **proposed** or UNKNOWN |
| **Pending external** | Awaiting E2 document | Remain **proposed**; set review date |
| **Stale** | Evidence expired (registrar transfer) | **disputed** or supersede via lifecycle |

**EV-INC-01:** Do not downgrade tier retroactively without change governance note.

**EV-INC-02:** Consumers may read **proposed** only if contract allows; canonical SoT is **active** ([ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md](ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md)).

---

## 8. Disputed evidence handling

### 8.1 Disputed vs UNKNOWN

| State | Meaning |
|-------|---------|
| **SAFE UNKNOWN** | Insufficient knowledge to assert |
| **disputed** | Competing claims with conflicting evidence |

Both block **new irreversible canonical dependencies** ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §7.3).

### 8.2 How disputed reality enters the registry

| Step | Behavior |
|------|----------|
| 1 | Competing **proposed** records or one **active** + one **proposed** challenger |
| 2 | Mark affected records/edges **disputed** |
| 3 | Evidence review — upgrade tier, merge, separate subjects, or UNKNOWN |
| 4 | Owner escalation if needed |
| 5 | Outcome: **one active** attest path, **merge**, **separate ids**, or **SAFE UNKNOWN** |

**EV-DISP-01:** Never **two active canonical** for same subject (D1).

**EV-DISP-02:** Disputed **active** OWNER edges forbidden — downgrade to **proposed** or **disputed**.

### 8.3 Disputed evidence tiers

If parties cite E1 vs E1 conflicting narratives → **disputed** until E2 resolves or subjects separated.

Fabricated evidence → **reject proposal**; governance incident (GV §3.3, AT-E-05).

---

## 9. Evidence expectations matrix (quick reference)

| Class | Active minimum (typical) | Import minimum | SERP/MIG |
|-------|--------------------------|----------------|----------|
| Organization | E0 (operator) / E1 (external) | E1/E3 + review | Proposal only |
| Person | E0 (operator) / E1 (external) | E1/E3 + review | N/A |
| Project | E0–E1 | E3 + review | N/A |
| Website | E0–E1 (internal) | E1/E3 + review | Proposal only |
| Domain | E1 | E3 + review | N/A |
| Relationship | E1 (most types) | E1/E3 + review | N/A |

---

## 10. Non-deliverables

No validators, APIs, storage schemas, or automated tier scoring.

---

*ATLAS Evidence Requirements v1 — Phase 7 Foundation. Documentation only.*
