# Runtime Connection Patterns — Phase 1B-D0

**Status:** DECISION (not implemented)

## Matrix

| Pattern | Producer | Coupling | Secret owner | Dedupe owner | Scheduler owner | Blast radius | Verdict |
|---------|----------|----------|--------------|--------------|-----------------|--------------|---------|
| **R1** Exporter as producer | Local Client Ops exporter (+ future `push-webhook`) | Low — monitor unchanged | Exporter host ignored secrets | n8n Data Table (primary) + optional producer ledger | Future Client Ops task from clean checkout | Contained to Bridge webhook + Telegram | **PREFERRED** |
| **R2** Monitor posts directly | SITE-002 monitor script | High — mixes prod monitor with delivery secrets | Would force secrets into monitor runtime | Ambiguous | Existing monitor task (dirty-main risk) | Monitor failure ↔ delivery failure coupled | **Reject for first connection** |
| **R3** File/report pickup adapter | Dedicated pickup reading sanitized report/outbox | Medium — new component | Adapter host | Shared with R1 model | Adapter schedule | Medium; clear rollback of adapter only | **FALLBACK** |
| **R4** n8n pulls source | n8n Schedule + read Storage/API | High — n8n gains source-path authority | n8n credentials for source | Inside n8n | n8n schedule trigger | Large; crosses production access boundaries | **Defer / caution** — not first |

## R1 detail (PREFERRED)

```text
SITE-002 monitor/report (unchanged)
  → local exporter/adapter (sanitize + envelope)
  → authenticated Client Ops webhook
  → HTTP response
  → Telegram (Pattern B, after accept)
```

**Evidence supporting R1:** Phase 1A offline exporter exists; PROFILE_B_REQUIRED; design docs forbid n8n re-reading raw artifacts; secrets already modeled for exporter-side Header Auth.

**Required before R1 live POST:** durable dedupe (D1); `push-webhook` or narrow adapter POST capability; ignored endpoint profile; HITL temporary activation for tests.

## R3 fallback

Use when exporter POST remains blocked longer than needed, but a sanitized outbox file already exists. Pickup adapter owns secrets and POST; monitor and exporter normalize remain separate.

## R2 / R4 rejection notes

- **R2:** Contaminates production monitor with webhook secrets; complicates SITE-002 rollback; fights exporter security gate.
- **R4:** Current workflow is webhook-driven; Storage/production read from n8n not authorized; expands blast radius.

## Selected

- **Preferred first runtime-connection pattern:** **R1**
- **Fallback:** **R3**
- **Implementation in D0:** none
