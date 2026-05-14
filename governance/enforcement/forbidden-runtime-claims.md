# Forbidden runtime claims — review triggers

**Status:** **documented** — **governance review** cues, **not** an automated blocklist in CI.

When these patterns appear **without** strong evidence citations and [AGENTS.md](../../AGENTS.md)-aligned qualifiers, treat as **stop and rewrite**.

---

## 1. High-risk phrases (typical triggers)

Use judgment: context matters (e.g. quoting a legacy doc vs stating product fact).

| Pattern / phrase family | Why it triggers review |
|-------------------------|-------------------------|
| **Fully autonomous** (agents, runtime, factory) | Implies unsupervised **MARS core** execution; conflicts HITL-first posture. |
| **Production orchestrator** / **orchestrates production** | Implies shipped orchestration **in this repo**. |
| **Automatic agent coordination** | Implies multi-agent dispatch without human/editor gates. |
| **Self-managing runtime** / **self-healing production** (as factual now) | **Self-Heal** contracts are **plan-only** v0; “heals” in prod is a claim class. |
| **Enforces policy across the repository** | No repo-wide policy engine is asserted for MARS Phase 1. |
| **Always-on** / **24/7** MARS **core** | Operations language without evidence of such a service here. |
| **Single source of truth** (runtime) | Often erases split between governance markdown, R1 JS, and external systems — see [../runtime-registry-boundaries.md](../runtime-registry-boundaries.md). |
| **Implements the full control plane** | Implementation claim; needs path-level proof or downgrade to **planned** / **partial**. |
| **Daemon** / **worker pool** / **queue consumer** (**as shipped MARS**) | May be true for **external** systems; false trigger if clearly labeled **external** or **planned**. |
| **End-to-end verified by MARS** | “Operationally verified” in README = **human-controlled** work, not MARS automation ([../../README.md](../../README.md)). |

---

## 2. Medium-risk (qualify carefully)

| Pattern | Safe direction |
|---------|----------------|
| **Orchestration** | Prefer **documented** workflow/orchestration **contracts** vs **live** engine unless engine is named and evidenced. |
| **Registry sync** | State **manual** governance vs **experimental** JS vs **external** catalog. |
| **Runtime-ready** | Clarify **documentation runtime-readiness** (Stage 8.5) vs **product runtime shipped**. |
| **Validated** | Say **who** validated (human, editor, optional script) and **what scope**. |

---

## 3. Allowed wording (when accurate)

- **Documented**, **normative for documentation**, **contract v0**, **roadmap**, **planned implementation**, **experimental R1**, **narrow demo**, **human-in-the-loop**, **editor-executed**, **Web-GPT → Cursor** execution path ([../execution-model.md](../execution-model.md)).
- **May later**, **intended evolution**, **target shape**, **illustrative** — for forward-looking material.

---

## 4. Safe wording templates

- “This repository **primarily** contains **documentation**; **minimal experimental R1** code exists under `mars-runtime/` and does **not** constitute a full MARS runtime.”
- “**Governance** markdown is the honesty SoT for **claims**; **source files** are evidence of **what exists** in-tree.”
- “**SAFE UNKNOWN:** … (what would verify)”

---

## 5. Documentation-only wording

Use when describing design without implementation proof:

- “**As documented in** …”
- “**No in-repo implementation** of … unless paths …”
- “**Legacy imported** material; not current product truth without reconciliation.”

---

*Pair with [governance-checks.md](governance-checks.md) GC-RUNTIME-CLAIM-001 and GC-OPS-008.*
