# Current Production Architecture

**Product:** i-SEO Sales Manager Bot  
**Stable designation:** Sales Manager v2 — Production Stable Baseline 2026-08-17  
**Status:** PRODUCTION STABLE  
**Freeze commit:** `35819a63bed132f2ccdb9e2d468e3ec3de9d23fe`  
**Canonical baseline:** [PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md)

This document describes the live production contour as accepted at the stable baseline. MARS documents the system; it does not execute the bot. Runtime authority is n8n at `n8n.ai-metacode.com`.

## Runtime Authority

| Area | Current production truth |
|------|--------------------------|
| Runtime host | `n8n.ai-metacode.com` |
| Operational workflow | `Operational.dev` / `xSnXPy8cEHoZw6xG` / active |
| Admin workflow | `Admin.dev` / `wLrLp4WQHm1VJmxz` / active |
| Inactive references | `Sales-Manager-v2`, `Sales-Manager-v1` |
| AI | OFF: `ai_enabled=false`, OpenRouter node disabled |
| Persistence today | Google Sheets |
| Execution truth | n8n workflows and their credentials/config |

Google Sheets are the current operational persistence. They are not the preferred target architecture for new successors; see [DB-FIRST-SUCCESSOR-BLUEPRINT.md](../roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md).

## Textual Dataflow

```text
Gmail mailbox
  -> Operational.dev Gmail Fetch Leads (simple=false, full body)
  -> Parse Lead (capture full source before normalization)
  -> RAW workbook lead_raw_v2 (durable visible source)
  -> CLEAN workbook lead_clean_v2 (normalized operational lead)
  -> Telegram manager card
      -> ✅ Обработано / 🚫 Спам callbacks
          -> Admin.dev updates CLEAN lifecycle + events
      -> 📄 Исходная заявка callback
          -> Admin.dev reads RAW by lead_id and returns literal source

Admin.dev schedule
  -> CONFIG reminder settings + CLEAN pending candidates
  -> Telegram reminder notification
  -> no lifecycle mutation
```

## External Systems

- Gmail is the intake source for new lead messages.
- Google Sheets hold RAW, CLEAN, CONFIG, LEAD_EVENTS, ERRORS, and DEDUP_INDEX.
- Telegram is the manager-facing product surface.
- n8n credentials and workflow configuration hold external access; docs must never include secret values.
- MARS/Git store documentation and evidence only, not runtime state.

## Gmail Intake

Operational.dev fetches full Gmail messages with `simple=false`. The parser captures the full visible body before extracting fields. It prefers `text/plain`; if unavailable, it uses a structure-preserving HTML-to-text fallback. Snippets are not authoritative when a body exists.

## RAW And CLEAN

RAW is the durable visible intake source. CLEAN is the normalized operational lead used for card rendering, lifecycle, reminders, and dedupe. RAW must not be reconstructed from CLEAN, and CLEAN must not replace RAW in raw-source UX.

## Parser And Identity

The parser creates a stable lead identity and normalized fields from Gmail input while preserving the original visible source. `lead_id` is the cross-workflow identity used by cards, callbacks, RAW lookup, and events. Callback tokens must carry enough identity to resolve the intended lead without broad sheet reads.

## Telegram Product Surface

The production manager card exposes:

- `✅ Обработано`
- `🚫 Спам`
- `📄 Исходная заявка`

Processed and spam are lifecycle actions. Raw source is read-only and returns literal source text with minimal privacy/Telegram cleanup; IP is omitted.

## Lifecycle

Current lifecycle is intentionally small: pending/actionable, processed, spam, test, and archive/legacy exclusions. Reminders and raw-source views do not mutate lifecycle.

## Dedupe And Retry

Operational.dev keeps dedupe and delivery guards through DEDUP_INDEX, duplicate classification, Telegram result gates, attempt stamping, and finalization. Re-delivery may resend or update product messages; it must not re-ingest the same Gmail message as a new lead.

## Raw Callback And Legacy Fallback

Current raw callback reads filtered RAW by `lead_id`, not a broad RAW sheet scan. For legacy records with lossy stored source, Admin.dev may use a READ-only Gmail fallback by `source_message_id`; it must not replay ingestion, mutate Gmail state, or rewrite lifecycle.

## Reminders

Reminders are enabled Mon-Fri at 10:00 Europe/Moscow. They include all still-actionable real pending leads; Monday includes weekend backlog. They exclude spam, processed, tests, archive, and legacy non-production records. Reminder delivery is notification only. Natural Monday reminder acceptance remains **PENDING OBSERVATION**, not PASS.

## Admin Boundary

Admin.dev owns callbacks, reminders, admin commands, raw source display, events, and errors. It is an operator surface, not an automatic task processor or CRM.

## AI Boundary

AI is off in the stable baseline. `ai_enabled=false` and OpenRouter is disabled. Do not document AI extraction, scoring, routing, or generation as active production behavior.

## Secrets And Configuration

Docs may reference CONFIG keys and n8n credential names by role only. Never write token values, email credentials, Telegram bot tokens, API keys, or raw PII.

## Observability

Current evidence comes from baseline docs, stable evidence, n8n execution state, Sheets tabs, LEAD_EVENTS, ERRORS, Telegram behavior, and targeted acceptance reports. There is no separate MARS runtime telemetry product for this bot.

## Failure Modes

| Failure | Expected safe posture |
|---------|-----------------------|
| Gmail body fetched as snippet only | Stop and restore `simple=false`; snippets are lossy |
| RAW lookup too broad / 429 | Use filtered RAW-by-`lead_id` lookup |
| Sheets unavailable | Fail closed for writes; record/inspect ERRORS when available |
| Telegram callback repeated | Treat lifecycle actions idempotently |
| Raw callback unavailable | Do not reconstruct from CLEAN; use bounded READ-only legacy fallback if applicable |
| Reminder schedule missed | Investigate gate/config/timezone; do not mutate lifecycle to compensate |
| AI accidentally enabled | Disable; stable baseline is deterministic AI OFF |

