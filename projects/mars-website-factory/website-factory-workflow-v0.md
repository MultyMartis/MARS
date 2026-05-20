# MARS Website Factory — Workflow v0 (orchestration model)

**Status:** **documentation only** — **orchestration-first**, **contract-first**, **document-first**.  
**Not claimed:** automated execution, a runnable workflow engine, autonomous agents, or production runtime in this repository.

**Version:** v0.

**Related:** [workflow-map.md](workflow-map.md) (diagrams and HITL summary), [`../../workflows/task-contract-v0.md`](../../workflows/task-contract-v0.md), [`../../workflows/execution-flow.md`](../../workflows/execution-flow.md), [`../../control-plane/contract.md`](../../control-plane/contract.md).

---

## Purpose

### Orchestration role

This document is the **canonical high-level production chain** for the **MARS Website Factory**: it names **stages**, **artifacts**, **registries**, **QA gates**, **human-in-the-loop (HITL)** expectations, and **failure / escalation** behavior **as design** — so future **Control Plane** scheduling, **Task** bundles, and human runbooks stay aligned without implying that code exists today.

### Relation to Control Plane

The **Control Plane** (see `control-plane/contract.md`) is the **intended** authority for **task lifecycle**, policy, and routing when a runtime exists. In **v0**, this workflow **maps** each factory stage to **Task Contract v0** concepts (`required_agents`, `hitl_gates`, `signals`) **as narrative alignment only** — no API, no persisted state format, no scheduler.

### Relation to registries and contracts

| Artifact type | Role in v0 workflow |
|---------------|---------------------|
| **Site Type Registry v0** | [`site-type-registry-v0.md`](site-type-registry-v0.md) — **classification** and defaults for strategy, SEO, blocks, frontend posture, QA emphasis. |
| **Block Registry v0** | [`block-registry-v0.md`](block-registry-v0.md) — **section semantics** and **compatibility** with site types; constrains blueprint blocks. |
| **Page Blueprint Contract v0** | [`page-blueprint-contract-v0.md`](page-blueprint-contract-v0.md) — **normalized page orchestration fields** from strategy through QA hooks. |
| **Design Handoff Contract v0** | [`design-handoff-contract-v0.md`](design-handoff-contract-v0.md) — **blueprint → design production** requirements (no automated Figma claim). |
| **Frontend Handoff Contract v0** | [`frontend-handoff-contract-v0.md`](frontend-handoff-contract-v0.md) — **blueprint/design → static frontend** (Gulp-oriented intent). |
| **Page Blueprint QA Checklist v0** | [`page-blueprint-qa-checklist-v0.md`](page-blueprint-qa-checklist-v0.md) — **blueprint-level** validation categories and escalation. |

Registries and contracts are **SoT for vocabulary and handoff shape**; they do **not** prove tooling or automation.

### Relation to HITL

**HITL** is **mandatory** at defined **gates** (see per-stage **HITL requirements**). The workflow **assumes** a human can **approve**, **reject**, **request revision**, or **park** a run. **NEED HUMAN APPROVAL** (per `governance/system-signals-dictionary.md`) applies where policy or risk requires it.

### SAFE UNKNOWN boundaries

- Anything **not** specified in linked registry/contract docs is **SAFE UNKNOWN** until authored — do **not** infer stack, CMS, hosting, or CI.
- **Agent** participation is **planned** per [agent-map.md](agent-map.md) unless **Agent Registry** evidence says otherwise — no claim that specialist agents are **implemented** for Website Factory.
- **Validator Agent** integration depth vs specialist QA is **TBD** (see agent-map) — treat split as **SAFE UNKNOWN** unless a later contract narrows it.

### No runtime / autonomy claims

This file **does not** describe daemons, queues, n8n graphs, or Cursor automation. **Phase 1** execution remains **human-supervised** per `governance/execution-model.md`. Mapping to **prompt → task → plan → route → execute → validate → report → log** is **conceptual** (see `workflows/execution-flow.md`).

---

## Core pipeline (normalized stages)

Each row is a **stage** in order. **Primary agents** reference [agent-map.md](agent-map.md) (**planned** unless registry proves otherwise). **Registries used** cite v0 docs above. **Signals** use v0-allowed names from Task Contract v0 / system signals dictionary.

