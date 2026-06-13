# Website Factory — Runtime Gaps v1



**Версия:** v1 (governance synchronization update 2026-06-04)  

**Область:** `workspaces/website-factory-reference-v1/runtime-architecture/`  

**Статус:** future work register — **documentation only**



**Правило:** этот документ регистрирует **только будущую работу** (преимущественно **implementation**). Не описывает реализацию и не утверждает существование перечисленных систем.



**Governance sync:** [WEBSITE-FACTORY-GOVERNANCE-SYNCHRONIZATION-PASS-v1.md](../WEBSITE-FACTORY-GOVERNANCE-SYNCHRONIZATION-PASS-v1.md). Колонка **Doctrine** = architecture/charter **COMPLETE** в дереве; колонка **Implementation** = runtime/product **NOT STARTED**.



---



## 1. Назначение



Runtime Gaps v1 — единый регистр пробелов **после** Runtime Architecture v1, Factory Engine Architecture v1 (documentation), и post-Engine doctrine charters. Все пункты implementation требуют **operator charter** перед началом.



---



## 2. Gap register



| Gap ID | Topic | Doctrine / architecture | Implementation | Notes |

|--------|-------|-------------------------|----------------|-------|

| **RT-G01** | Workflow engine | N/A | **NOT STARTED** | BPMN/state machine execution — out of v1 scope |

| **RT-G02** | Agent execution | N/A | **NOT STARTED** | No AI agent orchestration in Factory runtime |

| **RT-G03** | Automation (n8n, CI state) | N/A | **NOT STARTED** | No automated state mutation |

| **RT-G04** | Runtime storage | N/A | **NOT STARTED** | DB / file-backed project state persistence |

| **RT-G05** | Project registry | **CHARTERED** — [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](../FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | **NOT STARTED** | Central index of Factory projects |

| **RT-G06** | Queue system | N/A | **NOT STARTED** | Work queues, prioritization |

| **RT-G07** | Execution logs | N/A | **NOT STARTED** | Machine-readable transition audit trail |

| **RT-G08** | MIG integration | N/A | **NOT STARTED** | `incoming/mig/` interoperability — charter required |

| **RT-G09** | Website Factory Engine | **CHARTERED** — Stages 1–6 + [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](../FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) **COMPLETE** (documentation) | **NOT STARTED** | Runtime product / automation — separate charters |

| **RT-G10** | Project manifest standard | **CHARTERED** — [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](../FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | **NOT STARTED** | Canonical JSON/YAML project state file |

| **RT-G11** | Validator CLI binding | N/A | **NOT STARTED** | Wire layer validators to state gates |

| **RT-G12** | Operator UI / dashboard | **CHARTERED** — [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](../FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | **NOT STARTED** | Visual state + gate tracking |

| **RT-G13** | Notification / webhook gates | N/A | **NOT STARTED** | External approval integrations |

| **RT-G14** | Multi-project concurrency rules | N/A | **NOT STARTED** | Resource locking semantics |

| **RT-G15** | Rollback automation | N/A | **NOT STARTED** | Scripted cascade invalidation |



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

Doctrine complete (Engine + Manifest + Registry + Tracking charters)

    → Project manifest implementation (RT-G10 impl)

    → Runtime storage (RT-G04) + Project registry implementation (RT-G05 impl)

    → Execution logs (RT-G07)

    → Queue system (RT-G06) [optional]

    → MIG integration (RT-G08)

    → Factory Engine runtime product (RT-G09 impl) — separate from documentation closure

    → Workflow engine / automation (RT-G01, RT-G03) — highest risk; charter last

```



**SAFE UNKNOWN:** actual priority order — **requires operator charter** (Operational Design phase).



---



*Runtime Gaps v1 — governance sync 2026-06-04. Future work only; no implementation claims.*

