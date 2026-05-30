# Website Factory — Legal Template Hardening v1.1

**Версия:** v1.1  
**Дата:** 2026-05-30  
**Область:** `workspaces/website-factory-reference-v1/legal/`  
**Статус:** operator-approved hardening — **documentation + Core templates**  
**Предшественник:** [LEGAL-TEMPLATE-REVIEW-v1.md](LEGAL-TEMPLATE-REVIEW-v1.md), [reports/legal-template-cleanup-report-v1.md](reports/legal-template-cleanup-report-v1.md)

**Не является:** юридической экспертизой, автоматической валидацией, rewrite Extension Packs.

---

## 1. Изменения (summary)

| Шаблон | Действие | Результат |
|--------|----------|-----------|
| L3 `user-agreement-template.md` | Hardening CORE | Удалены предположения об аккаунтах, регистрации, UGC-платформе; добавлен блок «Связанные документы» |
| L4 `cookie-files-policy-template.md` | Upgrade to canonical | Структура §1–§5, категории cookie, нейтральный тон, без login-centric narrative |
| L1 `privacy-policy-template.md` | Validation only | Без изменений текста в v1.1 |
| L2 `consent-personal-data-template.md` | Validation only | Без изменений текста в v1.1 |

---

## 2. User Agreement hardening (L3)

### 2.1. Удалённые положения (из CORE)

Перенесены в **Future extension recommendations** (§6) — не должны возвращаться в CORE без charter:

| # | Удалённый фрагмент (смысл) | Причина удаления |
|---|---------------------------|------------------|
| 1 | «удалять учётные записи» | Предполагает user accounts |
| 2 | «отказывать в регистрации без объяснения причин» | Registration system |
| 3 | «обновлять персональные данные, предоставленные при регистрации» | Registration / profile |
| 4 | «не регистрировать учётную запись от имени или вместо другого лица» | Account registration |
| 5 | «не размещать материалы рекламного, эротического, порнографического…» | UGC / content platform |
| 6 | «не копировать информацию с других источников» | Forum-style UGC rule |
| 7 | «не совершать действий, направленных на введение других пользователей в заблуждение» | Multi-user community platform |
| 8 | «обеспечивать сохранность личных данных от доступа третьих лиц» (как обязанность «пользователя сайта») | Смешение с account/cabinet duty; L1/L2 покрывают ПДн |
| 9 | «пользователь лично несёт полную ответственность за распространяемую им информацию» | UGC liability model |
| 10 | «сохранность информации, размещённой пользователем» (форс-мажор) | User-generated content storage |

### 2.2. Добавлено / сохранено в CORE

- Право обращаться через формы и контакты на сайте.
- Обязанность достоверности данных **в формах** (не «при регистрации»).
- Обобщённое соблюдение законодательства РФ вместо перечня «контент-платформенных» запретов.
- Блок **«Связанные документы»** — перекрёстные ссылки на L1, L2, L4.
- Ответственность: внешние ссылки, третьи лица, форс-мажор — **без UGC-модели**.
- Уточнение про услуги: «если иное не предусмотрено отдельным договором или офертой» — нейтрально для ECOMMERCE **без** встраивания оферты в CORE.

### 2.3. Намеренно не добавлено в CORE

- Публичная оферта, оплата, возвраты (ECOMMERCE Extension).
- Подписки, API, SLA (SAAS Extension).
- Правила продавцов/покупателей (MARKETPLACE Extension).
- Личный кабинет, удаление профиля (WEB_APPLICATION / SAAS Extension).

---

## 3. Cookie Policy hardening (L4)

### 3.1. Улучшения

| Секция | Содержание |
|--------|------------|
| **§1 Что такое cookie** | Определение, назначение, границы идентификации |
| **§2 Какие cookie могут использоваться** | Подразделы: технические, аналитические, маркетинговые (conditional), сторонние |
| **§3 Управление cookie** | Нейтральное описание механизма уведомления на проекте |
| **§4 Как отключить cookie** | Действия пользователя в браузере |
| **§5 Справочная информация браузеров** | Таблица браузеров + темы справки (без client/domain URL) |

### 3.2. Удалено из L4

- Login-centric абзац («не придётся вводить логин и пароль»).
- Неформальный тон «Что мы делаем с cookie» / «Зачем нам нужны».
- Прямая привязка к авторизации как основной цели cookie.

### 3.3. Сохранённые переменные

`{{domain}}`, `{{company_name}}`, `{{email}}` — без client data.

---

## 4. Core template suitability matrix (post v1.1)

Оценка: **PASS** = достаточно для production baseline; **WEAK** = с ограничениями; **GAP** = нужен Extension Pack.

### L1 — Политика конфиденциальности

| Site type | Rating |
|-----------|--------|
| LANDING | **PASS** |
| PROMO | **PASS** |
| CATALOG | **PASS** |
| ECOMMERCE | **WEAK** |
| CORPORATE | **WEAK** |
| SAAS | **WEAK** |
| WEB_APPLICATION | **WEAK** |
| MARKETPLACE | **GAP** |

**Gaps:** payment/order data, subprocessors table, retention specificity, multi-party flows (MARKETPLACE).

### L2 — Согласие на обработку ПДн

