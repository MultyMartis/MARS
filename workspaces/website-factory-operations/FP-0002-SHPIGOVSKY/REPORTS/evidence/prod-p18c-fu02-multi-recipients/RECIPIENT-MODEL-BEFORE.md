# Recipient model before P18C-FU02

**UTC:** 2026-08-18T20:57:17Z  
**Source:** production `INTAKE-BEFORE.json` (password never printed)

## Storage owner

`RECIPIENT STORAGE OWNER IDENTIFIED`

- Option: `fp02_mail_ops`
- Nested key: `recipients`
- Class: `Shpigovsky\Core\Mail\MailOps`
- Secret option (untouched): `fp02_mailbox_auth`

Not ACF. Not a single scalar option. Not a competing SMTP plugin.

## Raw type

`serialized_array_of_rows` — WordPress option array of `{ email, label }`.

Example (operator-entered, preserved 1:1):

```json
[
  {
    "email": "client.leads@polygon-ws.ru",
    "label": "MetaCODE"
  }
]
```

UI before this wave padded a second **blank** row in HTML (`count < 2`). That blank row was not stored. There was **no** Add/Remove control (`add_button=false`, `remove_button=false`).

## Target (unchanged owner)

Same option and key. Canonical record:

- `recipient_email` stored as `email`
- `recipient_label` stored as `label`
- first row = primary
- additional rows = copies of the same lead mail operation

Idempotent normalize accepts the current rows as-is (also string emails and `recipient_email` aliases if ever present). No re-entry required.
