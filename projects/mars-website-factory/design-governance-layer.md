# MARS Website Factory — Design Governance Layer

**Status:** **documented** — governance architecture only. **Not** frontend implementation, **not** design generation, **not** runtime orchestration, **not** autonomous agents.

**Purpose:** Formalize the **boundary between approved design and frontend production**: how human-supervised workflows turn pixels/exports plus intent into **machine-readable implementation law** that reduces semantic drift, version contamination, and silent invention.

---

## 1. Problem the layer addresses

Forge-style frontend validation surfaced failure modes when **PNG/Figma exports alone** were treated as sufficient authority:

| Risk | Symptom |
|------|---------|
| **Semantic drift** | DOM or component choices that “look fine” but change meaning, hierarchy, or conversion story. |
| **V1/V2 contamination** | Assets, copy, or section order from archived generations leak into the active build. |
| **Visual flow ≠ semantic flow** | Reading order, heading levels, or CTA roles diverge from approved structure. |
| **Entity-count mutation** | Cards, reviews, logos, bullets added/removed vs approved content model. |
| **Invented copy** | Placeholder text promoted to “final” without content authority. |
| **Archive as authority** | Old folders or mockups interpreted as current without an explicit freeze. |

The **Design Governance Layer** inserts a **document-first, versioned artifact** — the **Canonical Design Implementation Pack** — so frontend agents bind to **explicit semantics and constraints**, not only to raster or canvas state.

---

## 2. Position in the factory

```text
Approved blueprint ──► Design execution (visuals, exports)
                              │
                              ▼
              ┌───────────────────────────────────┐
              │ Design Governance Layer (human)   │
              │ Canonical Design Implementation   │
              │ Pack (versioned, machine-readable)│
              └───────────────────────────────────┘
                              │
                              ▼
        Frontend Handoff Contract v0 ──► Gulp Frontend Agent / Forge (doc packs)
```

- **Upstream:** [Design Handoff Contract v0](design-handoff-contract-v0.md), design exports, blueprint and block registry.
- **Peer:** [Agent input contracts](../../governance/agent-input-contracts.md) — each role declares required/forbidden inputs and SAFE UNKNOWN behavior.
- **Downstream:** [Frontend Handoff Contract v0](frontend-handoff-contract-v0.md), [frontend-production-rules-v0.md](frontend-production-rules-v0.md), specialist packs under `agents/frontend-gulp-agent/`, `agents/mars-forge/`.
- **Visual intent (peer):** [Visual Reconciliation Layer v0](visual-reconciliation-layer.md) — human-supervised reading of hierarchy/emphasis after semantic discipline; **not** automated visual QA.

Normative structure and artifact names: **[Canonical Design Implementation Pack architecture](canonical-implementation-pack-architecture.md)**.

Role that **authors/maintains** the pack under human review: **[Design Governance Agent](../../agents/design-governance-agent.md)** (`design_governance_agent` in [agents/registry.md](../../agents/registry.md) §4.1 when listed).

---

## 3. What the layer is and is not

| The layer **is** | The layer **is not** |
|------------------|---------------------|
| Versioned **governance** artifacts (Markdown-first; optional future structured formats per project policy). | A running service, queue, or orchestration engine. |
| **Semantic** and **implementation** rules frontend work must respect. | The frontend codebase or build pipeline. |
| **Validation** checklists and quarantine semantics for freeze. | Automatic enforcement unless humans/tools explicitly adopt checklists. |
| **SAFE UNKNOWN**–friendly: gaps stop “confident guessing.” | A substitute for [HITL](hitl-prompt-boundary-v0.md) where policy requires human approval. |

---

## 4. Canonical vs archive vs shared assets (summary)

| Concept | Meaning |
|---------|---------|
| **Active design version** | One **`design/vN/`** tree (or project-agreed equivalent) referenced by freeze notes and frontend handoff. **Only** this version’s **`semantics/`**, **`implementation-pack/`**, **`exports/`**, and **`validation/`** are canonical for implementation. |
| **Archive** | Older **`v*`** folders or tagged snapshots — **historical reference only**. Must not drive implementation unless explicitly re-activated via governance (version bump + HITL). |
| **`shared-assets/`** | Cross-version **physical** assets (e.g. licensed logo masters, font files). **Not** semantic truth: semantics live per version under **`semantics/`**. |

Full rules: [canonical-implementation-pack-architecture.md §5–6](canonical-implementation-pack-architecture.md).

---

## 5. Relation to semantic source lock (Forge)

Where [MARS Forge semantic source lock](../../agents/mars-forge/semantic-source-lock.md) is used, the **Canonical Design Implementation Pack** is the **natural home** for frozen **section order**, **content authority**, and **forbidden rewrites** aligned to a single **`design/vN/`**. Forge and the pack are **documentation patterns**; neither implies automatic enforcement in-repo.

---

## 6. SAFE UNKNOWN (layer-level)

- Whether every project **must** produce a full pack before first frontend line — **project policy**; default recommendation: **pack present or explicit gap list** in `SAFE_UNKNOWN_notes` on [Frontend Handoff Contract v0](frontend-handoff-contract-v0.md).
- Machine-readable schemas (JSON/YAML) for packs — **optional future**; v0 is **Markdown-first** for human auditability.
- Tooling that diffs pack vs `dist` — **not** claimed by MARS core.

---

## 7. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-16 | Initial Design Governance Layer overview. |
| v0.1 | 2026-05-16 | Cross-link to Visual Reconciliation Layer (peer methodology). |
