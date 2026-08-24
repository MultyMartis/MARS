# ISEO-SU GLOSSARY FINAL CORPUS v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-FINAL-CORPUS-AND-BATCH-01-CONTENT  
**Date:** 2026-07-25  
**Source workbook:** `materials/glossary/ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx`  
**Prior audit:** `data/glossary-editorial/ISEO-SU-GLOSSARY-TERM-AUDIT-v1.csv`  
**Dataset:** `data/glossary-editorial/ISEO-SU-GLOSSARY-FINAL-CORPUS-v1.csv`

---

## 1. Corpus Status

Final operational disposition assigned for **all 241** source terms.

**Batch 04 final content completion (2026-07-26)** re-evaluated the remaining publication-pool candidates and updated dispositions where needed. Counts below are **current**.

| Disposition | Count |
|-------------|------:|
| APPROVED | 137 |
| APPROVED_RENAME | 47 |
| MERGED | 30 |
| DEFERRED | 14 |
| EXCLUDED | 13 |
| **Total** | **241** |

**Publication pool (APPROVED + APPROVED_RENAME):** 184  
**Populated production-quality drafts:** 184 (Batches 01–04)  
**Publication-eligible:** 184 — see `ISEO-SU-GLOSSARY-PUBLICATION-ELIGIBILITY-v1.md`  
**Published:** 184 (publication completed 2026-07-26; current production authority is `ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md`)

Historical note: initial final-corpus cut was APPROVED 146 / APPROVED_RENAME 48 / MERGED 26 / DEFERRED 8 / EXCLUDED 13 (publication pool 194). Batch 04 moved 4→MERGED and 6→DEFERRED rather than padding weak articles.

---

## 2. Decision Authority

Operator authorized MARS to make reasonable editorial decisions independently for the glossary.

Policy applied:

- obvious KEEP → APPROVED;
- obvious RENAME → APPROVED_RENAME;
- obvious MERGE → MERGED with synonym retention;
- REVIEW → DEFERRED unless clearly verifiable (none of the 8 REVIEW terms cleared that bar);
- EXCLUDE → EXCLUDED retained;
- `expert_review=YES` does **not** auto-exclude: approved when primary framing is verifiable;
- no publication in this task.

---

## 3. Source Baseline

- Immutable Nikita workbook (241 terms).
- Editorial audit v1: KEEP 146 / RENAME 48 / MERGE 26 / REVIEW 8 / EXCLUDE 13.
- Expert-review flag: 34 terms.
- WordPress: 241 draft CPT `glossary` records already exist.

---

## 4. Final Decision Model

| Final disposition | Meaning |
|-------------------|---------|
| APPROVED | Own glossary article under source-compatible canonical title |
| APPROVED_RENAME | Own article under corrected canonical title; source title retained as synonym/provenance |
| MERGED | No separate article; maps to another canonical article |
| DEFERRED | Potentially useful later; not in publication corpus now |
| EXCLUDED | Unsuitable as independent glossary concept |

---

## 5. Approved Terms

Count: **137** (after Batch 04 disposition cleanup; see CSV for authoritative list)

