# MARS Website Factory — Source Discovery v1

**Status:** **documented** — mandatory pre-audit layer for Website Factory frontend production.  
**Not:** runtime file scanner, automated inventory daemon, content extraction engine, or replacement of [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md).

**Version:** v1  
**Date:** 2026-06-14  
**Provenance:** FP-0002 Shpigovsky.ru — process defect: foundation and design audit started before full incoming-material inventory.

**Scope boundary:** Website Factory **documentation only**. Does **not** modify FP-0002 workspace artefacts, frontend code, or project working documents.

**Related (detail — do not duplicate here):**

| Concern | Document |
|---------|----------|
| Production workflow order | [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) |
| Production mode charter | [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) |
| Design → Frontend mapping | [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) |
| Source lineage layers | [source-lineage-model.md](source-lineage-model.md) |
| Source interpretation | [source-interpretation-governance.md](source-interpretation-governance.md) |
| Source confidence | [source-confidence-model.md](source-confidence-model.md) |

**FP-0002 instance (read-only reference):** [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) · [FP-0002-DESIGN-FRONTEND-MAPPING-QA-RECORD-v1.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-DESIGN-FRONTEND-MAPPING-QA-RECORD-v1.md).

---

## 1. Purpose

Source Discovery is **mandatory** because design packs are rarely limited to visual PDFs. Real projects ship **mixed incoming folders** — structure spreadsheets, content documents, technical briefs, client notes, and asset bundles — that govern **information architecture**, **navigation**, **URL strategy**, **page inventory**, and **internal linking** as strongly as visual design governs layout.

**Without Source Discovery, agents and operators risk:**

| Failure mode | Effect |
|--------------|--------|
| **Partial intake** | Agent audits PDF only; site structure XLSX, content docs, or briefs remain invisible |
| **False design completeness** | Design Audit REPORT passes while IA, menu, and page list are **SAFE UNKNOWN** or wrong |
| **Foundation on incomplete evidence** | Production Standards Draft, shell, and UI Demo built before structural sources are read |
| **Late rework** | High-authority source discovered mid-build invalidates page order, URLs, and shell navigation |
| **Authority inversion** | Visual PDF treated as sole SSOT while structural spreadsheet already defines page graph |

**Source Discovery answers one question before any Design Audit:**

> **What material exists in the project intake, where does it live, what authority does it carry, and has every registered source been read?**

**Honesty boundary:** Source Discovery is **human-operated** inventory and registration in Cursor. No claim of automated folder crawl, checksum sync, or enforcement engine unless a project explicitly adopts tooling.

---

## 2. Position in workflow

Source Discovery is **Phase A0** — it precedes Design Audit and all downstream frontend work.

```text
PHASE A0  Source Discovery
    ↓
PHASE A   Design Audit
    ↓
PHASE B   Fresh Frontend Workspace Creation
    ↓
PHASE C   Desktop Shell (Header · Footer · Main placeholder)
    → Operator Approval → Stable Backup v0
    ↓
PHASE D   UI Demo / Visual Foundation
    → Operator Approval → Stable Backup v1
    ↓
PHASE E   Operator chooses first production page
    ↓
PHASE F   Production Page Build (one block · approval · backup per block)
    ↓
PHASE G   Page Completion (modals · hidden states · QA)
    → Operator Approval → Stable Backup
    ↓
PHASE H   Mobile Version
    → Operator Approval → Stable Backup
    ↓
PHASE I   Next Page (reuse components · return to E or F as needed)
```

### Phase A0 — Source Discovery

| # | Activity | Output |
|---|----------|--------|
| A0.1 | Scan project intake paths (`INCOMING/`, design folder, operator-provided paths) | Candidate file list |
| A0.2 | Register every material source as **SOURCE-NNN** | Source Inventory Register |
| A0.3 | Assign **Authority Classification** per source | Authority column in register |
| A0.4 | Set **Source Status** — READ / PARTIALLY READ / NOT READ | Status column in register |
| A0.5 | **Confirm production mode** from passport — branch checklist emphasis per [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md): **PIXEL_PERFECT** → visual SSOT mandatory; **TEMPLATE_ART** → blueprint/content path mandatory. Undeclared → **STOP** | Mode branch note in register |
| A0.6 | File **Source Discovery REPORT** | `# REPORT — <project> source discovery` |

**Gate:** **No Design Audit (Phase A)** until every registered source is **READ** or **PARTIALLY READ with documented scope** — see §5 Mandatory Audit Rule. **NOT READ** on any registered source **blocks** Phase A. **Production mode undeclared** **blocks** all downstream frontend work.

