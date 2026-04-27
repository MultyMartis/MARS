# MARS — Versioning Model (governance)

**Status:** **documented** — how **system**, **entity** (e.g. registry, contracts), and **compatibility** are **thought** about. No semver enforcement script exists in this repo for MARS as a product.

**Version:** v0.

---

## 1. Purpose

The **versioning model** defines:

- **System** versions (the **MARS** program or **release** line, when it exists).  
- **Entity** versions (documents, **agent** cards, **Task** **contract** snapshots).  
- **Contract** **changes** and **compatibility** **rules** so that **governance** can decide when **updates** are **major** (breaking) vs **compatible**.

---

## 2. System versions

| Concept | Definition | Current repo **truth** |
|---------|------------|------------------------|
| **MARS** **System** | The **as-designed** MARS stack (Control Plane, workflows, agents, memory, **future** **runtime**). | **No** **single** **SemVer** **string** in CI for “MARS 1.0” as a **binary**; **phases** are **described** in `../README.md`, `../AGENTS.md`, and `../web-gpt-sources/14_roadmap.md`. |
| **Phase** | **Coarse** **milestone** (e.g. Phase 1 = documentation **pack** / **governance** **foundation**). | **Project**-declared; **not** a **daily** version **bump** on every doc edit. |
| **Build / release** | **Future**: artifact **version** for a **runnable** **MARS** **or** **component** | **N/A** until build artifacts **exist**; use **git** and **conventional** **tags** as **the** team **chooses** (**SAFE UNKNOWN** for exact policy). |

**Rule:** **Do not** conflate **repo** **git** **history** with a **formal** **MARS** **LTS** **line** without an **explicit** **product** **decision** documented elsewhere.

---

## 3. Entity versions

| Entity class | What gets versioned | How (v0 governance) |
|--------------|----------------------|---------------------|
| **Layer contracts** | e.g. **Task** **Contract** **v0**, **Workflow** **v0** | **Filename** + **in-doc** `**Version:**` **(e.g.** `../workflows/task-contract-v0.md` **)**. A **bump** **creates** **a** new **version** (e.g. v1) **or** a **new** file **if** the team **splits** **versions** **in** **the** **tree** **(convention TBD**). |
| **Agent** **cards** | **Card** **content** **per** **role** | `changelog` field on **card** (required in `../agents/registry.md`); **registry** **itself** is **v0** as a **container** **doc**. |
| **Control** **Plane** **docs** | **Component** and **orchestrator** **contracts** | **v0** **snapshot** in `../control-plane/contract.md` **+** `components.md`; same **bump** **pattern** as **workflows**. |
| **Execution** / **governance** **addenda** | **This** `governance/` set | `**Version:**` **+** **changelog** table **in** each **file** **(footer)**. |
| **Imported** **pack** | **Web-GPT** **sourced** **docs** | **Treated** as **legacy** **imported**; **revisions** **may** **be** **incremental** **edits** **with** **git** **blame** **as** **provenance** **(no** **single** **import** **version** in **all** **headers**). |

**Minor vs patch (documentation):**

- **Patch**-level: typos, clarifications **that** **do** **not** **change** **obligations**.  
- **Minor** **doc**: new **section**, **new** **optional** **field** **in** a **table** with **default** **SAFE UNKNOWN** for **old** **readers**.  
- **Major** **/ breaking**: **renamed** **required** **field**, **removed** **state**, **redefined** **signal** **—** must **be** **called** out **in** **changelog** **and** **compat** **(§5)**.

---

## 4. Contract changes (process, not code)

1. **Propose** change in the **authoritative** **file** (or a **new** version **file** if **v0** is **frozen** for **a** **branch** **of** **product**s).  
2. **State** **scope**: **doc-only** **vs** **future** **API** (this repo is **doc-first**; **API** is **future**).  
3. **Update** **changelog** **(entity-level)** and **governance** **if** **cross**-**layer** **terms** **change**.  
4. **If** **breaking** **(§5)**, add **Migration** / **compatibility** **note** in **the** same **file** or **`../web-gpt-sources/13_migration.md`**.  
5. **No** **automatic** **bump** **of** “MARS 2.0”** **for** **one** **markdown** **edit** **without** **governance** **agreement** **(human** **decision**).

---

## 5. Compatibility rules (normative for documentation consumers)

| Change type | Consumer expectation |
|-------------|------------------------|
| **Forward-compatible** | **Older** **docs** **can** still **read** **new** **values** as **optional** or **strict superset** (new **row** in **table**, new **state** with **default**). |
| **Backward-incompatible** | **Consumers** (humans, **future** **code** **generators**) **must** **re-scan**; **old** **task** **JSON** **example** may be **invalid**. **Must** be **announced** in **changelog** **+** **major**-style **version** **(v0 →** **v1** **contract**). |
| **Registry** **card** | **Routers** (future) should **treat** **new** **permission** as **tighter** **=** **not** a **compatibility** **break**; **removing** **a** **permission** **or** **renaming** **role** **is** **breaking** for **stored** **references** **(task** `required_agents` **). |
| **Signals** **set** | **Renaming** **or** **dropping** **a** **signal** **=** **breaking** for **orchestration** **design**; **adding** a **new** **signal** **=** **minor** if **orchestrator** **defaults** **to** **ignoring** **unknown** **signals** **(future** **impl**). |

**Dual publication:** During **migrations**, **old** and **new** **contract** **docs** may **coexist** in **separate** **files** ( **preferred** to **unbounded** “§deprecated” in **one** file **if** the **divergence** is **large** ).

---

## 6. Relation to Git

- **Git** commit history is the provenance of who changed what.  
- A **MARS** version label for a deliverable release, when one exists, is a governance and product decision. See `../web-gpt-sources/04-workflows__git-rules.md` for Git checkpoint **conventions**; that is not a rule defined in this file.  

---

## 7. SAFE UNKNOWN

- **Exact** **SemVer** **policy** for a **future** `mars-runtime` **crate** or **package**.  
- **Calendar** or **LTS** **windows** for **MARS** **as** a **product**.

---

## 8. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-04-27 | Initial versioning model. |
