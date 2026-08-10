# AUTHORITATIVE CARD REGISTRY

Contract: `iseo-lead-card-instance-registry-v1`

Deployed into Admin node **Expand Card Sync Copies**.

## Rule
- Each business lead may have multiple Telegram card instances
- Exactly **one authoritative current card per recipient**
- Prefer latest `operator_resurface` delivery over older initial deliveries
- `superseded` / historical instances are ignored for current sync failure accounting

## Apply receipt
- at: `2026-08-10T09:41:23.472Z`
- checks: {"expand_authoritative":true,"expand_superseded_ignore":true,"agg_semantic_independent":true,"agg_spam_ack":true,"agg_reopen_ack":true,"admin_active":true}
