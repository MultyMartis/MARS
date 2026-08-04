# REPORT — iseo-sales-manager-bot phase 3d7.1 duplicate delivery containment

**Date:** 2026-08-04  
**Process-line:** ISEO-SALES-MANAGER-BOT — PHASE 3D.7.1 EMERGENCY DUPLICATE DELIVERY CONTAINMENT  
**Scope:** `projects/iseo-sales-manager-bot/**` (clean worktree from `origin/mars/canonical-post-recovery`)

## Verdict

**`COMPLETE — PATCH READY, LIVE NO-DUPLICATE CONFIRMATION PENDING`**

Repeated production delivery loop is **stopped**. Claim-before-send patch is live on Operational.dev. Operator confirmation of a fresh four-recipient synthetic (exactly one card each) remains pending.

## Exact root cause

`Stamp Delivery Result` used `runOnceForEachItem` and called `$input.first()`. After each successful 4-way Telegram fan-out it threw (`Can't use .first() here`), so LEAD_DELIVERIES was never written and Gmail never received PROCESSED / intake removal. Every ~30s poll reprocessed the same Gmail message as `duplicate_status=new` with `skip_telegram=false` for all recipients.

## Counts

| Metric | Value |
|---|---:|
| Unique business leads | 1 |
| Repeated Operational executions | 16 (20637–20652) |
| Telegram cards sent | **64** |
| Affected recipients | **4** (16 cards each) |
| LEAD_DELIVERIES rows during incident | 0 |
| Post-activate monitored sends | **0** |

## Delivery key behavior

Keys were already deterministic (`lead_delivery:<stable>:<u:HASH>`) and stable across polls. Idempotency failed because ledger writes never committed after send.

## Claim-before-send repair

Added: Prepare Delivery Claims → Upsert LEAD_DELIVERIES Claim → Restore Claimed Delivery Items → IF Need Telegram Send → … → Stamp (`runOnceForAllItems`) → Append LEAD_DELIVERIES → Aggregate (admin-anchor finalize).

## Gmail finalization

Policy: finalize when Admin-anchor delivered; do not wait for all moderators. Affected message finalized during reconciliation sidecar.

## Affected-lead reconciliation

Four delivered ledger rows + CONFIG `tg_delivered:*` + Gmail labels. No extra Telegram cards. Duplicate historical Telegram messages preserved.

## Repeated-poll harness

**26/26 PASS** (required cases 1–23).

## Final workflow states

| Workflow | Active |
|---|---|
| Operational.dev `xSnXPy8cEHoZw6xG` | YES |
| Admin.dev `wLrLp4WQHm1VJmxz` | YES |
| Sales-Manager-v2 `h8I2Tl2yl4uzhUnB` | NO |

- Active Gmail intake count: **1**
- AI calls: **0** (OpenRouter disabled)
- Client messages: **0**
- Workflows created: **0**

## Evidence

`projects/iseo-sales-manager-bot/evidence/phase3d7-1/`

## Git

Clean worktree commit + push to `origin/mars/canonical-post-recovery` (no force; dirty main index untouched).

## Operator next step (Task M)

Send **one** dedicated synthetic lead with a unique identity only when ready to watch Telegram. Confirm exactly one card each for Андрей / Оля / Мопс / Никита across ≥3 further poll intervals before button sync testing.

## Execution safety

- cwd / worktree under `X:\AI MARS` / `X:\AI MARS STORAGE`
- scope lock honored: yes (`projects/iseo-sales-manager-bot/**`)
- destructive ops: none
- protected zone touch: none
