# MARS — Risk Register v0

**Status:** **documented** — human-maintained register of **known** and **emerging** risks for MARS **documentation** and **planned** systems. **No** automated enforcement, **no** runtime scanner, **no** machine schema in-repo for v0.

**Version:** v0. Revisable per [versioning-model.md](versioning-model.md) and [master-build-map.md](master-build-map.md). Supersedes informal “mental risk list” only when a later version explicitly replaces this register.

---

## 1. Purpose

- Make **risks explicit** before Self-Heal narratives, Tool Layer, Model Layer, Storage, external integrations, and **runtime** **implementation** documentation mature — so trade-offs and gaps are **visible**, not implicit.
- Give **one place** to record **what can go wrong**, **who owns** tracking, **how** it is mitigated (documentation or future controls), and **how** it links to **signals** and **dependencies**.
- Complement [dependency-map.md](dependency-map.md) (structural **edges**) and [system-signals-dictionary.md](system-signals-dictionary.md) (**operational** **vocabulary**): risks often sit **on** edges or **at** signal boundaries.

**SAFE UNKNOWN:** Rows not present in **section 8** are **unregistered** for this artefact until added; absence of a risk does **not** mean absence of hazard in the real world.

---

## 2. When to add a risk

Add (or split) a row when **any** of the following holds:

- A **new** hazard is identified in review, audit, lifecycle discussion, or cross-doc reading.
- A **dependency-map** change exposes a **new** `risk_if_broken` class that warrants **standalone** tracking (optional but recommended for **high** / **critical**).
- A **new** external **integration**, **runtime** surface, **storage** of sensitive data, or **governance** rule is **scoped** in documentation — **before** treating the scope as “safe by default”.
- **SECURITY RISK** is emitted (see **section 7**): entry is **mandatory**.
- **NEED HUMAN APPROVAL** is emitted for a **non-trivial** gate (irreversible effect, high blast radius, unclear policy): entry is **recommended**; **required** if the approval concerns **security**, **data**, **compliance**, or **integration** posture.

---

## 3. When to update a risk

Update **status**, **mitigation**, **owner**, **last_updated**, and **related_signal** when:

- Mitigation **progresses** (new doc, new gate, narrowed scope) or **stalls** (**blocked**).
- Severity **changes** (new evidence, scope creep, or reduced exposure).
- The risk is **superseded** by another row → mark **obsolete** and point to the replacing `risk_id`.
- A **lifecycle** event (see [../logs/lifecycle-log.md](../logs/lifecycle-log.md)) **closes** or **reopens** the underlying issue — reflect that in **status** / **mitigation** and optionally cite `event_id` in **mitigation** text.

**Material** changes to **risk posture** for a **build stage** should also be reflected in [master-build-map.md](master-build-map.md) or [dependency-map.md](dependency-map.md) when those files are the SoT for the change (same change set where practical).

---

## 4. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [dependency-map.md](dependency-map.md) | **Structural** **dependencies** (`entity_id` → `depends_on`). Broken edges imply **hazards**; the register names **risk** **instances** and **owners**. New entities in the map often warrant a **risk** row (or update). |
| [system-signals-dictionary.md](system-signals-dictionary.md) | **Canonical** **signal** names for **related_signal** and for **trigger** narratives. **SECURITY RISK** and **NEED HUMAN APPROVAL** tie directly to **section 7** rules here. |
| [../security/guardrails-v0.md](../security/guardrails-v0.md) | **Policy** and **validation** expectations; many **security**-type risks **mitigate** via guardrails + permissions docs. Register rows **must not** contradict guardrails without an explicit **accepted** risk. |
| [../logs/lifecycle-log.md](../logs/lifecycle-log.md) | **Append-only** trace for **governance** events (gate pass, map revision, audit). Significant **risk** **status** transitions may cite a lifecycle **event**; large **register** revisions may warrant a **lifecycle** row per [master-build-map.md](master-build-map.md) authority rules. |

---

## 5. Required fields (v0)

Every risk row **must** include:

