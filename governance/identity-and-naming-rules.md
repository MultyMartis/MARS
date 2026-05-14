# MARS — Identity and naming rules (minimal discipline)

**Status:** **documented** — governance only. **Version:** v0 (Phase S2).

**Purpose:** Reduce **naming drift**, **semantic overload**, **registry illusion**, and **runtime confusion** without introducing a new identity product or code.

---

## 1. Entity classes (use the right word)

| Class | Meaning | Examples |
|-------|---------|----------|
| **Canonical system (external)** | A product or bot that **runs outside** MARS core and **owns** its graphs, credentials, and schedules | MetaBOT — SEO Content Agent (n8n-hosted) |
| **Adapter** | **In-repo** thin code (or doc stub) that **calls** an external entrypoint for demos/tests — **not** the external system itself | `mars-runtime/adapters/*-adapter.js` |
| **Bridge** | **Contract / translation** layer between MARS semantics and a concrete runner (concept or doc); may include payload shapes | Execution Bridge (concept); n8n bridge notes in project packs |
| **Runtime demo / R1** | Narrow experimental script path — **not** full MARS runtime | `mars-runtime/runtime/*` test flows |
| **External workflow** | A concrete graph or automation **in** n8n / SaaS — IDs are **native to that system** | Worker v13, Intake graph |
| **Governance entity** | A row or card in **Markdown registries** describing intended MARS-side roles or tools | `agents/registry.md`, `tools/registry.md` |

**Rule:** Do not call an **adapter** file the **system** name. Do not treat an **external workflow ID** as a **MARS governance entity id** unless a human maps it in documentation.

---

## 2. Minimal naming patterns

| Topic | Guideline |
|-------|-----------|
| **Agents** | Prefer **stable role names** matching `agents/registry.md`; avoid marketing nicknames in registry rows unless quoted in `display_name` |
| **Workflows** | MARS **contracts** use neutral names (`workflow-v0`); external engines use **their** names — prefix doc sections when ambiguous (`n8n: Worker`) |
| **Runtime adapters** | File name pattern `*-adapter.js`; describe **target system** in module header, not only “tool” |
| **Tools** | `tool_id` in governance is a **documentation key**; R1 JS keys may differ — state “demo key” when they diverge |
| **Projects** | Use **`project_id`** from `registry/project-registry.md`; legacy packs get **`legacy`** in registry narrative, not silent reuse of the same display title as the new pack |
| **Website Factory** | Prefer **`mars-website-factory`** and pack terms (*site type*, *block*, *blueprint*) — do not label Factory docs as “MARS runtime registry” |
| **Bridges** | Use **Bridge** for handoff semantics; reserve **Adapter** for code modules that perform I/O |
| **Experimental implementations** | Label docs and commits **experimental** / **R1**; avoid “production registry” language |
| **Governance docs** | File names use **kebab-case**; titles state **status** (**documented**, **planned**) where ambiguity would imply shipped code |

---

## 3. GOOD vs BAD naming (examples)

| BAD | Why | GOOD |
|-----|-----|------|
| “The SEO tool in MARS” | Collapses MetaBOT + adapter + governance tool row | “MetaBOT — SEO Content Agent (external)” **or** “`seo-content-agent-adapter` (R1 demo)” **or** “`tools/registry.md` row `…` (planned)” |
| “Registry says it’s live” | **Registry illusion** — a row describes intent, not uptime | “Row status `active` means **documentation pack** maintained; execution is **external**” |
| “n8n id `abc` is the canonical agent” | Wrong layer — graph id ≠ MARS agent | “n8n workflow id `abc` (external); MARS agent role `SeoValidator` (governance)” |
| “Website Factory registry is the runtime” | Conflates **doc registries** with **execution** | “Website Factory **block registry v0** (documented); **not** a running service” |

---

## 4. MetaBOT vs legacy pack (short)

- **`projects/metabot-seo-content-agent/`** — canonical **in-repo documentation** for the **external** MetaBOT system.  
- **`projects/seo-content-agent/`** — **legacy** early spec; **do not** extend; new work goes to the MetaBOT pack or governance.

---

## 5. SAFE UNKNOWN

- Exact display strings for public marketing vs internal registry until both are aligned in a deliberate edit.

---

*This document does **not** define a runtime identity service, UUID issuance, or automated naming enforcement.*
