# Triumph Manipulator V6 — Legal Entity Card v1

**Schema:** [LEGAL-ENTITY-CARD-v1.md](../../website-factory-reference-v1/legal-entity/LEGAL-ENTITY-CARD-v1.md)  
**Input Sheet:** [TRIUMPH-LEGAL-INPUT-v1.md](../legal/TRIUMPH-LEGAL-INPUT-v1.md)

---

## Card header

| Поле | Значение |
|------|----------|
| `card_id` | `triumph-manipulator-legal-entity-2026-05` |
| `project_name` | Triumph Manipulator Landing V6 |
| `workspace_path` | `workspaces/triumph-manipulator-landing-v6/` |
| `created_at` | 2026-05-30 |
| `updated_at` | 2026-05-30 |
| **card_status** | `READY` |

---

## Identity block

| Поле | Значение | source_document | source_priority | confidence_level |
|------|----------|-----------------|-----------------|------------------|
| **company_name** | ООО «ТРИУМФ» | Operator decision (Phase 2, 2026-05-30) | P6_OPERATOR_CONFIRM | high |
| **legal_name** | Общество с ограниченной ответственностью «ТРИУМФ» | Operator decision (Phase 2, 2026-05-30) | P6_OPERATOR_CONFIRM | high |
| **entity_type** | `LEGAL_ENTITY` | ИНН 10 цифр + operator confirm | P6_OPERATOR_CONFIRM | high |
| **inn** | `5009114932` | Footer v6 + operator-provided pilot data | P4_FOOTER / P6_OPERATOR_CONFIRM | high |
| **ogrn** | `1185027010321` | Footer v6 + operator-provided pilot data | P4_FOOTER / P6_OPERATOR_CONFIRM | high |
| **kpp** | *(not provided)* | — | — | unknown |
| **address** | *(not provided)* | — | — | unknown |
| **email** | `info@manipulator-triumph.ru` | Operator decision — canonical public website email | P6_OPERATOR_CONFIRM | high |
| **phone** | `+7 (918) 991-2-991` | Operator decision — canonical public website phone | P6_OPERATOR_CONFIRM | high |
| **website** | `manipulator-triumph.ru` | Input Sheet / canonical domain | P6_OPERATOR_CONFIRM | high |

### Public contact rule (operator-approved)

Для legal pages, footer, contacts и публичной информации на сайте используется **website domain email** и **website phone** (`info@manipulator-triumph.ru`, `+7 (918) 991-2-991`), а не бухгалтерские или банковские контакты из карточки компании.

---

## Banking block

| Поле | Значение | source_document | source_priority | confidence_level |
|------|----------|-----------------|-----------------|------------------|
| **bank_name** | *(not provided)* | — | — | unknown |
| **bik** | *(not provided)* | — | — | unknown |
| **checking_account** | *(not provided)* | — | — | unknown |
| **correspondent_account** | *(not provided)* | — | — | unknown |

---

## Metadata block

| Поле | Значение |
|------|----------|
| **operator_verified** | `true` |
| **operator_name** | Operator (Phase 2 charter) |
| **operator_verify_date** | 2026-05-30 |
| **extraction_notes** | Legal entity document supplied by operator. Identity fields `company_name` and `legal_name` confirmed with Russian quotation marks « ». Registry fields `inn` / `ogrn` aligned with v6 footer. Public email and phone set to website domain contacts per operator rule. |
| **conflict_report_ref** | Resolved — Phase 1 blocker (`ТРИУМФ` vs `Триумф` vs legacy `ООО «Триумф»`) closed by operator canonical strings |
| **fields_unknown** | `kpp`, `address`, banking block |

---

## Operator sign-off (card)

**Statement:** Юридический документ предоставлен оператором. Поля идентичности подтверждены. Карточка готова для передачи в Legal Input Sheet и генерацию Core Legal Pack L1–L4.

| Поле | Значение |
|------|-------|
| Operator name | Operator (Phase 2 approved) |
| Date | 2026-05-30 |
| Signature channel | In-repo charter — Triumph Legal Pilot Phase 2 |

---

*Card version: v1. Location: `workspaces/triumph-manipulator-landing-v6/legal-entity/`.*
