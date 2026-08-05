# Telegram parse safety — Phase 3G.2.1

**Parse mode:** HTML (Safe Telegram Reply unchanged).

## Rules applied

- `cmdHtml` wraps only slash tokens in `<code>` after `escHtml`.
- Placeholders such as `<номер>` / `<имя>` rendered as `&lt;номер&gt;` / `&lt;имя&gt;` outside code.
- Dynamic values (AI/reminder labels, reply names) passed through `escHtml`.
- Config values are plain Russian labels — no raw IDs.

## Checks

| Check | Result |
|-------|--------|
| Admin help contains `&lt;номер&gt;` | pass (harness) |
| Moderator start name escaped | pass (builder uses escHtml) |
| No literal unescaped `<номер>` in help | pass |
