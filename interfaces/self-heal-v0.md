# MARS — Self-Heal / Recovery System v0

**Status:** **documented** — **specification only** (no code, no automation, no auto-fix). **Self-Heal v0** defines how MARS **proposes** **recovery** and **remediation** **plans** for **detected** **issues** and **risks**. It does **not** execute fixes, mutate the filesystem, or apply registry changes.

**Version:** v0. Aligns with [self-check-v0.md](self-check-v0.md), [self-audit-v0.md](self-audit-v0.md), [governance/system-signals-dictionary.md](governance/system-signals-dictionary.md), [governance/risk-register.md](governance/risk-register.md), [governance/dependency-map.md](governance/dependency-map.md), and [security/guardrails-v0.md](../security/guardrails-v0.md).

---

## 1. Purpose

- **Primary goal:** Given **issues** and **risks** already surfaced by MARS documentation and governance artifacts, **produce** a **structured** **recovery** / **fix** **plan** (ordered steps, approvals, unknowns) that a **human** or **future** **governed** **process** may **execute** **outside** this spec.
- **Non-goals:** **No** direct system mutation, **no** “heal” **execution** **loop**, **no** implied **runtime** **or** **tool** **invocation**. Anything that sounds like **auto-repair** is **out of scope** for v0.

---

## 2. Input sources (normative)

A **Self-Heal** v0 **planning** **pass** **consumes** **evidence** **from** **one** **or** **more** **of**:

| Source | Role in Self-Heal |
|--------|-------------------|
| **[Self-Check v0](self-check-v0.md) results** | Fast **verdicts** (**PASS** / **FAIL** / **NEED REVIEW**), check **#** references, **issues**, and **recommended_fix** lines — primary **triggers** for **entity-level** **documentation** and **registry** gaps. |
| **[Self-Audit v0](self-audit-v0.md) findings** | **Findings**, **risks**, **fix plan** hints, **SAFE UNKNOWN** items — **cross-cutting** **inconsistency** and **dependency** **horizon**. |
| **[Risk Register](../governance/risk-register.md) entries** | **Explicit** **risk** **ids**, **severity**, **enums**, and **rules** — **prioritization**, **mitigation** **class**, and **register** **update** **proposals**. |
| **[Dependency Map](../governance/dependency-map.md)** | **Entity → entity** **edges** and **types** — **affected** **neighbors**, **blast** **radius**, and **dependency** **correction** **steps**. |
| **[Lifecycle Log](../logs/lifecycle-log.md)** | **Events** **relevant** to **phase**, **gates**, and **governance** **decisions** — **temporal** **context** and **what** **changed** **before** the **issue**. |

**SAFE UNKNOWN:** If an input slice is **missing**, **stale**, or **not** **applicable**, the Self-Heal **output** **must** **list** that slice under **SAFE UNKNOWN items** (see §5) and **must not** **invent** **evidence**.

---

## 3. Output (normative)

A **Self-Heal** v0 **artifact** (**recovery** **plan** **document** or **equivalent** **structured** **block**) **must** **include**:

