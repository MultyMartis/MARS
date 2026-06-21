# Scroll Process Timeline Pattern

**ID:** `WF-SCROLL-PROCESS-TIMELINE`  
**Status:** **documented** — approved **Interactive Commercial Pattern** from Triumph Cargo Taxi (`/services/gruzovoe-taksi/`) operator validation on DEV.  
**Not:** runtime enforcement, automated scroll QA, or modification of live site code.

**Date:** 2026-06-18  
**Evidence:** DEV implementation on Triumph project — scroll-driven order-process block with route line, progress line, branded vehicle PNG, step cards, and reverse-on-scroll-up; passed operator review.

**Related:** [registries.md](registries.md) §3 · [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) §11 · [frontend-production-rules-v0.md](frontend-production-rules-v0.md)

---

## Назначение

Показывать **путь клиента** через понятный пошаговый процесс — заявка → расчёт → выполнение — как часть контента страницы услуги, а не как декоративный баннер.

### Когда использовать

| Vertical | Примеры |
|----------|---------|
| **Логистика / доставка / перевозки** | Грузовое такси, курьер, междугородние перевозки |
| **Сервисные компании** | Выезд мастера, аренда техники, обслуживание |
| **Монтаж / строительство** | Этапы работ от замера до сдачи |
| **Любая услуга с линейным процессом** | 3–5 шагов с понятной последовательностью |

### Когда не использовать

- Процесс не линейный или шаги неочевидны без HITL-контента.
- Нет брендированного визуала (транспорт / объект / инструмент) — SVG-иконка часто выглядит как декор, не как часть услуги.
- Страница не даёт достаточной scroll-дистанции для плавного progress (см. Engineering Lessons §4).

---

## Состав паттерна

| Element | Role |
|---------|------|
| **Track** | Статическая линия маршрута — геометрическая основа движения |
| **Progress Line** | Заполняемая линия, синхронизированная с scroll progress |
| **Vehicle** | Брендированный PNG (транспорт / объект услуги), движущийся по треку |
| **Step Cards** | Карточки шагов процесса, привязанные к позициям на маршруте |
| **Scroll Progress** | Единый `progress` (0–1), управляемый scroll пользователя |
| **Reverse Scroll Support** | При прокрутке вверх progress и позиции **уменьшаются** — анимация обратима |

---

## UX Rule

**Пользователь должен управлять анимацией.**

| Запрещено | Предпочтительно |
|-----------|-----------------|
| Autoplay | Scroll-driven animation |
| Бесконечные циклы | Progress-based movement |
| Декоративное движение без участия пользователя | Reverse-on-scroll-up |

Анимация — **иллюстрация процесса**, не отвлечение. Блок должен читаться как контент, помогающий объяснить услугу.

---

## Triumph Case Study

| Aspect | Detail |
|--------|--------|
| **Кейс** | Грузовое такси → страница услуги `/services/gruzovoe-taksi/` |
| **Решение** | 3 шага процесса; PNG Газель с брендингом; движение по маршруту; движение связано со scroll |
| **Результат** | Выглядит как часть контента; не как рекламный баннер; не раздражает; помогает объяснить услугу |

---

## Engineering Lessons

### Ошибка №1 — движение относительно ширины элемента

**Плохо:**

```css
transform: translateX(calc(var(--progress) * 100%));
```

**Проблема:** машина движется относительно **собственной ширины**, а не длины маршрута.

**Правильно:** движение относительно **ширины трека** (track width minus vehicle width), например через `calc(var(--progress) * (100% - <vehicle-width>))` или эквивалент в JS с измерением track.

---

### Ошибка №2 — SVG вместо брендированного PNG

| Плохо | Правильно |
|-------|-----------|
| SVG-грузовик как иконка | PNG с брендингом компании (логотип, цвет, узнаваемая модель) |

SVG выглядел как **иконка**, не как часть коммерческого предложения.

---

### Ошибка №3 — старт от viewport-позиции блока

**Проблема:** на больших мониторах при входе блока в viewport машина сразу оказывалась **в середине пути**.

**Правильно:** `setProgress(0)` при загрузке; начальная позиция — **нулевая**, независимо от того, где блок попал в viewport при первом paint.

---

### Ошибка №4 — слишком короткая scroll-дистанция

**Проблема:** машина перемещалась слишком быстро — progress менялся на малом scroll delta.

**Финальное решение:** scroll distance **≈ 800px** (или эквивалент по проекту) для плавного, контролируемого движения.

---

## Frontend Rules

Для блоков этого паттерна:

| Rule | Detail |
|------|--------|
| **Scoped CSS** | Стили только в scope блока — без утечки в тему |
| **Scoped JS** | Инициализация по root-селектору блока; без глобальных side effects |
| **Изоляция от темы** | Не менять глобальные токены, layout shell, другие секции |
| **Изоляция от других страниц** | Код не влияет на страницы без этого блока |
| **WPBakery Raw HTML** | Допускается вставка через Raw HTML при соблюдении scope и отсутствии конфликтов с builder CSS |

Наследует [frontend-production-rules-v0.md](frontend-production-rules-v0.md) — edit source only, no `dist` manual edits.

---

## QA Checklist

| Check | Expectation |
|-------|-------------|
| **Старт** | Vehicle и progress line в **нулевой** позиции при загрузке |
| **Scroll вниз** | Progress и vehicle движутся вперёд синхронно |
| **Scroll вверх** | Progress и vehicle **откатываются** (reverse) |
| **Синхронность** | Progress line и vehicle совпадают по progress на всех кадрах |
| **Desktop** | Корректная геометрия трека и карточек |
| **Mobile** | Читаемость карточек; трек не ломает layout |
| **Большие мониторы** | Нет «прыжка» в середину пути при первом появлении |
| **Layout shift** | Нет CLS от загрузки PNG или пересчёта progress |

**REPORT line (when scroll process timeline is in scope):**

```text
SCROLL PROCESS TIMELINE — PASS | partial (list) | FAIL | N/A | SAFE UNKNOWN
```

---

## Website Factory Classification

| Field | Value |
|-------|-------|
| **Category** | Interactive Commercial Pattern |
| **Complexity** | Medium |
| **Reuse** | High |
| **Platforms** | WordPress · OpenCart · Static HTML · Website Factory |

**Registry:** [registries.md](registries.md) §3 — Commercial Pattern Library · `pattern_id`: `scroll_process_timeline`

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-18 | v1 — lesson extracted from Triumph Cargo Taxi DEV (`/services/gruzovoe-taksi/`) after operator approval |
