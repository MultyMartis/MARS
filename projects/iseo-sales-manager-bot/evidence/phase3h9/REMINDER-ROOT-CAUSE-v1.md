# REMINDER ROOT CAUSE v1

**Primary:** Google Sheets OAuth `invalid_grant` on `Read Reminder CONFIG` — ERROR_BEFORE_EVALUATION. No claims, no Telegram.

**Secondary:** Classifier treated string `json.error` as SHEETS_PERMANENT (msg empty), so last_error_class was wrong; 429 retry not applicable anyway.

Not: current-state selector error, recipient resolver failure, claim construction, premature last_window, 10:15 missing.
