# OPS Document Foundation v1

**Status:** **documented** — Document Foundation pack (documentation only).  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-10  
**Pass:** Reality Audit & Template Program — foundation wave  
**Parent:** [OPS-BOUNDARIES-v1.md](OPS-BOUNDARIES-v1.md) · [OPS-ATLAS-RELATIONSHIP-v1.md](OPS-ATLAS-RELATIONSHIP-v1.md) · [OPS-WF-02-DOCUMENT-CLOSING-v1.md](../workflows/OPS-WF-02-DOCUMENT-CLOSING-v1.md)  
**Is not:** template library, contract text, runtime, automation, legal authority, or document storage system.

---

## 1. Purpose

Establish the **documented foundation** for a real studio document package:

- what OPS owns in the document lane
- how documents relate to ATLAS and external storage
- how documents will be inventoried and audited before any redesign

**Normative scope of this pass:** foundation, taxonomy, audit methodology, and empty inventory structure only.

**Explicitly deferred:** document analysis, template creation, contract redesign, population of inventory rows.

---

## 2. Context and decisions

| Prior state | Decision |
|-------------|----------|
| ATLAS Agreement Layer | **COMPLETE** (documentation) |
| ATLAS Agreement Metadata | **COMPLETE** (documentation) |
| OPS registration | **REGISTERED** (`project_id` **ops**) |
| ATLAS contract storage | **Does NOT store contracts** — ATLAS stores business reality references only |
| Real document files | **Belong outside ATLAS** — human-operated storage |

**Foundation decision:**

> OPS becomes the **owner of document process documentation** — templates, standards, lifecycle visibility, and preparation guidance — **not** document execution, accounting, or legal authority.

---

## 3. What OPS owns (document lane)

| # | Domain | Description | Authority level |
|---|--------|-------------|-----------------|
| **DOC-O-01** | Document templates | Normative template definitions, version labels, and preparation guidance for studio operational documents | Human-maintained; OPS documents standards |
| **DOC-O-02** | Document categories | Practical taxonomy for classifying studio documents — see [OPS-DOCUMENT-TAXONOMY-v1.md](OPS-DOCUMENT-TAXONOMY-v1.md) | OPS-owned vocabulary |
| **DOC-O-03** | Document status visibility | Operational visibility into whether a document type is **ACTIVE**, **LEGACY**, or **UNKNOWN** — not legal validity | Human attestation |
| **DOC-O-04** | Document preparation guidance | Step-by-step human guidance for preparing, reviewing, and routing documents within OPS workflows (e.g. WF-02) | Human executes |
| **DOC-O-05** | Document audit inventory | Structured register of discovered studio documents — see [../population/OPS-DOCUMENT-INVENTORY-v1.md](../population/OPS-DOCUMENT-INVENTORY-v1.md) | Human-populated via audit |
| **DOC-O-06** | Template candidate tracking | Flagging documents that should become or inform future templates — audit output only in v1 | Human review |

**Normative statement:**

> OPS owns **how studio documents are classified, audited, and prepared operationally** — not **what is legally binding, financially recorded, or cryptographically signed**.

---

## 4. What OPS does not own (hard exclusions)

| # | Exclusion | Owner / lane | Rationale |
|---|-----------|--------------|-----------|
| **DOC-X-01** | Legal authority | Human + qualified legal process | OPS documents workflow, not law |
| **DOC-X-02** | Accounting authority | Human + accounting system | No ledger, balances, or tax filings |
| **DOC-X-03** | Document signing | Human + qualified signatory / EDO provider | OPS tracks routing; does not sign |
| **DOC-X-04** | EDO systems | External EDO platform (if any) | OPS does not operate EDO |
| **DOC-X-05** | Contract storage authority | External document storage + human governance | ATLAS references existence; does not store files |
| **DOC-X-06** | Agreement text SoT | ATLAS (metadata) + external storage (files) | ATLAS Agreement Metadata is overlay only |
| **DOC-X-07** | Canonical business identity | **ATLAS** | Requisites, org identity — reference only |
| **DOC-X-08** | Payment confirmation | Human + bank/payment channel | OPS cannot confirm money moved |
| **DOC-X-09** | Autonomous document generation | MARS runtime / automation (when exists) | Foundation v1 forbids claiming it exists |

Aligned with [OPS-BOUNDARIES-v1.md](OPS-BOUNDARIES-v1.md) exclusions **X-04**, **X-05**, **X-06**.

---

## 5. Three-layer document relationship model

```
┌─────────────────────────────────────────────────────────────────┐
│  ATLAS — Business Reality Registry                              │
│  → Agreement exists (AGR-*)                                       │
│  → Agreement metadata (operational_status, document_expectation)│
│  → Org / project / requisite references                         │
│  Does NOT store contract files, PDFs, or signed documents        │
└──────────────────────────┬──────────────────────────────────────┘
                           │ references (read/consume)
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  OPS — Document Process                                         │
│  → Document categories and taxonomy                               │
│  → Preparation guidance and workflow stages (WF-02)             │
│  → Template standards and version labels                        │
│  → Audit inventory (status, quality, improvement flags)         │
│  Does NOT execute signing, accounting, or legal interpretation  │
└──────────────────────────┬──────────────────────────────────────┘
                           │ pointers to
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  Storage — Actual Files                                         │
│  → Contract PDFs, DOCX templates, signed acts, invoices         │
│  → Human-operated file systems, cloud folders, EDO exports        │
│  Location: SAFE UNKNOWN until infrastructure attestation        │
└─────────────────────────────────────────────────────────────────┘
```