- `АГС` → **АГС** (search engines and indexing, MEDIUM)
- `Алгоритм ранжирования` → **Алгоритм ранжирования** (search engines and indexing, MEDIUM)
- `Апдейт алгоритма` → **Апдейт алгоритма** (search engines and indexing, MEDIUM)
- `Асессор` → **Асессор** (analytics and metrics, MEDIUM)
- `Аутрич` → **Аутрич** (link building, MEDIUM)
- `Аффилированность` → **Аффилированность** (SEO fundamentals, MEDIUM)
- `Бан сайта` → **Бан сайта** (search engines and indexing, MEDIUM)
- `Безанкорная ссылка` → **Безанкорная ссылка** (link building, MEDIUM)
- `Белая оптимизация` → **Белая оптимизация** (SEO fundamentals, MEDIUM)
- `Биржа ссылок` → **Биржа ссылок** (link building, MEDIUM)
- `Битые ссылки` → **Битые ссылки** (link building, MEDIUM)
- `Брендовый трафик` → **Брендовый трафик** (digital marketing, MEDIUM)
- `Веб-мастер` → **Веб-мастер** (SEO fundamentals, MEDIUM)
- `Вертикальный поиск` → **Вертикальный поиск** (SEO fundamentals, MEDIUM)
- `Видимость сайта` → **Видимость сайта** (SEO fundamentals, MEDIUM)
- `Внешняя оптимизация` → **Внешняя оптимизация** (SEO fundamentals, HIGH)
- `Внутренняя оптимизация` → **Внутренняя оптимизация** (SEO fundamentals, HIGH)
- `Внутренняя перелинковка` → **Внутренняя перелинковка** (SEO fundamentals, MEDIUM)
- `Вода в тексте` → **Вода в тексте** (content and semantics, MEDIUM)
- `Воронка продаж` → **Воронка продаж** (UX and conversion, MEDIUM)
- `Геозависимый запрос` → **Геозависимый запрос** (content and semantics, MEDIUM)
- `Геонезависимый запрос` → **Геонезависимый запрос** (content and semantics, MEDIUM)
- `Главная страница сайта` → **Главная страница сайта** (SEO fundamentals, MEDIUM)
- `Главное зеркало сайта` → **Главное зеркало сайта** (SEO fundamentals, MEDIUM)
- `Глубина вложенности` → **Глубина вложенности** (SEO fundamentals, MEDIUM)
- `Донор ссылки` → **Донор ссылки** (link building, MEDIUM)
- `Дорвей` → **Дорвей** (SEO fundamentals, MEDIUM)
- `Дубли страниц` → **Дубли страниц** (SEO fundamentals, MEDIUM)
- `Естественные ссылки` → **Естественные ссылки** (link building, MEDIUM)
- `Заспамленность текста` → **Заспамленность текста** (content and semantics, MEDIUM)
- `Индекс` → **Индекс** (search engines and indexing, MEDIUM)
- `Индексация` → **Индексация** (search engines and indexing, HIGH)
- `Каннибализация запросов` → **Каннибализация запросов** (content and semantics, MEDIUM)
- `Кластеризация запросов` → **Кластеризация запросов** (content and semantics, MEDIUM)
- `Клик` → **Клик** (SEO fundamentals, LOW)
- `Кликфрод` → **Кликфрод** (SEO fundamentals, MEDIUM)
- `Ключевое слово` → **Ключевое слово** (content and semantics, MEDIUM)
- `Конверсия` → **Конверсия** (analytics and metrics, HIGH)
- `Конкурентность запроса` → **Конкурентность запроса** (content and semantics, MEDIUM)
- `Контент-маркетинг` → **Контент-маркетинг** (content and semantics, MEDIUM)
- `Копирайтинг` → **Копирайтинг** (SEO fundamentals, MEDIUM)
- `Краулинг` → **Краулинг** (search engines and indexing, MEDIUM)
- `Краулинговый бюджет` → **Краулинговый бюджет** (search engines and indexing, MEDIUM)
- `Лид` → **Лид** (SEO fundamentals, LOW)
- `Линкбилдинг` → **Линкбилдинг** (SEO fundamentals, MEDIUM)
- `Метатеги` → **Метатеги** (technical SEO, MEDIUM)
- `Мобильная версия сайта` → **Мобильная версия сайта** (SEO fundamentals, MEDIUM)
- `Морда` → **Морда** (SEO fundamentals, LOW)
- `Морфологическое вхождение` → **Морфологическое вхождение** (SEO fundamentals, MEDIUM)
- `Мультиязычность сайта` → **Мультиязычность сайта** (SEO fundamentals, MEDIUM)
- `Навигационный интент` → **Навигационный интент** (content and semantics, MEDIUM)
- `Небрендовый трафик` → **Небрендовый трафик** (digital marketing, MEDIUM)
- `Оптимизация под голосовой поиск` → **Оптимизация под голосовой поиск** (SEO fundamentals, MEDIUM)
- `Органическая выдача` → **Органическая выдача** (search engines and indexing, MEDIUM)
- `Органический трафик` → **Органический трафик** (analytics and metrics, HIGH)
- `Отдел антиспама` → **Отдел антиспама** (SEO fundamentals, MEDIUM)
- `Пагинация` → **Пагинация** (SEO fundamentals, MEDIUM)
- `Панель вебмастера` → **Панель вебмастера** (SEO fundamentals, MEDIUM)
- `Плотность ключевых слов` → **Плотность ключевых слов** (content and semantics, MEDIUM)
- `Поведенческие факторы` → **Поведенческие факторы** (SEO fundamentals, HIGH)
- `Подсветка в выдаче` → **Подсветка в выдаче** (search engines and indexing, MEDIUM)
- `Позиции сайта` → **Позиции сайта** (SEO fundamentals, MEDIUM)
- `Поисковая контекстная реклама` → **Поисковая контекстная реклама** (contextual advertising, MEDIUM)
- `Поисковый запрос` → **Поисковый запрос** (content and semantics, MEDIUM)
- `Поисковый спам` → **Поисковый спам** (SEO fundamentals, MEDIUM)
- `Посетитель` → **Посетитель** (SEO fundamentals, MEDIUM)
- `Пост-фильтры` → **Пост-фильтры** (search engines and indexing, MEDIUM)
- `ПРЕСЕО` → **ПРЕСЕО** (SEO fundamentals, MEDIUM)
- `Процент вхождений` → **Процент вхождений** (SEO fundamentals, MEDIUM)
- `Прямые заходы` → **Прямые заходы** (SEO fundamentals, MEDIUM)
- `Разбавленное вхождение` → **Разбавленное вхождение** (SEO fundamentals, MEDIUM)
- `Ранжирование` → **Ранжирование** (SEO fundamentals, HIGH)
- `Редирект` → **Редирект** (technical SEO, MEDIUM)
- `Релевантность страницы` → **Релевантность страницы** (SEO fundamentals, MEDIUM)
- `Реферальный трафик` → **Реферальный трафик** (SEO fundamentals, MEDIUM)
- `Рунет` → **Рунет** (SEO fundamentals, MEDIUM)
- `Сателлит` → **Сателлит** (SEO fundamentals, MEDIUM)
- `СДЛ` → **СДЛ** (SEO fundamentals, MEDIUM)
- `Семантическое ядро` → **Семантическое ядро** (content and semantics, HIGH)
- `Сквозная аналитика` → **Сквозная аналитика** (analytics and metrics, MEDIUM)
- `Скорость загрузки страницы` → **Скорость загрузки страницы** (SEO fundamentals, MEDIUM)
- `Сниппет` → **Сниппет** (search engines and indexing, HIGH)
- `СНСС (ранее НПС)` → **СНСС (ранее НПС)** (SEO fundamentals, MEDIUM)
- `Социальные сигналы` → **Социальные сигналы** (digital marketing, MEDIUM)
- `СПЕКТР` → **СПЕКТР** (SEO fundamentals, MEDIUM)
- `Ссылочная масса` → **Ссылочная масса** (link building, MEDIUM)
- `Ссылочный профиль` → **Ссылочный профиль** (link building, MEDIUM)
- `Ссылочный спам` → **Ссылочный спам** (link building, MEDIUM)
- `Структура сайта` → **Структура сайта** (SEO fundamentals, MEDIUM)
- `Счетчик посещаемости` → **Счетчик посещаемости** (SEO fundamentals, MEDIUM)
- `Текстовые факторы` → **Текстовые факторы** (SEO fundamentals, MEDIUM)
- `Техническая оптимизация` → **Техническая оптимизация** (SEO fundamentals, MEDIUM)
- `тИЦ` → **тИЦ** (SEO fundamentals, MEDIUM)
- `Точное вхождение` → **Точное вхождение** (SEO fundamentals, MEDIUM)
- `Транзакционный интент` → **Транзакционный интент** (content and semantics, MEDIUM)
- `Траст сайта` → **Траст сайта** (SEO fundamentals, LOW)
- `УВ` → **УВ** (SEO fundamentals, MEDIUM)
- `Уникальность текста` → **Уникальность текста** (SEO fundamentals, MEDIUM)
- `Уникальный посетитель` → **Уникальный посетитель** (SEO fundamentals, MEDIUM)
- `Устранение дублей` → **Устранение дублей** (SEO fundamentals, MEDIUM)
- `Фактор ранжирования` → **Фактор ранжирования** (SEO fundamentals, MEDIUM)
- `Фильтр поисковой системы` → **Фильтр поисковой системы** (search engines and indexing, MEDIUM)
- `Хлебные крошки` → **Хлебные крошки** (technical SEO, MEDIUM)
- `Хостинг` → **Хостинг** (security and infrastructure, MEDIUM)
- `Хостинг-провайдер` → **Хостинг-провайдер** (security and infrastructure, MEDIUM)
- `Целевая аудитория` → **Целевая аудитория** (SEO fundamentals, MEDIUM)
- `Целевой поисковый запрос` → **Целевой поисковый запрос** (content and semantics, MEDIUM)
- `Частотность запроса` → **Частотность запроса** (content and semantics, MEDIUM)
- `Чёрные методы оптимизации` → **Чёрные методы оптимизации** (SEO fundamentals, MEDIUM)
- `Шингл` → **Шингл** (SEO fundamentals, MEDIUM)
- `Экспертность контента` → **Экспертность контента** (content and semantics, MEDIUM)
- `Яндекс.Вебмастер` → **Яндекс.Вебмастер** (search engines and indexing, HIGH)
- `Яндекс Директ` → **Яндекс Директ** (contextual advertising, HIGH)
- `Яндекс.Метрика` → **Яндекс.Метрика** (analytics and metrics, HIGH)
- `BERT` → **BERT** (content and semantics, MEDIUM)
- `CatBoost` → **CatBoost** (SEO fundamentals, MEDIUM)
- `Core Web Vitals` → **Core Web Vitals** (technical SEO, HIGH)
- `CPA` → **CPA** (analytics and metrics, MEDIUM)
- `CPC` → **CPC** (analytics and metrics, MEDIUM)
- `CPL` → **CPL** (analytics and metrics, MEDIUM)
- `Disavow` → **Disavow** (link building, MEDIUM)
- `E-E-A-T` → **E-E-A-T** (SEO fundamentals, HIGH)
- `Event tracking` → **Event tracking** (analytics and metrics, MEDIUM)
- `GEO` → **GEO** (AI search and GEO, HIGH)
- `Google Ads` → **Google Ads** (contextual advertising, HIGH)
- `Google AdSense` → **Google AdSense** (contextual advertising, MEDIUM)
- `Google Analytics` → **Google Analytics** (analytics and metrics, HIGH)
- `Google Search Console` → **Google Search Console** (search engines and indexing, HIGH)
- `HTTP-код ответа` → **HTTP-код ответа** (technical SEO, MEDIUM)
- `HTTPS` → **HTTPS** (technical SEO, MEDIUM)
- `LSI` → **LSI** (content and semantics, HIGH)
- `LTV` → **LTV** (analytics and metrics, MEDIUM)
- `Mixed content` → **Mixed content** (technical SEO, MEDIUM)
- `Mobile-first indexing` → **Mobile-first indexing** (technical SEO, MEDIUM)
- `Neural Matching` → **Neural Matching** (AI search and GEO, MEDIUM)
- `Noindex` → **Noindex** (technical SEO, MEDIUM)
- `PBN` → **PBN** (link building, MEDIUM)
- `RankBrain` → **RankBrain** (AI search and GEO, MEDIUM)
- `ROMI` → **ROMI** (analytics and metrics, MEDIUM)
- `SEO` → **SEO** (SEO fundamentals, HIGH)
- `SERM` → **SERM** (digital marketing, MEDIUM)
- `Spam Update` → **Spam Update** (search engines and indexing, MEDIUM)
- `TF-IDF` → **TF-IDF** (content and semantics, MEDIUM)
- `UTM-метки` → **UTM-метки** (analytics and metrics, MEDIUM)
- `Wayback Machine` → **Wayback Machine** (SEO fundamentals, MEDIUM)
- `WHOIS` → **WHOIS** (security and infrastructure, MEDIUM)

