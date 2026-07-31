# INVALID-CONTACT-RENDERING-v1

Archive + live formatters + callback edit reject:

- `#ERROR!`, `#VALUE!`, `#REF!`, `#N/A`
- `Formula parse error`
- `UNKNOWN`, `44`, empty/generic dashes

Behavior:

- omit invalid field from card
- archive may show `⚠️ Контакт в архивной записи повреждён` when the raw value is a Sheets error
- do not fabricate contacts from request text
