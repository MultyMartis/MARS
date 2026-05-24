# MARS Website Factory — Prompt Structure Standard v0

**Status:** **documentation only** — normalized **prompt sections** for factory operations. **Not** a prompt engine, **not** a runtime template loader, **not** a guarantee of agent behavior.

**Version:** v0.

**Related:** [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [`../../workflows/task-contract-v0.md`](../../workflows/task-contract-v0.md).

**RU commercial landings:** Frontend QA prompts must route to [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md).

---

## 1. Purpose

This standard defines the **canonical sections** every Website Factory prompt should contain (in prose, in Cursor input, or in a future Task payload). It exists so that:

- intent is **explicit** and **comparable** across stages;
- agents and humans can **refuse** ambiguous prompts honestly;
- QA can **cite** the original instruction when filing findings;
- handoffs preserve **artifact identity** across stage boundaries.

The standard is **deliberately prose-shaped** — there is **no** mandated JSON or YAML envelope in v0.

---

## 2. Canonical sections

A factory prompt is composed from the following **named sections**. Order is recommended for readability; presence is what matters.

### 2.1 `context`

- Where the prompt sits in [website-factory-workflow-v0.md](website-factory-workflow-v0.md) (`stage_id`).
- Project, page/template/section identifiers.
- Reference to upstream **artifact_id** values (blueprint, design handoff, frontend handoff, etc.).
- Why this prompt is being issued **now**.

### 2.2 `objective`

- One paragraph stating **what counts as “done”**.
- Must be **verifiable** by reading the produced artifact and report.
- Forbidden: vague verbs like “improve”, “optimize”, “polish” **without** a measurable target.

### 2.3 `scope`

- **In scope:** pages / sections / files / domains explicitly named.
- **Out of scope:** what must **not** be touched (paths, artifacts, neighboring stages).
- **Boundary anchors:** filesystem paths (e.g. `projects/mars-website-factory/...`), `block_id`, `site_type_id`, `blueprint_id`.

### 2.4 `constraints`

- Hard rules the prompt **must** respect:
  - Locale (per `AGENTS.md`).
  - SAFE UNKNOWN discipline ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)).
  - Forbidden file zones (e.g. `mars-runtime/*` for documentation tasks).
  - Source-first rules ([frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md)).
  - No commits / no pushes unless explicitly requested.

### 2.5 `allowed assumptions`

- Statements the prompt **may** treat as given, with reference to upstream artifacts.
- Each assumption **must** be derivable from a named source.

### 2.6 `forbidden assumptions`

- Statements the prompt **must not** silently introduce, e.g.:
  - “Runtime exists.”
  - “Validator is automated.”
  - “n8n is bound.”
  - “Figma export pipeline is live.”
  - “CI is green.”
- Each forbidden assumption is paired with the **honest alternative**: emit **SAFE UNKNOWN** or escalate.

### 2.7 `artifacts in`

- Named upstream artifacts ([artifact-types-v0.md](artifact-types-v0.md)) the prompt may consume.
- Stable references (artifact_id, path).
- Mutability state (mutable / frozen) per [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md).

### 2.8 `artifacts out`

- Named artifacts the prompt **must** produce.
- Expected paths or document classes.
- Required fields per the relevant contract (blueprint, design handoff, frontend handoff, QA payload).

### 2.9 `QA expectations`

- Which **QA lanes** the artifact will face downstream ([qa-validation-model.md](qa-validation-model.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md)).
- Acceptance criteria, severity tolerance.
- Whether **Validator** is in scope (planned/legacy-bridge — see [agent-map.md](agent-map.md)).

### 2.10 `escalation rules`

- When to **stop and ask**:
  - missing approver,
  - contradiction with upstream artifact,
  - registry mismatch,
  - frontend requirement outside the static model.
