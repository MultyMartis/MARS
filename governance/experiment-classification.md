# MARS — Experiment classification

**Status:** **documented** — governance-only, **Phase S7**. **Not** a taxonomy engine, **not** automated labeling.

**Purpose:** Lightweight **experiment types** so operators can scope work, set evidence expectations, and see **risk** to governance vs runtime narratives—without implying orchestration or autonomous agents.

> **Note:** “Workflow” below means **documented or piloted human/external execution flow** (tasks, n8n, checklists)—**not** a MARS workflow engine product unless separately evidenced and honestly described per [AGENTS.md](../AGENTS.md).

---

## 1. Shared columns (all types)

| Column | Meaning |
|--------|---------|
| **Acceptable scope** | What the experiment may touch without becoming a platform claim. |
| **Evidence expectations** | Minimum artifacts operators should aim to capture—see [experiment-evidence-rules.md](experiment-evidence-rules.md). |
| **Runtime-risk** | Risk of **misread** as shipped runtime / daemon / orchestration (Low / Med / High). |
| **Governance-risk** | Risk of polluting SoT, terminology, or registry truth (Low / Med / High). |
| **Stabilization expectations** | What must happen **before** treating outcomes as pattern—[experiment-to-pattern-transition.md](experiment-to-pattern-transition.md). |

---

## 2. Types

### 2.1 Documentation experiment

| | |
|--|--|
| **Acceptable scope** | Restructure prose, add cross-links, pilot a new section in a **non-canonical** branch or draft file if repo practice allows; no executable authority. |
| **Evidence expectations** | Before/after outline, reader notes, link check results if applicable. |
| **Runtime-risk** | Low |
| **Governance-risk** | Med (terminology drift if merged carelessly) |
| **Stabilization expectations** | Human editorial pass; merge into canonical doc only after review—[documentation-entropy-rules.md](documentation-entropy-rules.md). |

### 2.2 Governance experiment

| | |
|--|--|
| **Acceptable scope** | Trial wording, table layouts, or cross-doc patterns inside `governance/**` with clear **experimental** framing in commit messages or adjacent notes—not silent SoT swaps. |
| **Evidence expectations** | Rationale, conflicts with prior docs listed, **SAFE UNKNOWN** called out. |
| **Runtime-risk** | Low |
| **Governance-risk** | High |
| **Stabilization expectations** | Explicit promotion: index updates, deprecation of superseded sections, operator sign-off—[registry-source-of-truth.md](registry-source-of-truth.md). |

### 2.3 Operational helper experiment

| | |
|--|--|
| **Acceptable scope** | New or changed script/utility under narrow invocation; fits [operational-helper-classification.md](operational-helper-classification.md). |
| **Evidence expectations** | Invocation command, inputs/outputs, failure modes, dependency notes. |
| **Runtime-risk** | Med |
| **Governance-risk** | Low–Med |
| **Stabilization expectations** | Repeatable runbook + boundary review against [tooling-boundary-rules.md](tooling-boundary-rules.md); no auto-promotion. |

### 2.4 Interoperability experiment

| | |
|--|--|
| **Acceptable scope** | Import/export/envelope handshake with **named** external system or bridge—[interoperability-semantics.md](interoperability-semantics.md). |
| **Evidence expectations** | Sample payload (redacted), manual steps, external prerequisites stated. |
| **Runtime-risk** | Med |
| **Governance-risk** | Med |
| **Stabilization expectations** | Documented contract + boundaries; no “MARS owns the external system” implication—[external-system-boundaries.md](external-system-boundaries.md). |

### 2.5 Runtime-scoped experiment

| | |
|--|--|
| **Acceptable scope** | Code paths explicitly scoped to demo/test trees; labeled per [artifact-lifecycle-rules.md](artifact-lifecycle-rules.md), [execution-boundary-clarification.md](execution-boundary-clarification.md). |
| **Evidence expectations** | Path list, how to run, what is **not** generalized to “MARS runtime.” |
| **Runtime-risk** | High |
| **Governance-risk** | Med–High |
| **Stabilization expectations** | Maturity honesty—[operationalization-maturity-levels.md](operationalization-maturity-levels.md); governance SoT unchanged unless separately reviewed. |

### 2.6 Validation experiment

| | |
|--|--|
| **Acceptable scope** | Try a checklist, manual validation chain, or read-only scan on a subset—[validation-chain-semantics.md](validation-chain-semantics.md). |
| **Evidence expectations** | What was validated, by whom, tool version, scope limits. |
| **Runtime-risk** | Low–Med |
| **Governance-risk** | Med (false “CI/automation exists” drift) |
| **Stabilization expectations** | Clear statement that validation mention ≠ automated product unless evidenced. |

### 2.7 Adapter experiment

| | |
|--|--|
| **Acceptable scope** | Narrow I/O mapping toward one surface—[adapter-and-bridge-boundaries.md](adapter-and-bridge-boundaries.md). |
| **Evidence expectations** | Sample request/response shapes, error handling notes, external IDs not conflated with MARS entities. |
| **Runtime-risk** | Med |
| **Governance-risk** | Med |
| **Stabilization expectations** | Registry/identity review if names appear in catalogs—[identity-and-naming-rules.md](identity-and-naming-rules.md). |

### 2.8 Workflow experiment

| | |
|--|--|
| **Acceptable scope** | Pilot ordering of human steps, external automation (e.g. n8n), or task contract wording—**no** claim of in-repo orchestration engine. |
| **Evidence expectations** | Diagram or step list, ownership of each step, where execution **actually** happens. |
| **Runtime-risk** | Med–High |
| **Governance-risk** | Med |
| **Stabilization expectations** | Execution boundary doc update if the pilot changes “where work runs” narrative—[execution-boundary-clarification.md](execution-boundary-clarification.md). |

### 2.9 Migration experiment

| | |
|--|--|
| **Acceptable scope** | Dry-run of moving artifacts, renaming paths, or reconciling legacy imports—human-operated. |
| **Evidence expectations** | Inventory diff, rollback plan, **SAFE UNKNOWN** for unmapped references. |
| **Runtime-risk** | Low–Med |
| **Governance-risk** | High |
| **Stabilization expectations** | Lifecycle log or REPORT-style closeout; canonical indices updated in one controlled pass—[context-continuity-rules.md](context-continuity-rules.md). |

---

## 3. SAFE UNKNOWN

If an activity spans multiple types, pick the **highest** governance-risk and **highest** runtime-risk expectations from the contributing types until scoped.
