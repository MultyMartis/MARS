# 01-architecture/01-architecture__observability-layer.md

## observability-layer.md

# Слой наблюдаемости (Observability Layer)

Полная **прослеживаемость** запусков агентов, вызовов моделей и инструментов — наследие **lifecycle logs** и **workflow trackers** в промышленном виде.

## Сигналы и артефакты

- **Tracing** — распределённые трейсы шагов workflow.
- **Logging** — структурированные логи с correlation id.
- **Metrics** — латентность, ошибки, стоимость токенов, success rate.
- **Telemetry** — агрегированная телеметрия агентов.
- **Run History** — история запусков (связь с Audit / Lifecycle).
- **Tool Call Log** — кто, когда, с какими аргументами вызывал инструмент.
- **Audit Trail** — неизменяемая цепочка для compliance.
- **Evaluation Log** — результаты evals и регрессий.

## Инструменты (справочно)

**OpenTelemetry**, **LangSmith**, **Langfuse**, **AgentOps**, **Arize Phoenix**, **Grafana**, **Prometheus**, **Loki** — типичный стек; выбор — **будущий**.

## Принцип

Без наблюдаемости мультиагентная система **не отлаживается** и **не сертифицируется** по качеству; слой обязателен в целевой архитектуре.


---

# 01-architecture/01-architecture__evaluation-layer.md

## evaluation-layer.md

# Слой оценки качества (Evaluation Layer)

Систематическая **проверка** поведения MARS, а не только ручной «глазом».

## Практики

| Практика | Описание |
|----------|----------|
| **Evals** | Наборы проверок на фиксированных входах/ожиданиях |
| **Regression Tests** | Защита от деградации после смены модели/промпта |
| **Golden Dataset** | Эталонные пары вопрос–ожидаемый формат ответа |
| **Scenario Tests** | End-to-end сценарии с моками внешних систем |
| **LLM-as-a-Judge** | Вторичная модель как судья (с оговорками по bias) |
| **Human Review** | Выборочная или обязательная человеческая оценка |
| **Task Success Rate** | Метрика завершения задачи по контракту |
| **Hallucination Check** | Согласованность с источниками, SAFE UNKNOWN |
| **Tool Accuracy Check** | Корректность вызовов и побочных эффектов |

## Инструменты (справочно)

**OpenAI Evals**, **LangSmith Evaluations**, **Ragas**, **DeepEval**, **TruLens** — примеры; внедрение — **будущее**.

## Связь с Validator Agent

Автоматические evals **дополняют**, но **не полностью заменяют** специализированного валидатора и политики guardrails.


---

