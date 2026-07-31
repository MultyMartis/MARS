# CLEAN-LEAD-EXACTLY-ONCE-CLOSEOUT v1

**Phase:** 3D.2  
**Date:** 2026-08-01  
**Scope:** Accepted production lead «Тест Парсер 3.1»

## Verdict

**PASS — exactly-once confirmed**

## Matrix

| Stage | Attempts | Successful Business Result | Duplicate Delivery | Final State |
|-------|----------|----------------------------|--------------------|-------------|
| Gmail identity / parse | 1 | 1 | 0 | PARSED_v3.1 |
| Business process | 1 | 1 | 0 | new |
| Telegram delivery | 1 | 1 | 0 | DELIVERED_ONCE |
| Later poll windows | 49 | 0 | 0 | NO_RESEND_ACROSS_POLLS |
| Idempotent skip / reprocess | 0 | 0 | 0 | NO_LATER_RESEND |

## Observations (sanitized)

- Parser stamp on lead: `sm-parser-v3.1`
- Quality: ok / Данных достаточно
- Service: Audit
- OpenRouter runs on lead execution: **0**
- Automatic client replies: **0**
- Later Telegram sends for the same marker: **0**
- Poll windows after delivery (≥3 required): **49** observed, all without re-send

## Pre-polish note

Accepted card still contained tautological next-step wording at acceptance time; Phase 3D.2 replaced manager guidance without resending that card.

## Security

No Gmail IDs, Telegram IDs, phones, emails, or raw payloads in this evidence file.
