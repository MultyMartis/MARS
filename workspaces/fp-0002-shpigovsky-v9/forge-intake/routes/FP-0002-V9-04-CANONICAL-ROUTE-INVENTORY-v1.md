# FP-0002 V9-04 Canonical Route Inventory v1

**Date:** 2026-07-02 | **Count:** 31 | **Excluded:** `/uslugi/genotipirovanie/`

| Route | title | classification | status | template | object | blocker |
|-------|---|---|---|---|---|---|
| `/` | Главная | full | APPROVED_FULL | TPL-FRONT-PAGE | page | — |
| `/uslugi/` | Услуги | full | APPROVED_FULL | TPL-SERVICES-HUB | page | — |
| `/uslugi/zavisimosti/` | Зависимости | full | APPROVED_FULL | TPL-SERVICE-SUBDIVISION | page | — |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | Лечение алкогольной зависимости | full | APPROVED_FULL | TPL-SERVICE-LEAF | page | — |
| `/uslugi/zavisimosti/profilakticheskiy-analiz/` | Профилактический анализ | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/zavisimosti/specialistam/` | Специалистам | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/psihicheskoe-zdorovie/` | Психическое здоровье | placeholder | PLACEHOLDER | TPL-SERVICE-SUBDIVISION | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/psihicheskoe-zdorovie/depressiya/` | Депрессия | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/psihicheskoe-zdorovie/ptrs/` | ПТСР | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/` | Эмоциональное выгорание | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/` | Тревожные расстройства | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/psihicheskoe-zdorovie/rasstroystva-sna/` | Расстройства сна | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/psihicheskoe-zdorovie/travma/` | Травма | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | Расстройства пищевого поведения | placeholder | PLACEHOLDER | TPL-SERVICE-SUBDIVISION | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/` | Нервная анорексия | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/` | Нервная булимия | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/` | Компульсивное переедание | placeholder | PLACEHOLDER | TPL-SERVICE-LEAF | page | PLACEHOLDER_CONTENT_PENDING |
| `/o-centre/` | О центре | full | APPROVED_FULL | TPL-INSTITUTIONAL | page | — |
| `/o-centre/o-nas/` | О нас | placeholder | PLACEHOLDER | TPL-INSTITUTIONAL | page | PLACEHOLDER_CONTENT_PENDING |
| `/o-centre/programma-lecheniya/` | Программа лечения | placeholder | PLACEHOLDER | TPL-INSTITUTIONAL | page | PLACEHOLDER_CONTENT_PENDING |
| `/o-centre/galereya-o-dome/` | Галерея о доме | placeholder | PLACEHOLDER | TPL-INSTITUTIONAL | page | PLACEHOLDER_CONTENT_PENDING |
| `/o-centre/specialistam/` | Специалистам | placeholder | PLACEHOLDER | TPL-INSTITUTIONAL | page | PLACEHOLDER_CONTENT_PENDING |
| `/o-centre/rodstvennikam/` | Родственникам | placeholder | PLACEHOLDER | TPL-INSTITUTIONAL | page | PLACEHOLDER_CONTENT_PENDING |
| `/otzyvy/` | Отзывы | full | APPROVED_FULL | TPL-REVIEWS | page | — |
| `/blog/` | Статьи | full | APPROVED_FULL | TPL-BLOG-ARCHIVE | posts_page | — |
| `/blog/nazvanie-stati/` | Название статьи | full | APPROVED_FULL | TPL-BLOG-SINGLE | post | — |
| `/kontakty/` | Контакты | full | APPROVED_FULL | TPL-CONTACTS | page | — |
| `/privacy-policy/` | Политика конфиденциальности | legal | LEGAL_DEMO_DOCUMENT | TPL-LEGAL | page | LEGAL_DEMO_TOKENS |
| `/user-agreement/` | Пользовательское соглашение | legal | LEGAL_DEMO_DOCUMENT | TPL-LEGAL | page | LEGAL_DEMO_TOKENS |
| `/consent-personal-data/` | Согласие на обработку персональных данных | legal | LEGAL_DEMO_DOCUMENT | TPL-LEGAL | page | LEGAL_DEMO_TOKENS |
| `/cookie-files-policy/` | Политика Cookie-файлов | legal | LEGAL_DEMO_DOCUMENT | TPL-LEGAL | page | LEGAL_DEMO_TOKENS |

## Invariants

- `/uslugi/zavisimosti/` is canonical Dependencies hub (not genotyping).
- Alcohol dependence leaf is **full-page exception** — not collapsed to generic placeholder.
- Blog fixture `/blog/nazvanie-stati/` is migration reference, not sole article.
- Legal routes carry DEMO production blockers.
- 18 placeholder routes preserve hierarchy and approved placeholder copy.
