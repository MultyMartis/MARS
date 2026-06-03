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
| `mig` | active | **OPERATIONAL** — **R1** market groundtruth acquisition; **narrow v0.1** session spine in-repo (Node.js + n8n export); human-supervised; **not** production runtime, orchestration, or ORCA automation; see `../projects/mig/README.md` | *(none yet)* | 2026-06-02 |
| `ocpilot` | active | **OPERATIONAL** — human-supervised OpenCart / ocStore operational pack (External Systems lane); Phase 0+ documentation baseline; **not** MARS runtime, **not** autonomous CMS; sibling to `wpilot`; see `../projects/ocpilot/README.md` | *(none yet)* | 2026-06-02 |
| `ear-runtime` | active | **ENGINEERING** — EAR Runtime Program (Mode 2 acquisition helpers); R1 foundation skeleton + config loader only; **not** live connector or production acquisition; see `../projects/ear-runtime/README.md` | *(none yet)* | 2026-06-02 |
| `mars-survivability` | active | **OPERATIONAL** — survivability / safe execution documentation pack (contracts, protocols, registries, human-invoked tools); **not** automated enforcement or policy engine; extends governance S3; see `../projects/mars-survivability/README.md` | *(none yet)* | 2026-06-02 |
| `nova` | planned | **FOUNDATION** — documentation-first Mobile Application Factory methodology (RBM v1 complete); **not** runtime, **not** agent cards; implementation **not started**; see `../projects/nova/README.md` | *(none yet)* | 2026-06-02 |
| `wpilot` | active | **OPERATIONAL** — human-supervised WordPress administration (External Systems lane); Phase 1 documentation + **planned** plugin bridge; **not** MARS runtime, **not** autonomous CMS; see `../projects/wpilot/README.md` | *(none yet)* | 2026-05-19 |
| `homegateway-v4-ai` | planned | **PLANNED / DRAFT** — documentation-first **Personal Operational Cockpit** (private web UI surface layer); **STATIC-FIRST** target; **not** MARS agent, **not** n8n workflow, **not** Telegram bot, **not** control plane; see `../projects/homegateway-v4-ai/README.md` | *(none yet)* | 2026-06-02 |

*(Replace the example row or add rows as projects are formally registered.)*

**IdeaBox / `continuity/` (cross-cutting — not a project row):** **IdeaBox** (`../continuity/`) is **not** registered here as a `project_id`. **Status:** **OPERATIONAL** (human-operated discipline). **Ecosystem role:** **Incubation Layer** (optional — **not** a mandatory entry path). **Use when:** an idea exists but implementation is deferred. **Direct creation** of program packs or governance docs remains valid without IdeaBox. **Type:** filesystem-backed operational continuity workflow. **Authority:** human-operated. **Purpose:** continuity, idea capture, anti-entropy, operational memory hygiene. It **does not** imply runtime code, autonomous memory, orchestration, or governance auto-mutation — see `../continuity/README.md`, `../logs/cleanup/actions/ideabox-alignment-v1.md`.

**GitGuard (cross-cutting — not a project row):** **REGISTERED** (Wave 2B, 2026-06-03) as **Repository Survivability Layer** — human-operated advisory framework under `../projects/mars-survivability/` (contracts, validator, helpers, observability). **Responsibilities (documented):** checkpoint visibility, freeze visibility, rollback visibility, baseline visibility, backup intelligence, release traceability. **Not** a `project_id` row, **not** `projects/gitguard/` pack, **not** autonomous product. **SoT:** `../projects/mars-survivability/registries/gitguard-system-entry-v1.md`. Evidence: `../logs/cleanup/actions/gitguard-registration-v1.md`.

**ORCA boundaries:** **ORCA** (`projects/orca/`) is registered as **OPERATIONAL** documentation and human-supervised PPC workflow support. Runtime, autonomous optimization, bidding, scheduling, queueing, validator daemons, and orchestration are **EXCLUDED**. Experimental extensions, if any, must remain clearly labeled **EXPERIMENTAL** and outside runtime claims. Boundary-only references should be marked **BOUNDARY ONLY** when they exist only to prevent drift.

**MIG boundaries:** **MIG** (`projects/mig/`) is registered as **OPERATIONAL** for **R1** market groundtruth acquisition. **v0.1** in-repo session spine (Node.js + n8n workflow export) is **narrow experimental tooling** — **not** production deployment, orchestration platform, or ORCA transport. Full vision (SERP, competitor, local pack, reviews, trust, offer, CTA, evidence grading) remains **mostly planned** beyond v0.1. Canonical split: **MIG acquires reality; ORCA interprets reality.** Intent/semantic clustering, campaign architecture, LRL, PPC exports, Factory blueprints, content generation, CMS operations, production automation, and autonomous handoff are **EXCLUDED**. Handoff to ORCA is **human-only** per `../projects/mig/contracts/mig-orca-handoff-contract-v0.md`.

