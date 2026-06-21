# HomeGateway v4.ai — project documentation pack

**project_id:** `homegateway-v4-ai`  
**Program status (registry):** **`planned`** — PLANNED / DRAFT  
**Workspace status:** **UI Prototype** — `workspaces/homegateway-v4-ai/v1/` (static Gulp skeleton)  
**Documentation status:** **Operational Documentation Pack** (дисциплина ведения docs; **не** зрелость продукта)  
**Статус документации:** **DRAFT** · **PLANNING** · **STATIC-FIRST**  
**Реестр:** [registry/project-registry.md](../../registry/project-registry.md)

**Навигация сессии:** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) — открывать **Core Run** в первую очередь.

---

## Что это

**HomeGateway v4.ai** — **Personal Operational Cockpit** (личный операционный кокпит): приватный веб-интерфейс / многостраничный кокпит с доступом по логину для владельца веб-студии и оператора AI-assisted production ecosystem.

Роль в экосистеме MARS:

| Роль | Описание |
|------|----------|
| **Операционный surface layer** | Единая визуальная поверхность для частых ссылок, клиентов, проектов, дедлайнов и сигналов |
| **Cockpit UI** | Интерфейс «приборной панели», а не автономная система управления |
| **Display/control preparation layer** | Слой отображения и подготовки к будущему управлению; на этапе v0.1 — **только документация и статический фронтенд** |

HomeGateway **подключается к** MARS, n8n, Telegram-ботам, клиентским проектам, дедлайнам и операционным сигналам как **поверхность отображения и быстрых действий**, но **не является** ни одним из этих компонентов.

---

## Чем HomeGateway является

- Документационно-первый (**documentation-first**) операционный проект MARS.
- Личный операционный кокпит: централизация ссылок, клиент/проект, быстрая навигация, дедлайны, буфер обмена, быстрые действия.
- Планируемая связь с MARS (display-only блоки), n8n, ботами, локальным хранилищем — **только как FUTURE-INTEGRATION**.
- Проект с **block-screen** как базовой визуальной/UX-единицей (см. [cockpit-architecture-blueprint-v0.1.md](cockpit-architecture-blueprint-v0.1.md)).

---

## Чем HomeGateway НЕ является

- **Не** MARS-агент, **не** n8n workflow, **не** Telegram-бот.
- **Не** автономная система, **не** развёрнутый runtime, **не** активный control plane MARS.
- **Не** production orchestrator.
- **Не** замена MARS, ORCA, WPilot, MetaBOT или GitGuard.
- **Не** готовое динамическое приложение на текущем этапе.

---

## Граница MVP (v0.1)

**STATIC-FIRST** — статический фронтенд без реального backend:

- экран логина (mock/static);
- главная страница кокпита;
- layout на block-screen;
- образцы клиентов/проектов, MARS display-only, bot status, deadlines, quick actions, clipboard;
- mock popup-слоя;
- точка входа в admin (admin **не** реализован);
- основа тёмной/светлой темы через семантические токены.

**Не в scope v0.1:** реальный backend, реальная интеграция MARS/n8n, автоматизация дедлайнов.

---

## Карта документов (v0.1)

| Документ | Назначение |
|----------|------------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Операционная навигация сессии (Core Run) |
| [product-positioning-v0.1.md](product-positioning-v0.1.md) | Позиционирование продукта и границы честности |
| [cockpit-architecture-blueprint-v0.1.md](cockpit-architecture-blueprint-v0.1.md) | Архитектура кокпита, block-screen, зоны контента |
| [module-registry-draft-v0.1.md](module-registry-draft-v0.1.md) | Черновой реестр модулей кокпита |
| [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) | Черновик системы сигналов и уровней дедлайнов |
| [admin-layer-plan-v0.1.md](admin-layer-plan-v0.1.md) | План admin-слоя (после статического MVP) |
| [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md) | Семантические токены темы dark/light |
| [roadmap-v0.1.md](roadmap-v0.1.md) | Фазы 0–8 |

---

## Связи с экосистемой (кратко)

| Система | Связь с HomeGateway |
|---------|---------------------|
| **MARS** | Display-only статус/сигналы; **не** управление runtime |
| **n8n** | Планируемый bridge статусов/событий (**FUTURE-INTEGRATION**) |
| **Telegram bots** | Планируемые блоки статуса ботов (**FUTURE-INTEGRATION**) |
| **MetaBOT / SEO Content Agent** | Возможный источник display-сигналов (**SAFE UNKNOWN** — формат API) |
| **ORCA / WPilot** | Соседние операционные проекты; **не** заменяются HG |
| **Website Factory** | Клиентские сайты/проекты как контент кокпита; без orchestration claim |
| **Web Studio Polygon / MetaCODE sites** | Монитор лидов/заявок (планируется) |

Топология: [governance/ecosystem-topology-index.md](../../governance/ecosystem-topology-index.md).

---

## SAFE UNKNOWN

- Фактический стек фронтенда (Gulp vs Vite vs plain HTML) — **не зафиксирован** до Phase 4.
- Хостинг, домен, auth-провайдер — **не определены**.
- Формат данных MARS/n8n export для display-блоков — **не определён**.
- Рабочая папка `workspaces/homegateway-v4-ai/` — **не создана** в этой задаче (только project entity).

---

## Честность (MARS Phase 1)

См. [AGENTS.md](../../AGENTS.md): документация в репозитории **не доказывает** развёрнутое приложение, backend или live-интеграции.

*Последнее обновление пакета: 2026-05-20.*