**Blocks if missing:** Design Audit, Production Standards Draft, Gulp workspace creation, any HTML.

### Phase A — Design Audit (after A0)

Design Audit **consumes** the Source Inventory Register. It does **not** replace A0.

| # | Activity | Output |
|---|----------|--------|
| A.1 | Cross-reference design sources from register (PDF, Figma, PNG, mixed) | Design source priority list |
| A.2 | Cross-reference structural sources (XLSX, briefs, IA docs) | Page inventory draft + URL/menu implications |
| A.3 | Block inventory draft — reusable blocks per page | Block ID list |
| A.4 | Design Audit REPORT — gaps, conflicts, SAFE UNKNOWN | `# REPORT — <project> design audit` |

**Authority:** [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) · [source-interpretation-governance.md](source-interpretation-governance.md).

---

## 3. Source Inventory Model

Every discovered material **must** be registered. Ad-hoc references in chat or REPORT prose **do not** satisfy inventory — each source gets a stable ID.

### Register fields (minimum)

| Field | Required | Notes |
|-------|----------|-------|
| **SOURCE-ID** | Yes | `SOURCE-001` … `SOURCE-NNN` — monotonic per project |
| **Label** | Yes | Human-readable type name |
| **Path** | Yes | Repo-relative or operator-stored path |
| **Format** | Yes | PDF, XLSX, DOCX, Figma URL, PNG pack, etc. |
| **Authority** | Yes | Low · Medium · High · Critical — see §7 |
| **Status** | Yes | READ · PARTIALLY READ · NOT READ — see §4 |
| **Scope notes** | If PARTIALLY READ | Which sheets, pages, or sections were read |
| **IA impact** | If applicable | menu · URL · page list · linking · content structure |
| **Visual impact** | If applicable | layout · typography · components · breakpoints |

### Canonical source type examples

| SOURCE-ID | Label | Typical path pattern | Primary impact |
|-----------|-------|----------------------|----------------|
| **SOURCE-001** | PDF Desktop Design | `INCOMING/01_DESIGN/*.pdf` | Visual layout, typography, components |
| **SOURCE-002** | PDF Mobile Design | `INCOMING/01_DESIGN/*mobile*.pdf` | Responsive layout, mobile shell |
| **SOURCE-003** | Site Structure XLSX | `INCOMING/02_CONTENT/*.xlsx` | IA, menu, URLs, page inventory, linking |
| **SOURCE-004** | Technical Brief | `INCOMING/03_BRIEF/` or operator path | Constraints, integrations, non-visual requirements |
| **SOURCE-005** | Content Documents | `INCOMING/02_CONTENT/` | Copy structure, headings, page body requirements |
| **SOURCE-006** | Client Notes | `INCOMING/08_CLIENT_MATERIALS/` | Decisions, clarifications, ad-hoc authority |
| **SOURCE-007** | Assets | `INCOMING/04_ASSETS/` or `src/assets/design/` | Images, icons, logos, fonts |

**FIG / Figma multi-brand warning:** When SOURCE-001 or embedded `.fig` drives logo selection, apply [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) — **do not** assume first image node is the chartered logo (`ASSET_IDENTITY_COLLISION`).

**Rule:** IDs are **per project**, not global Factory registry. Reuse labels for consistency; assign new SOURCE-NNN for every distinct file or bundle.

### Intake scan scope (minimum)

Agents **must** inspect at least:

```text
<project-pack>/INCOMING/
  01_DESIGN/
  02_CONTENT/
  03_BRIEF/          (if present)
  04_ASSETS/         (if present)
  08_CLIENT_MATERIALS/
src/assets/design/   (if workspace exists)
operator-provided paths cited in session prompt
```

**SAFE UNKNOWN:** If operator confirms intake is complete but a expected folder is empty, register **SOURCE-NNN — Expected intake (absent)** with Status **NOT READ** and Authority per type — blocks audit until resolved or operator waiver documented.

---

## 4. Source Status

Each registered source carries exactly one status:

| Status | Definition | Allowed for Phase A gate |
|--------|------------|--------------------------|
| **READ** | Agent or operator has opened and reviewed the full source (all sheets, pages, or files in bundle) | **Yes** |
| **PARTIALLY READ** | Material scope is large; documented subset read; remainder listed with reason | **Yes** — only if partial scope is **explicitly sufficient** for current phase and remainder marked with impact note |
| **NOT READ** | Source registered but content not reviewed | **No** — **blocks** Design Audit |

