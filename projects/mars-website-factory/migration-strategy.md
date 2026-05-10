# MARS Website Factory — migration strategy

## Sources consolidated

| Source | Role |
|--------|------|
| **`web-gpt-sources/04_agents.md`** | Legacy **Gulp Frontend Agent** and **Validator Agent** narratives |
| **`web-gpt-sources/03_core.md`** | Imported capability map rows: web development, page generation, frontend coding, QA |
| **`web-gpt-sources/05_workflows.md`**, **`02_architecture.md`** | **prompt → execute → report** and expanded workflow ideas (**requirements**, not shipped v1) |
| **`agents/registry.md`** | **Gulp Frontend Agent** (**legacy-bridge**), **Validator Agent** (**planned** / **legacy-bridge**) |
| **`workflows/execution-flow.md`** | Canonical **validate** stage and **Validator** placement |

## What “migration” means here

**Not** a database migration. **Documentation migration** means:

1. **Naming** Website Factory as the **umbrella** for multi-agent **static site** production in MARS.
2. **Avoiding** duplicate SoT — factory details live under `projects/mars-website-factory/`; core contracts stay in `governance/`, `workflows/`, `agents/`.
3. **Preserving** honesty: legacy imported files remain **legacy imported** per root `README.md` three-way split.

## Coexistence with MetaBOT SEO Content Agent

- **MetaBOT** pack = **external** orchestrated product documentation.
- **Website Factory** = **strategic** in-repo direction for **site factory** semantics.
- Cross-links may be added when **integration** is scoped; **no** integration assumed at registration.

## SAFE UNKNOWN

- Deprecation of any legacy path inside `web-gpt-sources` — **not** decided here.
- Whether **Gulp Frontend Agent** gets a full **agent card** file under `agents/` — **future** work ([implementation-phase-1.md](implementation-phase-1.md)).
