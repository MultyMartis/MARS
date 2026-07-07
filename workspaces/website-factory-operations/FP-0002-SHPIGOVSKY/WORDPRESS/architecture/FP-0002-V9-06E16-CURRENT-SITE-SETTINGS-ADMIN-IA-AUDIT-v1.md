# FP-0002 V9-06E16 — Current Site Settings Admin IA Audit

**Evidence:** `validation/v9-06e16-operator-qa-closure-reusable-blocks-clone-cleanup-audit/current-site-settings-admin-ia-audit.json`

## Implementation

| Item | Current state |
|------|----------------|
| Mechanism | ACF Pro options pages |
| Primary menu | **Настройки сайта** (`fp02-site-settings`) |
| Registration | `plugins/shpigovsky-core/src/Admin/OptionsPage.php` |
| Capability | `manage_options` |
| Field groups | Contacts + Modal/Global CTA on `fp02-site-settings` |
| Reviews admin | Separate top-level **Отзывы** (`fp02-reviews`) in `theme/shpigovsky/inc/admin-options.php` |

## Current fields under Настройки сайта

**Contacts:** organisation_name, phones, email, address, hours, map_link, social_links, legal_org_identifiers.

**Modal/CTA:** default_callback_*, default_button_label, default_secondary_button_label, consent reference, global_cta_*.

## Render consumers

Header, footer, consultation modal, final-form, contacts helpers, service CTA helpers.

## Target IA (future, not E16)

```
Настройки сайта
  ├── Общие настройки
  └── Повторяемые блоки
        ├── Шапка
        ├── Подвал
        ├── Финальная форма
        ├── Специалисты
        ├── Отзывы
        └── …
```

See `FP-0002-V9-06E16-SITE-SETTINGS-RESTRUCTURE-PLAN-v1.md`.
