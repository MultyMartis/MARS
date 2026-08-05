# RECIPIENT REPLY STORAGE v1

**Phase:** 3G.1  
**Preference:** dedicated `RECIPIENT_REPLIES` table **or** additive extension of `LEAD_DELIVERIES`

## Shared vs personalized

| Store | Fields (conceptual) |
|-------|---------------------|
| `LEADS` | `selected_template_id`, versions, `reply_generation_mode`, `deterministic_task_summary`, geo flag — **no** per-recipient name |
| Recipient row | `lead_id`, recipient key, `customer_reply_text`, `reply_sender_name_snapshot`, `company_name_snapshot`, `recipient_reply_state`, `generated_at`, template/version stamps |

## Reporting

External reporting workbook stores **shared template id only**. Do not explode one lead into N reporting rows by recipient.

## Lifecycle

One business lead lifecycle; multiple delivery/recipient drafts do not multiply statistics counts.

## Live apply

Storage schema apply / live patch: pending or in progress until operator evidence filled.