---

### Stage 1 — Intake / Discovery

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S01_INTAKE` |
| **purpose** | Capture business goals, audience, constraints, brand/compliance sensitivity, and delivery expectations; establish **scope_in** / **scope_out** for downstream Tasks. |
| **primary agents** | Project Intake Agent (planned); human PM/lead owns final scope narrative. |
| **input artifacts** | Client briefs, stakeholder notes, existing analytics (if any), legal/compliance flags, prior site exports (**optional**). |
| **output artifacts** | Intake summary; **Task**-shaped scope draft (goal, constraints, risk_level hypothesis); open questions list. |
| **registries used** | None mandatory; may **pre-reference** Site Type Registry for vocabulary only. |
| **QA gates** | Completeness check: goals, audience, constraints, and approval chain identified. |
| **HITL requirements** | **G1** (per workflow-map): PM/lead confirms intake accuracy and **scope_in** / **scope_out**. |
| **SAFE UNKNOWN escalation** | If business model, markets, or compliance posture are **missing** → emit **UNKNOWN** or **SAFE UNKNOWN** with bounded assumptions **only** if policy allows; otherwise **park** until resolved. |
| **downstream dependencies** | Site Type Classification requires stable intake **goal** and **constraints**. |

---

### Stage 2 — Site Type Classification

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S02_SITE_TYPE` |
| **purpose** | Assign or refine **site_type_id** and defaults that drive strategy, block palette, SEO posture, and frontend QA emphasis. |
| **primary agents** | Site Type Classifier Agent (planned); human approver for edge cases. |
| **input artifacts** | Intake summary; optional competitive set; product/service taxonomy. |
| **output artifacts** | **site_type_id** selection + rationale; registry row references; deltas vs defaults (**if** custom). |
| **registries used** | **Site Type Registry v0** (authoritative for classification layer). |
| **QA gates** | Classification **consistent** with intake; no contradictory **site_type_id** vs stated business model. |
| **HITL requirements** | **G1** extension: lead confirms **site_type_id** when **ambiguous** or **multi-site** program. |
| **SAFE UNKNOWN escalation** | If no registry row fits → **SAFE UNKNOWN** / **STRUCTURE CHANGE**: propose new site type row **or** park for registry update (**not** silent best-guess). |
| **downstream dependencies** | Strategic Layer and IA consume **site_type_id** and defaults. |

---

### Stage 3 — Strategic Layer

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S03_STRATEGY` |
| **purpose** | Positioning, messaging, funnel narrative; align commercial and SEO hypotheses with **site type**. |
| **primary agents** | Marketing Strategy Agent; SEO Strategy Agent (both planned). |
| **input artifacts** | Intake; **site_type_id**; brand guidelines (**if** any). |
| **output artifacts** | Strategy memo; SEO hypothesis doc; CTA / conversion narrative; **risks** list. |
| **registries used** | Site Type Registry v0 (constraints); Block Registry v0 (indirect — which story types blocks must support). |
| **QA gates** | Internal consistency: messaging vs audience vs **site_type**; no orphan CTAs without destination intent. |
| **HITL requirements** | **G2**: marketing lead approves strategy + SEO hypotheses (brand/compliance sensitivity). |
| **SAFE UNKNOWN escalation** | Conflicting SEO vs commercial goals → **NEED HUMAN APPROVAL** or **STRUCTURE CHANGE**; do not proceed to IA until resolved. |
| **downstream dependencies** | IA and blueprints need approved **strategy** and **SEO** intent. |

---

### Stage 4 — Information Architecture

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S04_IA` |
| **purpose** | Sitemap, templates, URL patterns, content requirements, navigation model. |
| **primary agents** | Information Architecture Agent (planned). |
| **input artifacts** | Approved strategy; **site_type_id**; optional legacy URL map. |
| **output artifacts** | Sitemap; template list; URL/content requirements; navigation spec. |
| **registries used** | Site Type Registry v0; Block Registry v0 (template ↔ block expectations). |
| **QA gates** | Reachability: key journeys covered; depth vs scope realistic; **no** dead-end critical paths. |
| **HITL requirements** | **G3** (partial): PM + tech lead on scope/size; major IA shifts may re-trigger **G2**. |
| **SAFE UNKNOWN escalation** | If CTA flow is **impossible** given IA → return to Strategy or IA with **STRUCTURE CHANGE**; **unknown stack** for CMS/hosting → **SAFE UNKNOWN** (document assumptions explicitly). |
| **downstream dependencies** | Page Blueprint Generation needs **stable** sitemap and templates. |

