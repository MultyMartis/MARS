# OPS Document Audit Methodology v1

**Status:** **documented** — human-operated audit procedure for studio document inventory.  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-10  
**Parent:** [OPS-DOCUMENT-FOUNDATION-v1.md](OPS-DOCUMENT-FOUNDATION-v1.md) · [OPS-DOCUMENT-TAXONOMY-v1.md](OPS-DOCUMENT-TAXONOMY-v1.md)  
**Is not:** automated scanner, legal review protocol, or template redesign workflow.

---

## 1. Purpose

Define the **repeatable human audit procedure** for discovering, classifying, and assessing all operational documents used by the studio.

**Audit answers:**

| Question | Audit output field |
|----------|-------------------|
| What documents exist? | Document ID, File Name |
| What type are they? | Category |
| Are they still used? | Current Usage, Status |
| Who is responsible? | Owner |
| How good are they? | Quality |
| What needs work? | Improvement Needed, Template Candidate |
| Context? | Notes |

**This pass:** methodology and field definitions only — **no audit execution**, **no population**.

---

## 2. Audit principles

| Principle | Requirement |
|-----------|-------------|
| **Evidence-based** | Every inventory row must trace to a real file or attested absence — no guessing |
| **No redesign** | Audit records current state; does not rewrite documents |
| **No template creation** | Template Candidate is a **flag**, not an authorization to build |
| **ATLAS separation** | Inventory describes files; ATLAS describes agreements and identity |
| **Human-operated** | No automation, OCR pipeline, or runtime claimed in v1 |
| **Incremental** | Partial audit is valid — mark incomplete scope in pass report |

---

## 3. Audit procedure (steps)

### Step 1 — Scope definition

| Action | Output |
|--------|--------|
| Identify storage locations to scan (folders, cloud, EDO exports) | Scope list in audit pass report |
| Identify excluded zones (personal, archived backups) | Exclusion list |
| Set audit pass ID (e.g. `AUD-DOC-01`) | Referenced in inventory **Notes** |

**If storage root is unknown → STOP at scope definition; record **SAFE UNKNOWN** in pass report.**

### Step 2 — Discovery

| Action | Output |
|--------|--------|
| List files found in scope | Candidate file list |
| Record file name, path pointer, format | Pre-inventory worksheet |
| Deduplicate (same file, multiple copies) | One row per logical document; copies noted |

### Step 3 — Classification

| Action | Output |
|--------|--------|
| Assign primary category per [OPS-DOCUMENT-TAXONOMY-v1.md](OPS-DOCUMENT-TAXONOMY-v1.md) | **Category** field |
| Link to ATLAS refs if identifiable (AGR-*, ORG-*, PRJ-*) | **Notes** — not separate column in v1 |
| Assign **Owner** (role or named human) | **Owner** field |

### Step 4 — Usage and status assessment

| Action | Output |
|--------|--------|
| Determine whether document is actively used in current operations | **Current Usage** |
| Assign lifecycle status | **Status** (ACTIVE / LEGACY / UNKNOWN) |
| If usage unclear → **UNKNOWN** status, not assumed ACTIVE | Honest gap recording |

### Step 5 — Quality and improvement assessment

| Action | Output |
|--------|--------|
| Assess document quality against operational needs (not legal review) | **Quality** |
| Record specific improvement needs | **Improvement Needed** |
| Flag template candidacy | **Template Candidate** (YES / NO / MAYBE) |

### Step 6 — Inventory registration

| Action | Output |
|--------|--------|
| Assign stable Document ID | **Document ID** (see §4) |
| Enter row in [OPS-DOCUMENT-INVENTORY-v1.md](../population/OPS-DOCUMENT-INVENTORY-v1.md) | Populated register |
| Cross-check row count vs discovery list | Reconciliation note in pass report |

### Step 7 — Pass report

| Action | Output |
|--------|--------|
| Summarize counts by category and status | Audit pass report under `projects/ops/reports/` |
| List blockers and **SAFE UNKNOWN** items | Recommendations for next pass |

---

## 4. Field definitions

### Document ID

| Property | Specification |
|----------|---------------|
| Format | `DOC-####` (zero-padded four digits) |
| Assignment | Sequential per inventory; never reused |
| Stability | ID persists even if file renamed — update **File Name** only |
| Example | `DOC-0001` |

### File Name

| Property | Specification |
|----------|---------------|
| Content | Actual file name as discovered (include extension) |
| Path | Storage path pointer in **Notes** if not obvious — not a separate column in v1 |
| Multiple versions | One row per version OR one row with version list in **Notes** — auditor chooses consistently per pass |

### Category

| Property | Specification |
|----------|---------------|
| Values | One of: `Contracts`, `Addendums`, `Acts`, `Invoices`, `Commercial Proposals`, `Reports`, `Requisites`, `Internal Templates`, `Other` |
| Maps to | CAT-01..CAT-09 in [OPS-DOCUMENT-TAXONOMY-v1.md](OPS-DOCUMENT-TAXONOMY-v1.md) |
| Rule | Exactly one primary category per row |

### Current Usage

| Property | Specification |
|----------|---------------|
| Purpose | Describe how the document is used **today** in studio operations |
| Values | Free text — concise operational description |
| Examples | `Active client contract template for SEO retainers`, `Last used 2024-Q3`, `Reference only`, `Not found in recent WF-02 cases` |
| Rule | Evidence-based; if unknown → state `Usage unknown — not observed in current ops` |

