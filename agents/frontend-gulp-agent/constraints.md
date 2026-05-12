# Constraints — Gulp Frontend Agent pack

Normative guardrails for anyone operating under this pack (human or Cursor).

| Constraint | Rationale |
|------------|-----------|
| **No `git add .`** | Prevents accidental staging of secrets, `dist/`, or unrelated files. Stage paths explicitly. |
| **No silent commits** | Every commit must be intentional, described, and aligned with project policy. |
| **No silent push** | Push only when explicitly requested and verified. |
| **No unrelated refactors** | Stay within the prompt’s `scope.in`; do not “clean up” neighboring modules. |
| **No framework replacement** | Do not introduce React/Vue/Svelte/etc. unless `target_stack` and governance allow a **STRUCTURE CHANGE**. |
| **No `dist/` edits** | Generated output is reproducible from source only. |
| **No CMS assumptions** | No WordPress/headless wiring unless **`integration_notes`** documents a real integration. |
| **No fake build success** | If the build was not run, say so; if it failed, report failure and partial state. |
| **No fake QA pass** | QA results must reflect checks actually performed. |
| **No asset invention** | Do not fabricate image/font URLs; use handoff paths or **SAFE UNKNOWN**. |
| **No design guessing** | If copy, spacing, or breakpoint intent is missing, mark **SAFE UNKNOWN** — do not invent brand-critical details. |

---

## Alignment

- Repository-wide honesty: [`../../AGENTS.md`](../../AGENTS.md)
- Cursor execution: [`../../projects/mars-website-factory/cursor-execution-standard-v0.md`](../../projects/mars-website-factory/cursor-execution-standard-v0.md)
- SAFE UNKNOWN prompts: [`../../projects/mars-website-factory/safe-unknown-prompt-rules-v0.md`](../../projects/mars-website-factory/safe-unknown-prompt-rules-v0.md)
