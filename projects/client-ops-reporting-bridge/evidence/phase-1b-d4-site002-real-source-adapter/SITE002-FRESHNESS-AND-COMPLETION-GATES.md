# Freshness and Completion Gates

## Completion (D4)

Require three JSON authorities present and parseable after firewall. No separate completion marker in hardening contract. Incomplete directory fails closed.

## Freshness

Offline historical fixtures allowed with pinned fixture-meta.now_utc. Existing STALE_AFTER_SECONDS=93600 => BLOCKED. Future live: explicit max-age or operator confirmation (proposed). No watcher/polling.
