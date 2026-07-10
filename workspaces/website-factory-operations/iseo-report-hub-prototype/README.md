# i-SEO Report Hub — статический прототип v0.4

**Статус:** только прототип / демо — **НЕ production**

---

## Что это

Self-contained static HTML/CSS/JS прототип **i-SEO Report Hub** в рамках prototype lane MARS Website Factory.

### v0.3 → v0.4

| v0.3 | v0.4 |
|------|------|
| Report Content Architecture + Type Block Matrix | **+ INTLSEO / i-seo.su inspired visual style** |
| Staged lifecycle (Final / W3 / W1) | **+ Рабочая панель SEO-специалиста** (`specialist-workspace.html`) |
| Weekly / monthly structured views | **+ Чек-листы, тексты, KPI, evidence mockups, readiness panel** |
| Dashboard + review queue | **+ Ясное разделение: workspace = заполнение, weekly/monthly = structured view** |

### Архитектура (без изменений)

- Автономный статический HTML/CSS/JS **без Gulp**
- **Не требуется** `npm install`, сборка или build-шаг
- Откройте `index.html` в браузере

## Чего это НЕ является

- **Не** production-код
- **Не** WordPress, PHP, MySQL
- **Не** n8n, API или backend
- **Не** реальные клиентские данные или секреты
- **Не** реальная загрузка файлов или скриншотов

Весь контент — **санитизированные демо-данные** (`*.example`).

---

## Платформа

**Платформа не выбрана.** Реализация **не начата**.

---

## Demo projects (v0.4 staged)

| Проект | Тип | Стадия | Client report |
|--------|-----|--------|---------------|
| **Регион Сервис** | Local / Regional | Final published (100%) | ✓ Доступен |
| **Industrial Tools** | E-commerce | Week 3 active, monthly draft (58%) | ✗ Не готов |
| **Инжиниринг Сервис** | Service / Corporate | Week 1 active, monthly shell (12%) | ✗ Не готов |

---

## Страницы

| Файл | Экран |
|------|--------|
| `index.html` | Dashboard — lifecycle matrix, project cards |
| `specialist-workspace.html` | **Рабочая панель SEO** — заполнение отчёта (чек-листы, тексты, KPI, evidence) |
| `project.html` | Project detail — type block list, lifecycle |
| `weekly.html` | Structured weekly view — W1/W2/W3 states (заполнение → workspace) |
| `monthly.html` | Structured monthly view — type block matrix + anatomy |
| `client-report.html` | Client report — gate для B/C |
| `review.html` | Review queue — staged statuses |

---

## Как открыть

`X:\AI MARS\workspaces\website-factory-operations\iseo-report-hub-prototype\index.html`

**Без build. Без npm.**

### Рекомендуемый порядок review (оператор)

1. `index.html` — dashboard, lifecycle matrix, v0.4 overview
2. `specialist-workspace.html` — **главный новый экран** — заполнение отчёта
3. `monthly.html` — structured monthly view, type block matrix
4. `client-report.html?project=local` — полный client report
5. `weekly.html` — structured weekly view, связь с workspace
6. `review.html` — queue: B primary, C not in queue

---

## Готовность

**SEO feedback: not yet** — отложено до operator visual/content review v0.4.

---

## Структура файлов

```
iseo-report-hub-prototype/
  README.md
  index.html
  specialist-workspace.html
  project.html
  weekly.html
  monthly.html
  client-report.html
  review.html
  assets/
    css/styles.css
    js/demo.js
```

Нет `node_modules`. Нет build toolchain. Нет Gulp.
