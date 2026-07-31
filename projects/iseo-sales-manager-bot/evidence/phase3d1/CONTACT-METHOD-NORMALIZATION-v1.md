# CONTACT-METHOD-NORMALIZATION-v1

**Phase:** 3D.1

## Rules

1. Read `Способ связи` when present.
2. Parse `Контакт` according to method; also honor direct `Телефон:` / `Email:` labels.
3. Phone validity: digit length 10–15 after stripping non-digits; display form may keep `+`, spaces, parentheses, hyphens.
4. Email: standard local@domain check; lowercased for storage.
5. Messenger: `@handle`, `t.me/...`, or Telegram method bare username.
6. Invalid tokens never become primary contact.

## Quality impact

Valid phone/email/messenger ⇒ must **not** classify as `Недостаточно для связи` / `bad` solely for missing contact.

## Fixtures covering this

F-AF01–F-AF05, F-AF07–F-AF09, F-AF11–F-AF12 (see PARSER-FIXTURE-ACCEPTANCE-v1).