### Status transition rules

1. New file discovered → register → **NOT READ**.
2. Agent reads file → update to **READ** or **PARTIALLY READ** with scope notes.
3. **PARTIALLY READ → READ** before Production Standards Approval if source is **High** or **Critical** authority.
4. Status changes must appear in Source Discovery REPORT or project inventory amendment — not only in chat.

### PARTIALLY READ constraints

| Authority | PARTIALLY READ allowed at A0 gate? |
|-----------|-------------------------------------|
| **Critical** | **No** — must be **READ** before Phase A |
| **High** | **No** — must be **READ** before Phase A |
| **Medium** | Yes — if unread portion documented as non-blocking for IA/visual audit |
| **Low** | Yes — with scope note |

---

## 5. Mandatory Audit Rule

**Design Audit (Phase A) is forbidden while any registered source remains NOT READ.**

| Condition | Verdict | Action |
|-----------|---------|--------|
| All sources **READ** | Gate **PASS** | Proceed to Phase A |
| Critical/High sources **READ**; only Low/Medium **PARTIALLY READ** with scope | Gate **PASS** | Proceed; document partial scope in A.4 |
| Any source **NOT READ** | Gate **FAIL** | STOP — read or operator-waive with documented cause |
| Expected intake absent (registered, NOT READ) | Gate **FAIL** | Operator places file or issues explicit waiver |

**Operator waiver (exception only):**

- Operator may waive a **Low** or **Medium** source for Phase A only.
- **High** and **Critical** sources — **no waiver** for Design Audit; must be **READ**.
- Waiver must cite SOURCE-ID, authority, reason, and approving operator in REPORT.

**Agent obligation:** If asked to start Design Audit, Production Standards, shell, or UI Demo without A0 register — **refuse** and request Source Discovery completion first.

---

## 6. Source Update Rule

Incoming material is not frozen at project start. Operators may add files after Phase A0, Phase A, or mid-build.

**When a new file appears after Source Discovery REPORT:**

| Step | Agent action |
|------|--------------|
| 1 | **Register** new **SOURCE-NNN** immediately — do not reference only in passing |
| 2 | Set Status **NOT READ** until reviewed |
| 3 | Perform **impact assessment** — see table below |
| 4 | Update Source Inventory Register + amendment REPORT |
| 5 | If impact is material — **STOP** current work; escalate to operator before continuing |

### Impact assessment matrix

| Impact area | Material if new source affects… | Required response |
|-------------|--------------------------------|-------------------|
| **IA / structure** | Page list, menu, URL map, breadcrumbs, linking | Re-run Phase A items A.1–A.2; may invalidate Production Standards §page inventory |
| **Visual** | Layout, shell, tokens, components | Re-run affected Design Audit blocks; may invalidate Phase C–D |
| **Content** | Copy, headings, legal text | Update page blueprints; may affect Phase F blocks already approved |
| **Assets** | Logos, icons, photography | Replace assets; may affect Phase D calibration |
| **Constraints** | Integrations, CMS, legal, analytics | Update Production Standards; may block Phase B approval |

**Authority escalation:** New **Critical** or **High** source after foundation approval → treat as **dependency invalidation** per project governance; do not silently merge.

**REPORT expectation:** `# REPORT — <project> source discovery amendment` with SOURCE-ID, impact verdict (**none · localized · structural · full re-audit**), and operator decision.

---

## 7. Authority Classification

Authority classifies how strongly a source may override agent inference, prior drafts, or visual-only assumptions.

| Class | Definition | Examples | Phase A0 requirement |
|-------|------------|----------|----------------------|
| **Low** | Supplementary; fills gaps only | Misc client notes, reference screenshots, competitor links | Register; READ optional before A if waived |
| **Medium** | Influences copy, SEO nuance, or secondary pages | Content docs, keyword lists, blog drafts | Register; READ or documented PARTIALLY READ |
| **High** | Governs site structure, navigation, URLs, page set, linking | **Site structure XLSX**, approved IA spreadsheet, sitemap doc | Register; **READ** mandatory before Phase A |
| **Critical** | Governs visual implementation truth for layout and components | **PDF design** (desktop/mobile), primary Figma when named SSOT | Register; **READ** mandatory before Phase A |

### Default authority by source type

