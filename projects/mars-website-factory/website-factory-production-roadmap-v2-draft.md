# MARS Website Factory — Production Roadmap v2 (draft)

**Status:** **draft** — documented production workflow derived from **FP-0002** real-project experience.  
**Not:** runtime orchestration, automated phase router, workflow engine, or replacement of [website-factory-workflow-v0.md](website-factory-workflow-v0.md) intake→delivery chain.

**Version:** v2-draft  
**Date:** 2026-06-14  
**Provenance:** FP-0002 Shpigovsky.ru — M1 baseline, M2 false PASS, PRE-M2 reset, Start Sequence v1, Enforcement Pack v1, Foundation Governance evolution (2026-06-13 — 2026-06-14).

**Scope boundary:** Website Factory **documentation only**. Does **not** modify FP-0002 workspace artefacts, frontend code, or project working documents.

**Related (detail — do not duplicate here):**

| Concern | Document |
|---------|----------|
| Production mode charter | [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) |
| Source Discovery (A0) | [website-factory-source-discovery-v1.md](website-factory-source-discovery-v1.md) |
| Shell-first gate (v1) | [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) |
| Visual Foundation composition | [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) |
| Production Standards | [production-standards-governance-v1.md](production-standards-governance-v1.md) |
| Design → Frontend mapping | [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) |
| Layout shell law | [layout-shell-governance.md](layout-shell-governance.md) |
| Enforcement (compiled CSS) | [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) |
| Operator Visual Approval Law | [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) |
| Layout Spec Law | [layout-spec-law-v1.md](layout-spec-law-v1.md) — mandatory composition artifact before HTML/CSS |
| Group Decomposition Law | [group-decomposition-law-v1.md](group-decomposition-law-v1.md) — discrete GROUP-IDs per ROW before Layout Spec |
| **Canonical Clean Shell** | [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) — mandatory empty shell (`HEADER/MAIN/FOOTER NOT STARTED`) before Layout Spec |
| Workspace reset / archive | [workspace-reset-governance.md](workspace-reset-governance.md) — **Workspace Archive Rule** §8 |
| Freeze / backup discipline | [freeze-discipline-v1.md](freeze-discipline-v1.md) |
| Strategic Factory roadmap | [roadmap.md](roadmap.md) |

**FP-0002 instance (read-only reference):** [FP-0002-FRONTEND-START-SEQUENCE-v1.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-FRONTEND-START-SEQUENCE-v1.md) · [FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md) · [FP-0002-RESET-COMPLETE.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-RESET-COMPLETE.md).

---

## 1. Purpose

This document fixes a **new production workflow order** for Website Factory **frontend implementation** — the sequence that proved necessary during FP-0002 after the v1 implicit order produced **false progress**, **false PASS**, and a **full workspace reset**.

**v2 answers:**

1. Why the previous order failed in practice.
2. What order operators and agents must follow from design intake through multi-page production.
3. Mandatory rules that survived FP-0002 audit.
4. Lessons to carry into the next Factory projects.

**Honesty boundary:** Phases A–I describe **human-operated** Cursor work with operator HITL. No claim of automated phase transitions, backup daemons, or enforcement engines unless a project explicitly adopts tooling.

---

## 2. Why the previous order was ineffective

The pre–v2 implicit order — visible in early FP-0002 M2 work and in generic Factory paths that jump from **Design Handoff → Frontend Production (Home)** — failed for documented reasons:

### 2.1 Foundation treated as product progress

| Symptom | Effect |
|---------|--------|
| Large **UI Demo / Foundation Demo** built before stable shell | Operator saw “a page” and assumed the site was advancing |
| Tokens and component SCSS present in `src/` | Gates could PASS on **structure** without **compiled output** fidelity |
| No commercial page started | Stakeholders perceived stall despite heavy engineering work |

**FP-0002 evidence:** M2 Foundation Demo (14 sections, 6 component SCSS files) was removed on reset — it did not survive audit as a stable baseline ([FP-0002-RESET-COMPLETE.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-RESET-COMPLETE.md)).

