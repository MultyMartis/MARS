# ISEO-SU TECH REPAIR WAVE 01 — отчёт (RU)

**Task ID:** `ISEO-SU-SITE-OPS-TECH-REPAIR-WAVE-01`  
**Дата:** 2026-09-04  
**Статус:** COMPLETE

---

## Что было сломано

1. **CSS на страницах авторов блога.** В re-audit 02 зафиксировано **6** битых CSS-запросов вида `/blog/author/css/...` и `/blog/author/libs/...`.
2. **Картинка `/img/logo.svg`.** Ответ сервера **HTTP 404**.

SEO-бэклог (canonical, title, meta, H1, alt, OG, меню) **не входил** в эту волну и **не менялся**.

---

## Почему author pages искали CSS по неверному nested path

- URL вида `/blog/author/{slug}` **не** открывают отдельный шаблон автора WordPress.
- Они отвечают **301** на главную `https://i-seo.su/`.
- После редиректа отдаётся HTML главной (`page-home.php`).
- В шаблоне главной стили были подключены **относительно документа**: `href="css/..."`, `href="libs/..."`.
- Краулер, резолвя пути относительно исходного `/blog/author/...`, получал `/blog/author/css/...` → **404**.
- Реальные файлы уже лежали и открывались по корневым путям `/css/*` и `/libs/*` (HTTP 200).

Исправление сделано **в одном источнике** — `page-home.php`: пути приведены к корневым `/css/...` и `/libs/...`. Копировать CSS в `/blog/author/css/` не требовалось и не делалось.

---

## Что было с `/img/logo.svg`

- Живой URL `/img/logo.svg` давал **404**.
- Актуальный логотип сайта уже есть: `/img/logo-intl.svg` → **200**.
- Единственный значимый эмиттер битой ссылки — статический `blog.html` (`src="img/logo.svg"`).

Выбран **MODEL A (stale reference)**: ссылка перенаправлена на `/img/logo-intl.svg`. Файл `logo.svg` заново не рисовали и не выдумывали.

---

## Как исправлено

| Объект | Действие |
|--------|----------|
| `production-source/theme/iseoblog/page-home.php` | root-relative CSS/libs |
| `production-source/static-html/blog.html` | logo → `/img/logo-intl.svg` |
| Production | scoped backup + SFTP deploy тех же двух файлов |
| Проверка | targeted recrawl: broken author CSS **0**, broken logo refs **0** |

Backup: `X:\AI MARS\local\sites\iseo-su-production\_tech-repair-wave-01\20260904T155608Z\`

---

## Что не трогали

- title / description / H1 / canonical / robots  
- sitemap  
- menu / navigation  
- SEO review backlog  
- контент, формы, дизайн логотипа  

---

## Как перепроверено

- Preflight: volume `AI WS`, branch `mars/canonical-post-recovery`, foreign WIP сохранён.
- Deploy checksum: production = MARS source.
- Все 6 author URL: CSS root-relative, nested `/blog/author/css/` нет.
- Smoke: `/`, `/blog/`, пост, категория — без CSS-регрессии.
- `/img/logo-intl.svg` = 200; живых ссылок на битый `logo.svg` = 0.

Подробности: [EVIDENCE](../ISEO-SU-TECH-REPAIR-WAVE-01-EVIDENCE-v1.md) · [REPORT](REPORT-ISEO-SU-SITE-OPS-TECH-REPAIR-WAVE-01.md).
