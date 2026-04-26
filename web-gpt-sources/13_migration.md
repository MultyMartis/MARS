# 07-migration/07-migration__legacy-system-analysis.md

## legacy-system-analysis.md

# Анализ legacy: «Мой первый ИИ system»

## Честное резюме

Система **условно** называемая **«Мой первый ИИ system»** начиналась как **Gulp-сборщик страниц** и workflow вокруг него, затем **органически выросла** в конструкции вроде **Main Brain**, пакетов **MCA / AI.Pack**, реестров и памяти — без полной унификации под индустриальную MAS-терминологию.

## Что в ней ценно (идеи для MARS)

- Ранний **control plane** в образе **Main Brain**.
- **Agent Registry** как мысль о каталоге ролей.
- **WebGPT Memory Module** — стремление к структурированной памяти.
- **Lifecycle logs** и **workflow trackers** — прослеживаемость.
- **Project registry** — учёт контекста проектов.
- **SAFE UNKNOWN** — антигаллюциногенный принцип.
- **Git safety checkpoints** — дисциплина отката.
- **Gulp Frontend Agent** — практичный специалист по статике.
- Цикл **prompt → execute → report** — операционный стандарт.

## Что требует нормализации

- Смешение **имён** и ролей без маппинга на стандарт MAS.
- Риск **хаоса** в структуре артефактов без жёсткого DevOps и evals.

## Вывод для MARS

MARS — **новая** система на стандартной архитектуре; legacy — **источник уроков**, не шаблон копирования «как есть».


---

# 07-migration/07-migration__mapping-old-to-mars.md

## mapping-old-to-mars.md

# Маппинг: «Мой первый ИИ system» → слои MARS

| Элемент legacy | Слой / компонент MARS |
|----------------|------------------------|
| Main Brain | **Control Plane** (Orchestrator / Supervisor) |
| Factory Engineer | **Agent Layer** — Agent Builder |
| FlyCheck | **Agent Layer** — Validator + **Security/Guardrails** |
| Agent Registry | **Agent Layer** + `02-core/agent-registry.md` |
| System Signals | **Security/Guardrails** + `02-core/system-signals.md` |
| Self-Describe | **Memory** + introspection, **Interface** (контекст для Cursor) |
| Project Registry | **Memory** / **Storage** — System Registry |
| Lifecycle Log | **Observability** + **Storage** (audit / run history) |
| Workflow Tracker | **Workflow Layer** + State Store |
| WebGPT Memory Module | **Memory Layer** + будущий **RAG** |
| Gulp page builder | **Agent Layer** — Gulp Frontend Agent; **Tool** — Gulp/File/Git |
| prompt → execute → report | **Workflow Layer** + **Interface** (Web-GPT ↔ Cursor) |
| Git checkpoints | **DevOps/Runtime** + правила Web-GPT / Cursor |


---

# 07-migration/07-migration__migration-principles.md

## migration-principles.md

# Принципы миграции в MARS

1. **Брать полезные идеи** — реестры, логи, специалист по Gulp, SAFE UNKNOWN, Git-чекпоинты.
2. **Не копировать хаос** — новая структура документов и кода осмысленно и минимально достаточно.
3. **Переименовать в стандартные термины** — см. `terminology-map.md`.
4. **Сохранить практичный workflow** — prompt → execute → report + validate + log.
5. **Сохранить Gulp Frontend Agent** как явного специалиста в карточке и реестре.
6. **Сначала чистая структура** — док-пак, starter, репозиторий, затем автоматизация и интеграции.


---

