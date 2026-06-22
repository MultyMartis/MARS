# MARS Website Factory — layer map

**Status:** **planned** — design vocabulary for the factory. Layers are **not** separate deployed services unless future implementation proves otherwise.

For each layer: **purpose**, **planned agents**, **expected artifacts**, **QA gates**, **SAFE UNKNOWN risks**.

---

## 1. Intake / Discovery

| Aspect | Content |
|--------|---------|
| **Purpose** | Capture client goals, constraints, brand inputs, compliance boundaries, and success metrics; normalize into factory-ready **scope** for downstream tasks. |
| **Planned agents** | **Project Intake Agent**; **Site Type Classifier Agent** (may be one logical step or split). |
| **Expected artifacts** | Intake brief, constraint list, stakeholder map, raw asset inventory (links), **SAFE UNKNOWN** flags where facts are missing. |
| **QA gates** | Completeness check vs **Task** / workflow template; **Validator Agent** or human checklist on PII/secrets in pasted content; **NEED HUMAN APPROVAL** for ambiguous legal/compliance scope. |
| **SAFE UNKNOWN risks** | Incomplete intake leading to fabricated strategy; unclear **site type** → wrong registry defaults. |

---

## 2. Strategic Layer

| Aspect | Content |
|--------|---------|
| **Purpose** | Positioning, messaging hierarchy, funnel assumptions, channel hints; feeds IA and page priorities. |
| **Planned agents** | **Marketing Strategy Agent**; **SEO Strategy Agent** (parallel or sequential with explicit handoff contract). |
| **Expected artifacts** | Strategy memo, keyword / topic hypotheses, competitive framing (evidence-cited or explicitly bounded **SAFE UNKNOWN**). |
| **QA gates** | **Validator Agent**: claims without sources → **SAFE UNKNOWN**; brand alignment review; optional human sign-off before IA. |
| **SAFE UNKNOWN risks** | SEO “facts” invented; strategy drift vs intake. |

---

## 3. Page Architecture Layer

| Aspect | Content |
|--------|---------|
| **Purpose** | Site map, templates, URL logic, content requirements per page, internal linking rules. |
| **Planned agents** | **Information Architecture Agent**; **Page Blueprint Agent**. |
| **Expected artifacts** | Sitemap (structured), page blueprint set (one per page), content block requirements, navigation model. |
| **QA gates** | Consistency vs strategy; orphan pages; duplicate intent; **Validator** structural checks vs **Block Registry** (when it exists). |
| **SAFE UNKNOWN risks** | Blueprints that assume CMS features not in static stack; scale of pages unbounded. |

---

## 4. Design Layer

| Aspect | Content |
|--------|---------|
| **Purpose** | UX structure, wireframes, visual design direction, design-system alignment. |
| **Planned agents** | **UX Structure Agent**; **Wireframe Generator Agent**; **AI Designer Agent**; **Full Design Generator Agent** (may collapse to fewer cards in implementation). |
| **Expected artifacts** | Wireframes, design specs / tokens reference, component-level notes, export manifests (format **TBD** — **SAFE UNKNOWN** for Figma vs markdown-only). |
| **QA gates** | **Design QA Agent**; human approval before frontend handoff; accessibility heuristic pass (**planned**). |
| **SAFE UNKNOWN risks** | Design artifacts not translatable to static sections; brand token drift. |

---

## 5. Production Layer

| Aspect | Content |
|--------|---------|
| **Purpose** | Implement approved design as **HTML / SCSS / JS** in a **Gulp-oriented** static pipeline (target profile per legacy docs); reusable sections; no manual `dist` edits. |
| **Planned agents** | **Gulp Frontend Agent** (see `agents/registry.md` — **legacy-bridge** catalog entry). |
| **Expected artifacts** | Source files under agreed tree, build output per policy, implementation report, diff summary. |
| **QA gates** | **Frontend QA Agent**; build succeeds; **Validator** on secrets / unsafe patterns; responsive smoke criteria. |
| **SAFE UNKNOWN risks** | Repo has **no** evidenced Gulp starter here — implementation environment is **external** to this doc pack; merge conflicts; global JS pollution. |

