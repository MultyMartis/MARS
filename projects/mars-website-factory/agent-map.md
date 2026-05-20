# MARS Website Factory — agent map

**Status:** **planned** unless an existing MARS file proves a role is **implemented** or **active** with in-repo runtime evidence. Per `AGENTS.md`, this repository’s **Phase 1** agent definitions are **documentation-only**.

**Registry SoT:** [`../../agents/registry.md`](../../agents/registry.md) — **§4.1** lists planned **`agent_id`** rows with links to **agent cards** (v0) under [`../../agents/cards/`](../../agents/cards/). **This file** remains the **SoT** for extended **what each factory role does** in prose; **cards** add contracts, I/O boundaries, QA, and escalation fields per [`../../agents/agent-card-template.md`](../../agents/agent-card-template.md) vocabulary. **Dependency map:** factory pack **`entity_id`** s in [`../../governance/dependency-map.md`](../../governance/dependency-map.md) §4 — **documentation-only**, not a runtime graph.

**Agent cards (v0):** one Markdown card per planned factory **`agent_id`** — paths in [`../../agents/registry.md`](../../agents/registry.md) §4.1; all files live under [`../../agents/cards/`](../../agents/cards/) (**documentation-only**; **not** runtime).

## Legend

| Label | Meaning |
|-------|---------|
| **planned** | Role accepted for factory design; no implementation claim. |
| **legacy-bridge** | Catalogued in MARS with legacy alignment (see registry rows). |

---

## Planned factory agents

| Agent | Factory role | Default status (evidence-based) |
|-------|----------------|----------------------------------|
| **Project Intake Agent** | Structured intake, scope, constraints | **planned** |
| **Site Type Classifier Agent** | Maps project to **Site Type Registry** defaults | **planned** |
| **Marketing Strategy Agent** | Positioning, messaging, funnel narrative | **planned** |
| **SEO Strategy Agent** | Topics, intent, on-page strategy (hypothesis-level) | **planned** |
| **Information Architecture Agent** | Sitemap, templates, URL/content requirements | **planned** |
| **Page Blueprint Agent** | Per-page block specs, linking, CTA logic | **planned** |
| **UX Structure Agent** | Layout hierarchy, responsive behavior intent | **planned** |
| **AI Designer Agent** | Visual direction, tokens, component styling intent | **planned** |
| **Wireframe Generator Agent** | Low-fidelity structure artifacts | **planned** |
| **Full Design Generator Agent** | High-fidelity spec / export (**format TBD**) | **planned** |
| **Design Governance Agent** | Canonical **Design Implementation Pack** (`design/vN/semantics`, `implementation-pack`, `validation`); bridges approved design → machine-readable frontend law | **planned** ([`../../agents/design-governance-agent.md`](../../agents/design-governance-agent.md), [`../../agents/cards/design-governance-agent-v0.md`](../../agents/cards/design-governance-agent-v0.md); [design-governance-layer.md](design-governance-layer.md); **not** runtime) |
| **Gulp Frontend Agent** | HTML/SCSS/JS in **Gulp-oriented** static pipeline | **operational_doc_pack** (per `agents/registry.md`; doc pack — **not** autonomous runtime, **not** in-repo Gulp code) |
| **Frontend QA Agent** | Build, markup, a11y heuristics, responsive checks | **planned** |
| **Design QA Agent** | Fidelity vs approved design | **planned** |
| **SEO QA Agent** | On-page SEO, metadata, heading hierarchy | **planned** |
| **Conversion QA Agent** | CTA clarity, form friction, trust signals | **planned** |

## Validator Agent integration

| Aspect | Content |
|--------|---------|
| **Role** | **Validator Agent** — independent checks vs **task contract**, policy, structure; aligns with legacy **FlyCheck** concept (`agents/registry.md`, `web-gpt-sources/04_agents.md`). |
| **Status** | **planned** / **legacy-bridge** in registry — **no** automated Validator runtime evidenced in MARS core. |
| **Integration** | Invoked at **validate** stage in `workflows/execution-flow.md`; factory QA agents **complement** Validator (specialist depth) rather than replace it — exact split **TBD** in contracts. |

## Existing MARS evidence (for honesty)

- **Gulp Frontend Agent** and **Validator Agent** appear in **`agents/registry.md`** with documented statuses.
- Legacy **Gulp** profile text exists in **`web-gpt-sources/04_agents.md`** (embedded section).
- **Website Factory** planned roles have **v0 cards** under **`agents/cards/`** (see **`agents/registry.md`** §4.1) — **documentation-only**; **no** factory agent runtime evidenced in MARS core.
