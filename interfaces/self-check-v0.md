# MARS — Self-Check v0

**Status:** **documented** — **specification only** (no code, no config). **Self-Check** is a fast **consistency** check for a **single** [entity type](governance/universal-entity-operations.md#2-supported-entity-types-normative) before **Self-Audit** or **migration** work.

**Version:** v0. Revises with [universal-entity-operations.md](governance/universal-entity-operations.md).

---

## 1. Purpose

- Verify that a **target entity** (system, subsystem, agent, workflow, tool, project, integration, storage, or model) has the **minimum** documentation and registry coverage required for truthful **Self-Describe** and governance, per [universal-entity-operations.md](governance/universal-entity-operations.md).
- Fail fast on **missing** passports, invalid status, or **dishonest** implementation claims (per [AGENTS.md](AGENTS.md)).
- Complement, not replace, [introspection-v0.md](introspection-v0.md): **Self-Check** is a **gate** result; **Self-Describe** is narration from **bound** sources of truth.

---

## 2. When to run

- Before **publishing** or **re-baselining** an entity.
- As a **pre-step** to [self-audit-v0.md](self-audit-v0.md) or **SELF MIGRATE** in the [universal operations](governance/universal-entity-operations.md#4-universal-operations-normative) model.
- After **registry** or **passport**-shaped edits to an **agent** card, **project** row, or **subsystem** document.

---

## 3. Normative checks (v0)

| # | Check | Pass criterion |
|---|--------|----------------|
| 1 | Passport exists | A **passport-like** artifact (or [agent card](agents/agent-card-template.md) equivalent per [governance/README.md](governance/README.md)) exists and contains identity (`entity_id` or stable name), type, and scope; in-repo links resolve where the repository is the SoT. |
| 2 | Registry entry exists | A **row** in the **applicable** registry (e.g. [agents/registry.md](agents/registry.md), [registry/project-registry.md](registry/project-registry.md), or another **governance-recognized** list) **references** the same identity as the passport. |
| 3 | Status is valid | Status is one of the **allowed** values for that entity class (see [governance/state-model.md](governance/state-model.md) and relevant registry columns). Unlisted or invalid values → **FAIL**. |
| 4 | **owner_layer** exists | An **owner**, **steward**, or **governance layer** is named (e.g. Control Plane ownership, subsystem lead, or document-declared owner). **TBD** is allowed only if explicitly marked; default outcome **NEED REVIEW** until resolved. |
| 5 | Related docs exist | **Minimum** pointers to source-of-truth documents (contracts, workflow refs, integration notes) **resolve in-repo**. Broken or missing **required** links → **FAIL**; optional depth missing → **NEED REVIEW** at author discretion. |
| 6 | No false implementation claim | Passport, registry, and related docs **must not** state that runtime, RAG, **live** integrations, or **shipped** adapters **exist** without in-repo **evidence** (per [AGENTS.md](AGENTS.md)). Violation → **FAIL**; recommended fix: re-label as **documented** / **planned** only. |

**Gaps:** If a check does not apply to an entity class, record the reason under **issues**; default **NEED REVIEW** unless governance **explicitly** waives the facet.

---

## 4. Output (normative)

A **Self-Check** v0 result **must** include:

| Field | Content |
|-------|---------|
| **verdict** | **PASS** — all applicable checks pass. **FAIL** — at least one **hard** failure (e.g. false implementation claim or missing passport). **NEED REVIEW** — ambiguity, missing optional documentation, TBD **owner_layer**, or incomplete **SAFE UNKNOWN** labelling. |
| **issues** | Ordered list of findings with check **#** reference. |
| **recommended_fix** | Concrete next steps (e.g. *Add a row to project-registry for &lt;id&gt;.*, *Set status to documented.*, *Add **SAFE UNKNOWN** for live model endpoint.*). |

**Downstream:** **NEED REVIEW** **should** block treating the entity as **fully** governed until resolved or an **explicit** governance **waiver** is recorded.

---

## 5. Relation to Self-Describe

- **SELF DESCRIBE** (including **ENTITY** and **PROJECT** [modes](self-describe-modes.md)) can read the same SoT but does not assign pass/fail. **Self-Check** is the correct gate when a **boolean** result is required (e.g. pre-audit).
- If the user asks whether an entity is *OK* and **Self-Check** was not run, **Introspection** output may note that the entity is **not verified** by **Self-Check** v0 (design guidance; not a **shipped** string in a spec-only repo).

---

*Last updated: Self-Check v0 (entity-level quick consistency; documentation only).*

**System signals (vs Self-Check verdicts):** Verdicts **PASS** / **FAIL** / **NEED REVIEW** are **local** to this spec. **MARS** **canonical** **system** **signal** **names** (**UNKNOWN**, **SAFE UNKNOWN**, **GIT CHECKPOINT NEEDED**, **NO GIT CHECKPOINT**, …) are defined in [governance/system-signals-dictionary.md](governance/system-signals-dictionary.md); do **not** conflate with **NEED HUMAN APPROVAL** or **HITL** without reading that dictionary.