---

## 6. QA / Validation Layer

| Aspect | Content |
|--------|---------|
| **Purpose** | Cross-cutting quality: technical, design fidelity, SEO on-page, conversion heuristics; consolidation before release. |
| **Planned agents** | **Frontend QA Agent**, **Design QA Agent**, **SEO QA Agent**, **Conversion QA Agent**; **Validator Agent** as **integration** for policy and task-contract alignment (`agents/registry.md`). |
| **Expected artifacts** | QA report, issue list with severities, **signals** (`UNKNOWN`, **SAFE UNKNOWN**, **NEED HUMAN APPROVAL**, **STRUCTURE CHANGE**) per `workflows/execution-flow.md`. |
| **QA gates** | Release blocked on open **P0**; human approval for public deploy. |
| **SAFE UNKNOWN risks** | Automated QA depth **not** proven in MARS; overlap between Validator and specialist QA roles unless scoped in contracts. |

---

## 7. Supervisory Layer

| Aspect | Content |
|--------|---------|
| **Purpose** | Orchestration semantics: bind **Tasks**, enforce **HITL**, route stages, merge state — aligns with **Control Plane** design (`control-plane/contract.md`) **when** a runtime exists; until then, **human** supervision. |
| **Planned agents** | No separate “supervisor bot” required in v0 docs — **Control Plane** + human operator; optional **Documentation Agent** for pack maintenance. |
| **Expected artifacts** | Run records (**planned**), lifecycle log entries, approved stage transitions. |
| **QA gates** | **hitl_gates** on **Task** (`workflows/task-contract-v0.md`); escalation on **SECURITY RISK**. |
| **SAFE UNKNOWN risks** | Assuming autonomous orchestration without runtime; unclear ownership between human PM and Control Plane. |

---

## 8. Artifact Bus (cross-cutting documentation)

The **Artifact Bus Layer v0** is **not** an eighth runtime pipeline — it is **shared semantics** for how logical artifacts are **enveloped, routed, transferred, published, consumed,** and **invalidated** across layers **1–7**, aligned with [website-factory-workflow-v0.md](website-factory-workflow-v0.md) and [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md). SoT: [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md) and linked bus docs in [README.md](README.md). **Documentation only** — **not** a queue, **not** an event engine, **not** Kafka/Rabbit-style transport, **not** async execution infrastructure, **not** hidden state sync.

---

## 9. Candidate WordPress Implementation Layer

| Aspect | Content |
|--------|---------|
| **Purpose** | Transform **approved Website Factory frontend packages** into **WordPress implementation packages** (theme/plugin architecture, content model, templates, admin UX planning, QA-gated handoff). |
| **Subsystem** | **Forge WordPress** — [subsystems/forge-wordpress/](subsystems/forge-wordpress/README.md) (**FOUNDATION / PRE-OPERATIONAL**; FW-04 complete; [capability pack](subsystems/forge-wordpress/capability/OPERATIONAL-INDEX.md) **documented**; local execution **not ready**). |
| **Planned agents** | **SAFE UNKNOWN** — `AG-WP-001` internal seed only; **not** registered; [promotion decision](subsystems/forge-wordpress/capability/reports/FORGE-WORDPRESS-AG-WP-001-PROMOTION-DECISION-v1.md) defers registration until synthetic validation. |
| **Expected artifacts** | Per [FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md](subsystems/forge-wordpress/FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md) — **defined**; none evidenced on disk for pilots yet. |
| **QA gates** | **WV0–WV9** — [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](subsystems/forge-wordpress/FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md); Factory VL0–VL6 applies **upstream** only. |
| **Downstream** | **WPilot** — controlled WordPress **operations** (not development). |
| **SAFE UNKNOWN risks** | Conflating **MARS Forge** (frontend overlay) with **Forge WordPress**; starting implementation before Phase 1 architecture; duplicating WPilot operations scope. |
| **Status honesty** | **Candidate layer** — **not** operational, **not** runtime, **not** a built production layer until architecture approval and pilot evidence. |