---

### Stage 5 — Page Blueprint Generation

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S05_BLUEPRINT` |
| **purpose** | Per-page **block** ordering, linking, CTA logic, SEO fields per **Page Blueprint Contract v0**. |
| **primary agents** | Page Blueprint Agent; UX Structure Agent (planned). |
| **input artifacts** | IA pack; strategy/SEO; **site_type_id**; design/frontend constraints from registry defaults. |
| **output artifacts** | Blueprint set (one per URL/template instance as defined by IA); cross-page link graph notes. |
| **registries used** | **Block Registry v0**; **Site Type Registry v0**; **Page Blueprint Contract v0**. |
| **QA gates** | Contract field completeness; block IDs **valid** per registry; CTA targets resolvable in IA. |
| **HITL requirements** | **G3**: PM + tech lead approve blueprint batch before **Blueprint QA** sign-off for handoff. |
| **SAFE UNKNOWN escalation** | **Registry mismatch** (block not allowed for **site_type_id**) → fix blueprint **or** amend registry under governance — **no** silent drop of blocks. |
| **downstream dependencies** | Blueprint QA, then Design Handoff, consume this output. |

---

### Stage 6 — Blueprint QA

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S06_BLUEPRINT_QA` |
| **purpose** | Validate blueprints against **Page Blueprint QA Checklist v0** and contract rules before visual or code work. |
| **primary agents** | SEO QA Agent; Conversion QA Agent; Validator Agent (**planned** / legacy-bridge per registry — depth **TBD**). |
| **input artifacts** | Blueprint set; IA; strategy/SEO; checklists. |
| **output artifacts** | QA report; defect list; **pass** / **fail** / **conditional** recommendation. |
| **registries used** | Page Blueprint Contract v0; Page Blueprint QA Checklist v0; Site Type Registry v0. |
| **QA gates** | Checklist categories satisfied or explicitly waived with HITL. |
| **HITL requirements** | Failed or **high-risk** → **NEED HUMAN APPROVAL** to waive or to send back to **S05**. |
| **SAFE UNKNOWN escalation** | Ambiguous checklist item → **SAFE UNKNOWN** with written assumption **or** checklist amendment request. |
| **downstream dependencies** | Design Handoff requires **pass** or approved waiver. |

---

### Stage 7 — Design Handoff

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S07_DESIGN_HANDOFF` |
| **purpose** | Package blueprint-approved pages into **Design Handoff Contract v0** inputs (tokens, sections, QA hooks). |
| **primary agents** | AI Designer Agent (planned) for handoff pack assembly; human design lead owns contract completeness. |
| **input artifacts** | Approved blueprints; brand/tokens (**if** any); **Design Handoff** template fields. |
| **output artifacts** | Design handoff pack per page/template; open design questions. |
| **registries used** | Page Blueprint Contract v0; Design Handoff Contract v0; Block Registry v0 (semantic → visual mapping notes). |
| **QA gates** | Handoff contract completeness vs blueprint; no **unsupported** visual requirements without flag. |
| **HITL requirements** | Design lead confirms handoff pack before **Design Production**. |
| **SAFE UNKNOWN escalation** | Tooling/format for high-fidelity export **TBD** → **SAFE UNKNOWN**; document export intent only. |
| **downstream dependencies** | Design Production consumes handoff pack. |

---

### Stage 8 — Design Production

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S08_DESIGN_PRODUCTION` |
| **purpose** | Produce visual design artifacts per handoff (tool-agnostic in v0; **not** claiming Figma automation). |
| **primary agents** | Wireframe Generator Agent; Full Design Generator Agent (planned). |
| **input artifacts** | Design handoff pack; brand system; reference sites. |
| **output artifacts** | Wireframes; high-fidelity designs or spec exports (**format explicit per project**). |
| **registries used** | Design Handoff Contract v0; Site Type Registry v0 (density, patterns). |
| **QA gates** | Internal design review checklist (see **Design QA**). |
| **HITL requirements** | **G4** / **G5** per workflow-map (UX/client; design lead/client). |
| **SAFE UNKNOWN escalation** | **Design inconsistency** across templates → **STRUCTURE CHANGE** or revision loop; **SECURITY RISK** if assets/compliance breach → stop line until cleared. |
| **downstream dependencies** | Design QA then Frontend Handoff. |

