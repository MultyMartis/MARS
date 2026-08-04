# ACTOR DISPLAY PRECEDENCE v1

1. Non-empty normalized ACCESS_CONTROL display_name
2. ACCESS_CONTROL username as @username
3. Neutral fallback сотрудник

Optional combined form when both exist and concise:

Display Name · @username

## Must not display

- raw Telegram user id
- chat id
- actor hash
- approval code
- registry row number

## Escaping

HTML-escape display name and username before card insert. Bound label length (64).
