# HomeGateway v4.ai — signal system draft v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 1

Черновик операционных сигналов и уровней для дедлайнов/задач. **Не** automation engine, **не** alerting product.

**UX context:** [ux-discovery-notes-v0.1.md](ux-discovery-notes-v0.1.md) · **Display:** `zone-rail-right`, block-screens `hg-deadline-*`

---

## Назначение

HomeGateway отображает **операционные сигналы** для человека: срочность дедлайнов, состояние систем, будущие события MARS/bots.

На v0.1 — **визуальные уровни на sample data**; доставка из внешних систем — **FUTURE-INTEGRATION**.

---

## Логика близости дедлайна (human-readable)

| Состояние | Операторское ощущение | Уровень (draft) |
|-----------|----------------------|-----------------|
| Далеко от срока | Спокойно, в плане | **INFO** |
| Приближается | Стоит периодически смотреть | **WATCH** |
| Близко к сроку | Риск срыва | **WARNING** |
| Срок сегодня | Особое внимание | **CRITICAL** + state **due-today** |
| После срока | Не исчезает до закрытия | **OVERDUE** (persistent) |

**Automation** расчёта — Phase 6+; v0.1 — ручные `data-hg-signal-level` в sample data.

---

## Уровни сигнала (канонический набор)

| Level | Смысл | Визуал (draft) |
|-------|-------|----------------|
| **INFO** | Информирование | Muted badge, calm |
| **WATCH** | Наблюдение | Accent outline |
| **WARNING** | Предупреждение | Warning token |
| **CRITICAL** | Критично сегодня/завтра | Critical token + due-today styling |
| **OVERDUE** | Просрочено | Overdue token, persistent row |

### Визуальные состояния (дополнительно к level)

| State | Описание |
|-------|----------|
| **due-today** | Специальное выделение в календарный день срока (может совпадать с CRITICAL) |
| **overdue** | Отдельная стойкость строки до manual resolve в admin |

---

## Примеры задач (sample content для static MVP)

| Пример | Тип | Typical level (illustrative) |
|--------|-----|------------------------------|
| Ежемесячный SEO-отчёт для клиента | recurring / client report | INFO → WATCH → WARNING по дате |
| Recurring payment / check | recurring | WATCH |
| Дедлайн этапа проекта (launch, delivery) | project deadline | WARNING / CRITICAL |
| MARS update checkpoint (doc review) | operational / MARS-related | INFO / WATCH |
| Client follow-up (call, approval) | ad hoc deadline | WATCH / WARNING |
| Bot/system maintenance (restart n8n, token rotate) | system task | INFO / WATCH |

Все примеры — **sample labels** в static HTML; не live MARS/n8n.

---

## Типы мониторов дедлайнов

| Monitor | Содержимое | module_id |
|---------|------------|-----------|
| **active deadlines** | Разовые сроки | `hg-deadline-active` |
| **recurring monthly** | Ежемесячные задачи | `hg-deadline-recurring` |
| **client reports** | Отчёты клиентам | часть recurring |
| **remaining days** | Число дней в строке | field в signal list |
| **danger by proximity** | Эскалация INFO → CRITICAL | manual/sample v0.1 |

---

## Draft proximity rules (для Phase 6 automation — не v0.1)

| Days remaining | Suggested level |
|----------------|-----------------|
| > 14 | INFO |
| 8–14 | WATCH |
| 3–7 | WARNING |
| 0 (today) | CRITICAL + due-today |
| < 0 | OVERDUE |

**SAFE UNKNOWN:** рабочие дни vs календарные; timezone — operator locale TBD.

---

## Сигналы систем (display-only, future)

| Source | Signal examples | Integration phase |
|--------|-----------------|-------------------|
| **MARS** | Pack lane, maintenance mode hint | Phase 7 — **display-only** |
| **n8n** | Last run, error flag | Phase 7 |
| **Telegram bots** | Online/offline | Phase 7 |
| **Leads** | New request count | Phase 7 |
| **Health checks** | HTTP probe | Phase 7–8 |

**Запрет v0.1:** кнопки «run workflow», «invoke agent».

---

## Визуальное сопоставление (theme)

Семантические токены — [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md):

- `--hg-signal-info` … `--hg-signal-overdue`
- `--hg-danger` для destructive hints (не путать с OVERDUE без label)

Сигнал **не** только цвет: icon + text label + level code.

---

## Поведение (human-operated)

1. OVERDUE снимается оператором через admin (future) — **не** auto-clear.
2. MARS governance escalation — только display + link to docs.
3. Секреты **не** в clipboard signal blocks.

---

## SAFE UNKNOWN

- Push notifications — не решено.
- Snooze / dismiss — Phase 6 admin feature TBD.
- Event history timeline — Phase 7.

---

*Last updated: 2026-05-20 — Phase 1 examples and proximity logic.*
