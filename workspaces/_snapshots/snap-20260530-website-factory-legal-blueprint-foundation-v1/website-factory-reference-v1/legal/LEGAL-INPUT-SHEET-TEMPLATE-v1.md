# Legal Input Sheet — Template v1

**Инструкции:** [LEGAL-INPUT-INSTRUCTIONS-v1.md](LEGAL-INPUT-INSTRUCTIONS-v1.md)  
**Схема:** [LEGAL-INPUT-SHEET-v1.md](LEGAL-INPUT-SHEET-v1.md)

> Скопируйте этот файл в project/pilot folder. Заполните все Required поля.  
> Не выдумывайте значения — используйте `UNKNOWN` с пояснением в Notes.

---

## Meta

| Поле | Значение |
|------|----------|
| **sheet_id** | |
| **project_name** | |
| **workspace_path** | |
| **created_date** | |
| **last_updated** | |

---

## Site Type

| Поле | Значение |
|------|----------|
| **site_type** | `LANDING` \| `PROMO` \| `CATALOG` \| `ECOMMERCE` \| `CORPORATE` \| `SAAS` \| `WEB_APPLICATION` \| `MARKETPLACE` |

**Mapping reference:** [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md)

---

## Identity (Required)

| Поле | Значение | Variable |
|------|----------|----------|
| **company_name** | | `{{company_name}}` |
| **legal_name** | | audit only |
| **domain** | | `{{domain}}` |
| **email** | | `{{email}}` |
| **phone** | | `{{phone}}` |

---

## Legal Entity

| Поле | Значение | Variable |
|------|----------|----------|
| **entity_type** | `LEGAL_ENTITY` \| `INDIVIDUAL_ENTREPRENEUR` \| `SELF_EMPLOYED` \| `UNKNOWN` | — |
| **inn** | | `{{inn}}` |
| **ogrn** | | `{{ogrn}}` (или ОГРНИП для ИП) |

---

## Address

| Поле | Значение |
|------|----------|
| **address_status** | `PROVIDED` \| `NOT_PROVIDED` |
| **address** | *(заполнять только при PROVIDED)* |

**Notes on address decision:**

---

## Derived URLs (Required)

| Поле | Значение | Variable |
|------|----------|----------|
| **privacy_policy_url** | `https://{{domain}}/privacy-policy/` | `{{privacy_policy_url}}` |
| **consent_personal_data_url** | `https://{{domain}}/consent-personal-data/` | `{{consent_personal_data_url}}` |

---

## Cookie Inventory (Optional)

### Analytics systems

| System | Active (yes/no) | Notes |
|--------|:-----------------:|-------|
| Yandex Metrika | | |
| Google Analytics | | |
| Other | | |

### Tracking systems

| System | Active (yes/no) | Notes |
|--------|:-----------------:|-------|
| reCAPTCHA | | |
| Chat widgets | | |
| Call tracking | | |
| Other | | |

---

## Footer Confirmation

| Check | Confirmed (yes/no) |
|-------|:------------------:|
| Footer will use 4 canonical links per LEGAL-IMPLEMENTATION-RULES §3 | |

**Canonical links:**

- Политика конфиденциальности → `/privacy-policy/`
- Согласие на обработку персональных данных → `/consent-personal-data/`
- Пользовательское соглашение → `/user-agreement/`
- Политика Cookie-файлов → `/cookie-files-policy/`

---

## Consent Confirmation

| Check | Confirmed (yes/no) |
|-------|:------------------:|
| All PD forms will use canonical Consent Rule per LEGAL-IMPLEMENTATION-RULES §4 | |

**Forms with PD collection (list partials):**

1.
2.
3.

---

## Notes

*(Источники данных, UNKNOWN пояснения, HITL-решения, legacy drift warnings)*

---

## Operator Sign-Off

| Field | Value |
|-------|-------|
| **Signed by** | |
| **Date** | |
| **Generation authorized** | yes / no |

**Statement:** Я подтверждаю, что значения в этом Legal Input Sheet проверены и могут использоваться для генерации Core Legal Pack L1–L4.

---

*Template version: v1. Do not edit canonical template in-place for project data — copy first.*
