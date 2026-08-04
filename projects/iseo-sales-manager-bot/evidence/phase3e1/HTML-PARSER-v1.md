# HTML PARSER v1 — Phase 3E.1

**Module:** `implementation/parser-fixtures/parse-lead-lib.mjs`  
**Harness:** H01

## Behavior

1. Accept HTML body from form mail (`<br>`, `<b>`, entities).
2. `htmlToPlainText` → labeled extraction via `LABEL_DEFS` (От кого / Телефон / Адрес сайта / Комментарий / Отправлено со страницы / IP / …).
3. Comment ends at next top-level label; IP and source-page do not enter `comment_normalized`.
4. Site classification runs after extraction.

## Acceptance

- Labeled name, site, comment recovered from HTML fixture.
- Page / IP separated from client comment.
- Synthetic only (`example` / documentation IPs).
