# ATLAS Organization Acquisition Rules v1

**Status:** **documented** — Phase 9 organization entry rules (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) · [ATLAS-POPULATION-EXECUTION-PLAN-v1.md](ATLAS-POPULATION-EXECUTION-PLAN-v1.md) · [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md)  
**Companion:** [OPS-ATLAS-ALIGNMENT-v1.md](OPS-ATLAS-ALIGNMENT-v1.md) · [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md)  
**Is not:** CRM integration spec, legal document taxonomy, contract management policy.

**Phase 1–8 constraint:** Does not modify entity taxonomy or attestation tiers. Clarifies acquisition **priority** without contradicting Phase 7 evidence minimums.

---

## 1. Purpose

Define **how organizations enter ATLAS** — priority order of acquisition sources, prohibited primary sources, and human confirmation requirements.

**Normative statement:**

> Organizations enter ATLAS through **Counterparty Card-first evidence**, **human confirmation**, and **supplementary corroboration** — never through contracts, invoices, or operational documents as primary intake.

---

## 2. Acquisition priority order

```text
┌─────────────────────────┐
│  1. Counterparty Card   │  Preferred — business reality evidence
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│  2. Human Confirmation  │  Steward/owner attestation (E0) or review gate
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│  3. Other Evidence      │  Corroboration only — not primary alone
└─────────────────────────┘
            │
            ▼
     Proposal → Review → Attestation → Organization Registry
```

### 2.1 Priority 1 — Counterparty Card

| Aspect | Rule |
|--------|------|
| **Role** | Primary organization acquisition artifact |
| **When required** | **Always preferred** for W1-B external orgs; **strongly preferred** for W1-A operator core |
| **Outcome** | Evidence package → Organization **proposal** |
| **Reference** | [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) |

**OAR-01:** If a valid Counterparty Card exists, stewards **must use it** as primary evidence before relying on informal notes alone.

**OAR-02:** Absence of CC for operator-known org (W1-A) does **not** block intake — E0 human confirmation path applies (§3).

### 2.2 Priority 2 — Human Confirmation

| Aspect | Rule |
|--------|------|
| **Role** | Mandatory gate for all **active** canonical Organization records |
| **Forms** | Steward attest (E0), evidence review sign-off (E1+), owner escalation resolution |
| **Never skipped** | Import, agent, OCR, or card extraction |

**OAR-HUM-01:** No Organization becomes **active** without qualified human attest ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §2.1).

**OAR-HUM-02:** Human confirmation **validates** card extraction — it does not replace card when card is available and applicable.

### 2.3 Priority 3 — Other Evidence (corroboration)

**Other evidence** may **support** or **raise tier** — not replace Counterparty Card as primary when CC is obtainable.

| Source type | Tier | Primary for org intake? |
|-------------|------|-------------------------|
| Corporate registry extract | E2 | **Alternate primary** if no CC — steward documents why CC unavailable |
| Bank details letter | E1–E2 | Corroboration |
| Consumer CRM export | E3 | **No** — import proposal only |
| Website / SERP | E1 proposal | **No** — AT-E-03 |
| Contract excerpt | E2 | **No** — corroboration in dispute only (§4) |
| Operator institutional memory | E0 | Valid for W1-A **with** human confirmation — CC still preferred |

**OAR-03:** "Other evidence" path requires **written rationale** when CC was not used but could reasonably have been obtained.

---

## 3. Acquisition paths by organization class

### 3.1 W1-A — Operator core organizations

Examples (illustrative): Polygon, MetaCode, i-SEO.

| Path | Steps | Minimum tier at active |
|------|-------|------------------------|
| **CC + confirm** (preferred) | CC intake → extract → duplicate review → steward attest | E0–E1 |
| **E0 confirm only** | Steward proposal from operator knowledge → attest note | E0 |
| **CC partial + E0** | Incomplete CC + steward gap register + attest | E0 |

