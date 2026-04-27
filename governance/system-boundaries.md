# MARS — System Boundaries (governance)

**Status:** **documented** — responsibility and containment model. Does **not** define APIs or network zones.

**Version:** v0.

---

## 1. Purpose

**System boundaries** make explicit **what is inside** the MARS **design and repository**, what lives **outside** (external systems), and where **responsibility** starts and ends. This reduces confusion between **documented architecture**, **planned implementation**, and **operational environments** (see `../AGENTS.md`).

---

## 2. Inside MARS (in scope of the MARS program / repo)

| Area | What “inside” means here |
|------|---------------------------|
| **Documentation & contracts** | Markdown specs for Control Plane, workflows, tasks, agents, layers (`workflows/`, `control-plane/`, `agents/`, `web-gpt-sources/`, `governance/`, etc.). |
| **Normative language** | Shared vocabulary: `../web-gpt-sources/01_system.md` terminology; signals in `../workflows/task-contract-v0.md`. |
| **Repository layout** | Folders for memory, security, tools, **planned** code areas (`mars-runtime/`, etc.) as **design placeholders**—**inside** the repo, but **code may be absent** in Phase 1. |
| **Governance** | This folder: capability/boundary/execution/state/versioning models, links to registries and roadmaps. |
| **Operational discipline (human)** | Human-in-the-loop, Git rules as **documented** (e.g. `../web-gpt-sources/04-workflows__git-rules.md`); behavior follows team process, not an automated MARS service today. |

**Not implied:** that every folder contains **running** software. **Honesty** per `../README.md` and `../AGENTS.md`.

---

## 3. Outside MARS (external systems)

These are **typically external** to a “MARS runtime in a box” (which is **not** claimed to exist in-repo):

| External class | Examples (non-exhaustive) | Why “outside” |
|----------------|---------------------------|----------------|
| **User interfaces** | Web-GPT UI, Cursor IDE, browsers | Host applications; not defined as part of a single MARS binary. |
| **Model providers** | LLM API vendors, on-prem inference if used | **Models** are consumed **through** agreed interfaces; provider contracts are vendor-side. |
| **Infrastructure** | Cloud accounts, k8s, DBaaS, secrets stores | **Deployment** and **data plane** for a future MARS; not specified as implemented here. |
| **Integration platforms** | n8n, Zapier-like systems, enterprise buses | **Future** execution bridges per `execution-model.md`. |
| **Identity / org** | IdPs, org directories | Unless/until MARS **implements** a dedicated authn/z service. |
| **Customer data** | User content in repos, tickets, wikis | **Owned** by the customer/operator; MARS design must respect residency and policy **at integration points**. |

**Boundary rule:** MARS **specifies** how to **relate** to some of these (e.g. Web-GPT ↔ Cursor in legacy pack); it does **not** own vendor SLAs or IDE internals.

---

## 4. Responsibility borders

| Locus | Owns | Does **not** own |
|-------|------|------------------|
| **MARS design (this repo)** | **Contracts**, terminology, **target** component responsibilities, **governance** rules for updating docs. | Production uptime, user machines, third-party TOS, cost of API calls. |
| **Control Plane (design)** | **Planned** orchestration: task state, routing, dispatch **when** implemented. | Physical execution of tools on a developer PC unless a future runtime **defines** that process. |
| **Agent layer (design)** | **Role** definitions, registry **as documentation**. | Guarantees that any **named** role exists as code in a given week. |
| **Operator / user** | Approvals, secrets, “run in Cursor” execution today, final **correctness** of changes to filesystem and Git. | Automated MARS **enforcement** without human review where policy demands HITL. |
| **Web-GPT (legacy product context)** | In imported docs: prompts, packaging, **Web-GPT** rules. | MARS **repo** file layout beyond what the team has copied. |

**Cross-boundary work:** “Execution Bridge” in `execution-model.md` is the **concept** for how **inside** (MARS task/workflow state) **connects** to **outside** (Cursor, n8n, future runtime).

---

## 5. Safe unknowns

- **Exact** network trust zones for a future MARS **deployment** — **not** fixed in this file.
- Whether “System Registry” is a **single** database or **distributed** config — **implementation TBD**; see mapping in `../web-gpt-sources/13_migration.md`.

---

## 6. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-04-27 | Initial system boundaries. |
