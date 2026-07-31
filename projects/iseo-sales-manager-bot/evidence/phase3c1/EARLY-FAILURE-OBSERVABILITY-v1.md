# EARLY FAILURE OBSERVABILITY v1

## Stable stages recognized

`schedule_trigger`, `gmail_read`, `parse_lead`, `raw_write`, `config_read`, `deterministic_processing`, `dedupe_lookup`, `clean_write`, `telegram_send`, `gmail_labels`, `runtime_state`

## Empty poll

- Intake Gate routes `empty` → Update Runtime → Apply CONFIG
- Writes **`last_poll_success_at` only** (does not set lead success)

## Gmail read failure

- Gmail Fetch `onError=continueRegularOutput` + `alwaysOutputData`
- Intake Gate `error` → Error Handler → Append ERRORS → … → runtime last_error_*

## Admin visibility

- `/status` shows poll vs lead vs error timestamps separately (verified).