| Field | Content |
|-------|---------|
| **issue summary** | **Plain-language** **summary** of **what** **is** **wrong** **or** **at** **risk**, tied to **input** **pointers** (check #, audit finding id, risk id, dependency row, lifecycle event id). |
| **risk level** | **Alignment** with [risk-register.md](../governance/risk-register.md) **severity** / **category** **where** **possible**; **otherwise** **NEED REVIEW** **or** **SAFE UNKNOWN** **with** **rationale**. |
| **affected entities** | **Entity** **ids** **and** **types** per [universal-entity-operations.md](../governance/universal-entity-operations.md) **and** **dependency-map** **rows** **touched** **or** **implied**. |
| **recommended fix steps** | **Ordered** **steps** **only** — **documentation** **edits**, **registry** **row** **proposals**, **permission** **narrative** **updates**, **dependency** **map** **addenda**, **risk** **mitigation** **actions**. **Each** **step** **must** **name** **recovery** **type** (§4). |
| **required approvals** | **Per** **step**: **none** (doc-only **clarification**), **governance** **review**, or **NEED HUMAN APPROVAL** / **escalation** (§4, §6). |
| **SAFE UNKNOWN items** | **Explicit** **list** **matching** [self-audit-v0.md](self-audit-v0.md) **and** [system-signals-dictionary.md](../governance/system-signals-dictionary.md) **discipline** — **what** **cannot** **be** **verified** **in-repo** **and** **what** **would** **discharge** **each** **unknown**. |

---

## 4. Recovery types (normative taxonomy)

Every **recommended** **fix** **step** **must** **tag** **one** **primary** **recovery** **type**:

| Type | Description |
|------|-------------|
| **documentation fix** | **Correct** **or** **extend** **markdown** / **contract** **text**, **links**, **terminology**, **examples** — **no** **structural** **repo** **change** **beyond** **normal** **edits**. |
| **dependency correction** | **Propose** **updates** to [dependency-map.md](../governance/dependency-map.md) **(new** **edges**, **corrections**, **deprecation** **notes)** — **documentation** **only** **until** **a** **human** **applies** **the** **edit**. |
| **registry update** | **Propose** **new** **or** **changed** **rows** in **registries** (e.g. [project-registry.md](../registry/project-registry.md), [agents/registry.md](../agents/registry.md)) — **plan** **only**; **execution** is **human** **or** **future** **pipeline**. |
| **permission correction** | **Align** **stated** **permissions**, **guardrails**, **or** **approval** **gates** **with** **SoT** — **references** [security/permissions-v0.md](../security/permissions-v0.md), [security/approval-gates.md](../security/approval-gates.md), [guardrails-v0.md](../security/guardrails-v0.md). |
| **risk mitigation plan** | **Propose** **mitigations** **tied** to [risk-register.md](../governance/risk-register.md) **entries** **(new** **or** **updated** **rows**, **control** **narrative**, **residual** **risk)**. |
| **escalation (NEED HUMAN APPROVAL)** | **Step** **cannot** **be** **safely** **specified** **or** **adopted** **without** **human** **decision** — **mandatory** **when** §6 **triggers** **fire** **or** **when** **policy** **requires** **HITL** per **approval** **gates**. |

---

## 5. Rules (normative)

1. **No direct mutation** — **Self-Heal** **never** **modifies** **the** **system** **directly** (no writes to **repo**, **registries**, **maps**, **logs** **as** **part** **of** **this** **spec**). **Output** is **always** a **plan**, **not** **execution**.
2. **Plan not execution** — **Artifacts** **are** **inputs** **to** **human** **or** **future** **governed** **workflows**; **they** **do** **not** **close** **tasks** **or** **imply** **merge** **without** **separate** **process**.
3. **Filesystem, structure, external integrations** — **Any** **recommended** **fix** **involving** **any** **of** **the** **following** **must** **carry** **required** **approvals** **including** **NEED HUMAN APPROVAL** **(and** **often** **escalation** **recovery** **type)**:
   - **filesystem** — **paths**, **tree** **layout**, **moves**, **adds** **of** **new** **top-level** **areas**, **bulk** **renames**;
   - **structure** — **task** / **plan** **decomposition** **changes** **at** **system** **level**, **new** **stages** **or** **boundaries** **in** **master** **build** **map**, **breaking** **contract** **reshapes**;
   - **external integrations** — **new** **or** **changed** **third-party** **dependencies**, **credentials**, **live** **endpoints**, **out-of-repo** **SoT**.
4. **No auto-fixing logic** — **v0** **forbids** **specifying** **automated** **repair** **procedures**, **bots**, **or** **“apply** **fix”** **semantics**; **only** **human-readable** **plans** **and** **explicit** **gates**.
5. **Honesty** — **Plans** **must** **obey** [AGENTS.md](../AGENTS.md): **do** **not** **claim** **implementation** **exists** **unless** **evidenced**; **use** **SAFE UNKNOWN** **for** **unverified** **slices**.

---

## 6. Relation to system signals

When **inputs** **or** **inferred** **state** **map** **to** **canonical** **signals** in [system-signals-dictionary.md](../governance/system-signals-dictionary.md), **Self-Heal** **outputs** **must** **treat** **them** **as** **follows**:

| Signal | Self-Heal behavior |
|--------|-------------------|
| **UNKNOWN** | **Request** **clarification** **in** **the** **plan** **(first** **steps** **=** **resolve** **bindings**, **name** **SoT**, **stop** **short** **of** **guessing**); **do** **not** **fabricate** **downstream** **steps** **that** **assume** **missing** **facts**. |
| **SAFE UNKNOWN** | **Allow** **a** **partial** **plan** **for** **verified** **slices** **only**; **list** **each** **unknown** **under** **SAFE UNKNOWN** **items**; **mark** **steps** **that** **depend** **on** **discharging** **unknowns** **as** **blocked** **or** **conditional**. |
| **SECURITY RISK** | **Escalate** **priority** **in** **issue** **summary** **and** **risk** **level**; **bias** **toward** **escalation** **(NEED HUMAN APPROVAL)** **and** **risk** **mitigation** **plan** **type**; **cross-link** [risk-register.md](../governance/risk-register.md) **and** [guardrails-v0.md](../security/guardrails-v0.md). |
| **STRUCTURE CHANGE** | **Require** **approval** **before** **any** **adoption** **of** **structural** **recommendations**; **recovery** **steps** **must** **state** **that** **the** **plan** **slice** **is** **invalid** **until** **re-scoping** **is** **approved** **(align** **with** **dictionary** **typical** **next** **actions**). |

**Note:** **NEED HUMAN APPROVAL** **is** **both** **a** **signal** **and** **a** **recovery** **type** **(escalation)** **when** **the** **plan** **itself** **cannot** **proceed** **without** **a** **human** **gate**.

---

## 7. Relations to other documents (contract graph)

| Document | Relation |
|----------|----------|
| [governance/risk-register.md](../governance/risk-register.md) | **Source** **of** **risk** **ids** **and** **rules**; **Self-Heal** **may** **propose** **new** **rows** **or** **field** **updates** **as** **text** **only**. |
| [governance/dependency-map.md](../governance/dependency-map.md) | **Source** **for** **blast** **radius** **and** **dependency** **correction** **steps**; **must** **stay** **consistent** **with** **affected** **entities**. |
| [security/guardrails-v0.md](../security/guardrails-v0.md) | **Constrains** **what** **plans** **may** **recommend** **(no** **silent** **widening**, **evidence** **for** **claims)**; **security**-**angled** **findings** **tie** **to** **SECURITY** **RISK** **handling**. |
| [interfaces/self-audit-v0.md](self-audit-v0.md) | **Upstream** **deep** **findings** **and** **fix** **plan** **hints**; **Self-Heal** **may** **normalize** **and** **merge** **multiple** **audits** **into** **one** **recovery** **artifact**. |
| [interfaces/self-check-v0.md](self-check-v0.md) | **Upstream** **quick** **gates**; **FAIL** / **NEED REVIEW** **often** **seed** **documentation** **fix** **or** **registry** **update** **steps**. |
| [interfaces/recovery-playbooks-v0.md](recovery-playbooks-v0.md) | **Normative** **playbook** **types** **and** **per**-**playbook** **(trigger,** **allow/forbid,** **approvals,** **signals**)** **—** **each** **Self**-**Heal** **step** **should** **map** **to** **a** **playbook** **where** **applicable** **(Stage** **8.5** **P0**). |

---

## 8. When to use (guidance)

- After **Self-Check** **FAIL** **or** **NEED** **REVIEW** **when** **a** **single** **coherent** **remediation** **narrative** **is** **needed**.
- After **Self-Audit** **when** **findings** **span** **multiple** **entities** **or** **require** **ordered** **governance** **actions**.
- When **Risk** **Register** **or** **Dependency** **Map** **review** **(§7** **risk-register**, **dependency-map** **§5)** **is** **triggered** **by** **build** **map** **or** **lifecycle** **events** — **Self-Heal** **can** **package** **the** **proposed** **doc** **changes** **only**.

---

*End of Self-Heal / Recovery System v0 (documentation only; plans, not execution).*
