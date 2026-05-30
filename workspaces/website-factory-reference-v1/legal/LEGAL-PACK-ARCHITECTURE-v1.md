# Website Factory — Legal Pack Architecture v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/legal/`  
**Статус:** каноническая архитектура Legal Pack для Site Types v1 — **documentation only**  
**Не является:** runtime, автоматической генерацией, юридической экспертизой, CI-валидатором

---

## Назначение

Legal Pack Architecture v1 определяет **структурный слой** юридических документов Website Factory: что входит в базовый пакет, какие расширения существуют для Extended Types и hybrid-сценариев, и как Legal Pack связан с [SITE-TYPE-REGISTRY-v1](../registry/SITE-TYPE-REGISTRY-v1.md).

**Принцип:** один **Core Legal Pack** покрывает все 8 approved site types; специализированные документы добавляются через **Extension Packs** — без изменения базовой таксономии.

**Связанные документы:**

| Документ | Назначение |
|----------|------------|
| [LEGAL-IMPLEMENTATION-RULES.md](LEGAL-IMPLEMENTATION-RULES.md) | Footer Rule, Consent Rule, условия обязательности |
| [LEGAL-VARIABLE-REGISTRY.md](LEGAL-VARIABLE-REGISTRY.md) | Переменные подстановки |
| [LEGAL-GENERATION-CONTRACT-v1.md](LEGAL-GENERATION-CONTRACT-v1.md) | Production gate — запрет плейсхолдеров |
| [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md) | Матрица требований по site type |
| [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) | Каноническая таксономия (8 типов) |
| [LEGAL-ENTITY-DISCOVERY-RULES-v1.md](../legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md) | Discovery priorities, `project-input/legal-entity/` |
| [LEGAL-ENTITY-CARD-v1.md](../legal-entity/LEGAL-ENTITY-CARD-v1.md) | Primary entity data artifact |
| [LEGAL-ENTITY-WORKFLOW-v1.md](../legal-entity/LEGAL-ENTITY-WORKFLOW-v1.md) | Discovery → card → Input Sheet |

**Предшественник:** [SITE-TYPE-LEGAL-MAPPING-v1.md](../registry/SITE-TYPE-LEGAL-MAPPING-v1.md) — сохранён в registry; v2 — расширенная legal-матрица в `legal/`.

---

## Область применения

| В scope | Out of scope |
|---------|--------------|
| Website Factory — все 8 approved site types | **Mobile App Factory** — FUTURE separate factory |
| Core + Extension Pack architecture | Автоматическая генерация HTML/страниц |
| Канонические шаблоны L1–L4 | Переписывание legal-текстов |
| Production rules (footer, consent, placeholders) | Governance expansion |

**Mobile App Factory** упоминается только как **FUTURE separate factory** — mobile apps, native stores и in-app legal flows **не входят** в Website Factory Legal Pack v1.

---

## Legal Entity Discovery layer (v1)

**Статус:** канонический слой (2026-05-30) — **documentation only**.

Website Factory **не** получает данные о юрлице из footer, случайного контента или неструктурированных notes как primary source. Обязательный поток:

```text
Discovery (P1–P6)
        ↓
Legal Entity Card v1          ← primary source for entity fields
        ↓
Legal Input Sheet v1          ← consumes card; adds domain, site_type, sign-off
        ↓
Legal Generation (L1–L4)
```

| Слой | Расположение | Назначение |
|------|--------------|------------|
| Input inbox | `<project>/project-input/legal-entity/` | PDF, DOCX, EGRUL, scans — Priority P1 |
| Discovery rules | `legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md` | Приоритеты; no downgrade overwrite |
| Card | `legal-entity/LEGAL-ENTITY-CARD-v1.md` | `company_name`, `legal_name`, inn, ogrn, banking, metadata |
| Validation | `legal-entity/LEGAL-ENTITY-VALIDATION-RULES-v1.md` | Format, conflicts — never guess |

**Запрет:** extraction output **не** пишется напрямую в Legal Templates, Footer partials или Input Sheet без card + operator verify.