---

### Stage 9 — Design QA

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S09_DESIGN_QA` |
| **purpose** | Fidelity and consistency vs **approved** blueprint + handoff; brand and a11y intent checks. |
| **primary agents** | Design QA Agent (planned). |
| **input artifacts** | Design outputs; Design Handoff Contract v0; blueprints. |
| **output artifacts** | Design QA report; change requests. |
| **registries used** | Design Handoff Contract v0; Page Blueprint Contract v0. |
| **QA gates** | Pass or **bounded** CR list before frontend. |
| **HITL requirements** | **G5** closure: design lead / client approves **frozen** design for frontend. |
| **SAFE UNKNOWN escalation** | Ambiguous “approved” vs “iterating” → **NEED HUMAN APPROVAL** to freeze scope. |
| **downstream dependencies** | Frontend Handoff requires **frozen** design baseline. |

---

### Stage 10 — Frontend Handoff

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S10_FRONTEND_HANDOFF` |
| **purpose** | Translate frozen design + blueprint into **Frontend Handoff Contract v0** (Gulp-oriented static production intent). |
| **primary agents** | Gulp Frontend Agent (legacy-bridge — **documentation** alignment; human implements in Phase 1). |
| **input artifacts** | Frozen design; blueprints; **Frontend Handoff** fields; build conventions doc (**if** any). |
| **output artifacts** | Frontend handoff spec; asset list; breakpoint/responsive notes. |
| **registries used** | Frontend Handoff Contract v0; Block Registry v0; Site Type Registry v0. |
| **QA gates** | Handoff completeness; **no** unsupported component without **UNKNOWN** flag. |
| **HITL requirements** | Tech lead approves handoff before **Frontend Production**. |
| **SAFE UNKNOWN escalation** | **Unsupported frontend requirement** (framework, CMS, non-static) → **UNKNOWN** / **STRUCTURE CHANGE** relative to factory static model — explicit human decision. |
| **downstream dependencies** | Frontend Production uses handoff spec. |

---

### Stage 11 — Frontend Production

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S11_FRONTEND_PRODUCTION` |
| **purpose** | Implement HTML/SCSS/JS (or agreed static stack) per handoff; **human-executed** in Phase 1 unless future runtime exists. |
| **primary agents** | Gulp Frontend Agent (legacy-bridge naming); engineers. |
| **input artifacts** | Frontend handoff spec; design exports; content copy deck. |
| **output artifacts** | Source files; build instructions; PR or change bundle. |
| **registries used** | Frontend Handoff Contract v0; Block Registry v0. |
| **QA gates** | Build succeeds locally/CI (**when** CI exists — **SAFE UNKNOWN** if not). |
| **HITL requirements** | **G6**: tech + design sign-off on PR/file set alignment to frozen design. |
| **SAFE UNKNOWN escalation** | **Unknown stack** or missing CI → document **SAFE UNKNOWN**; do not claim green build. |
| **downstream dependencies** | Frontend QA and Final Validation. |

---

### Stage 12 — Frontend QA

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S12_FRONTEND_QA` |
| **purpose** | Markup, responsive, a11y heuristics, performance smoke per `qa-validation-model.md` lanes (specialist depth). |
| **primary agents** | Frontend QA Agent (planned); Validator Agent (planned / legacy-bridge). |
| **input artifacts** | Built static pages; handoff spec; QA checklists. |
| **output artifacts** | Frontend QA report; defect backlog. |
| **registries used** | Site Type Registry v0 (QA emphasis); Page Blueprint Contract v0 (metadata, headings). |
| **QA gates** | Severity-tagged issues; **blocker** list empty or waived with HITL. |
| **HITL requirements** | Waivers for **blockers** → **NEED HUMAN APPROVAL** + **SECURITY RISK** if applicable. |
| **SAFE UNKNOWN escalation** | **QA rejection** cycles to **S11** until pass or approved exception path. |
| **downstream dependencies** | Final Validation aggregates blueprint + design + frontend checks. |