**Lesson:** Foundation is **infrastructure**, not **product**. Progress is measured by **operator-approved milestones** tied to shell, reusable UI, and first production page — not by file count in `src/`. **Technical PASS on any visual stage does not substitute for operator visual acceptance** — see [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md).

### 2.2 Wrong build sequence inside foundation

| Prior implicit order | Problem |
|---------------------|---------|
| UI Demo / typography first, shell later | Header/footer grid and container law untested before component library |
| Home requested early | Hero (BLK-007) leaked into foundation; **HEADER ≠ HERO** violated |
| Global styles deferred or mixed with page work | Shell markup lacked token-backed CSS; rework cascaded |

**v1 protocol partial fix:** [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) introduced shell-first — but FP-0002 proved **Header/Footer desktop must precede UI Demo**, not merely coexist in the same sprint.

### 2.3 False PASS on governance gates

| Gap | FP-0002 M2 audit finding |
|-----|--------------------------|
| Source-level token presence | Compiled CSS could diverge — gates still PASS |
| Structural completeness | WF-GRID / WF-LAYOUT checked without inline-style / Operator Law sweep |
| Foundation Health high | **ROOT COMPLIANCE** failures undetected until post-hoc audit |

**Closed by:** [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) (EG-01–EG-05). **v2 rule:** no milestone backup without enforcement-aligned REPORT.

### 2.4 No stable recovery points

| Symptom | Effect |
|---------|--------|
| Long multi-section M2 pass without operator checkpoint | Rollback required full PRE-M2 mirror from external storage |
| Agent continued after partial approval | Irreversible drift; reset cost high |

**FP-0002 evidence:** Restore source `WEBSITE-FACTORY-FP-0002-PRE-M2-SNAPSHOT-2026-06-13-v1` — without snapshot, recovery scope was **SAFE UNKNOWN**.

### 2.5 Agent-chosen page order

| Symptom | Effect |
|---------|--------|
| Default “start with Home” | Wrong for catalog/service-first sites; wasted foundation alignment |
| Agent inferred priority from design pack order | Misaligned with operator commercial intent |

**v2 rule:** **Operator chooses** first production page (Phase E). Agent **must ask** — never assume Home.

### 2.6 Workflow v0 stage gap

[website-factory-workflow-v0.md](website-factory-workflow-v0.md) Stages 1–11 cover intake→delivery but **under-specify** the **frontend sub-chain** between Design Handoff and first commercial page. v2 fills that gap without replacing S01–S15.

---

## 3. New production workflow (Phases A–I)

```text
PHASE A0  Source Discovery
    ↓
PHASE A   Design Audit
    ↓
PHASE B   Fresh Frontend Workspace Creation → **Canonical Clean Shell v1**
    ↓
PHASE C  Desktop Shell (Header · Footer · Main placeholder)
    → Layout Spec (Header · Footer) → Operator APPROVED → HTML/CSS
    → Operator Visual Approval → Stable Backup v0
    ↓
PHASE D  UI Demo / Visual Foundation
    → Operator Approval → Stable Backup v1
    ↓
PHASE E  Operator chooses first production page
    ↓
PHASE F  Production Page Build (Layout Spec per block → APPROVED → one block · approval · backup per block)
    ↓
PHASE G  Page Completion (modals · hidden states · QA)
    → Operator Approval → Stable Backup
    ↓
PHASE H  Mobile Version
    → Operator Approval → Stable Backup
    ↓
PHASE I  Next Page (reuse components · return to E or F as needed)
```

**Desktop-first default:** Phases C–G target **desktop ≥1024px** unless project Production Standards state otherwise. Mobile is **Phase H**, not interleaved block-by-block — reduces responsive rework during pixel audit.

---

### PHASE A0 — Source Discovery

**Purpose:** Full inventory of **all** incoming project material **before** any design audit or code — PDF alone is insufficient.

