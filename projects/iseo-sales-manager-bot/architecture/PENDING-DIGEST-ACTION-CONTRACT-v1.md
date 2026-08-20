# PENDING DIGEST ACTION CONTRACT v1

**Contract id:** `iseo-pending-digest-action-v1.0`  
**Phase:** 3H.10  
**Status:** deployed (Admin.dev callback path)

## Purpose

Resolve digest lead actions to the **exact stable lead** and show a compact actionable view using **current** authoritative state.

## Callback namespace

| Prefix | Meaning |
|--------|---------|
| `sm:q:<opaque>` | Open compact lead from digest |
| `sm:q:__all__` | Open `/pending_leads` equivalent |
| `sm:f:<opaque>` | Full card (canonical renderer) |

Opaque token derived from stable `lead_id` (not Sheet row, not PII).

## Compact view fields

Client · status · human category · received (MSK) · age · safe contact · short context

## Actions (reuse existing contracts)

- ✅ Обработано / 🚫 Спам — same lifecycle as lead cards
- 📄 Исходная заявка — repaired raw-access permission contract
- 🟢 Полная карточка — canonical full-card renderer

## Stale digest

Snapshot is not authority. Click resolves **current** state (e.g. Spam if already marked).

## Concurrent staff

Idempotent transitions; no duplicate LEAD_EVENTS for repeated identical terminal actions.
