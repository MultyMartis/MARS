# HomeGateway v4.ai — UI semantics and interaction system v0.1

**Статус:** **DRAFT** · **CANONICAL SEMANTICS** · post–MVP v1 stabilization  
**Назначение:** формализовать канонические **операционные значения** элементов HG shell: вкладки, индикаторы, utility controls, favorites, monitor, status module и правила поведения `#main_area`.

**Не является:** visual redesign task, layout rewrite, component redesign, animation charter, shell geometry spec.

**Связанные:** [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) · [desktop-viewport-shell-rule-v0.1.md](desktop-viewport-shell-rule-v0.1.md) · [viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md) · [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) · [information-priority-model-v0.1.md](information-priority-model-v0.1.md) · [reports/mvp-v1-stabilization-report.md](reports/mvp-v1-stabilization-report.md)

---

## Canonical assertion

> **HomeGateway shell elements are operational semantics, not decorative chrome.**

После стабилизации MVP v1 базовые элементы интерфейса нужно читать как **рабочие значения и поведенческие контракты**, а не как «визуальные украшения dark dashboard».

Это означает:

- tabs в `top_bar` = **workspace contexts**;
- project/tool indicators = **telemetry**, не decorative stars;
- favorites = **operational shortcuts**, не marketing links;
- monitor/status modules = **signal and health surfaces**, не ornamental side cards;
- `#main_area` = **active work surface only**.

---

## `top_bar`

### Каноническая роль

Верхняя панель содержит **глобальный operational context switch**, а не декоративные вкладки браузерного типа.

### Навигационные вкладки

| Tab | Каноническая роль | Операционное назначение |
|-----|-------------------|-------------------------|
| **Общий** | Default workspace context | Общий cockpit / базовый operational overview |
| **Системы** | Systems context | Состояние систем, инфраструктуры, runtime-модулей |
| **Фокус** | Focus context | Узкая рабочая поза для одной активной задачи / проекта |
| **Сигналы** | Signals context | Приоритетные события, уведомления, tactical feed |

### State model

| State | Meaning | UI rule |
|-------|---------|---------|
| **Inactive** | Контекст доступен, но не открыт | Низкий контраст, без active underline |
| **Active** | Текущий workspace context | Выделение текста + active underline |
| **Hover** | Исследование доступного переключения | Краткий акцент без подмены active state |

### Active underline logic

- underline обозначает **только текущий активный operational context**;
- underline не должен использоваться как декоративная линия под всеми вкладками;
- underline не «живет своей жизнью» отдельно от active state;
- в каждый момент активна **ровно одна** вкладка;
- переключение вкладки = **намеренная смена рабочего контекста**, а не cosmetic toggle.

### Operational rule

Эти вкладки **не являются декоративными tabs**.  
Это **operational workspace contexts**, которые управляют тем, какой тип работы загружается в shell, прежде всего в `#main_area`.

---

## Utility buttons

### Канонические значения

| Diagram marker | Каноническое значение | Роль |
|----------------|------------------------|------|
| **01** | **Профиль** | Доступ к профилю / identity controls |
| **02** | **Настройки** | Переход к interface/system settings |
| **03** | **О системе** | Информация о HG / environment / build state |
| **04** | **Переключение темы** | Theme mode toggle |

### Важное уточнение

Числовые метки `01`, `02`, `03`, `04` в исходной схеме были **только diagram markers**.  
Они **не являются** буквальным UI-текстом.

Текущая MVP v1 реализация с видимыми кнопками `01`, `02`, `03` семантически **некорректна** и позже должна быть заменена на реальные icon/buttons с понятным meaning.

### Future implementation notes

- заменить literal numeric labels на icon-first controls;
- сохранить tooltip / accessible label с явным meaning;
- `04` трактовать как theme toggle behavior, а не как числовую кнопку;
- не менять геометрию `top_bar` ради этой коррекции: меняется **семантическое выражение**, не layout.

---

## Project panel

### Каноническая роль

Project panel показывает список **операционных рабочих сущностей**, доступных для открытия в основном рабочем поле.

### Behavior of project row

Клик по строке проекта:

1. выбирает project context;
2. загружает project workspace в `#main_area`;
3. обновляет active state выбранной строки;
4. при необходимости синхронизирует связанные сигналы / status context.

### Canonical operational indicators

| Marker | Meaning | Definition |
|--------|---------|------------|
| **5** | **Entity count** | Количество first-level sections / modules / categories / folders only |
| **6** | **Active problems / issues** | Текущее число активных проблем, блокеров, ошибок, незакрытых issue |
| **7** | **Active tasks / processes** | Текущее число активных задач, процессов, workstreams |
| **8** | **Completed / resolved** | Число завершенных или закрытых единиц |

### Important clarification

Эти индикаторы **не являются декоративными stars**.  
Это **operational telemetry indicators**, которые должны сообщать оператору структуру и состояние проекта до открытия детального workspace.

Текущие MVP placeholder-stars нельзя считать финальным semantic contract.

### Severity logic recommendations

| Semantic tone | Recommended usage |
|---------------|-------------------|
| **neutral** | entity count, stable baseline, informational totals |
| **warning** | active problems / issue growth / degraded state |
| **processing** | active tasks / work in progress / ongoing execution |
| **success** | completed / resolved / healthy completion |

### Interaction rule

Row itself = primary action.  
Indicators = telemetry layer of the row, а не отдельный декоративный ornament.

