# PHASE-1B-C — Telegram Bot Intake and Sandbox Integration Preparation

**Date:** 2026-07-24
**Status:** COMPLETE for intake/preparation; semantics verified in Phase 1B-C0S — **READY** for sandbox integration apply (HITL)
**Follow-on:** Phase 1B-C0R2 chat target confirmed; Phase 1B-C0S `PATTERN_B_CONFIRMED` (see `PHASE-1B-C0S-TELEGRAM-INTEGRATION-SEMANTICS-VERIFICATION.md`); next is Phase 1B-C1
**Workflow:** `MARS Client Ops Bridge — bzpm.ru` (`tkM4H0G0gM3q9Foi`) — **unchanged, inactive**
**Telegram bot:** `@monitor_bzpm_metacode_bot` — display name exact match
**Telegram credential:** `MARS Client Ops Telegram — bzpm.ru` (`2bIC5376l7ElXb4B`) — **created, unbound**

## What was done

1. Verified local Telegram secret boundary (gitignored).
2. Validated bot via read-only `getMe` / `getWebhookInfo` / conditional `getUpdates`.
3. Confirmed n8n credential type `telegramApi` and create schema (`accessToken`, optional `baseUrl`).
4. Created exactly one dedicated n8n Telegram credential.
5. Prepared message contract and inactive proposed integration payload (not applied).
6. Did **not** send Telegram messages, update the Client Ops workflow, or activate it.

## Bot identity

| Field | Value |
|-------|-------|
| Bot ID | `8852310960` |
| Username | `monitor_bzpm_metacode_bot` |
| First name | `Монитор bzpm.ru — MetaCODE` |
| Required name | `Монитор bzpm.ru — MetaCODE` |
| Match | exact |
| Avatar | SAFE UNKNOWN (requirement: bzpm.ru logo) |

## Telegram webhook

Clear (empty URL). Credential create allowed.

## Chat target

`TELEGRAM_CHAT_TARGET_CONFIRMED` (Phase 1B-C0R2)

Phase 1B-C initial discovery: 0 updates.
Phase 1B-C0 retry: 0 updates.
Phase 1B-C0R2 final retry: 1 private update; chat ID confirmed in ignored local target file.

## Credential

| Field | Value |
|-------|-------|
| Name | `MARS Client Ops Telegram — bzpm.ru` |
| Type | `telegramApi` |
| ID | `2bIC5376l7ElXb4B` |
| Bound to Client Ops workflow | NO |
| Token visible in metadata | NO |

## Proposed integration (not applied)

- Pattern **B**: Respond to Webhook first, then Telegram `sendMessage` on accepted path only — **runtime-confirmed** in Phase 1B-C0S.
- Credential reference: `telegramApi` → dedicated credential above.
- Chat ID confirmed in Phase 1B-C0R2 (proposal not applied).
- Header Auth, deferred dedupe, inactive state preserved.

## Readiness verdict

`READY_FOR_TELEGRAM_SANDBOX_INTEGRATION_APPLY` (after Phase 1B-C0S)

Blocking gate cleared: Pattern B continuation-after-Respond = `PATTERN_B_CONFIRMED`.

## Next recommendation

**Phase 1B-C1 — Telegram Sandbox Integration Controlled Apply**

## Evidence

`n8n/evidence/phase-1b-c-telegram-bot-intake/` + `n8n/evidence/phase-1b-c0s-telegram-integration-semantics/`
