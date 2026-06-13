# MARS Website Factory — Frontend Design Completeness Governance v1

**Status:** **documented** — Foundation-level **canonical completeness law** for verifying that **all design entities** present in approved design evidence are **represented** in frontend implementation before fidelity QA and Production PASS.  
**Not:** runtime inventory scanner, DOM diff engine, CI gate, computer vision, or automated section detector.

**Purpose:** Close the gap where frontend may **PASS** pixel fidelity and QA domains on **implemented slices** while **entire design entities** (sections, components, states, assets) are **absent**. Completeness is a **separate gate** from mapping layer completeness, token fidelity, layout discipline, and per-entity pixel audit.

**Problem statement (canonical example):**

| Design entity inventory (page) | Frontend entity inventory (page) |
|--------------------------------|----------------------------------|
| Header · Hero · Advantages · Services · FAQ · CTA · Footer | Header · Hero · Services · Footer |

Pixel QA on existing blocks may **PASS**; **Design Completeness Audit** → **FAIL** (missing Advantages, FAQ, CTA).

**Authority order (canonical):** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md)

| Rank | Layer | Role in completeness |
|------|-------|----------------------|
| **1** | **Project Production Standards** | Scope of chartered pages, block bindings (C-11), asset list (C-09), open questions (C-13–C-14) |
| **2** | **Approved Operator Laws (OL-01–OL-07)** | Does not waive missing entities — layout law applies only to **present** entities |
| **3** | **This doc** + peer Factory governance | Entity registries, comparison model, audit gate, severity, verdict |
| **4** | **Layout Pattern Library (LP-* / WF zones)** | Pattern IDs attach to **matched** section entities — not substitute for presence |
| **5–6** | Industry Best Practice · Agent Preference | **Never** override ranks 1–4; **never** shrink scope silently |

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules) — register on integration wave.

**Related (integration — not duplication):**

| Document | Role |
|----------|------|
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | Pre-code **mapping layer** completeness (L-01–L-08) — feeds Design Entity Registry |
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | Draft + Approval; C-11 layout zones; charter scope |
| [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) | **Fidelity** QA on **present** implementation — runs **after** completeness PASS |
| [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) | Numeric/visual variance on **matched** entities |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Stage chain placement |
| [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) | Foundation **composition** completeness (demo categories) — subset of this model |
| [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md) | Blueprint block list — authoritative input for page/section entities |
| [block-registry-v0.md](block-registry-v0.md) | Normalized `block_id` vocabulary for section/card entities |
| [registries.md](registries.md) | Site type, block registry — cross-ref for entity naming |

**Honesty boundary:** This document is **human-operated governance**. It does **not** claim an in-repo inventory engine, linter, or automated Design Completeness PASS unless a project explicitly adopts checklists as tooling.

---

## 1. Purpose

Answer:

> **Does frontend implementation include every design entity required by approved design evidence, project charter, and Production Standards — before we judge how well each entity is built?**

| In scope | Out of scope |
|----------|--------------|
| **Presence** of pages, sections, components, forms, navigation, cards, tables, modals, states, assets, interactive elements | Pixel-perfect **quality** of present entities (peer: QA Matrix, Pixel Fidelity) |
| **Pairing** design inventory ↔ frontend inventory with stable IDs | Autonomous DOM or Figma parsing |
| **Verdict** PASS / PASS WITH NOTES / FAIL blocking Production PASS when Critical gaps remain | SEO copy strategy, legal claims, conversion hypothesis |
| **Severity** for missing, extra, or mis-scoped entities | WF-GRID / WF-LAYOUT numeric compliance (peer gates) |
| REPORT evidence for audit | Runtime enforcement products |

**Distinction from peer “completeness” concepts:**

| Peer concept | What it checks | This doc |
|--------------|----------------|----------|
| Mapping L-01–L-08 layer completeness | Extraction **draft** before Approval | **Implementation** presence after production |
| Visual Foundation §3 composition | Demo page **category** checklist | Full page/ site entity inventories |
| DQ-10 Content Fidelity | **Copy** and counts inside present blocks | **Structural** entity presence |
| DQ-06 Components (QA Matrix) | **Fidelity** of implemented components | Whether component **exists at all** |

---

## 2. Authority

### 2.1 Sources of truth for Design Entity Registry

Build the registry from **approved** inputs in priority order:

| Priority | Source | Typical entities captured |
|----------|--------|---------------------------|
| **A1** | Active design source frames / exports (Figma, PDF, PNG per viewport) | Sections, components, states visible in artboards |
| **A2** | **Page Blueprint** + **block_id** list | Chartered sections per page |
| **A3** | **Design handoff contract** | Components, forms, modals, asset manifest |
| **A4** | **Project Production Standards** C-11 (layout zones), C-09 (assets), C-08 (components) | Named zones and component patterns |
| **A5** | Production Decisions C-12 / C-13 / C-14 | Scope cuts, waivers, UNKNOWN with policy |

**Forbidden:** Agent memory, unstated chat, or starter template defaults as registry rows without A1–A5 promotion.

### 2.2 Sources of truth for Frontend Entity Registry

| Priority | Source | Evidence |
|----------|--------|----------|
| **F1** | Built `src/` tree — pages, partials, sections, components | File paths + include graph |
| **F2** | Built `dist/` output at audit viewport(s) | Rendered DOM regions (human or DevTools) |
| **F3** | Project asset folders (`src/img`, `src/svg`, `src/fonts`, `src/favicon`) | Wired assets |
| **F4** | JS modules initializing interactive behavior | `data-*` hooks, module init map |

**Rule:** Frontend registry documents **what shipped**, not what is planned.

### 2.3 Conflict resolution

| Conflict | Winner |
|----------|--------|
| Design shows section; blueprint omits | **HITL** — resolve charter before audit; do not silent-drop |
| Blueprint lists block; design frame absent | Blueprint + C-12 decision — record Assumed or UNKNOWN |
| Production Standards waives entity (C-13) | Waived row marked **OUT OF SCOPE** — not FAIL |
| Frontend has extra section not in design | **Extra entity finding** — Major or Observation per §8 |

---

## 3. Inputs

### 3.1 Mandatory inputs (Design Completeness Audit)

| ID | Input | Minimum content |
|----|-------|-----------------|
| **IN-DC01** | **Design Entity Registry** (§5) | All applicable categories populated or explicitly OUT OF SCOPE / UNKNOWN |
| **IN-DC02** | **Frontend Entity Registry** (§6) | Same scope as IN-DC01 — page or slice under audit |
| **IN-DC03** | Approved design source set | S1–S6 priority per mapping governance |
| **IN-DC04** | Project Production Standards (approved) | Version + scope (pages, breakpoints) |
| **IN-DC05** | Build evidence | `npm run build` PASS for audited slice |
| **IN-DC06** | Comparison scope declaration | Page URL(s), viewport(s), locale, slice name |

### 3.2 Optional but recommended inputs

| Input | Use |
|-------|-----|
| Page Blueprint / handoff contract | Row IDs and `block_id` alignment |
| Mapping QA record | Trace L-01 section order → registry rows |
| Visual Foundation / Foundation QA reports | Shell-level entities pre-checked |

### 3.3 Entry criteria (gate open)

| ID | Criterion |
|----|-----------|
| **EC-01** | Page or production slice declared **implementation-complete** by operator (not mid-block WIP) |
| **EC-02** | Production Standards Approval PASS for project |
| **EC-03** | Design Entity Registry **frozen for audit** — version ID or timestamp in REPORT |
| **EC-04** | Frontend Entity Registry extracted from current `src/` + `dist/` |
| **EC-05** | No open **scope UNKNOWN** without C-13/C-14 policy for entities in comparison set |

**Not an entry criterion:** Frontend Design QA Matrix PASS — completeness runs **before** full fidelity matrix at page level (§11).

---

## 4. Outputs

| Output | Description |
|--------|-------------|
| **Design Completeness Audit Report** | Human-readable REPORT block (§10) |
| **Verdict** | PASS · PASS WITH NOTES · FAIL (§9) |
| **Finding list** | Each gap: entity ID, category, severity, evidence, disposition |
| **Updated registries** | Optional revision of Frontend Entity Registry post-fix |
| **Production PASS signal** | Completeness PASS or PASS WITH NOTES required before matrix final PASS (§9) |

---

## 5. Design Entity Registry

### 5.1 Definition

The **Design Entity Registry** is the **authoritative inventory of entities the design (and charter) require** for the audited scope — independent of implementation quality.

### 5.2 Minimum categories

Every registry **must** use these categories (empty category → explicit **N/A for scope**):

