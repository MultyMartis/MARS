# Admin UI after P18C-FU02

Rendered via CLI `MailFormsSettings::render_page()` as `mars` Administrator after deploy.

| Control | Present |
|---------|---------|
| Heading Получатели | yes |
| Email + Подпись fields | yes |
| **Добавить получателя** | yes (`data-fp02-recipient-add`) |
| **Удалить** per row | yes (`data-fp02-recipient-remove`) |
| JS template token `__i__` | yes |
| Raw JSON/serialized field | no |
| Password input value | empty (write-only) |
| Password status | CONFIGURED |

Initial stored row count: **1** (plus `<template>` clone source in markup, not a stored recipient).

Assets:

- `assets/js/mail-forms-admin.js`
- `assets/css/mail-forms-admin.css`

enqueued only on `fp02-site-settings-mail-forms`.
