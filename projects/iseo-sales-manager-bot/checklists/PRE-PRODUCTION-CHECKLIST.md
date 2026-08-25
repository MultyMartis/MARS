# Pre-Production Checklist

- [ ] Product charter names runtime owner, manager audience, and non-goals.
- [ ] Active n8n host and workflow names/IDs are documented.
- [ ] Secrets are stored in credentials/config, not docs.
- [ ] AI state is explicitly defined; for stable baseline, AI is OFF.
- [ ] Full Gmail/body intake uses `simple=false` or equivalent full-source mode.
- [ ] RAW/source authority is captured before parsing.
- [ ] CLEAN normalized model is separate from RAW.
- [ ] Dedupe keys and unique identity are defined.
- [ ] Telegram card actions are documented.
- [ ] Raw-source action is read-only.
- [ ] Reminder candidate rules and timezone are documented.
- [ ] Reminder path has no lifecycle mutation.
- [ ] Events and errors are written without secrets or raw PII.
- [ ] Unauthorized Telegram users are denied safely.
- [ ] Acceptance fixtures avoid real PII.
- [ ] Rollback path is known before production activation.

