# PENDING VIEW CONTRACT v1

**Function:** `buildPendingView(rows, opts)` in `implementation/runtime-libs/pending-leads-lib.mjs`.

## Pipeline

1. Filter out non-object rows.
2. Drop technical-retry-only rows.
3. Drop probable-invalid/empty-shell rows.
4. Resolve lifecycle (`resolveLifecycle`) — keep only `pending`.
5. Drop probable-test rows unless `includeTests=true`.
6. Deduplicate by **business key** (`businessKey(r)`), keeping the most informative/most recent duplicate (`prefer()` — newest timestamp wins; ties broken by field-completeness score).
7. Compute per-item view fields (age, display strings, safe fallbacks) and a deterministic **oldest-first** sort key.
8. Bucket items by age (`under_2h`, `from_2h_to_24h`, `over_24h`, `unknown`).

## Business key precedence

`stable_lead_ref` → `lead_id` → Gmail message id → fallback composite (`name|site|created_at`). Guarantees one logical lead is never double-counted even if RAW/CLEAN carries more than one physical row for it (checked by harness #5: "One logical lead counted once").

## Per-item output fields (no PII beyond what the card already shows)

`stable_lead_ref`, `received_at`, `age_minutes`/`age_hours`/`age_days`/`age_display`, `client_display_name`, `contact_summary`, `website_summary`, `resolved_service_label`, `request_summary` (truncated to 120 chars), `lifecycle`, `is_probable_test`, `source_context_short`, `first_reply_ready`, `delivery_state_summary`, `pending_sort_key`.

Fallback labels reuse the existing manager-card vocabulary (`Без имени`, `Контакт не указан`, `Сайт не указан`, `Задача требует уточнения`) — no new terms invented.

## Ordering

Oldest-first (`pending_sort_key` = zero-padded timestamp + stable ref; missing timestamp sorts to the end). Rationale: operational attention order — the longest-waiting lead surfaces first for both `/pending_leads` and the reminder message (harness #9).

## Aggregate fields

`total`, `buckets`, `oldest_age_minutes`, `oldest_age_display`, `warnings` (e.g. `missing_timestamp`, deduplicated).

## Harness coverage

Checks 1–10, 43–44, X1–X2 in `implementation/harness/phase3f1-harness.mjs`.

*Related: [../../architecture/PENDING-LEADS-VIEW-v1.md](../../architecture/PENDING-LEADS-VIEW-v1.md), [PENDING-SOURCE-FORENSIC-v1.md](PENDING-SOURCE-FORENSIC-v1.md).*
