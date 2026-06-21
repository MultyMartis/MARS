# ATLAS Wave 1 Execution v1

**Status:** **documented** — Phase 9 first population wave execution charter (methodology).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-05  
**Parent:** [ATLAS-POPULATION-EXECUTION-PLAN-v1.md](ATLAS-POPULATION-EXECUTION-PLAN-v1.md) · [ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md)  
**Companion:** [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) · [ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) · [ATLAS-POPULATION-READINESS-CHECKLIST-v1.md](ATLAS-POPULATION-READINESS-CHECKLIST-v1.md)  
**Is not:** canonical records, sprint backlog, card file inventory, implementation tickets.

**Important:** This document defines **execution methodology** using **known reality as examples**. It does **not** create canonical Organization or Person records, assign `ORG-*` / `PER-*` ids, or attest any entity active.

**Phase 1–8 constraint:** Examples reference foundation exemplars only — not population shortcuts.

---

## 1. Purpose

Design **Wave 1 execution** — the first controlled population tranche — covering:

- **Wave 1** — Organizations (anchor set)
- **Wave 2** — People (paired execution plan for Stage A)
- **Wave 2B** — Participation relationships (execution sequencing)

Uses operator-known examples: **Polygon, MetaCode, i-SEO, Triumph** (organizations); **Andrey, Sergey, Roman, Triumph contacts** (people).

---

## 2. Wave 1 scope

### 2.1 In scope

| Tier | Description | Example subjects (illustrative) |
|------|-------------|--------------------------------|
| **W1-A Operator core** | Operator-owned durable business units | Polygon, MetaCode, i-SEO |
| **W1-B Active client** | Commercial counterparties with active delivery | Triumph (client organization) |
| **W1-C Latent** | **Out of Wave 1 execution** unless owner exception | Historical clients — defer |

### 2.2 Out of scope for Wave 1

| Excluded | Wave |
|----------|------|
| Projects (e.g. Triumph pilot as Project) | Wave 3 |
| Websites / domains | Waves 4–5 |
| CLIENT_OF / VENDOR_OF edges | Wave 6A |
| MIG session artifacts | Proposal support only |
| OPS Agreement / invoice-derived orgs | Prohibited primary path |

**Distinction — Triumph:**

| Concept | Entity class | Wave |
|---------|--------------|------|
| Triumph as **client business** | Organization | **Wave 1** (W1-B) |
| Triumph gruzotaxi Krasnodar **pilot** | Project | Wave 3 — not Wave 1 |

---

## 3. Execution sequence overview

```text
Phase A ── Readiness checklist (Wave 1)
    │
    ▼
Step 1 ── Collect / compile Counterparty Cards (W1-A, W1-B)
    │
    ▼
Step 2 ── Intake Organization proposals (one package each)
    │
    ▼
Step 3 ── Duplicate review batch (all W1 before any active)
    │
    ▼
Step 4 ── W1-A active attest tranche (operator core)
    │
    ▼
Step 5 ── W1-B active attest tranche (Triumph — after W1-A stable)
    │
    ▼
Step 6 ── Wave 2 People intake (Andrey, Sergey, Roman, Triumph contacts)
    │
    ▼
Step 7 ── Wave 2B participation edges
    │
    ▼
Gate GA-01 ── Stage A organization anchor exit
```

**W1-EXEC-01:** Complete duplicate review for **all** Wave 1 candidates before first **active** attest — prevents early alias mistakes poisoning Wave 2B.

---

## 4. Organization execution methodology

### 4.1 W1-A tranche — operator core

#### Polygon (example)

| Execution step | Action |
|----------------|--------|
| Card | Obtain or compile CC — legal name, INN/OGRN if available, aliases (Полигон, WSP, Web Studio Polygon) |
| Intake | Organization proposal — note alias candidates, not separate orgs |
| Duplicate review | Check against MetaCode, i-SEO, WSP homonyms ([ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md)) |
| Evidence | E0–E1; CC preferred |
| Attest | Steward active attest with alias register intent |
| Gaps | Document UNKNOWN fields (bank details until expansion) |