| # | Activity | Output |
|---|----------|--------|
| A0.1 | Scan intake paths (`INCOMING/`, design folder, operator paths) | Candidate file list |
| A0.2 | Register every source as **SOURCE-NNN** with authority class | Source Inventory Register |
| A0.3 | Set read status — READ / PARTIALLY READ / NOT READ | Status per source |
| A0.4 | Source Discovery REPORT | `# REPORT — <project> source discovery` |

**Authority:** [website-factory-source-discovery-v1.md](website-factory-source-discovery-v1.md).

**Gate:** **No NOT READ** on any registered source; **Critical** and **High** sources must be **READ**. **No Design Audit (Phase A)** until A0.4 filed (or explicit operator waiver per Source Discovery §5).

**Blocks if missing:** Design Audit, Production Standards Draft, Gulp workspace, any HTML.

---

### PHASE A — Design Audit

**Purpose:** Establish what design and structural evidence **means** for implementation — **after** Source Discovery (A0) register exists.

| # | Activity | Output |
|---|----------|--------|
| A.1 | Cross-reference design sources from A0 register (PDF, Figma, PNG, mixed) | Design source priority list |
| A.2 | Cross-reference structural sources (XLSX, briefs, IA docs) — page inventory draft | Page list + Missing Pages Register |
| A.3 | Block inventory draft — reusable blocks per page | Block ID list |
| A.4 | Design Audit REPORT — gaps, conflicts, SAFE UNKNOWN | `# REPORT — <project> design audit` |

**Authority:** [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) · [source-interpretation-governance.md](source-interpretation-governance.md) · [website-factory-source-discovery-v1.md](website-factory-source-discovery-v1.md).

**Gate:** A0 complete; design and structural sources catalogued in register. **No Gulp workspace** until A.4 filed (or explicit operator waiver).

**Blocks if missing:** Production Standards Draft (Phase B prep), any HTML.

---

### PHASE B — Fresh Frontend Workspace Creation

**Purpose:** Clean Gulp workspace with **no residue** from prior attempts.

**Canonical baseline:** [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) — `desktop-shell.html` shows **HEADER NOT STARTED / MAIN NOT STARTED / FOOTER NOT STARTED** only; no starter demo, ui-demo, tokens, or chrome until Layout Spec APPROVED.

| # | Activity | Output |
|---|----------|--------|
| B.1 | Create workspace from starter / template | `workspaces/<project-slug>-frontend/` — on **full cycle restart**, archive prior tree per [workspace-reset-governance.md](workspace-reset-governance.md) §8 **Workspace Archive Rule**; **one ACTIVE** canonical name only |
| B.2 | Production Standards **Draft** (C-01–C-16) | `<PROJECT>-PRODUCTION-STANDARDS-DRAFT-vN.md` |
| B.3 | **DESIGN → FRONTEND MAPPING QA** on Draft | Mapping QA record PASS |
| B.4 | Production Standards **Approval** (Lead sign-off) | `<PROJECT>-APPROVAL-vN.md` |
| B.5 | `npm install` + `npm run build` — empty/minimal entry | Build PASS evidence |

**Authority:** [production-standards-governance-v1.md](production-standards-governance-v1.md) · [workspace-reset-governance.md](workspace-reset-governance.md).

**Rule:** If rebuilding after failed pass → **fresh tree or audited reset** — do not layer “fixes” on false PASS residue.

**Explicit exclusions:** No Home, no hero, no commercial sections.

---

### PHASE C — Desktop Shell

**Purpose:** Persistent layout frame — **HEADER ≠ HERO**. Main holds placeholder only.

**Layout Spec Gate (mandatory):** Before C.1 or C.2 HTML/CSS — file Layout Spec for Header and Footer; operator **APPROVED** per [layout-spec-law-v1.md](layout-spec-law-v1.md). **Forbidden:** `Visual SSOT → HTML/CSS` without approved Layout Spec.

| # | Deliverable | Notes |
|---|-------------|-------|
| C.0 | **Layout Spec** — Header + Footer | Zones, rows, grouping, container model — operator **APPROVED** before markup |
| C.1 | **Header** (desktop) | Layout partial; implement **only** approved Layout Spec |
| C.2 | **Footer** (desktop) | Layout partial; implement **only** approved Layout Spec |
| C.3 | **Main placeholder** | Minimal `main` content — “shell ready” marker, not UI Demo |
| C.4 | Shell page entry | e.g. `ui-demo.html` — **not** `index.html` Home |

