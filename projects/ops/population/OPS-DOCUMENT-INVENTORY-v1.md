# OPS Document Inventory v1

**Status:** **structure only** — empty register; awaiting first audit population pass.  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-10  
**Parent:** [OPS-DOCUMENT-FOUNDATION-v1.md](../foundation/OPS-DOCUMENT-FOUNDATION-v1.md) · [OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md](../foundation/OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md)  
**Is not:** populated document list, template library, contract archive, or ATLAS register.

---

## 1. Purpose

Provide the **canonical empty inventory structure** for studio operational documents.

**Current state:** **0 rows** — no documents audited, no files guessed, no placeholder entries.

**Population rule:** Rows enter this register **only** through a human audit pass per [OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md](../foundation/OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md).

---

## 2. Register summary

| Metric | Count |
|--------|-------|
| Total inventory rows | **0** |
| ACTIVE | **0** |
| LEGACY | **0** |
| UNKNOWN | **0** |
| Template candidates (YES) | **0** |

*Updated on first audit population pass.*

---

## 3. Field schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **Document ID** | `DOC-####` | Yes | Stable sequential identifier |
| **File Name** | string | Yes | Discovered file name with extension |
| **Category** | enum | Yes | One of taxonomy labels — see [OPS-DOCUMENT-TAXONOMY-v1.md](../foundation/OPS-DOCUMENT-TAXONOMY-v1.md) |
| **Current Usage** | text | Yes | How document is used in current operations |
| **Owner** | text | Yes | Operational responsibility |
| **Status** | enum | Yes | `ACTIVE` · `LEGACY` · `UNKNOWN` |
| **Quality** | enum | Yes | `GOOD` · `PARTIAL` · `WEAK` · `UNKNOWN` |
| **Improvement Needed** | text | Yes | Specific improvements or `None` |
| **Template Candidate** | enum | Yes | `YES` · `NO` · `MAYBE` |
| **Notes** | text | No | ATLAS refs, paths, audit pass ID, version notes |

---

## 4. Category allowed values

| Value | Taxonomy ID |
|-------|-------------|
| Contracts | CAT-01 |
| Addendums | CAT-02 |
| Acts | CAT-03 |
| Invoices | CAT-04 |
| Commercial Proposals | CAT-05 |
| Reports | CAT-06 |
| Requisites | CAT-07 |
| Internal Templates | CAT-08 |
| Other | CAT-09 |

---

## 5. Inventory table

**Population status:** **EMPTY** — awaiting audit pass `AUD-DOC-01` (or successor).

| Document ID | File Name | Category | Current Usage | Owner | Status | Quality | Improvement Needed | Template Candidate | Notes |
|-------------|-----------|----------|---------------|-------|--------|---------|-------------------|-------------------|-------|
| — | — | — | — | — | — | — | — | — | *No rows — foundation pass only* |

---

## 6. Population instructions (for future audit pass)

1. Confirm storage scope and audit pass ID
2. Discover files per [OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md](../foundation/OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md) §3
3. Assign `DOC-0001` sequentially — do not skip or reuse IDs
4. Enter one row per logical document in §5 table
5. Update §2 register summary counts
6. Publish audit pass report under `projects/ops/reports/`
7. Do **not** redesign documents or create templates in the same pass

---

## 7. Boundaries

| Rule | Requirement |
|------|-------------|
| **INV-01** | No guessed rows — evidence only |
| **INV-02** | No ATLAS entity duplication — reference AGR-*/ORG-* in **Notes** |
| **INV-03** | No contract text or requisites SoT in inventory |
| **INV-04** | Status **UNKNOWN** preferred over false **ACTIVE** |
| **INV-05** | Inventory updates require audit pass report cross-reference |

---

## 8. Cross-reference

| Document | Relationship |
|----------|--------------|
| [OPS-DOCUMENT-FOUNDATION-v1.md](../foundation/OPS-DOCUMENT-FOUNDATION-v1.md) | Ownership and three-layer model |
| [OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md](../foundation/OPS-DOCUMENT-AUDIT-METHODOLOGY-v1.md) | How to populate this register |
| [OPS-DOCUMENT-TAXONOMY-v1.md](../foundation/OPS-DOCUMENT-TAXONOMY-v1.md) | Category definitions |

---

*OPS Document Inventory v1 · Structure only · 2026-06-10.*
