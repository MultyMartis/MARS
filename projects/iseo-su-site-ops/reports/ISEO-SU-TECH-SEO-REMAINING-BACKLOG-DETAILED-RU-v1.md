# ОСТАВШИЕСЯ ТЕХНИЧЕСКИЕ И SEO-ЗАМЕЧАНИЯ ПО I-SEO.SU

**Задача:** ISEO-SU-SITE-OPS-TECH-SEO-BACKLOG-EXTRACTION-01  
**Дата извлечения:** 2026-08-24  
**Режим:** READ / ANALYZE / REPORT ONLY — без фиксов, без production mutations  
**Источник истины по находкам:** `audits/tech-seo/ISEO-SU-TECH-SEO-FINDINGS-v1.csv` + evidence/отчёты аудита 2026-08-21  
**Сверка статуса:** CURRENT-STATE, HIGH-FIX-WAVE-01, STATIC-SITEMAP-COMPLETENESS-FIX  

**Важно про счётчики аудита:** в исходном отчёте опубликовано **MEDIUM 6 + LOW 8 + REVIEW 14 = 28 сигналов**.  
`REVIEW 14` — это **не** третья независимая корзина severity с отдельными ID, а статус **`REVIEW NEEDED`** у тех же **14 уникальных finding_id** (ровно 6 MEDIUM + 8 LOW).  
Уникальных открытых ID бэклога: **14**. Сумма корзин для hard-check: **28**.

---

## 1. Краткий итог

| Корзина исходного аудита | Количество |
|--------------------------|-----------:|
| MEDIUM (severity) | **6** |
| LOW (severity) | **8** |
| REVIEW (status = REVIEW NEEDED) | **14** |
| Сумма корзин (сигналы) | **28** |
| Уникальных finding_id в бэклоге | **14** |

| Текущая классификация (уникальные ID) | Кол-во | ID |
|--------------------------------------|-------:|----|
| Реально открыты для решения (не CLOSED) | **14** | все ниже |
| Требуют SEO-решения / согласования | **11** | CANON-MISSING, CANON-MISMATCH, SM-MISSING-INDEXABLE, SM-NONINDEX, TITLE-DUP, ORPHAN-CRAWLER, TITLE-LONG, META-MISSING, META-DUP, IMG-ALT, OG-MISSING |
| Выглядят как нормальное / низкоприоритетное поведение tool-поверхностей или декоратива | **2–3 кандидата** | H1-MISSING; частично TITLE-DUP (пагинация); частично SM-NONINDEX (offers); частично IMG-ALT |
| Требуют повторной проверки (устаревший масштаб после фиксов sitemap) | **1** | SM-MISSING-INDEXABLE |
| Технически закрыты после аудита (не входят в 28) | **2 HIGH** | SM-CHILD-404, IMG-BROKEN |
| Static completeness defect | **CLOSED** | не re-open |

Production mutations в этой задаче: **0**. Fixes applied: **0**.

---

## 2. MEDIUM

### [CANON-MISSING] Отсутствует canonical на content-like страницах

**Что найдено:**  
На content-like HTTP 200 страницах отсутствует `link rel=canonical`. В evidence указано, что многие статические `.html` marketing-страницы могут не иметь canonical по дизайну шаблона.

**Где:**  
Смешанные типы (MIXED): статика, услуги, кейсы и др. Sample: `https://i-seo.su/`; также `home.html`, `services.html`, `cases.html`, `contacts.html`, `about.html`, `reviews.html`, `partners.html` и др.

**Масштаб:**  
**162** URL (affected_count).

**Почему это проблема:**  
Без self-canonical поисковик сам выбирает предпочтительный URL; при наличии twin-страниц (`/` vs `home.html` и т.п.) возможны дубли сигналов. Аудит классифицировал как MEDIUM / REVIEW NEEDED, confidence MEDIUM.

**Текущий статус:**  
`SEO_REVIEW` — не закрыто последующими fix-wave. Техническая реализация возможна после SEO-стратегии.

**Кто должен принять решение:**  
**MARS + SEO** — SEO задаёт политику; Site Ops внедряет в шаблоны.

**Что предлагается сделать:**  
Добавить self-referencing canonical на шаблонах (recommended_fix_direction из CSV).

**Риск ложного срабатывания:**  
Средний: часть пропусков может быть историческим template design, а не «поломкой». Без SEO-политики массовый autofix нежелателен.