---

## 6. Approved Renames

Count: **47** (after Batch 04: `ВЧ / СЧ / НЧ запросы` moved to MERGED → Частотность запроса)

- `Акцептор` → **Акцептор ссылки** (`акцептор-ссылки`)
- `Анкор (анкорный текст)` → **Анкорный текст** (`анкорный-текст`)
- `Атрибут rel="nofollow"` → **Nofollow** (`nofollow`)
- `Аудит сайта (SEO-аудит)` → **SEO-аудит** (`seo-аудит`)
- `Баден-Баден (алгоритм)` → **Баден-Баден** (`баден-баден`)
- `Быстрые ссылки (сайтлинки)` → **Быстрые ссылки** (`быстрые-ссылки`)
- `Визит / Сессия` → **Сессия** (`сессия`)
- `ВЧ / СЧ / НЧ запросы` → **Частотность запроса** (`частотность-запроса`)
- `Дашборд (Dashboard)` → **Дашборд** (`дашборд`)
- `Длинный хвост (long tail)` → **Длинный хвост** (`длинный-хвост`)
- `Заголовки H1–H6` → **Заголовки H1–H6** (`заголовки-h1-h6`)
- `Запрос информационный` → **Информационный запрос** (`информационный-запрос`)
- `Запрос коммерческий` → **Коммерческий запрос** (`коммерческий-запрос`)
- `Запрос навигационный` → **Навигационный запрос** (`навигационный-запрос`)
- `Индекс качества сайта (ИКС)` → **ИКС** (`икс`)
- `Интент` → **Поисковый интент** (`поисковый-интент`)
- `Канонический URL (canonical)` → **Канонический URL** (`канонический-url`)
- `КАПЧА (CAPTCHA)` → **CAPTCHA** (`captcha`)
- `Карта сайта (sitemap.xml)` → **Карта сайта** (`карта-сайта`)
- `Краулер (поисковый робот)` → **Поисковый робот** (`поисковый-робот`)
- `Лендинг (посадочная страница)` → **Посадочная страница** (`посадочная-страница`)
- `Матрикснет (Matrixnet)` → **MatrixNet** (`matrixnet`)
- `Микроразметка (Schema.org)` → **Микроразметка** (`микроразметка`)
- `Минусинск (алгоритм)` → **Минусинск** (`минусинск`)
- `Обратная ссылка (backlink)` → **Обратная ссылка** (`обратная-ссылка`)
- `Отказы (показатель отказов)` → **Показатель отказов** (`показатель-отказов`)
- `Панда (алгоритм)` → **Google Panda** (`google-panda`)
- `Пингвин (алгоритм)` → **Google Penguin** (`google-penguin`)
- `Поисковая выдача (SERP)` → **Поисковая выдача** (`поисковая-выдача`)
- `Файл robots.txt` → **robots.txt** (`robots.txt`)
- `ЧПУ (человекопонятный URL)` → **ЧПУ** (`чпу`)
- `Alt-атрибут` → **Alt-текст** (`alt-текст`)
- `AMP (ускоренные мобильные страницы)` → **AMP** (`amp`)
- `BM25 (Okapi BM25)` → **BM25** (`bm25`)
- `CMS (система управления сайтом)` → **CMS** (`cms`)
- `CTR (кликабельность)` → **CTR** (`ctr`)
- `DA (Domain Authority)` → **Domain Authority** (`domain-authority`)
- `DR (Domain Rating)` → **Domain Rating** (`domain-rating`)
- `FAQ-разметка` → **FAQ-разметка** (`faq-разметка`)
- `GET-параметр (CGI-параметр)` → **GET-параметр** (`get-параметр`)
- `KPI (ключевые показатели эффективности)` → **KPI** (`kpi`)
- `Pay-per-Click (PPC)` → **PPC** (`ppc`)
- `PR (PageRank)` → **PageRank** (`pagerank`)
- `ROI (окупаемость инвестиций)` → **ROI** (`roi`)
- `UX/UI (юзабилити и интерфейс)` → **UX и UI** (`ux-и-ui`)
- `404 ошибка` → **Ошибка 404** (`ошибка-404`)
- `410 ошибка` → **Ошибка 410** (`ошибка-410`)
- `500 ошибка` → **Ошибка 500** (`ошибка-500`)

