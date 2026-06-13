# Website Factory — Legal Template Review v1

**Версия:** v1  
**Дата review:** 2026-05-30  
**Область:** Core Legal Pack templates L1–L4  
**Статус:** audit only — **без переписывания текстов**

**Reviewed templates:**

| ID | File |
|----|------|
| L1 | `privacy-policy-template.md` |
| L2 | `consent-personal-data-template.md` |
| L3 | `user-agreement-template.md` |
| L4 | `cookie-files-policy-template.md` |

**Контекст:** [legal-template-cleanup-report-v1.md](reports/legal-template-cleanup-report-v1.md), [LEGAL-PACK-ARCHITECTURE-v1.md](LEGAL-PACK-ARCHITECTURE-v1.md)

---

## Методология

Для каждого шаблона оценены:

1. **Website Factory suitability** — соответствие канону (H1, URL, variables, neutral wording)
2. **Site type fit** — LANDING, PROMO, CATALOG, ECOMMERCE, SAAS, MARKETPLACE, CORPORATE, WEB_APPLICATION

Оценка: **PASS** (baseline OK) / **WEAK** (работает с ограничениями) / **GAP** (требует Extension или rewrite в будущем).

Юридическая полнота по законодательству РФ — **SAFE UNKNOWN** без licensed legal review.

---

## L1 — Privacy Policy (`privacy-policy-template.md`)

### Website Factory suitability — **PASS**

| Критерий | Статус |
|----------|--------|
| H1 канон | ✓ «Политика конфиденциальности» |
| Variables | `{{company_name}}`, `{{domain}}`, `{{email}}`, `{{privacy_policy_url}}` |
| Cross-links | `/consent-personal-data/`, `/cookie-files-policy/` |
| Client-neutral | ✓ (post-cleanup) |
| 152-FZ reference | ✓ |

### Site type fit

| Site type | Rating | Notes |
|-----------|--------|-------|
| LANDING | **PASS** | Lead forms, analytics, cookie — покрыто |
| PROMO | **PASS** | Multi-page contact forms — достаточно |
| CATALOG | **PASS** | RFQ forms — достаточно |
| ECOMMERCE | **WEAK** | Нет: payment data, order history, buyer account data, third-party payment processors |
| SAAS | **WEAK** | Нет: subscription billing data, product usage analytics, B2B processor list |
| MARKETPLACE | **GAP** | Нет: multi-party data flows, seller/buyer roles, platform intermediary |
| CORPORATE | **WEAK** | Baseline OK; partner/employee portals — GAP без Custom Extension |
| WEB_APPLICATION | **WEAK** | Нет: RBAC, operational logs, retention schedules |

### Weaknesses

1. **Generic data categories** — не различает lead-only vs account vs transaction data.
2. **Third-party processors** — упомянуты обобщённо; нет таблицы subprocessors (SaaS/marketplace gap).
3. **Retention periods** — «до достижения целей» без конкретики; слабо для WEB_APPLICATION / SAAS.
4. **Cross-border transfers** — не описаны (EU clients — SAFE UNKNOWN).
5. **`{{phone}}`, `{{address}}`, `{{inn}}`, `{{ogrn}}`** — не в теле; реквизиты часто требуются для RU commercial trust.

### Future improvements (не rewrite сейчас)

- Ecommerce addendum block: payment/order data section.
- SaaS addendum: subscription + product analytics section.
- Optional requisites block with `{{inn}}`, `{{ogrn}}`, `{{address}}`.
- Subprocessor table template (FUTURE Extension).

---

## L2 — Personal Data Consent (`consent-personal-data-template.md`)

### Website Factory suitability — **PASS**

| Критерий | Статус |
|----------|--------|
| H1 канон | ✓ |
| Variables | `{{company_name}}`, `{{domain}}`, `{{email}}`, `{{consent_personal_data_url}}` |
| Cross-link privacy | ✓ `/privacy-policy/` |
| Form consent alignment | ✓ Consent Rule ссылается на L2 + L1 |

### Site type fit

| Site type | Rating | Notes |
|-----------|--------|-------|
| LANDING | **PASS** | Стандартная lead form |
| PROMO | **PASS** | Contact forms |
| CATALOG | **PASS** | RFQ |
| ECOMMERCE | **WEAK** | Нет отдельного consent для checkout / marketing opt-in granularity |
| SAAS | **WEAK** | Нет trial/signup-specific consent variants |
| MARKETPLACE | **GAP** | Нет seller vs buyer consent differentiation |
| CORPORATE | **PASS** | Baseline forms |
| WEB_APPLICATION | **WEAK** | Нет operational / employment consent variants |

### Weaknesses

1. **Single consent model** — один документ для всех целей; ecommerce/SaaS often need granular consents.
2. **No marketing consent separation** — «аналитика» в целях смешана с lead processing.
3. **No minor / representative clause** — edge case для B2B forms.
4. **Static URL reference** — `{{consent_personal_data_url}}` at bottom; OK but depends on correct substitution.

### Future improvements

- Optional «marketing communications» consent block (checkbox separation).
- Ecommerce checkout consent variant (FUTURE).
- Seller registration consent variant for MARKETPLACE Extension.

---

## L3 — User Agreement (`user-agreement-template.md`)

### Website Factory suitability — **PASS** (with tone caveat)

| Критерий | Статус |
|----------|--------|
| H1 канон | ✓ «Пользовательское соглашение» |
| Variables | `{{company_name}}`, `{{domain}}` |
| URL footer line | `/user-agreement/` (hardcoded in template) |
| Neutral wording | ✓ post-cleanup |

