# ISEO-SU SEO TEAM NEW TASK PACK — 2026-09 v1

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** `ISEO-SU-SITE-OPS-SEO-TEAM-TASK-PACK-REGISTRATION-01`  
**Site:** `https://i-seo.su/`  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Registered:** 2026-09-03  
**Mode:** DOCUMENTATION / ROADMAP ONLY — no production implementation in this registration wave

---

## 1. Статус

**APPROVED FOR IMPLEMENTATION PLANNING**

Пакет утверждён как каноническая карта будущих implementation waves.  
Production mutations в рамках registration: **0**.  
Implementation **не** стартует автоматически после регистрации.

---

## 2. Источник задач

Задачи получены от **SEO-команды** как утверждённый content / requirements package по сайту `i-seo.su`.

Canonical authority для планирования:

- этот документ;
- [ISEO-SU-IMPLEMENTATION-ROADMAP-2026-09-v1.md](ISEO-SU-IMPLEMENTATION-ROADMAP-2026-09-v1.md);
- текущие baselines форм / sitemap / protected zones.

Временные user-upload / chat-temp пути **не** являются canonical authority и в MARS не сохраняются как SoT.

Контентный authority для city / USA / UAE текстов: пакет текстов, предоставленный SEO-командой. MARS **не** переписывает SEO-копирайт самостоятельно.

---

## 3. Общая карта

| Wave | Задача | Scope | Production | Sitemap | Menu | SEO decision dependency | Status |
|------|--------|-------|------------|---------|------|-------------------------|--------|
| 1 | Form Consent | Checkbox согласия на всех контактных формах с ПДн; client + server validation | Да (forms / shared helper / JS) | Нет | Нет | Exact privacy policy URL | **NEXT** |
| 2 | City SEO pages ×5 | Clone `/services/seo/b-regionakh.html` + city content; hub linking; self-canonical; sitemap allowlist regen | Да (static pages + hub + sitemap regen) | Да (5 new URLs) | Да (внутренние ссылки с hub; не отдельный глобальный menu charter) | SEO content package; Advego/Turgenev = SEO-side residual | **QUEUED** |
| 3 | USA / UAE draft pages ×2 | Clone `/services/seo/zarubezhnye.html`; draft for SEO approval | Да (static pages only after decisions) | **Нет** | **Нет** | Indexability policy; title brand suffix confirmation | **QUEUED / OPEN DECISIONS** |

---

## 4. WAVE 1 — Form Consent

### Основание

SEO-команда указала: на контактных формах отсутствуют обязательные чекбоксы согласия на обработку персональных данных.

### Требование

На **всех** контактных формах, где пользователь передаёт персональные данные, добавить checkbox **непосредственно перед** кнопкой отправки.

**Текст:**

> Я соглашаюсь с политикой конфиденциальности и даю согласие на обработку персональных данных

### Требования к реализации

- checkbox **обязательный**;
- client-side validation;
- server-side validation;
- без checkbox POST **должен отклоняться**;
- ссылка «политикой конфиденциальности» → реальная действующая страница политики;
- **до реализации** определить exact canonical URL политики;
- не ломать текущий HMAC;
- не ломать honeypot;
- не ломать min fill time;
- не ломать rate limit;
- не ломать duplicate suppression;
- production recipient остаётся: `nikel007i33@yandex.ru` **only**;
- `test_mode` остаётся **OFF**;
- по возможности серверную проверку централизовать через общий form security/helper (`iseo-form-security.php`);
- не создавать новые handler'ы без необходимости.

### Приоритет

WAVE 1 выполняется **первой**: новые страницы будут клонировать текущие формы, поэтому form baseline сначала должен стать корректным.

### Candidate privacy URL (не утверждён молча)

В static inventory уже есть `https://i-seo.su/privacy-policy.html`.  
Это **кандидат**, не silent approval. См. §8 Open Decisions.

---

## 5. WAVE 2 — City Pages

### Source page

`https://i-seo.su/services/seo/b-regionakh.html`

### Новые URL (×5)

1. `https://i-seo.su/services/seo/prodvizhenie-v-sankt-peterburge.html`
2. `https://i-seo.su/services/seo/prodvizhenie-v-kazani.html`
3. `https://i-seo.su/services/seo/prodvizhenie-v-ekaterinburge.html`
4. `https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html`
5. `https://i-seo.su/services/seo/prodvizhenie-v-krasnoyarske.html`

### Структура

Полный clone структуры source page:

- HTML / CSS / JS;
- forms + handlers integration;
- menu/footer;
- schema.org (если есть);
- calculator, tariffs, team slider, cases, FAQ structure;
- recommendations, акции, выбор тематики, другие услуги.

### Меняется только утверждённый SEO-content

- title;
- meta description;
- H1;
- intro;
- основной city-specific блок;
- FAQ answer #4.

Не переписывать SEO-копирайт самостоятельно.

### Internal linking

- На `b-regionakh.html` — блок «Выберите ваш город» со ссылками на все 5 новых страниц.
- На каждой новой странице — ссылка обратно на `b-regionakh.html`.