- Signal vocabulary: **UNKNOWN**, **SAFE UNKNOWN**, **NEED HUMAN APPROVAL**, **STRUCTURE CHANGE**, **SECURITY RISK** ([`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md)).

### 2.11 `SAFE UNKNOWN rules`

- Where the prompt **expects** unknowns.
- How they must be **flagged** in the report ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)).
- The honest alternative to fabrication.

### 2.12 `reporting requirements`

- The expected **REPORT** format ([reporting-standard-v0.md](reporting-standard-v0.md)).
- Required headings, e.g. `# REPORT — <task name>`.
- Mandatory fields: created files, updated files, git status, runtime exclusions, SAFE UNKNOWN, risks.

---

## 3. Prompt variants

### 3.1 Minimal prompt

For small, single-file, documentation-only tweaks (typo, link fix, paragraph clarification).

Required sections:

- `context` (project + file)
- `objective` (one line)
- `scope` (one file or one section)
- `constraints` (no runtime edits, no commits unless asked)
- `reporting requirements` (REPORT block)

Optional but recommended: `forbidden assumptions`, `SAFE UNKNOWN rules`.

### 3.2 Production prompt

For stage-bound deliverables (creating a blueprint, drafting a design handoff, producing a section payload, drafting a contract file).

Required sections: **all of §2** except QA-only and HITL-only sections may be condensed.

### 3.3 HITL prompt

Used at approval gates (G1–G7 per [workflow-map.md](workflow-map.md)).

Required sections:

- `context` (which gate, which artifact_id, what approver role).
- `objective` (approve / reject / request revision / waive).
- `evidence in` (artifact and prior QA reports).
- `decision options` (explicit, enumerated).
- `escalation rules` (when HITL itself must escalate further).
- `reporting requirements` (a signed approval artifact per [artifact-types-v0.md](artifact-types-v0.md) §Approval artifact).

A HITL prompt **must not** request the agent to “approve on behalf of” a human.

### 3.4 QA prompt

See [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md). Distinct from production prompts.

Required sections:

- `context` (lane: Design / SEO / Conversion / Frontend / Validator).
- `subject artifact` (artifact_id under test).
- `checklist reference` (e.g. [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md)).
- `evidence expectations` (what counts as evidence per [qa-result-payloads-v0.md](qa-result-payloads-v0.md)).
- `severity scale` (info / warn / blocker — project-normalized).
- `escalation rules` (waivers require named approver).
- `reporting requirements` (QA result payload prose).

### 3.5 Frontend execution prompt

See [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md). Adds:

- `target_stack` echo from [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md);
- `section_map` boundaries (`block_id` → partial path);
- `SCSS_mapping` discipline (no monolithic dumps);
- `data_attribute_hooks` enforcement;
- `forbidden_patterns` (no `dist/` edits, no undeclared globals);
- `QA_requirements` echo;
- `SAFE_UNKNOWN_notes` echo.

---

## 4. Examples

The examples below are **illustrative prose templates**, not runnable payloads. They may be paraphrased; the **section discipline** is the point.

### 4.1 Minimal documentation prompt

```text
context:
  project: mars-website-factory
  file: projects/mars-website-factory/README.md

objective:
  Fix the dead link to design-handoff-contract-v0.md in the pack index row.

scope:
  in:  projects/mars-website-factory/README.md (one row)
  out: every other file

constraints:
  - no runtime edits
  - no commits unless explicitly requested
  - locale: leave existing prose untouched

reporting requirements:
  REPORT block with created / updated files, git status, SAFE UNKNOWN notes.
```

### 4.2 Production prompt — blueprint draft

```text
context:
  stage:    WF_V0_S05_BLUEPRINT
  project:  example-roof-inspection
  inputs:   IA pack (approved), site_type_id = service_landing

objective:
  Produce one Page Blueprint document for /roof-inspection-moscow
  per page-blueprint-contract-v0.md required fields.

scope:
  in:  one page slug, blueprint artifact only
  out: design tokens, frontend code, copywriting beyond CTA semantics

constraints:
  - reference block_ids from block-registry-v0.md only
  - SAFE UNKNOWN for any field with no evidence in IA
  - no Figma claim, no automation claim

allowed assumptions:
  - approved IA defines URL and template
  - site_type defaults from site-type-registry-v0.md

forbidden assumptions:
  - that design exists
  - that frontend handoff exists
  - that Validator runs automatically

artifacts in:
  - IA pack (approved)
  - site-type-registry-v0 row for service_landing
  - block-registry-v0 entries

artifacts out:
  - blueprint document (blueprint_id: bp_roof_inspection_moscow_v1)

QA expectations:
  - page-blueprint-qa-checklist-v0.md categories
  - blueprint QA agent (planned) review at G3

escalation rules:
  - registry mismatch -> STRUCTURE CHANGE, no silent block drop
  - missing CTA target -> NEED HUMAN APPROVAL

SAFE UNKNOWN rules:
  - mark SEO copy variants as SAFE UNKNOWN until SEO QA reviews

reporting requirements:
  REPORT with created files, blueprint_id, SAFE UNKNOWN list,
  git status, no commit unless requested.
```

### 4.3 HITL prompt — design freeze (G5)

```text
context:
  gate:    G5
  artifact:design_id = dh_roof_inspection_moscow_v1 + design output set
  approver:design lead

objective:
  Decide: approve / reject / request revision / park.

evidence in:
  - design outputs (wireframes + hi-fi)
  - design QA report (S09)
  - design handoff pack (S07)

decision options:
  - approve  -> freeze baseline for frontend
  - reject   -> return to S08 with reasons
  - revision -> bounded CR list, re-gate at S09
  - park     -> NEED HUMAN APPROVAL escalation upward

escalation rules:
  - SECURITY RISK in assets -> stop line, do not approve
  - registry mismatch -> STRUCTURE CHANGE upward

reporting requirements:
  Approval artifact (immutable) per artifact-types-v0.md §Approval artifact.
  No autonomous approval. No agent-side signoff.
```

### 4.4 QA prompt — frontend lane

```text
context:
  lane:    Frontend QA
  stage:   WF_V0_S12_FRONTEND_QA
  subject: frontend_handoff_id = fh_roof_inspection_moscow_v1
           + built static pages from S11

objective:
  Produce a Frontend QA report against:
    - frontend-handoff-contract-v0.md QA_requirements
    - frontend-production-model.md heuristics

checklist reference:
  - qa-validation-model.md (Frontend lane)
  - qa-result-payloads-v0.md fields

evidence expectations:
  - URL / file path
  - viewport / breakpoint
  - reproduction step
  - blocker vs warn vs info

severity scale:
  info | warn | blocker (project-normalized)

escalation rules:
  - blocker without fix -> NEED HUMAN APPROVAL for waiver
  - missing CI evidence -> SAFE UNKNOWN, do not assert green build

reporting requirements:
  QA report with categories, evidence, severity, waiver flags,
  HITL required flag, SAFE UNKNOWN list, no fake pass.
  RU commercial: RU TYPOGRAPHY / NO WORD-SPLITTING line per ru-landing-qa-preset-v1.md.
```

### 4.5 Frontend execution prompt — section partial

```text
context:
  stage:   WF_V0_S11_FRONTEND_PRODUCTION
  subject: section block_id = faq_accordion
           on page_slug = roof-inspection-moscow

objective:
  Implement src/partials/sections/faq-accordion.html and
  src/scss/sections/_faq-accordion.scss per
  frontend-handoff-contract-v0.md fh_roof_inspection_moscow_v1.

scope:
  in:  src/partials/sections/faq-accordion.html
       src/scss/sections/_faq-accordion.scss
       data-component="faq-accordion" JS module (scoped)
  out: dist/* (never hand-edit), unrelated sections, global resets

constraints:
  - source-first; never patch dist/
  - modular SCSS; no monolithic page dump
  - no new window.* without explicit note in SAFE_UNKNOWN_notes
  - data-attribute hooks only; no id-soup

artifacts in:
  - frontend handoff fh_roof_inspection_moscow_v1
  - design tokens from frozen design baseline

artifacts out:
  - HTML partial, SCSS partial, scoped JS hook

QA expectations:
  - Frontend QA lane: build, semantics, a11y, responsive (375 / 768 / 1280 — supplementary generic only)
  - RU commercial: ru-landing-qa-preset-v1.md mandatory

escalation rules:
  - unsupported framework requirement -> STRUCTURE CHANGE
  - missing CI -> SAFE UNKNOWN, do not claim green build

reporting requirements:
  REPORT with created / updated source files,
  SAFE UNKNOWN notes for unverifiable items,
  no commit unless requested.
```

---

## 5. Anti-patterns (forbidden prompt shapes)

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| “Generate the whole website end-to-end.” | Collapses workflow stages and HITL gates. | Decompose by stage; one prompt per stage with explicit artifacts. |
| “Approve the design automatically.” | Bypasses HITL ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)). | Issue a HITL prompt with explicit decision options; never autosign. |
| “Make it SEO-optimal.” | Unverifiable objective. | Reference [seo-intent-model-v0.md](seo-intent-model-v0.md); name measurable expectations and QA lane. |
| “Assume the runtime executes this.” | Forbidden assumption ([safe-unknown-boundary.md](safe-unknown-boundary.md)). | Document the prompt as human-supervised; SAFE UNKNOWN on runtime. |
| “Fill missing data with best guess.” | Fabrication. | Emit SAFE UNKNOWN with explicit assumption boundary. |
| “Add a Validator pass.” | Validator integration depth is TBD. | Mark Validator as planned/legacy-bridge; cite [agent-map.md](agent-map.md). |
| “Generate fields without naming the contract.” | Breaks artifact discipline. | Cite contract document and required fields per [artifact-types-v0.md](artifact-types-v0.md). |

---

## 6. Non-claims

- This standard does **not** ship runtime parsers, validators, or generators for prompts.
- LLM behavior is **not** guaranteed; this layer reduces ambiguity but does not eliminate hallucination — that is what **QA**, **HITL**, and **SAFE UNKNOWN** are for.
- No fields here are **wire formats**; they are **prose discipline**.

---

## 7. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial prompt-structure standard (documentation only). |