**Triumph lesson:** [TRIUMPH-LEGAL-ENTITY-LESSON-v1.md](../legal-entity/TRIUMPH-LEGAL-ENTITY-LESSON-v1.md).

---

## Архитектура — обзор

```text
Website Factory Legal Architecture v1
│
├── LEGAL ENTITY DISCOVERY (v1)      ← project-input → card
│
├── CORE LEGAL PACK (L1–L4)          ← все 8 site types
│   ├── L1 Privacy Policy
│   ├── L2 Personal Data Consent
│   ├── L3 User Agreement
│   └── L4 Cookie Policy
│
├── EXTENSION PACKS (FUTURE templates) ← по site type / subtree
│   ├── ECOMMERCE EXTENSION
│   ├── SAAS EXTENSION
│   ├── MARKETPLACE EXTENSION
│   └── CORPORATE CUSTOM EXTENSION
│
└── IMPLEMENTATION LAYER
    ├── LEGAL-IMPLEMENTATION-RULES (footer, consent, H1)
    ├── LEGAL-VARIABLE-REGISTRY (placeholders)
    └── LEGAL-GENERATION-CONTRACT (production gate)
```

---

## CORE LEGAL PACK

### Обязательность

Core Legal Pack **требуется** для всех approved site types при выполнении условий production — см. [LEGAL-IMPLEMENTATION-RULES.md §1](LEGAL-IMPLEMENTATION-RULES.md).

| site_type_code | Core Pack |
|----------------|-----------|
| `LANDING` | L1, L2, L3, L4 |
| `PROMO` | L1, L2, L3, L4 |
| `CATALOG` | L1, L2, L3, L4 |
| `ECOMMERCE` | L1, L2, L3, L4 |
| `CORPORATE` | L1, L2, L3, L4 |
| `SAAS` | L1, L2, L3, L4 |
| `WEB_APPLICATION` | L1, L2, L3, L4* |
| `MARKETPLACE` | L1, L2, L3, L4 |

\* Для `WEB_APPLICATION` L3/L4 могут быть optional на minimal public shell — см. [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md). Baseline architecture: Core Pack определён для всех типов; granular optional — в mapping v2.

### Документы Core Pack

| ID | Документ | H1 (канон) | Шаблон | URL |
|----|----------|------------|--------|-----|
| **L1** | Privacy Policy | Политика конфиденциальности | `privacy-policy-template.md` | `/privacy-policy/` |
| **L2** | Personal Data Consent | Согласие на обработку персональных данных | `consent-personal-data-template.md` | `/consent-personal-data/` |
| **L3** | User Agreement | Пользовательское соглашение | `user-agreement-template.md` | `/user-agreement/` |
| **L4** | Cookie Policy | Политика Cookie-файлов | `cookie-files-policy-template.md` | `/cookie-files-policy/` |

### Инварианты Core Pack

1. **H1 = footer link text** — строгое совпадение (Footer Rule).
2. **URL фиксированы** — альтернативные пути запрещены.
3. **Consent Rule** — единственный канонический HTML для форм (см. LEGAL-IMPLEMENTATION-RULES §4).
4. **Переменные** — только из [LEGAL-VARIABLE-REGISTRY.md](LEGAL-VARIABLE-REGISTRY.md).
5. **Production gate** — zero unresolved placeholders (см. LEGAL-GENERATION-CONTRACT-v1).

---

## EXTENSION PACKS

Extension Packs **не заменяют** Core Legal Pack. Они добавляют документы поверх L1–L4 когда business model требует расширенного legal surface.

**Статус v1:** architecture + mapping only. Шаблоны Extension Packs — **FUTURE**; требуют human legal review перед канонизацией.

---

### ECOMMERCE EXTENSION

**Применимость:** `ECOMMERCE`; ecommerce subtrees в `CORPORATE`.