**Known relationship context (Wave 2B — not Wave 1):** Andrey → OWNER ([ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md) exemplar).

#### MetaCode (example)

| Execution step | Action |
|----------------|--------|
| Card | CC intake — watch Cyrillic/Latin alias (MetaCode / Метакод) |
| Duplicate review | I1-class investigation if vendor homonym ([ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md)) |
| Evidence | E0–E1 operator core |
| Attest | Separate Organization from Polygon — **no ownership collapse** |
| Gaps | SAFE UNKNOWN until card confirms legal requisites |

**Known relationship context (Wave 2B):** Andrey → OWNER.

#### i-SEO (example)

| Execution step | Action |
|----------------|--------|
| Card | CC intake — preserve hyphenation in alias register |
| Duplicate review | Agency vs client org confusion — boundary check |
| Evidence | E0–E1 |
| Attest | Organization entity — not "department" pseudo-org |
| Gaps | Client portfolio orgs **not** inferred from i-SEO card |

**Known relationship context (Wave 2B):** Andrey → MANAGER (not OWNER — multi-hat discipline).

### 4.2 W1-B tranche — Triumph (client org example)

| Execution step | Action |
|----------------|--------|
| Card | **Required path** — client CC (PDF/DOCX/XLSX/image/text) |
| Intake | Organization proposal — W1-B tier |
| Duplicate review | "Triumph" homonym — disambiguation note (gruzotaxi Krasnodar) |
| Evidence | **E1 minimum** — no E0 for external client |
| Attest | Active after critical fields reviewed |
| Gaps | Contacts on card → **proposed** Person (Wave 2) — not bundled active |
| Explicit non-action | Do **not** create Project record in Wave 1 |

**W1-EXEC-02:** W1-B attest **after** W1-A tranche complete — reduces duplicate pressure and establishes operator anchor context.

### 4.3 Organization execution package template (conceptual)

Each Organization execution uses one package:

| Field | Example (Polygon) |
|-------|-------------------|
| Wave tier | W1-A |
| CC evidence_ref | `[pointer — not created in this doc]` |
| Extracted legal name | `[from card — steward verified]` |
| Alias candidates | Полигон, WSP, Web Studio Polygon |
| Duplicate signals | WSP brand overlap |
| Evidence tier | E0 + CC E1 |
| Proposed state outcome | proposed → review → active |
| Gap register | Bank requisites UNKNOWN until expansion |
| Wave 2B notes | Andrey OWNER pending |

---

## 5. People execution methodology (Wave 2 paired)

Wave 2 executes **after** Wave 1 org proposals exist (active preferred for 2B).

### 5.1 Operator persons

| Person (example) | Intake source | Evidence | Duplicate note |
|------------------|---------------|----------|----------------|
| **Andrey** | Operator E0 + optional CC contact lines | E0 | U4 homonym — canonical name disambiguation |
| **Sergey** | Operator E0 | E0 | Scope narrative person — attest within business scope |
| **Roman** | Operator E0 | E0 | Same discipline as Sergey |

**W1-EXEC-03:** Andrey, Sergey, Roman are **Person** entities — not WP users, not scope labels.

### 5.2 Triumph contacts (example)

| Source | Handling |
|--------|----------|
| Names on Triumph CC | **proposed** Person each |
| Phone/email only | Metadata — no Person mint |
| Role on card | Notes for Wave 2B relationship type review |

**W1-EXEC-04:** Triumph contacts are **not** OPS Contact entities — Person + future REPRESENTATIVE/EMPLOYEE.

### 5.3 Person execution package template (conceptual)

| Field | Example (Andrey) |
|-------|------------------|
| Wave | 2 |
| Intake source | E0 operator knowledge |
| CC contact extraction | Optional corroboration — not required for E0 |
| Canonical name | Disambiguated legal/preferred name |
| Homonym check | U4 — separate PER if two Andrey |
| Endpoint deps | Polygon, MetaCode, i-SEO orgs from Wave 1 |
| 2B edges queued | OWNER ×2, MANAGER ×1 |

---

## 6. Wave 2B execution methodology

