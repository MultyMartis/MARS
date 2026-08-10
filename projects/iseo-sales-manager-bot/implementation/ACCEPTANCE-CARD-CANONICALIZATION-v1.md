# ACCEPTANCE CARD CANONICALIZATION — Phase 3H.7.3.1

## Problem
After Phase 3H.7.3 parity repair, live Spam/Processed/Reopen still rewrote authoritative Telegram cards via reduced `buildFinalCard`, collapsing production body to status-only.

## Repair
1. Replace reduced callback edit body with full canonical status card text (`iseo-canonical-lead-card-renderer-v1` contract).
2. Re-canonicalize REAL_REOPEN_A/B/C current cards (12/12) without new LEADS rows.
3. Preserve each lead’s actual status (pending/spam) and matching keyboards.
4. Prove full body survives Spam ↔ Reopen on one acceptance lead.

## Non-goals
- No AI enablement
- No new workflows
- No customer auto-send
- No redesign of intake/parser/reminders