| ID | Документ (FUTURE) | Назначение |
|----|-------------------|------------|
| E1 | Public Offer (Публичная оферта) | Distance selling, условия покупки |
| E2 | Payment Rules (Правила оплаты) | Способы оплаты, сроки, безопасность |
| E3 | Delivery Rules (Условия доставки) | Сроки, зоны, стоимость, риски |
| E4 | Return Policy (Политика возврата и обмена) | Возврат, обмен, refund |

**Ограничение:** L3 User Agreement **не является** заменой публичной оферты без юридического sign-off.

---

### SAAS EXTENSION

**Применимость:** `SAAS`; SaaS subtrees в `CORPORATE`.

| ID | Документ (FUTURE) | Назначение |
|----|-------------------|------------|
| S1 | Subscription Terms (Условия подписки) | Billing cycles, renewal, cancellation |
| S2 | Acceptable Use Policy (AUP) | Запрещённое использование продукта |
| S3 | SLA | Uptime, support response, credits |
| S4 | Data Processing Addendum (DPA) | B2B data processing, 152-FZ / GDPR annexes |

---

### MARKETPLACE EXTENSION

**Применимость:** `MARKETPLACE`; marketplace subtrees в `CORPORATE`.

| ID | Документ (FUTURE) | Назначение |
|----|-------------------|------------|
| M1 | Seller Agreement (Договор с продавцом) | Onboarding, commission, obligations |
| M2 | Buyer Rules (Правила для покупателей) | Buyer conduct, protection |
| M3 | Dispute Resolution (Разрешение споров) | Escalation, mediation, platform role |
| M4 | Marketplace Terms (Условия маркетплейса) | Platform rules, prohibited items, ratings |

---

### CORPORATE CUSTOM EXTENSION

**Применимость:** `CORPORATE` и hybrid sites с project-specific legal requirements.

| Категория | Примеры (FUTURE / project-specific) |
|-----------|-------------------------------------|
| Partner portal | Partner agreement, NDA pages |
| Employee services | Internal portal terms |
| Investor / regulated | Disclaimers, sector disclosures |
| Subtree inheritance | Ecommerce / SaaS / Marketplace extensions per route group |

**Правило:** Corporate Custom Extension **не стандартизируется** в Website Factory v1 — документируется per project charter; Core Pack остаётся обязательным baseline.

---

## Связь Extension ↔ Site Type

| site_type_code | Core Pack | Extension Pack |
|----------------|-----------|----------------|
| `LANDING` | L1–L4 | — |
| `PROMO` | L1–L4 | — |
| `CATALOG` | L1–L4 | — |
| `ECOMMERCE` | L1–L4 | ECOMMERCE EXTENSION (FUTURE) |
| `CORPORATE` | L1–L4 | CORPORATE CUSTOM + subtree extensions |
| `SAAS` | L1–L4 | SAAS EXTENSION (FUTURE) |
| `WEB_APPLICATION` | L1–L4* | Operational ToS (FUTURE) |
| `MARKETPLACE` | L1–L4 | MARKETPLACE EXTENSION (FUTURE) |

---

## Версионирование

| Артефакт | Версия | Расположение |
|----------|--------|--------------|
| Legal Pack Architecture | v1 | `legal/LEGAL-PACK-ARCHITECTURE-v1.md` |
| Core templates L1–L4 | v1 | `legal/*-template.md` |
| Site Type Legal Mapping | v2 | `legal/SITE-TYPE-LEGAL-MAPPING-v2.md` |
| Generation Contract | v1 | `legal/LEGAL-GENERATION-CONTRACT-v1.md` |
| Legal Entity Discovery | v1 | `legal-entity/` |

При добавлении Extension Pack templates — increment extension pack version; Core Pack L1–L4 меняется только через explicit operator charter.

---

## SAFE UNKNOWN

- Machine-readable export (JSON/YAML) Legal Pack schema — **не определён**; канон — Markdown.
- Industry-specific compliance (медицина, финансы, gambling) — **не закодирован** exhaustively.
- Cross-border variants (EU GDPR standalone pages) — **не** в Core Pack v1.
- Автоматическая сборка legal HTML из Markdown — **не реализована** в reference workspace.

---

*Architecture version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal/`.*
