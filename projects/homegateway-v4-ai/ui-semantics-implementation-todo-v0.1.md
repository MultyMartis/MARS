# HomeGateway v4.ai — UI semantics implementation TODO v0.1

**Статус:** **DRAFT** · **IMPLEMENTATION GAP LIST** · post–MVP v1 stabilization  
**Назначение:** зафиксировать semantic gaps между текущим MVP v1 и каноникой из [ui-semantics-and-interaction-system-v0.1.md](ui-semantics-and-interaction-system-v0.1.md).

**Не является:** redesign backlog, layout rewrite, permission на изменение shell geometry.

**Связанные:** [ui-semantics-and-interaction-system-v0.1.md](ui-semantics-and-interaction-system-v0.1.md) · [reports/mvp-v1-stabilization-report.md](reports/mvp-v1-stabilization-report.md) · [desktop-viewport-shell-rule-v0.1.md](desktop-viewport-shell-rule-v0.1.md)

---

## Core principle

Все нижеописанные gaps должны закрываться **внутри существующего shell**:

- без layout changes;
- без CSS redesign;
- без изменений shell geometry;
- без изменений rhythm tokens;
- без декоративного наполнения `#main_area`.

---

## Priority recommendations

| Priority | Meaning |
|----------|---------|
| **P1** | Семантическая ошибка, искажающая meaning уже существующего UI |
| **P2** | Важное незавершенное interaction behavior |
| **P3** | Placeholder module, допустимый в MVP, но требующий дальнейшей operationalization |

---

## Implementation gaps

| Priority | Area | Current MVP gap | Canonical target |
|----------|------|-----------------|------------------|
| **P1** | Utility buttons | Используются literal labels `01`, `02`, `03` | Заменить на profile / settings / about-system controls с реальными icon meanings |
| **P1** | Project / tools indicators | Вместо semantic telemetry используются fake stars / placeholder affordances | Ввести 4 operational indicators с mapping 5/6/7/8 |
| **P1** | Semantic icons | Отсутствует финальная семантическая icon layer для utility и status controls | Подключить real semantic icons без изменения layout |
| **P1** | `#main_area` loading | Нет реальной загрузки active operational content | Клик по project/tool context должен загружать рабочее содержимое в `#main_area` |
| **P2** | Favorites pagination | `#01` и slide hook существуют как placeholder, но pagination semantics не реализована полноценно | Реализовать page cycling, current page indicator, infinite loop |
| **P2** | Favorites hover secondary action | Нет вторичного hover action для shortcut rows | Добавить canonical secondary action типа open in new/background tab |
| **P2** | Topbar semantics expression | Tabs already exist, but their operational workspace behavior is still mostly visual/static | Привязать tabs к реальным workspace contexts и active underline logic |
| **P3** | Monitor cards | Monitor uses placeholder logic and demo content | Ввести real signal card structure: title, short description, timestamp, severity, actions, status |
| **P3** | `A4` module | `A4` остается placeholder health tile | Определить агрегированный health indicator semantics и data composition |

---

## Detailed notes

### 1. Utility buttons still use literal `01/02/03` labels

Числа были diagram markers, а не UI copy.  
Это нужно исправить в первую очередь, потому что текущая реализация искажает meaning интерфейса на уровне чтения.

### 2. Fake stars instead of operational indicators

Stars создают ложное впечатление decorative rating system.  
Канонически здесь должны быть telemetry values:

- entity count
- active problems
- active tasks / processes
- completed / resolved

### 3. Missing semantic icons

MVP допускает placeholder shapes, но дальнейшая стабилизация требует понятной semantic iconography для:

- profile
- settings
- about system
- theme
- project/tool functions
- status/health helpers

### 4. Favorites pagination not implemented

Сейчас есть только partial hook/placeholder behavior.  
Нужно реализовать:

- смену набора favorites pages;
- бесконечный цикл;
- current page indicator semantics;
- calm replacement behavior без redesign shell.

### 5. Hover secondary action not implemented

Favorites должны поддерживать secondary shortcut behavior на hover.  
Текст кнопки может быть гибким, но тип действия должен быть каноническим.

### 6. Monitor cards still placeholder logic

Сигнальные карточки существуют как structural placeholder, но пока не выражают завершенный operational contract:

- нет формализованного timestamp usage;
- нет явного severity discipline;
- status/action semantics остаются demo-level.

### 7. `A4` module still placeholder

Правый health block должен стать compact aggregated health module, а не произвольным мини-графиком.

### 8. No operational loading into `#main_area` yet

Пустой canvas был корректным stabilization step, но следующий этап должен подключить реальный active workspace content.  
При этом запрещено компенсировать отсутствие логики декоративными static widgets.

---

## Recommended rollout order

1. Исправить semantic misread controls: utility buttons + project/tools indicators.
2. Подключить real operational loading into `#main_area`.
3. Реализовать favorites pagination and secondary hover action.
4. После этого доработать signal feed semantics и `A4` aggregated health module.

---

## Constraint reminder

Все эти задачи должны выполняться как **semantics / behavior implementation**, а не как повод для:

- нового визуального языка;
- изменений grid/layout;
- модификации `#main_area` geometry;
- внедрения animation-heavy effects;
- пересмотра spacing rhythm.

---

*Last updated: 2026-05-25 — implementation gaps listed after MVP v1 stabilization.*
