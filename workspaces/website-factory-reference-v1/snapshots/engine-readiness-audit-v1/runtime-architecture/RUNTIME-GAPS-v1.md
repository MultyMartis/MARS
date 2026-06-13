# Website Factory — Runtime Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/runtime-architecture/`  
**Статус:** future work register — **documentation only**

**Правило:** этот документ регистрирует **только будущую работу**. Не описывает реализацию и не утверждает существование перечисленных систем.

---

## 1. Назначение

Runtime Gaps v1 — единый регистр пробелов **после** Runtime Architecture v1 (movement discipline). Все пункты требуют **operator charter** перед началом.

---

## 2. Gap register

| Gap ID | Topic | Status | Notes |
|--------|-------|--------|-------|
| **RT-G01** | Workflow engine | **NOT STARTED** | BPMN/state machine execution — out of v1 scope |
| **RT-G02** | Agent execution | **NOT STARTED** | No AI agent orchestration in Factory runtime |
| **RT-G03** | Automation (n8n, CI state) | **NOT STARTED** | No automated state mutation |
| **RT-G04** | Runtime storage | **NOT STARTED** | DB / file-backed project state persistence |
| **RT-G05** | Project registry | **NOT STARTED** | Central index of Factory projects |
| **RT-G06** | Queue system | **NOT STARTED** | Work queues, prioritization |
| **RT-G07** | Execution logs | **NOT STARTED** | Machine-readable transition audit trail |
| **RT-G08** | MIG integration | **NOT STARTED** | `incoming/mig/` interoperability — charter required |
| **RT-G09** | Website Factory Engine | **NOT STARTED** | See Factory Engine Architecture — NOT QUEUED |
| **RT-G10** | Project manifest standard | **NOT STARTED** | Canonical JSON/YAML project state file |
| **RT-G11** | Validator CLI binding | **NOT STARTED** | Wire layer validators to state gates |
| **RT-G12** | Operator UI / dashboard | **NOT STARTED** | Visual state + gate tracking |
| **RT-G13** | Notification / webhook gates | **NOT STARTED** | External approval integrations |
| **RT-G14** | Multi-project concurrency rules | **NOT STARTED** | Resource locking semantics |
| **RT-G15** | Rollback automation | **NOT STARTED** | Scripted cascade invalidation |

---

## 3. Explicit non-gaps (handled elsewhere)

| Item | Location |
|------|----------|
| Page block validation automation | [VALIDATION-GAPS-v1.md](../page-block-validation/VALIDATION-GAPS-v1.md) |
| Content validation automation | [CONTENT-VALIDATION-GAPS-v1.md](../content-validation/CONTENT-VALIDATION-GAPS-v1.md) |
| Generation implementation | [GENERATION-GAPS-v1.md](../generation-contracts/GENERATION-GAPS-v1.md) |
| Production QA automation | [PRODUCTION-QA-GAPS-v1.md](../production-qa/PRODUCTION-QA-GAPS-v1.md) |

---

## 4. Dependency order (suggested — not approved schedule)

```text
Project manifest (RT-G10)
    → Runtime storage (RT-G04) + Project registry (RT-G05)
    → Execution logs (RT-G07)
    → Queue system (RT-G06) [optional]
    → MIG integration (RT-G08)
    → Factory Engine Architecture (RT-G09)
    → Workflow engine / automation (RT-G01, RT-G03) — highest risk; charter last
```

**SAFE UNKNOWN:** actual priority order — **requires operator charter**.

---

*Runtime Gaps v1 — 2026-06-01. Future work only; no implementation claims.*