| Category ID | Category | Registry captures (minimum) |
|-------------|----------|----------------------------|
| **DE-PAGES** | **Pages** | Page IDs, routes, template type, in-scope flag |
| **DE-SECTIONS** | **Sections** | Top-to-bottom section list per page; `block_id` when applicable |
| **DE-COMPONENTS** | **Components** | Reusable UI parts (buttons, badges, chips, nav items) required by design |
| **DE-FORMS** | **Forms** | Form blocks, field sets, submit flows |
| **DE-NAV** | **Navigation** | Header nav, footer nav, in-page anchors, breadcrumbs |
| **DE-CARDS** | **Cards** | Card patterns and **count** per grid/list |
| **DE-TABLES** | **Tables** | Data/comparison tables |
| **DE-MODALS** | **Modals** | Overlays, drawers, lightboxes |
| **DE-STATES** | **States** | Required UI states per interactive entity (default, hover, focus, open, error, …) |
| **DE-ASSETS** | **Assets** | Logos, icons, photos, illustrations, favicon, fonts |
| **DE-INTERACTIVE** | **Interactive Elements** | Accordion, tabs, slider, carousel, video, map embed, sticky CTA |

### 5.3 Row schema (minimum fields)

| Field | Required | Notes |
|-------|----------|-------|
| `entity_id` | Yes | Stable ID — e.g. `home.section.faq`, `global.header.nav` |
| `category` | Yes | One of §5.2 |
| `display_name` | Yes | Human label matching design |
| `design_source_ref` | Yes | Frame, export, or artboard path |
| `page_id` | When applicable | DE-PAGES key |
| `block_id` | When applicable | [block-registry-v0.md](block-registry-v0.md) |
| `count` | When applicable | Cards, list items, FAQ items |
| `state_matrix` | For DE-STATES / interactive | List required states or UNKNOWN |
| `scope_status` | Yes | `IN_SCOPE` · `OUT_OF_SCOPE` · `WAIVED` · `UNKNOWN` |
| `authority_ref` | When waived/unknown | C-12 / C-13 / C-14 pointer |

### 5.4 Lifecycle hooks

| Phase | Action |
|-------|--------|
| **Mapping Draft** | Seed DE-SECTIONS, DE-COMPONENTS from L-01, L-05, L-07, L-08 |
| **Mapping QA** | Verify registry covers L-01 section order — gaps → mapping FAIL |
| **Standards Approval** | Freeze scope rows; waivers in C-13 |
| **Pre-audit refresh** | Add entities from late design revisions only with HITL + version bump |
| **Audit** | Compare to Frontend Entity Registry |

---

## 6. Frontend Entity Registry

### 6.1 Definition

The **Frontend Entity Registry** is the **inventory of entities present in implementation** for the same scope as the Design Entity Registry.

### 6.2 Categories

**Same category set as §5.2** — enables 1:1 comparison.

### 6.3 Row schema (minimum fields)

| Field | Required | Notes |
|-------|----------|-------|
| `entity_id` | Yes | **Must match** design row when representing same entity |
| `category` | Yes | Same taxonomy as design |
| `implementation_ref` | Yes | Partial path, section include, component file |
| `dom_hook` | Recommended | Section class, `id`, or `data-*` root |
| `rendered_verified` | Yes | `yes` / `no` / `partial` — dist check at audit viewport |
| `asset_path` | For DE-ASSETS | Actual file wired |
| `state_implemented` | For interactive | Subset of required states |
| `notes` | Optional | Stub, placeholder policy, feature flag |

### 6.4 Extraction method (honest scope)

| Method | Allowed claim |
|--------|---------------|
| Include graph + section files | **Structural presence** |
| Open `dist/` page + visual/DOM scan | **Rendered presence** |
| Agent guess without dist open | **SAFE UNKNOWN** — not PASS |

---

## 7. Comparison model

### 7.1 Matching rules

Compare registries **by `entity_id` first**, then **category + page_id + display_name** fallback with explicit human ack (avoid fuzzy auto-merge).

| Design row | Frontend row | Result |
|------------|--------------|--------|
| IN_SCOPE | Matching `entity_id`, rendered_verified=yes | **MATCH** |
| IN_SCOPE | Matching id, rendered_verified=partial | **PARTIAL** — finding |
| IN_SCOPE | No row | **MISSING** — finding |
| IN_SCOPE | Row exists, wrong page placement | **MISPLACED** — Major |
| WAIVED / OUT_OF_SCOPE | Absent | **OK** (document waiver) |
| UNKNOWN | Absent | **UNKNOWN** — does not auto-FAIL if C-14 policy allows deferral |
| — | Extra row not in design | **EXTRA** — finding |

### 7.2 Category-level rollup

