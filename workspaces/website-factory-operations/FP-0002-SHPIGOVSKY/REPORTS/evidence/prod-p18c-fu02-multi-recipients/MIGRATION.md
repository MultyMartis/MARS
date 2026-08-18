# Recipient migration

Storage owner already matched the target model (`fp02_mail_ops.recipients` = array of `{email,label}`).

Idempotent normalize:

- current array-of-rows → unchanged
- string email → one row
- `{recipient_email, recipient_label}` aliases → `{email, label}`
- case-insensitive dedupe; first label wins
- cap 20

Operator row before = after:

`client.leads@polygon-ws.ru` / `MetaCODE`

**EXISTING RECIPIENT PRESERVED 1:1** — no manual re-entry.
