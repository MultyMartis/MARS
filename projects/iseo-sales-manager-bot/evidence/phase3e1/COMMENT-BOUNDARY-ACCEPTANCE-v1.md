# COMMENT BOUNDARY ACCEPTANCE v1 — Phase 3E.1

**Research:** [COMMENT-BOUNDARY-REQUIREMENTS-v1.md](../../research/parser-3.3/COMMENT-BOUNDARY-REQUIREMENTS-v1.md) — **implemented**  
**Harness:** H12–H15

## Accepted behaviors

1. Comment starts at recognized label; ends at next valid top-level label only.
2. Words «телефон» / «сайт» / «email» inside natural language do **not** terminate the comment without a label pattern.
3. Newline, CRLF, NBSP, collapsed lines supported.
4. Source page, form offer title, IP excluded from comment and Telegram body where required.
5. Truncation is stamped, not silent.

## Not accepted

- Mixing quoted prior mail / signature into current form comment without isolation.
- Bleeding «Отправлено со страницы» into client comment on cards.
