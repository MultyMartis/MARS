# SITE-002 — Client Ops Telegram Product Contract

**Bot display name:** Монитор bzpm.ru — MetaCODE  
**Access:** operator-authorized only.

## Accepted message types (current generation)

1. Import success
2. Incomplete import / offers missing (ATTENTION)
3. Import failure
4. No-import watchdog
5. Other accepted operational events only if currently implemented in workflow

## UX rules

- Russian language
- Concise, operator-readable
- Local time (Europe/Moscow operational context)
- No raw internal enums as primary text
- No synthetic counts
- Factual filenames when relevant
- No secrets / tokens / credentials
- Avoid low-level implementation noise (PHP class names, stack traces)

## Parse mode

Use whatever is currently configured in the live n8n workflow (often HTML/Markdown-compatible formatting). Do not invent a new parse mode in docs-only waves; verify live node settings when changing UX.
