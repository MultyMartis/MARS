# FP-0002 V6 URL Map

**Authority:** XLSX `Предварит структура и спрос.xlsx` (see audit) + operator canonical header/footer  
**Updated:** 2026-06-23

## Core routes

| Page | URL | Static build file | Active nav key |
| ---- | --- | ----------------- | -------------- |
| Главная | `/` | `dist/index.html` | — |
| Услуги (hub) | `/uslugi/` | `dist/uslugi.html` | `uslugi` (operator label: Лечение и профилактика) |
| Генотипирование | `/uslugi/genotipirovanie/` | — | — |
| Специалисты | `/specyalisty/` | — | — |
| О центре | `/o-centre/` | — | — |
| Отзывы | `/otzyvy/` | — | — |
| Статьи | `/blog/` | — | — |
| Контакты | `/kontakty/` | — | — |

## Service tree (confirmed slugs)

| URL | Label |
| --- | ----- |
| `/uslugi/zavisimosti/` | Зависимости и пристрастия |
| `/uslugi/psihicheskoe-zdorovie/` | Психическое здоровье |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | Расстройства пищевого поведения |
| `/uslugi/genotipirovanie/` | Генотипирование |

## About subpages

| URL | Label |
| --- | ----- |
| `/o-centre/o-nas/` | О нас |
| `/o-centre/programma-lecheniya/` | Программа лечения |
| `/o-centre/galereya-o-dome/` | Галерея о доме |
| `/o-centre/specialistam/` | Специалистам |
| `/o-centre/rodstvennikam/` | Родственникам |
| `/o-centre/intervyu-i-smi/` | Интервью и СМИ |

## Legal

| URL | Label | Source |
| --- | ----- | ------ |
| `/pravovaya-informaciya-pilzovatelyu/` | Правовая информация (hub) | XLSX |
| `/privacy-policy/` | Политика конфиденциальности | Operator footer |
| `/user-agreement/` | Пользовательское соглашение | Operator footer |
| `/consent-personal-data/` | Согласие на обработку ПДн | Operator footer |
| `/cookie-files-policy/` | Политика Cookie-файлов | Operator footer |

## WordPress policy

- User navigation: `/slug/` only — no `.html`, no `#`, no `localhost`
- Allowed exceptions: `tel:`, `mailto:`, `data-modal-open`, `data-fancybox`
- Static preview files do not define public URLs

## Conflicts / SAFE UNKNOWN

| Topic | Status |
| ----- | ------ |
| Header «Услуги» vs «Лечение и профилактика» | Operator label preserved; URL `/uslugi/` |
| Legal hub XLSX vs discrete footer pages | Both retained; WP IA reconciliation deferred |
| Messenger social URLs | SAFE UNKNOWN — remain `#` |
