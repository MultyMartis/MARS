# MARS — Release Gates v0

**Status:** **documented** — which **change** **classes** require **evaluation** before **adoption**; not **automation,** not **a** **CI** **job.**

**Version:** v0. Revisable per [governance/versioning-model.md](../governance/versioning-model.md) and [governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Named approvers, review SLAs, and evidence format for NEED REVIEW are TBD in v0.

---

## 1. Purpose

**Release** **gates** state **which** **kinds** of **change** must **clear** a **quality** **bar** (per [evals-v0.md](evals-v0.md), [governance/risk-register.md](../governance/risk-register.md), and [../logs/lifecycle-log.md](../logs/lifecycle-log.md) where applicable) before the change is **treated** **as** **adopted** for a **line** of **defence** or **project** **narrative**. They are **complementary** to **operation**-**time** **HITL** in [../security/approval-gates.md](../security/approval-gates.md) (a **policy** **or** **registry** **change** may **require** **both** **a** **release** **eval** and **HITL** for **tactical** **execution**).

**No** **automated** **eval** **runner** or **merge**-**time** **enforcer** **is** **implemented** in **v0.**

---

## 2. What changes require evaluation before adoption (v0)

| Change class | Why eval matters (documentation) |
|--------------|----------------------------------|
| **Agent** **changes** | **Registry** **/ **card** **rows** **affect** **orchestration** and **tool** **allowlists** ([../agents/registry.md](../agents/registry.md), [../tools/tool-agent-binding-v0.md](../tools/tool-agent-binding-v0.md)). |
| **Prompt** **/ **policy** **changes** | **Safety,** **memory,** and **tool** **use;** [../control-plane/contract.md](../control-plane/contract.md), [../security/guardrails-v0.md](../security/guardrails-v0.md). |
| **Model** **routing** **/ **policy** **/ **registry** **changes** | **Eligibility,** **fallback,** **cost,** **data** **policy;** [../models/model-routing-v0.md](../models/model-routing-v0.md), [../models/model-policy-v0.md](../models/model-policy-v0.md), [../models/model-registry-v0.md](../models/model-registry-v0.md). |
| **Tool** **/ **MCP** **/ **side**-**effect** **surface** **changes** | **Integration** and **threat** **class;** [../tools/](../tools/) **contracts;** [../governance/dependency-map.md](../governance/dependency-map.md) **(tool**-**layer** **entities) **. ** |
| **Memory** **/ **RAG** **changes** | **Durable** **knowledge,** **retention,** **RAG;** [../memory/](../memory/) **SoT,** e.g. [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md), [../memory/rag-architecture-v0.md](../memory/rag-architecture-v0.md). |

**SAFE UNKNOWN:** **Smoke** **vs** **full** **regression** **depth** is **TBD** **per** **project. **

---

## 3. Outcomes (v0, closed set)

| Outcome | Meaning |
|---------|---------|
| **PASS** | Stated **eval** or **harness** **criteria** met; **adoption** **allowed** if there are no **unresolved** RISK or **SAFE** `UNKNOWN` **/ **governance** **gaps** (waivers must be explicit). |
| **FAIL** | **Adoption** not acceptable **until** defects fixed **or** HITL **/ **waiver; see [../security/approval-gates.md](../security/approval-gates.md) for operation-time gates. |
| **NEED** **REVIEW** | Evidence **inconclusive;** **human** **/ **governance** **triage;** may append [../logs/lifecycle-log.md](../logs/lifecycle-log.md) and revisit [governance/risk-register.md](../governance/risk-register.md). |

---

*End of Release Gates v0.*