---

### [CANON-MISMATCH] Несовпадение canonical и self-URL

**Что найдено:**  
Canonical не совпадает с self-URL или target неразрешён (canonical/self mismatch or unresolved target).

**Где:**  
MIXED; sample `https://i-seo.su/blog/?sort=date-asc`; также варианты `sort=*`, `tags=*`, комбинации query на blog.

**Масштаб:**  
**117** URL.

**Почему это проблема:**  
Query-варианты блога могут канонизироваться иначе, чем ожидается SEO; риск индексации / склейки не тех URL. Severity MEDIUM, REVIEW NEEDED.

**Текущий статус:**  
`SEO_REVIEW` — открыто.

**Кто должен принять решение:**  
**MARS + SEO**.

**Что предлагается сделать:**  
Выровнять canonical с preferred URL (CSV).

**Риск ложного срабатывания:**  
Средний: для сортировок/фильтров blog mismatch часто ожидаем, если canonical указывает на «чистый» archive. Нужна SEO-политика, не слепой rewrite.

---

### [SM-MISSING-INDEXABLE] Indexable URL вне обнаруженных sitemap

**Что найдено:**  
Indexable crawled URLs отсутствуют в объединении обнаруженных sitemap. Аудит прямо предупреждает: может быть intentional dual-sitemap architecture; **не** авто-дублировать.

**Где:**  
MIXED. Sample исходного аудита: `home.html`, `blog.html`, `glossary/`, `report-hub/`, `services/ai-optimization*` и др.

**Масштаб (исходный аудит):**  
**197** URL.

**Почему это проблема:**  
Часть публичных страниц могла не попасть в sitemap → слабее discovery. После аудита подтверждён дефект **неполноты static allowlist** (54 SEO URL + 2 legal); он **закрыт** completeness-fix (static = **127**, gate = 0). Остаток gaps (WP/blog/home/report-hub и dual ownership) — зона REVIEW, не auto-merge.

**Текущий статус:**  
`CLOSED / RECHECKED` (TECH CLEANUP WAVE 01, 2026-08-24): raw gap **161**, eligible canonical gap **0** (query 149 + report-hub 8 + noncanonical 4). Исторический count=197 сохранён как audit history.

**Кто должен принять решение:**  
**MARS + SEO**.

**Что предлагается сделать:**  
1) Пересчитать gaps после 127 static.  
2) Решить ownership surfaces.  
3) Не дублировать static ↔ WP автоматически.

**Риск ложного срабатывания:**  
Высокий для исходного count=197: цифра **устарела** после completeness fix. **НУЖНА ПОВТОРНАЯ ПРОВЕРКА** остатка.

---

### [SM-NONINDEX] В sitemap попали noindex / non-indexable URL

**Что найдено:**  
URL из sitemap классифицированы как noindex/non-indexable. Evidence: likely includes offer CPT / intentional noindex surfaces из wp-sitemap.

**Где:**  
MIXED. Sample: `tariff-calc`, `offers`, `offer/*` (в т.ч. тестовые/КП).

**Масштаб:**  
**52** URL (совпадает с INDEXABILITY CONFLICTS ≈54 в сводке).

**Почему это проблема:**  
Sitemap обычно для indexable; конфликт сигнал/интент. Может быть осознанно (offers закрыты robots `/offer/*`).

**Текущий статус:**  
`SEO_REVIEW` — открыто; возможный кандидат на EXPECTED для offers после SEO-подтверждения.

**Кто должен принять решение:**  
**SEO** (политика); внедрение — MARS при необходимости.

**Что предлагается сделать:**  
Убрать из sitemap **или** сделать indexable намеренно (CSV).

**Риск ложного срабатывания:**  
Высокий для offer-поверхностей: robots disallow `/offer/*` описан как expected behavior в evidence.

---

### [TITLE-DUP] Дублирующие title

**Что найдено:**  
Одинаковые `<title>` на разных URL. Крупнейший кластер: title blog archive ~**119** URL (pagination/category likely). Отдельно — report-hub query variants. В сводке: ~10 групп / ~161 URL involvements; в CSV affected_count=20 (сэмпл групп).

**Где:**  
MIXED. Sample: `blog/`, `blog`, `/`, `home.html`, report-hub workspace/weekly с query.

**Масштаб:**  
Группы дублей; крупнейший кластер ~119 blog archive URLs.

