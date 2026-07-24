# Phase 1B-D3 — Controlled Sequential Producer Connection Evidence

Sanitized evidence pack for the first real Client Ops producer HTTPS POST through the D2/D3 producer layer.

## Scope

- Synthetic source → producer → HTTPS → Header Auth → workflow → durable dedupe → FIRST_SEEN → Telegram
- Optional exact replay → DUPLICATE_SUPPRESSED → Telegram 0
- No SITE-002 runtime connection, no scheduler, no workflow graph mutation

## Status

See `D3-DECISION.json` readiness label.
