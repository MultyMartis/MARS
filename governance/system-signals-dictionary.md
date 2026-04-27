# MARS — System Signals Dictionary v0

**Status:** **documented** — **normative vocabulary** for named **system signals** used across workflow, security, interfaces, and governance. **No** runtime emission, **no** parser, and **no** new subsystems are implied by this file.

**Version:** v0. Revisable per [versioning-model.md](versioning-model.md); **canonical spellings** in this file supersede informal use elsewhere when versions align.

**Scope:** This dictionary defines **what each signal means**, **when** it may appear in **documentation, contracts, and (future) orchestration state**, and **where** to look for related policy. It does **not** implement routing, storage, or UI.

---

## Authority and use

- **Single index:** New docs and future contracts should use **only** the **canonical** forms in §2 unless a scoped exception is explicitly recorded.
- **Cross-references:** Layer-specific docs (workflows, security, interfaces) **may** add nuance but **must not** split meanings without updating this dictionary or a formal addendum version.
- **Planned implementation:** A future **Control Plane** or **log** service may record these strings as an enumerated set; until code exists, humans and authors apply the vocabulary **consistently** per [AGENTS.md](../AGENTS.md).

---

## 2. Canonical signal definitions

### UNKNOWN

| Facet | Content |
|--------|---------|
| **Meaning** | A **required binding** is **missing** or **unresolvable** so the run (or the documented process) **cannot** honestly proceed with assumed facts — e.g. no agent in registry, no route target, no permission declaration, no mandatory input. |
| **When to emit** | **Prompt** / **task** with unresolved **required_agents**; **route** with no eligible capability; any step where **policy** demands a SoT and none is available. |
| **When NOT to emit** | For **bounded** uncertainty where proceeding with explicit limits is allowed — use **SAFE UNKNOWN** instead. For **policy-violation** or **injection** suspicion — use **SECURITY RISK**. |
| **Related layers** | **Workflow** (task binding), **Control Plane** (router), **Agent Registry**, **Security** (fail-closed), **governance** (evidence and SoT). |
| **Typical next action** | **Stop** or **park**; **resolve** registry, inputs, or permissions; optionally invoke **Agent Factory** only if product policy allows — never guess missing bindings. |

---

### SAFE UNKNOWN

| Facet | Content |
|--------|---------|
| **Meaning** | A **claim** or **slice of state** cannot be **verified** from in-repo evidence or a named external SoT; the system (or author) must **not** **fabricate** detail. Honest “we don’t know (and what would verify it).” |
| **When to emit** | **Plan** / **validate** when evidence is **partial**; **introspection** and **governance** outputs; **any** field or operational guarantee not provable from artifacts. |
| **When NOT to emit** | As a **blanket** substitute for **UNKNOWN** when a **hard** missing **binding** blocks the next step. As approval to **skip** **HITL** — it is **not** a waiver. |
| **Related layers** | **Security / Guardrails** (anti-fabrication), **Introspection**, **governance** ([universal-entity-operations.md](universal-entity-operations.md)), **Validation**. |
| **Typical next action** | **Label** the unknown slice; **collect** evidence; **narrow** scope; or **escalate** to **NEED HUMAN APPROVAL** if decisions are blocked. |

---

### NEED HUMAN APPROVAL

| Facet | Content |
|--------|---------|
| **Meaning** | A **human** must **approve** (or **reject**) before a **gated** effect, adoption of results, or continuation — per **HITL** policy, **risk level**, or **approval gate** class. |
| **When to emit** | **High**-risk plans; **gated** tools; **public** or **irreversible** **release**; any condition in [../security/approval-gates.md](../security/approval-gates.md) **v0** table. |
| **When NOT to emit** | For **missing** data alone — use **UNKNOWN**. For **unverified** but non-gating claims — **SAFE UNKNOWN** may suffice without a full **approval** cycle, per product policy. |
| **Related layers** | **Workflow** (**hitl_gates**), **Security** ([approval-gates.md](../security/approval-gates.md)), **Control Plane** (dispatch pause), **Task Contract**. |
| **Typical next action** | **Pause** automation; **obtain** explicit **human** decision; **log** (future) or document outcome; then **resume** or **abort**. |