| Field | Description |
|-------|-------------|
| **risk_id** | Stable identifier, unique in this register (e.g. `RISK-V0-0001`). |
| **entity_id** | Primary **system-level** entity or scope (align with [dependency-map.md](dependency-map.md) §4 vocabulary where possible; otherwise `mars` or a short **doc** scope name). |
| **risk_type** | One allowed value from **section 6.1**. |
| **severity** | One allowed value from **section 6.2**. |
| **status** | One allowed value from **section 6.3**. |
| **trigger** | What **causes** or **exposes** the risk (event, omission, or state). |
| **impact** | What **goes wrong** if the risk materialises (doc drift, false confidence, policy breach, …). |
| **mitigation** | **Current** handling: doc rule, gate, process, or **SAFE UNKNOWN** until addressed. |
| **owner** | **Role** or **named** maintainer (`TBD` allowed if explicitly unassigned). |
| **related_signal** | Canonical signal from [system-signals-dictionary.md](system-signals-dictionary.md) §2, or `—` if none applies. |
| **last_updated** | ISO date `YYYY-MM-DD` of last substantive edit to the row. |

---

## 6. Allowed values

### 6.1 risk_type

| Value | Use when |
|-------|----------|
| **architecture** | Structure, boundaries, layers, or **path** / SoT resolution. |
| **security** | Policy escape, injection class, permission gaps, **guardrail** failures. |
| **data** | Wrong, lost, or **unauthorised** **data** handling (incl. memory/RAG **design**). |
| **tooling** | Editor, agent, CI, or **dev** **workflow** hazards (not product “Tool Layer” alone). |
| **integration** | Third-party systems, credentials, **external** APIs. |
| **runtime** | **Processes**, workers, enforcement **engines** — **planned** or **missing**. |
| **governance** | Roadmap, honesty, **register** discipline, **git** **checkpoint** culture. |
| **compliance** | **Legal** / **regulatory** obligations (e.g. **PII**, locale-specific rules). |

### 6.2 severity

| Value | Guidance (v0) |
|-------|----------------|
| **low** | Nuisance, easy rollback, limited blast radius. |
| **medium** | Material **doc** or **process** harm; recoverable with effort. |
| **high** | Wrong **decisions**, **security** ambiguity, or **large** rework if unaddressed. |
| **critical** | **Immediate** **integrity** or **safety** threat if triggered; blocks **honest** **progression** until mitigated or **explicitly** **accepted**. |

### 6.3 status

| Value | Meaning |
|-------|---------|
| **open** | Active; mitigation incomplete or unproven. |
| **mitigated** | Acceptable residual; controls or **docs** in place and **verified** at **design** level. |
| **accepted** | Known residual; stakeholders accept **no** further mitigation in scope. |
| **blocked** | Cannot progress mitigation until **dependency** / **decision** / **resource** clears. |
| **obsolete** | Superseded or no longer applicable; cite successor `risk_id` if any. |

---

## 7. Rules (normative v0)

