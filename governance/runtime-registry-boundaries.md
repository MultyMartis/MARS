# Runtime vs governance registry boundaries

**Status:** **documented** — **governance clarification only**. **Version:** v0.

---

## 1. Three different “registries”

| Registry kind | Typical location | Role |
|---------------|------------------|------|
| **Governance / contract registries** | e.g. `tools/registry.md`, `agents/registry.md`, `registry/project-registry.md` | **Human-maintained** design vocabulary, rows, and **documentation** lifecycle. **Not** a running service unless separately evidenced. |
| **Runtime experimental registries** | e.g. `mars-runtime/runtime/tool-registry.js` | **Local demo / test** lookup objects for **R1** scripts. **Not** the MARS Tool Layer product; **not** canonical **`tool_id`** governance entries. |
| **External system catalogs** | e.g. live n8n graphs, SaaS admin, MCP server config | **Authoritative** for **that** system’s execution. MARS docs may **reference** them; they **do not** live in this repo unless explicitly imported (often **sanitized**). |

---

## 2. Rules that prevent “registry illusion”

1. **`tools/registry.md`** rows describe **intended** MARS tool semantics. They **do not** auto-populate from `mars-runtime/runtime/tool-registry.js`, and the reverse is **not** true.
2. **R1** `tool_id` / keys in experimental JS are **convenience identifiers** for adapters and tests. They are **not** proof that a tool is **`active`** in the governance registry or that permissions are **enforced** repo-wide.
3. **MetaBOT — SEO Content Agent** is an **external multi-workflow** system; it is **not** reducible to a single runtime tool row. See `projects/metabot-seo-content-agent/integration-boundary.md` §6–7.
4. **Runtime source code** (`mars-runtime/**/*.js`) is **evidence of experiments** only. **Governance markdown** + **`AGENTS.md`** remain the **documentation** **source of truth** for what MARS **claims** as implemented vs **planned**.

---

*Cross-ref: `governance/master-build-map.md` (Stage 9), `mars-runtime/README.md`, `tools/registry.md`.*
