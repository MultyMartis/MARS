# MARS — Agent Builder contract (v0, planned)

**Status:** planned — specification for the **Agent Builder** role when operating inside the **Agent Factory** (see `agent-factory-v0.md`). No implementation, no API, and no builder binary in this directory.

**Version:** v0.

**Legacy:** **Factory Engineer** (imported / documented) maps to **Agent Builder** as the governed successor name; this file does not port legacy code.

---

## 1. Purpose

**Agent Builder** is the named registry role that **authors or revises agent card content** under Factory rules. It produces **proposals**; it does **not** alone activate agents or set **active** status without governance and, for non-trivial risk, **Validator Agent** (legacy **FlyCheck**) review (see §4 and §7).

---

## 2. Inputs (v0, logical)

| Input | Description |
|-------|-------------|
| **request** | New agent, or update to a named agent; may come from a **Workflow** gap (`required_agents` missing), operator initiative, or a **Control Plane** handoff (documented). |
| **context** | Task / objective or product rationale; may link to `../workflows/task-contract-v0.md` when applicable. |
| **policy envelope** | What may be proposed (data scopes, allowed tool classes, forbidden egress). Sourced from **Security** in the target design, not invented by the Builder alone. |
| **current registry view** | Read-only snapshot of existing cards to avoid duplication and naming collisions (`registry.md`). |
| **SAFE UNKNOWN triggers** | If any mandatory input is absent or ambiguous, the outcome is **SAFE UNKNOWN** (see `agent-factory-v0.md` outcomes), not a silent fill. |

---

## 3. Outputs (v0, logical)

| Output | Description |
|--------|-------------|
| **Proposal — new card** | Full agent card per `agent-card-template.md`; default status **planned** or **draft**; not **active** without proof of implementation and governance (`registry.md`). |
| **Proposal — update** | Revised card with changelog entry; same name unless renames are a separate migration (out of v0). |
| **Rejection rationale** | Why no card (duplicate, unsafe scope, policy block). |
| **Flags for Validator** | What the FlyCheck-successor **Validator Agent** must check (see §4); not a bypass of validation for high-risk definitions. |

**NEED HUMAN APPROVAL** is emitted or recorded when §6 applies.

---

## 4. Required checks before creating or updating an agent (v0)

1. **Uniqueness** of `name` in the catalog, or a documented rename plan.  
2. **No** contradiction between **responsibilities** and **non-responsibilities**; no “god agent” without HITL and product sign-off.  
3. **Permissions** review (§5): data, model classes, external calls — must align with the policy envelope.  
4. **Tool** access review (§6): every tool id or pattern is justified; least privilege where possible.  
5. **Validation** requirements (§7): acceptance for the **card** itself (e.g. test plan for a future implementation, HITL checklists).  
6. **Validator Agent** (legacy **FlyCheck**): for any **risky** definition — broad tools, PII adjacency, untrusted code execution — must **validate before adoption**; rejection or conditions are valid outcomes.  
7. **Changelog** (§8): every material change to a proposed or accepted card is recorded.  

If checks cannot be completed: **SAFE UNKNOWN** or **reject**, not “assume OK”.

---

## 5. Required agent-card fields

Same as the v0 registry contract (`agent-card-template.md` / `registry.md` §3): **name**, **type**, **purpose**, **responsibilities**, **non-responsibilities**, **inputs**, **outputs**, **tools**, **permissions**, **limitations**, **workflow**, **validation**, **changelog** — all must be filled in a complete proposal, or the relevant subfield explicitly marked **SAFE UNKNOWN** (documentation level).

---

## 6. Permissions review (v0)

- The **permissions** field must list scopes (data, tenancy, environments) and what the agent may request of the **Control Plane** / **Tool** layer.  
- **NEED HUMAN APPROVAL** if broad or elevated access is proposed (what counts as “broad” = product/Security; if undefined, use **SAFE UNKNOWN**).  
- No card is adopted for production routing if permissions contradict **Security** (**SECURITY RISK** in workflow signals).  

---

## 7. Tool access review (v0)

- The **tools** field must enumerate or name each tool class or MCP capability (or “none”).  
- Rationale for any destructive, network, or data-writing tool.  
- **NEED HUMAN APPROVAL** for new external integrations or new tool chains on an update.  
- **Validator Agent** (FlyCheck role) flags dangerous combinations before adoption (see §4 and `agent-factory-v0.md` §8).  

---

## 8. Validation requirements (v0, for the definition)

- The **validation** field on the card: how a future runtime or org will verify the agent behaves (tests, evals, human sampling).  
- **Risky** agent definitions (§4): Validator sign-off or block.  
- Not a claim that code exists; if there is no test plan, use **SAFE UNKNOWN**.  

---

## 9. Changelog requirements (v0)

- The **changelog** field on the card must gain a row for each material proposed or accepted change: date (optional), author (optional), summary, and any notable risk/permission change.  
- Revisions that tighten permissions or remove tools are still changeloged.  
- Registry ingestion in implementation may add machine metadata; in v0 the source of truth is the human-readable template.  

---

## 10. Outcomes (cross-reference to Factory)

See `agent-factory-v0.md` §9: new card proposed, update proposed, reject, **SAFE UNKNOWN**, **NEED HUMAN APPROVAL**.  

---

## 11. Implementation honesty

- Do not mark **active** on any card unless implementation (or operations proof) in the repository (or a stated package) supports it; otherwise use **planned** or **draft**.  
- This file is not a runtime.  