---

## Project utility buttons

### Канонические значения

| Marker | Meaning | MVP state | Future role |
|--------|---------|-----------|-------------|
| **9** | **Project settings** | disabled / non-active | config, structure, project-specific controls |
| **10** | **Project archive** | disabled / non-active | snapshots, historical workspaces, archived states |

### MVP interpretation

В MVP v1 эти controls допустимо держать как **disabled / non-active placeholders**, если они явно не обещают работающую функциональность.

---

## Favorites system

### Каноническая роль

Favorites — это **operational shortcuts**, а не декоративная строка бренд-ссылок.

Типовые примеры:

- Yandex
- Google
- YouTube
- Mail
- VK

### Canonical behavior

- favorites дают быстрый доступ к часто используемым внешним ресурсам;
- набор ссылок может меняться по operator habit и workflow;
- текстовый label может быть адаптирован;
- поведение shortcut остается каноническим, даже если конкретный label меняется.

### Hover behavior

На hover появляется **secondary action** типа:

- open in new tab;
- open in background tab;
- аналогичное быстрое вторичное действие.

Текст secondary action может отличаться.  
**Канонично именно поведение**, а не конкретная формулировка label.

---

## Favorites slide controller

### Каноническая роль

Кнопка со star marker и индикатором `#01` **не декоративна**.

Это **favorites pagination controller**.

### Required behavior

- циклически переключает rows/pages избранного;
- использует **infinite loop** behavior;
- выполняет smooth replacement transition при смене набора ссылок;
- показывает текущий page index.

### Page indicator semantics

`#01` означает **текущую страницу favorites**, а не декоративный hash-label.

### MVP note

Если в MVP есть только hook или простое переключение placeholder state, это еще не означает, что pagination semantics реализована полностью.

---

## Tools panel

### Каноническая роль

Секции:

- **Системы**
- **Процессы**
- **Роботы**
- **Вики**

трактуются как **tool categories / modules**, а не как стилизованный второй список.

### Indicator rule

Tools panel использует **ту же operational indicators logic**, что и project rows:

- entity / module scope;
- active problems;
- active tasks / processes;
- completed / resolved.

Разница только в типе сущности: project row представляет проект, tools row представляет категорию инструмента / operational module.

---

## Monitor panel

### Каноническая роль

Monitor — это **operational signal feed**.

### Signal classes

| Marker | Meaning |
|--------|---------|
| **A1** | critical signal |
| **A2** | notification / update |
| **A3** | operational event |

### Expected signal card structure

Каждая карточка сигнала должна содержать:

- title
- short description
- timestamp
- severity
- actions
- status

### Behavioral intent

Monitor не должен деградировать в generic news/inbox column.  
Это лента рабочих сигналов с короткими действиями и ясной степенью важности.

---

## Status system panel

### Каноническая роль

Status panel — это **global operational health module**.

### Left side

Левая часть показывает **runtime/system metrics**:

- compute / load
- memory / storage
- network / I/O
- аналогичные базовые метрики окружения

### Right side: `A4`

`A4` — **aggregated health indicator**.

Он может содержать:

- mini charts
- health score
- operational state
- stability metrics

### Semantic rule

`A4` не должен быть декоративной chart toy-вставкой.  
Это агрегированный модуль состояния, который сообщает общее здоровье среды в компактной форме.

---

## `#main_area`

### Каноническая роль

`#main_area` — это **dynamic operational workspace**.

Сюда загружается активный контент:

- project workspace;
- systems workspace;
- focus workspace;
- signal detail workspace;
- другой реальный operational content по выбранному context.

### Strict rule

**Do NOT:**

- decorate;
- overload;
- fill with fake dashboard art;
- place static widgets there.

В `#main_area` может появляться **только активный operational content**.

### MVP interpretation

Пустой placeholder в MVP v1 допустим как stabilization state, если он честно показывает, что workspace content еще не подключен.  
Но финально `#main_area` должен стать рабочим контейнером, а не витриной декоративных блоков.

---

## Design philosophy

### From visual concept to operational interface system

HomeGateway эволюционирует:

- из dark dashboard concept
- в structured operational UI framework

Это смещение означает переход от «красивой схемы cockpit-like UI» к **согласованной operational semantics system**.

Ключевые опоры:

- **rhythm system** — единый ритм spacing и плотности;
- **operational hierarchy** — shell zones имеют разные роли внимания;
- **semantic indicators** — цифры, метки и статусы выражают смысл, а не ornament;
- **interaction semantics** — click, hover, active, disabled читаются как рабочее поведение;
- **unified spacing language** — spacing поддерживает иерархию, а не случайную визуальную декоративность.

---

## Scope guardrails

Этот документ фиксирует **смысл и behavior rules**, но не разрешает:

- менять layout;
- перестраивать shell geometry;
- модифицировать `#main_area` в декоративный dashboard;
- менять spacing rhythm tokens;
- вводить animation/glow systems как отдельную задачу.

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Final icon set for utility buttons | Требует отдельной icon/system formalization |
| Exact pagination transition style for favorites | Behavior canon defined; implementation variant TBD |
| Formula for `A4` aggregated health | Placeholder semantics known; metric composition future |
| Exact project indicator rendering shape | Meaning fixed here; final visual carrier may evolve without layout redesign |

---

*Last updated: 2026-05-25 — canonical UI semantics formalized after MVP v1 stabilization.*
