# REMINDER DELIVERY IDEMPOTENCY v1

**Product:** i-SEO Sales Manager Bot
**Phase:** 3F.1
**Scope:** batch (multi-recipient) idempotency for the daily pending-lead reminder
**Companion to:** `DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md` (lead-card delivery — unchanged, not reused code path, same *policy family*)

---

## 1. Why a reminder needs its own idempotency layer

Lead-card delivery is idempotent **per lead**. The reminder is idempotent **per (calendar window, recipient)** — a different unit, because a reminder is a scheduled batch notification with no single triggering business event to key off of. Reusing the lead-delivery ledger's key shape (`lead_delivery:<stable_lead_ref>:<recipient_ref>`) would not fit; a new, parallel-but-analogous ledger was required.

## 2. Two-layer model

| Layer | Mechanism | Prevents |
|---|---|---|
| Window-level | `pending_reminder_last_window` CONFIG key compared against the deterministic window key | The same calendar window firing more than once across the multiple 15-minute schedule checks inside the due period, and after operator restart/downtime |
| Recipient-level | `REMINDER_DELIVERIES` row per `(window, recipient)`, claimed before send | One recipient succeeding while another fails, without resending the successful recipient on the next check |

## 3. Window key

`pending-reminder:<YYYY-MM-DD>:<HH:MM>:<timezone>` — pure function of configured schedule + calendar date, no execution id, no PII. See `evidence/phase3f1/REMINDER-WINDOW-KEY-v1.md`.

## 4. Claim before send

Before any Telegram send is attempted for a recipient, a `REMINDER_DELIVERIES` row is written with `status=claimed`, `claimed_at` set. Only after a successful send does the row become `status=delivered` with `sent_at` set. This mirrors the claim-before-send discipline already proven for lead cards.

## 5. Fail-closed table

| Condition | Result |
|---|---|
| `REMINDER_DELIVERIES` read fails | Zero sends this tick (cannot prove no prior claim exists) |
| Claim write fails for a recipient | Zero send for that recipient |
| Telegram send succeeds, stamp write uncertain | Row remains `claimed`; treated as `reconciliation_required`, never blindly resent |
| A recipient already `delivered` for this window | Skipped on any later check |

## 6. Google Sheets limitation carried over

Same caveat as lead delivery: Google Sheets has no atomic compare-and-swap. Claim → send → stamp is best-effort sequential, not transactional. The documented target is **at-most-once send with reconciliation**, not exactly-once under every failure mode.

## 7. Harness and live coverage

Offline: `implementation/harness/phase3f1-harness.mjs` checks #24–#36 (schedule + idempotency). Live: `evidence/phase3f1/CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md` — a real Sheets quota condition was hit before recipient claim, and the engine correctly produced zero sends rather than a partial/duplicate attempt.

---

*Related: [PENDING-REMINDER-v1.md](PENDING-REMINDER-v1.md), `../evidence/phase3f1/REMINDER-DELIVERY-LEDGER-v1.md`, `../evidence/phase3f1/REMINDER-IDEMPOTENCY-v1.md`.*