---

### SECURITY RISK

| Facet | Content |
|--------|---------|
| **Meaning** | **Policy violation**, **suspected injection**, **scope escape**, or **dangerous** route — **automation** must **not** continue **unchallenged**; resolution is **not** only “ask later.” |
| **When to emit** | **Route** / **execute** denial or contradiction with **passport** / **permissions**; **validate** **failure** on **security** checks; confirmed or suspected **prompt injection** shaping. |
| **When NOT to emit** | For **benign** **unknowns** with no **policy** or **safety** angle (prefer **UNKNOWN** or **SAFE UNKNOWN**). For **organizational** “we need a git commit” (see **GIT CHECKPOINT NEEDED** / **NO GIT CHECKPOINT**). |
| **Related layers** | **Security / Guardrails**, **Control Plane** (router), **Validator**, **Tool** layer (future), **Workflow**. |
| **Typical next action** | **Block** or **rollback** the step; **narrow** scope; **escalate**; **NEED HUMAN APPROVAL** may be required before **retry** — not automatic continuation. |

---

### STRUCTURE CHANGE

| Facet | Content |
|--------|---------|
| **Meaning** | The current **Task** and/or **Plan** **decomposition** is **wrong** or **obsolete** — must **re-scope**, **replan**, or **reshape** structure (not a small fix inside the same step). |
| **When to emit** | **Task** cannot fit the **goal**; **plan** infeasible; **validate** **requires** **replan**; **required_agents** set **impossible**; **scope_in** / **layout** wrong. |
| **When NOT to emit** | For **trivial** edits, single-file **content** fixes, or **normal** validation **FAIL** that does **not** require **re-decomposing** the work — use step-level **failure** or other signals, not **structure** change, unless the **plan** is **void**. |
| **Related layers** | **Workflow**, **Control Plane** (**Planner** / **State**), **Agent Factory** (optional **off-ramp** per product policy), **Approval gates** (overlap with project-tree changes). |
| **Typical next action** | **Discard** or **archive** the **invalid** plan slice; **author** a new **Task** or **plan**; optionally trigger **Agent Builder** + registry update — **documented** path only in Phase 1. |

---

### CONTEXT MIGRATION NEEDED

| Facet | Content |
|--------|---------|
| **Meaning** | **Memory**, **knowledge pack**, or **self-describe**-style **context** is **inconsistent** with the **current** SoT, **layout**, or **version**; a **defined migration** (or rebuild) of **context artifacts** is required before **trustworthy** **routing** or **narration**. |
| **When to emit** | **Phase** or **layout** **shift**; **renamed** **paths** or **registry** **ids**; **stale** **RAG** / **memory** **slice**; **orchestration** or **introspection** would **mislead** without an **import** or **rebuild** step. |
| **When NOT to emit** | For **in-run** **UNKNOWN** (missing **agent** binding) — that is **UNKNOWN** unless the **sole** **issue** is **context** pack **lag**. For **one** bad **file** in an otherwise **valid** **tree** — may be ordinary **editing**, not full **context migration**. |
| **Related layers** | **Interfaces** (introspection, self-describe), **governance** (versioning, entity ops), **memory** (design docs), **Workflow** (if migration is a **gated** **track**). |
| **Typical next action** | **Run** **context** or **import** **checklist**; **rebuild** or **pin** **memory** **artifacts**; align **pointers** in SoT; then **re-run** **Self-Check** / **Self-Audit** as needed. |

---

### GIT CHECKPOINT NEEDED

