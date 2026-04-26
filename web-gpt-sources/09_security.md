# 01-architecture/01-architecture__security-guardrails-layer.md

## security-guardrails-layer.md

# Слой безопасности и guardrails (Security / Guardrails)

Защита **данных**, **модели поведения** и **инструментов** от злоупотреблений и ошибок.

## Элементы

| Элемент | Назначение |
|---------|------------|
| **Guardrails** | Жёсткие и мягкие правила на вход/выход (токсичность, утечки, формат) |
| **Policy Engine** | Централизованные политики (кто что может, куда пишем) |
| **Permission System** | Роли, scopes, approval |
| **Access Control** | RBAC/ABAC по мере зрелости |
| **Tool Approval** | Явное разрешение на опасные тулы |
| **Human Approval** | HITL на критических ветках |
| **Input / Output Validation** | Схемы, санитизация, ограничение длины |
| **Prompt Injection Defense** | Разделение инструкций и данных, фильтры, мониторинг |
| **PII Protection** | Маскирование, минимизация, региональные политики |
| **Secrets Management** | Vault-подобные решения, не хардкод в репо |
| **Sandboxing** | Изоляция исполнения кода и shell |

## Инструментарий (рынок, справочно)

- **OpenAI Agents SDK Guardrails**
- **NVIDIA NeMo Guardrails**
- **Pydantic / JSON Schema** — контракты данных
- **OPA** — policy-as-code (при необходимости)
- **HashiCorp Vault / Doppler / SOPS** — секреты

Статус для MARS: **планируемая** интеграция по фазам; конкретный набор — после threat model проекта.


---

