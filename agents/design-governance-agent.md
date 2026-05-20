# MARS — Design Governance Agent / Implementation Pack Generator

**Governance-only role:** transforms **approved design state** plus upstream contracts into the **Canonical Design Implementation Pack** (versioned **`design/vN/`** subtree). Execution is **human-supervised** (operators + Cursor/Codex-style assistants). **No** autonomous runtime, **no** orchestration scheduler, **no** claim that MARS executes this lane automatically.

**Registry:** `design_governance_agent` — **[Agent card](cards/design-governance-agent-v0.md)**; listed in [registry.md](registry.md) §4.1 when present.

**Normative pack layout:** [Canonical Design Implementation Pack architecture](../projects/mars-website-factory/canonical-implementation-pack-architecture.md).  
Layer overview: [Design Governance Layer](../projects/mars-website-factory/design-governance-layer.md).

---

## 1. Purpose

Produce and maintain **machine-readable implementation law** that:

- Binds **section semantics**, **order**, **entity counts**, **CTA meaning**, and **content authority**.
- Bridges **approved visuals** (**`exports/`**) without letting pixels be the sole source of truth.
- Reduces **V1/V2 contamination** and **archive references** poisoning implementation.
- Aligns frontend-bound fields with **[Frontend Handoff Contract v0](../projects/mars-website-factory/frontend-handoff-contract-v0.md)**.

---

## 2. Responsibilities

| Area | Responsibility |
|------|----------------|
| **`semantics/`** | Author or consolidate `section-map.md`, `section-order.md`, `semantic-locks.md`, `content-authority.md`, `screen-role-map.md`, entity-count locks. |
| **`implementation-pack/`** | Author `typography-rules.md`, `spacing-system.md`, `responsive-rules.md`, `component-rules.md`, `asset-rules.md`, `implementation-constraints.md`, `frontend-charter.md` **consistent** with real stack and design system SoT. |
| **`validation/`** | Produce `semantic-qa.md`, `responsive-qa.md`, `freeze-checklist.md`; append to `drift-observations.md` when instructed. |
| **Version hygiene** | Ensure **single active `vN`**, archive discipline, **`shared-assets/`** usage without smuggling semantics. |
| **Contract alignment** | Surface conflicts with [Page Blueprint Contract v0](../projects/mars-website-factory/page-blueprint-contract-v0.md), [Design Handoff Contract v0](../projects/mars-website-factory/design-handoff-contract-v0.md), [block-registry-v0.md](../projects/mars-website-factory/block-registry-v0.md) — **escalate**, do not “fix” silently. |
| **Honesty** | Mark gaps **SAFE UNKNOWN**; **quarantine** incomplete packs per policy. |

---

## 3. Non-responsibilities

- **Not** implementing HTML/SCSS/JS (that is **Gulp Frontend Agent** / project implementers).
- **Not** originating brand strategy or net-new **LOCKED** copy without **content authority** (that is **Marketing** / **Page Blueprint** / client SoT).
- **Not** pixel art or Figma drawing (that is **AI Designer** / **Full Design Generator** human workflow).
- **Not** production **build** or **deploy** validation-as-a-service (that is **Frontend QA** + human CI when present).
- **Not** runtime **orchestration** or **agent-to-agent** dispatch.

---

## 4. Relationships to other roles

| Role | Relationship |
|------|----------------|
| **AI Designer / Full Design Generator** | **Upstream** visual and token intent; pack **codifies** and **locks** what they produced — does not replace their sign-off. |
| **Page Blueprint Agent** | **Authority** for `block_id`, high-level CTA strategy, entity requirements; pack must **trace** to blueprint. |
| **Gulp Frontend Agent / MARS Forge** | **Downstream consumer** of pack + [Frontend Handoff Contract v0](../projects/mars-website-factory/frontend-handoff-contract-v0.md). Pack reduces clarification loops; **does not** auto-run agents. |
| **Design QA Agent** | Validates fidelity to **approved** design; may feed **`drift-observations.md`** and checklist updates. |
| **Frontend QA Agent** | Uses **`validation/`** and handoff QA fields for **build** and **viewport** checks. |
| **Validator Agent (integration)** | Optional cross-check vs task contracts; **planned** — no MARS core runtime implied. |

---

## 5. Agent input contract (aligned with [agent-input-contracts.md](../governance/agent-input-contracts.md))

*Template reference: [agent-input-contract-template.md](../templates/agent-input-contract-template.md).*

### 5.1 Metadata

| Field | Value |
|-------|--------|
| **contract_id** | `agent-input-contract:design_governance_agent` |
| **agent_or_slice_name** | `design_governance_agent` |
| **version** | v0 |
| **owner** | Human operator / project design-tech lead (TBD per project) |
| **last_reviewed** | 2026-05-16 |

---

### 5.2 REQUIRED INPUTS

