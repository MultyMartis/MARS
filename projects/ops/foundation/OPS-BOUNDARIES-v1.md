# OPS Boundaries v1

**Status:** **documented** — Foundation v1 normative boundary contract.  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-04  
**Parent:** [../README.md](../README.md) · [OPS-ATLAS-RELATIONSHIP-v1.md](OPS-ATLAS-RELATIONSHIP-v1.md)  
**Is not:** enforcement code, linter rules, automated policy engine, or registry entry.

---

## 1. Purpose

Define **what OPS owns** as operational methodology and **what OPS must never absorb**, so back-office documentation does not become a parallel CRM, ledger, legal system, or business identity registry.

---

## 2. OPS owns (operational domain)

OPS **owns** the **documented operational responsibility** for human-supervised back-office rhythms:

| # | Domain | Description | Authority level |
|---|--------|-------------|-----------------|
| **O-01** | Reminders | Operational reminders for reporting cycles, document prep, follow-ups — **tracking intent**, not autonomous scheduling product | Human sets and dismisses |
| **O-02** | Deadlines | Deadline **tracking model** for OPS workflows (e.g. monthly report due date) | Human attestation |
| **O-03** | Reporting workflows | Normative stages, checkpoints, and completion recording for client reporting | Human executes |
| **O-04** | Document workflows | Operational steps for preparing, reviewing, and routing business documents (not legal substance) | Human executes |
| **O-05** | Approval workflows | **Operational** approval gates — who must review before client delivery | Human approves |
| **O-06** | Operational tracking | Status of OPS cycles (triggered → draft → reviewed → delivered → closed) | Human updates |

**Normative statement:**

> OPS owns **how operational back-office work is structured and tracked**, not **what is legally or financially true** about a client or organization.

---

## 3. OPS does not own (hard exclusions)

| # | Exclusion | Owner / lane | Rationale |
|---|-----------|--------------|-----------|
| **X-01** | Business identity (canonical) | **ATLAS** | Single business-reality SoT intent |
| **X-02** | Canonical client records | **ATLAS** | OPS may reference; must not fork SoT |
| **X-03** | Requisites source of truth | **ATLAS** (+ human attestation) | Bank/legal identifiers not invented in OPS |
| **X-04** | Legal authority | Human + qualified legal process | OPS documents workflow, not law |
| **X-05** | Accounting authority | Human + accounting system | No ledger, balances, or tax filings |
| **X-06** | Payment confirmation authority | Human + bank/payment channel | OPS cannot confirm money moved |
| **X-07** | CRM pipeline and deals | External CRM (if any) | No sales SoT |
| **X-08** | ERP resources | External ERP (if any) | No enterprise planning SoT |
| **X-09** | PPC campaign truth | **ORCA** | Evidence may be cited in reports only |
| **X-10** | Market research truth | **MIG** | Evidence may be cited in reports only |
| **X-11** | SEO content production runtime | **MetaBOT** (external) | OPS does not run workflows |
| **X-12** | CMS / storefront operations | **WPilot** / **OCPilot** | Site ops stay in product lanes |
| **X-13** | MARS program registry rows | `registry/project-registry.md` | Not modified in Foundation v1 |
| **X-14** | Autonomous agents and automation | MARS runtime / n8n (when exists) | Foundation v1 is docs-only |

---

## 4. Ownership matrix (summary)

| Concern | OPS | ATLAS | Other consumers |
|---------|-----|-------|-----------------|
| Monthly report **workflow stages** | **Owns (documented)** | — | — |
| Client **display name** for report | References | **SoT (intent)** | — |
| Organization **legal identity** | References | **SoT (intent)** | — |
| Contract **legal meaning** | — | References only | Legal process |
| Invoice **amounts and payment status** | — | — | Accounting / human |
| Project **structural link** to website | References | **SoT (intent)** | Website Factory, WPilot |
| Report **draft text** | Human-authored under OPS workflow | — | — |
| Report **approval to send** | Human gate in OPS workflow | — | — |
| Reminder **that report is due** | OPS tracking model | — | HomeGateway may display later |

---

## 5. Creep resistance rules

| Rule | Requirement |
|------|-------------|
| **BR-01** | If a field defines **who the client is** in canonical terms → **ATLAS**, not OPS |
| **BR-02** | If a field defines **money, tax, or payment state** → **outside OPS** |
| **BR-03** | If a workflow step **signs or binds** legally → **outside OPS** operational authority |
| **BR-04** | If automation is proposed → **separate charter**; Foundation v1 forbids claiming it exists |
| **BR-05** | On ambiguity → **SAFE UNKNOWN** + human attestation; no silent invention |

---

## 6. Phase 1 (Foundation) scope

Foundation v1 delivers **boundaries only**. No enforcement tooling, no storage layout, no API.

---

*OPS Boundaries v1 · Business Operations Domain.*