### Site type fit

| Site type | Rating | Notes |
|-----------|--------|-------|
| LANDING | **PASS** | Informational site + forms |
| PROMO | **PASS** | Content site |
| CATALOG | **PASS** | Browse + RFQ |
| ECOMMERCE | **GAP** | Не заменяет публичную оферту; нет purchase terms |
| SAAS | **GAP** | Нет subscription, account, API usage terms |
| MARKETPLACE | **GAP** | Нет platform / seller / buyer rules |
| CORPORATE | **WEAK** | Baseline; partner portals need Custom Extension |
| WEB_APPLICATION | **WEAK** | Mentions «учётные записи» but no operational ToS depth |

### Weaknesses

1. **Legacy forum-style clauses** — «не копировать информацию», «эротический контент» — из generic user agreement; **weak fit** for B2B landing/catalog.
2. **Account registration language** — present but site may have no registration (LANDING mismatch — low risk).
3. **No limitation of liability** tuned for service business vs content platform.
4. **No governing law / jurisdiction** clause.
5. **No link to privacy/cookie** in body (only implicit via footer on site).
6. **Ecommerce/SaaS/Marketplace** — structurally wrong document type for transactions; requires Extension Packs.

### Future improvements

- LANDING/PROMO simplified User Agreement variant (remove UGC-heavy clauses).
- Keep L3 as «site usage terms»; never conflate with Public Offer.
- Add cross-reference block to L1/L4 in body.
- ECOMMERCE / SAAS / MARKETPLACE — separate Extension templates (E1, S1, M4).

---

## L4 — Cookie Policy (`cookie-files-policy-template.md`)

### Website Factory suitability — **WEAK**

| Критерий | Статус |
|----------|--------|
| H1 канон | ✓ «Политика Cookie-файлов» |
| Variables | `{{domain}}`, `{{company_name}}`, `{{email}}` |
| Cross-links | ✓ privacy, consent |
| Tone | **Conversational** — «Вам не придётся постоянно вводить логин» |

### Site type fit

| Site type | Rating | Notes |
|-----------|--------|-------|
| LANDING | **WEAK** | Most landings have no login; login-centric wording misleading |
| PROMO | **WEAK** | Same |
| CATALOG | **WEAK** | Same |
| ECOMMERCE | **WEAK** | Needs cart/session cookie taxonomy |
| SAAS | **PASS** | Login/session relevance higher |
| MARKETPLACE | **WEAK** | Needs multi-role session description |
| CORPORATE | **WEAK** | Generic |
| WEB_APPLICATION | **PASS** | Session cookies relevant |

### Weaknesses

1. **Login-centric narrative** — inappropriate default for LANDING/PROMO/CATALOG (no auth).
2. **No cookie categories** — missing necessary / analytics / marketing table.
3. **No retention durations** per cookie type.
4. **No consent mechanism description** — banner behavior not documented.
5. **Third-party cookies** — «Яндекс и др.» mentioned in privacy; cookie doc lacks specifics.
6. **Shortest template** — lowest structural depth of Core Pack.

### Future improvements

- Neutral opening without login assumption.
- Cookie category table (necessary, analytics, marketing).
- Site-type-specific optional blocks (ecommerce cart cookies).
- Align tone with L1/L3 formal register.

---

## Cross-template summary

| Dimension | Overall assessment |
|-----------|-------------------|
| **Core Types (LANDING, PROMO, CATALOG)** | **PASS** — Core Pack sufficient for v1 production with noted L4 tone issue |
| **ECOMMERCE** | **WEAK/GAP** — Core OK for baseline; Extension Pack mandatory for full commerce |
| **SAAS** | **WEAK/GAP** — Core OK for marketing shell; Extension mandatory for product |
| **MARKETPLACE** | **GAP** — Core baseline only |
| **CORPORATE** | **WEAK** — Core baseline; Custom Extension per project |
| **WEB_APPLICATION** | **WEAK** — Core partial; operational docs FUTURE |

### Priority weaknesses (ranked)

1. **L3 legacy UGC clauses** — poor fit for commercial landings.
2. **L4 login-centric + informal tone** — mismatch for majority of Core site types.
3. **No Extension templates** — ECOMMERCE, SAAS, MARKETPLACE cannot reach full legal coverage.
4. **Missing requisites variables in body** — INN/OGRN/address often needed for RU trust.
5. **No granular consents** — marketing vs processing separation.

### What works well (preserve)

- H1 / URL canon across all four templates.
- Variable hydration discipline (post-cleanup).
- 152-FZ anchoring in L1/L2.
- Cross-links between L1, L2, L4.
- Consent Rule alignment with L2 + L1.

---

## Rewrite policy

| Action | Status |
|--------|--------|
| Rewrite templates now | **NOT APPROVED** — this review only |
| Triumph pilot | Use current templates + variable substitution — see [TRIUMPH-LEGAL-PILOT-PLAN-v1.md](pilots/TRIUMPH-LEGAL-PILOT-PLAN-v1.md) |
| Post-pilot improvements | Charter per weakness block above |

---

## SAFE UNKNOWN

- Legal adequacy under current RU law — **UNKNOWN** without licensed review.
- Cookie consent banner legal requirements (ePrivacy / RU practice) — **not encoded** in templates.
- Whether L3 clauses enforceable for B2B service sites — **UNKNOWN**.

---

*Review version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal/`.*
