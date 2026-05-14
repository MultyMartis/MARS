# MARS — Adapter and bridge boundaries

**Status:** **documented** — governance-only, **Phase S5**. **Not** new integration design; **not** runtime product claims.

**Purpose:** Reduce confusion among **adapters**, **bridges**, **execution helpers**, **external workflow integrations**, and **runtime claims** — consistent with MetaBOT boundaries, execution boundaries, and registry rules.

---

## 1. Adapter

- An **adapter** **maps** interfaces, payloads, or file shapes between a **documented** MARS-facing surface and something else (external API, legacy pack, test harness).  
- **Adapter ≠ external system** — the external system **owns** its graphs, credentials, retries, and live truth — [external-system-boundaries.md](external-system-boundaries.md).  
- In-repo adapters under e.g. `mars-runtime/adapters/` are **experimental / narrow** unless separately proven; they **do not** dispatch MetaBOT — same doc §2.

---

## 2. Bridge

- A **bridge** is a **handoff** concept between **semantics** and a **concrete runner** — [execution-model.md](execution-model.md), [execution-boundary-clarification.md](execution-boundary-clarification.md).  
- **Bridge ≠ orchestration engine** — describing a bridge **does not** create a running service.  
- **Webhook utility** (one endpoint, one transform) **≠ autonomous workflow runtime** — n8n (or similar) remains the engine for hosted workflows unless explicitly stated otherwise with evidence.

---

## 3. Execution helper

- Informal term for **small** code that runs a **single** step (parse file, call one API in a demo).  
- Must stay **explainable** and **invoked explicitly**; if it grows multi-step scheduling or cross-system state, it crosses into **orchestrator** territory — [tooling-boundary-rules.md](tooling-boundary-rules.md).

---

## 4. External workflow integration

- **Integration** documents wires, IDs, and operator procedures between MARS docs and an **external** engine.  
- **Integration ≠ ownership** — live workflow truth stays **outside** unless copied into repo as **sanitized** artifacts with clear scope — [registry-source-of-truth.md](registry-source-of-truth.md).  
- External IDs **do not** auto-become canonical MARS entities — [external-system-boundaries.md](external-system-boundaries.md) §4.

---

## 5. Runtime claims

- **Code present** proves **files exist**, not “MARS runtime is operational as a product.” — [AGENTS.md](../AGENTS.md), [runtime-registry-boundaries.md](runtime-registry-boundaries.md).  
- **Registry rows** describe intent; they **do not** auto-enforce permissions repo-wide — [runtime-registry-boundaries.md](runtime-registry-boundaries.md) §2.

---

## 6. MetaBOT alignment

- **MetaBOT — SEO Content Agent** is an **external multi-workflow** system — [external-system-boundaries.md](external-system-boundaries.md).  
- MARS adapters **must not** be narrated as replacements for MetaBOT’s internal orchestration.

---

## 7. SAFE UNKNOWN

Undocumented one-off scripts that call external APIs without a cited contract or runbook: treat integration scope as **SAFE UNKNOWN** until mapped.
