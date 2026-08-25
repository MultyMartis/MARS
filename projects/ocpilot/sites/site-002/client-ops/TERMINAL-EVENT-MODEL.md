# SITE-002 — Terminal State / Event Model

## Core concepts

| Concept | Role |
|---------|------|
| `run_id` | Unique import run identity (authoritative on server terminal) |
| `trigger_source` | `SCHEDULED` \| `ADMIN_MANUAL` |
| Catalog phase | Result of `import0_*.xml` processing |
| Offers phase | Result of `offers0_*.xml` processing |
| Classification | Success / ATTENTION / Failure (+ codes e.g. `OFFERS_INPUT_MISSING`) |
| Terminal timestamp | When run became terminal |
| Dispatcher status | PENDING / SENDING / SENT / FAILED_* (conceptual; see dispatcher) |
| `event_id` | Client Ops event identity for dedupe/delivery |
| Delivery status | Data Table / n8n delivery state (`FIRST_SEEN` → `SENT`, etc.) |

## Idempotency boundary

| Case | Expected |
|------|----------|
| Same exact run replay | Deduped — do not spam Telegram |
| New daily/new run with same recurring condition | **New independent event** — must notify |

Same condition on a later run ≠ same event as yesterday.

## Authority

Terminal run state on server is **run truth**. n8n/Data Table is **delivery/dedupe memory**, not a replacement for terminal.
