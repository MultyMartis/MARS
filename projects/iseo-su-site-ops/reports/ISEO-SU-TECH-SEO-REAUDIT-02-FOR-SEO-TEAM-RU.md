# Повторный технический и SEO-аудит i-seo.su

**Дата контура:** 2026-09-04 (`tech-seo-reaudit-02` / `20260904-163451`)  
**Сайт:** https://i-seo.su/  
**Режим:** только проверка (без правок production / меню / sitemap)

**Важно:** расположение новых страниц в меню пока **НЕ** менялось. Решение по menu/navigation ждём от **Никиты**.

---

## 1. Что проверили

- Свежий crawl всего production (не опирались только на аудит августа 2026).
- HTTP-здоровье URL, битые внутренние ссылки и ассеты.
- Sitemap (`sitemap.xml`, `sitemap-static.xml`, `wp-sitemap.xml`) и `robots.txt`.
- Indexability / canonical / title / description / H1.
- Внутреннюю перелинковку и «сиротские» страницы.
- Новые city / niche / USA / UAE / webinar-лендинги.
- Формы и согласие на ПДн, безопасность обработчиков (read-only).
- Регрессию first-screen (`height:100vh`) на 14 новых SEO-лендингах.
- Сравнение с прошлым tech SEO audit / SEO review pack.

---

## 2. Что сейчас работает нормально

- Сайт отдаёт страницы: **нет** page-level 4xx/5xx в crawl.
- Битых внутренних HTML-ссылок: **0**.
- Ссылок на редиректы (link-to-redirect): **0** (раньше было массово — закрыто).
- Корневой sitemap и дочерние static/WP — **живые** (старые битые child refs закрыты).
- Static sitemap: **139** URL, локальная completeness **PASS** (разрыв 0).
- 5 городских + 7 нишевых лендингов: **200**, в sitemap, формы с согласием, без overlap first-screen.
- USA / UAE / Webinar: **200**, индексны, но **намеренно** вне sitemap/меню (политика оператора).
- Webinar: дата **10 сентября 2026**, время **19:00 МСК**; старых дат на live — **0**.
- Lead-формы: незакрытых согласий на живых lead-surfaces — **0**.
- `test_mode` выключен; основной получатель — `nikel007i33@yandex.ru`.

---

## 3. Критические проблемы

**Нет критических** (доступность сайта / обвал индексации / провал lead-форм или routing получателя не обнаружены).

---

## 4. Высокий приоритет

1. **Относительные CSS на страницах авторов блога**  
   Пути вида `/blog/author/css/...` → 404 (6 случаев в выборке).  
   Риск: поломанная вёрстка/скрипты плагинов на author-архивах.  
   Нужен тех. фикс путей (не SEO-решение).

2. **Битый `/img/logo.svg` (404)**  
   Один явный broken image; проверить, кто на него ссылается, и заменить/убрать.

---

## 5. Средний приоритет

- **Canonical missing / mismatch** на большом слое статики и части WP (порядок ~156 missing на indexable; ~120 mismatch). Это известный backlog SEO-review — **не ухудшился радикально**, missing чуть лучше.
- **SM-NONINDEX** (~54): URL в sitemap с noindex — пересмотреть состав WP sitemap / политику.
- **Title duplicates** (семья блога «Блог - INTLSEO Studio» и др.).
- **H1 missing** на report-hub / query-вариантах.
- **Слабая перелинковка** у части indexable URL с 0 crawler-inlinks (авторы, slash-варианты; USA/UAE/webinar — отдельно как политика).

---

## 6. Низкий приоритет

- Длинные title (>70).
- Missing / duplicate meta description (частично те же семьи, что раньше).
- Content images без alt (review; декоративный пустой alt не считать авто-багом).
- Крупные JPG кейсов (~1.5–1.7 MB) — performance red flag.
- Неполный Open Graph на многих лендингах (часто есть только `og:image`).

---

## 7. Вопросы, где нужно решение SEO

| Тема | Комментарий |
|------|-------------|
| Нужны ли city/niche в **глобальном меню** | Сейчас нет; хабы и body-links есть. Решение — Никита / SEO. |
| Продвигать ли USA / UAE через sitemap/меню | Сейчас direct-only / policy. |
| Webinar в sitemap | Сейчас campaign direct-only — ок, если так задумано. |
| Чистка CANON-MISSING / MISMATCH | Технически возможно, но нужна SEO-приоритизация семейств URL. |
| SM-NONINDEX backlog | Решение: убрать из sitemap vs снять noindex. |

---

## 8. Новые страницы

| Группа | Статус HTTP | Sitemap | Меню | Заметки |
|--------|-------------|---------|-------|---------|
| 5 городов | 200 | да | нет | Cross-link с `b-regionakh` + между собой |
| 7 ниш | 200 | да | нет | Ссылки с `/services/seo.html` |
| USA / UAE | 200 | нет | нет | Политика; не «сломанные сироты» |
| Webinar | 200 | нет | нет | Дата 10.09.2026; campaign landing |

First-screen / low-height: **регрессий overlap нет**.

---

## 9. Перелинковка

- Города: hub ↔ city ↔ city — ожидаемо.
- Ниши: hub `seo.html` → niche — ожидаемо; в глобальном nav ниш нет.
- USA / UAE / Webinar: 0 crawler-inlinks — **ожидаемо при текущей политике**.
- Есть indexable URL только из sitemap / со слабыми inlinks — в очереди review, не всё дефект.

---

## 10. Sitemap / индексация

- Root sitemap → static + WP children: OK.
- Static **139**, completeness OK.
- USA / UAE / Webinar **намеренно** отсутствуют.
- Часть WP URL в sitemap с noindex — backlog.

---

## 11. Canonical

- Самоканоникал есть на части HTML.
- Большой слой **без** canonical и слой **mismatch** — тот же класс проблем, что в SEO Review Pack 01.
- Canonical → 404 / redirect: **не** найдено в этом контуре.

---

## 12. Title / Description / H1

- Missing title: 0.
- Дубли title: в основном блог/шаблоны.
- Meta missing: ~23 (как ранее).
- H1 missing: report-hub и варианты; multiple H1: 0.

---

## 13. Изображения / alt

- 1 broken: `logo.svg`.
- Большие слайды кейсов — compression candidate.
- Alt: разделять декоративные и контентные.

---

## 14. Формы

- 12 handlers; HMAC; test_mode OFF; получатель nikel only.
- Lead consent: **0** uncovered.
- Search UI (offers/glossary) без consent — не lead PII.

---

## 15. Что осталось от прошлого аудита

| Было | Сейчас |
|------|--------|
| Битые sitemap children | **Закрыто** |
| Completeness static 139 | **PASS** |
| LINK-TO-REDIR массово | **0** |
| Относительные blog images | почти закрыто; остатки ассетов |
| CANON / TITLE / META backlog | **живёт**, без критического ухудшения |
| New landings / webinar | **добавлены и здоровы** |

---

## 16. Что рекомендуем делать дальше

**A. Безопасные техфиксы (без меню):** относительные CSS author; `logo.svg`; опционально сжатие huge JPG.  
**B. SEO-решения:** canonical backlog; SM-NONINDEX; title-dup блога.  
**C. Меню:** ждать Никиту (city / niche / international / webinar).  
**D. Контент-review:** alt, OG family, слабые inlinks.  
**E. Без действия:** USA/UAE/Webinar вне sitemap при текущей политике; search forms без consent.

Полный внутренний отчёт и CSV findings — в репозитории `projects/iseo-su-site-ops/` (Reaudit 02).
