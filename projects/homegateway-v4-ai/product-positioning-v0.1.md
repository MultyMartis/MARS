# HomeGateway v4.ai — product positioning v0.1

**Статус:** **DRAFT** · **PLANNING**  
**Версия:** v0.1

---

## One-liner

**HomeGateway v4.ai** = **Personal Operational Cockpit** — приватный веб-кокпит оператора веб-студии для AI-assisted production ecosystem, клиентских операций и MARS-connected infrastructure.

---

## Для кого

- Владелец / главный оператор веб-студии.
- Один primary user (личный кокпит); не публичный SaaS и не multi-tenant продукт на текущем этапе.

---

## Какую проблему решает

| Проблема | Как HG помогает (целевое состояние) |
|----------|-------------------------------------|
| Разрозненные закладки и админки | Единая панель частых ссылок и ресурсов |
| Потеря контекста по клиентам | Экраны client/project с быстрым доступом |
| Пропуск дедлайнов | Мониторы active/recurring/overdue с уровнями сигнала |
| Непрозрачность ботов и automation | Display-only блоки статуса n8n/Telegram/MARS |
| Медленные повторяющиеся действия | Quick actions и clipboard blocks |

---

## Позиционирование в экосистеме

```text
[ Operator ]
     │
     ▼
┌─────────────────────────────────────┐
│  HomeGateway v4.ai (Cockpit UI)     │  ← surface layer (display + quick actions)
└──────────┬──────────────────────────┘
           │ planned reads / future control prep
     ┌─────┴─────┬──────────┬──────────────┐
     ▼           ▼          ▼              ▼
  MARS       n8n flows   Telegram      Client sites /
  (display)  (status)    bots          WPilot / Factory packs
```

HomeGateway — **верхний слой для человека**, не замена нижних систем.

---

## Тип продукта (канонические формулировки)

**Использовать:**

- operational surface layer
- cockpit UI
- display/control preparation layer
- documentation-first project (текущая стадия)
- Personal Operational Cockpit

**Не использовать:**

- autonomous system
- deployed runtime (как факт)
- active MARS control plane
- production orchestrator
- replacement for MARS / ORCA / WPilot / MetaBOT / GitGuard
- finished dynamic application

---

## Конкурентная дистанция (внутри MARS)

| Система | Отличие от HomeGateway |
|---------|------------------------|
| **MARS core / mars-runtime** | Контракты и эксперименты; HG только **потребляет display**, не исполняет агентов |
| **ORCA** | PPC operational toolkit; HG может **ссылаться**, не дублировать PPC-логику |
| **WPilot** | WordPress admin workflow; HG — ссылки на сайты/admin, не CMS runtime |
| **MetaBOT** | n8n multi-workflow; HG — статус/сигналы, не workflow engine |
| **Website Factory** | Производство сайтов; HG — обзор проектов/доставки, не factory orchestration |

---

## MVP narrative (v0.1)

**STATIC-FIRST:** оператор открывает mock-login → главный кокпит из block-screens → видит образцы данных → использует sample quick actions / clipboard → видит точку входа Admin (disabled/mock) → переключает dark/light theme foundation.

Ценность MVP: **проверить UX-плотность и визуальный язык**, не интеграции.

---

## Будущее (FUTURE-INTEGRATION only)

- Локальное хранилище / JSON / API для данных кокпита.
- Admin CRUD.
- MARS export / display API.
- n8n bridge, Telegram bot registry.
- Lead/request feed для Web Studio Polygon и MetaCODE.

---

## SAFE UNKNOWN

- Публичный URL, SSL, auth (OAuth vs basic vs magic link) — **не выбрано**.
- Mobile-first vs desktop-only приоритет — **требует UX discovery (Phase 1)**.
- Один домен vs subdirectory install — **не определено**.

---

*Last updated: 2026-05-20.*