| Rollup | Rule |
|--------|------|
| **Page completeness** | All IN_SCOPE DE-PAGES have full section chain |
| **Section completeness** | All IN_SCOPE DE-SECTIONS MATCH |
| **Component completeness** | All IN_SCOPE DE-COMPONENTS MATCH or PARTIAL dispositioned |
| **State completeness** | Required states ⊆ implemented states (subset check) |
| **Asset completeness** | Every IN_SCOPE DE-ASSETS row has wired file — no production placeholders |

### 7.3 Count-sensitive entities

For DE-CARDS, DE-TABLES rows, FAQ items, service tiles:

| Condition | Finding |
|-----------|---------|
| Design count N, frontend count N | MATCH |
| Design count N, frontend count M < N | **MISSING (count)** — severity per §8 |
| Design count N, frontend count M > N | **EXTRA (count)** — usually Major or Observation |

---

## 8. Severity model

Assign **one severity per finding**. Multiple **Critical** → audit **FAIL** unless Lead waiver (§9).

| Severity | Meaning | Examples |
|----------|---------|----------|
| **Critical** | Missing entity **blocks page purpose**, conversion path, legal/trust requirement, or global shell | Missing **Footer** on landing; missing **primary CTA** section; missing **lead form** when chartered; missing **Header**; entire **FAQ** section absent when in design + blueprint; missing **logo/favicon** in production path |
| **Major** | Missing or partial entity **materially changes** page narrative or UX vs design | Missing **Advantages** section; missing **Services** subsection; accordion present but **FAQ section shell** missing; **modal** not implemented; **card grid** with &lt;50% of designed cards; **navigation item** missing from primary nav |
| **Minor** | Missing secondary/decorative entity; partial state with core path intact | Missing decorative illustration; missing **hover** when default+focus work; one **trust badge** of five; secondary footer link group |
| **Observation** | Extra entity, deferred optional state, backlog note | Extra **promo strip** not in design; **tablet-specific** state deferred with C-14; documentation-only gap |

**Canonical example severities (user scenario):**

| Missing entity | Severity |
|----------------|----------|
| Advantages (full section) | **Major** |
| FAQ (full section) | **Critical** if support/trust charter — else **Major** |
| CTA (conversion block) | **Critical** |

**Forbidden severity rationale:** “Section not important”, “pixel QA passed elsewhere”, “starter had no FAQ” — reclassify as **Major** or **Critical**, not dismissed.

---

## 9. PASS and FAIL criteria

### 9.1 Audit verdicts

| Verdict | Criteria | Production PASS |
|---------|----------|-----------------|
| **PASS** | All IN_SCOPE design entities **MATCH**; no open **Critical** or **Major**; PARTIAL only if dispositioned as Minor/Observation | **Allowed** to proceed to Frontend Design QA Matrix |
| **PASS WITH NOTES** | No open **Critical**; **Major** findings explicitly **waived** or scheduled with Lead ack; Minor/Observation listed | **Allowed** with documented notes |
| **FAIL** | Any open **Critical**; or any **Major** without waiver; or scope UNKNOWN violating EC-05; or registry not frozen | **Blocked** — fix registry gaps before fidelity QA |

### 9.2 Relationship to Production PASS

**Design Completeness Audit FAIL** → **Production PASS blocked** regardless of Frontend Design QA Matrix or Pixel Fidelity partial PASS on implemented subset.

**Design Completeness PASS** does **not** imply Production PASS — fidelity, build, mapping, calibration peers still required.

---

## 10. Reporting requirements

### 10.1 Mandatory REPORT block

```text
DESIGN COMPLETENESS AUDIT — PASS | PASS WITH NOTES | FAIL
SCOPE — page/slice: … · viewport(s): … · standards version: …
DESIGN ENTITY REGISTRY — version/id: … · rows: (n)
FRONTEND ENTITY REGISTRY — extracted: … · rows: (n)
COMPARISON — MATCH: (n) · MISSING: (n) · PARTIAL: (n) · EXTRA: (n) · MISPLACED: (n)
SEVERITY — Critical: (n) · Major: (n) · Minor: (n) · Observation: (n)
CATEGORY ROLLUP — DE-PAGES: … · DE-SECTIONS: … · … · DE-INTERACTIVE: …
FINDINGS — (entity_id · category · severity · one-line evidence)
DISPOSITION — fix | waiver (Lead) | defer (C-14)
```

### 10.2 Finding line format

```text
FINDING — home.section.faq · DE-SECTIONS · Critical · design frame p.4 present; no src/partials/sections/*faq*; dist missing #faq
```

### 10.3 Peer REPORT cross-links

When proceeding to fidelity QA, REPORT must cite:

```text
DESIGN COMPLETENESS — PASS | PASS WITH NOTES (required before matrix)
FRONTEND DESIGN QA MATRIX — …
PIXEL FIDELITY AUDIT — …
```