---

## 7. Merged Terms

Count: **30**

- `Алгоритмы поисковых систем` → **Алгоритм ранжирования**
- `Гостевой постинг` → **Аутрич**
- `ГС` → **Главная страница сайта**
- `Зеркало сайта` → **Главное зеркало сайта**
- `Исходящие ссылки` → **Ссылка**
- `Крауд-маркетинг` → **Аутрич**
- `Мета-тег Keywords` → **Метатеги**
- `Неестественная ссылка` → **Ссылочный спам**
- `Переспам ключевыми словами` → **Заспамленность текста**
- `Поисковая оптимизация` → **SEO**
- `Продвижение сайта` → **SEO**
- `Редирект 301` → **Редирект**
- `Редирект 302` → **Редирект**
- `Сквозные ссылки` → **Внутренняя перелинковка**
- `Ссылочный агрегатор` → **Биржа ссылок**
- `Ссылочный взрыв` → **Ссылочный спам**
- `Ссылочный граф` → **Ссылочный профиль**
- `Тег description` → **Метатеги**
- `Тег title` → **Метатеги**
- `Топ-10 / Топ-3` → **Позиции сайта**
- `Трафик` → **Сессия**
- `CLS` → **Core Web Vitals**
- `FID` → **Core Web Vitals**
- `LCP` → **Core Web Vitals**
- `SSL` → **HTTPS**
- `Юзабилити` → **UX и UI**
- `ВЧ / СЧ / НЧ запросы` → **Частотность запроса** *(Batch 04)*
- `Морда` → **Главная страница сайта** *(Batch 04)*
- `УВ` → **Уникальный посетитель** *(Batch 04)*
- `Процент вхождений` → **Плотность ключевых слов** *(Batch 04)*

