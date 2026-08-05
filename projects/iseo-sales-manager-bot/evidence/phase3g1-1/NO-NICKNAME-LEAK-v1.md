# NO NICKNAME LEAK — Phase 3G.1.1

**Invariant:** Internal display token `Мопс` (MOD_A) must **never** appear in client-facing copy.

## Scope

- T1 acceptance set (`T1-PERSONALIZED-ACCEPTANCE-v1.md`)
- T3 acceptance set (`T3-PERSONALIZED-ACCEPTANCE-v1.md`)
- Fail-closed harness band (Phase 3G.1.1 subset)

## Results

| Surface | `Мопс` occurrences |
|---------|-------------------:|
| ADMIN_A client copy (T1) | 0 |
| MOD_A client copy (T1) | 0 |
| ADMIN_A client copy (T3) | 0 |
| MOD_A client copy (T3) | 0 |
| Harness personalization cases | 0 |

## Approved substitution

MOD_A → client-facing **Михаил** via `reply_sender_name` profile field only.

## Forbidden fallbacks (verified absent)

- Telegram display name
- Username-shaped display label
- Actor label
- Role label (`Модератор`, `Админ`)

## Harness cases (fail-closed band)

- PASS — no display-name fallback
- PASS — no nickname fallback
- PASS — no username fallback

## Verdict

**PASS** — zero nickname leak in acceptance set and harness.
