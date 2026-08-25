# Incident Forensic Checklist

- [ ] Record incident time, timezone, and observed symptom.
- [ ] Identify whether issue is intake, RAW, CLEAN, Telegram, reminder, Admin, Sheets, or n8n runtime.
- [ ] Confirm active workflow IDs before changing anything.
- [ ] Preserve evidence without raw PII or secrets.
- [ ] Check CONFIG by key name.
- [ ] Check LEAD_EVENTS for affected `lead_id`.
- [ ] Check ERRORS for runtime failures.
- [ ] Check dedupe/delivery state before re-sending.
- [ ] Distinguish re-delivery from re-ingestion.
- [ ] Use filtered `lead_id` lookup, not broad RAW scans.
- [ ] Do not reconstruct RAW from CLEAN.
- [ ] Do not mutate lifecycle while investigating raw/reminder issues.
- [ ] If Gmail fallback is needed, keep it READ-only.
- [ ] Define safe action and rollback before applying a fix.
- [ ] Record validation after recovery.

