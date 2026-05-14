# MARS — Operational helper classification

**Status:** **documented** — governance-only, **Phase S6**. **Not** a registry engine, **not** automated policy. Classifications support **human** triage.

**Purpose:** Lightweight **classes** of operational helpers: purpose, acceptable scope, danger zones, and **runtime-risk level** (semantic only—**not** a scored product).

**Alignment:** [tooling-boundary-rules.md](tooling-boundary-rules.md), [tooling-escalation-warnings.md](tooling-escalation-warnings.md), [execution-boundary-clarification.md](execution-boundary-clarification.md).

---

## 1. Runtime-risk level (vocabulary)

| Level | Meaning |
|-------|---------|
| **Low** | Read-only or report-only; no standing credentials; obvious I/O; easy to audit in one sitting. |
| **Medium** | Writes **scoped** files or generates artifacts under explicit flags; may call external APIs for **narrow** demos—human must own secrets and review output. |
| **High** | Cross-lane writes, registry mutation, migration-like bulk edits, or chains that **could** resemble orchestration if grown—requires strict scope docs and operator verification each time. |

**Risk level ≠ permission to bypass governance.** High-risk helpers demand **more** documentation and **narrower** default use—not “automation approval.”

---

## 2. Classes

### Formatter

| | |
|--|--|
| **Purpose** | Normalize text/markdown/JSON snippets for paste, diff, or review. |
| **Acceptable scope** | stdin/stdout or explicit paths; deterministic transforms. |
| **Danger zones** | Stripping audit trails, auto-rewriting governance meaning, “fixing” legal/security text without human read. |
| **Runtime-risk** | Low (raises to **Medium** if it writes without dry-run). |

### Validator

| | |
|--|--|
| **Purpose** | Check invariants, links, forbidden phrases, envelope shape hints—**read-only** triage. |
| **Acceptable scope** | Emit human-readable report; exit codes as **hints** only. |
| **Danger zones** | Claiming “validated = shipped,” silent auto-fix, CI coupling without honest labeling—[validation-chain-semantics.md](validation-chain-semantics.md). |
| **Runtime-risk** | Low. |

### Exporter

| | |
|--|--|
| **Purpose** | Produce CSV/JSON/markdown lists from repo content for review or handoff. |
| **Acceptable scope** | Explicit inputs; outputs to operator-chosen location. |
| **Danger zones** | Exporting secrets, PII, or huge dumps that obscure review; implicit “publish.” |
| **Runtime-risk** | Low–Medium. |

### Scanner

| | |
|--|--|
| **Purpose** | Inventory or grep-style passes; dependency/phrase scans. |
| **Acceptable scope** | Read-only tree walks; summarized output. |
| **Danger zones** | Acting on findings without human triage; “auto-delete unused.” |
| **Runtime-risk** | Low. |

### Mapper

| | |
|--|--|
| **Purpose** | Translate between **documented** shapes (e.g. field rename tables, doc→checklist). |
| **Acceptable scope** | Pure transform or side-by-side diff output. |
| **Danger zones** | Silent semantic loss; mapping **to** external IDs as if canonical—[external-system-boundaries.md](external-system-boundaries.md). |
| **Runtime-risk** | Low–Medium. |

### Adapter

| | |
|--|--|
| **Purpose** | Narrow I/O or API shape mapping toward a MARS-facing surface or demo. |
| **Acceptable scope** | Single responsibility; labeled experimental when appropriate—[experimental-tooling-status.md](experimental-tooling-status.md). |
| **Danger zones** | Adapter presented as “the system”; hidden retries; credential vending—[adapter-and-bridge-boundaries.md](adapter-and-bridge-boundaries.md). |
| **Runtime-risk** | Medium–High. |

### Bridge helper

| | |
|--|--|
| **Purpose** | Assist a **documented** handoff between semantics and a concrete runner (e.g. packaging a payload for human paste). |
| **Acceptable scope** | Explicit invocation; logs/artifacts visible to operator. |
| **Danger zones** | Bridge helper **described** as always-on **service**; silent cross-system chains—[execution-boundary-clarification.md](execution-boundary-clarification.md). |
| **Runtime-risk** | Medium–High. |

### Inventory helper

| | |
|--|--|
| **Purpose** | List registry rows, paths, or artifacts for human reconciliation. |
| **Acceptable scope** | Read-mostly; optional markdown table for review. |
| **Danger zones** | Auto-editing registries or lifecycle logs as “sync.” |
| **Runtime-risk** | Low (Medium if writes). |

### Report helper

| | |
|--|--|
| **Purpose** | Assemble REPORT sections, checklists, or diff summaries—operator edits narrative. |
| **Acceptable scope** | Suggestions only; includes UNKNOWN placeholders where needed. |
| **Danger zones** | Auto-filling **SAFE UNKNOWN** or security attestations—[tooling-boundary-rules.md](tooling-boundary-rules.md). |
| **Runtime-risk** | Low. |

### Migration helper

| | |
|--|--|
| **Purpose** | Scripted bulk moves/renames with dry-run and explicit file list—**human-gated**. |
| **Acceptable scope** | Idempotent plans; small batches; documented rollback notes. |
| **Danger zones** | Cross-lane refactors, unstoppable loops, ownership transfer without chat scope—[tooling-escalation-warnings.md](tooling-escalation-warnings.md). |
| **Runtime-risk** | High. |

---

## 3. Cross-references

- Drift signals: [operationalization-drift-warnings.md](operationalization-drift-warnings.md).  
- Interop: [interoperability-semantics.md](interoperability-semantics.md).  
- Maturity: [operationalization-maturity-levels.md](operationalization-maturity-levels.md).

---

## 4. SAFE UNKNOWN

Unlisted scripts are **SAFE UNKNOWN** by class until a human maps them to this table and records scope.
