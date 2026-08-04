# REPORT — ISEO SALES MANAGER BOT PHASE 3D.7 MULTI-RECIPIENT LEAD DELIVERY AND SYNCHRONIZED ACTION CARDS

**Date:** 2026-08-04  
**Verdict:** **COMPLETE — DELIVERY READY, LIVE FOUR-USER CONFIRMATION PENDING**

## Summary

Root cause: Operational.dev sent every lead to a single CONFIG `telegram_manager_chat_id` (Андрей), ignoring ACCESS_CONTROL staff. Phase 3D.7 deploys ACCESS_CONTROL fan-out, per-recipient idempotency (`LEAD_DELIVERIES`), Admin-anchor finalization, and multi-copy lifecycle sync on Admin.dev.

## Root cause

Single CONFIG destination on both Telegram send nodes. No ACCESS_CONTROL read in Operational pre-patch. Lead-level delivery guard only.

## Recipient selection / eligibility

Active admin+moderator with confirmed private chat target (`telegram_user_id` = private chat id). Public/pending/revoked/blocked/missing chat/duplicates excluded.

## Fan-out / idempotency / LEAD_DELIVERIES

Expand after Format; key `lead_delivery:<lead>:<recipient_ref>`; upsert LEAD_DELIVERIES; Aggregate Admin-anchor finalize before Gmail PROCESSED.

## Failure isolation / button auth / sync

Per-recipient stamp; moderator failures isolated; callbacks re-check ACCESS_CONTROL; Expand Card Sync edits all delivered copies.

## Live acceptance

Harness **37/37 PASS**. Operator four-user confirmation **PENDING**.

## Final access / workflows

- Expected active staff recipients: Admin 1 + moderators 3 (confirm Nikita private-chat eligibility via `/delivery_users`)
- Sales-Manager-v2 inactive; Operational active (42 nodes); Admin active (57 nodes)
- AI calls=0 · client messages=0 · workflows created=0 · rollback=no

## Commit / push

- Commit: `ce06f240` — `feat(iseo-sales-manager-bot): deliver leads to all active moderators`
- Pushed to `origin/mars/canonical-post-recovery` (no force)
