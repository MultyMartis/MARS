# FP-0002 V9-06E1 Static Legal Source Extraction v1

**Phase:** V9-06E1 Legal Static Copy Seed  
**Date:** 2026-07-06  
**Authority:** `workspaces/fp-0002-shpigovsky-v9/src/partials/sections/legal/content/`

## Summary

Four static V9 legal body partials extracted one-to-one for WordPress `post_content` seeding. Source preference: `src` body partials (not dist assembly wrappers).

| Legal page | Source file | Length | SHA256 (prefix) | Result |
|---|---|---:|---|---|
| Политика конфиденциальности | `privacy-policy-body.html` | 7472 | `588845cf` | FOUND |
| Пользовательское соглашение | `user-agreement-body.html` | 5696 | `47e15c92` | FOUND |
| Согласие на обработку ПД | `consent-personal-data-body.html` | 3054 | `8ac84893` | FOUND |
| Политика Cookie-файлов | `cookie-files-policy-body.html` | 6226 | `a06f0209` | FOUND |

## Extraction method

- Read UTF-8 body partial from static V9 `src`.
- Preserve headings, paragraphs, lists, tables, and inline links.
- No text rewriting; DEMO tokens retained as in static source.
- Dist pages verified present for cross-check only.

Evidence: `validation/v9-06e1-legal-static-copy-seed/static-legal-source-extraction.json`
