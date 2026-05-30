# Triumph Manipulator V6 — Legal Entity Card (Draft) v1

**Версия:** v1 (draft)  
**Дата:** 2026-05-30  
**Schema:** [LEGAL-ENTITY-CARD-v1.md](../../website-factory-reference-v1/legal-entity/LEGAL-ENTITY-CARD-v1.md)  
**Пилот:** Triumph Legal Entity Discovery Pilot v1  
**card_status:** `NOT_READY`  
**Discovery gate:** **BLOCKED** — P1 `project-input/legal-entity/` пуст

---

## Card header

| Поле | Значение |
|------|----------|
| `card_id` | `triumph-manipulator-legal-entity-2026-05` |
| `project_name` | Triumph Manipulator V6 |
| `workspace_path` | `workspaces/triumph-manipulator-landing-v6/` |
| `created_at` | 2026-05-30 |
| `updated_at` | 2026-05-30 |
| **card_status** | `NOT_READY` |

---

## Identity block

| Поле | Значение | source_document | source_priority | confidence_level |
|------|----------|-----------------|-----------------|------------------|
| **company_name** | UNKNOWN | — | — | unknown |
| **legal_name** | UNKNOWN | — | — | unknown |
| **entity_type** | UNKNOWN | — | — | unknown |
| **inn** | `5009114932` | `src/partials/sections/v5-page01/landing-footer.html` (P4 signal — **не** P1 verify) | P4_FOOTER | high |
| **ogrn** | `1185027010321` | `src/partials/sections/v5-page01/landing-footer.html` (P4 signal — **не** P1 verify) | P4_FOOTER | high |
| **kpp** | UNKNOWN | — | — | unknown |
| **address** | UNKNOWN | — | — | unknown |
| **email** | `info@manipulator-triumph.ru` | Footer, `backend/config/mail.config.php` | P4_FOOTER / P5_CONTENT | high |
| **phone** | `+7 (918) 991-2-991` | Header, footer, forms (`tel:+79189912991`) | P4_FOOTER / P5_CONTENT | high |
| **website** | `manipulator-triumph.ru` | `src/pages/*.html` canonical URLs | P5_CONTENT | high |

**domain (Input Sheet meta, not card field):** `manipulator-triumph.ru` — подтверждён canonical в production candidate pages; переносится в Legal Input Sheet на Step 6.

### Запреты (соблюдены)

| Поле | Статус |
|------|--------|
| `company_name` | **Не изобретено** — UNKNOWN (footer «ООО «ТРИУМФ»» = P4 signal, не записано как verified value) |
| `legal_name` | **Не изобретено** — UNKNOWN |
| `address` | **Не изобретено** — UNKNOWN |
| Banking block | **Не изобретено** — все поля UNKNOWN |

---

## Banking block

| Поле | Значение | source_document | source_priority | confidence_level |
|------|----------|-----------------|-----------------|------------------|
| **bank_name** | UNKNOWN | — | — | unknown |
| **bik** | UNKNOWN | — | — | unknown |
| **checking_account** | UNKNOWN | — | — | unknown |
| **correspondent_account** | UNKNOWN | — | — | unknown |

---

## Metadata block

| Поле | Значение |
|------|----------|
| **operator_verified** | `false` |
| **operator_name** | — |
| **operator_verify_date** | — |
| **extraction_notes** | P1 inbox пуст. Частичные P4/P5 signals (inn, ogrn, email, phone, domain) зафиксированы для audit only; **не** заменяют P1 extraction и P6 verify. Identity block (`company_name`, `legal_name`) требует ЕГРЮЛ/реквизиты в `project-input/legal-entity/`. |
| **conflict_report_ref** | — (conflict resolution deferred — нет P1 для сравнения с P4 «ООО «ТРИУМФ»» vs «Триумф») |
| **fields_unknown** | `company_name`, `legal_name`, `entity_type`, `kpp`, `address`, `bank_name`, `bik`, `checking_account`, `correspondent_account` |

---

## Readiness decision

| Decision | **BLOCKED** |
|----------|-------------|
| Reason | Нет P1 source documents; `company_name` и `legal_name` = UNKNOWN; `operator_verified = false` |
| Unblock path | Operator places P1 docs → extraction → P6 verify → `card_status = READY` |

---

## Operator sign-off (card)

**Не выполнен** — card не готов к sign-off.

| Поле | Значение |
|------|----------|
| Operator name | — |
| Date | — |
| Signature channel | — |

---

*Draft version: v1. Not a verified Legal Entity Card. Do not use for Legal Input Sheet or Legal Generation.*