**Justification:** Operator core orgs are highest-trust context ([ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.1). CC still preferred for requisites consistency with OPS and future expansion fields.

### 3.2 W1-B — Active client / third-party organizations

Examples (illustrative): Triumph (client org).

| Path | Steps | Minimum tier at active |
|------|-------|------------------------|
| **CC required path** | CC intake → full field review → duplicate review → attest | E1 |
| **Registry extract alternate** | No CC — E2 registry + steward note why CC missing | E2 |
| **Import row** | CRM export → proposed → batch review → attest | E1 or E3 + review |

**Justification:** External orgs carry higher duplicate and homonym risk — CC provides structured identity independent of OPS contract narrative.

### 3.3 W1-C — Latent / historical organizations

| Path | Default state |
|------|---------------|
| CC available | **proposed** until delivery relevance confirmed |
| CC absent | Defer or reject — do not active-attest from memory alone |

---

## 4. Prohibited primary sources

**Decision A4 (normative):** Contracts must **never** be primary acquisition evidence for Organization intake.

| Prohibited primary source | Why | Allowed use |
|---------------------------|-----|-------------|
| **Contract** | Legal/OPS artifact — proves agreement scope, not registry identity discipline | E2 **corroboration** in duplicate/dispute review only |
| **Act of acceptance** | Operational delivery proof | None for org intake |
| **Invoice** | Financial transaction | None for org intake |
| **Technical specification** | Project artifact | None for org intake |
| **Project report** | OPS narrative | None for org intake — may reference existing org id |
| **CRM Account object alone** | Boundary violation (E-26) | E3 import → proposed |

**OAR-BAN-01:** Intake labeled "org from contract" → **reject at intake** or reclassify as corroboration attachment to CC-led proposal.

**OAR-BAN-02:** OPS Agreement (C-07) does **not** create Organization — [OPS-ATLAS-ALIGNMENT-v1.md](OPS-ATLAS-ALIGNMENT-v1.md) §4.5.

**OAR-BAN-03:** Website hostname does **not** create Organization — [ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md) Wave 4 discipline.

---

## 5. Can an organization enter from Counterparty Card alone?

**Decision A1 — consolidated ruling:**

| State | Card alone? |
|-------|-------------|
| **proposed** | **Yes** — valid CC intake is sufficient to open proposal |
| **active** (W1-A) | **Yes with human confirmation (E0)** — card supports but steward attest is mandatory |
| **active** (W1-B) | **Conditional** — E1+ card, critical identifiers reviewed, duplicate check passed |
| **active** (merge) | **No** — E2 + identity governance |

Card alone **never** bypasses human confirmation or duplicate review.

---

## 6. Field trust and review (Decisions A5–A6)

### 6.1 Safe to trust (after steward visual confirm)

| Field | Trust level |
|-------|-------------|
| INN (checksum-valid if verified) | High — primary dedup key |
| OGRN / ОГРНИП | High |
| KPP | High — watch multi-branch |
| Legal name (полное наименование) | High |
| EDO operator + participant id | Medium-high — structural identifier |

### 6.2 Require human review before active

| Field | Risk |
|-------|------|
| Trade / brand name | Duplicate org vs alias |
| Director name | Person homonym; role type |
| Contacts | Person vs metadata |
| Addresses | Branch confusion |
| Bank details | OPS overlap; sensitivity |
| URLs on card | Website wave — not org proof |

---

## 7. Incomplete and multiple cards

See [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) §9–10.

| Situation | Acquisition rule |
|-----------|------------------|
| Incomplete CC | Proposed allowed; active blocked until minimum met |
| Multiple CCs same INN | Single org — evidence bundle |
| Conflicting CCs | Disputed — no new active CLIENT_OF/OWNER deps |

---

## 8. Analysis and justification summary

| Design choice | Justification |
|---------------|---------------|
| **CC first** | Separates **business identity** from **operational/legal workflow**; aligns with OPS requisites without importing OPS objects |
| **Human confirmation mandatory** | Preserves attestation model; prevents OCR/import pollution |
| **Contracts excluded** | Prevents ATLAS becoming contract registry; OPS owns agreement lifecycle |
| **Registry extract as alternate** | Rare CC absence for Russian legal entities — E2 path without contract |
| **E0 path for operator core** | Phase 7 evidence rules preserved — CC preferred but not blocking for W1-A |
| **Import never primary** | AT-IMP-01 — bulk rows are proposals, not acquisition truth |

---

## 9. Acquisition anti-patterns

| Anti-pattern | Response |
|--------------|----------|
| "We have a contract — create the client org" | Reject — obtain CC or registry extract |
| "CRM says they're a client" | Import proposal — CC or confirm path |
| "SERP shows a company at this domain" | MIG proposal — not org intake |
| "Same name as Polygon — new org" | D1 alias review first |
| "Invoice header has INN — good enough" | Reject primary — CC or registry |

---

## 10. Non-deliverables

No acquisition APIs, contract parsers, or CRM field mappings.

---

*ATLAS Organization Acquisition Rules v1 — Phase 9 Foundation. Documentation only.*