**Почему это проблема:**  
Слабая дифференциация в SERP для «разных» URL. Для пагинации/рубрик дубль title часто ожидаем.

**Текущий статус:**  
`SEO_REVIEW`.

**Кто должен принять решение:**  
**SEO**.

**Что предлагается сделать:**  
Дифференцировать title где страницы действительно distinct; pagination may be expected (CSV).

**Риск ложного срабатывания:**  
Высокий для blog pagination/category — аудит сам помечает как возможное expected.

---

### [ORPHAN-CRAWLER] Crawler-level «сироты»

**Что найдено:**  
URL видны через sitemap/crawl, но **0** внутренних inlink в графе обхода. Явно: **НЕ** истина Search Console.

**Где:**  
MIXED. Sample: `offers`, `offer/*` КП и др.

**Масштаб:**  
**57** URL.

**Почему это проблема:**  
Слабая внутренняя discoverability, если страница должна быть в nav. Не доказательство «невидимости» для Google.

**Текущий статус:**  
`SEO_REVIEW`.

**Кто должен принять решение:**  
**SEO**.

**Что предлагается сделать:**  
Добавить contextual internal links только если страницы должны быть discoverable via nav (CSV).

**Риск ложного срабатывания:**  
Высокий: crawler orphan ≠ GSC orphan; offers могут быть намеренно слабо перелинкованы.

---

## 3. LOW

### [LINK-TO-REDIR] Внутренние ссылки на URL с редиректом

**Что найдено:**  
Внутренние `<a>` указывают на URL, которые редиректят (не на final URL). Цепочек ≥2 hop в crawl: **0**.

**Где:**  
MIXED. Sample: `blog/` и date-архивы blog (часто 301).

**Масштаб:**  
**129** внутренних ссылок на redirecting URLs (при 136 URL с redirect history).

**Почему это проблема:**  
Косметический техдолг / лишний hop; не broken link (4xx/5xx внутренних документов = 0).

**Текущий статус:**  
`CLOSED` (TECH CLEANUP WAVE 01): residual = **0**.

**Кто должен принять решение:**  
**MARS / SITE OPS** (можно планировать отдельно после SEO-приоритетов).

**Что предлагается сделать:**  
Point anchors directly at final URLs (CSV).

**Риск ложного срабатывания:**  
Низкий по факту редиректов; низкая бизнес-критичность.

---

### [TITLE-LONG] Длинные title (>~70 символов)

**Что найдено:**  
Titles длиннее ~70 символов (SERP display heuristic).

**Где:**  
MIXED. Sample: `services/seo/kompleksnoe.html`, другие services/seo и длинные blog posts.

**Масштаб:**  
**24** URL.

**Почему это проблема:**  
Возможное обрезание в выдаче; не ошибка индексации.

**Текущий статус:**  
`SEO_REVIEW`.

**Кто должен принять решение:**  
**SEO**.

**Что предлагается сделать:**  
Shorten for SERP display if desired (CSV).

**Риск ложного срабатывания:**  
Средний: порог ~70 условный; длинный title не всегда вреден.

---

### [META-MISSING] Нет meta description

**Что найдено:**  
Отсутствует meta description на indexable 200. Evidence: not always critical.

**Где:**  
MIXED. Sample: `blog.html`, `glossary/`, `report-hub/**`.

**Масштаб:**  
**23** URL.

**Почему это проблема:**  
Google может сгенерировать snippet сам; качество сниппета на части URL может быть хуже.

**Текущий статус:**  
`SEO_REVIEW`.

**Кто должен принять решение:**  
**SEO** (какие URL важны); Site Ops — шаблоны.

**Что предлагается сделать:**  
Add where SERP snippet quality matters (CSV).

**Риск ложного срабатывания:**  
Средний: отсутствие description ≠ критический дефект.

---

### [META-DUP] Дубли meta description

**Что найдено:**  
Одинаковые meta description на разных URL. Evidence: distinct=2; urls=137.

**Где:**  
MIXED. Sample: `blog/`, `blog`, `/`, `home.html`.

**Масштаб:**  
**2** distinct duplicate descriptions, вовлечено **~137** URL; CSV affected_count=4 (сэмпл).

**Почему это проблема:**  
Слабая дифференциация сниппетов; часть может быть template default.

**Текущий статус:**  
`SEO_REVIEW`.

**Кто должен принять решение:**  
**SEO**.