| Source type | Default authority | Notes |
|-------------|-------------------|-------|
| PDF Desktop Design | **Critical** | Visual SSOT when PDF is primary design pack |
| PDF Mobile Design | **Critical** | Same; responsive SSOT |
| Site Structure XLSX | **High** | Governs IA — not optional intake |
| Technical Brief | **High** | May include non-visual constraints affecting architecture |
| Content Documents | **Medium** | May rise to **High** if they define page set |
| Client Notes | **Low** | May rise to **High** if operator declares decision authority |
| Assets | **Medium** | **Critical** for brand logo/mark when design depends on exact asset |

**Conflict rule:** When **High** structural source and **Critical** visual source disagree (e.g. XLSX lists page not shown in PDF), record **conflict** in Design Audit REPORT — do not silently prefer PDF. Escalate per [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md).

**PDF is Visual Source of Truth** ([website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) R-02) applies to **visual** claims — not to page inventory, menu, or URL graph when **High** structural source exists.

---

## 8. FP-0002 Lessons Learned

### L-SD-01 — Site structure XLSX missed in early audit path

| Field | Value |
|-------|-------|
| **Project** | FP-0002 Shpigovsky.ru |
| **Source** | `INCOMING/02_CONTENT/Предварит структура и спрос.xlsx` |
| **Authority** | **High** — sheets `Структура`, `Спрос набросок` govern IA and search-demand intake |
| **Defect** | Agent path toward design audit and foundation proceeded with **PDF-centric** intake; XLSX not in early design-audit scope |
| **Effect** | Page inventory, menu, URL strategy, and linking risked **PDF inference** instead of spreadsheet SSOT; Production Standards v1 marked Excel intake **SAFE UNKNOWN** (file not found in workspace at that time) |
| **Recovery evidence** | v2/v3 Production Standards integrated Excel §10–11 after file placed in `INCOMING/02_CONTENT/` — proves source was material, not optional |

**Process lesson:** A design pack containing PDF **plus** content-folder XLSX is **mixed authority intake**. PDF alone cannot satisfy Source Discovery. **SOURCE-003 Site Structure XLSX** must be registered and **READ** before Design Audit.

### L-SD-02 — Inventory timing vs Production Standards timing

| Field | Value |
|-------|-------|
| **Defect** | Structural source integrated at Production Standards normalization — **after** implicit design/foundation pressure had already started |
| **Lesson** | Source Discovery belongs **before** Design Audit (A0), not as a side effect of Production Standards Draft (Phase B) |

### L-SD-03 — Register ≠ reference

| Field | Value |
|-------|-------|
| **Defect** | Source cited in mapping QA or standards prose without prior **SOURCE-NNN** register and read status |
| **Lesson** | Citation in downstream docs does not retroactively satisfy A0; register first, read second, audit third |

**FP-0002 workspace:** **read-only** for Factory evolution — this section captures lesson only; does not edit FP-0002 artefacts.

---

## 9. Changes Required

This document is the **authority** for Phase A0. Downstream docs should **reference** it, not duplicate full inventory rules.

| Consumer | Required adjustment |
|----------|---------------------|
| [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) | Insert Phase A0 before Phase A; add gate and lesson cross-reference |
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | Mapping chain assumes sources are **discovered and registered** — no change required in v1 body; future v2 may add A0 pointer |
| [source-lineage-model.md](source-lineage-model.md) | Complementary — lineage classifies authority layers; A0 registers **files** before lineage interpretation |
| Project REPORT templates | Add Source Inventory Register table to A0 REPORT |

**Not required:** Changes to FP-0002 workspace, frontend code, OPERATIONAL-INDEX (separate task after operator-verified pilot).

---

## 10. Mandatory rules (A0)

| # | Rule |
|---|------|
| **SD-01** | **Source Discovery before Design Audit** — Phase A0 complete with REPORT before Phase A |
| **SD-02** | **Every material file registered** — SOURCE-NNN; no orphan references |
| **SD-03** | **No NOT READ at audit gate** — Design Audit blocked until resolved |
| **SD-04** | **Critical and High sources fully READ** — no PARTIALLY READ waiver at A0 gate |
| **SD-05** | **New file → register → impact assessment** — Source Update Rule mandatory |
| **SD-06** | **PDF does not subsume structure XLSX** — separate SOURCE-IDs; separate authority |
| **SD-07** | **Intake scan is explicit** — list paths scanned; empty folders documented |

---

## 11. Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Created | 2026-06-14 |
| Author | Website Factory documentation (FP-0002 process defect extraction) |
| Commit / push | Not performed |
| FP-0002 modified | **No** |
| Frontend modified | **No** |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v1 — Source Discovery Layer: inventory model, status, mandatory audit rule, update rule, authority classification, FP-0002 lessons |