---

### Stage 13 — Final Validation

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S13_FINAL_VALIDATION` |
| **purpose** | Cross-lane validation: SEO, conversion, security/compliance hooks, **Task** acceptance criteria vs delivery pack. |
| **primary agents** | SEO QA Agent; Conversion QA Agent; Validator Agent (combination **TBD**). |
| **input artifacts** | All prior approved artifacts; deployment checklist (**if** any). |
| **output artifacts** | Final validation report; **go** / **no-go** recommendation. |
| **registries used** | Full stack of v0 contracts + checklists; Site Type Registry v0. |
| **QA gates** | End-to-end consistency; links; metadata; legal pages present when required. |
| **HITL requirements** | **G7** prep: ops/client inputs on **go** / **no-go**. |
| **SAFE UNKNOWN escalation** | Cross-cutting **registry mismatch** at late stage → **park**; may require **S05**–**S12** targeted fixes — document **STRUCTURE CHANGE** if scope shifts. |
| **downstream dependencies** | Human Approval (delivery authorization). |

---

### Stage 14 — Human Approval

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S14_HITL_APPROVAL` |
| **purpose** | Formal **NEED HUMAN APPROVAL** resolution: authorize release, exports, or deploy per `security/approval-gates.md` alignment. |
| **primary agents** | None — human governance. |
| **input artifacts** | Final validation report; risk summary; rollback notes. |
| **output artifacts** | Signed approval record (format **TBD**); release tag intent. |
| **registries used** | N/A (policy-driven). |
| **QA gates** | All prior **G*** gates satisfied or explicitly waived with audit trail. |
| **HITL requirements** | **Mandatory** — this stage **is** HITL. |
| **SAFE UNKNOWN escalation** | Missing approver role → **UNKNOWN**; do not deliver. |
| **downstream dependencies** | Delivery / Export. |

---

### Stage 15 — Delivery / Export

| Field | Content |
|-------|---------|
| **stage_id** | `WF_V0_S15_DELIVERY` |
| **purpose** | Package deliverables: static build, documentation bundle, handoff to hosting — **method project-specific**. |
| **primary agents** | Human ops/release; **no** dedicated “delivery agent” claimed in v0. |
| **input artifacts** | Approved artifacts; build output; runbooks. |
| **output artifacts** | Delivery package; **report** narrative per execution-flow; optional **log** hooks (**future**). Future Factory-native WordPress handoff through WPilot may add approved template/content payload, dry-run diff, rollback notes, and human publish approval as project-specific delivery artifacts. |
| **registries used** | Contracts as **reference** for what was delivered; not executable. |
| **QA gates** | Checksum/manifest; smoke on **target** environment (**if** known). |
| **HITL requirements** | **G7**: ops/client when **public** deploy. |
| **SAFE UNKNOWN escalation** | Hosting/CDN/CMS details **unknown** → **SAFE UNKNOWN** in delivery notes; no false “live” claim. WPilot WordPress publishing remains **SAFE UNKNOWN** unless a separate integration contract, target site, approval artifact, and rollback path exist. |
| **downstream dependencies** | None within v0 factory chain; **post-delivery** monitoring **out of scope** for this doc. |

---

## Workflow failure classes

Examples of **failure classes** (non-exhaustive). Each should map to **signals** and **orchestration response** when a Control Plane exists; today they guide **human runbooks**.