| Layer | Question it answers | Does not answer |
|-------|---------------------|-----------------|
| **ATLAS** | Does an agreement exist? What operational documents are expected? Who is the counterparty? | Where is the PDF? What are the legal clauses? |
| **OPS** | How should we prepare this document? What template applies? Is this document type active or legacy? | Is the contract legally valid? Has payment cleared? |
| **Storage** | Where is the actual file? What version was signed? | What is the canonical org identity? (→ ATLAS) |

---

## 6. Relationship with ATLAS

| Aspect | Foundation v1 stance |
|--------|----------------------|
| Agreement existence | ATLAS **AGR-*** entities — OPS references via `related_atlas_entities` on OpsCase |
| Agreement metadata | ATLAS Agreement Metadata overlay — `document_expectation`, `operational_status` inform OPS document scope |
| Contract text / PDFs | **Not in ATLAS** — OPS audit may record storage pointers in inventory **Notes** only |
| Requisites in documents | **ATLAS-attested only** — per AD-06 in [OPS-ATLAS-RELATIONSHIP-v1.md](OPS-ATLAS-RELATIONSHIP-v1.md) |
| New agreement discovery during audit | Intake to ATLAS governance — not silent OPS-only creation |

**Anti-duplication (document lane):**

| Rule ID | Rule |
|---------|------|
| **DOC-AD-01** | Document inventory **must not** duplicate ATLAS as agreement or identity SoT |
| **DOC-AD-02** | Inventory rows describe **operational document artifacts** (files, templates) — not canonical entity records |
| **DOC-AD-03** | If audit reveals agreement not in ATLAS → flag for ATLAS intake; do not treat inventory as registry |
| **DOC-AD-04** | Template requisites blocks **must** match ATLAS-attested values or be marked **SAFE UNKNOWN** |

---

## 7. Relationship with OPS workflows

| Workflow | Document Foundation link |
|----------|--------------------------|
| **WF-02 Document Closing** | Primary consumer — preparation, review, routing stages use taxonomy categories and future templates |
| **WF-01 Monthly Reporting** | May surface missing document obligations via ATLAS `document_expectation` |
| **WF-03 Client Follow-Up** | May trigger when document audit reveals gaps or client requests |
| **WF-06 Project Completion** | May open document closing sub-threads for closure packages |

Document Foundation **does not** modify workflow contracts in v1 — it provides the classification and audit layer WF-02 will consume in future passes.

---

## 8. Document Foundation artifact map

| Artifact | Path | Role |
|----------|------|------|
| Document Foundation (this file) | `foundation/OPS-DOCUMENT-FOUNDATION-v1.md` | Ownership model, ATLAS/storage relationship, scope |
| Document Taxonomy | [OPS-DOCUMENT-TAXONOMY-v1.md](OPS-DOCUMENT-TAXONOMY-v1.md) | Practical category vocabulary |
| Audit Methodology | [OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md](OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md) | Per-document audit procedure and field definitions |
| Document Inventory | [../population/OPS-DOCUMENT-INVENTORY-v1.md](../population/OPS-DOCUMENT-INVENTORY-v1.md) | Empty register — future audit population |
| Pass report | [../reports/REPORT-ops-document-foundation-v1.md](../reports/REPORT-ops-document-foundation-v1.md) | Foundation pass record |

---

## 9. Explicit exclusions (this pack)

This foundation pack **does not**:

- Analyze existing studio documents
- Create or redesign templates or contract texts
- Populate the inventory with guessed rows
- Create runtime, automation, or EDO integration
- Modify ATLAS files, registry, or topology
- Claim document storage location ( **SAFE UNKNOWN** until attested )

---

## 10. SAFE UNKNOWN

| Topic | What is unknown | What would verify |
|-------|-----------------|-------------------|
| Document storage root | Where studio keeps master templates and signed files | Infrastructure / operator attestation |
| Template format standard | DOCX vs Google Docs vs other | Audit pass on existing files |
| EDO provider in use | Whether studio uses Diadoc, SBIS, or other | Operator attestation |
| Count of existing documents | Total files to audit | First audit population pass |
| Agreement ↔ file mapping | Which AGR-* maps to which stored contract | Cross-reference audit with ATLAS register |

---

## 11. Recommended sequence (post-foundation)

1. **Audit population pass** — apply [OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md](OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md) to real studio documents; populate [OPS-DOCUMENT-INVENTORY-v1.md](../population/OPS-DOCUMENT-INVENTORY-v1.md)
2. **Reality report** — summarize active vs legacy vs unknown; template candidates
3. **Template charter** (separate pass) — only after audit completes; no redesign in audit pass
4. **WF-02 binding** — link inventory categories to WF-02 stages when templates exist

---

*OPS Document Foundation v1 · Reality Audit & Template Program · 2026-06-10.*