---

## 8. Deferred Terms

Count: **14**

- `Контент` — Very broad; KEEP only if short foundational definition wanted. | Too broad foundational term; defer separate article unless short fundamentals layer authorized.
- `Скрипт` — Too vague — may EXCLUDE. | Too vague for glossary concept.
- `Ссылка` — Very broad foundational term — KEEP short or EXCLUDE in favor of specific link terms. | Too broad; covered by specific link terms.
- `Human-First Content` — Marketing/SEO framing term — align with Google helpful content guidance; avoid slogan tone. | Positioning slogan vs helpful-content guidance; defer until wording approved.
- `MFA` — Made-for-Advertising sites — confirm acronym usage for RU audience. | Made-for-Advertising acronym — confirm RU audience usefulness.
- `Sandbox` — Often mythical/overstated; expert decide KEEP with myth-busting or EXCLUDE. | Often mythical/overstated; defer until myth-busting framing approved.
- `Spam Score` — Moz proprietary metric — disclose or EXCLUDE. | Moz proprietary metric; defer pending vendor-disclosure decision.
- `URL-адрес` — Very basic; KEEP short or EXCLUDE. | Too basic relative to glossary scope.
- `СНСС (ранее НПС)` — *(Batch 04)* historical Yandex anti-paid-link framing; naming/status unstable.
- `СПЕКТР` — *(Batch 04)* diversity-of-SERP framing; primary docs insufficient.
- `ПРЕСЕО` — *(Batch 04)* agency process jargon.
- `Отдел антиспама` — *(Batch 04)* organizational metaphor, not glossary concept.
- `Пост-фильтры` — *(Batch 04)* unstable jargon vs filter/algorithm.
- `CatBoost` — *(Batch 04)* ML library; ranking role opaque.

