# PENDING REMINDER v1

> **Production supersession (2026-08-17):** Reminders are **enabled** in production CONFIG (`pending_reminders_enabled=true`), Mon–Fri **10:00 Europe/Moscow**, weekday fail-close gate active. Canonical: [baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md). The historical `enabled=false` status line below is obsolete for live production.

**Product:** i-SEO Sales Manager Bot
**Phase:** 3F.1
**Scope:** daily scheduled reminder for unresolved pending leads
**Status:** implemented, `enabled=false` in production — activation is a separate operator decision
**Version:** `pending_reminder_version = sm-pending-reminder-v1.0`

Supersedes: `product/PENDING-LEAD-REMINDER-SPEC-v1-DRAFT.md` (draft is retained with a pointer to this implemented v1).

---

## 1. Placement

The reminder engine is an **internal addition to Admin.dev** (same workflow ID `wLrLp4WQHm1VJmxz`), triggered by a **15-minute internal Schedule Trigger** node. It is explicitly **not** a third workflow and does not touch Operational.dev.

## 2. Pipeline

```
Schedule Trigger (15m)
  → Read CONFIG (reminder keys)
  → isReminderWindowDue(now, cfg)
       due=false → stop (no further Sheets calls)
       due=true  → Read lead_clean_v2 → buildPendingView()
                     pending below min_count → stop
                     pending >= min_count →
                       Read ACCESS_CONTROL → selectActiveStaffRecipients()
                         → Read REMINDER_DELIVERIES (window) → per-recipient claim
                           → Telegram send → stamp REMINDER_DELIVERIES
                             → Write CONFIG (pending_reminder_last_window, *_last_success_at, …)
```

Every stage that cannot positively confirm "safe to proceed" stops the pipeline with zero sends (see §5).

## 3. Schedule gate

`isReminderWindowDue()` (`implementation/runtime-libs/pending-leads-lib.mjs`) — disabled check → config validity check → time-window check (configurable local time, timezone-aware, tolerant window for schedule drift) → already-completed-window check. See `evidence/phase3f1/REMINDER-SCHEDULE-GATE-v1.md`.

## 4. Recipient snapshot

Active Admin + active moderator only, from the same ACCESS_CONTROL registry the rest of the product uses — never a separate reminder-specific allowlist. Revoked/public/pending/blocked are always excluded. See `evidence/phase3f1/REMINDER-RECIPIENT-SNAPSHOT-v1.md`.

## 5. Fail-closed contract

| Failure | Outcome |
|---|---|
| Reminders disabled | zero sends |
| Invalid time/timezone config | zero sends |
| Zero pending leads in window | zero sends |
| Pending below configured minimum | zero sends |
| Already-completed window | zero sends |
| Ledger read error | zero sends (contract) |
| Claim failure for a recipient | zero sends for that recipient (contract) |
| Send success + stamp uncertainty | reconciliation required, no blind resend (contract) |

## 6. Idempotency

Two layers: a deterministic **window key** (`pending-reminder:<date>:<time>:<timezone>`, see `evidence/phase3f1/REMINDER-WINDOW-KEY-v1.md`) prevents the whole batch from repeating across the multiple 15-minute checks that fall inside one due window, and a per-`(window, recipient)` row in `REMINDER_DELIVERIES` prevents a single recipient from being resent if one recipient's send fails while another's succeeds. Full contract: `architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md`.

## 7. Message content

Compact Russian summary: total pending count, over-24h count if any, oldest-age display, and a pointer to `/pending_leads`. No lead PII, no lead ids. See `formatReminderMessage()` and `evidence/phase3f1/PENDING-LIST-ACCEPTANCE-v1.md`.

## 8. Administration

`/reminder_status` (staff read) and `/reminder_on` / `/reminder_off` / `/reminder_time` / `/reminder_timezone` / `/reminder_min` (Admin-only) — see `implementation/REMINDER-CONFIG-COMMANDS-v1.md` and `evidence/phase3f1/REMINDER-CONFIG-CONTRACT-v1.md`.

## 9. Production status

`pending_reminders_enabled=false`; default `10:00` `Europe/Moscow`. A controlled live exercise reached the ACCESS_CONTROL read step and correctly failed closed on a Sheets quota condition without sending — see `evidence/phase3f1/CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md`. Full production activation is a separate, later operator decision.

---

*Related: [PENDING-LEADS-VIEW-v1.md](PENDING-LEADS-VIEW-v1.md), [REMINDER-DELIVERY-IDEMPOTENCY-v1.md](REMINDER-DELIVERY-IDEMPOTENCY-v1.md), [../implementation/REMINDER-CONFIG-COMMANDS-v1.md](../implementation/REMINDER-CONFIG-COMMANDS-v1.md).*
