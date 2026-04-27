# MARS — Evaluations (Evals) v0

**Status:** **documented** — evaluation **types** and their **intended** **use**; **not** a test suite, **not** a runner, and **not** a golden dataset in-repo.

**Version:** v0. Revisable per [governance/versioning-model.md](../governance/versioning-model.md) and [governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Dataset locations, pass thresholds, and who signs off on production adoption are not fixed in v0.

---

## 1. Purpose

**Evals** in MARS **v0** are the **designed** **kinds** of **quality** **or** **correctness** **checks** applied to **agent**-**mediated** **work** (tasks, runs) **or** to **adoption** of **config** and **registry** **changes**, so that “works on my machine” is **replaced** **(when** **implemented) ** with **evidence**-**backed** **claims**. They **complement** **not** **replace** [../interfaces/self-audit-v0.md](../interfaces/self-audit-v0.md) (governance-**wide** file and risk posture) and **align** with **Validator** **role** **expectations** in [../agents/registry.md](../agents/registry.md) **(Validator** **Agent)**.

**No** **automated** **eval** **runner,** **CI** **job,** or **harness** is **implemented** in this **repository** for **v0** (Phase 1).

---

## 2. Eval types (v0)

| Eval type | Purpose |
|-----------|---------|
| **Task success** | **Whether** a **Task** (or run) met **stated** **outcomes** **(acceptance,** **artifact** **presence,** **terminal** **status)** per [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md) and [../workflows/workflow-v0.md](../workflows/workflow-v0.md). |
| **Hallucination check** | **Detect** **or** **score** **unsupported** **factual** **assertions** **(especially** where **RAG** **/ **grounding** **is** **claimed) **; **aligns** **with** [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md) **+** [../memory/knowledge-freshness-v0.md](../memory/knowledge-freshness-v0.md) **(documentation).** |
| **Source grounding** | **Whether** **outputs** **cite** or **rely** **on** **admissible** **retrieved** or **injected** **slices,** **per** [../memory/memory-retrieval-v0.md](../memory/memory-retrieval-v0.md) **+** [../models/context-budget-policy-v0.md](../models/context-budget-policy-v0.md) **(documentation).** |
| **Tool accuracy** | **Alignment** of **observed** **invocations** with **intended** **objectives** and **static** **contract** **(inputs,** **allowed** **agents,** **outcomes)**; **use** [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md), [../tools/tool-validation-rules-v0.md](../tools/tool-validation-rules-v0.md), and [../observability/tool-call-log-v0.md](../observability/tool-call-log-v0.md) (when **materialised**). |
| **Model routing correctness** | **Eligibility,** **fallback,** and **match** to **task** **risk** **(see** [../models/model-routing-v0.md](../models/model-routing-v0.md), [../models/model-policy-v0.md](../models/model-policy-v0.md)); **eval** **is** **design**-**time** or **harness**-**based** **until** **router** **exists. |
| **Memory write safety** | **Writes** **(or** **tombstones) ** that **conform** **to** [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) and **to** [../memory/memory-lifecycle-v0.md](../memory/memory-lifecycle-v0.md) **(authorisation,** **prohibited** **content,** **metadata) **. |

**SAFE UNKNOWN:** Weights, sampling strategy, and human- or LLM-as-judge mix per eval type are TBD.

---

## 3. Relation to Self-Audit and Validator Agent

- **Self**-**Audit** [../interfaces/self-audit-v0.md](../interfaces/self-audit-v0.md) may **in** **scope** **include** **evidence** of **evals** (or their **absence** as a **governance** **signal)** and may **recommend** **further** **evals** when **posture** **gaps** (see [governance/risk-register.md](../governance/risk-register.md)).
- The **Validator** **Agent** (registry **row,** [../agents/registry.md](../agents/registry.md)) is a design-time **role** for **constraining** **risky** **definitions;** **evals** are a **broader** **category** (runtime or batch **quality**). **Where** **both** **apply,** **governance** should **avoid** **duplicative** or **conflicting** sign-off without a **clear** SoT (documentation risk).

---

*End of Evaluations v0.*