---

## 9. Excluded Terms

Count: **13**

- `Веб-страница` — Too basic/generic for professional SEO glossary.
- `Домен` — Too basic; keep DA/DR/WHOIS instead. Operator may override to KEEP.
- `Лайк и шара` — Colloquial social engagement phrase, not a glossary concept.
- `Обмен ссылками между проектами Исполнителя` — Contractual/operational practice, not a public glossary term.
- `Обмен тематически близкими ссылками` — Service/process phrase; not a standalone concept (cover under естественные/неестественные ссылки if needed).
- `Сервер` — Too basic for this glossary.
- `Яндекс Каталог (YACA)` — Historical/obsolete Yandex product; exclude or archive note only.
- `Cookie` — General web/privacy concept; not core SEO glossary unless analytics angle insisted.
- `d-url-rewriter.php (seo-модуль)` — Product/module filename, not a general glossary concept.
- `Flash/Флэш` — Obsolete web technology; not useful for current i-seo.su glossary.
- `HTML` — General web tech; out of SEO glossary scope unless Nikita wants fundamentals layer.
- `IP-адрес` — Too generic for SEO glossary.
- `JS / JavaScript` — General web tech; JS SEO nuances can live under technical SEO terms.

---

## 10. Expert Verification Resolution

Expert-flagged source terms: **34**.

