# MARS Website Factory — agent map

**Status:** **planned** unless an existing MARS file proves a role is **implemented** or **active** with in-repo runtime evidence. Per `AGENTS.md`, this repository’s **Phase 1** agent definitions are **documentation-only**.

**Registry SoT:** [`../../agents/registry.md`](../../agents/registry.md) — **§4.1** lists planned **`agent_id`** rows (**no** agent cards yet). **This file** remains the **SoT** for **what each factory role does** in prose until cards are authored.

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
| **Gulp Frontend Agent** | HTML/SCSS/JS in **Gulp-oriented** static pipeline | **legacy-bridge** (per `agents/registry.md`; **not** a claim of in-repo Gulp code) |
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
- **No** separate agent cards for factory-only roles were found under `agents/` at registration time — **SAFE UNKNOWN** whether cards will live in `agents/` or only in this pack until authored.
