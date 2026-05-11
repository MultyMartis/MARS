# MARS Website Factory — Artifact types v0

**Status:** **documentation only** — taxonomy for **logical artifacts** moving through [website-factory-workflow-v0.md](website-factory-workflow-v0.md). **Not** a JSON schema registry, **not** storage layout.

**Related:** [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md).

---

## artifact_id philosophy

- **Stable within a project:** human-meaningful slug or UUID per project convention (same spirit as `blueprint_id`, `design_handoff_id` in v0 contracts).
- **Traceable:** downstream artifacts **reference** upstream ids in prose or tables; **no** mandated global registry service.
- **Versioning:** suffix or changelog row when semantics change materially (**STRUCTURE CHANGE**); exact policy **SAFE UNKNOWN** until authored.

---

## Type catalog

### Intake artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S01 Intake / Discovery |
| **Upstream** | Client briefs, stakeholder notes, optional analytics |
| **Downstream** | Site type classification, strategy |
| **Lifecycle** | Draft → reviewed → **approved** (G1); superseded if scope changes |
| **Mutable vs immutable** | Mutable during discovery; **approved** summary and **scope_in/scope_out** treated as **immutable baseline** unless HITL reopens |
| **HITL** | G1 — PM/lead confirms accuracy |
| **SAFE UNKNOWN** | Missing compliance or market facts → **UNKNOWN** / bounded **SAFE UNKNOWN** per policy |
| **QA relationship** | Completeness checks; no formal “intake schema” engine claimed |

### Strategy artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S03 Strategic Layer |
| **Upstream** | Intake, **site_type_id** |
| **Downstream** | IA, blueprints (positioning, funnel narrative) |
| **Lifecycle** | Hypothesis → **approved** memo (G2) |
| **Mutable vs immutable** | Messaging mutable until approval; **approved** narrative immutable for downstream unless **STRUCTURE CHANGE** |
| **HITL** | G2 — marketing lead |
| **SAFE UNKNOWN** | Conflicting goals → **NEED HUMAN APPROVAL** |
| **QA relationship** | Conversion QA may later test **consistency** with implemented pages |

### SEO strategy artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S03 (often joint with strategy) |
| **Upstream** | Intake, **site_type_id**, strategy memo |
| **Downstream** | IA (content requirements), blueprints (**SEO_intent**) |
| **Lifecycle** | Hypothesis doc → **approved** with strategy |
| **Mutable vs immutable** | Same as strategy; **approved** keyword/intent hypotheses are baseline for blueprint QA |
| **HITL** | G2 extension for sensitive verticals |
| **SAFE UNKNOWN** | SERP/competitive facts not verified → label **SAFE UNKNOWN**; no guaranteed rank claims |
| **QA relationship** | SEO QA lane ([qa-validation-model.md](qa-validation-model.md)) |

### IA artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S04 Information Architecture |
| **Upstream** | Approved strategy/SEO, **site_type_id** |
| **Downstream** | Page blueprints, internal linking |
| **Lifecycle** | Sitemap/templates draft → **approved** (G3 partial) |
| **Mutable vs immutable** | URLs/templates volatile until approval; **approved** IA **immutable** for blueprint batch unless change order |
| **HITL** | G3 — PM + tech lead for scope |
| **SAFE UNKNOWN** | Stack/CMS unknown → document assumptions |
| **QA relationship** | Blueprint QA checks CTA targets against IA |

### Blueprint artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S05 Page Blueprint Generation |
| **Upstream** | IA, strategy, **Block** / **Site Type** registries |
| **Downstream** | Blueprint QA, design handoff |
| **Lifecycle** | Per-page logical docs → batch **approval** (G3) |
| **Mutable vs immutable** | Editable until approval; post-approval changes require revision + re-gate |
| **HITL** | G3, G6 downstream consumers |
| **SAFE UNKNOWN** | Per [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md) **notes** |
| **QA relationship** | [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md) |

### Design handoff artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S07 Design Handoff |
| **Upstream** | Approved blueprints |
| **Downstream** | Design production |
| **Lifecycle** | Pack per page → design lead sign-off |
| **Mutable vs immutable** | Mutable during pack assembly; **frozen** after G5 design baseline |
| **HITL** | Design lead before production |
| **SAFE UNKNOWN** | Export tooling **TBD** per [design-handoff-contract-v0.md](design-handoff-contract-v0.md) |
| **QA relationship** | Design QA compares outputs to pack |

### Design artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S08 Design Production |
| **Upstream** | Design handoff, brand system |
| **Downstream** | Design QA, frontend handoff |
| **Lifecycle** | Wireframes → hi-fi → **frozen** |
| **Mutable vs immutable** | Iterative until freeze; **frozen** immutable for frontend without change order |
| **HITL** | G4, G5 |
| **SAFE UNKNOWN** | File format per project |
| **QA relationship** | Design QA lane |

### Frontend handoff artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S10 Frontend Handoff |
| **Upstream** | Frozen design, blueprints |
| **Downstream** | Frontend production |
| **Lifecycle** | Spec doc → tech lead approval |
| **Mutable vs immutable** | Editable until **S11** start; then treat as **build contract** |
| **HITL** | Tech lead approval |
| **SAFE UNKNOWN** | Exact `src` paths, CI name |
| **QA relationship** | Frontend QA uses **QA_requirements** fields ([frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md)) |

### Frontend production artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S11 Frontend Production |
| **Upstream** | Frontend handoff, copy deck |
| **Downstream** | Frontend QA, final validation |
| **Lifecycle** | PR / file set → reviewed → merged (project-defined) |
| **Mutable vs immutable** | Code mutable under change control; **release tag** intent immutable once approved |
| **HITL** | G6 |
| **SAFE UNKNOWN** | Build/CI evidence per environment |
| **QA relationship** | Frontend QA + Validator (when exists) |

### QA artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S06, S09, S12, S13 (lane-specific) |
| **Upstream** | Subject artifact under test + checklists |
| **Downstream** | Waivers, fix loops, approval |
| **Lifecycle** | Report emitted per run/review |
| **Mutable vs immutable** | Append-only audit narrative preferred; **verdict** immutable once filed unless superseded by new run |
| **HITL** | Waivers, blockers per gate |
| **SAFE UNKNOWN** | Evidence gaps → flagged in report ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)) |
| **QA relationship** | Self-referential; feeds **validation** summary |

### Validation artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S13 Final Validation (aggregate); Validator may appear earlier **when** routed |
| **Upstream** | Consolidated lane outputs |
| **Downstream** | Human approval |
| **Lifecycle** | **go** / **no-go** recommendation |
| **Mutable vs immutable** | Recommendation fixed for that run id |
| **HITL** | G7 prep |
| **SAFE UNKNOWN** | Cross-lane gaps explicitly listed |
| **QA relationship** | Cross-cutting; **complements** specialist QA ([qa-validation-model.md](qa-validation-model.md)) |

### Approval artifact

| Aspect | Content |
|--------|---------|
| **Owner stage** | S14 Human Approval |
| **Upstream** | Validation / risk summary |
| **Downstream** | Delivery |
| **Lifecycle** | Signed / recorded approval (**format TBD**) |
| **Mutable vs immutable** | **Immutable** record; revocation = new approval cycle |
| **HITL** | **Mandatory** — this artifact **is** HITL |
| **SAFE UNKNOWN** | Missing approver role → **UNKNOWN** |
| **QA relationship** | Audits trace waivers to approver |

---

*Last updated: 2026-05-11.*
