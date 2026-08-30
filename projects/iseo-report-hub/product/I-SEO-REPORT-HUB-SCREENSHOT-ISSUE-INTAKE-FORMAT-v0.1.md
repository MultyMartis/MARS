# i-SEO Report Hub — Screenshot Issue Intake Format v0.1

**Для кого:** Андрей  
**Назначение:** единый простой формат замечаний по скриншотам  
**Язык:** русский

---

## Шаблон (копировать)

```
Page: 
Screenshot: iseo-hub-YYYYMMDD-##_page-name.png
Problem: 
Expected: 
Priority: low / medium / high
Category: 
Comment: 
```

### Пример

```
Page: Клиентский предпросмотр /monthly-reports/1/preview
Screenshot: iseo-hub-20260821-09-client-preview.png
Problem: В шапке документа остался служебный английский текст
Expected: Только русский клиентский заголовок и период
Priority: high
Category: client report
Comment: Мешает показывать клиенту даже локально
```

---

## Категории (Category)

| Category | Когда ставить |
|----------|----------------|
| `text/content` | тексты, переводы, формулировки |
| `layout` | отступы, сетка, таблицы, «ломается» вид |
| `form` | поля, borders, labels, focus |
| `navigation` | меню, ссылки, «непонятно куда» |
| `warning/error` | баннеры, lock, empty, 404 |
| `client report` | preview / print документ |
| `export/share` | файлы отчёта, shares UI |
| `data/model` | странные данные, счётчики, статусы |
| `blocker` | нельзя продолжать работу / стыдно показывать |

Можно указать одну категорию. Если сомневаешься — `text/content` или `layout`.

---

## Приоритеты

| Priority | Смысл |
|----------|--------|
| `high` | мешает работе или клиентскому виду |
| `medium` | заметно, но можно жить |
| `low` | косметика / «было бы лучше» |

---

## Правила

1. Один шаблон = одно замечание (на одном скрине может быть несколько блоков).
2. Не вставляй пароли, токены share, полные checksum.
3. Если «всё ок» на экране — можно коротко: `Problem: нет / ок`.
4. После сбора замечаний — волна **Screenshot QA Triage 01**.
