# T3 PERSONALIZED ACCEPTANCE — Phase 3G.1.1

**Template:** `T3_MEANINGFUL_TASK`  
**Deterministic task summary:** разобраться, почему снизился поисковый трафик

## Recipients exercised

| Label | Expected client intro line |
|-------|---------------------------|
| ADMIN_A | `Меня зовут Андрей, компания INTLSEO` |
| MOD_A | `Меня зовут Михаил, компания INTLSEO` |

## Acceptance checks

| Check | ADMIN_A | MOD_A |
|-------|---------|-------|
| Template id | T3_MEANINGFUL_TASK | T3_MEANINGFUL_TASK |
| Task summary in body | traffic-decline phrasing | traffic-decline phrasing |
| `Мопс` in client copy | 0 | 0 |
| Manager guidance outside `<pre>` | yes | yes |
| Telegram delivery success | yes | yes |

## Shared invariants

- One business fixture → two personalized recipient drafts
- Shared template metadata on LEADS / TEST_LEADS mirror row
- Per-recipient name snapshot immutable in recipient storage

## Operator note

Visual sign-off required in Telegram for T3 cards alongside T1. See `guides/OPERATOR-RUNBOOK-v1.md` Phase 3G.1.1 checklist.