Resolution rule: approve when a factual definition can be established from authoritative framing (Google Search Central / quality rater docs, Yandex product docs, web.dev, vendor proprietary-metric disclosure). Otherwise defer.

Notable approvals with caution notes: E-E-A-T, GEO, Показатель отказов, АГС, Баден-Баден, Минусинск, MatrixNet, ИКС, Domain Authority, Domain Rating, PageRank, AMP, BM25, PBN, SERM, FAQ-разметка, Поведенческие факторы, Траст.

Deferred from REVIEW queue: Контент, Скрипт, Ссылка, Human-First Content, MFA, Sandbox, Spam Score, URL-адрес.

---

## 11. Canonical Naming Rules

- Prefer industry-standard Latin abbreviations where normal (SEO, CTR, PPC, robots.txt, HTTPS, CMS).
- Prefer official product spellings (Core Web Vitals, Google Search Console, Яндекс.Метрика).
- Prefer E-E-A-T established form.
- Prefer Russian common titles when that is the audience-facing form (Обратная ссылка, Анкорный текст).
- Do not Russify technical identifiers unnaturally (`robots.txt`, not «файл роботс»).
- Do not fabricate synonyms for keyword coverage.
- One concept per published page; merges absorb near-duplicates.

---

## 12. Publication Pool

The final eligible pool is **184** concepts, all now published as canonical glossary articles. Batch descriptions below remain historical wave context.

---

## 13. Deferred Pool

**14** terms remain DEFERRED and non-public pending clearer definitions, audience fit, or myth-risk framing.

---

## 14. Future Reconsideration Rules

Reconsider a deferred/excluded term only when:

1. primary documentation or a clear audience need appears;
2. a distinct concept not covered by an existing approved page can be stated;
3. proprietary metrics include explicit vendor disclosure;
4. operator/Nikita overrides the disposition in writing.

Do not reopen merges solely for SEO landing-page multiplication.

---

*ISEO-SU Glossary Final Corpus v1 · 2026-07-25 · independent editorial disposition · no publication.*
