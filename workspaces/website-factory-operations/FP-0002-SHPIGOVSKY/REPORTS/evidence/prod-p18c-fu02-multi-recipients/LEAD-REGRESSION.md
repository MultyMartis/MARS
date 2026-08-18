# Lead / frontend regression

| Check | Result |
|-------|--------|
| Consultation form on privacy (inner origin) | present (`data-lead-form`) |
| Persist QA | `accepted=true`, `mail_attempted=false`, status `SMTP_PENDING` (config complete + suppression ON) |
| One lead row | `is_qa=1` then deleted; 0 QA rows left |
| Real SMTP send | none |
| Metrika goal | still empty (preserved) |
| UTM | `utm_source=p18c-fu02` captured on QA path |
| Indexing | CLOSED |

`SMTP_PENDING` (not `MAIL_SUPPRESSED`) is expected now that SMTP fields are complete while outbound remains suppressed.
