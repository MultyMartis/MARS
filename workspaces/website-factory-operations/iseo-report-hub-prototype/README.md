# i-SEO Report Hub — статический прототип Website Factory v0.1

**Статус:** только прототип / демо — **НЕ production**

---

## Что это

Этот workspace — **self-contained static HTML/CSS/JS** прототип **i-SEO Report Hub**, созданный в рамках prototype lane MARS Website Factory. Он визуализирует админский workflow, структуру клиентского web-отчёта и цели для будущей реализации на WordPress (i-seo.su).

### Архитектура v0.1 (важно)

- Текущая **v0.1 демка** — автономный статический HTML/CSS/JS **без Gulp**.
- Прототип относится к **Website Factory prototype lane** и совместим с ним по назначению.
- **Не требуется** `npm install`, сборка или build-шаг — откройте `index.html` в браузере.
- Полноценный gulp workspace (по образцу Website Factory) может быть отдельным этапом позже, если оператор решит мигрировать или пересоздать демо.
- Текущая цель — быстрый визуальный обзор и UX-валидация для SEO-специалистов.

## Чего это НЕ является

- **Не** production-код
- **Не** WordPress-плагин, тема или PHP
- **Не** подключено к n8n, API или любому backend
- **Не** использует реальные клиентские данные, учётные записи или секреты
- **Не** развёрнуто и не хостится

Весь контент — **только фейковые/санитизированные демо-данные**.

---

## Исходная документация

- [I-SEO-REPORT-HUB-WEBSITE-FACTORY-PROTOTYPE-CHARTER-v0.1.md](../../../projects/iseo-report-hub/product/I-SEO-REPORT-HUB-WEBSITE-FACTORY-PROTOTYPE-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-WEBSITE-FACTORY-DEMO-BRIEF-v0.1.md](../../../projects/iseo-report-hub/product/I-SEO-REPORT-HUB-WEBSITE-FACTORY-DEMO-BRIEF-v0.1.md)
- [I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md](../../../projects/iseo-report-hub/product/I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md)
- [I-SEO-REPORT-HUB-WEB-REPORT-STRUCTURE-v0.1.md](../../../projects/iseo-report-hub/product/I-SEO-REPORT-HUB-WEB-REPORT-STRUCTURE-v0.1.md)

---

## Страницы

| Файл | Экран |
|------|--------|
| `index.html` | Панель SEO-специалиста |
| `project.html` | Проект и отчётный цикл |
| `weekly.html` | Редактор недельного чекпоинта |
| `monthly.html` | Редактор месячного отчёта |
| `client-report.html` | Клиентский web-отчёт |
| `review.html` | Очередь проверки (вид проверяющего) |

---

## Как открыть

Откройте `index.html` в локальном браузере (`file://` или через простой static server). **Без build-шага. Без npm install.**

Рекомендуемый порядок просмотра:

1. `index.html` — панель специалиста
2. `project.html` — обзор отчётного цикла
3. `weekly.html` — редактор недельного чекпоинта
4. `monthly.html` — редактор месячного отчёта
5. `review.html` — очередь проверки
6. `client-report.html` — клиентский отчёт

---

## Демо-данные

- **Клиент:** Демо-клиент Industrial Tools
- **Сайт:** demo-tools.example
- **Проект:** SEO продвижение интернет-магазина
- **Профиль:** E-commerce
- **Период:** Июль 2026

---

## Следующие шаги

1. Визуальный обзор оператором русскоязычной локализованной демки
2. Доработка прототипа по обратной связи **ИЛИ**
3. Переход к спецификации WordPress-реализации / MVP charter

---

## Структура файлов

```
iseo-report-hub-prototype/
  README.md
  index.html
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