**OCPilot boundaries:** **OCPilot** (`projects/ocpilot/`) is registered as **OPERATIONAL** human-supervised OpenCart / ocStore workflow documentation (External Systems lane). Live hosting, FTP/PMA, credentials, and production file/DB writes are **external** and **EXCLUDED** from MARS core. **Sibling** to WPilot — **not** child or parent. Reuses survivability **patterns** only; does not inherit WPilot implementation.

**EAR Runtime boundaries:** **EAR Runtime** (`projects/ear-runtime/`) is the **engineering home** for Mode 2 acquisition helpers per frozen EAR Architecture (`shared/external-access-runtime/`). Current in-repo code is **R1 foundation skeleton + config loader only** — **not** live SFTP connector, snapshot publisher, or PILOT-001 execution. Architecture normative design stays in `shared/external-access-runtime/`; runtime **must not** silently amend architecture.

**MARS Survivability boundaries:** **mars-survivability** (`projects/mars-survivability/`) centralizes incident-informed survivability contracts, protocols, registries, and human-invoked CLI aids. It **extends** `governance/operational-survivability.md` and repo-wide `AGENTS.md` / `.cursorrules` — **does not** replace them. **Not** automated GitGuard product, policy engine, or filesystem sandbox.

**NOVA boundaries:** **NOVA** (`projects/nova/`) is registered as **FOUNDATION** documentation for mobile/PWA production methodology (RBM v1). **Not** runtime, orchestration, agent cards, or governance system. Mobile counterpart philosophy to Website Factory — implementation **not started** until chartered Agent Cards phase.

**WPilot boundaries:** **WPilot** (`projects/wpilot/`) is registered as **OPERATIONAL** human-supervised WordPress workflow documentation (External Systems lane). Live WordPress, Beget/hosting, credentials, and plugin runtime are **external** and **EXCLUDED** from MARS core. MetaCODE WPilot plugin **source exists in-repo** under `../projects/wpilot/plugin/metacode-wpilot/` (DEV / repository-only implementation evidence); production deployment and runtime bridge ownership remain **SAFE UNKNOWN / EXTERNAL** — see `../projects/wpilot/plugin-mvp/reconciliation-map-v0.md`.

**HomeGateway v4.ai boundaries:** **HomeGateway** (`projects/homegateway-v4-ai/`) is registered with **`status: planned`** — **PLANNED / DRAFT** program with an **operational documentation pack** (discipline for how docs are maintained; **not** product maturity “operational”). Classification: **documentation-first planned program** + **UI prototype workspace** (`workspaces/homegateway-v4-ai/v1/`). It is a private web **surface layer** for links, clients/projects, deadlines, display-only MARS/bot/n8n signals, and quick actions. It is **not** a MARS agent, **not** an n8n workflow, **not** a Telegram bot, **not** an autonomous system, **not** a deployed runtime, **not** an active MARS control plane, and **not** a replacement for MARS, ORCA, WPilot, MetaBOT, or GitGuard. Runtime, backend, live integrations, and admin CRUD are **EXCLUDED** until explicit phase evidence exists — see `../projects/homegateway-v4-ai/roadmap-v0.1.md`.

**Topology navigation:** Compact ecosystem map — `../governance/ecosystem-topology-index.md`; external systems — `../governance/external-systems-relationship-map-v0.md`.

**Note:** **`metabot-seo-content-agent`** (`projects/metabot-seo-content-agent/`) is the **canonical** MARS folder for **MetaBOT — SEO Content Agent** documentation, sanitized exports (`exports/`), and integration contracts. **`seo-content-agent`** (`projects/seo-content-agent/`) is **legacy** (early spec / bridge); **do not** add new docs there. Reconcile execution detail against **live n8n**, not only markdown.

---

## Maintenance rules

1. **Single source of truth** — Do not duplicate canonical project rows in other markdown files; **link** to this file or cite `project_id` instead.
2. **Consistency** — When **status** or **phase** changes, update **last_updated** and prefer recording a matching event in `../logs/lifecycle-log.md`.
3. **No shadow registries** — Spreadsheets, chats, or external tools are **not** authoritative unless their content is reflected here.
