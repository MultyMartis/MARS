# HomeGateway v4.ai — UX discovery notes v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 1  
**Не является:** результатом formal user research, deployed product feedback.

---

## Каноническое позиционирование

**HomeGateway v4.ai** = **Personal Operational Cockpit** — приватный веб-кокпит / сайт с доступом по логину для владельца веб-студии, AI-assisted production ecosystem, клиентских операций и MARS-connected infrastructure.

| Термин | Значение в HG |
|--------|----------------|
| **cockpit** | Главная метафора UI — приборная панель оператора |
| **operational surface layer** | Поверхность отображения и быстрых действий; **не** control plane |
| **block-screen** | Базовая визуальная единица (см. [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md)) |
| **signal system** | Уровни срочности и статусы (см. [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md)) |
| **display-only MARS** | Блоки MARS только для чтения на v0.1 |
| **static-first** | Статический фронтенд до backend и live integrations |
| **admin-aware** | Разметка и структура данных готовы к будущему CRUD |

HG **не** MARS-агент, **не** n8n workflow, **не** Telegram-бот — но **связан** с ними как operational surface layer.

---

## Primary operator (draft persona)

- **Кто:** владелец / главный оператор веб-студии (один primary user).
- **Контекст:** переключение между клиентами, сайтами, MARS-документацией, automation (n8n/bots), дедлайнами и ручными задачами.
- **Цель сессии в HG:** быстро понять «что горит», открыть нужный ресурс, скопировать подготовленную строку, не теряясь в закладках.

---

## Jobs-to-be-done (операторские задачи)

| # | Задача | Как HG должен помочь | Приоритет (draft) |
|---|--------|----------------------|-------------------|
| 1 | Открыть частый ресурс (админка, repo, doc) | Frequent links, website/admin blocks | P0 |
| 2 | Вспомнить статус клиента/проекта | Clients/Projects, Project view | P0 |
| 3 | Не пропустить дедлайн | Active + recurring monitors, signal rail | P0 |
| 4 | Понять «жив ли» automation | Bot/n8n/system status (display-only) | P1 |
| 5 | Glance at MARS lane / pack status | MARS monitor (display-only) | P1 |
| 6 | Увидеть новые лиды с сайтов студии | Leads: Polygon + MetaCODE | P1 |
| 7 | Повторяющееся действие в один клик | Quick actions strip | P1 |
| 8 | Скопировать шаблон (brief, handoff line) | Clipboard blocks | P2 |
| 9 | Детали без ухода с кокпита | Popup / overlay layer | P2 |
| 10 | Комфорт при долгой работе | Dark/light theme | P0 |
| 11 | Позже править данные без правки HTML | Admin (after static MVP) | P1 (planned) |

---

## Pain points (гипотезы для валидации на wireframes)

| Pain | Текущее состояние (типично) | Целевое в HG |
|------|-----------------------------|--------------|
| Разрозненные закладки | Десятки папок в браузере | Единый cockpit + группы ссылок |
| Потеря дедлайнов | Календарь / заметки вне контекста клиента | Signal rail + overdue persistence |
| Непрозрачность bots/n8n | Заходить в каждую систему | Aggregated status block-screens |
| MARS context switch | Открывать repo / OPERATIONAL-INDEX вручную | Display-only summary + deep links |
| Повторный ввод текста | Копировать из старых писем | Clipboard templates |
| Страх «сломать» automation | Случайные кнопки «run» | **No** orchestration controls v0.1 |

---

## Сценарии дня (draft flows)

### Утро — обзор

1. Login (mock v0.1) → Main Cockpit.
2. Взгляд на **right signal rail** (deadlines, overdue).
3. Leads block — есть ли новые заявки.
4. MARS / bots — display-only OK / attention.

### Работа с клиентом

1. Clients/Projects → выбор клиента.
2. Project Detail — ссылки на сайт, staging, WP-admin, Figma, repo.
3. Quick action (например «open staging») — mock handler v0.1.

### Конец месяца — recurring

1. Recurring monitor — SEO-отчёты, платежи, отчёты клиентам.
2. Эскалация WATCH → WARNING по календарю (sample data v0.1).

### Вечер — подготовка

1. Clipboard — скопировать handoff line для завтра.
2. Settings — переключить theme при необходимости.

---

## Информационная архитектура (связь с screen map)

Полная карта экранов: [screen-map-v0.1.md](screen-map-v0.1.md).

**Решение Phase 1:** Main Cockpit — **hub**; специализированные экраны (MARS Monitor, Signals) могут быть как отдельные views **или** крупные block-screens на hub — **финальный выбор на Phase 2 wireframes** (SAFE UNKNOWN).

---

## Non-goals (UX)

- Публичный landing / SEO-сайт студии (это отдельные сайты; HG — private cockpit).
- Multi-user RBAC, командные роли.
- Запуск MARS agents / n8n workflows из HG v0.1.
- Real-time chat с клиентами.

---

## Открытые вопросы (для Phase 2)

| Вопрос | Влияние |
|--------|---------|
| Hub-only vs multi-page navigation | Wireframes, routing |
| Mobile/tablet priority | Layout breakpoints |
| Плотность block-screens (compact vs airy) | Visual direction Phase 3 |
| Где живёт Project Detail — panel vs page | screen-map |

---

## SAFE UNKNOWN

- Реальные interview transcripts оператора — **не приложены**; notes основаны на charter задачи.
- Количество одновременных клиентов на экране — TBD.
- Язык UI (RU/EN mix) — TBD; docs RU, tech labels могут быть EN.

---

## Связанные документы

| Doc | Role |
|-----|------|
| [screen-map-v0.1.md](screen-map-v0.1.md) | Экраны и навигация |
| [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md) | Зоны layout |
| [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) | Типы block-screen |
| [admin-entry-and-future-crud-notes-v0.1.md](admin-entry-and-future-crud-notes-v0.1.md) | Admin-aware static prep |

---

*Last updated: 2026-05-20 — Phase 1 UX discovery foundation.*