### Indexing / sitemap

- `index,follow`;
- self-canonical на каждой из 5 новых страниц;
- добавить все 5 URL в canonical static sitemap inventory;
- **не** редактировать `sitemap-static.xml` вручную как SoT;
- использовать generator / allowlist model;
- regenerate `sitemap-static.xml`;
- completeness validation;
- проверить 200 / canonical / sitemap presence / отсутствие новых 4xx/5xx.

### Важно

- Общую **CANON-MISSING** задачу по старым страницам **не трогать**.
- Self-canonical в этой волне **только** для 5 новых city pages.

### Content residual (SEO-side)

Тексты ещё должны быть проверены через Advego / Тургенев.  
MARS **не** меняет контент по этим сервисам без нового утверждённого текста.

---

## 6. WAVE 3 — USA / UAE

### Source page

`https://i-seo.su/services/seo/zarubezhnye.html`

### Новые URL (×2)

- USA: `https://i-seo.su/services/seo/prodvizhenie-v-ssha.html`
- UAE: `https://i-seo.su/services/seo/prodvizhenie-v-oae.html`

### Структура

Полный clone source page. Сохраняются layout, styles, JS, forms, stats/ratings, tariffs, work stages, what is included, calculator, акции, team, recommendations, FAQ, free audit, other services.

### Меняются

- title / meta description / H1 / intro;
- 2nd H2 section title + full content;
- intro paragraph in work stages;
- cases;
- **remove** секцию «Выберите тематику» полностью.

### Ограничения публикации

Страницы пока **не**:

- выводить в menu;
- добавлять в sitemap.

Purpose: создать для согласования SEO-командой.

### Cases to verify (только в implementation wave)

| Market | Cases |
|--------|-------|
| USA | `/cases/aaa-limo.html`, `/cases/drnicole.html` |
| UAE | `/cases/iluve-me.html`, `/cases/youfleet.html` |

Проверка существования/корректности — **не** сейчас.

---

## 7. Implementation Order

Утверждённый порядок:

1. **WAVE 1 — FORM CONSENT**
2. **WAVE 2 — 5 CITY SEO PAGES**
3. **WAVE 3 — USA / UAE DRAFT PAGES**

Не менять порядок без operator decision.

Reason: FORM CONSENT first — чтобы все новые страницы наследовали корректный form baseline.

---

## 8. Open Decisions

### 8.1 USA/UAE PRE-APPROVAL INDEXABILITY — **UNRESOLVED**

В исходном SEO ТЗ:

- menu = NO;
- sitemap = NO;
- отдельный `noindex` **не** указан.

MARS **не** придумывает `noindex` без решения.

До production реализации требуется:

- explicit SEO/operator decision; **или**
- deployment strategy, исключающая нежелательное обнаружение поисковиком.

### 8.2 OPEN CONTENT CONFIRMATION — USA/UAE TITLE BRAND SUFFIX

В SEO ТЗ:

- USA: `Заказать SEO-продвижение сайта компании в США |itlseo`
- UAE: `Заказать SEO-продвижение сайта компании в ОАЭ | itlseo.su`

Возможная опечатка относительно бренда/domain `i-seo.su`.  
**Не исправлять молча.**

Перед implementation: подтвердить — оставлять текст SEO буквально **или** заменить на корректный `i-seo.su` branding.

### 8.3 Exact privacy policy URL (перед WAVE 1)

Кандидат из inventory: `https://i-seo.su/privacy-policy.html`.  
Требуется подтверждение, что это действующая canonical страница политики для ссылки в checkbox.

---

## 9. Protected Existing Systems

Не нарушать / не смешивать без отдельного charter:

- HMAC + production-local secret authority;
- antispam (honeypot, min fill time, rate limit, duplicate suppression);
- recipient routing (`nikel007i33@yandex.ru` only; `test_mode` OFF);
- forms security helper architecture;
- sitemap generator / allowlist / completeness gate;
- static vs WP sitemap ownership;
- текущий SEO review backlog (CANON-*, SM-NONINDEX, TITLE-*, META-*, ORPHAN-CRAWLER, IMG-ALT, OG-MISSING, H1-MISSING review).

---

## 10. Acceptance Model

После **каждой** wave — отдельный REPORT + validation evidence.  
Registration REPORT этой задачи **не** закрывает implementation waves.

---

## 11. Deferred / Out of Scope

Не смешивать этот task pack с оставшимся SEO-review backlog:

- CANON-MISSING
- CANON-MISMATCH
- SM-NONINDEX
- TITLE-DUP
- TITLE-LONG
- META-MISSING
- META-DUP
- ORPHAN-CRAWLER
- IMG-ALT
- OG-MISSING
- H1-MISSING review

Эти пункты остаются отдельным SEO review contour и **не** закрываются этой задачей.

---

## 12. Current Decision

**READY TO START WAVE 1**

Следующий operator/charter шаг: отдельная implementation задача на Form Consent (после подтверждения privacy policy URL).  
WAVE 2 / WAVE 3 остаются в очереди. WAVE 3 дополнительно ждёт open decisions.