Execute when Wave 1 orgs and Wave 2 persons reach **active** (or documented proposed pairs per W2B-R01).

### 6.1 Exemplar edge queue (methodology — not attested)

| Person | Organization | Relationship type | Evidence |
|--------|--------------|-------------------|----------|
| Andrey | Polygon | OWNER | E0 operator-direct |
| Andrey | MetaCode | OWNER | E0 operator-direct |
| Andrey | i-SEO | MANAGER | E1 — role distinct from OWNER |
| Sergey | [scope org TBD at execution] | TBD at review | E1 when org endpoint active |
| Roman | [scope org TBD at execution] | TBD at review | E1 when org endpoint active |
| Triumph contact | Triumph | REPRESENTATIVE or EMPLOYEE | E1 from CC + review |

**W1-EXEC-05:** Do **not** attest CLIENT_OF (agency → Triumph) in Wave 2B — that is Wave 6A ([ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md)).

### 6.2 2B execution steps

1. Verify endpoint ids **active** (or approved proposed pair).
2. Queue one relationship proposal per edge.
3. Evidence review per type ([ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.6).
4. Attest edges — no disputed OWNER.
5. Record FORMER_* only when role ending is known — not in initial wave unless explicit.

---

## 7. Counterparty Card collection plan (methodology)

| Organization | CC action | Fallback |
|--------------|-----------|----------|
| Polygon | Compile from operator records / request formal card | E0 steward path |
| MetaCode | Same | E0 steward path |
| i-SEO | Same | E0 steward path |
| Triumph | **Obtain client card** — primary path | E2 registry extract + rationale if CC unavailable |

**W1-EXEC-06:** Card collection is **human operational work** — not automated scrape from contracts or invoices.

---

## 8. Duplicate and identity watchlist (Wave 1)

Pre-seed duplicate review with known exemplar signals:

| Signal | Entities | Review class |
|--------|----------|--------------|
| WSP / Полигон / Polygon | Polygon | Alias — not second org |
| MetaCode / Метакод | MetaCode | I1 investigation if vendor homonym |
| i-SEO hyphenation | i-SEO | Alias preservation |
| Triumph / Триумф | Triumph org vs pilot name | Disambiguation note |
| Andrey homonym | Person | U4 / D3 |

---

## 9. Stop conditions within Wave 1 execution

| STOP | Trigger |
|------|---------|
| STOP-W1-01 | Unresolved D1 duplicate org |
| STOP-W1-02 | Contract used as primary intake |
| STOP-W1-03 | Active attest before duplicate batch complete |
| STOP-W1-04 | Triumph active without E1+ evidence |
| STOP-W1-05 | `org-unknown-*` mint attempted |

Aligns with [ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md) population halt rules.

---

## 10. Exit criteria (Wave 1 execution complete)

| Criterion | Evidence |
|-----------|----------|
| W1-A orgs active | Polygon, MetaCode, i-SEO — E0–E1 trail |
| W1-B Triumph org | Active or documented defer with owner sign-off |
| No unresolved D1 | Duplicate log clear |
| Wave 2 persons | Andrey minimum active; Sergey/Roman active or proposed with note |
| Wave 2B | Core Andrey edges active or GA-03 defer |
| Gap register | UNKNOWN fields enumerated |
| Execution log | All packages recorded |

**Maps to roadmap gate GA-01** ([ATLAS-POPULATION-ROADMAP-v1.md](ATLAS-POPULATION-ROADMAP-v1.md) §3.5).

---

## 11. What this document does not create

| Not created | Reason |
|-------------|--------|
| `ORG-*` identifiers | Identity assignment happens at execution time by steward |
| `PER-*` identifiers | Wave 2 execution act |
| `REL-*` identifiers | Wave 2B execution act |
| Canonical active records | Methodology only |
| Counterparty Card files | Operational artifact — outside this package |

---

## 12. Non-deliverables

No tickets, no card repository paths, no CRM exports, no canonical JSON/MD registry rows.

---

*ATLAS Wave 1 Execution v1 — Phase 9 Foundation. Documentation only.*