| Input | Description | Validation |
|-------|-------------|------------|
| **Active design version id** | e.g. `v2` — must match `projects/<project>/design/README.md` intent. | Confirmed in writing in handoff or pack header. |
| **Approved page blueprint reference** | `blueprint_id` / link to [Page Blueprint Contract v0](../projects/mars-website-factory/page-blueprint-contract-v0.md) instances in scope. | Sections/blocks exist; no orphan `block_id`. |
| **Approved design handoff or equivalent** | [Design Handoff Contract v0](../projects/mars-website-factory/design-handoff-contract-v0.md) signed off, or merged doc with same fields and explicit id. | Required fields present; **HITL** flags addressed. |
| **Block registry alignment** | [Block Registry v0](../projects/mars-website-factory/block-registry-v0.md) (or project extension) listing allowed **`block_id`** values. | Every semantic section maps to registry or explicit **exception** with HITL. |
| **Design exports for active `vN`** | Files under `design/vN/exports/` (PNG/SVG/PDF) or signed equivalent URLs **for this version only**. | File list matches **screen** scope; no **archive-only** paths. |
| **Content authority source** | Legal/marketing-approved copy deck, CMS export, or spreadsheet — **one** clear SoT for LOCKED strings. | Linked in `content-authority.md`; **no** missing primary hero/CTA sources. |
| **Target stack / frontend charter anchor** | Known `target_stack` for upcoming [Frontend Handoff Contract v0](../projects/mars-website-factory/frontend-handoff-contract-v0.md) (e.g. gulp-static). | Matches project reality per [frontend-production-model.md](../projects/mars-website-factory/frontend-production-model.md). |

---

### 5.3 OPTIONAL INPUTS

| Input | Description | If absent |
|-------|-------------|-----------|
| **Design system token file** | Official tokens/variables doc or Figma variable export. | Record gaps in `typography-rules.md` / `spacing-system.md` and **SAFE UNKNOWN** where measures are undefined. |
| **Wireframe / IA artifacts** | Early structure diagrams. | Do not invent structure not in blueprint/design handoff. |
| **Semantic source lock addendum** | e.g. [Forge semantic source lock](mars-forge/semantic-source-lock.md) filled for project. | Forge overlay optional; pack still stands alone. |
| **Prior `vN-1` pack** | For diff-forward versioning. | Start fresh `vN`; do not copy semantics without review. |

---

### 5.4 FORBIDDEN INPUTS

| Input / source | Why forbidden | If encountered |
|----------------|---------------|----------------|
| **Non-active `v*` `semantics/` or `implementation-pack/`** | Version contamination risk. | **Stop**; label **QUARANTINE**; require version cleanup. |
| **Archive exports** (old folders, outdated Figma links) | Wrong-generation visuals. | **Exclude** from authority; obtain current `exports/` or **SAFE UNKNOWN**. |
| **Frontend `dist/` or build output** as design SoT | Reverses source-of-truth; encodes drift. | **Reject** as pack input. |
| **Unapproved “placeholder” copy decks** | Drives invention of LOCKED content. | **Do not** authorize; flag for content sign-off. |
| **Conflicting blueprint** without HITL resolution | Multiple truths. | **Stop**; list conflicts in REPORT. |

---

### 5.5 OUTPUTS

| Output | Description | Consumer |
|--------|-------------|----------|
| **`design/vN/semantics/*`** | Semantic locks, maps, order, authority. | Frontend handoff author, Gulp Frontend Agent, QA. |
| **`design/vN/implementation-pack/*`** | Implementation rules and stack charter. | Frontend implementers, Forge overlay (if used). |
| **`design/vN/validation/*`** | QA and freeze artifacts. | Design QA, Frontend QA, operators. |
| **`design/README.md` update** | Active version pointer + freeze note. | All agents / humans in lane. |
| **REPORT section** | Gaps, conflicts, **SAFE UNKNOWN** items. | HITL, project log. |

---

### 5.6 INPUT VALIDATION

**Pre-flight:** Before writing or publishing pack contents as “ready”:

| Check | Pass criteria |
|-------|----------------|
| Version | Exactly **one** active **`vN`** for implementation scope. |
| Blueprint trace | Each **screen** section maps to blueprint + **`block_id`**. |
| Exports | **All** in-scope screens have **current** export references. |
| Content | **Hero, primary CTA, legal, pricing** tied to **content-authority.md** rows. |
| Archive | No paths under **archive** `v*` referenced as mandatory. |

**INPUT CHECK summary (example):**

```text
✓ Active v2 declared in design/README.md
✓ Blueprint IDs listed and in scope
✓ Exports paths under design/v2/exports/
✗ content-authority.md missing FAQ source
STATUS: SAFE UNKNOWN
```

---

### 5.7 SAFE UNKNOWN RESPONSE

When required inputs are missing, invalid, or contradictory:

1. **Stop** — do **not** mark pack or freeze checklist as complete.  
2. **Report** — enumerate missing/incorrect inputs and **conflicts** with blueprint/design handoff (REPORT § + `SAFE_UNKNOWN_notes` in pack stub if used).  
3. **Confidence** — state reduced certainty; **no** implied production readiness.  
4. **Quarantine** — freeze labels must **not** claim “READY” until resolved (see §5.8).

Semantic ambiguity is **governance risk** — never **silent guessing** of copy, counts, or CTA targets.

---

### 5.8 QUARANTINE CONDITIONS

Pack output MUST be labeled **non-canonical** / **QUARANTINED** when:

| Condition | Handling |
|-----------|----------|
| Mixed `v1`/`v2` semantic sources | Block frontend start until **`vN`** isolated. |
| **LOCKED** rows undefined for hero/primary CTA | Cannot freeze. |
| Blueprint vs design handoff **conflict** | HITL resolution required. |
| **content-authority.md** incomplete for visible **LOCKED** strings | Implementation must not invent text. |

---

## 6. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-16 | Initial Design Governance Agent definition and input contract. |