| Facet | Content |
|--------|---------|
| **Meaning** | An **annotator** (human or policy) should **create** a **git** **milestone** (**commit** / **tag** / **push** as defined by [web-gpt-sources/04-workflows__git-rules.md](../web-gpt-sources/04-workflows__git-rules.md)) so **rollback** and **audit** **match** **change** **risk** or **size**. |
| **When to emit** | **Large** or **milestone** **edits**; **cross-cutting** **structural** **work**; **governance** **says** a **milestone** **warrants** a **record** per **git-rules**; **end** of **trajectory** before **hazardous** next step. |
| **When NOT to emit** | **Default** **doc** or **trivial** **touches** — [AGENTS.md](../AGENTS.md) **omits** this in **typical** **tasks**; do **not** use as **routine** **tag**. Prefer **NO GIT CHECKPOINT** to **explicit** **forego** when the user or policy wants **clarity**. |
| **Related layers** | **Governance** (commissions / **closeout**), **Cursor** / **ops** **workflow** (imported **git-rules**), **governance** **versioning** when **releases** are tied to **revisions**. |
| **Typical next action** | **Commit** (or **request** **commit**) with **conventional** **message**; **push** if **remote** **backup** **required**; then **continue** or **open** a **new** **task**. |

---

### NO GIT CHECKPOINT

| Facet | Content |
|--------|---------|
| **Meaning** | A **run** or **closeout** **actively** **declines** a **git** **milestone** for this **unit of work** — e.g. **doc-only** **hardening**, **draft**, or **user**-directed **omit** — to **avoid** **noise** or **contradict** [AGENTS.md](../AGENTS.md) **default**. |
| **When to emit** | **Explicit** user or **policy** **stipulation**; **scenarios** in **git-rules** where **checkpoint** is **optional**; **end**-of-task **summary** to **state** that **no** **commit** was **needed**. |
| **When NOT to emit** | When **GIT CHECKPOINT NEEDED** **criteria** are **met** — do **not** **declare** “no **checkpoint**” to **bypass** **governance** **milestone** **expectations** without **recorded** **rationale** or **waiver**. |
| **Related layers** | Same as **GIT CHECKPOINT NEEDED**; **governance** **and** **AGENTS.md** **closeout** **narrative**. |
| **Typical next action** | **Close** the **task** **without** a **commit**; **or** **switch** to **GIT CHECKPOINT NEEDED** if the **scope** **grew**. |

---

## 3. Alias and spelling policy (normative)

| Alias / variant | Status | Map to |
|-----------------|--------|--------|
| **`STRUCTURE_CHANGE`** (underscore) | **Legacy / non-canonical** | **STRUCTURE CHANGE** — always **prefer** the **spaced** **canonical** form in **new** **text** and **contracts**. |
| Other **underscore** or **abbrev** forms of **v0** names | **Non-canonical** | Map to the **§2** **titles**; **do not** **introduce** **new** **spellings** **without** a **dictionary** **revision** or **tracked** **exception** list. |

- **If** legacy text or external packs use **`STRUCTURE_CHANGE`**, **treat** it as **STRUCTURE CHANGE**; **update** the **string** when **editing** that **passage** for other reasons, or in a **dedicated** **normalization** **pass**.
- **Silent** **introduction** of **new** **signal** **tokens** (alternate **spellings** or **synonyms** **as** if **first-class**) is **out of** **scope**; **add** to **v1** or **amend** **v0** **here** first.

---

## 4. Cross-references (non-exhaustive)

| Document | Relevance |
|----------|-----------|
| [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md) | **Task** `signals` field. |
| [../workflows/execution-flow.md](../workflows/execution-flow.md) | **Stage**-level **emission** **points**. |
| [../security/README.md](../security/README.md) | **Security** **lens** on each signal. |
| [../security/approval-gates.md](../security/approval-gates.md) | **NEED HUMAN APPROVAL** **triggers**. |
| [../interfaces/self-check-v0.md](../interfaces/self-check-v0.md), [../interfaces/self-audit-v0.md](../interfaces/self-audit-v0.md) | **Gates** and **deep** **review**; overlap with **SAFE UNKNOWN**, **CONTEXT MIGRATION NEEDED**. |
| [../governance/master-build-map.md](master-build-map.md) | **Build** **order**; **where** **contracts** **land**. |

---

*End of System Signals Dictionary v0.*
