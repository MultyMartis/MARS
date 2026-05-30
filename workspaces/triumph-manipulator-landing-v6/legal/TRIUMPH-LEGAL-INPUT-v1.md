# Triumph Manipulator V6 — Legal Input Sheet v1

**Инструкции:** [LEGAL-INPUT-INSTRUCTIONS-v1.md](../../website-factory-reference-v1/legal/LEGAL-INPUT-INSTRUCTIONS-v1.md)  
**Схема:** [LEGAL-INPUT-SHEET-v1.md](../../website-factory-reference-v1/legal/LEGAL-INPUT-SHEET-v1.md)  
**Legal Entity Card:** [LEGAL-ENTITY-CARD-v1.md](../legal-entity/LEGAL-ENTITY-CARD-v1.md)  
**Pilot execution (Phase 1):** [TRIUMPH-LEGAL-PILOT-EXECUTION-v1.md](../../website-factory-reference-v1/legal/pilots/TRIUMPH-LEGAL-PILOT-EXECUTION-v1.md)

> Production Legal Input Sheet для Website Factory pilot — **Phase 2 unblocked**.

---

## Meta

| Поле | Значение |
|------|----------|
| **sheet_id** | `triumph-manipulator-v6-legal-input-2026-05-30` |
| **project_name** | Triumph Manipulator Landing V6 |
| **workspace_path** | `workspaces/triumph-manipulator-landing-v6/` |
| **created_date** | 2026-05-30 |
| **last_updated** | 2026-05-30 |
| **card_id** | `triumph-manipulator-legal-entity-2026-05` |

---

## Site Type

| Поле | Значение |
|------|----------|
| **site_type** | `LANDING` |

**Mapping reference:** [SITE-TYPE-LEGAL-MAPPING-v2.md](../../website-factory-reference-v1/legal/SITE-TYPE-LEGAL-MAPPING-v2.md) — L1–L4 required; Footer Rule + Consent Rule apply.

---

## Identity (Required)

| Поле | Значение | Variable | Source / Notes |
|------|----------|----------|----------------|
| **company_name** | ООО «ТРИУМФ» | `{{company_name}}` | Operator-approved (Phase 2). Russian quotation marks « ». |
| **legal_name** | Общество с ограниченной ответственностью «ТРИУМФ» | audit only | Operator-approved (Phase 2). Full legal name per registration form. |
| **domain** | `manipulator-triumph.ru` | `{{domain}}` | Operator-provided + canonical in `src/pages/` |
| **email** | `info@manipulator-triumph.ru` | `{{email}}` | Operator-approved — canonical public website email |
| **phone** | `+7 (918) 991-2-991` | `{{phone}}` | Operator-approved — canonical public website phone |

---

## Legal Entity

| Поле | Значение | Variable | Source / Notes |
|------|----------|----------|----------------|
| **entity_type** | `LEGAL_ENTITY` | — | ИНН 10 цифр → юрлицо |
| **inn** | `5009114932` | `{{inn}}` | Legal Entity Card + footer v6 |
| **ogrn** | `1185027010321` | `{{ogrn}}` | Legal Entity Card + footer v6 |

---

## Address

| Поле | Значение |
|------|----------|
| **address_status** | `NOT_PROVIDED` |
| **address** | *(empty — not used for `{{address}}`)* |

**Notes on address decision:** Юридический адрес **не подтверждён** оператором в Phase 2. «Краснодар, Россия» в footer — маркетинговый контакт, **не** `{{address}}`. Core templates v1 не требуют `{{address}}` в теле.

---

## Derived URLs (Required)

| Поле | Значение | Variable |
|------|----------|----------|
| **privacy_policy_url** | `https://manipulator-triumph.ru/privacy-policy/` | `{{privacy_policy_url}}` |
| **consent_personal_data_url** | `https://manipulator-triumph.ru/consent-personal-data/` | `{{consent_personal_data_url}}` |

---

## Cookie Inventory (Optional)

### Analytics systems

| System | Active (yes/no) | Notes |
|--------|:-----------------:|-------|
| Yandex Metrika | UNKNOWN | Not operator-confirmed for L4 |
| Google Analytics | UNKNOWN | Not operator-confirmed |
| Other | — | |

### Tracking systems

| System | Active (yes/no) | Notes |
|--------|:-----------------:|-------|
| reCAPTCHA | UNKNOWN | Deploy reports reference config; L4 factual list not signed off |
| Chat widgets | UNKNOWN | |
| Call tracking | UNKNOWN | |
| Other | — | |

---

## Footer Confirmation

| Check | Confirmed (yes/no) |
|-------|:------------------:|
| Footer will use 4 canonical links per LEGAL-IMPLEMENTATION-RULES §3 | **yes** — L4 drift fixed in Phase 2 |

**Canonical links (target):**

- Политика конфиденциальности → `/privacy-policy/`
- Согласие на обработку персональных данных → `/consent-personal-data/`
- Пользовательское соглашение → `/user-agreement/`
- Политика Cookie-файлов → `/cookie-files-policy/`

---

## Consent Confirmation

| Check | Confirmed (yes/no) |
|-------|:------------------:|
| All PD forms will use canonical Consent Rule per LEGAL-IMPLEMENTATION-RULES §4 | **yes** — verified at Phase 1; re-validated Phase 2 |

---

## Notes

### Generation source

- Templates: `workspaces/website-factory-reference-v1/legal/*-template.md`
- Substitution values: this sheet + [LEGAL-ENTITY-CARD-v1.md](../legal-entity/LEGAL-ENTITY-CARD-v1.md)
- **No AI paraphrasing** — verbatim template text with variable substitution only

### Legacy signals (must not appear in generated L1–L4)

- `gruzotaxi-triumph.ru`, `info@gktriumph.ru`, `gruzotaxi_triumph` (Telegram)

---

## Operator Sign-Off

| Field | Value |
|-------|-------|
| **Signed by** | Operator (Triumph Legal Pilot Phase 2 — APPROVED) |
| **Date** | 2026-05-30 |
| **Generation authorized** | **yes** |

**Statement:** `company_name`, `legal_name`, `domain`, `email`, `phone`, `inn`, `ogrn`, `site_type` подтверждены оператором. Генерация L1–L4 авторизована.

---

*Sheet version: v1. Location: `workspaces/triumph-manipulator-landing-v6/legal/`.*