**Что предлагается сделать:**  
Differentiate descriptions for distinct pages (CSV).

**Риск ложного срабатывания:**  
Средний: twin home/blog surfaces могут делить description осознанно или по шаблону.

---

### [H1-MISSING] Нет H1

**Что найдено:**  
Missing H1 на **5** URL: `varvara-new.php` + report-hub `client-report` query variants. Evidence: sibling/tool surfaces, **not** primary marketing templates. Multiple/empty H1 в crawl: **0**.

**Где:**  
Tool / Report Hub sibling routes.

**Масштаб:**  
**5** URL.

**Почему это проблема:**  
Для marketing — обычно важно; здесь поверхности помечены как tool/sibling, низкий marketing priority.

**Текущий статус:**  
`EXPECTED_BEHAVIOR` (как кандидат) / низкий приоритет; формально исходный status REVIEW NEEDED.

**Кто должен принять решение:**  
**НИЧЕГО НЕ ДЕЛАТЬ** по умолчанию; иначе MARS после SEO.

**Что предлагается сделать:**  
Ensure one clear H1 per content template — только если SEO/продукт требуют для этих tool URL.

**Риск ложного срабатывания:**  
Высокий относительно «сайт без H1»: затронуты не primary marketing templates.

---

### [IMG-HUGE] Крупные изображения (>1.5MB)

**Что найдено:**  
В image sample **2** файла >1.5MB.

**Где:**  
`/img/cases/seo_ai_cases/makita_01.png`, `maltipoo_01.png`.

**Масштаб:**  
**2** файла (выборка, не полный audit всех ассетов).

**Почему это проблема:**  
Вес страницы / lab performance; не broken image (HIGH image 404 уже CLOSED).

**Текущий статус:**  
`CLOSED` (TECH CLEANUP WAVE 01): makita/maltipoo below 1.5MB; residual = **0**.

**Кто должен принять решение:**  
**MARS / SITE OPS**.

**Что предлагается сделать:**  
Compress / serve modern formats (CSV).

**Риск ложного срабатывания:**  
Низкий по размеру файлов; выборка ограничена ≤250 image URL.

---

### [IMG-ALT] Пустые / отсутствующие alt

**Что найдено:**  
Страницы с множеством images missing/empty alt. Evidence: decorative empties may be OK; **do not mass-fix without design review**.

**Где:**  
MIXED. Sample: blog hubs, `about.html`, `bonuses.html`, services/cases pages.

**Масштаб:**  
**445** страниц (сигнал «много пустых alt»), не «445 битых картинок».

**Почему это проблема:**  
a11y / image SEO для контентных картинок; для декоративных empty alt часто норма.

**Текущий статус:**  
`SEO_REVIEW` (возможен EXPECTED для декоратива).

**Кто должен принять решение:**  
**SEO** (+ дизайн).

**Что предлагается сделать:**  
Add alt for content-significant images only (CSV). Без массового autofill.

**Риск ложного срабатывания:**  
Очень высокий при mass-fix: аудит прямо предупреждает.

---

### [OG-MISSING] Нет ключевых Open Graph тегов

**Что найдено:**  
Missing key OG tags (og:title/url/image) на important templates. Secondary priority unless template corruption (не наблюдалось как systemic blank titles).

