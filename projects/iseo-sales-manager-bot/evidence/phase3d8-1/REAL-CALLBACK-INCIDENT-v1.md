# REAL CALLBACK INCIDENT v1

**Phase:** 3D.8.1  
**Window:** ~2026-08-04 20:30–20:50 UTC (operator ~03:35 +07) and follow-up real clicks ~20:56 UTC

## Operator observation

Buttons visible on newer lead; moderator «Мопс» pressed processed; Telegram loading state without clear final UX; earlier `✅ Обработан` demo existed.

## Findings (sanitized)

| Item | Result |
|------|--------|
| Real Telegram Trigger callbacks in operator window | **None** — only harness webhook executions |
| Real moderator callbacks | Executions **21584**, **21585** @ ~20:56 UTC — Telegram Trigger |
| Actor | Test moderator (opaque hash `h:518CC34C4C0F`) |
| Authorization | `authorized=true`, `manager_action_authorized=true` |
| Callback shape | `sm:p:<12-char-token>` |
| Outcome | **idempotent** — CLEAN already `processed` |
| answerCallbackQuery | Ran successfully on real clicks |
| Safe Telegram Reply | Ran with «уже отмечен» text |
| Card multi-copy edit | **Not performed** on idempotent path (pre-repair) |
| LEAD_DELIVERIES read | Failed: sheet tab missing |

## Incident chain

1. Phase 3D.8 harness webhook mutated the lead to processed and edited **one** initiator card.
2. During harness, Admin was briefly reconfigured — real clicks around button-restore window were not observed as Telegram Trigger executions.
3. Later real moderator clicks correctly authorized but hit already-processed lifecycle.

## Verdict for this incident

Real user callback path **exists** and authorizes, but **did not prove** end-to-end pending→processed mutation + multi-copy sync on the clicked lead.
