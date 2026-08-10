# CONTACT #ERROR ROOT CAUSE

## Proven cause
Resurface builder used:

```js
escapeHtml(o.primary_contact || o.phone || '—')
```

`lead_clean_v2.primary_contact` can contain Google Sheets formula error tokens (`#ERROR!`).
Canonical formatter never uses `primary_contact` for display; it uses `phone`/`email`/`messenger` through `isValidContactValue`, which rejects `#ERROR!`.

## Per alias
- **REAL_REOPEN_A**: ROOT_CAUSE — resurface builder used lead_clean.primary_contact (formula error token) instead of canonical phone/email via isValidContactValue
- **REAL_REOPEN_B**: ROOT_CAUSE — resurface builder used lead_clean.primary_contact (formula error token) instead of canonical phone/email via isValidContactValue
- **REAL_REOPEN_C**: no formula error on this lead for primary_contact||phone path

## Repair
- Use canonical contact resolver (`sanitizeContactField` + phone/email/messenger)
- Never render formula-error tokens
