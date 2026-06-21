# OPS Document Taxonomy v1

**Status:** **documented** — practical category vocabulary for studio document audit.  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-10  
**Parent:** [OPS-DOCUMENT-FOUNDATION-v1.md](OPS-DOCUMENT-FOUNDATION-v1.md)  
**Is not:** legal classification system, accounting chart of accounts, or file-system folder map.

---

## 1. Purpose

Provide a **practical, studio-oriented taxonomy** for classifying operational documents during audit and future template work.

**Rules:**

- One primary category per inventory row
- Secondary tags allowed in **Notes** only — not separate taxonomy levels in v1
- Categories describe **document type**, not storage location or ATLAS entity type
- When uncertain → category **OTHER** + explain in **Notes**

---

## 2. Category definitions

### CAT-01 — Contracts

**Definition:** Primary legal or commercial agreements establishing the relationship, scope, or terms of engagement between studio and counterparty.

**Examples (illustrative, not exhaustive):**

- Service agreement
- Framework contract
- NDA (as standalone agreement)
- Retainer agreement

**Not in this category:** addendums (→ CAT-02), acts (→ CAT-03), invoices (→ CAT-04)

**ATLAS link:** Agreement entity (AGR-*) references expected; file lives in Storage layer.

---

### CAT-02 — Addendums

**Definition:** Amendments, supplements, or annexes that modify or extend an existing contract without replacing it.

**Examples:**

- Additional agreement (дополнительное соглашение)
- Scope amendment
- Rate change annex
- Technical specification annex bound to parent contract

**ATLAS link:** May reference parent AGR-*; OPS inventory should note parent relationship in **Notes**.

---

### CAT-03 — Acts

**Definition:** Acceptance, delivery, or completion documents confirming performed work or transferred deliverables.

**Examples:**

- Act of completed works (акт выполненных работ)
- Delivery acceptance act
- Transfer act
- Closing act for project phase

**Not in this category:** invoices (→ CAT-04), internal reports (→ CAT-06)

---

### CAT-04 — Invoices

**Definition:** Payment request documents — bills, счета, invoices — issued to counterparty or received from supplier.

**Examples:**

- Outgoing invoice to client
- Incoming invoice from vendor
- Proforma invoice (if used operationally)

**Boundary:** OPS tracks preparation and routing; **accounting authority is outside OPS**.

---

### CAT-05 — Commercial Proposals

**Definition:** Pre-contract commercial offers, quotations, and proposals not yet bound as agreements.

**Examples:**

- Commercial proposal (КП)
- Quotation
- Estimate for client approval
- Pitch deck document (if maintained as formal doc artifact)

**Status note:** Often **LEGACY** or superseded once contract signed — audit should record transition in **Notes**.

---

### CAT-06 — Reports

**Definition:** Operational or client-facing report documents produced on a recurring or ad-hoc basis.

**Examples:**

- Monthly client report (deliverable file)
- SEO report export
- Project status report
- Analytics summary attached to client communication

**OPS link:** WF-01 Monthly Reporting may produce artifacts in this category.

---

### CAT-07 — Requisites

**Definition:** Counterparty or studio identity and banking detail documents used for invoicing and contractual headers.

**Examples:**

- Company requisites card (реквизиты)
- Bank details sheet
- Counterparty profile document

**ATLAS link:** Canonical requisites SoT is **ATLAS** — inventory row describes **file artifact**, not authoritative values. Requisites in templates must match ATLAS or be **SAFE UNKNOWN**.

---

### CAT-08 — Internal Templates

**Definition:** Studio-internal document shells, boilerplate, or master templates not specific to one counterparty.

**Examples:**

- Blank contract template
- Standard act template
- Invoice template shell
- Email-to-document conversion boilerplate

**Template candidate:** Usually **YES** — primary source for future OPS template library.

---

### CAT-09 — Other

**Definition:** Documents that do not fit categories CAT-01–CAT-08 without forced misclassification.

**Requirement:** **Notes** field **must** explain why **OTHER** was chosen and suggest a future category if taxonomy expands.

**Examples that may land here:**

- Power of attorney (доверенность)
- Internal policy document
- License agreement (non-client)
- Correspondence archive

---

## 3. Category summary table

| ID | Category | Primary use in OPS | Typical ATLAS link |
|----|----------|-------------------|-------------------|
| CAT-01 | Contracts | WF-02 closing, audit | AGR-* |
| CAT-02 | Addendums | WF-02 closing, audit | AGR-* parent ref |
| CAT-03 | Acts | WF-02 closing, audit | AGR-* + PRJ-* |
| CAT-04 | Invoices | WF-02 routing | ORG-* / LE-* |
| CAT-05 | Commercial Proposals | Pre-sale ops | ORG-* (prospect) |
| CAT-06 | Reports | WF-01 delivery | AGR-* + PRJ-* |
| CAT-07 | Requisites | Document prep | ATLAS requisites |
| CAT-08 | Internal Templates | Template program | — |
| CAT-09 | Other | Catch-all with mandatory Notes | Varies |

---

## 4. Category selection rules (audit)

| Rule ID | Rule |
|---------|------|
| **TX-01** | Assign **one** primary category per inventory row |
| **TX-02** | If document serves dual purpose (e.g. act + invoice combo) → primary category by **dominant operational purpose**; note secondary in **Notes** |
| **TX-03** | Template versions of executed documents → classify by **document type** (CAT-08 if blank shell; CAT-01 if filled contract template) |
| **TX-04** | Scanned signed PDF vs editable DOCX → same category; note format in **Notes** |
| **TX-05** | Do not invent subcategories in v1 — use **Notes** for granularity |
| **TX-06** | **UNKNOWN** status does not block category assignment — category and status are independent |

---

## 5. Future taxonomy expansion (deferred)

Possible v2 categories — **not authorized** without explicit charter:

| Proposed | Rationale for deferral |
|----------|------------------------|
| Correspondence | Needs volume assessment from first audit |
| HR / employment | Outside current studio ops scope — **SAFE UNKNOWN** |
| Tax / regulatory filings | Accounting authority — outside OPS |
| EDO export artifacts | Depends on EDO provider attestation |

Expansion requires: audit evidence, foundation amendment, inventory migration note.

---

## 6. Cross-reference

| Document | Relationship |
|----------|--------------|
| [OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md](OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md) | Uses **Category** field with this taxonomy |
| [OPS-DOCUMENT-INVENTORY-v1.md](../population/OPS-DOCUMENT-INVENTORY-v1.md) | **Category** column values = CAT-01..CAT-09 labels |
| [OPS-WF-02-DOCUMENT-CLOSING-v1.md](../workflows/OPS-WF-02-DOCUMENT-CLOSING-v1.md) | Workflow stages consume categories operationally |

---

*OPS Document Taxonomy v1 · 2026-06-10.*
