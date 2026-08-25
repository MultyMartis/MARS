# Deferred Product Roadmap

Roadmap only. None of these items are current stable production behavior unless a later accepted baseline says so.

## ACCESS Vs DELIVERY

Separate who may use the system from who receives operational delivery. Access controls admin/callback rights; delivery controls notification recipients.

## DND

Potential do-not-disturb rules for manager notifications. Must define emergency exceptions, timezone, and backlog behavior before implementation.

## Delivery Modes

Potential modes:

- immediate lead cards;
- daily digest;
- pending reminder;
- admin-only diagnostics.

Each mode needs explicit lifecycle non-effects.

## Anomaly Monitor

Potential observer for duplicate spikes, failed callbacks, Sheets/DB write drift, reminder misses, and Telegram delivery failures. This would be monitoring, not autonomous repair by default.

## `/announce`

Potential admin command for operator-authored announcements. Must include authorization, preview, confirmation, and audit event.

## `/admin` Panel

Potential Telegram admin panel for safe controls. Must avoid exposing secrets and avoid becoming an implicit CRM.

## Delivery Ownership

If delivery assignment is added, it needs a product charter, status model, and rollback. It is not part of the stable Sales Manager v2 baseline.

## AI Reintroduction

AI can be considered only with a separate safety plan, observability, deterministic fallback, and explicit evidence. Current stable production is AI OFF.

