# Raw Source Acceptance Checklist

- [ ] Gmail/source fetch captures full visible body.
- [ ] RAW is written before parsing/normalization.
- [ ] Raw response preserves original wording.
- [ ] Raw response preserves line/paragraph structure as available.
- [ ] Raw response does not reconstruct fields from CLEAN.
- [ ] Raw response does not substitute the Telegram card.
- [ ] IP is omitted from Telegram raw UX.
- [ ] Minimal privacy/Telegram-safe cleanup is applied.
- [ ] Lookup is filtered by `lead_id`.
- [ ] Legacy Gmail fallback is READ-only by `source_message_id`.
- [ ] Raw click does not mutate RAW, CLEAN, Gmail, or lifecycle.
- [ ] Evidence avoids committing raw PII.

