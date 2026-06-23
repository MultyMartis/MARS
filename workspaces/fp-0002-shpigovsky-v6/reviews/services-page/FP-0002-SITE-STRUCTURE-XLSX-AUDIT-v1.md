# FP-0002 SITE STRUCTURE XLSX AUDIT

## Source file

| Field | Value |
|-------|-------|
| Task path | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/02_CONTENT/ Предварит структура и спрос.xlsx` |
| Audited copy | `C:\AI MARS STORAGE\website-factory\snapshots\FP-0002-PRE-M2-OPS-2026-06-13-v1\FP-0002-SHPIGOVSKY\INCOMING\02_CONTENT\Предварит структура и спрос.xlsx` |
| Workspace INCOMING `02_CONTENT/` | **EMPTY** at audit time — Excel not present in active intake tree |
| Edit policy | **READ-ONLY** — source not modified |

## Workbook sheets

| Sheet | Used range | Role |
|-------|------------|------|
| `Структура` | A1:E53 (53 rows × 5 cols) | Site hierarchy, URLs, page labels by depth |
| `Спрос Яндекс` | A1:H53 | Search-demand volumes per service phrase |

## Pages discovered

**52 production URL nodes** on sheet `Структура` (including placeholders). **L0–L4** depth columns map to URL path segments.

Top-level (L1) pages with confirmed URLs:

| Label (XLSX) | URL |
|--------------|-----|
| Главная | `/` |
| Услуги | `/uslugi/` |
| Специалисты | `/specyalisty/` |
| О центре | `/o-centre/` |
| Отзывы | `/otzyvy/` |
| Статьи | `/blog/` |
| Контакты | `/kontakty/` |
| Правовая информация | `/pravovaya-informaciya-pilzovatelyu/` |

## Hierarchy

```
/ (Главная)
├── /uslugi/ (Услуги)
│   ├── /uslugi/zavisimosti/ (Зависимости и пристрастия)
│   │   ├── …/lechenie-alkogolnoy-zavisimosti/
│   │   ├── …/lechenie-narkoticheskoy-zavisimosti/ (+ L4 sub-leaves)
│   │   └── …/lechenie-povedencheskoy-zavisimosti/ (+ L4 sub-leaves)
│   ├── /uslugi/psihicheskoe-zdorovie/ (+ L3 leaves)
│   ├── /uslugi/rasstroystva-pischevogo-povedeniya/ (+ L3 leaves)
│   └── /uslugi/genotipirovanie/
├── /specyalisty/ (+ profile slugs)
├── /o-centre/ (+ 6 subpages)
├── /otzyvy/
├── /blog/ (+ article instances)
├── /kontakty/
└── /pravovaya-informaciya-pilzovatelyu/
```

## Service pages

| Level | Example URL | Label |
|-------|-------------|-------|
| Hub | `/uslugi/` | Услуги |
| Section L2 | `/uslugi/zavisimosti/` | Зависимости и пристрастия |
| Section L2 | `/uslugi/psihicheskoe-zdorovie/` | Психическое здоровье |
| Section L2 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | РПП |
| Direction L2 | `/uslugi/genotipirovanie/` | Генотипирование |
| Leaf L3+ | `…/lechenie-alkogolnoy-zavisimosti/` etc. | Per-row labels |

## Utility and legal pages

| Page | URL (XLSX) |
|------|------------|
| Legal hub | `/pravovaya-informaciya-pilzovatelyu/` (note trailing `//` in raw cell) |
| Privacy / consent / cookies | **Not separate rows in XLSX** — footer links confirmed in operator source |

## Proposed URL map

Canonical relative paths (trailing slash, no `.html`):

- Home: `/`
- Services hub: `/uslugi/`
- Genotyping: `/uslugi/genotipirovanie/`
- Specialists: `/specyalisty/`
- About: `/o-centre/`
- Reviews: `/otzyvy/`
- Blog: `/blog/`
- Contacts: `/kontakty/`
- Legal hub: `/pravovaya-informaciya-pilzovatelyu/`
- Operator legal slugs (preserved): `/privacy-policy/`, `/consent-personal-data/`, `/user-agreement/`, `/cookie-files-policy/`

## Main menu map

**XLSX / design authority (5-item main nav):** Услуги → `/uslugi/` · О центре → `/o-centre/` · Отзывы → `/otzyvy/` · Статьи → `/blog/` · Контакты → `/kontakty/`

**Operator canonical header (7 items):** Лечение и профилактика → `/uslugi/` · Генотипирование → `/uslugi/genotipirovanie/` · Специалисты → `/specyalisty/` · О центре → `/o-centre/` · Отзывы → `/otzyvy/` · Статьи → `/blog/` · Контакты → `/kontakty/`

**Conflict:** label «Услуги» (XLSX) vs «Лечение и профилактика» (operator header). **Resolution:** preserve operator labels; map services hub URL `/uslugi/` to operator item «Лечение и профилактика».

## Footer menu map

| Column | Heading | Links (sample) |
|--------|---------|----------------|
| 1 | Услуги | `/uslugi/zavisimosti/`, `/uslugi/psihicheskoe-zdorovie/`, `/uslugi/rasstroystva-pischevogo-povedeniya/`, `/uslugi/genotipirovanie/` |
| 2 | О центре | `/o-centre/o-nas/`, `/o-centre/programma-lecheniya/`, … |
| 3 | Информация | `/privacy-policy/`, `/user-agreement/`, `/consent-personal-data/`, `/cookie-files-policy/` |

## Duplicates and conflicts

| Issue | Detail |
|-------|--------|
| Placeholder rows | L4 «Название» ×2 under dependencies; L3 «Название» ×3 under mental health; specialist placeholders 4–6 |
| Duplicate blog URL | Three article rows share `/blog/nazvanie-stati/` |
| Trailing spaces in URLs | `genotipirovanie/ `, `otzyvy/ `, `kontakty/ `, legal hub `// ` in raw cells — normalized to `/slug/` in implementation |
| Header label vs XLSX | See Main menu map |
| Legal sub-pages | XLSX has hub only; operator footer has discrete legal slugs |

## SAFE UNKNOWN

- Messenger `href="#"` targets (Telegram/WhatsApp/Max) — not in XLSX
- Search button behavior — not in XLSX
- Exact meta description for services hub page — not confirmed in content pack
- Task mockup filenames `Услуги - раздел.png` / mobile variant — **NOT FOUND** in workspace intake; authority fallback: Figma frame «Услуги хаб» + `FP-0002-BLOCK-INVENTORY-v1.md` G-SERVICE scroll order

## WordPress migration notes

- Static Gulp output: `dist/uslugi.html` for preview; user-facing hrefs use `/uslugi/` without `.html`
- Services hub maps to WordPress page slug `uslugi` (parent of service CPT/taxonomy per future WP charter)
- Operator header preserved — WP menu sync must not overwrite labels without operator sign-off
- Legal URLs already WordPress-shaped; reconcile `/pravovaya-informaciya-pilzovatelyu/` hub vs discrete policy pages at WP integration
