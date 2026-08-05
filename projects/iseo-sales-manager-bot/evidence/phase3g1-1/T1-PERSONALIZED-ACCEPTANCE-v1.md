# T1 PERSONALIZED ACCEPTANCE — Phase 3G.1.1

**Template:** `T1_EXISTING_SITE_GROWTH`  
**Site fixture:** `t1-accept.iseo-phase3g11.local` (sanitized)  
**geo_ai_clause:** false

## Recipients exercised

| Label | Expected client intro line |
|-------|---------------------------|
| ADMIN_A | `Меня зовут Андрей, компания INTLSEO` |
| MOD_A | `Меня зовут Михаил, компания INTLSEO` |

## Acceptance checks

| Check | ADMIN_A | MOD_A |
|-------|---------|-------|
| Template id | T1_EXISTING_SITE_GROWTH | T1_EXISTING_SITE_GROWTH |
| Site line present | yes | yes |
| Audit CTA present | yes | yes |
| `Мопс` in client copy | 0 | 0 |
| Manager guidance outside `<pre>` | yes | yes |
| Telegram delivery success | yes | yes |

## Copy structure (shared)

- Greeting + personalized name + INTLSEO + site reference + audit/materials CTA
- Guidance block: `💡 Подсказка менеджеру` — separate from copy `<pre>`
- No auto-send disclaimer outside copy block

## Operator note

Accept **latest acceptance-set cards** only. Earlier exploratory inject batches may show empty copy (test_suppressed before profile repair). Do not treat those as regression.

## Cross-reference

- `NO-NICKNAME-LEAK-v1.md`
- `TEST-DELIVERY-IDEMPOTENCY-v1.md`
