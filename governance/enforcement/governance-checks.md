# Governance check catalog (human review)

**Status:** **documented** — **manual** review aids. **No** implied CI, **no** autonomous scanning, **no** runtime hooks.

Each check: **ID**, **purpose**, **detection logic** (how a human or a *future optional* script might notice it), **severity**, **human action**.

---

## GC-RUNTIME-CLAIM-001 — Runtime claim drift

| Field | Content |
|--------|---------|
| **Purpose** | Prevent text that asserts **full MARS runtime**, **control plane implementation**, or **repo-wide enforcement** without file-level evidence. |
| **Detection logic** | Search markdown for absolute claims (“ships with”, “implements the control plane”, “enforces across the repo”) without pointers to specific source paths **or** without matching [AGENTS.md](../../AGENTS.md) three-way split; compare tone to [../../mars-runtime/README.md](../../mars-runtime/README.md) (R1 narrow scope). |
| **Severity** | **High** |
| **Human action** | Rewrite to **documented** / **planned** / **experimental R1** per evidence; add **SAFE UNKNOWN** if unsure. |

---

## GC-TERM-002 — Terminology drift

| Field | Content |
|--------|---------|
| **Purpose** | Keep **runtime**, **governance**, **orchestration**, **bridge**, **workflow**, **agent** aligned with [terminology-boundaries.md](terminology-boundaries.md) and [../execution-model.md](../execution-model.md). |
| **Detection logic** | Same word used for two layers in one doc (e.g. “registry” = both `agents/registry.md` and `mars-runtime/.../tool-registry.js` without distinction); new synonyms for “runtime” without definition. |
| **Severity** | **Medium** |
| **Human action** | Align wording; cross-link [../runtime-registry-boundaries.md](../runtime-registry-boundaries.md) when “registry” is ambiguous. |

---

## GC-DISCLAIMER-003 — Missing documentation disclaimers

| Field | Content |
|--------|---------|
| **Purpose** | Normative contracts should state **documentation vs implementation** posture where readers might assume code exists. |
| **Detection logic** | New or heavily edited `interfaces/`, `control-plane/`, `workflows/`, `security/` files lack a short **Status:** line or equivalent near the top; root-facing docs omit pointer to [AGENTS.md](../../AGENTS.md) when scope is ambiguous. |
| **Severity** | **Medium** |
| **Human action** | Add concise **Status:** **documented** / **planned** / **experimental** as appropriate; link master map or AGENTS. |

---

## GC-REGISTRY-004 — Registry inconsistency

| Field | Content |
|--------|---------|
| **Purpose** | Avoid **registry illusion**: governance rows vs R1 JS keys vs external catalogs treated as one SoT. |
| **Detection logic** | Doc cites a `tool_id` or agent name that does not appear in [../../agents/registry.md](../../agents/registry.md) / [../../tools/registry.md](../../tools/registry.md) (if claiming governance SoT); or equates `mars-runtime/**` lookup tables with product registry. |
| **Severity** | **High** |
| **Human action** | Fix references or label **SAFE UNKNOWN**; clarify which registry kind per [../runtime-registry-boundaries.md](../runtime-registry-boundaries.md). |

---

## GC-PHASE-005 — Phase / status inconsistency

| Field | Content |
|--------|---------|
| **Purpose** | Stage labels in [../master-build-map.md](../master-build-map.md) and lifecycle entries stay coherent with root [../../README.md](../../README.md) phase statements. |
| **Detection logic** | “Stage X complete” in prose but stage table still `partial-docs`; lifecycle event claims not echoed in master map **What exists now** / status column. |
| **Severity** | **Medium** |
| **Human action** | Reconcile tables and prose; log material changes per master map maintenance rules. |

---

## GC-LANE-006 — Lane contamination

| Field | Content |
|--------|---------|
| **Purpose** | Keep **MARS core / governance** work separate from **production frontend** paths and chat scopes per [../parallel-cursor-chat-work-mode-v0.md](../parallel-cursor-chat-work-mode-v0.md). |
| **Detection logic** | Same change set mixes `governance/` or `interfaces/` edits with unrelated `projects/*/frontend*` or customer deploy assets without explicit charter; instructions blur “factory pilot” vs “MARS core repo hygiene.” |
| **Severity** | **Medium** |
| **Human action** | Split workstreams; document lane in task / REPORT; revert accidental path scope. |

---

## GC-SAFE-007 — Missing SAFE UNKNOWN handling

| Field | Content |
|--------|---------|
| **Purpose** | Unknowns must be explicit per [AGENTS.md](../../AGENTS.md), not papered over with confident defaults. |
| **Detection logic** | Spec contains “TBD”, “assumed”, “probably”, or silent gaps on security, data residency, or wire format without a **SAFE UNKNOWN** block or ticket pointer. |
| **Severity** | **Medium** |
| **Human action** | Add **SAFE UNKNOWN** with what would verify; or file follow-up in risk/register workflow if tracked. |

---

## GC-OPS-008 — Fake operational claims

| Field | Content |
|--------|---------|
| **Purpose** | Block language that implies **live** MARS operations center, **automated** verification of product behaviour, or **always-on** governance **execution**. |
| **Detection logic** | Phrases like “the system automatically”, “continuous enforcement”, “self-managing governance” in this repo’s docs; see [forbidden-runtime-claims.md](forbidden-runtime-claims.md). |
| **Severity** | **High** |
| **Human action** | Replace with human-run / editor-run / **planned** wording; cite [../execution-model.md](../execution-model.md). |

---

## GC-REPORT-009 — Missing REPORT discipline

| Field | Content |
|--------|---------|
| **Purpose** | Task closeouts that require reporting use the **`# REPORT — …`** heading and list changed files / summary / git status per [AGENTS.md](../../AGENTS.md). |
| **Detection logic** | User asked for REPORT format; agent response has no top-level `# REPORT —` or omits changed-files list when edits occurred. |
| **Severity** | **Low** (process) |
| **Human action** | Amend response or template; not a codebase linter concern unless team adopts checklists in runbooks. |

---

## GC-ARCH-010 — Architecture vs runtime confusion

| Field | Content |
|--------|---------|
| **Purpose** | Distinguish **documented architecture** (Web-GPT pack, governance) from **planned implementation** and **legacy imported** material. |
| **Detection logic** | Single paragraph cites `web-gpt-sources/` as “current implementation” or treats roadmap dates as completion guarantees. |
| **Severity** | **Medium** |
| **Human action** | Apply three-way split wording; point to [../../README.md](../../README.md) and [../master-build-map.md](../master-build-map.md). |

---

*IDs are stable handles for conversation and future optional tooling — **not** deployed checks today.*
