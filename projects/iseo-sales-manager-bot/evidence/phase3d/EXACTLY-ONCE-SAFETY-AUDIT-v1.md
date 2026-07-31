# EXACTLY-ONCE-SAFETY-AUDIT-v1

**Phase:** 3D  
**Target:** Operational.dev (same workflow ID; no replacement workflow)

## Identity mapping

| Check | Result |
|-------|--------|
| One Gmail message → stable `lead_id` | **yes** (parser lead_id retained across retries) |
| Same message after PROCESSED cannot create another card | **yes** (incoming removed; not eligible) |
| Reprocess only when prior processing incomplete | **yes** (incoming retained until TG success + finalize) |
| Exact DEDUP match by normalized_value | **patched in 3D** (was type-only; risk of false reprocessed) |

## Write policies

| Store | Policy | Audit note |
|-------|--------|------------|
| RAW | Immutable append | Retries may append additional RAW rows; business identity remains message/lead |
| CLEAN | Intended upsert; live node still `append` | Duplicate CLEAN rows possible on retry — documented risk; business lead identity via `lead_id` / `source_message_id` |
| DEDUP_INDEX | Key rows for identity | Primary gmail key fields stamped on Classify output after 3D |
| LEAD_EVENTS | Append | Retries/events allowed without new business lead |

## Telegram / Gmail gates

| Check | Result |
|-------|--------|
| Telegram uses CONFIG manager destination only | **yes** (`Normalize CONFIG` chatId expression) |
| Gmail finalization only after Telegram success | **yes** (IF Telegram Success → PROCESSED → remove incoming) |
| DEDUP lookup cannot replace lead/config fields | **yes** (Classify bases on Merge AI or Fallback) |
| Delivery idempotency before resend | **yes** (CONFIG `tg_delivered:<gmail_message_id>`) |
| Bounded retry | **yes** (max 5 attempts; exhaustion → error path) |
| Resume finalize without resend | **yes** (`IF Need Telegram Send` → Skip Pass → Result Gate → PROCESSED) |

## Residual risks

- CLEAN node operation remains `append` (not true Sheets upsert) — row-level duplicates possible on retry; mitigated by delivery idempotency for Telegram fan-out.
- DEDUP Lookup still reads index broadly; Classify now matches exact normalized values.
- CONFIG accumulates per-message delivery keys — acceptable for v1; prune policy later if needed.

## Verdict

Exactly-once **Telegram delivery** after successful send is enforced. Business lead identity is stable. Sheet append duplication on incomplete retries remains a durability quirk, not a manager-card flood path.
