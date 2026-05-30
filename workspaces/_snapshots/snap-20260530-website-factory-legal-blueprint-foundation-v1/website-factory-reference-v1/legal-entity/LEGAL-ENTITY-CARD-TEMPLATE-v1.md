# Legal Entity Card — Template v1

**Версия:** v1  
**Инструкция:** скопировать в client workspace, заполнить после discovery.  
**Schema:** [LEGAL-ENTITY-CARD-v1.md](LEGAL-ENTITY-CARD-v1.md)

---

## Card header

| Поле | Значение |
|------|----------|
| `card_id` | |
| `project_name` | |
| `workspace_path` | |
| `created_at` | YYYY-MM-DD |
| `updated_at` | |
| **card_status** | `DRAFT` \| `CONFLICT` \| `READY` \| `NOT_READY` |

---

## Identity block

| Поле | Значение | source_document | source_priority | confidence_level |
|------|----------|-----------------|-----------------|------------------|
| **company_name** | | | | |
| **legal_name** | | | | |
| **entity_type** | `LEGAL_ENTITY` \| `INDIVIDUAL_ENTREPRENEUR` \| `SELF_EMPLOYED` \| `UNKNOWN` | | | |
| **inn** | | | | |
| **ogrn** | | | | |
| **kpp** | | | | |
| **address** | | | | |
| **email** | | | | |
| **phone** | | | | |
| **website** | | | | |

---

## Banking block

| Поле | Значение | source_document | source_priority | confidence_level |
|------|----------|-----------------|-----------------|------------------|
| **bank_name** | | | | |
| **bik** | | | | |
| **checking_account** | | | | |
| **correspondent_account** | | | | |

---

## Metadata block

| Поле | Значение |
|------|----------|
| **operator_verified** | `false` → set `true` after HITL |
| **operator_name** | |
| **operator_verify_date** | YYYY-MM-DD |
| **extraction_notes** | |
| **conflict_report_ref** | (path or ID if any) |
| **fields_unknown** | |

---

## Operator sign-off (card)

**Statement:** Я подтверждаю, что значения в этом Legal Entity Card проверены по первичным документам (или явному HITL) и могут использоваться для заполнения Legal Input Sheet.

| Поле | Значение |
|------|----------|
| Operator name | |
| Date | |
| Signature channel | (email / ticket / in-repo) |

---

*Template version: v1. Do not commit secrets (bank tokens, private keys) — only business requisites.*