### Owner

| Property | Specification |
|----------|---------------|
| Purpose | Operational responsibility for maintaining or using this document |
| Values | Role name, team, or named human |
| Examples | `Document Operations`, `Executive Assistant`, `Account Manager`, `External accountant (reference only)` |
| Rule | OPS role names from [OPS-AGENT-DECOMPOSITION-v1.md](OPS-AGENT-DECOMPOSITION-v1.md) preferred when applicable |

### Status

| Property | Specification |
|----------|---------------|
| Purpose | Lifecycle visibility for operational use |
| Values | **ACTIVE** · **LEGACY** · **UNKNOWN** |

| Status | Definition |
|--------|------------|
| **ACTIVE** | Currently used or required in live operations; safe to reference in new work |
| **LEGACY** | Superseded, expired, or retained for archive only — not for new operational use without review |
| **UNKNOWN** | Usage or currency not yet determined — requires follow-up |

**Rule:** Prefer **UNKNOWN** over false **ACTIVE**.

### Quality

| Property | Specification |
|----------|---------------|
| Purpose | Operational fitness assessment — not legal adequacy |
| Values | **GOOD** · **PARTIAL** · **WEAK** · **UNKNOWN** |

| Quality | Definition |
|---------|------------|
| **GOOD** | Fit for current operational use; complete for its purpose |
| **PARTIAL** | Usable with known gaps (missing fields, outdated branding, inconsistent structure) |
| **WEAK** | Significant operational problems; should not be used without rework |
| **UNKNOWN** | Not yet assessed |

### Improvement Needed

| Property | Specification |
|----------|---------------|
| Purpose | Specific, actionable improvement notes from audit |
| Values | Free text; `None` if no improvement identified |
| Examples | `Update requisites block`, `Align with current contract terms`, `Consolidate duplicate versions`, `Add ATLAS AGR reference field` |
| Rule | Describe **what** needs improvement — not the redesigned text |

### Template Candidate

| Property | Specification |
|----------|---------------|
| Purpose | Flag whether document should inform or become a future OPS template |
| Values | **YES** · **NO** · **MAYBE** |

| Value | Definition |
|-------|------------|
| **YES** | Strong candidate for template library — stable, reusable structure |
| **NO** | Instance-specific or not suitable as template |
| **MAYBE** | Potential template after cleanup or consolidation |

**Rule:** Template Candidate is advisory only — does not authorize template creation.

### Notes

| Property | Specification |
|----------|---------------|
| Purpose | Context, ATLAS links, storage paths, version history, audit pass reference |
| Values | Free text |
| Recommended content | `AUD-DOC-01` · `AGR-0005` · `path: ...` · `duplicate of DOC-0003` |

---

## 5. Status decision guide

```
                    ┌─────────────────┐
                    │  File discovered │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        Used in live    Superseded /    Cannot determine
        ops today?      archive only?   usage?
              │              │              │
              ▼              ▼              ▼
          ACTIVE          LEGACY         UNKNOWN
```

---

## 6. Quality decision guide

| Signal | Suggested quality |
|--------|-------------------|
| Used successfully in recent WF-02 / WF-01 with no operator complaints | **GOOD** |
| Usable but missing fields, old logo, or inconsistent with ATLAS refs | **PARTIAL** |
| Broken structure, wrong counterparty, or unsafe to send | **WEAK** |
| Not yet opened or reviewed | **UNKNOWN** |

---

## 7. Anti-patterns (forbidden during audit)

| Anti-pattern | Why forbidden |
|--------------|---------------|
| Inventing documents not found in storage | Violates evidence-based principle |
| Assigning **ACTIVE** without usage evidence | Creates false operational confidence |
| Rewriting document text during audit | Audit ≠ redesign |
| Creating templates during audit | Template work is separate charter |
| Duplicating ATLAS agreement rows as document inventory substitutes | Violates DOC-AD-01 |
| Storing full requisites in inventory as SoT | ATLAS is requisites SoT |

---

## 8. Audit pass deliverables (future execution)

When audit is executed (not in this foundation pass):

| Deliverable | Location |
|-------------|----------|
| Populated inventory rows | [OPS-DOCUMENT-INVENTORY-v1.md](../population/OPS-DOCUMENT-INVENTORY-v1.md) |
| Audit pass report | `projects/ops/reports/REPORT-ops-document-audit-<pass-id>.md` |
| Scope and exclusion record | Inside audit pass report |
| Template candidate summary | Inside audit pass report |

---

## 9. Relationship to other OPS artifacts

| Artifact | Relationship |
|----------|--------------|
| [OPS-DOCUMENT-INVENTORY-v1.md](../population/OPS-DOCUMENT-INVENTORY-v1.md) | Output register for audit rows |
| [OPS-DOCUMENT-TAXONOMY-v1.md](OPS-DOCUMENT-TAXONOMY-v1.md) | Category vocabulary |
| [OPS-WF-02-DOCUMENT-CLOSING-v1.md](../workflows/OPS-WF-02-DOCUMENT-CLOSING-v1.md) | Workflow that will consume audited templates later |
| [OPS-ATLAS-RELATIONSHIP-v1.md](OPS-ATLAS-RELATIONSHIP-v1.md) | ATLAS reference rules during classification |

---

*OPS Document Audit Methodology v1 · 2026-06-10.*
