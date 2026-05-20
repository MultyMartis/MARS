---
id: ideabox-wf-visual-density-budget
status: draft
type: idea
created: 2026-05-16
related:
  - ../../projects/mars-website-factory/page-blueprint-contract-v0.md
  - ../../projects/mars-website-factory/service-landing-template-v0.md
  - ../../projects/mars-website-factory/block-registry-v0.md
tags:
  - website-factory
  - blueprint
  - visual-hierarchy
  - landing
---

# Идея

Ввести для Website Factory явную сущность **visual density rules** / **visual density budget**: ограничения «насколько плотно» можно набить контентом ключевые зоны страницы, чтобы генерация (ИИ) не размывала иерархию и не превращала верх страницы в «простыню».

# Зачем

Наблюдаемый паттерн: модель часто **перегружает hero и верхние секции** — много строк, вторичных акцентов и блоков в одном экране. Последствия:

- падает **visual hierarchy** (неясно, что главное);
- теряется **воздух** и восприятие качества;
- **CTA** теряется среди шума;
- лендинг выглядит перегруженным уже на первом экране.

Цель идеи — не «красивые правила ради правил», а **переносимый бюджет плотности** по типам секций, чтобы blueprint/handoff/промпты могли ссылаться на одни и те же ограничения.

# Заметки

- Кандидаты на отдельные «бюджеты» или профили плотности: **hero**, **feature blocks**, **trust**, **CTA sections** (список открыт для уточнения).
- Возможная интеграция: описывать density как часть **page blueprint contract** (поля, лимиты, severity при превышении) — **гипотеза**, не решение.
- Связь с уже существующим наблюдением про раздувание hero в шаблоне сервисного лендинга см. `service-landing-template-v0.md` (таблица рисков / scope creep).
- Статус: **только идея** — без утверждённой схемы полей, без изменений governance и без обязательности для агентов до отдельного решения человека.
