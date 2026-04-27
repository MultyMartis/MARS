# MARS — Model Policy v0

**Status:** **documentation only** — normative **design-time** rules for **which** models may be used **how**, given task context, data sensitivity, and MARS security contracts. **No** policy engine or enforcement code is claimed in-repo ([../AGENTS.md](../AGENTS.md)).

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Bind **task → model** decisions to **explicit** rules so that routing is not an ad-hoc “pick the strongest model” choice.
- Ensure **high-risk** work, **external** provider calls, and **user/project** data flows are **governed** consistently with security, memory, and risk artefacts.
- Mandate that **no** **default unrestricted model** exists in the MARS narrative: every runnable path **must** be covered by task type, policy, registry row **status**, and budgets before a model is **eligible** ([model-registry-v0.md](model-registry-v0.md), [cost-token-budget-v0.md](cost-token-budget-v0.md)).

**SAFE UNKNOWN:** Exact policy grammar, storage of overrides per `project_id`, and runtime evaluation order are **not** specified until implementation is evidenced.

---

## 2. Normative references (must respect)

Model use **must** respect the following SoT documents where applicable:

| Document | Why |
|----------|-----|
| [../security/permissions-v0.md](../security/permissions-v0.md) | Grants and denials for agents, tools, and **future** model-invoke permissions must align. |
| [../security/threat-model-v0.md](../security/threat-model-v0.md) | Threat classes (injection, exfiltration, tool abuse, **etc.**) constrain **what** may be sent **where**. |
| [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) | Durable memory writes, PII classes, and retention **block** or **require HITL** certain model+memory combinations. |
| [../governance/risk-register.md](../governance/risk-register.md) | **RISK** rows for model selection, provider exposure, cost growth, fallback, and context hazards **must** stay coherent with policy text ([risk-register.md](../governance/risk-register.md) **§7** when emissions apply). |

Cross-references: [../security/guardrails-v0.md](../security/guardrails-v0.md), [../security/approval-gates.md](../security/approval-gates.md), [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md).

---

## 3. Task → model policy rules (v0)

- **Rule M-POL-01 — Task typing:** Every orchestrated **task** **must** carry a **task type** (or equivalent tag set) usable by policy. Without a type, the model path **must** **DENY** or emit **SAFE UNKNOWN** (no silent default model).
- **Rule M-POL-02 — Registry gate:** Only **model_id** rows with **status** in `{ approved, active }` may be **eligible** for selection once a registry exists at runtime; **planned**, **draft**, and **deprecated** are **ineligible** unless a **governance** exception is documented (which should produce **NEED HUMAN APPROVAL** / lifecycle evidence).
- **Rule M-POL-03 — allowed / prohibited:** A candidate model **must** appear as **allowed** for the task type and **must not** appear on **prohibited_tasks** for that row ([model-registry-v0.md](model-registry-v0.md)).
- **Rule M-POL-04 — Capability match:** If the task **requires** capabilities (e.g. vision, JSON mode), models **without** those capabilities are **ineligible**.
- **Rule M-POL-05 — Data policy match:** **data_policy** on the model row **must** be **compatible** with the task’s declared **data sensitivity** and **egress** class. **Mismatch → DENY** or **NEED HUMAN APPROVAL** per [../security/approval-gates.md](../security/approval-gates.md).

---

## 4. Risk-based model selection

- **Low risk tasks** — May use **lower** **cost_class** models when capabilities suffice; still subject to **budgets** and **registry** **status**.
- **Medium risk** — Prefer models with **clear** **data_policy** and **documented** retention posture; **external** providers require **integration**-class review per [risk-register.md](../governance/risk-register.md) **§7.3**.
- **High risk tasks** — **Must** use models explicitly **allowed** for that task class; **must** enforce **HITL** / **NEED HUMAN APPROVAL** where [../security/approval-gates.md](../security/approval-gates.md) applies; **must not** silently downgrade to a **higher** **risk_level** model without a **documented** exception path.

Risk alignment: see [../governance/risk-register.md](../governance/risk-register.md) rows for wrong model, provider exposure, fallback safety, and context hazards.

---

## 5. PII / sensitive data handling

- **No raw secrets or credentials** in prompts or tool-derived context assembled for models — per [../security/threat-model-v0.md](../security/threat-model-v0.md) and guardrails.
- **PII** — Follow [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md): **unapproved** PII **must not** be written to durable memory; similarly, **policy** **must** restrict which **models** and **providers** may **process** PII classes that are **allowed** in the task contract.
- **Minimisation:** Policy **prefers** **redacted** or **summarised** representations over raw user content when the task allows.

---

## 6. No default unrestricted model

- There is **no** “global default LLM” in MARS v0 policy: selection **requires** **task** context, **registry** eligibility, **routing** output, and **budget** outcome.
- If **no** model satisfies **all** constraints, the outcome is **DENY**, **degraded capability** with explicit **signals**, or **NEED HUMAN APPROVAL** — **not** silent use of an unrestricted model.

---

## 7. Rules for specific situations

### 7.1 High-risk tasks

- **Require** explicit **model allow-list** intersection (task × agent × project).
- **Require** **approval gates** for irreversible or high-blast-radius combinations ([../security/approval-gates.md](../security/approval-gates.md)).
- **Embeddings / indexing** of restricted content **must** follow the same **data_policy** and memory rules as **chat** models.

### 7.2 External provider calls

- Treated as **integration** surface: **egress**, **logging**, **subprocessor**, and **retention** **unknowns** **must** be labelled **SAFE UNKNOWN** until catalogued ([risk-register.md](../governance/risk-register.md) **§7.3**).
- **DENY** by default for **highly sensitive** tasks unless a **documented** exception and **risk** row updates exist.

### 7.3 User / project data

- **project_id**-scoped rules **must** align with [../registry/project-registry.md](../registry/project-registry.md) and permissions.
- **Cross-project** reuse of model traces, caches, or **fine-tuning** assumptions is **out of scope** for v0 unless explicitly added — treat as **denied** until specified.

### 7.4 Model fallback

- Fallback **only** along **registry** **fallback_model_id** edges or an explicit **ordered chain** from [model-routing-v0.md](model-routing-v0.md).
- **Each** fallback hop **must** **re-evaluate** policy (task type, data policy, risk, **budget**).
- **Must not** fall back from a **denied** or **high**-**risk** path to a **less**-**governed** model **without** **NEED HUMAN APPROVAL** or **DENY** outcome.

---

## 8. Relation to Tool Layer

- **Tool results** fed to models are subject to the same **context** and **PII** rules ([context-budget-policy-v0.md](context-budget-policy-v0.md)); tool **risk_level** and **approval_required** from [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md) / [../tools/registry.md](../tools/registry.md) **inform** whether **stronger** model policy tiers apply post-tool execution.

---

## 9. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Model Policy v0** — task rules, risk tiers, PII, no default model, external/provider/user/fallback rules; cross-refs to security, memory, risk register. |

---

*End of MARS Model Policy v0.*
