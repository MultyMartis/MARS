# OPS — ATLAS Relationship v1

**Status:** **documented** — consumer relationship contract (design).  
**Programs:** OPS (Business Operations Domain) · ATLAS (Business Reality Registry)  
**Date:** 2026-06-04  
**Parent:** [OPS-BOUNDARIES-v1.md](OPS-BOUNDARIES-v1.md) · [../../atlas/foundation/ATLAS-REALITY-MODEL-v1.md](../../atlas/foundation/ATLAS-REALITY-MODEL-v1.md)  
**Is not:** API specification, sync implementation, or duplicate registry.

---

## 1. Roles

| System | Role |
|--------|------|
| **ATLAS** | **Business Reality Registry** — canonical intent for **who exists, what exists, and how things are related** |
| **OPS** | **Business Operations Domain** — human-supervised **operational workflows** (reporting, documents, approvals, tracking) |

**Ecosystem rule (aligned with ATLAS):**

> **ATLAS maintains who exists, what exists, and how things are related.**  
> **OPS performs supervised operational work using that reality — without replacing it.**

---

## 2. What OPS consumes from ATLAS

OPS is an **ATLAS consumer** (design). When ATLAS data is available, OPS workflows **reference** the following entity classes for context — never as a parallel master copy:

| # | ATLAS consumer class | OPS use |
|---|----------------------|---------|
| **C-01** | **Clients** | Identify report recipient and contractual context |
| **C-02** | **Contacts** | Name roles (billing contact, technical contact) in reports |
| **C-03** | **Organizations** | Legal/display entity for report header and routing |
| **C-04** | **Projects** | Scope work evidence to the correct engagement |
| **C-05** | **Websites** | Anchor site-related operational summaries |
| **C-06** | **Services** | Describe which service lines apply to the reporting period |
| **C-07** | **Agreements** | Reference active agreement scope (not legal interpretation) |
| **C-08** | **Requisites** | Insert invoicing/payment details **only from ATLAS-attested fields** |
| **C-09** | **Relationships** | Structural edges (org ↔ project ↔ website) for narrative consistency |

**Consumption mode (Foundation v1):** **SAFE UNKNOWN** for machine read path — operator may manually copy from ATLAS exports or future read APIs. OPS documentation **does not** claim a live integration.

---

## 3. What OPS must never duplicate as source of truth

OPS **must not** maintain authoritative copies of:

| # | Forbidden duplicate | Correct source |
|---|---------------------|----------------|
| **D-01** | Master client list | ATLAS |
| **D-02** | Canonical organization records | ATLAS |
| **D-03** | Authoritative contact directory | ATLAS |
| **D-04** | Project registry as structural SoT | ATLAS |
| **D-05** | Website / domain identity SoT | ATLAS |
| **D-06** | Agreement text or legal status SoT | ATLAS + human/legal process |
| **D-07** | Bank requisites SoT | ATLAS (+ human attestation) |
| **D-08** | Relationship graph SoT | ATLAS |

**Allowed in OPS (operational artifacts only):**

- Report **drafts** and **delivery records** for a cycle
- **Workflow status** (stage, reviewer, approval timestamp) — operational metadata
- **Operator notes** clearly labeled non-canonical
- **Pointers** (ATLAS entity ids or stable references when ids exist)

---

## 4. Anti-duplication rules

| Rule ID | Rule |
|---------|------|
| **AD-01** | Every OPS artifact that names a client/org/project **must** cite an ATLAS reference when ids exist; if ids do not exist → **SAFE UNKNOWN** + human label |
| **AD-02** | Editing a “client card” inside OPS for canonical fields is **forbidden** — changes flow through ATLAS governance |
| **AD-03** | OPS spreadsheets or docs used during a cycle are **working copies**, not SoT — completion must not imply ATLAS promotion |
| **AD-04** | If ATLAS and an OPS working copy disagree → **ATLAS wins** for identity/structure; OPS report text is corrected by operator |
| **AD-05** | New entities discovered during reporting (e.g. new contact) → **intake to ATLAS** (future process), not silent OPS-only creation |
| **AD-06** | Requisites in a client report **must** match ATLAS-attested values or be omitted with explicit **SAFE UNKNOWN** |

---

## 5. Read vs write boundary

| Direction | OPS | ATLAS |
|-----------|-----|-------|
| **Read** | Consumes identity/structure for operational context | Publishes canonical reality (when implemented) |
| **Write (canonical)** | **No** | Human-supervised promotion only (ATLAS design) |
| **Write (operational)** | Report drafts, workflow status, completion records | **No** — unless explicit future “operational event” entity is chartered in ATLAS |

**Foundation v1:** No write contract is defined between OPS and ATLAS.

---

## 6. Consumer failure modes

| Failure | OPS behavior |
|---------|--------------|
| ATLAS entity missing | Stage 5 Missing Data Review; do not invent canonical facts |
| ATLAS stale vs operator knowledge | Escalate to ATLAS correction path; hold client delivery |
| ATLAS not implemented | Operator uses manual attested references; mark **SAFE UNKNOWN** in report footer |

---

## 7. Related documents

| Document | Link |
|----------|------|
| OPS boundaries | [OPS-BOUNDARIES-v1.md](OPS-BOUNDARIES-v1.md) |
| ATLAS reality model | [../../atlas/foundation/ATLAS-REALITY-MODEL-v1.md](../../atlas/foundation/ATLAS-REALITY-MODEL-v1.md) |
| ATLAS boundaries | [../../atlas/foundation/ATLAS-BOUNDARIES-v1.md](../../atlas/foundation/ATLAS-BOUNDARIES-v1.md) |
| Monthly reporting workflow | [../workflows/OPS-MONTHLY-REPORTING-WORKFLOW-v1.md](../workflows/OPS-MONTHLY-REPORTING-WORKFLOW-v1.md) |

---

*OPS — ATLAS Relationship v1 · consumer contract (documentation only).*