**Authority:** [layout-shell-governance.md](layout-shell-governance.md) · [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md).

**Minimum global CSS:** Reset, variables, shell-only styles required for header/footer render — full token demo deferred to Phase D.

#### Operator Approval — Phase C

Operator confirms:

- Header/footer match **PDF visual source** at desktop width
- Container width, padding, logo placement per Production Standards
- No hero block, no PG-001 content in codebase

#### Stable Backup v0

| Field | Requirement |
|-------|-------------|
| **Label** | `stable-backup-v0-shell` |
| **Scope** | `src/partials/layout/`, shell page entry, shell SCSS, approved Production Standards ref |
| **Evidence** | `# REPORT — <project> stable backup v0`; build PASS; screenshot desktop shell |
| **Storage** | Operator-chosen snapshot path (e.g. `C:\AI MARS STORAGE\website-factory\snapshots\`) — **not** automated |
| **Freeze** | Recommend L1 on layout partials per [freeze-discipline-v1.md](freeze-discipline-v1.md) |

---

### PHASE D — UI Demo / Visual Foundation

**Purpose:** Extract and verify **reusable UI** inside `main` before any production page.

**Mandatory categories** (presence on demo URL inside `main`):

| Category | Notes |
|----------|-------|
| Typography | H1–H6, body, lists, links, blockquote per Production Standards |
| HTML content styles | Prose, spacing samples, section gap labels |
| Buttons | Primary, secondary, states |
| Forms | Inputs, labels, validation states — radius per standards |
| Cards | Default card radius and padding |
| Tables | If in standards or design pack |
| Alerts | Status variants |
| FAQ | Accordion pattern per progressive enhancement rules |
| Media | Image aspect, video embed sample if in design |
| Other reusable UI | Badges, tags, breadcrumbs sample — per project inventory |

**Authority:** [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) · [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) · [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) (compiled CSS spot-check).

**Gate:** Design Calibration PASS + Foundation QA chain before Phase E.

#### Operator Approval — Phase D

Operator confirms (after technical REPORT — **DESIGN CALIBRATION PASS ≠ OPERATOR APPROVAL**):

- Every §3 category from Visual Foundation Contract **visible** on demo URL
- Compiled CSS matches Production Standards (not source-only)
- RU typography / no word-splitting — PASS or documented SAFE UNKNOWN
- **OPERATOR VISUAL REVIEW** block — **OPERATOR VISUAL ACCEPT — ACCEPT** per [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md)

#### Stable Backup v1

| Field | Requirement |
|-------|-------------|
| **Label** | `stable-backup-v1-visual-foundation` |
| **Scope** | v0 scope + all UI Demo sections/components + foundation SCSS |
| **Evidence** | `# REPORT — <project> stable backup v1`; enforcement gates EG-01–EG-04 cited |
| **Freeze** | L1 on demo sections; L3 prep on shared tokens |

---

### PHASE E — Operator chooses first production page

**Purpose:** Align production order with **operator commercial intent**, not agent default.

**Agent MUST ask operator:**

```text
Which page should we build first?

- Home
- Catalog
- Service
- Other (operator specifies page ID / slug)
```

| Rule | Detail |
|------|--------|
| **Agent cannot choose** | No default to Home; no inference from PDF sort order |
| **Record** | Decision in project REPORT + Production Charter amendment if needed |
| **Design required** | If chosen page lacks design → SAFE UNKNOWN + placeholder policy (PD-09 pattern) — operator waives or parks |

**Output:** Approved **first production page ID** (e.g. PG-001 Home, PG-003 Catalog hub, PG-00X Service leaf).

---

### PHASE F — Production Page Build

**Purpose:** Implement chosen page **one visual block at a time**.

| Rule | Detail |
|------|--------|
| **Layout Spec before block HTML** | Per-block Layout Spec → operator **APPROVED** — [layout-spec-law-v1.md](layout-spec-law-v1.md) |
| **One block at a time** | Single section/partial per agent delivery |
| **Operator approval after every block** | Wait for `approved` / `continue` / `fix this block` — **OPERATOR VISUAL REVIEW REQUIRED** per [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) |
| **Stable backup after every approved block** | Named snapshot per block — `stable-backup-v1-<page>-<block-id>` |
| **Reuse Phase D components** | No re-inventing buttons/forms/cards |
| **PDF fidelity** | Block layout from design PDF — no normalization without authority |
| **No mobile yet** | Desktop layout only until Phase H |

**Per-block REPORT must include:**

- Changed files
- Build PASS
- **OPERATOR VISUAL REVIEW** block (§5.7) — **TECHNICAL PASS** separate from **OPERATOR VISUAL ACCEPT**
- Design source reference (PDF page / frame)
- Pixel / Design QA status or explicit partial

**Authority:** [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) · [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md).

---

### PHASE G — Page Completion

**Purpose:** Close the page — states and QA missing from block-by-block pass.

| # | Activity | Notes |
|---|----------|-------|
| G.1 | Modals | Per design; progressive enhancement |
| G.2 | Popups / overlays | z-index vs shell law |
| G.3 | Hidden states | Empty, error, loading — **SAFE UNKNOWN** if not in design |
| G.4 | Missing design elements | Escalate — do not invent |
| G.5 | QA | Design Completeness → Design QA Matrix → Pixel Fidelity → Production PASS |

#### Operator Approval — Phase G

Operator confirms desktop page **production-complete** per QA chain and **OPERATOR VISUAL ACCEPT — ACCEPT** (**PAGE QA PASS ≠ OPERATOR APPROVAL**).

#### Stable Backup — page complete

| Field | Requirement |
|-------|-------------|
| **Label** | `stable-backup-v2-<page-id>-desktop-complete` |
| **Scope** | Full page partials, page SCSS, related JS modules |
| **Freeze** | L1 per approved block; L2 prep when all pages done |

---

### PHASE H — Mobile Version

**Purpose:** Responsive implementation **after** desktop page approval — avoids dual-axis rework.

| # | Activity | Notes |
|---|----------|-------|
| H.1 | Mobile header / footer | Condensed shell per design |
| H.2 | Page block responsive | Per breakpoint in Production Standards |
| H.3 | Mobile QA | Viewport list ≤1023px (or project breakpoint) |

#### Operator Approval — Phase H

Operator confirms mobile matches design or documented SAFE UNKNOWN waivers.

#### Stable Backup — mobile complete

| Field | Requirement |
|-------|-------------|
| **Label** | `stable-backup-v3-<page-id>-mobile-complete` |
| **Scope** | Responsive SCSS + shell mobile rules for this page |

---

### PHASE I — Next Page

**Purpose:** Repeat production with **reuse** — do not rebuild foundation.

```text
Operator chooses next page (return to PHASE E question)
    ↓
PHASE F — blocks (reuse components + styles from D and prior pages)
    ↓
PHASE G — page completion
    ↓
PHASE H — mobile
    ↓
PHASE I — again until page inventory complete
```

| Rule | Detail |
|------|--------|
| **Reuse** | Components, tokens, shell, patterns from Phases C–D and prior pages |
| **No foundation rebuild** | Unless operator authorizes reset with cause |
| **New page types** | May need new blocks — still one block per pass |
| **Cross-page QA** | Grid alignment header / sections / footer (WF-GRID-005) |

---

## 4. Mandatory rules

Non-negotiable for all projects adopting v2:

| # | Rule | Authority / note |
|---|------|------------------|
| **R-01** | **Header ≠ Hero** | [layout-shell-governance.md](layout-shell-governance.md) — shell partials own navigation; hero is page-local |
| **R-02** | **PDF is Visual Source of Truth** | When PDF exists in design pack, PDF measurements beat agent interpretation; Figma wins only when explicitly primary in Production Decisions |
| **R-03** | **No invention if design exists** | Implement what design shows; beautification drift forbidden |
| **R-04** | **SAFE UNKNOWN if design absent** | Record gap; STOP or placeholder per operator policy — no silent fill |
| **R-05** | **Stable backup after every approved milestone** | v0, v1, per-block, page desktop, page mobile — operator-stored snapshot + REPORT |
| **R-06** | **Operator chooses page order** | Phase E question mandatory; agent never auto-selects Home |
| **R-07** | **Operator approves every production block** | Phase F stop after each block |
| **R-08** | **Foundation before Home** | Phases A0–D complete before first PG-* production page |
| **R-13** | **Source Discovery before Design Audit** | Phase A0 complete; no NOT READ sources; Critical/High sources READ — [website-factory-source-discovery-v1.md](website-factory-source-discovery-v1.md) |
| **R-09** | **Compiled output verification** | Enforcement Pack gates on foundation and page QA — source-only PASS invalid |
| **R-10** | **Desktop before mobile** | Phase H after Phase G desktop PASS |
| **R-11** | **Authority order** | Project Production Standards → Operator Laws → Factory Governance → Pattern Library → Industry → Agent Preference |
| **R-12** | **No `dist/` edits** | Rebuild only; backups snapshot `src/` + config |
| **R-14** | **Layout Spec before HTML/CSS** | Header, Footer, Hero, any block, any page — operator **APPROVED** Layout Spec required — [layout-spec-law-v1.md](layout-spec-law-v1.md) |

---

## 5. Lessons learned from FP-0002

| # | Lesson | Evidence | v2 response |
|---|--------|----------|-------------|
| **L-01** | **Foundation alone is not product progress** | M2 demo removed on reset; operator perceived activity without shippable page | Phases C–D labeled infrastructure; Phase E+ = product; backups at real milestones |
| **L-02** | **Header/Footer before UI Demo** | Start Sequence v1 + M2 sequence drift | Phase C shell → Phase D demo — explicit order |
| **L-03** | **Component extraction before Home** | Home blocks assumed buttons/cards not yet calibrated | Phase D mandatory categories; Phase F reuses |
| **L-04** | **Production workflow must follow page reality** | 11 page types, missing genotyping design, service L4 depth | Phase E operator choice; SAFE UNKNOWN for missing design |
| **L-05** | **False PASS is expensive** | M2 ROOT CAUSE AUDIT → full PRE-M2 restore | Enforcement Pack + backup discipline |
| **L-06** | **Production Standards v3 is SSOT** | Normalization v1 conflicts resolved by charter | Phase B Approval before code |
| **L-07** | **Reset requires external snapshot** | `AI MARS STORAGE` snapshot saved recovery | R-05 stable backups at operator storage |
| **L-08** | **Agent must not default to Home** | Repeated “сверстай главную” redirects | Phase E explicit ask |
| **L-09** | **Structural XLSX is not optional intake** | `INCOMING/02_CONTENT/Предварит структура и спрос.xlsx` — IA/menu/URL source; missed in early PDF-centric audit; v1 standards SAFE UNKNOWN until file found | Phase A0 Source Discovery; SOURCE-003 class **High**; READ before Phase A |
| **L-10** | **Visual SSOT without Layout Spec causes composition failure** | FP-0002 Header — agent interpreted design internally; radically wrong chrome; caught only at operator screenshot compare | [layout-spec-law-v1.md](layout-spec-law-v1.md); Phase C.0 / Phase F Layout Spec gate; [FP-0002-layout-spec-lesson-v1.md](FP-0002-layout-spec-lesson-v1.md) |
| **L-11** | **Beautiful starter shell is more dangerous than empty shell** | FP-0002 RESET V3 — rich gulp-starter / foundation demo invited reuse without Layout Spec | [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md); [FP-0002-clean-shell-lesson-v1.md](FP-0002-clean-shell-lesson-v1.md) |
| **L-12** | **Row count without group decomposition breaks composition** | FP-0002 JPG test — 2 rows correct; ROW 1 collapsed to «CONTACT BLOCK» | [group-decomposition-law-v1.md](group-decomposition-law-v1.md); [FP-0002-group-decomposition-lesson-v1.md](FP-0002-group-decomposition-lesson-v1.md) |
| **L-13** | **First image in FIG ≠ chartered logo** | FP-0002 Header — node `1:880` (Skinerica, `de219c6e…`) auto-selected; correct mark `1:6720` (Шпиговский дом, `262f79db…`) in same `Шпиговский.fig` | [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md); Brand Asset Detection Layer; forbid **FIRST IMAGE = LOGO** |

**Promoted to Factory system (2026-06-13 — 2026-06-17):** Shell-first protocol, Visual Foundation Contract, Enforcement Pack, Authority Order, Failure Attribution Model, **Layout Spec Law**, **Canonical Clean Shell v1**, **Group Decomposition Law**, **Asset Identity Collision** — v2 **sequences** them; does not replace their detail.

---

## 6. Relationship to existing docs

| Layer | Role |
|-------|------|
| **website-factory-workflow-v0.md** | Macro chain S01–S15 (intake → delivery) — **unchanged** |
| **website-factory-source-discovery-v1.md** | Phase A0 — v2 **requires** before Design Audit |
| **frontend-shell-first-start-protocol-v1.md** | Phases B–D detail — v2 **aligns and extends** with backup + Phase E–I |
| **FP-0002 Start Sequence v1** | Project instance — **read-only**; v2 generalizes its lessons |
| **roadmap.md** | Strategic maturity phases 0–7 — v2 is **operational** frontend sub-roadmap |

**Supersedes (interpretation only):** Implicit “Home first” and “UI demo before shell” orders in ad-hoc prompts and early M2 specs.

---

## 7. Proposed future adoption level

Per [operationalization-maturity-levels.md](../../governance/operationalization-maturity-levels.md):

| Stage | Maturity label | Condition |
|-------|----------------|-----------|
| **Now (v2-draft)** | **Documentation-only** + **Governance-described** | Document authored from FP-0002 audit; not yet default in OPERATIONAL-INDEX Core Run |
| **After FP-0002 M2+ under v2** | **Operator-verified** | One full Phase A0–H cycle with REPORT evidence and stored backups |
| **After second greenfield project** | **Operationally repeatable** | Second operator repeats A–I without reset; lessons captured in REPORT only |
| **Not claimed** | Locally executable / Runtime-scoped | No phase router code, no backup automation |

**Recommended adoption path:**

1. **Pilot:** FP-0002 next M2 pass follows v2 phases C→D with v0/v1 backups — **do not edit** FP-0002 docs; operator cites v2 in session prompt.
2. **Index:** Add v2 pointer to [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) Core Run after operator-verified pass — **separate task**.
3. **Promote draft → v2:** When FP-0002 foundation completes with v0/v1 backups and no reset — rename drop `-draft`.

---

## 8. Document control

| Field | Value |
|-------|-------|
| Version | v2-draft |
| Created | 2026-06-14 |
| Author | Website Factory documentation (FP-0002 experience extraction) |
| Commit / push | Not performed |
| FP-0002 modified | **No** |
| Frontend modified | **No** |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v2-draft — created from FP-0002 M1/M2/reset audit; Phases A–I, mandatory rules, lessons, adoption proposal |
| 2026-06-14 | v2-draft — Phase A0 Source Discovery inserted before Design Audit; R-13, L-09; pointer to [website-factory-source-discovery-v1.md](website-factory-source-discovery-v1.md) |
| 2026-06-14 | v2-draft — Layout Spec Law integration: Phase C.0/F gates, R-14, L-10; [layout-spec-law-v1.md](layout-spec-law-v1.md) |
| 2026-06-14 | v2-draft — Canonical Clean Shell v1 pointer: Phase B baseline, L-11; [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) |
| 2026-06-15 | v2-draft — Group Decomposition Law pointer: L-12; [group-decomposition-law-v1.md](group-decomposition-law-v1.md) |
