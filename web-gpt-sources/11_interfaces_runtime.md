# 01-architecture/01-architecture__interface-layer.md

## interface-layer.md

# Слой интерфейсов (Interface Layer)

Каналы взаимодействия человека и внешних систем с MARS.

## Типы интерфейсов

- **Chat UI** — диалоговый фронт.
- **Admin Panel** — реестры, политики, статусы workflow.
- **CLI** — операторские и dev-команды.
- **Telegram Bot** — мобильный/быстрый канал (lead/bot сценарии).
- **Web Dashboard** — метрики, логи, evals.
- **API Gateway** — REST/GraphQL/WebSocket по политике проекта.
- **Webhooks** — вход/выход для n8n и внешних систем.
- **IDE Integration** — **Cursor / Codex** как основной канал исполнения для ФС и кода.

## Текущие практические интерфейсы (для MARS v0 документации)

**Web-GPT**, **Cursor**, **GitHub**, **Obsidian**, **n8n**, **Telegram Bot** — реальные точки входа/выхода на этапе «док пак + ручные процессы»; унификация через API — **будущая** фаза.

## Правило разделения

Web-GPT формулирует **планы и промпты**; **исполнение на диске** — через Cursor/Codex (см. `06-rules/`).


---

# 01-architecture/01-architecture__devops-runtime-layer.md

## devops-runtime-layer.md

# Слой DevOps и runtime (DevOps / Runtime Layer)

Как MARS **работает** в среде исполнения: процессы, очереди, деплой, откат.

## Компоненты

| Компонент | Назначение |
|-----------|------------|
| **Runtime** | Процесс(ы) выполнения агентов и оркестратора |
| **Worker** | Фоновая обработка задач |
| **Queue** | Асинхронная очередь (retry, DLQ) |
| **Scheduler** | Cron, отложенные задачи |
| **Container** | Упаковка и изоляция сервисов |
| **Deployment** | Стратегия выката (blue/green, canary — по зрелости) |
| **CI/CD** | Сборка, тесты, проверки безопасности |
| **Environment** | dev/stage/prod, конфигурация без секретов в git |
| **Secrets** | Внешние хранилища секретов |
| **Rollback** | Откат артефакта и при необходимости схемы БД |

## Технологии (справочно)

**Docker**, **Docker Compose**, **GitHub Actions**, **PostgreSQL**, **Redis**, **Nginx**, **systemd**, **VPS**, **Sentry**, **Prometheus/Grafana** — типичный минимум для self-hosted; конкретика — **будущая** настройка пилота.

## Git safety

**Git checkpoints** (commit/branch/tag) на важных вехах — операционная практика, согласованная с Interface (Cursor) и политикой проекта.


---

## Execution Bridge (важно)

Execution Bridge — слой между Control Plane и реальным выполнением.

Отвечает за:
- передачу задач из Orchestrator в:
  - Cursor (локальные операции)
  - n8n (workflow automation)
  - скрипты / runtime
- нормализацию формата задач (Task Contract → Execution Task)
- контроль статуса выполнения
- возврат результата обратно в систему

На этапе v0:
Execution Bridge реализуется вручную через связку:
Web-GPT → Cursor

В будущем:
выделяется в отдельный runtime-компонент.