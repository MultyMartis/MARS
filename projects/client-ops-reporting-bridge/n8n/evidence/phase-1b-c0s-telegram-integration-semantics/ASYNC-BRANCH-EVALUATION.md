# Async branch evaluation — Phase 1B-C0S

## Topology considered

```
Webhook
→ Accepted Gate
├→ Respond to Webhook
└→ Telegram sendMessage
```

## Evidence used

- Level 1 sequential continuation after `Respond to Webhook` is **supported** on this host.
- Level 2 sequential Telegram after Respond delivered **exactly one** message with final marker.
- No second live Telegram message was authorized for a branch topology test (message cap = 1).

## Ordering

Parallel / fan-out branches do **not** guarantee Telegram-before or after Respond timing without additional synchronization. On this installation, sequential Pattern B already preserves:

- deterministic webhook HTTP 202 before Telegram work completes;
- accepted-path-only delivery when gated upstream;
- single send when a single Telegram node is used.

## Duplicate risk

Async branches increase duplicate-send risk if both an accepted sequential path and a parallel branch could fire, or if retries re-enter both arms. Pattern B sequential graph avoids that class of risk for the proposed Client Ops apply.

## Selection

**Not selected** as the primary Client Ops pattern.

`ASYNC_BRANCH_PATTERN_CONFIRMED` is **not** claimed.

Selected: **`PATTERN_B_CONFIRMED`** (sequential Respond → Telegram).
