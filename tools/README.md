# `tools/` — Operational helpers index (lightweight)

**Purpose:** Human-facing **index** of **experimental / pilot** operational helpers under `tools/`. This folder also holds **Tool Layer v0 design contracts** (markdown only); see [Related: Tool Layer v0](#related-tool-layer-v0-design-contracts) below.

**Critical scope statement:** The path `tools/` is **not** a MARS runtime platform, **not** a control plane, **not** orchestration, **not** governance enforcement, and **not** evidence of shipped operational automation. Executable scripts here are **local, explicit-invocation** aids unless a **separate** document proves otherwise.

---

## Operational helper pilots

| Pilot | Path | Purpose | Status | Maturity (S6) | Posture |
|-------|------|---------|--------|---------------|---------|
| **PILOT 01** — Governance phrase scan | [`governance-scanner/`](governance-scanner/README.md) | Read-only substring hints on `.md` for drift-oriented triage | Experimental | Locally executable; human interpretation required | Manual; hints only |
| **PILOT 03** — Markdown link hints | [`markdown-link-validator/`](markdown-link-validator/README.md) | Read-only relative local link / optional anchor hints | Experimental | Locally executable; human interpretation required | Manual; hints only |

**Limitations (shared):** No negation or quote awareness; governance **definitions** of sensitive phrases can produce noise; output is **not** verdict, **not** SoT mutation, **not** CI gate unless you **separately** decide that in human process.

**PILOT 03 specifics:** Link and reference-line parsing are heuristic; anchor slugs do not match all renderers; absolute-path and site-root links are largely skipped by design — [markdown-link-validator/README.md](markdown-link-validator/README.md).

**Stabilization / lessons:** [helper-maturity-review.md](helper-maturity-review.md) · [helper-lessons-learned.md](helper-lessons-learned.md) · [helper-stabilization-rules.md](helper-stabilization-rules.md)

---

## Governance cross-references (S5–S7)

- [operational-experiments-overview.md](../governance/operational-experiments-overview.md) — S7 narrow pilots framing  
- [controlled-operationalization.md](../governance/controlled-operationalization.md) — S6 controlled helper evolution  
- [tooling-escalation-warnings.md](../governance/tooling-escalation-warnings.md) — S5 drift signals (pseudo-runtime, hidden automation)  
- [operationalization-maturity-levels.md](../governance/operationalization-maturity-levels.md) — S6 maturity vocabulary  
- [experimental-tooling-status.md](../governance/experimental-tooling-status.md) — experimental vs runtime capability honesty  

---

## Related: Tool Layer v0 (design contracts)

Markdown describing **planned** tool semantics, registry rows, and safety envelopes — **architecture / documentation** aligned with Web-GPT sources; **does not** assert an in-repo tool runtime. See [AGENTS.md](../AGENTS.md).

| File | Role |
|------|------|
| [registry.md](registry.md) | Tool registry row schema, lifecycle, planned examples |
| [tool-contract-v0.md](tool-contract-v0.md) | Invocation envelope, signals, failure model |
| [tool-execution-model-v0.md](tool-execution-model-v0.md) | Bridge mapping narrative (design) |
| [tool-safety-model-v0.md](tool-safety-model-v0.md) | Risk levels, approval alignment (design) |
| [tool-agent-binding-v0.md](tool-agent-binding-v0.md), [tool-workflow-integration-v0.md](tool-workflow-integration-v0.md), [tool-permission-enforcement-v0.md](tool-permission-enforcement-v0.md), [tool-validation-rules-v0.md](tool-validation-rules-v0.md) | Stage 9.5 integration narrative (documentation) |

**Build map:** [governance/master-build-map.md](../governance/master-build-map.md).