**Forbidden:** Claiming Production PASS with only matrix verdict and **no** completeness line.

---

## 11. Completeness lifecycle

```text
Design source + blueprint
        ↓
Design Entity Registry (draft)     ← seed from mapping L-01, L-05, handoff
        ↓
DESIGN → FRONTEND MAPPING QA       ← mapping layer + registry draft coherence
        ↓
Production Standards Approval      ← freeze scope / waivers
        ↓
Shell → Visual Foundation          ← subset: shell + demo entities
        ↓
Design Calibration · Foundation QA ← peer fidelity gates (not full page inventory)
        ↓
Page / block production
        ↓
Frontend Entity Registry (extract) ← from src/ + dist/
        ↓
DESIGN COMPLETENESS AUDIT          ← THIS GATE (page/slice level)
        ↓
Frontend Design QA Matrix (full)
        ↓
Pixel Fidelity Audit (peer)
        ↓
Production PASS
```

### 11.1 Scope variants

| Audit scope | When | Design registry scope |
|-------------|------|------------------------|
| **Foundation slice** | After Visual Foundation | Shell + demo categories per [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) — **not** full DE-PAGES site inventory |
| **Page slice** | Home or inner page production complete | Full page DE-SECTIONS chain + page-level entities |
| **Site slice** | Multi-page milestone | DE-PAGES + per-page registries |
| **Block swap** | Section replacement | Diff only affected entity IDs |

---

## 12. Factory pipeline placement (canonical)

### 12.1 Updated chain (page production path)

```text
Design source(s)
        ↓
Design Entity Registry (draft)
        ↓
Production Standards Draft
        ↓
DESIGN → FRONTEND MAPPING QA
        ↓
Production Standards Approval
        ↓
Shell → Visual Foundation → Design Calibration → Foundation QA
        ↓
Page / block production
        ↓
Frontend Entity Registry (extract)
        ↓
DESIGN COMPLETENESS AUDIT                    ← NEW GATE (this doc)
        ↓
Frontend Design QA Matrix (full)
        ↓
Pixel Fidelity Audit (peer detail)
        ↓
Production PASS
```

### 12.2 Placement rationale

| Position | Why |
|----------|-----|
| **After** page/block production | Frontend registry requires built `src/` + `dist/` |
| **Before** Frontend Design QA Matrix (full) | Fidelity QA on missing sections produces **false confidence** |
| **After** Foundation QA | Foundation path uses Visual Foundation contract; page completeness is **downstream** |
| **Parallel to** neither WF-GRID nor WF-LAYOUT | Discipline gates judge **structure of present markup** — not **entity coverage** |

### 12.3 Peer gate ordering (single page sign-off)

| Order | Gate | Question answered |
|-------|------|-------------------|
| 1 | Build | Does it compile? |
| 2 | **Design Completeness Audit** | Are all entities present? |
| 3 | WF-GRID / WF-LAYOUT discipline | Is present markup lawful? |
| 4 | Frontend Design QA Matrix | Is present markup faithful? |
| 5 | Production PASS | Lead closure |

---

## 13. Agent / operator stop rules

| Condition | Action |
|-----------|--------|
| Claim Production PASS without completeness verdict | **STOP** — complete §10 REPORT |
| Pixel Fidelity PASS cited as substitute for missing section | **STOP** — run completeness audit |
| Design registry not frozen / no version | **STOP** — freeze or document delta |
| Missing entity marked “N/A” without C-13 waiver | **STOP** — HITL |
| Implement Home before Foundation QA when shell-first applies | **STOP** — [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) |

---

## 14. Integration notes (documentation-only)

This v1 pack is **standalone**. Recommended **future** integrations (not applied in v1):

| Target doc | Recommended integration |
|------------|-------------------------|
| [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) | Add §7 chain row; require completeness PASS before §6 final PASS |
| [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) | §0 scope note — PF-* applies to **matched** entities only |
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | Cross-ref Design Entity Registry seed from L-01/L-05 |
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | C-11 zone list ↔ DE-SECTIONS |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Extended chain diagram |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Wave entry for Completeness Pack |
| [operational-qa-entry-v1.md](operational-qa-entry-v1.md) | Route: completeness before compact pass at page sign-off |
| [registries.md](registries.md) | Optional §7 Design Entity Registry module |

---

## 15. Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — Frontend Design Completeness Governance: Design Entity Registry + Frontend Entity Registry; comparison model; severity; audit verdicts; pipeline placement; reporting. |