1. **SECURITY RISK** — Any emission of **SECURITY RISK** (per [system-signals-dictionary.md](system-signals-dictionary.md)) **must** result in **create** or **update** of a **risk** row within the **same** maintenance episode (same PR / same doc session / same logged task), with **related_signal** = `SECURITY RISK` unless downgraded with recorded rationale.
2. **NEED HUMAN APPROVAL** — May **create** or **update** a row when the underlying decision is **non-trivial** (see **section 2**). **Must** update if the approval outcome **changes** accepted **security** / **compliance** / **integration** posture.
3. **New external integration** — Documenting or **scoping** a **new** third-party **integration** **requires** a **risk** **review**: add or update **integration**-type (and **security**/**compliance** as needed) rows **before** treating the integration as **approved** for narrative or **registry** purposes.
4. **New runtime implementation** — Any **new** **runtime** **implementation** claim, **repo** layout for processes, or **execution** **enforcement** **requires** a **risk** **review**: add or update **runtime** (and **security**) rows; align [dependency-map.md](dependency-map.md) per map **§5**.

---

## 8. Initial known risks (v0 seed rows)

| risk_id | entity_id | risk_type | severity | status | trigger | impact | mitigation | owner | related_signal | last_updated |
|---------|-----------|-----------|----------|--------|---------|--------|------------|-------|----------------|--------------|
| RISK-V0-0001 | `mars` | governance | medium | open | Conflicting guidance: **GIT CHECKPOINT NEEDED** vs **default no commit** in [AGENTS.md](../AGENTS.md) / [web-gpt-sources/04-workflows__git-rules.md](../web-gpt-sources/04-workflows__git-rules.md). | Noise commits, skipped **milestones**, or **disputed** audit trail. | Treat **AGENTS.md** + **git-rules** as **paired** SoT; explicit **NO GIT CHECKPOINT** or **GIT CHECKPOINT NEEDED** in **closeout** when ambiguous. | TBD | GIT CHECKPOINT NEEDED | 2026-04-27 |
| RISK-V0-0002 | `introspection_self_describe` | architecture | medium | mitigated | **Path** literals or links interpreted from **wrong** root (historical `../` vs repo-root-relative). | **Wrong** SoT in **Self-Describe** / audits (Stage **7.5** class). | **Introspection** v0 **default** **bindings**; **master** map **residual** **P2** hygiene for non-interface docs. | TBD | SAFE UNKNOWN | 2026-04-27 |
| RISK-V0-0003 | `mars` | governance | critical | open | **Outputs** claim **implementation** **exists** without **in-repo** evidence ([AGENTS.md](../AGENTS.md) **honesty**). | **False** **confidence**, **wrong** **roadmap** **decisions**. | **Guardrails** §8–9 + **Self-Check** / **Self-Audit**; **register** only **evidenced** facts. | TBD | SECURITY RISK | 2026-04-27 |
| RISK-V0-0004 | `mars` | tooling | medium | open | Large **uncommitted** or **unreviewed** **working** **tree** alongside **governance** edits. | **Missed** **conflicts**, **partial** **application** of **fixes**, **opaque** **reviews**. | **Small** **change** **sets**; **lifecycle** **notes** for **cross-cutting** **work**; **human** **diff** **discipline**. | TBD | NEED HUMAN APPROVAL | 2026-04-27 |
| RISK-V0-0005 | `mars` | runtime | high | open | **No** **runtime** **enforcement** **engine** in **Phase** **1** **repo**; **contracts** **describe** **future** **controls** only. | **Policy** **documented** but **not** **executable**; **gap** **between** **spec** and **behaviour**. | **Explicit** **doc-only** **stance** in **security** **README** and **maps**; **risk** **review** **before** **runtime** **code**. | TBD | SAFE UNKNOWN | 2026-04-27 |
| RISK-V0-0006 | `mars` | integration | high | open | **External** **integrations** **referenced** in **legacy** **pack** or **roadmap** **without** **MARS-native** **catalog** **row** **yet**. | **Unknown** **data** **flows**, **credential** **topology**, **review** **gaps**. | **Section** **7.3**; **SAFE UNKNOWN** for **live** **endpoints**; **Stage** **15** **catalog** **when** **scoped**. | TBD | SAFE UNKNOWN | 2026-04-27 |
| RISK-V0-0007 | `mars` | compliance | high | open | **PII** **storage**, **retention**, **locale** (**e.g.** **RF;** **laws** **including** **152-ФЗ**); **not** **encoded** **as** **product** **controls**. | **Regulatory** or **customer** **exposure** **if** **assumed** **done**; **unapproved** **PII** in **durable** **memory** without **governance** **(see** [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) **§3b,** **§4**). | **Do** **not** **claim** **compliance**; [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) **(unapproved** **PII** **prohibition,** **retention** **metadata**); **Stage** **8**/**11** **before** **data** **paths**; [../security/approval-gates.md](../security/approval-gates.md) **+** HITL; **legal** **interpretation** **of** **152-ФЗ** / **other** **norms** **—** **SAFE** **UNKNOWN** **until** **formal** **legal** **review** **(outside** **this** **repo**). | TBD | NEED HUMAN APPROVAL | 2026-04-27 |
| RISK-V0-0008 | `runtime_state_store` | data | high | open | **Contracts** **authored** ([../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md), [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md), [../storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md), [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md)); **residual:** **no** **implemented** **store** **or** **enforcement** — **inconsistent** **state** **after** **failure**/**partial** **write**/**timeout** **still** **possible** **without** **runtime**; **backend**, **clock**, **and** **exact** **dedup** **mechanisms** **remain** **SAFE** **UNKNOWN**. | **Lost** **run** **history**, **false** **resume**, **audit** **failure**, **wrong** **recovery** **SoT** **vs** [**lifecycle-log**](../logs/lifecycle-log.md), **operators** **trust** **stale** **checkpoints**. | **v0** **rules:** **append**/**no** **silent** **overwrite** **(store** **v0)**; **pre**-**resume** **validation** **+** **SAFE** **UNKNOWN** **on** **inconsistency** **(checkpoint**/**resume** **protocol)**; **retry**/**idempotency** **bounds** **(failure** **model)**; **keep** [**dependency-map.md**](dependency-map.md) **`runtime_state_store`** **edges** **current**; **risk** **review** **before** **runtime** **code** **(register** **§7.4)**. | TBD | SAFE UNKNOWN | 2026-04-27 |
| RISK-V0-0009 | `checkpoint_resume_protocol` | runtime | high | open | **Checkpoint**/**resume** **contract** **exists** ([../storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md)); **no** **runner** **implements** **it**; **mis**-**placed** **checkpoints**, **skewed** **timestamps**, **or** **wrong** **`step`** **binding** **still** **yield** **replay** **hazards** **at** **implementation** **time**. | **Duplicate** **execution** **of** **side** **effects**, **resume** **from** **wrong** **`step`**, **HITL** **pickup** **ambiguity**. | **Treat** **protocol** **as** **normative** **for** **design**; **pair** **with** [**failure-model-v0.md**](../workflows/failure-model-v0.md) **and** [**state-model.md**](state-model.md); **extend** **dependency**-**map** **edges** **when** **execution** **engine** **lands**; **integration**/**runtime** **risk** **rows** **per** **§7**. | TBD | SAFE UNKNOWN | 2026-04-27 |
| RISK-V0-0010 | `failure_model` | security | medium | mitigated | **Retry** **chaos** **and** **unbounded** **duplicate** **execution** **—** **documentation** **was** **thin**; **Failure** **Handling** **Model** **v0** **now** **caps** **retries**, **binds** **SECURITY** **RISK** **→** **escalate**, **and** **requires** **idempotency**/**duplicate**-**tool** **awareness** **([../workflows/failure-model-v0.md](../workflows/failure-model-v0.md))**. **Residual:** **numeric** **limits**, **token** **formats**, **and** **Tool**-**layer** **dedup** **remain** **SAFE** **UNKNOWN** **until** **Stage** **9+**. | **Double** **execution**, **integrity** **risk**, **uncontrolled** **retries** **amplifying** **failures** **or** **costs**. | **Adopt** **failure** **model** **in** **orchestration**/**bridge** **docs**; **enforce** **STRUCTURE** **CHANGE** **before** **blind** **retry**; **align** [**system-signals-dictionary.md**](system-signals-dictionary.md); **re**-**open** **row** **if** **Tool** **contracts** **contradict** **§5**. | TBD | SECURITY RISK | 2026-04-27 |
| RISK-V0-0011 | `memory_write_policy` | data | high | mitigated | **Unclear** **memory** **write** **authority** (who may write what, when) **at** **contract** **level** **before** Memory **Write** **Policy** **v0**. | **Policy** **escape**, **unauthorized** **retention** **paths** **in** **design**. | **Memory** **Write** **Policy** **v0** **authored** [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) **(allowed** **writers,** **prohibited** **content,** **metadata,** **types**); **pair** [../security/permissions-v0.md](../security/permissions-v0.md) / [../security/guardrails-v0.md](../security/guardrails-v0.md); [../governance/dependency-map.md](../governance/dependency-map.md) **`memory_write_policy`** **edges**. **Residual:** **no** **runtime** **enforcement** **or** **store** **—** **SAFE** **UNKNOWN** **until** **implementation**; **HITL** **for** **sensitive** **PII** per **policy** **§3b–§5**. | TBD | NEED HUMAN APPROVAL | 2026-04-27 |
| RISK-V0-0012 | `threat_model` | security | high | mitigated | **Residual:** **matured** **Tool** **/** **MCP** **documentation** **and** **any** **runtime** **can** **surface** **new** **tactics** **not** **listed** **in** [../security/threat-model-v0.md](../security/threat-model-v0.md) **(exhaustive** **catalog** **is** **not** **a** **v0** **claim**). | **Unregistered** **or** **under**-**modelled** **hazards** **on** **new** **surfaces** **(future**). | [../security/threat-model-v0.md](../security/threat-model-v0.md) **authored**; [**dependency-map.md**](dependency-map.md) **`threat_model`** **edges** **(incl.** **P0** **bridge** **/** **state** **/** **failure** **/** **memory**); **add** **or** **tighten** **rows** **at** **Stage** **9+** **when** **Tool** **contracts** **or** **implementation** **expand** **the** **attack** **narrative**. | TBD | SECURITY RISK | 2026-04-27 |
| RISK-V0-0013 | `recovery_playbooks` | governance | medium | mitigated | **Residual:** **live** **ops** **and** **future** **orchestrators** **are** **not** **covered** **by** **MARS** **v0** **(documentation**-**only**; **RISK**-**V0**-**0005**). | **Recovery** **could** **still** **bypass** **HITL** **/ approval** **in** **the** **field** **if** **processes** **ignore** **governance** **(people** **/** **runtime**). | [../interfaces/recovery-playbooks-v0.md](../interfaces/recovery-playbooks-v0.md) **authored**; **per**-**playbook** **triggers,** **allowed** **/** **forbidden,** **HITL**; **pair** [../interfaces/self-heal-v0.md](../interfaces/self-heal-v0.md) **+** [../security/approval-gates.md](../security/approval-gates.md) **+** [**dependency-map.md**](dependency-map.md) **`self_heal` → `recovery_playbooks`**. | TBD | NEED HUMAN APPROVAL | 2026-04-27 |
| RISK-V0-0014 | `tool_registry` | security | high | open | **Tool** **misuse** — **invocations** **outside** **registry** **rows,** **agent** **allowlists,** **or** **task** **scope** **(design** **or** **future** **runtime**). | **Policy** **escape,** **cost** **amplification,** **unreviewed** **side** **effects** **per** [../security/threat-model-v0.md](../security/threat-model-v0.md) **§3.3**. | [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md) **§4**; [../tools/registry.md](../tools/registry.md); [../security/permissions-v0.md](../security/permissions-v0.md); [**dependency-map.md**](dependency-map.md) **`tool_*`** **edges**; **residual:** **no** **enforcement** **engine** **(RISK**-**V0**-**0005**). | TBD | SECURITY RISK | 2026-04-27 |
| RISK-V0-0015 | `tool_registry` | integration | high | open | **Unsafe** **external** **calls** — **undeclared** **egress,** **wrong** **allowlists,** **or** **unreviewed** **third-party** **behaviour** **(see** [../security/threat-model-v0.md](../security/threat-model-v0.md) **§3.7**). | **Data** **exfiltration,** **integration** **abuse,** **credential** **exposure** **paths**. | [../tools/tool-safety-model-v0.md](../tools/tool-safety-model-v0.md) **§4** **(external** **class** **+** **`external-call`**); [../security/approval-gates.md](../security/approval-gates.md) **§2**; **SAFE** **UNKNOWN** **for** **live** **endpoints** **until** **catalogued** **(RISK**-**V0**-**0006**). | TBD | SECURITY RISK | 2026-04-27 |
| RISK-V0-0016 | `tool_safety_model` | security | high | open | **Hidden** **side** **effects** — **registry** **row** **under**-**states** **mutations** **or** **external** **reach** **vs** **actual** **tool** **behaviour** **(documentation** **/** **implementation** **gap**). | **False** **audit** **trail,** **replay** **harm,** **trust** **in** **wrong** **gates** **(links** **RISK**-**V0**-**0003** **honesty**). | [../tools/tool-safety-model-v0.md](../tools/tool-safety-model-v0.md) **§4** **(no** **hidden** **effects**); **registry** **reviews**; **Self**-**Check** **/** **Self**-**Audit** **when** **in** **scope**. | TBD | SECURITY RISK | 2026-04-27 |
| RISK-V0-0017 | `tool_safety_model` | governance | high | open | **Missing** **approval** **for** **high-risk** **tools** — **HITL** **skipped** **in** **process** **or** **automation** **before** **destructive** **/** **external** **effects**. | **Irreversible** **ops** **without** **accountable** **human** **decision** **per** [../security/approval-gates.md](../security/approval-gates.md). | [../tools/registry.md](../tools/registry.md) **`approval_required`** **`yes`** **for** **`high`** **risk** **(tool-safety-model** **v0)**; **composite** **rule** **with** **task** **`risk_level`**; **NEED** **HUMAN** **APPROVAL** **emission** **per** [system-signals-dictionary.md](system-signals-dictionary.md) **§2**. | TBD | NEED HUMAN APPROVAL | 2026-04-27 |
| RISK-V0-0018 | `tool_agent_binding` | architecture | high | open | **Wrong** **tool** **binding** — **stale** **`allowed_tools`**, **registry** **row** **mismatch** **(e.g.** **allowed_agents** **/ **tool_id**),** **or** **undocumented** **agent**-**to**-**tool** **drift** (see [../tools/tool-agent-binding-v0.md](../tools/tool-agent-binding-v0.md), [dependency-map.md](dependency-map.md)). | **Planned** **or** **routed** **invocations** **that** **do** **not** **match** **authoritative** **allowlists;** **false** **orchestration** **assumptions** (documentation; **residual** **RISK**-**V0**-**0005**). | [../tools/tool-agent-binding-v0.md](../tools/tool-agent-binding-v0.md); [dependency-map.md](dependency-map.md) **`tool_agent_binding`**; **card** / **registry** **reviews;** **pair** **RISK**-**V0**-**0014** **where** **overlap** **(tool** **misuse**). | TBD | STRUCTURE CHANGE | 2026-04-27 |
| RISK-V0-0019 | `tool_validation_rules` | security | high | open | **Tool** **bypassing** **validation** — **pre**-**call** **checks** **(see** [../tools/tool-validation-rules-v0.md](../tools/tool-validation-rules-v0.md) **)** **omitted,** **short**-**circuited,** **or** **routed** **around** the **Execution** **Bridge** (design or future implementation). | **Unauthorised** **side** **effects,** **lost** **signals,** [../security/threat-model-v0.md](../security/threat-model-v0.md) **Category** **3;** **amplifies** **RISK**-**V0**-**0005** **(no** **enforcement** **).** | [../tools/tool-workflow-integration-v0.md](../tools/tool-workflow-integration-v0.md); [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md); [dependency-map.md](dependency-map.md) **edges** **for** **`tool_workflow_integration`**, **`tool_validation_rules`**. | TBD | SECURITY RISK | 2026-04-27 |
| RISK-V0-0020 | `tool_agent_binding` | security | high | open | **Tool** **misuse** **by** **agent** — **permitted** **or** **borderline**-**permitted** **use** **for** **off**-**objective** **goals,** **prompt**-**driven** **abuse,** **or** **orchestration** **/ **HITL** **confusion** (distinct from **RISK**-**V0**-**0014** **(off**-**registry) ** and **RISK**-**V0**-**0018** **(wrong** **binding) ** in **focus**).** | **Harm** **to** **data,** **systems,** **or** **governance;** **audit** **/ **HITL** **circumvention** **(documentation** / **ops**).** | [../tools/tool-agent-binding-v0.md](../tools/tool-agent-binding-v0.md) **§4;** [../security/threat-model-v0.md](../security/threat-model-v0.md) **§3.3;** [../security/approval-gates.md](../security/approval-gates.md) **+** [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md); **cross**-**ref** **RISK**-**V0**-**0014. ** | TBD | SECURITY RISK | 2026-04-27 |

*Note:* **RISK-V0-0002** is marked **mitigated** for **interface**-scoped **P0** **path** work per **master** **build** **map** **audit** **block**; **residual** **P2** **remains** **outside** **`interfaces/`**.

---

## 9. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | **Risk Register v0** — purpose, add/update rules, relations, fields, enums, normative rules, seed rows. |
| 2026-04-27 | **GAP** **Analysis** — **RISK**-**V0**-**0008**–**0013** (**runtime** **state**, **checkpoint**/**resume**, **failure**/**retry**, **memory** **write** **authority**, **threat** **model**, **recovery**/**approval** **gates**); aligned with [master-build-map.md](master-build-map.md) **Stage** **8.5** and [dependency-map.md](dependency-map.md). |
| 2026-04-27 | **RISK**-**V0**-**0008** **refined** — **runtime** **persistence** **+** **lost**/**corrupted** **state** **risk** **linked** **to** [../storage/runtime-state-store-v0.md](../storage/runtime-state-store-v0.md), **Execution** **Bridge** **v0**, **remaining** **Stage** **8.5** **P0**, **`related_signal`** **→** **SAFE** **UNKNOWN** (**backend**/**residual** **gaps**). |
| 2026-04-27 | **Failure** **/** **Checkpoint** **contracts** — **RISK**-**V0**-**0008**/**0009**/**0010** **refined** **for** **inconsistent** **state** **after** **failure**, **duplicate** **execution**/**replay**, **retry** **chaos**; **cite** [../workflows/failure-model-v0.md](../workflows/failure-model-v0.md), [../storage/checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md); **RISK**-**V0**-**0010** **severity** **medium**, **status** **mitigated** **(residual** **SAFE** **UNKNOWN** **until** **Tool**/**runtime**). |
| 2026-04-27 | [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) — **RISK**-**V0-0011** **status** **mitigated** **(contract** **normative,** **residual** **enforcement** **/ store** **UNKNOWN**); **RISK**-**V0-0007** **refined** **(PII,** **RF,** **152-ФЗ** **+** **durable** **memory,** **approval** **citations**). |
| 2026-04-27 | [../security/threat-model-v0.md](../security/threat-model-v0.md) **and** [../interfaces/recovery-playbooks-v0.md](../interfaces/recovery-playbooks-v0.md) — **RISK**-**V0-0012** **and** **RISK**-**V0-0013** **mitigated** **(residual** **rows** **per** **§8**). |
| 2026-04-27 | **Stage** **9** **Tool** **Layer** **v0** — **RISK**-**V0-0014** **(tool** **misuse),** **RISK**-**V0-0015** **(unsafe** **external** **calls),** **RISK**-**V0-0016** **(hidden** **side** **effects),** **RISK**-**V0-0017** **(missing** **approval** **for** **high-risk** **tools**); **cross**-**ref** **[../tools/](../tools/)** **contracts** **and** [**dependency-map.md**](dependency-map.md). |
| 2026-04-27 | **Stage** **9.5** **Tool** **Layer** **integration** — **RISK**-**V0-0018** **(wrong** **tool** **binding),** **RISK**-**V0-0019** **(tool** **bypassing** **validation),** **RISK**-**V0-0020** **(tool** **misuse** **by** **agent**); **SoT** **[../tools/tool-agent-binding-v0.md](../tools/tool-agent-binding-v0.md)**, **[../tools/tool-workflow-integration-v0.md](../tools/tool-workflow-integration-v0.md)**, **[../tools/tool-permission-enforcement-v0.md](../tools/tool-permission-enforcement-v0.md)**, **[../tools/tool-validation-rules-v0.md](../tools/tool-validation-rules-v0.md)**. |

---

*End of MARS Risk Register v0.*