| Failure class | Typical cause | Primary signals | Orchestration response (intent) |
|---------------|---------------|-----------------|----------------------------------|
| **Insufficient business context** | Thin intake, missing ICP or offer | **UNKNOWN**, **SAFE UNKNOWN** | **Pause** at **S01** / **S03**; gather context |
| **Conflicting SEO / commercial goals** | Traffic vs conversion tradeoffs unresolved | **NEED HUMAN APPROVAL**, **STRUCTURE CHANGE** | **Pause** at **S03**; leadership arbitration |
| **Impossible CTA flow** | IA cannot support stated funnel | **STRUCTURE CHANGE** | Return to **S04** or **S03**; **block** blueprint |
| **Unsupported frontend requirement** | Framework/CMS not in static factory model | **UNKNOWN**, **STRUCTURE CHANGE** | **Block** at **S10**–**S11**; explicit scope change |
| **Design inconsistency** | Templates drift vs tokens/handoff | **STRUCTURE CHANGE** | **S08** revision loop; freeze gate reset |
| **Registry mismatch** | Block / site type / contract conflict | **STRUCTURE CHANGE**, **SAFE UNKNOWN** | Amend registry **or** blueprint under governance |
| **QA rejection** | Failed checklist or Validator outcome | **NEED HUMAN APPROVAL** (waivers) | **Return** to nearest upstream fix (often **S05**–**S12**) |
| **Unknown stack** | Build, host, CI not defined | **SAFE UNKNOWN** | Document assumptions; **limit** claims in delivery |

---

## Escalation rules

### When the workflow **pauses**

- Emit **UNKNOWN** when **required binding** is missing (e.g. approver, stack decision).
- Emit **SAFE UNKNOWN** only when **policy** allows bounded continuation with explicit documentation of assumptions.
- **Downstream stages** must **not** start until the **pause reason** is cleared or **waived** with HITL.

### When the workflow **requests HITL**

- Set **NEED HUMAN APPROVAL** on the **Task** (conceptually) and record **hitl_gate** id.
- **Block** the **next** stage until approval artifact exists (format **TBD**).

### When the workflow returns **UNKNOWN** / **SAFE UNKNOWN**

- **UNKNOWN**: **hard stop** for affected branch until resolved.
- **SAFE UNKNOWN**: continue **only** with **written** assumptions and **risk_level** review; escalate to full **UNKNOWN** if assumptions prove false.

### When downstream stages are **blocked**

- **QA rejection** without waiver → **no** Design freeze, **no** Frontend freeze, **no** Delivery.
- **SECURITY RISK** → follow **Control Plane** / security policy; **no** delivery until cleared.
- **STRUCTURE CHANGE** → **re-plan** slice; may invalidate prior approvals for affected pages — **re-run** minimum stage sequence for that slice.

---

## Artifact flow map (readable)

### How artifacts move

```text
Intake / scope
       → site_type_id + strategy / SEO pack
       → IA (sitemap, templates, URLs)
       → Blueprint set (per Page Blueprint Contract v0)
       → [Page Blueprint QA Checklist v0] → approved blueprints
       → Design Handoff pack (Design Handoff Contract v0)
       → Design files / specs
       → [Design QA] → frozen design
       → Frontend Handoff spec (Frontend Handoff Contract v0)
       → Frontend source / build
       → [Frontend QA] → [Final Validation]
       → Human approval → Delivery package
```

### How contracts connect

- **Page Blueprint Contract v0** sits at the **center** between **strategy/IA** and **design/frontend** lanes.
- **Design Handoff Contract v0** bridges **blueprints** → **design production**.
- **Frontend Handoff Contract v0** bridges **frozen design + blueprints** → **static implementation**.

### Where registries participate

- **Site Type Registry v0**: **S02** through **S13** — classification, defaults, QA emphasis.
- **Block Registry v0**: **S04**–**S07**, **S10**–**S11** — block validity and semantic mapping.

### Where QA occurs

- **S06** — **Page Blueprint QA Checklist v0** (blueprint slice).
- **S09**, **S12**, **S13** — design, frontend, and cross-lane QA per [qa-validation-model.md](qa-validation-model.md) and specialist agents (**planned**).

### Where approvals occur

- **HITL** at **S01**–**S03** (intake, classification, strategy), **S03**–**S04** (scope/IA), **S05**–**S06** (blueprint + QA), **S08**–**S09** (design), **S10**–**S12** (handoff + frontend + QA), **S13**–**S15** (final go, release). Exact **G*** mapping aligns with [workflow-map.md](workflow-map.md).

---

## Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial orchestration model (documentation only). |
