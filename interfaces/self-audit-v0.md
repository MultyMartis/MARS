# MARS — Self-Audit v0

**Status:** **documented** — **specification only** (no code, no config). **Self-Audit** is a deeper review of a **target** entity and its **documented** **dependencies** (registries, upstream and downstream **contracts**, governance **references**). Use it for governance and **pre-milestone** readiness, typically after [self-check-v0.md](self-check-v0.md).

**Version:** v0. Aligns with [universal-entity-operations.md](governance/universal-entity-operations.md).

---

## 1. Purpose

- Surface **cross-cutting** **inconsistencies** (terminology, version skew, lifecycle and log gaps, SoT gaps, **security/permissions** drift) that [Self-Check v0](self-check-v0.md) does not cover in a single pass.
- Produce a **fix** **plan** and an **explicit** list of **unknowns** so a full system audit or a broad **migration** does not rely on **silent** **gaps** in the documentation.
- This is **not** a substitute for a **formal** **operational** **security** **audit**: behavior **not** provable in-repo (or **via** **externally** **declared** **linked** SoT) is **SAFE UNKNOWN** **unless** **governance** **states** **otherwise**.

---

## 2. When to run

- When **expanding** **entity** **scope** (e.g. new **integration** type, new **subsystem** boundary).
- Before governance-oriented **narrative** (e.g. *ready for orchestration*, *pilot*) is **treated** as fact in public-facing or **contract** **docs** without **evidence** (per [AGENTS.md](AGENTS.md)).
- On **version** or **phase** **changes** that **span** **multiple** registries or **workflows**; align with [governance/versioning-model.md](governance/versioning-model.md).

**Prerequisite:** [self-check-v0.md](self-check-v0.md) should be **PASS**, or **NEED REVIEW** with a **documented** **rationale** for **deferred** **items**; **otherwise** **stabilize** **Self-Check** **outcomes** first.

---

## 3. Normative checks (v0)

| # | Check | What to verify |
|---|--------|----------------|
| 1 | Terminology consistency | Terms for the **entity** and its **dependencies** **match** [web-gpt-sources/01_system.md](web-gpt-sources/01_system.md) (terminology map) and **governance** **vocabulary**; **no** **conflicting** **role**, **state**, or **capability** **names** between **passport** and **contracts**. |
| 2 | Registry consistency | Every **registry** that **lists** the **entity** (agent, project, tool, supplementary **catalogs**) **agrees** on **id**, **status**, and **version**; **flag** **dangling** or **duplicate** **ids**. |
| 3 | Lifecycle and log consistency | [Documented events](logs/lifecycle-log.md) (where **this** file **is** the **log** of record) **align** with [governance/state-model.md](governance/state-model.md) and **entity-specific** **docs**; if a **declared** **phase** has **no** **expected** **event** where the process **is** **tracked** **locally** → **finding** **or** **SAFE** **UNKNOWN** (if **logging** **is** **not** **in** use **for** that **class**). |
| 4 | Versioning consistency | **Entity** version, **contract** version, and **compatibility** **per** [governance/versioning-model.md](governance/versioning-model.md); name **downstream** **readers** (e.g. **workflows**, [Control Plane](control-plane/contract.md) **narrative**) that **impose** **assumptions**. |
| 5 | Security and permissions risks | Stated access model, secrets handling, and PII / data residency (if **claimed**); unverified **assumptions** and **gaps** go to **risks** and **findings**. **Unimplemented** **controls** must **not** be **narrated** as **in** place. |
| 6 | Missing SoT links | Every **substantive** **assertion** in the **passport** **should** point to an **in-repo** SoT or be **labelled** **hypothesis** or **roadmap**; list **missing** **pointers** in **findings** or as **SAFE UNKNOWN**. |

**External SoT:** If the authoritative truth **lives** **outside** this repository (e.g. **corporate** wiki), the audit must **name** the **link** or **return** **SAFE UNKNOWN** for what **this** **workspace** **cannot** **verify** (see [universal-entity-operations.md](governance/universal-entity-operations.md) §6).

---

## 4. Output (normative)

A **Self-Audit** v0 result **must** include:

| Field | Content |
|-------|---------|
| **audit** **scope** | **Entity** id(s), **primary** type (see [supported entity types](governance/universal-entity-operations.md#2-supported-entity-types-normative)), **in**-**scope** and out-of-**scope** **boundaries**, and **dependency** **horizon** (e.g. **N**-hop registry and **contract** graph). |
| **findings** | **Structured** **list** with **severity**, **check** # **reference**, **summary**, and **evidence** path (or **explicit** **stated** **absence**). |
| **risks** | **Updates** to the **risks** **facet**; **security**, **operational**, **reputational** as **relevant**; name **owner** or **governance** **layer** when **known**. |
| **fix** **plan** | **Phased** **actions** (order, **dependencies**, **acceptance** **criteria**). **May** **include** **registry** **updates**, **doc** **migrations**, and **proposed** [lifecycle log](logs/lifecycle-log.md) **rows** (design-**only** in **v0**). |
| **SAFE** **UNKNOWN** **items** | **Explicit** **list** of **unverified** or **out-of-repo** **facts** and what **evidence** **type** or **location** would **discharge** each. |

**Optional conclusion:** A short narrative line may state **acceptable** (with or **without** **open** **findings**), or **not** **acceptable** **for** a **named** **purpose**; do **not** conflate with **Self-Check** **FAIL** if **deeper** **gaps** **differ**—**cross**-**link** in **findings** **as** **needed**.

---

## 5. Relation to other operations

- **RISK** **REVIEW** in [universal-entity-operations.md](governance/universal-entity-operations.md) may use **findings** and **risks** as **input**.
- **SELF MIGRATE** should not proceed (even as a **paper** plan) without an **updated** **fix** **plan** if **Self-Audit** **reveals** **blocking** **inconsistencies**, **unless** **governance** **records** a **waiver** (see [governance/versioning-model.md](governance/versioning-model.md) and [web-gpt-sources/14_roadmap.md](web-gpt-sources/14_roadmap.md)).
- **Introspection** / [Self-Describe](introspection-v0.md) does **not** **replace** **Self-Audit**; **output** must **not** **suggest** that **a** **Self**-**Audit** **passed** if one **was** **not** **performed** **(or** **if** **blocking** **findings** **remain** **open** **).**

---

*Last updated: Self-Audit v0 (entity + dependency review; documentation only).*

**System signals:** **Canonical** **names** and **meanings** for **SAFE UNKNOWN**, **CONTEXT MIGRATION NEEDED**, and related v0 **tokens** are in [governance/system-signals-dictionary.md](governance/system-signals-dictionary.md) (not all apply to every self-audit).
