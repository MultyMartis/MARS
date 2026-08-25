# Operational Runbooks

No procedure here requires writing secret values or raw PII into documentation.

## Confirm Current Production State

1. Open n8n at `n8n.ai-metacode.com`.
2. Confirm Operational.dev `xSnXPy8cEHoZw6xG` is active.
3. Confirm Admin.dev `wLrLp4WQHm1VJmxz` is active.
4. Confirm reference/legacy workflows remain inactive.
5. Confirm baseline docs still match observed runtime.

## Check AI Boundary

1. Inspect CONFIG key `ai_enabled`.
2. Confirm value is `false`.
3. Confirm OpenRouter node is disabled.
4. If enabled unexpectedly, disable and record incident evidence.

## Verify Gmail Intake

1. Confirm Gmail fetch node uses full body mode (`simple=false`).
2. Confirm parser captures source before normalization.
3. Confirm RAW receives full visible source.
4. Confirm CLEAN receives normalized operational fields.
5. Do not paste real message bodies into docs.

## Verify Telegram Card

1. Use a safe accepted test or controlled production observation.
2. Confirm card renders correctly.
3. Confirm buttons: `✅ Обработано`, `🚫 Спам`, `📄 Исходная заявка`.
4. Confirm no secret/debug data appears.

## Processed / Spam Callback Check

1. Resolve affected `lead_id`.
2. Confirm CLEAN row exists.
3. Trigger or inspect callback evidence.
4. Confirm lifecycle status changes once.
5. Confirm repeated callback is safe/idempotent.
6. Confirm LEAD_EVENTS records action.

## Raw Source Callback Check

1. Resolve `lead_id` from callback/card.
2. Read RAW by filtered `lead_id` lookup.
3. Confirm literal source response.
4. Confirm no lifecycle change.
5. For legacy lossy records, use READ-only Gmail fallback by `source_message_id` if eligible.

## Reminder Check

1. Confirm CONFIG:
   - `pending_reminders_enabled=true`
   - `pending_reminder_time=10:00`
   - `pending_reminder_timezone=Europe/Moscow`
2. Confirm Mon-Fri schedule gate.
3. Confirm candidate query includes still-actionable pending real leads.
4. Confirm exclusions: processed, spam, tests, archive/legacy.
5. Confirm reminder sends notification only.
6. Do not claim natural Monday PASS without observed evidence.

## Sheets 429 / Rate-Limit Response

1. Stop broad reads where possible.
2. Replace with filtered `lead_id` lookup for callbacks.
3. Preserve lifecycle state.
4. Record error evidence without raw PII.
5. Validate with a safe callback path.

## Telegram Delivery Failure

1. Check n8n execution error.
2. Check Telegram credential status by name/role only.
3. Check delivery attempt/finalization markers.
4. Re-deliver only when dedupe/delivery state proves safe.
5. Do not re-ingest Gmail to compensate for delivery failure.

## Stable Freeze Routine

1. Confirm active workflow IDs.
2. Confirm AI OFF.
3. Confirm persistence reality.
4. Confirm acceptance matrix.
5. Record known pending observations.
6. Link evidence folder.
7. Do not create tags, commits, or workflow copies unless explicitly chartered.

