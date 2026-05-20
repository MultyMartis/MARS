# MARS — Project registry

**Normative role:** This file is the **single source of truth** for **projects** in the MARS repository. Introspection, governance consumers, and human operators **must** treat rows defined here as authoritative for **project identity** and **project-level lifecycle fields** listed below. If a project is not listed, its project facts are **unknown** at registry level until a row is added (see `../interfaces/introspection-v0.md` — **SAFE UNKNOWN** for unresolved `<id>`).

**Version:** v0 (append or amend rows per `../governance/versioning-model.md` when governance requires it).

---

## Record schema (required fields)

Each project **must** have exactly one row (or one structured record) with:

| Field | Type / values | Meaning |
|-------|----------------|---------|
| **project_id** | Opaque string, stable | Unique project identifier used in introspection **PROJECT** mode and in cross-references. |
| **status** | `planned` \| `active` \| `archived` | Lifecycle band: not yet started, in use, or retired from active work. |
| **phase** | String | Current or target MARS / product phase label (align with `../README.md`, `../governance/` phase vocabulary when applicable). |
| **related_entities** | List or comma-separated ids | Agent names, cards, or other registry entity ids tied to this project (see `../agents/registry.md`). |
| **last_updated** | ISO-8601 date (or datetime) | When this row was last reviewed or changed. |

Optional narrative columns may be added **only** if governance documents them; do not use optional columns to bypass the required fields above.

---

## Projects (authoritative table)

| project_id | status | phase | related_entities | last_updated |
|------------|--------|-------|------------------|--------------|
| *example:* `mars-core` | planned | Phase 1 | *(none yet)* | 2026-04-27 |
| `seo-content-agent` | planned | **legacy** — early spec / single-tool bridge artifacts under `projects/seo-content-agent/`; **canonical** docs: `metabot-seo-content-agent` | *(none yet)* | 2026-05-04 |
| `metabot-seo-content-agent` | active | **canonical** documentation pack — external multi-workflow AI system (n8n runtime); Intake / Worker / Admin (+ future File Export); in-repo docs only | *(none yet)* | 2026-05-10 |
| `mars-website-factory` | planned | **strategic** — documentation-first multi-agent **website production** direction (contracts, registries, workflows, QA, HITL); **not** runtime-ready; see `../projects/mars-website-factory/README.md` | Gulp Frontend Agent, Validator Agent (catalog only; see `../agents/registry.md`) | 2026-05-11 |
| `triumph-manipulator-landing` | planned | **Website Factory production pack** — initialized documentation + local workspace placeholder; **not** deployed site; see `../projects/triumph-manipulator-landing/README.md` | Gulp Frontend Agent | 2026-05-13 |
| `orca` | active | **OPERATIONAL** — human-supervised PPC operational toolkit and live review framework; **not** runtime-ready; runtime status: **EXCLUDED**; owner system: MARS documentation / human operator workflow; see `../projects/orca/README.md` | *(none yet)* | 2026-05-18 |
| `wpilot` | active | **OPERATIONAL** — human-supervised WordPress administration (External Systems lane); Phase 1 documentation + **planned** plugin bridge; **not** MARS runtime, **not** autonomous CMS; see `../projects/wpilot/README.md` | *(none yet)* | 2026-05-19 |
| `homegateway-v4-ai` | planned | **OPERATIONAL** — documentation-first **Personal Operational Cockpit** (private web UI surface layer); **STATIC-FIRST** target; **not** MARS agent, **not** n8n workflow, **not** Telegram bot, **not** control plane; see `../projects/homegateway-v4-ai/README.md` | *(none yet)* | 2026-05-20 |

*(Replace the example row or add rows as projects are formally registered.)*

**IdeaBox / `continuity/` (cross-cutting — not a project row):** **IdeaBox** (`../continuity/`) is **not** registered here as a `project_id`. **Status:** **OPERATIONAL** (human-operated discipline). **Type:** filesystem-backed operational continuity workflow. **Authority:** human-operated. **Purpose:** continuity, idea capture, anti-entropy, operational memory hygiene. It **does not** imply runtime code, autonomous memory, orchestration, or governance auto-mutation — see `../continuity/README.md`, governance overview `../governance/README.md`.

**ORCA boundaries:** **ORCA** (`projects/orca/`) is registered as **OPERATIONAL** documentation and human-supervised PPC workflow support. Runtime, autonomous optimization, bidding, scheduling, queueing, validator daemons, and orchestration are **EXCLUDED**. Experimental extensions, if any, must remain clearly labeled **EXPERIMENTAL** and outside runtime claims. Boundary-only references should be marked **BOUNDARY ONLY** when they exist only to prevent drift.

**WPilot boundaries:** **WPilot** (`projects/wpilot/`) is registered as **OPERATIONAL** human-supervised WordPress workflow documentation (External Systems lane). Live WordPress, Beget/hosting, credentials, and plugin runtime are **external** and **EXCLUDED** from MARS core. The MetaCODE WPilot **plugin** remains **PLANNED** documentation only until source and deployment evidence exist — see `../projects/wpilot/plugin-mvp/reconciliation-map-v0.md`.

**HomeGateway v4.ai boundaries:** **HomeGateway** (`projects/homegateway-v4-ai/`) is registered as **OPERATIONAL** documentation for a **Personal Operational Cockpit** — a private web **surface layer** for links, clients/projects, deadlines, display-only MARS/bot/n8n signals, and quick actions. It is **not** a MARS agent, **not** an n8n workflow, **not** a Telegram bot, **not** an autonomous system, **not** a deployed runtime, **not** an active MARS control plane, and **not** a replacement for MARS, ORCA, WPilot, MetaBOT, or GitGuard. Runtime, backend, live integrations, and admin CRUD are **EXCLUDED** until explicit phase evidence exists — see `../projects/homegateway-v4-ai/roadmap-v0.1.md`.

**GitGuard:** Named as a **Program / Operational System** example in `../governance/system-entity-model.md` only — **no** `project_id` row here until a pack and human registration exist (**SAFE UNKNOWN** at registry level).

**Topology navigation:** Compact ecosystem map — `../governance/ecosystem-topology-index.md`; external systems — `../governance/external-systems-relationship-map-v0.md`.

**Note:** **`metabot-seo-content-agent`** (`projects/metabot-seo-content-agent/`) is the **canonical** MARS folder for **MetaBOT — SEO Content Agent** documentation, sanitized exports (`exports/`), and integration contracts. **`seo-content-agent`** (`projects/seo-content-agent/`) is **legacy** (early spec / bridge); **do not** add new docs there. Reconcile execution detail against **live n8n**, not only markdown.

---

## Maintenance rules

1. **Single source of truth** — Do not duplicate canonical project rows in other markdown files; **link** to this file or cite `project_id` instead.
2. **Consistency** — When **status** or **phase** changes, update **last_updated** and prefer recording a matching event in `../logs/lifecycle-log.md`.
3. **No shadow registries** — Spreadsheets, chats, or external tools are **not** authoritative unless their content is reflected here.
