# MARS — Audit Trail v0

**Status:** **documented** — contract for **what** must be **reconstructable** for **accountability** and **governance** **reviews.** Not a compliance system, WORM store, or implementation.

**Version:** v0. Revisable per [governance/versioning-model.md](../governance/versioning-model.md) and [governance/master-build-map.md](../governance/master-build-map.md).

**SAFE UNKNOWN:** Jurisdiction-specific retention, legal hold, and cryptographic notarization are out of scope for v0.

---

## 1. Purpose

The **audit trail** in MARS **v0** means the **set** of **artefacts** and **pointers** that **allow** a **reviewer** (human **or** **a** **future** **enforcement** **system)** **to** **reconstruct** **authoritative** **decisions** **affecting** **safety,** **data,** and **governance,** without **conflating** that **with** **gossip**-**level** **operational** **chatter. It **sits** **next** to **(and** **may** **index)** [run-history-v0.md](run-history-v0.md), [event-model-v0.md](event-model-v0.md), and [../logs/lifecycle-log.md](../logs/lifecycle-log.md) **(append**-**only** **governance**), **and** it **informs** [governance/risk-register.md](../governance/risk-register.md) **(explicit** **risks**).

**No** dedicated **compliance** **or** **immutable** **write**-**once** **storage** **is** **implemented** **in** this **repository** **(Phase** **1**).**

---

## 2. What must be auditable (v0)

| Category | Rationale and pointers |
|----------|-------------------------|
| **Approvals** | Gated work must retain **who/what/when** **—** [../security/approval-gates.md](../security/approval-gates.md); [tool-call-log-v0.md](tool-call-log-v0.md) **`approval_ref`**. |
| **Security risks** | Emissions and handling of **SECURITY RISK** and related signals; [governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md); [governance/risk-register.md](../governance/risk-register.md) rows. |
| **Memory writes** | Durable knowledge mutations per [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) and [../memory/memory-lifecycle-v0.md](../memory/memory-lifecycle-v0.md); not silent overwrites. |
| **External calls** | Egress to third parties **via** tools (see [../security/threat-model-v0.md](../security/threat-model-v0.md) **Categories 3, 7**; [../tools/tool-safety-model-v0.md](../tools/tool-safety-model-v0.md) **external** class). |
| **Model routing decisions** | Which model(s) and fallbacks; [../models/model-routing-v0.md](../models/model-routing-v0.md); [../models/model-policy-v0.md](../models/model-policy-v0.md). |
| **Tool calls with side effects** | [tool-call-log-v0.md](tool-call-log-v0.md) with **`side_effects`** and **`signals`**; alignment with [../tools/registry.md](../tools/registry.md) and safety model. |

**SAFE UNKNOWN:** The exact product mechanism (single store vs composite views) to satisfy every row in this table in production is not evidenced in-repo.

---

## 3. Append-only principle (documentation)

- **Lifecycle** log is **append**-**only** by **design** [../logs/lifecycle-log.md](../logs/lifecycle-log.md).
- **Run**-facing and audit-grade records ([run-history-v0.md](run-history-v0.md), [event-model-v0.md](event-model-v0.md), [tool-call-log-v0.md](tool-call-log-v0.md)) should favour **append** or **immutability**-tolerant **strategies**; **silent** **destructive** **edits** to historical “what was approved or invoked” are **incompatible** with this v0 narrative **unless** a **documented** **compensating** **receipt** is **added** (e.g. a new **row** that **supersedes** a prior one, with **pointers**).
- **WORM** or **tombstone**-**only** **edits** **in** a **dedicated** **audit** **store** are **a** **future** **implementation** **topic,** not **a** **v0** **deliverable.**

---

## 4. Relation to lifecycle log and risk register

- **Lifecycle** **log** **(governance) **: **“what** **we** **decided** as** a **build** or **governance** **org** (gates, **maps**).**
- **Audit** **trail** (this** **file)** **: **“what** **the** **system** **(when** **built) ** would **need** to **reconstruct** **safety**-**relevant** **and** **policy**-**relevant** **execution** **facts,**” **independent** of **day**-**to**-**day** **developer** **chatter.**
- **Risk** **register** (see [governance/risk-register.md](../governance/risk-register.md)) **lists** **named** **hazards;** **audit** **gaps** **(missing** **traces) ** are **governance** **/** **compliance**-**type** **risks** and should **appear** as **rows,** not as **implicit** **gaps.**

---

## 5. No compliance storage implementation (Phase 1)

- This **file** does **not** **claim** a **compliant** **archive,** **SIEM** **ingestion,** or **e**-**discovery** **readiness.**
- **Regulatory** or **industry** **obligations** are **TBD** **and** must **not** be **inferred** **from** MARS **v0** **markdown** **alone.**

---

*End of Audit Trail v0.*