**Где:**  
MIXED. Sample: `/`, `services.html`, report-hub, ряд services/*.

**Масштаб:**  
**97** URL.

**Почему это проблема:**  
Хуже превью в соцсетях/мессенджерах; на классический organic ranking влияние Indirect/secondary по формулировке аудита.

**Текущий статус:**  
`SEO_REVIEW` (внедрение — Site Ops после приоритета).

**Кто должен принять решение:**  
**MARS + SEO**.

**Что предлагается сделать:**  
Add og:title/url/image on high-value templates (CSV).

**Риск ложного срабатывания:**  
Средний: «important templates» — эвристика crawler; нужен SEO-приоритет списка.

---

## 4. REVIEW

Ниже — **те же 14 finding_id** со статусом исходного аудита **`REVIEW NEEDED`**.  
Это корзина **status**, не отдельный список новых ID. Severity у каждого указана в скобках.

### [CANON-MISSING] (MEDIUM) — см. §2

**Текущий статус:** `SEO_REVIEW`  
**Решение:** MARS + SEO — политика canonical для static/WP.

### [CANON-MISMATCH] (MEDIUM) — см. §2

**Текущий статус:** `SEO_REVIEW`  
**Решение:** MARS + SEO — preferred URL для blog query variants.

### [SM-MISSING-INDEXABLE] (MEDIUM) — см. §2

**Текущий статус:** `NEEDS_RECHECK` / частично SUPERSEDED (static 127)  
**Решение:** пересчёт gaps; не reopen static completeness.

### [SM-NONINDEX] (MEDIUM) — см. §2

**Текущий статус:** `SEO_REVIEW`  
**Решение:** SEO — sitemap vs noindex для offers/tools.

### [TITLE-DUP] (MEDIUM) — см. §2

**Текущий статус:** `SEO_REVIEW`  
**Решение:** SEO — нужны ли уникальные title пагинации/рубрик.

### [ORPHAN-CRAWLER] (MEDIUM) — см. §2

**Текущий статус:** `SEO_REVIEW`  
**Решение:** SEO — какие «сироты» реально нужны в nav.

### [LINK-TO-REDIR] (LOW) — см. §3

**Текущий статус:** `OPEN_TECH`  
**Решение:** MARS — якоря на final URL.

### [TITLE-LONG] (LOW) — см. §3

**Текущий статус:** `SEO_REVIEW`  
**Решение:** SEO — укорачивать ли title.

### [META-MISSING] (LOW) — см. §3

**Текущий статус:** `SEO_REVIEW`  
**Решение:** SEO — где обязателен description.

### [META-DUP] (LOW) — см. §3

**Текущий статус:** `SEO_REVIEW`  
**Решение:** SEO — разведение description.

### [H1-MISSING] (LOW) — см. §3

**Текущий статус:** `EXPECTED_BEHAVIOR` (кандидат)  
**Решение:** по умолчанию не трогать tool/hub.

### [IMG-HUGE] (LOW) — см. §3

**Текущий статус:** `OPEN_TECH`  
**Решение:** MARS — сжатие 2 файлов.

### [IMG-ALT] (LOW) — см. §3

**Текущий статус:** `SEO_REVIEW`  
**Решение:** SEO — alt только для значимых; без mass-fix.

### [OG-MISSING] (LOW) — см. §3

**Текущий статус:** `SEO_REVIEW`  
**Решение:** MARS + SEO — OG на high-value шаблонах.

---

## 5. Что уже исправлено после первоначального аудита

Кратко (не открывать снова):

| Тема | ID / дефект | Статус |
|------|-------------|--------|
| Root sitemap architecture | `SM-CHILD-404` | **CLOSED** (HIGH FIX WAVE 01) — `/sitemap.xml` → только `sitemap-static.xml` + `wp-sitemap.xml` |
| Blog relative images | `IMG-BROKEN` | **CLOSED** (HIGH FIX WAVE 01) — theme `/img/`; targeted recrawl PASS |
| Static sitemap completeness | дефект неполноты allowlist (54+2) | **CLOSED** — static **127** URL; completeness gate = 0 |
| Dual sitemap ownership model | `SM-DUAL-ARCH` (INFO) | **EXPECTED BEHAVIOR** (root repaired; split остаётся) |

---

## 6. Что MARS может исправить самостоятельно

Точные ID (после минимального operator/SEO OK или без семантических формулировок):

- **LINK-TO-REDIR** — якоря на final URL  
- **IMG-HUGE** — сжатие/modern formats для 2 sample files  

Условно (нужен короткий SEO-go / приоритет, но реализация техническая):

- **OG-MISSING** — после списка high-value templates  
- **CANON-MISSING** / **CANON-MISMATCH** — после политики preferred URL  
- **H1-MISSING** — только если SEO потребует для tool/hub  

---

## 7. Что нужно согласовать с SEO

| ID | Какое решение нужно |
|----|---------------------|
| **CANON-MISSING** | Нужен ли self-canonical на всех static `.html` / каких шаблонах |
| **CANON-MISMATCH** | Preferred URL для blog `?sort` / `?tags` / query variants |
| **SM-MISSING-INDEXABLE** | Ownership оставшихся non-static gaps; подтвердить что static 127 достаточен |
| **SM-NONINDEX** | Offers/tools: убрать из sitemap или оставить noindex осознанно |
| **TITLE-DUP** | Уникальные title для pagination/category blog и report-hub? |
| **ORPHAN-CRAWLER** | Какие из 57 URL должны получить inlink |
| **TITLE-LONG** | Укорачивать ли 24 title |
| **META-MISSING** | На каких из 23 URL обязателен description |
| **META-DUP** | Разводить ли template-default descriptions |
| **IMG-ALT** | Политика alt (только content-significant) |
| **OG-MISSING** | Приоритет OG vs контентные задачи; список шаблонов |

---

## 8. Что, вероятно, не требует исправления

| ID | Почему |
|----|--------|
| **H1-MISSING** | Tool/Report Hub sibling, не primary marketing (evidence аудита) |
| **TITLE-DUP** (часть) | Пагинация/рубрики blog — аудит: may be expected |
| **SM-NONINDEX** (часть offers) | `/offer/*` в robots disallow — expected commercial posture |
| **IMG-ALT** (декоратив) | Empty alt часто OK; mass-fix запрещён аудитом |
| **SM-DUAL-ARCH** | INFO / EXPECTED — не дефект бэклога MEDIUM/LOW |

---

## 9. Что нужно повторно проверить

| ID | Почему |
|----|--------|
| **SM-MISSING-INDEXABLE** | Исходный count=197 устарел после static completeness (127); **НУЖНА ПОВТОРНАЯ ПРОВЕРКА** residual gaps |
| **CANON-*** (опционально) | После любых будущих template changes — не сейчас как блокер |
| Mobile lab / CWV | В исходном аудите LIMITED / incomplete — вне 14 ID, но как lab gap |

---

## 10. Сводная таблица

| ID | Приоритет | Суть | Масштаб | Статус | Решение | Следующий шаг |
|----|-----------|------|---------|--------|---------|---------------|
| CANON-MISSING | MEDIUM | Нет canonical | 162 | SEO_REVIEW | MARS + SEO | Политика → шаблоны |
| CANON-MISMATCH | MEDIUM | Canonical ≠ self | 117 | SEO_REVIEW | MARS + SEO | Preferred URL blog query |
| SM-MISSING-INDEXABLE | MEDIUM | Indexable вне sitemap | 197*→0 eligible | CLOSED / RECHECKED | MARS | WAVE 01 recheck |
| SM-NONINDEX | MEDIUM | noindex в sitemap | 52 | SEO_REVIEW | SEO | Offers: keep or remove |
| TITLE-DUP | MEDIUM | Дубли title | ~119 cluster | SEO_REVIEW | SEO | Pagination policy |
| ORPHAN-CRAWLER | MEDIUM | 0 inlink (crawler) | 57 | SEO_REVIEW | SEO | Какие URL в nav |
| LINK-TO-REDIR | LOW | Ссылки на redirect | 129→0 | CLOSED | MARS | Done WAVE 01 |
| TITLE-LONG | LOW | Title >~70 | 24 | SEO_REVIEW | SEO | Укорачивать? |
| META-MISSING | LOW | Нет description | 23 | SEO_REVIEW | SEO | Точечно добавить |
| META-DUP | LOW | Дубли description | ~137 involvements | SEO_REVIEW | SEO | Развести? |
| H1-MISSING | LOW | Нет H1 (tools) | 5 | EXPECTED_BEHAVIOR | НИЧЕГО / SEO | Не трогать по умолчанию |
| IMG-HUGE | LOW | >1.5MB images | 2→0 | CLOSED | MARS | Done WAVE 01 |
| IMG-ALT | LOW | Empty alt pages | 445 | SEO_REVIEW | SEO | Только significant |
| OG-MISSING | LOW | Нет OG | 97 | SEO_REVIEW | MARS + SEO | High-value templates |

\*197 — исходный audit count; static subset уже reconciled.

---

## 11. Итог

Оставшийся бэклог после закрытия двух HIGH и static completeness — это **14 уникальных сигналов** (6 MEDIUM + 8 LOW), все изначально со статусом REVIEW NEEDED (корзина REVIEW = 14; сумма корзин = 28).  

После TECH CLEANUP WAVE 01 чисто технические кандидаты **LINK-TO-REDIR** и **IMG-HUGE** закрыты; **SM-MISSING-INDEXABLE** пересчитан (eligible gap 0).  

Оставшееся почти всё требует **маршрутизации с SEO**, а не слепого tech-fix.  

Историческая пометка extraction-задачи (0 mutations) сохранена выше по тексту; WAVE 01 отдельно задокументирован в evidence/REPORT.