| Site type | Rating |
|-----------|--------|
| LANDING | **PASS** |
| PROMO | **PASS** |
| CATALOG | **PASS** |
| ECOMMERCE | **WEAK** |
| CORPORATE | **PASS** |
| SAAS | **WEAK** |
| WEB_APPLICATION | **WEAK** |
| MARKETPLACE | **GAP** |

**Gaps:** granular checkout/marketing consents; seller/buyer separation (MARKETPLACE).

### L3 — Пользовательское соглашение (после v1.1)

| Site type | Rating |
|-----------|--------|
| LANDING | **PASS** |
| PROMO | **PASS** |
| CATALOG | **PASS** |
| ECOMMERCE | **WEAK** |
| CORPORATE | **WEAK** |
| SAAS | **GAP** |
| WEB_APPLICATION | **GAP** |
| MARKETPLACE | **GAP** |

**Gaps:** L3 = условия использования **сайта**, не оферта/подписка/платформа. ECOMMERCE — WEAK (базовый browse + forms OK; покупки — Extension). SAAS/MARKETPLACE/WEB_APPLICATION — GAP для account/API/platform terms.

### L4 — Политика Cookie-файлов (после v1.1)

| Site type | Rating |
|-----------|--------|
| LANDING | **PASS** |
| PROMO | **PASS** |
| CATALOG | **PASS** |
| ECOMMERCE | **WEAK** |
| CORPORATE | **PASS** |
| SAAS | **PASS** |
| WEB_APPLICATION | **PASS** |
| MARKETPLACE | **WEAK** |

**Gaps:** cart/session taxonomy detail (ECOMMERCE); multi-role sessions (MARKETPLACE); cookie banner implementation not encoded in template.

### Core Types aggregate (L1–L4)

| Site type | Core Pack v1.1 |
|-----------|----------------|
| LANDING | **PASS** |
| PROMO | **PASS** |
| CATALOG | **PASS** |
| ECOMMERCE | **WEAK** (L3/L1/L2 need Extension for full commerce) |
| CORPORATE | **WEAK** (baseline OK; portals — Extension) |
| SAAS | **WEAK/GAP** (L3/L1/L2 GAP for product; L4 PASS) |
| WEB_APPLICATION | **WEAK/GAP** |
| MARKETPLACE | **GAP** |

---

## 5. Оставшиеся ограничения (remaining limitations)

1. **Юридическая полнота по РФ** — SAFE UNKNOWN без licensed review.
2. **Cookie banner / consent UI** — не описаны в шаблонах; реализация на уровне проекта.
3. **Реквизиты** (`{{inn}}`, `{{ogrn}}`, `{{address}}`) — не в теле Core; допустимы в footer/расширениях оператора.
4. **ECOMMERCE / SAAS / MARKETPLACE** — Core не заменяет оферту, DPA, seller terms, subscription ToS.
5. **Яндекс.Метрика** — упомянута в L1 обобщённо; в L4 — без жёсткой привязки к конкретному счётчику (нейтрально).
6. **Сроки хранения cookie** — категории есть; per-cookie retention table — FUTURE.

---

## 6. Future extension recommendations

Рекомендации **не входят** в CORE. Требуют отдельного charter / Extension Pack.

### SAAS / WEB_APPLICATION

- Terms of Service: учётные записи, подписка, trial, API, acceptable use, suspension/termination.
- Privacy addendum: product usage logs, billing data, subprocessors.
- Cookie addendum: session/auth cookies, preference storage.
- Consent variants: signup, marketing, B2B representative.

### MARKETPLACE

- Platform rules: seller/buyer roles, listings, disputes, commissions.
- Multi-party privacy flows; seller PDn consent template.
- Cookie: multi-role sessions, ad/retargeting specifics.

### ECOMMERCE

- Public offer / purchase terms (отдельно от L3).
- Checkout PDn consent; payment processor disclosure in L1.
- Cookie: cart, checkout, payment session identifiers.

### UGC / community (removed from CORE L3)

- Вернуть **только** в Extension: moderation, user content liability, account registration rules, profile deletion, content prohibitions.

### CORPORATE (optional)

- Partner/employee portal terms; career data processing annex.

### L1/L2/L4 cross-cutting

- Subprocessor table template.
- Marketing vs processing consent checkbox separation.
- Optional requisites block in legal page footer body.

---

## 7. Validation (hardening scope)

| Check | Result |
|-------|--------|
| No new site types | **PASS** — только 8 из [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| No SAAS logic inside CORE L3 | **PASS** |
| No MARKETPLACE logic inside CORE L3 | **PASS** |
| Mobile App Factory separate | **PASS** — не затронут |
| Triumph workspace untouched | **PASS** — audit only |
| Client data in templates | **PASS** — none |

---

## 8. SAFE UNKNOWN

- Соответствие обновлённых текстов актуальной судебной и регуляторной практике РФ — **UNKNOWN**.
- Обязательность cookie-баннера для конкретного Triumph-стека (Метрика, reCAPTCHA) — **UNKNOWN** без tag inventory sign-off.
- Нужен ли юридический адрес ООО в теле L1 для Triumph — **operator decision**.

---

*Hardening version: v1.1. Canonical location: `workspaces/website-factory-reference-v1/legal/`.*
