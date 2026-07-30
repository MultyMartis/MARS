# TELEGRAM LIVE ACCEPTANCE v1

Operator-private sandbox only. Identifiers redacted.

| # | Fixture | Delivered | Notes |
|---|---------|-----------|-------|
| 1 | TG1 named SEO complete | PASS | q=ok; dup=new; mode=ai_off |
| 2 | TG2 unnamed Audit missing site | PASS | q=needs_data; dup=new; mode=ai_off |
| 3 | TG3 no-contact malformed | PASS | q=bad; dup=new; mode=ai_off |
| 4 | TG4 same-message reprocessing | PASS | q=needs_data; dup=reprocessed; mode=ai_off |
| 5 | TG5 repeat phone | PASS | q=needs_data; dup=repeat; mode=ai_off |
| 6 | TG6 site-only possible repeat | PASS | q=needs_data; dup=possible; mode=ai_off |
| 7 | TG7 AI invalid-JSON fallback | PASS | q=needs_data; dup=new; mode=ai_fallback |
| 8 | TG8 unsafe-deadline fallback | PASS | q=needs_data; dup=new; mode=ai_fallback |
| 9 | TG9 special-character case | PASS | q=needs_data; dup=new; mode=ai_off |

Footer on every card: `Тестовая заявка · PHASE 3B.3`

Delivered count: **9 / 9**
