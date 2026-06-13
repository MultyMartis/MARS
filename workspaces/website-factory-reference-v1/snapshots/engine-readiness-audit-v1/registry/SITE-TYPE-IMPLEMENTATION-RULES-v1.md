# Website Factory — Site Type Implementation Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/registry/`  
**Статус:** канонические правила классификации и production scope  
**Не является:** runtime enforcement, CI gate, orchestration product

---

## 1. Core Types — default production targets

**Core Types** являются **целевыми типами production** Website Factory v1 по умолчанию:

| Code | Name |
|------|------|
| `LANDING` | Продающая страница |
| `PROMO` | Промо-сайт |
| `CATALOG` | Виртуальный каталог |
| `ECOMMERCE` | Интернет-магазин |
| `CORPORATE` | Корпоративный сайт |

**Правило:** новый проект Website Factory **должен** быть классифицирован одним из Core Types, если нет явного charter на Extended Type.

**Reference workspace** (`workspaces/website-factory-reference-v1/`) — golden pattern для **`LANDING`** и базовых conversion blocks.

---

## 2. Extended Types — additional architecture required

**Extended Types** **не** являются default production targets. Перед стартом работ **обязателен** architecture charter:

| Code | Name |
|------|------|
| `SAAS` | SaaS-платформа |
| `WEB_APPLICATION` | Веб-приложение |
| `MARKETPLACE` | Маркетплейс |

**Правило:** Extended Types требуют:

- явного `site_type_code` в project intake;
- отдельного IA / integration / legal expansion plan;
- HITL на границах marketing site vs authenticated product;
- **не** применять Core-only block/SEO/legal defaults без адаптации.

**WEB_APPLICATION** — explicitly **not a traditional website**; Website Factory v1 workflows apply только к optional public shell.

---

## 3. Mobile applications — OUT OF SCOPE

**Мобильные приложения (iOS, Android, native/hybrid apps) — вне области Website Factory v1.**

```
MARS
├── Website Factory          ← текущий scope (web)
└── Mobile App Factory       ← FUTURE — не часть Website Factory v1
```

**Правило:**

- не классифицировать mobile app projects как site types данного registry;
- web companion / responsive web — **in scope**;
- app store presence, push, native SDK — **Mobile App Factory (FUTURE)**.

---

## 4. Legal pages

Юридические страницы production-сборок Website Factory **обязаны** следовать:

**[../legal/LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md)**

**Ключевые обязательства:**

- четыре legal URLs в футере (Privacy, Consent, User Agreement, Cookie Policy);
- канонический consent HTML в формах;
- шаблоны и переменные из `workspaces/website-factory-reference-v1/legal/`.

**Site-type-specific legal requirements:** [SITE-TYPE-LEGAL-MAPPING-v1.md](SITE-TYPE-LEGAL-MAPPING-v1.md)

**FUTURE EXPANSION** legal documents (ECOMMERCE, SAAS, MARKETPLACE) — **не** генерировать из v1 templates без legal sign-off.

---

## 5. Mandatory site type selection gate

**Выбор `site_type_code` обязателен до начала:**

| Stage | Зависимость от site type |
|-------|--------------------------|
| **SEO strategy** | [seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md](../seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md), [seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md](../seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md) (v1 hints: [SITE-TYPE-SEO-MAPPING-v1.md](SITE-TYPE-SEO-MAPPING-v1.md) — superseded) |
| **Legal generation** | [legal/SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md) + LEGAL-IMPLEMENTATION-RULES (registry v1 — superseded) |
| **Page architecture / IA** | [SITE-TYPE-REGISTRY-v1.md](SITE-TYPE-REGISTRY-v1.md) + matrix; [page-architecture/](../page-architecture/) |
| **Design generation** | complexity, UX model from registry + matrix |
| **Frontend generation / `block_id`** | [block-registry/BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md), [block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md](../block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md) (role hints: [SITE-TYPE-BLOCK-MAPPING-v1.md](SITE-TYPE-BLOCK-MAPPING-v1.md) — superseded) |

**Правило:** работа без зафиксированного `site_type_code` в project artefacts — **drift risk**; operator **должен** halt и классифицировать (см. mars-survivability operational halt patterns).

**Hybrid sites:** один primary `site_type_code` на project + **per-route-group** override в IA doc (typical: `CORPORATE` + subtrees).

---

## 6. Registry discipline

| Rule | Description |
|------|-------------|
| **Closed taxonomy v1** | Только 8 кодов — см. §7 Validation |
| **No invention** | Не добавлять site types в v1 без explicit human charter |
| **Version pin** | Ссылаться на `*-v1.md`; не смешивать с `site-type-registry-v0.md` IDs без migration note |
| **Documentation only** | Registry не implies runtime agents or automated enforcement |

---

## 7. Validation checklist (operator)

Перед закрытием intake / перед SEO-Legal-IA work:

- [ ] `site_type_code` выбран из closed list
- [ ] Core vs Extended acknowledged
- [ ] Legal mapping reviewed
- [ ] SEO priority aligned
- [ ] Block mapping reviewed
- [ ] Mobile app scope excluded (unless FUTURE charter)
- [ ] Hybrid subtrees documented (if applicable)

---

## 8. Related MARS documents

| Document | Path |
|----------|------|
| Website Factory workflow | `projects/mars-website-factory/` |
| Legal Pack | `workspaces/website-factory-reference-v1/legal/` |
| Survivability / Factory enforcement | `projects/mars-survivability/contracts/website-factory-enforcement-v1.md` |
| Site Type Registry v0 (legacy) | `projects/mars-website-factory/site-type-registry-v0.md` |

---

## SAFE UNKNOWN

- Automated gate preventing work without `site_type_code` — **not implemented**; human discipline only.
- Migration guide v0 → v1 IDs — **not in scope** of this document.
- Mobile App Factory timeline and ownership — **FUTURE**.

---

*Implementation rules version: v1.*
