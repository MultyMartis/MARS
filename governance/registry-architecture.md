# MARS — Registry architecture overview

**Status:** **documented** — governance clarification only. **Version:** v0 (Phase S2).

**Purpose:** Name the **different kinds** of “registry” in and around MARS so teams do not collapse them into one imaginary system.

---

## 1. Core rule (non-negotiable)

**Registry presence ≠ runtime existence.**  
A Markdown table, JSON export, or JavaScript lookup object in this repo is **evidence of documentation or local experiment**, not proof of a deployed registry service, enforced identity plane, or automated synchronization across systems.

---

## 2. Registry kinds (separate meanings)

| Kind | Typical location / examples | Canonical for what? | Nature |
|------|------------------------------|---------------------|--------|
| **Governance registries** | `agents/registry.md`, `tools/registry.md`, `registry/project-registry.md`, governance tables | **In-repo design vocabulary** and **contract posture** for the topics they claim (agents, tools, projects, etc.) | **Human-maintained**; normative **for documentation** unless a row explicitly defers to another file |
| **Operational registries** | Live admin UIs, SaaS configuration, n8n workflow libraries **outside** this repo | **That external system’s** execution and configuration | **External-only** for MARS; may be **referenced** or **sanitized** in docs — not auto-canonical for MARS semantics |
| **Experimental runtime registries** | e.g. `mars-runtime/runtime/tool-registry.js` (R1 demos) | **Nothing** governance-canonical | **Contextual / experimental** — convenience keys for scripts; see [runtime-registry-boundaries.md](runtime-registry-boundaries.md) |
| **External systems** | n8n graphs, Telegram bot config, cloud dashboards | **Their own** identities and schedules | **External-only**; authoritative for **their** runtime, not for MARS contract rows unless explicitly bridged and **human**-documented |
| **Documentation catalogs** | Long-form pack indexes (e.g. Website Factory pack tables, capability map) | **Navigation and scope** within that doc set | **Contextual** — authoritative **as catalogs of those docs**, not as substitute execution registries |
| **Lifecycle / event registries** | `logs/lifecycle-log.md` (append-only events) | **Key Event History** — what was recorded as a governance event; optional **Lifecycle Tracking Mode** for long ops | **Event log**, not implementation truth — distinct from `logs/cleanup/` and `logs/releases/` — see [registry-source-of-truth.md](registry-source-of-truth.md), [../logs/cleanup/actions/lifecycle-alignment-v1.md](../logs/cleanup/actions/lifecycle-alignment-v1.md) |
| **GitGuard (cross-cutting)** | `projects/mars-survivability/registries/gitguard-system-entry-v1.md` | **REGISTERED** Repository Survivability Layer — **not** a `project_id` row | Human-operated advisory; see [../registry/project-registry.md](../registry/project-registry.md) |
| **Website Factory structures** | `projects/mars-website-factory/` registries and contracts (site types, blocks, workflows v0, …) | **Planned / documented** website-production semantics **inside that program** | **Documented architecture** for the Factory program; **not** MARS core runtime; **not** evidence of automation |
| **Continuity / IdeaBox** | `continuity/**` (templates, protocols, optional manual index `continuity/registry/master-index.md`) | **Human-written** markdown notes for operational continuity within the repo | **Documentation catalog + discipline only** — markdown files are SoT; index is **navigation**, not a sync’d registry service; **not** runtime, **not** autonomous memory |

---

## 3. Canonical vs contextual vs experimental vs external-only

| Label | Meaning here |
|-------|----------------|
| **Canonical (governance)** | The designated Markdown (or stated contract file) for a **named concern** in-repo — e.g. `registry/project-registry.md` for **project_id** rows as defined there |
| **Canonical (external)** | The **live system** that actually runs the workload (e.g. n8n for MetaBOT graphs) — **authoritative for execution**, **not** automatically mirrored into MARS rows |
| **Contextual** | True **within** a pack or doc set (catalog index, tutorial table); must not silently override governance tables without an explicit human edit and cross-link |
| **Experimental** | R1 / demo lookups and adapters — **test and illustration** only |
| **External-only** | No MARS row “creates” ownership of that system; integration notes **describe** boundaries |

---

## 4. Cross-references

- [runtime-registry-boundaries.md](runtime-registry-boundaries.md) — three-way split (governance vs R1 vs external)  
- [registry-source-of-truth.md](registry-source-of-truth.md) — precedence and conflicts  
- [identity-and-naming-rules.md](identity-and-naming-rules.md) — naming to reduce overload  
- [registry-entry-minimal-standard.md](registry-entry-minimal-standard.md) — lightweight row shape for human registries  
- [external-system-boundaries.md](external-system-boundaries.md) — MetaBOT vs adapter vs MARS ownership  

---

*This file introduces **no** runtime service, **no** synchronization, and **no** automated enforcement.*
